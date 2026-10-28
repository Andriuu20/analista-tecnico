import numpy as np
import pandas as pd

from conftest import paseo_aleatorio
from estructura import calcular_estructura
from indicadores import atr, rsi


def test_rupturas_y_barridas_respetan_su_definicion():
    df = paseo_aleatorio(7, n=4000)
    sen, series, _ = calcular_estructura(df, atr(df), rsi(df["Close"]))
    c, h, l = df["Close"].to_numpy(), df["High"].to_numpy(), df["Low"].to_numpy()
    techo, suelo = series["ult_techo"], series["ult_suelo"]
    for t in np.flatnonzero((sen["bos"] == 1) | (sen["choch"] == 1)):
        assert c[t] > techo[t]
    for t in np.flatnonzero((sen["bos"] == -1) | (sen["choch"] == -1)):
        assert c[t] < suelo[t]
    for t in np.flatnonzero(sen["barrida"] == 1):
        assert l[t] < suelo[t] <= c[t]
    for t in np.flatnonzero(sen["barrida"] == -1):
        assert h[t] > techo[t] >= c[t]
    assert all((s != 0).sum() > 0 for s in sen.values()), "alguna estrategia de estructura nunca se activa"


def test_fvg_alcista_y_reaccion():
    # vela 20: hueco alcista (mínimo de la 22 por encima del máximo de la 20); la 30 vuelve al hueco y rebota
    n = 60
    o = np.full(n, 1.000); c = np.full(n, 1.000)
    o[21], c[21] = 1.000, 1.010
    o[22:], c[22:] = 1.010, 1.010
    h, l = np.maximum(o, c) + 0.0005, np.minimum(o, c) - 0.0005
    l[22] = 1.0075
    o[30], c[30], l[30], h[30] = 1.007, 1.0095, 1.004, 1.0098
    idx = pd.date_range("2025-01-01", periods=n, freq="15min", tz="UTC")
    df = pd.DataFrame({"Open": o, "High": h, "Low": l, "Close": c}, index=idx)
    sen, _, _ = calcular_estructura(df, atr(df), rsi(df["Close"]))
    assert sen["fvg"][30] == 1
