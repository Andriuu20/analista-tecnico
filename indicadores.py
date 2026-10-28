"""Indicadores técnicos: medias, RSI, MACD, ATR, Bollinger, estocástico, ADX, SuperTrend,
pivotes (techos/suelos) y Fibonacci. Una sola implementación de cada indicador."""
import numpy as np
import pandas as pd

NIVELES_FIBO = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
EXTENSIONES_FIBO = [1.272, 1.618]


def ema(serie: pd.Series, n: int) -> pd.Series:
    return serie.ewm(span=n, adjust=False).mean()


def sma(serie: pd.Series, n: int) -> pd.Series:
    return serie.rolling(n, min_periods=n).mean()


def rsi(cierre: pd.Series, n: int = 14) -> pd.Series:
    delta = cierre.diff()
    subida = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    bajada = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    valor = 100 - 100 / (1 + subida / bajada.replace(0, np.nan))
    # sin bajadas el RSI es 100 (antes quedaba vacío y la estrategia no podía activarse)
    return valor.where(bajada > 0, np.where(subida > 0, 100.0, 50.0))


def macd(cierre: pd.Series, rapida=12, lenta=26, senal=9):
    linea = ema(cierre, rapida) - ema(cierre, lenta)
    linea_senal = ema(linea, senal)
    return linea, linea_senal, linea - linea_senal


def rango_verdadero(df: pd.DataFrame) -> pd.Series:
    cierre_prev = df["Close"].shift(1)
    return pd.concat(
        [df["High"] - df["Low"], (df["High"] - cierre_prev).abs(), (df["Low"] - cierre_prev).abs()],
        axis=1,
    ).max(axis=1)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return rango_verdadero(df).ewm(alpha=1 / n, adjust=False).mean()


def bollinger(cierre: pd.Series, n: int = 20, k: float = 2.0):
    """(banda superior, media, banda inferior)."""
    media = sma(cierre, n)
    desv = cierre.rolling(n, min_periods=n).std(ddof=0)
    return media + k * desv, media, media - k * desv


def estocastico(df: pd.DataFrame, n: int = 14, suavizado: int = 3, d: int = 3):
    """Estocástico lento: (%K, %D), entre 0 y 100."""
    minimo = df["Low"].rolling(n, min_periods=n).min()
    maximo = df["High"].rolling(n, min_periods=n).max()
    k_rapido = 100 * (df["Close"] - minimo) / (maximo - minimo).replace(0, np.nan)
    k = k_rapido.rolling(suavizado).mean()
    return k, k.rolling(d).mean()


def adx(df: pd.DataFrame, n: int = 14):
    """ADX de Wilder: (ADX, +DI, -DI). ADX < 20 suele indicar mercado lateral; > 25, tendencia."""
    subida = df["High"].diff()
    bajada = -df["Low"].diff()
    dm_mas = pd.Series(np.where((subida > bajada) & (subida > 0), subida, 0.0), index=df.index)
    dm_menos = pd.Series(np.where((bajada > subida) & (bajada > 0), bajada, 0.0), index=df.index)
    media_tr = rango_verdadero(df).ewm(alpha=1 / n, adjust=False).mean().replace(0, np.nan)
    di_mas = 100 * dm_mas.ewm(alpha=1 / n, adjust=False).mean() / media_tr
    di_menos = 100 * dm_menos.ewm(alpha=1 / n, adjust=False).mean() / media_tr
    dx = 100 * (di_mas - di_menos).abs() / (di_mas + di_menos).replace(0, np.nan)
    return dx.ewm(alpha=1 / n, adjust=False).mean(), di_mas, di_menos


def supertrend(df: pd.DataFrame, n: int = 10, mult: float = 3.0):
    """(línea, dirección +1/-1). Bandas ATR alrededor de (máximo+mínimo)/2 que solo se estrechan."""
    h, l, c = (df[x].to_numpy() for x in ("High", "Low", "Close"))
    a = atr(df, n).to_numpy()
    medio = (h + l) / 2
    banda_sup, banda_inf = medio + mult * a, medio - mult * a
    sup, inf = banda_sup.copy(), banda_inf.copy()
    direccion = np.ones(len(c), dtype=int)
    for i in range(1, len(c)):
        sup[i] = banda_sup[i] if banda_sup[i] < sup[i - 1] or c[i - 1] > sup[i - 1] else sup[i - 1]
        inf[i] = banda_inf[i] if banda_inf[i] > inf[i - 1] or c[i - 1] < inf[i - 1] else inf[i - 1]
        if direccion[i - 1] == 1:
            direccion[i] = -1 if c[i] < inf[i] else 1
        else:
            direccion[i] = 1 if c[i] > sup[i] else -1
    linea = np.where(direccion == 1, inf, sup)
    return pd.Series(linea, index=df.index), pd.Series(direccion, index=df.index)


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


def extensiones_fibonacci(maximo: float, minimo: float, impulso_alcista: bool) -> dict:
    """Objetivos más allá del impulso (127,2 % y 161,8 %), en la dirección del impulso."""
    rango = maximo - minimo
    if impulso_alcista:
        return {nivel: minimo + nivel * rango for nivel in EXTENSIONES_FIBO}
    return {nivel: maximo - nivel * rango for nivel in EXTENSIONES_FIBO}
