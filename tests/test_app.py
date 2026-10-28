"""La app arranca y analiza sin errores con datos de prueba (sin conexión)."""
import os
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def test_app_analiza_sin_errores(tmp_path, monkeypatch):
    monkeypatch.setenv("ANALISTA_DEMO", "1")
    monkeypatch.chdir(tmp_path)
    at = AppTest.from_file(APP, default_timeout=300).run()
    for mercado in ("EUR/USD", "BTC/USDT", "🔍 Buscar en todos"):
        at.selectbox[0].select(mercado).run()
        at.button[0].click().run()
        assert not at.exception, [e.value for e in at.exception]
