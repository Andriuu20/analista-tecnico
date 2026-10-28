import numpy as np
import pandas as pd

from indicadores import adx, atr, bollinger, estocastico, extensiones_fibonacci, niveles_fibonacci, rsi, sma, supertrend


def test_sma_es_la_media_movil(velas):
    c = velas["Close"]
    assert np.allclose(sma(c, 50).dropna(), c.rolling(50).mean().dropna())


def test_rsi_vale_100_si_solo_sube_y_esta_entre_0_y_100(velas):
    subida = pd.Series(np.linspace(1, 2, 50))
    assert (rsi(subida).iloc[1:] == 100).all()
    r = rsi(velas["Close"]).dropna()
    assert r.between(0, 100).all()


def test_bollinger_simetricas_y_ordenadas(velas):
    sup, media, inf = bollinger(velas["Close"])
    ok = sup.notna()
    assert np.allclose((sup - media)[ok], (media - inf)[ok])
    assert (sup[ok] >= inf[ok]).all()


def test_estocastico_y_adx_en_rango(velas):
    k, d = estocastico(velas)
    assert k.dropna().between(0, 100).all() and d.dropna().between(0, 100).all()
    valor, di_mas, di_menos = adx(velas)
    assert valor.dropna().between(0, 100).all()
    assert (di_mas.dropna() >= 0).all() and (di_menos.dropna() >= 0).all()


def test_supertrend_sigue_una_tendencia_clara():
    n = 300
    precio = np.r_[np.linspace(1.0, 1.5, n // 2), np.linspace(1.5, 1.0, n // 2)]
    df = pd.DataFrame({"Open": precio, "High": precio * 1.001, "Low": precio * 0.999, "Close": precio})
    _, direccion = supertrend(df)
    assert direccion.iloc[100] == 1 and direccion.iloc[-1] == -1


def test_atr_positivo(velas):
    assert (atr(velas).iloc[1:] > 0).all()


def test_fibonacci_retrocesos_y_extensiones():
    niveles = niveles_fibonacci(2.0, 1.0, impulso_alcista=True)
    assert niveles[0.5] == 1.5 and niveles[0.0] == 2.0 and niveles[1.0] == 1.0
    ext = extensiones_fibonacci(2.0, 1.0, impulso_alcista=True)
    assert np.isclose(ext[1.618], 2.618)
    ext_baja = extensiones_fibonacci(2.0, 1.0, impulso_alcista=False)
    assert np.isclose(ext_baja[1.272], 0.728)
