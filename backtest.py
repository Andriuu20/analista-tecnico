"""Backtest: para cada estrategia y plazo, cuántas veces el precio fue en la dirección
de la señal al cabo de N velas (como una opción binaria a vencimiento)."""
import numpy as np
import pandas as pd

HORIZONTES = [1, 2, 3, 5, 10, 15, 20]  # en velas
PARTE_RECIENTE = 0.3  # último 30 % del histórico, para comprobar que no se ha "agotado"
PRIOR = 20  # peso del 50 % inicial al estimar el acierto (evita fiarse de pocas muestras)


def estimar(aciertos, total):
    """Acierto estimado, encogido hacia el 50 %: con pocas señales se queda cerca del 50 %."""
    return (aciertos + PRIOR / 2) / (total + PRIOR)


def backtest(cierre: np.ndarray, senales: dict, coste: float) -> pd.DataFrame:
    n = len(cierre)
    corte = int(n * (1 - PARTE_RECIENTE))
    filas = []
    for nombre, senal in senales.items():
        idx = np.flatnonzero(senal)
        for hz in HORIZONTES:
            v = idx[idx + hz < n]
            fila = {"estrategia": nombre, "horizonte": hz, "senales": len(v), "aciertos": 0,
                    "acierto": np.nan, "acierto_neto": np.nan, "senales_ant": 0, "aciertos_ant": 0,
                    "senales_rec": 0, "aciertos_rec": 0, "acierto_rec": np.nan, "mov_medio": np.nan}
            if len(v):
                mov = (cierre[v + hz] - cierre[v]) / cierre[v] * senal[v]
                ok = mov > 0
                rec = v >= corte
                fila.update(
                    aciertos=int(ok.sum()),
                    acierto=ok.mean(),
                    acierto_neto=(mov > coste).mean(),
                    senales_ant=int((~rec).sum()),
                    aciertos_ant=int(ok[~rec].sum()),
                    senales_rec=int(rec.sum()),
                    aciertos_rec=int(ok[rec].sum()),
                    acierto_rec=ok[rec].mean() if rec.any() else np.nan,
                    mov_medio=mov.mean(),
                )
            filas.append(fila)
    return pd.DataFrame(filas)
