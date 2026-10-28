"""Motor de decisión: de las velas de un mercado a COMPRAR / VENDER / ESPERAR.

Lo usan la app (app.py), la simulación sobre el pasado (simulacion.py) y el laboratorio en directo
(laboratorio.py), para que los tres tomen exactamente las mismas decisiones."""
import numpy as np
import pandas as pd

from backtest import backtest
from datos import MINUTOS
from estrategias import ESTRATEGIAS, calcular
from noticias import en_ventana, monedas
from plan import COSTE_MAXIMO_R
from plan import evaluar as evaluar_plan
from senal import generar
from tendencia import CONTEXTOS, alinear, backtest_por_contexto, contextos, filtro, serie_tendencia

ZONA = "Europe/Madrid"
# temporalidades que se analizan solas; cada una se confirma con la tendencia de la siguiente
TEMPORALIDADES = ["5m", "15m", "1h", "4h", "1d"]
SUPERIOR = {"5m": "15m", "15m": "1h", "1h": "4h", "4h": "1d", "1d": None}
# preferencia de plazo -> (mínimo, máximo) en minutos de la operación
PLAZOS = {"Cualquiera": (0, 10**9), "Minutos": (0, 59), "Horas": (60, 1439), "Días": (1440, 10**9)}
MAX_VELAS = 8000


def hora_local(ts, formato="%d/%m %H:%M") -> str:
    return pd.Timestamp(ts).tz_convert(ZONA).strftime(formato)


def preparar(df: pd.DataFrame, coste: float):
    """Indicadores, señales, contexto y backtest de una temporalidad."""
    df = df.iloc[-MAX_VELAS:]
    if len(df) < 300:
        raise ValueError(f"solo hay {len(df)} velas; hacen falta al menos 300")
    ind, senales, contexto = calcular(df)
    bt = backtest(df["Close"].to_numpy(), senales, coste)
    return df, ind, senales, contexto, bt


def tendencia_superior(r: dict, codigo: str, por_tf: dict) -> np.ndarray:
    """Tendencia del plazo mayor conocida al cierre de cada vela (1 día usa la suya). Anota cuál se usó."""
    sup = por_tf.get(SUPERIOR[codigo])
    if sup and "error" not in sup:
        r["tf_tendencia"] = SUPERIOR[codigo]
        return alinear(r["df"].index, MINUTOS[codigo], sup["ind"], MINUTOS[SUPERIOR[codigo]])
    r["tf_tendencia"] = codigo
    return serie_tendencia(r["ind"])


def juzgar(r: dict, coste: float, codigo: str, tendencia: np.ndarray, vivo: pd.DataFrame | None) -> dict:
    """Señal de una temporalidad. Las estrategias que van en contra de la tendencia del plazo mayor se
    descartan, salvo que en este mercado el histórico muestre que eso no les ha funcionado peor."""
    senales = r["senales"]
    ctx = contextos(senales, tendencia)
    r["bt_ctx"] = backtest_por_contexto(r["df"]["Close"].to_numpy(), senales, ctx, coste)

    activas, descartadas = {}, []
    for k, s in senales.items():
        activas[k] = s
        if s[-1] and ctx[k][-1] == -1:
            descartar, a_contra, a_resto = filtro(r["bt_ctx"], k)
            if descartar:
                activas[k] = np.r_[s[:-1], 0]
                motivo = "va en contra de la tendencia"
                if not np.isnan(a_contra):
                    motivo += f" y aquí eso ha funcionado peor ({a_contra:.0%} frente a {a_resto:.0%})"
                descartadas.append({"estrategia": k, "descripcion": ESTRATEGIAS[k], "direccion": int(s[-1]),
                                    "valida": False, "motivo": motivo})
    senal = generar(activas, r["bt"], vivo, MINUTOS[codigo])
    senal["votos"] += descartadas
    for v in senal["votos"]:
        v["situacion"] = CONTEXTOS[int(ctx[v["estrategia"]][-1])]
    if descartadas and not senal["direccion"] and len(descartadas) == len(senal["votos"]):
        senal["motivo"] = "Las señales iban en contra de la tendencia del plazo mayor."
    if senal["direccion"]:
        senal["plan"] = evaluar_plan(r["df"], r["ind"], senales, senal["estrategias"], senal["direccion"], coste)
        if senal["plan"]["coste_r"] > COSTE_MAXIMO_R:
            senal.update(accion="ESPERAR", direccion=0,
                         motivo=f"El movimiento típico es demasiado pequeño: el coste de operar se comería el "
                                f"{senal['plan']['coste_r']:.0%} del riesgo.")
    senal["contexto"] = int(np.sign(senal["direccion"] * tendencia[-1])) if senal["direccion"] else None
    return senal


def filtrar_noticias(senal: dict, r: dict, codigo: str, cfg: dict, eventos, mon: set, ahora: pd.Timestamp) -> dict:
    """En forex y oro no se opera si una noticia de alto impacto cae antes del vencimiento (plazos < 1 día)."""
    if not senal["direccion"]:
        return senal
    vence = r["df"].index[-1] + pd.Timedelta(minutes=MINUTOS[codigo] * (senal["horizonte"] + 1))
    senal["noticias"] = en_ventana(eventos, mon, ahora, vence)
    if senal["noticias"] and cfg["fuente"] != "binance" and MINUTOS[codigo] * senal["horizonte"] < 1440:
        e = senal["noticias"][0]
        return {**senal, "accion": "ESPERAR", "direccion": 0,
                "motivo": f"Noticia de alto impacto antes del vencimiento ({e['moneda']}: {e['titulo']}, "
                          f"a las {hora_local(e['hora'], '%H:%M')}): mejor no operar."}
    return senal


def analizar_mercado(nombre: str, cfg: dict, plazo: str | tuple, cargar, vivo_de, eventos) -> dict:
    """Analiza todas las temporalidades y se queda con la mejor señal confirmada del plazo pedido.

    cargar(codigo) -> (df, origen, ind, senales, contexto, bt); vivo_de(codigo) -> resultados reales."""
    por_tf = {}
    for codigo in TEMPORALIDADES:
        try:
            df, origen, ind, senales, contexto, bt = cargar(codigo)
        except Exception as e:
            por_tf[codigo] = {"error": str(e)}
            continue
        por_tf[codigo] = {"df": df, "origen": origen, "ind": ind, "senales": senales, "contexto": contexto, "bt": bt}

    mon, ahora = monedas(nombre, cfg), pd.Timestamp.now(tz="UTC")
    for codigo, r in por_tf.items():
        if "error" not in r:
            senal = juzgar(r, cfg["coste"], codigo, tendencia_superior(r, codigo, por_tf), vivo_de(codigo))
            r["senal"] = filtrar_noticias(senal, r, codigo, cfg, eventos, mon, ahora)

    validos = [c for c, r in por_tf.items() if "error" not in r]
    if not validos:
        raise ValueError(next(iter(por_tf.values()))["error"])
    minimo, maximo = PLAZOS[plazo] if isinstance(plazo, str) else plazo  # o (mín, máx) en minutos
    con_senal = [c for c in validos if por_tf[c]["senal"]["direccion"]
                 and minimo <= por_tf[c]["senal"]["horizonte"] * MINUTOS[c] <= maximo]
    mejor = max(con_senal, key=lambda c: por_tf[c]["senal"]["confianza"]) if con_senal else None
    return {"nombre": nombre, "cfg": cfg, "por_tf": por_tf, "mejor": mejor,
            "principal": mejor or ("15m" if "15m" in validos else validos[0]),
            "noticias": en_ventana(eventos, mon, ahora, ahora + pd.Timedelta(hours=24)),
            "calendario_ok": eventos is not None}
