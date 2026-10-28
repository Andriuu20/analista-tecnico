"""La simulación sobre el pasado decide igual que la app en directo y respeta sus reglas."""
import numpy as np
import pandas as pd

import simulacion
from backtest import backtest
from conftest import paseo_aleatorio
from datos import ACTIVOS, MINUTOS
from motor import juzgar, preparar
from tendencia import alinear


def _datos():
    base = paseo_aleatorio(21, n=6000, minutos=15)
    agregar = lambda regla: base.resample(regla).agg(
        {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"}).dropna()
    return {"15m": base, "1h": agregar("1h"), "4h": agregar("4h"), "1d": agregar("1D")}


def test_simulacion_respeta_plazos_y_no_solapa(monkeypatch):
    monkeypatch.setattr(simulacion, "VELAS_SIMULADAS", {"5m": 0, "15m": 900, "1h": 200, "4h": 0})
    filas = simulacion.simular_mercado("EUR/USD", ACTIVOS["EUR/USD"], _datos())
    assert filas, "la simulación no produjo ninguna señal"
    df = pd.DataFrame(filas)
    assert df["plazo_min"].between(simulacion.PLAZO_MIN, simulacion.PLAZO_MAX).all()
    for (_, tf), grupo in df.groupby(["mercado", "temporalidad"]):
        velas = pd.to_datetime(grupo["vela"]).sort_values()
        fin = velas + pd.to_timedelta(grupo.loc[velas.index, "horizonte"] * MINUTOS[tf], unit="min")
        assert (velas.iloc[1:].to_numpy() >= fin.iloc[:-1].to_numpy()).all(), "operaciones solapadas"


def test_decide_igual_que_en_directo(monkeypatch):
    """La decisión simulada en la vela t es la misma que se obtiene preparando solo los datos hasta t."""
    monkeypatch.setattr(simulacion, "VELAS_SIMULADAS", {"5m": 0, "15m": 700, "1h": 0, "4h": 0})
    datos = _datos()
    filas = simulacion.simular_mercado("EUR/USD", ACTIVOS["EUR/USD"], datos)
    coste = ACTIVOS["EUR/USD"]["coste"]
    _, ind_1h, _, _, _ = preparar(datos["1h"], coste)
    for fila in filas[:5]:
        t = datos["15m"].index.get_loc(pd.Timestamp(fila["vela"]))
        df, ind, senales, _, _ = preparar(datos["15m"].iloc[: t + 1], coste)
        r = {"df": df, "ind": ind, "senales": senales,
             "bt": backtest(df["Close"].to_numpy(), senales, coste)}
        tendencia = alinear(df.index, 15, ind_1h, 60)
        senal = juzgar(r, coste, "15m", tendencia, None)
        assert senal["direccion"] == fila["direccion"] and senal["horizonte"] == fila["horizonte"]
        assert np.isclose(senal["confianza"], fila["confianza"], atol=1e-4)


def test_informe_con_archivos_vacios_o_inexistentes(tmp_path):
    """El laboratorio recién empezado no tiene señales comprobadas: el informe no debe fallar."""
    import subprocess, sys
    from pathlib import Path
    vacio = tmp_path / "vivo.csv"
    pd.DataFrame([]).to_csv(vacio, index=False)
    salida = tmp_path / "INFORME.md"
    raiz = Path(__file__).resolve().parent.parent
    r = subprocess.run([sys.executable, str(raiz / "informe.py"), str(tmp_path / "simulacion.csv"), str(vacio),
                        "--salida", str(salida)], cwd=raiz, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "Todavía no hay señales comprobadas" in salida.read_text()
