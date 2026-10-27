"""Indicadores técnicos: medias, RSI, MACD, ATR, pivotes (techos/suelos) y Fibonacci."""
import numpy as np
import pandas as pd

NIVELES_FIBO = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]


def ema(serie: pd.Series, n: int) -> pd.Series:
    return serie.ewm(span=n, adjust=False).mean()


def rsi(cierre: pd.Series, n: int = 14) -> pd.Series:
    delta = cierre.diff()
    subida = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    bajada = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + subida / bajada.replace(0, np.nan))


def macd(cierre: pd.Series, rapida=12, lenta=26, senal=9):
    linea = ema(cierre, rapida) - ema(cierre, lenta)
    linea_senal = ema(linea, senal)
    return linea, linea_senal, linea - linea_senal


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    cierre_prev = df["Close"].shift(1)
    rango = pd.concat(
        [df["High"] - df["Low"], (df["High"] - cierre_prev).abs(), (df["Low"] - cierre_prev).abs()],
        axis=1,
    ).max(axis=1)
    return rango.ewm(alpha=1 / n, adjust=False).mean()


def pivotes(df: pd.DataFrame, k: int = 5):
    """Techos y suelos locales. Un pivote en la vela i solo se confirma en i + k
    (hacen falta k velas posteriores), así el backtest no mira al futuro.

    Devuelve dos listas de (índice_pivote, precio) para techos y suelos."""
    ventana = 2 * k + 1
    alto, bajo = df["High"], df["Low"]
    es_techo = alto == alto.rolling(ventana, center=True).max()
    es_suelo = bajo == bajo.rolling(ventana, center=True).min()
    techos = [(i, alto.iat[i]) for i in np.flatnonzero(es_techo.to_numpy())]
    suelos = [(i, bajo.iat[i]) for i in np.flatnonzero(es_suelo.to_numpy())]
    return techos, suelos


def niveles_fibonacci(maximo: float, minimo: float, impulso_alcista: bool) -> dict:
    """Niveles de retroceso. En impulso alcista se miden desde el máximo hacia abajo."""
    rango = maximo - minimo
    if impulso_alcista:
        return {nivel: maximo - nivel * rango for nivel in NIVELES_FIBO}
    return {nivel: minimo + nivel * rango for nivel in NIVELES_FIBO}
