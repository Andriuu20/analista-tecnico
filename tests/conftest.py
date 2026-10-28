"""Configuración común: importar los módulos de la app y generar datos aleatorios reproducibles."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def paseo_aleatorio(semilla: int, n: int = 3000, minutos: int = 15) -> pd.DataFrame:
    """Velas de un paseo aleatorio: ninguna estrategia puede tener ventaja real sobre ellas."""
    rng = np.random.default_rng(semilla)
    idx = pd.date_range("2025-01-01", periods=n, freq=f"{minutos}min", tz="UTC")
    cierre = 1.08 * np.exp(np.cumsum(rng.normal(0, 0.0008, n)))
    apertura = np.r_[cierre[0], cierre[:-1]] * (1 + rng.normal(0, 0.0002, n))
    alto = np.maximum(apertura, cierre) * (1 + np.abs(rng.normal(0, 0.0004, n)))
    bajo = np.minimum(apertura, cierre) * (1 - np.abs(rng.normal(0, 0.0004, n)))
    return pd.DataFrame({"Open": apertura, "High": alto, "Low": bajo, "Close": cierre, "Volume": 0.0}, index=idx)


@pytest.fixture
def velas():
    return paseo_aleatorio(1)
