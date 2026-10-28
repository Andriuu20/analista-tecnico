"""Laboratorio en directo: lo ejecuta GitHub cada 30 minutos (.github/workflows/laboratorio.yml).

1. Comprueba las señales ya vencidas (¿el precio fue a favor? ¿se tocó antes el SL o el TP?).
2. Analiza los 14 mercados con el mismo motor que la app y guarda todas las señales con plazos de
   30 min a 4 h (de cualquier temporalidad, marcando cuál habría elegido la app).
3. Exporta los resultados a CSV en el mismo formato que la simulación, para el informe de errores.

No opera ni envía órdenes a ningún broker: solo apunta y comprueba.

Uso: python laboratorio.py [--carpeta resultados]"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from datos import ACTIVOS, MINUTOS, descargar
from motor import analizar_mercado, preparar
from noticias import descargar_calendario
from plan import simular
from registro import anadir, nueva_entrada, resolver
from simulacion import PLAZO_MAX, PLAZO_MIN, rasgos


def resolver_sl_tp(entradas: list[dict], cargar) -> None:
    """Resultado en R del plan SL/TP cuando ya hay suficientes velas después de la entrada."""
    for e in entradas:
        if e.get("resultado_r") is not None or e.get("sl") is None:
            continue
        try:
            df, _ = cargar(e["fuente"], e["simbolo"], e["intervalo"])
        except Exception:
            continue
        vela = pd.Timestamp(e["vela"])
        if vela not in df.index:
            continue
        i = df.index.get_loc(vela)
        h, l, c = (df[x].to_numpy() for x in ("High", "Low", "Close"))
        riesgo = abs(e["precio_entrada"] - e["sl"])
        res, dur = simular(h, l, c, [i], [e["direccion"]], [riesgo], e["plan_r"], ACTIVOS.get(e["activo"], {}).get("coste", 0))
        if not np.isnan(res[0]):
            e["resultado_r"], e["duracion_velas"] = round(float(res[0]), 3), float(dur[0])


def exportar_csv(entradas: list[dict], ruta: Path) -> None:
    filas = []
    for e in entradas:
        if e["resultado"] not in ("acierto", "fallo"):
            continue
        mov = (e["precio_salida"] - e["precio_entrada"]) / e["precio_entrada"] * e["direccion"]
        filas.append({
            "mercado": e["activo"], "temporalidad": e["intervalo"], "vela": e["vela"], "accion": e["accion"],
            "direccion": e["direccion"], "horizonte": e["horizonte"],
            "plazo_min": e["horizonte"] * MINUTOS[e["intervalo"]], "confianza": e["confianza"],
            "estrategias": "+".join(e["estrategias"]), "precio": e["precio_entrada"],
            "precio_final": e["precio_salida"], "acierto": e["resultado"] == "acierto",
            "movimiento_pct": round(mov * 100, 4), "resultado_r": e.get("resultado_r"),
            "duracion_velas": e.get("duracion_velas"), "plan_r": e.get("plan_r"),
            "plan_esperanza": e.get("plan_esperanza"), "coste_r": e.get("coste_r"),
            "elegida": e.get("elegida"), **e.get("rasgos", {}),
        })
    pd.DataFrame(filas).to_csv(ruta, index=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--carpeta", default="resultados")
    args = parser.parse_args()
    carpeta = Path(args.carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = carpeta / "vivo.json"
    entradas = json.loads(ruta.read_text()) if ruta.exists() else []

    cache = {}

    def cargar(fuente, simbolo, codigo):
        if (fuente, simbolo, codigo) not in cache:
            cache[(fuente, simbolo, codigo)] = descargar(fuente, simbolo, codigo)
        return cache[(fuente, simbolo, codigo)]

    resolver(entradas, cargar)
    resolver_sl_tp(entradas, cargar)

    eventos, nuevas, fallos = descargar_calendario(), 0, []
    for nombre, cfg in ACTIVOS.items():
        def cargar_tf(codigo, cfg=cfg):
            df, origen = cargar(cfg["fuente"], cfg["simbolo"], codigo)
            df, ind, senales, contexto, bt = preparar(df, cfg["coste"])
            return df, origen, ind, senales, contexto, bt
        try:
            a = analizar_mercado(nombre, cfg, (PLAZO_MIN, PLAZO_MAX), cargar_tf, lambda codigo: None, eventos)
        except Exception as e:
            fallos.append(f"{nombre}: {e}")
            continue
        for codigo, r in a["por_tf"].items():
            s = r.get("senal")
            if not s or not s["direccion"] or not PLAZO_MIN <= s["horizonte"] * MINUTOS[codigo] <= PLAZO_MAX:
                continue
            df = r["df"]
            entrada = nueva_entrada(nombre, cfg, codigo, df.index[-1], float(df["Close"].iat[-1]), s)
            entrada.update(elegida=codigo == a["mejor"], plan_r=s["plan"]["r"],
                           plan_esperanza=round(float(s["plan"]["esperanza"]), 3),
                           coste_r=round(float(s["plan"]["coste_r"]), 3), resultado_r=None,
                           rasgos=rasgos(df, r["ind"], len(df) - 1, s))
            nuevas += anadir(entradas, entrada)

    ruta.write_text(json.dumps(entradas, ensure_ascii=False, indent=1, default=str))
    exportar_csv(entradas, carpeta / "vivo.csv")
    resueltas = sum(e["resultado"] in ("acierto", "fallo") for e in entradas)
    print(f"Señales nuevas: {nuevas} · comprobadas: {resueltas} · pendientes: "
          f"{sum(e['resultado'] == 'pendiente' for e in entradas)}")
    for f in fallos:
        print("AVISO:", f, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
