"""Sección «Análisis de inversión»: medición tras los informes sin mirar al futuro, rentabilidades y puntos orientativos."""
from pathlib import Path

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest

from empresas import evaluar, reaccion_a_resultados, rentabilidades

FECHAS = pd.bdate_range("2024-01-01", periods=300, tz="UTC")


def test_la_reaccion_empieza_a_contar_despues_del_informe():
    """Un salto el mismo día del informe no debe contarse: solo lo que pasa desde el día siguiente."""
    precios = pd.Series(100.0, index=FECHAS)
    referencia = pd.Series(100.0, index=FECHAS)
    informe = FECHAS[100]
    precios[FECHAS >= informe] = 150.0  # salta un 50 % el propio día del informe y luego se queda plano
    resultados = pd.DataFrame({"estimado": [1.0], "real": [1.2], "sorpresa": [20.0]}, index=[informe])
    r = reaccion_a_resultados(precios, referencia, resultados)
    assert r["bate"]["casos"] == 1 and abs(r["bate"]["exceso_medio"]) < 1e-12

    precios2 = pd.Series(100.0, index=FECHAS)
    precios2[FECHAS > FECHAS[101]] = 110.0  # sube después de conocerse el resultado
    r2 = reaccion_a_resultados(precios2, referencia, resultados)
    assert np.isclose(r2["bate"]["exceso_medio"], 0.10)


def test_rentabilidades_frente_al_indice():
    precios = pd.Series(np.linspace(100, 200, len(FECHAS)), index=FECHAS)
    referencia = pd.Series(np.linspace(100, 110, len(FECHAS)), index=FECHAS)
    r = rentabilidades(precios, referencia)
    assert list(r["periodo"]) == ["1 año"]  # con poco más de un año de datos no se inventan 3 ni 5 años
    assert r["empresa"].iat[0] > r["sp500"].iat[0]


def test_puntos_orientativos_con_umbrales_fijos():
    precios = pd.Series(np.linspace(100, 120, len(FECHAS)), index=FECHAS)
    datos = {"ticker": "XYZ.HK", "info": {"revenueGrowth": 0.30, "profitMargins": -0.1, "trailingPE": 80,
                                          "debtToEquity": 300, "freeCashflow": 1e9},
             "precios": precios, "resultados": pd.DataFrame(columns=["estimado", "real", "sorpresa"]),
             "noticias": [], "errores": []}
    e = evaluar(datos, precios)
    texto = " ".join(e["fuertes"] + e["debiles"] + e["riesgos"])
    for esperado in ("ventas crecen rápido", "Pierde dinero", "Mucha deuda", "Muy cara", "Empresa china"):
        assert esperado in texto, esperado


def test_seccion_empresas_en_la_app(tmp_path, monkeypatch):
    monkeypatch.setenv("ANALISTA_DEMO", "1")
    monkeypatch.chdir(tmp_path)
    at = AppTest.from_file(str(Path(__file__).resolve().parent.parent / "app.py"), default_timeout=300).run()
    at.button_group[0].set_value("💼 Análisis de inversión").run()
    at.selectbox[1].select("TSMC (Taiwán) · fabrican los chips").run()
    at.button(key="analizar_empresa").click().run()
    assert not at.exception, [e.value for e in at.exception]
    at.selectbox[1].select("🔗 Ver la cadena completa").run()
    at.button(key="analizar_empresa").click().run()
    assert not at.exception
    eslabones, empresas = at.dataframe[0].value, at.dataframe[1].value
    assert len(eslabones) == 7 and len(empresas) == 22  # 6 eslabones + S&P 500; 22 empresas de IA
