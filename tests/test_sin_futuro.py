"""Ninguna estrategia ni indicador puede usar velas futuras: el resultado en la vela k debe ser el mismo
calculando con todo el histórico que cortando los datos justo después de k."""
import numpy as np
import pandas as pd

from conftest import paseo_aleatorio
from estrategias import calcular
from tendencia import alinear


def test_estrategias_e_indicadores_no_miran_al_futuro():
    df = paseo_aleatorio(3, n=900)
    ind_completo, completo, _ = calcular(df)
    for k in range(250, len(df), 13):
        ind_parcial, parcial, _ = calcular(df.iloc[: k + 1])
        for nombre in completo:
            assert parcial[nombre][-1] == completo[nombre][k], f"{nombre} mira al futuro en la vela {k}"
        for col in ("estructura", "ult_techo", "ult_suelo", "supertrend", "adx", "rsi"):
            a, b = ind_parcial[col].iat[-1], ind_completo[col].iat[k]
            assert (pd.isna(a) and pd.isna(b)) or np.isclose(a, b), f"{col} mira al futuro en la vela {k}"


def test_tendencia_superior_solo_usa_velas_cerradas():
    df = paseo_aleatorio(5, n=4000)
    hora = lambda d: d.resample("1h").agg({"Open": "first", "High": "max", "Low": "min", "Close": "last"}).dropna()
    ind_sup, _, _ = calcular(hora(df))
    completo = alinear(df.index, 15, ind_sup, 60)
    for k in range(2500, len(df), 151):
        corte = df.index[k] + pd.Timedelta(minutes=15)
        sup = hora(df.iloc[: k + 1])
        sup = sup[sup.index + pd.Timedelta(minutes=60) <= corte]
        ind_k, _, _ = calcular(sup)
        assert alinear(df.index[: k + 1], 15, ind_k, 60)[-1] == completo[k]
