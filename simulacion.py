"""Simulación sobre el pasado reciente: la app «revive» las últimas semanas vela a vela y da sus
señales como si fuera en directo, para tener muchos resultados comprobados sin esperar.

Garantías:
- En cada vela, el motor (motor.juzgar, el mismo que usa la app) solo ve datos hasta esa vela: las
  señales no miran al futuro (test de truncado) y el backtest con el que decide se recalcula recortado.
- No se abre otra operación en el mismo mercado y temporalidad hasta que vence la anterior, para que
  una misma situación no cuente muchas veces.
- Solo plazos de 30 min a 4 h. El filtro de noticias no se aplica (no hay calendario histórico).

Uso: python simulacion.py [--salida resultados/simulacion.csv] [--mercados "EUR/USD,BTC/USDT"]"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

from backtest import backtest
from datos import ACTIVOS, MINUTOS, descargar
from motor import SUPERIOR, juzgar, preparar
from plan import simular
from tendencia import alinear, serie_tendencia

PLAZO_MIN, PLAZO_MAX = 30, 240  # minutos
TEMPORALIDADES_SIM = ["5m", "15m", "1h", "4h"]
VELAS_SIMULADAS = {"5m": 7000, "15m": 4600, "1h": 7000, "4h": 3400}  # hasta ~3 meses (5m) - 2 años (4h)
HISTORIA_MINIMA = 1000  # velas previas que necesita el motor para decidir


def rasgos(df: pd.DataFrame, ind: pd.DataFrame, t: int, senal: dict) -> dict:
    """Situación del mercado en la vela t, para analizar después dónde falla la app."""
    atr_v = ind["atr"].to_numpy()
    techo, suelo, cierre = ind["ult_techo"].iat[t], ind["ult_suelo"].iat[t], df["Close"].iat[t]
    zona = np.nan
    if techo > suelo:
        zona = "premium" if (cierre - suelo) / (techo - suelo) > 0.5 else "discount"
    return {
        "adx": round(float(ind["adx"].iat[t]), 1),
        "volatilidad_pct": round(float((atr_v[max(0, t - 500):t] < atr_v[t]).mean()), 2),
        "zona": zona,
        "estructura": int(ind["estructura"].iat[t]),
        "rsi": round(float(ind["rsi"].iat[t]), 1),
        "tendencia": senal.get("contexto"),
    }


def resultado_sl_tp(df: pd.DataFrame, t: int, senal: dict, coste: float) -> tuple[float, float]:
    """(resultado en R tras costes, duración en velas) del plan SL/TP desde la vela t; NaN si no hay datos."""
    plan = senal.get("plan")
    if not plan:
        return np.nan, np.nan
    riesgo = abs(plan["entrada"] - plan["sl"])
    h, l, c = (df[x].to_numpy() for x in ("High", "Low", "Close"))
    res, dur = simular(h, l, c, [t], [senal["direccion"]], [riesgo], plan["r"], coste)
    return float(res[0]), float(dur[0])


def simular_mercado(nombre: str, cfg: dict, datos: dict, diagnostico: dict | None = None) -> list[dict]:
    """Señales simuladas del mercado. Si se pasa `diagnostico`, anota cuántas velas se evaluaron y por qué se
    descartó cada posible señal (para encontrar errores sin tener que leer los registros de GitHub)."""
    diag = diagnostico if diagnostico is not None else {}
    prep = {}
    for codigo, df in datos.items():
        try:
            df, ind, senales, _, _ = preparar(df, cfg["coste"])
        except ValueError as e:  # pocas velas en esa temporalidad: se simula el resto
            diag[f"{codigo} sin datos suficientes"] = str(e)
            continue
        prep[codigo] = {"df": df, "ind": ind, "senales": senales}

    filas = []
    for codigo in TEMPORALIDADES_SIM:
        if codigo not in prep:
            continue
        p = prep[codigo]
        df, ind, senales = p["df"], p["ind"], p["senales"]
        cierre, n, minutos = df["Close"].to_numpy(), len(df), MINUTOS[codigo]
        sup = SUPERIOR[codigo]
        tendencia = (alinear(df.index, minutos, prep[sup]["ind"], MINUTOS[sup]) if sup in prep
                     else serie_tendencia(ind))
        activa = np.any([s != 0 for s in senales.values()], axis=0)
        libre_desde = 0
        cuenta = diag.setdefault(codigo, {"velas": n, "evaluadas": 0, "con estrategia activa": 0,
                                          "ESPERAR": 0, "fuera de 30 min-4 h": 0, "señales": 0, "motivos ESPERAR": {}})
        for t in range(max(n - VELAS_SIMULADAS[codigo], HISTORIA_MINIMA), n - 1):
            cuenta["evaluadas"] += 1
            if t < libre_desde or not activa[t]:
                continue
            cuenta["con estrategia activa"] += 1
            r = {"df": df.iloc[: t + 1], "ind": ind.iloc[: t + 1],
                 "senales": {k: v[: t + 1] for k, v in senales.items()}}
            r["bt"] = backtest(cierre[: t + 1], r["senales"], cfg["coste"])
            senal = juzgar(r, cfg["coste"], codigo, tendencia[: t + 1], None)
            if not senal["direccion"]:
                cuenta["ESPERAR"] += 1
                motivo = senal["motivo"].split(":")[0].split("(")[0].strip()[:70]
                cuenta["motivos ESPERAR"][motivo] = cuenta["motivos ESPERAR"].get(motivo, 0) + 1
                continue
            h = senal["horizonte"]
            if not PLAZO_MIN <= h * minutos <= PLAZO_MAX or t + h >= n:
                cuenta["fuera de 30 min-4 h"] += 1
                continue
            cuenta["señales"] += 1
            d = senal["direccion"]
            movimiento = (cierre[t + h] - cierre[t]) / cierre[t] * d
            res_r, dur = resultado_sl_tp(df, t, senal, cfg["coste"])
            filas.append({
                "mercado": nombre, "temporalidad": codigo, "vela": df.index[t].isoformat(),
                "accion": senal["accion"], "direccion": d, "horizonte": h, "plazo_min": h * minutos,
                "confianza": round(senal["confianza"], 4), "estrategias": "+".join(senal["estrategias"]),
                "precio": cierre[t], "precio_final": cierre[t + h],
                "acierto": bool(movimiento > 0), "movimiento_pct": round(movimiento * 100, 4),
                "resultado_r": round(res_r, 3), "duracion_velas": dur,
                "plan_r": senal["plan"]["r"], "plan_esperanza": round(senal["plan"]["esperanza"], 3),
                "coste_r": round(senal["plan"]["coste_r"], 3),
                **rasgos(df, ind, t, senal),
            })
            libre_desde = t + h  # no solapar operaciones en el mismo mercado y temporalidad
    return filas


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--salida", default="resultados/simulacion.csv")
    parser.add_argument("--mercados", default=",".join(ACTIVOS))
    args = parser.parse_args()

    filas, diagnosticos = [], {}
    for nombre in [m.strip() for m in args.mercados.split(",") if m.strip()]:
        cfg, inicio = ACTIVOS[nombre], time.time()
        diag = diagnosticos.setdefault(nombre, {})
        datos = {}
        for codigo in [*TEMPORALIDADES_SIM, "1d"]:
            try:
                datos[codigo], origen = descargar(cfg["fuente"], cfg["simbolo"], codigo)
                diag[f"descarga {codigo}"] = f"{len(datos[codigo])} velas de {origen}"
            except Exception as e:
                diag[f"descarga {codigo}"] = f"ERROR: {type(e).__name__}: {e}"
        try:
            nuevas = simular_mercado(nombre, cfg, datos, diag)
        except Exception as e:
            diag["ERROR en la simulación"] = f"{type(e).__name__}: {e}"
            nuevas = []
        filas += nuevas
        print(f"{nombre}: {len(nuevas)} señales simuladas ({time.time() - inicio:.0f} s)", flush=True)

    salida = Path(args.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(filas).to_csv(salida, index=False)
    salida.with_suffix(".diag.json").write_text(json.dumps(diagnosticos, ensure_ascii=False, indent=1))
    print(f"Total: {len(filas)} señales -> {salida}")
    return 0  # sin señales no es un error: el diagnóstico explica por qué


if __name__ == "__main__":
    sys.exit(main())
