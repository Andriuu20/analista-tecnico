"""Plan de operación (entrada, Stop Loss, Take Profit) y su evaluación con el histórico.

Reglas fijas y comprobables:
- Entrada: cierre de la última vela.
- Stop Loss: más allá del último suelo confirmado (compras) o techo (ventas) + 0,1 ATR. Si esa
  distancia no está entre 0,5 y 3 ATR, se usa 1,5 ATR.
- Take Profit: R veces el riesgo, con R ∈ {1; 1,5; 2; 3}.
- Se simulan las señales pasadas de las mismas estrategias con la misma regla: gana si toca el TP
  antes que el SL; si en la misma vela se tocan los dos, se cuenta como pérdida (lo prudente); si en
  50 velas no toca ninguno, se cierra al precio de ese momento. Se descuenta el coste de operar.
- R se elige con el 70 % antiguo del histórico y los resultados se miden con el 30 % reciente,
  igual que el resto de la app, para no engañarse eligiendo a posteriori."""
import numpy as np
import pandas as pd

from backtest import PARTE_RECIENTE

R_OPCIONES = (1.0, 1.5, 2.0, 3.0)
MAX_VELAS = 50
MIN_OPERACIONES = 20
COSTE_MAXIMO_R = 0.25  # si el coste se come más de un 25 % del riesgo, no compensa operar


def riesgo(direccion, cierre, atr_v, ult_techo, ult_suelo):
    """Distancia del Stop Loss según la regla del módulo (vale para escalares o arrays)."""
    estructural = np.where(np.asarray(direccion) == 1, cierre - ult_suelo, ult_techo - cierre) + 0.1 * atr_v
    with np.errstate(invalid="ignore"):
        valido = (estructural >= 0.5 * atr_v) & (estructural <= 3 * atr_v)
    return np.where(valido, estructural, 1.5 * atr_v)


def simular(h, l, c, idx, dirs, riesgos, r: float, coste: float):
    """Resultado en múltiplos de R (ya descontado el coste) y duración en velas de cada operación."""
    resultado = np.full(len(idx), np.nan)
    duracion = np.full(len(idx), np.nan)
    for j, (i, d, rk) in enumerate(zip(idx, dirs, riesgos)):
        fin = i + MAX_VELAS
        if fin >= len(c) or not rk > 0:
            continue
        entrada = c[i]
        sl, tp = entrada - d * rk, entrada + d * r * rk
        altos, bajos = h[i + 1: fin + 1], l[i + 1: fin + 1]
        toca_sl = bajos <= sl if d == 1 else altos >= sl
        toca_tp = altos >= tp if d == 1 else bajos <= tp
        k_sl = np.argmax(toca_sl) if toca_sl.any() else MAX_VELAS
        k_tp = np.argmax(toca_tp) if toca_tp.any() else MAX_VELAS
        if k_sl < MAX_VELAS and k_sl <= k_tp:
            resultado[j], duracion[j] = -1.0, k_sl + 1
        elif k_tp < MAX_VELAS:
            resultado[j], duracion[j] = r, k_tp + 1
        else:
            resultado[j], duracion[j] = d * (c[fin] - entrada) / rk, MAX_VELAS
        resultado[j] -= coste * entrada / rk
    return resultado, duracion


def evaluar(df: pd.DataFrame, ind: pd.DataFrame, senales: dict, estrategias: list, direccion: int,
            coste: float) -> dict:
    """Plan para la señal actual y cómo le fue a esa misma configuración en el pasado."""
    h, l, c = (df[x].to_numpy() for x in ("High", "Low", "Close"))
    a = ind["atr"].to_numpy()
    techo, suelo = ind["ult_techo"].to_numpy(), ind["ult_suelo"].to_numpy()

    # señales pasadas de las estrategias que apoyan la operación (si se contradicen en una vela, fuera)
    suma = np.sum([senales[k] for k in estrategias], axis=0)
    cuenta = np.sum([senales[k] != 0 for k in estrategias], axis=0)
    idx = np.flatnonzero((cuenta > 0) & (np.abs(suma) == cuenta))  # las de las últimas velas no tienen futuro
    dirs = np.sign(suma[idx]).astype(int)
    riesgos = riesgo(dirs, c[idx], a[idx], techo[idx], suelo[idx])
    reciente = idx >= int(len(c) * (1 - PARTE_RECIENTE))

    por_r = {}
    for r in R_OPCIONES:
        res, dur = simular(h, l, c, idx, dirs, riesgos, r, coste)
        ok = ~np.isnan(res)
        ant, rec = ok & ~reciente, ok & reciente
        por_r[r] = {
            "n_ant": int(ant.sum()), "esperanza_ant": res[ant].mean() if ant.any() else np.nan,
            "n_rec": int(rec.sum()), "esperanza_rec": res[rec].mean() if rec.any() else np.nan,
            "tp_rec": int((res[rec] > 0).sum()), "duracion": float(np.nanmedian(dur[ok])) if ok.any() else np.nan,
        }
    candidatos = [r for r in R_OPCIONES if por_r[r]["n_ant"] >= MIN_OPERACIONES]
    r_elegido = max(candidatos, key=lambda r: por_r[r]["esperanza_ant"]) if candidatos else 2.0

    entrada = c[-1]
    rk = float(riesgo(direccion, entrada, a[-1], techo[-1], suelo[-1]))
    stats = por_r[r_elegido]
    return {
        "entrada": entrada,
        "sl": entrada - direccion * rk,
        "tp": entrada + direccion * r_elegido * rk,
        "r": r_elegido,
        "coste_r": coste * entrada / rk if rk > 0 else np.inf,
        "operaciones": stats["n_rec"],
        "tp_alcanzado": stats["tp_rec"],
        "esperanza": stats["esperanza_rec"],
        "duracion_velas": stats["duracion"],
        "datos_suficientes": bool(candidatos) and stats["n_rec"] >= MIN_OPERACIONES // 2,
    }
