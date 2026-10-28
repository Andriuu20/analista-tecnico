"""Filtro de tendencia medido, no supuesto.

Cada señal se clasifica según la tendencia de la temporalidad superior en ese momento:
a favor (+1), en contra (-1) o sin tendencia clara (0). El filtro (descartar las señales en
contra) está activo por defecto, y para cada mercado y estrategia solo se desactiva si en la
parte antigua del histórico las señales en contra no funcionaron peor que el resto.

No se juzga cada señal solo con las cifras de su situación: trocear el histórico deja pocas
muestras y, con datos aleatorios, más que duplicaba las señales falsas."""
import numpy as np
import pandas as pd

from backtest import backtest

CONTEXTOS = {1: "a favor de la tendencia", -1: "en contra de la tendencia", 0: "sin tendencia clara"}
_CALENTAMIENTO = 210  # la EMA 200 necesita historia para ser fiable
MIN_CONTRA = 30  # señales en contra necesarias para poder desactivar el filtro


def serie_tendencia(ind: pd.DataFrame) -> np.ndarray:
    """+1 alcista (EMA 50 > EMA 200 y subiendo), -1 bajista, 0 lateral; por vela."""
    e50, e200 = ind["ema50"], ind["ema200"]
    pendiente = e50 - e50.shift(9)
    t = np.where((e50 > e200) & (pendiente > 0), 1, np.where((e50 < e200) & (pendiente < 0), -1, 0))
    t[:_CALENTAMIENTO] = 0
    return t


def alinear(indice_bajo: pd.DatetimeIndex, minutos_bajo: int, ind_sup: pd.DataFrame, minutos_sup: int) -> np.ndarray:
    """Tendencia superior que se conocía al cerrar cada vela inferior (solo velas superiores ya cerradas)."""
    t = serie_tendencia(ind_sup)
    disponible = ind_sup.index + pd.Timedelta(minutes=minutos_sup)
    cierre_bajo = indice_bajo + pd.Timedelta(minutes=minutos_bajo)
    pos = disponible.searchsorted(cierre_bajo, side="right") - 1
    return np.where(pos >= 0, t[np.clip(pos, 0, None)], 0)


def contextos(senales: dict, tendencia_sup: np.ndarray) -> dict:
    """Situación de cada señal: +1 a favor, -1 en contra, 0 sin tendencia (0 también donde no hay señal)."""
    return {k: np.sign(s * tendencia_sup) for k, s in senales.items()}


def backtest_por_contexto(cierre: np.ndarray, senales: dict, ctx: dict, coste: float) -> dict:
    return {c: backtest(cierre, {k: s * (ctx[k] == c) for k, s in senales.items()}, coste) for c in CONTEXTOS}


def filtro(por_contexto: dict, estrategia: str) -> tuple[bool, float, float]:
    """(¿descartar sus señales en contra?, acierto en contra, acierto del resto), con la parte antigua."""
    filas = {c: t[t["estrategia"] == estrategia] for c, t in por_contexto.items()}
    n_contra, a_contra = filas[-1]["senales_ant"].sum(), filas[-1]["aciertos_ant"].sum()
    n_resto = filas[1]["senales_ant"].sum() + filas[0]["senales_ant"].sum()
    a_resto = filas[1]["aciertos_ant"].sum() + filas[0]["aciertos_ant"].sum()
    acierto_contra = a_contra / n_contra if n_contra else np.nan
    acierto_resto = a_resto / n_resto if n_resto else np.nan
    if n_contra < MIN_CONTRA or not n_resto:
        return True, acierto_contra, acierto_resto
    return bool(acierto_contra < acierto_resto), acierto_contra, acierto_resto


def resumen(por_contexto: dict) -> pd.DataFrame:
    """Acierto medio de todas las estrategias y plazos en cada situación, para mostrarlo."""
    filas = []
    for c, nombre in CONTEXTOS.items():
        bt = por_contexto[c]
        total = bt["senales"].sum()
        filas.append({"Situación": nombre.capitalize(),
                      "Señales": int(bt.loc[bt["horizonte"] == bt["horizonte"].min(), "senales"].sum()),
                      "Acierto": bt["aciertos"].sum() / total if total else np.nan})
    return pd.DataFrame(filas)
