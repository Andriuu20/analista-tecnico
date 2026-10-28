"""Estructura de mercado y Smart Money Concepts, a partir de los mismos techos y suelos
confirmados que usa el resto de la app (indicadores.pivotes, confirmados k velas después).

Todo se calcula recorriendo las velas en orden y usando solo lo conocido al cierre de cada una:
- Etiquetas HH/LH (techos) y HL/LL (suelos), y estado de la estructura (+1 alcista, -1 bajista).
- BOS (ruptura a favor de la estructura) y CHoCH (ruptura en contra: cambio de carácter), al
  cerrar más allá del último techo/suelo confirmado aún no roto.
- Barrida de liquidez: la mecha supera el último techo/suelo pero la vela cierra de vuelta dentro.
- Ruptura y retesteo: tras una ruptura, el precio vuelve al nivel roto y rebota en él.
- Fair Value Gaps (FVG): hueco entre la vela i-2 y la i; señal cuando el precio vuelve y reacciona.
- Order Blocks: última vela contraria antes de una ruptura; señal cuando el precio vuelve a ella.
- Divergencias del RSI entre dos techos o dos suelos consecutivos.
- Máximos/mínimos iguales (liquidez) y zona premium/discount, solo como contexto."""
import numpy as np
import pandas as pd

from indicadores import pivotes

K_PIVOTE = 5  # el mismo que usan soportes/resistencias y Fibonacci
_MAX_DIVERGENCIA = 60  # velas máximas entre los dos pivotes de una divergencia
_MAX_RETEST = 20  # velas para que llegue el retesteo tras una ruptura
_MAX_FVG = 100  # vida máxima de un FVG sin reaccionar
_MAX_OB = 150  # vida máxima de un order block
_BUSQUEDA_OB = 30  # velas hacia atrás para buscar la vela del order block

SENALES_ESTRUCTURA = ("bos", "choch", "barrida", "ruptura", "fvg", "order_block", "divergencia")


def calcular_estructura(df: pd.DataFrame, atr_s: pd.Series, rsi_s: pd.Series) -> tuple[dict, dict, dict]:
    """Devuelve (señales por estrategia, series por vela, contexto de la última vela)."""
    n = len(df)
    o, h, l, c = (df[x].to_numpy() for x in ("Open", "High", "Low", "Close"))
    a = atr_s.to_numpy()
    r = rsi_s.to_numpy()
    techos, suelos = pivotes(df, K_PIVOTE)
    sen = {k: np.zeros(n, dtype=int) for k in SENALES_ESTRUCTURA}
    estado_s = np.zeros(n, dtype=int)
    ult_techo_s = np.full(n, np.nan)
    ult_suelo_s = np.full(n, np.nan)

    it = isu = 0
    ult_t = ult_s = None  # (índice, precio) del último techo/suelo confirmado
    etiqueta_t = etiqueta_s = None
    roto_t = roto_s = barrido_t = barrido_s = True  # el nivel ya no cuenta para romper/barrer
    estado = 0
    eq_altos = eq_bajos = None  # (precio, vela de confirmación)
    retests, fvgs, obs = [], [], []  # pendientes: (dirección, ..., vela de origen)

    for t in range(n):
        tol = 0.1 * a[t] if a[t] > 0 else 0.0
        # --- nuevos pivotes confirmados en esta vela ---
        while it < len(techos) and techos[it][0] + K_PIVOTE <= t:
            i, p = techos[it]
            it += 1
            if ult_t is not None:
                etiqueta_t = "HH" if p > ult_t[1] else "LH"
                if abs(p - ult_t[1]) <= tol:
                    eq_altos = (max(p, ult_t[1]), t)
                if i - ult_t[0] <= _MAX_DIVERGENCIA and p > ult_t[1] and r[i] < r[ult_t[0]]:
                    sen["divergencia"][t] = -1  # precio hace techo más alto, RSI más bajo
            ult_t, roto_t, barrido_t = (i, p), False, False
        while isu < len(suelos) and suelos[isu][0] + K_PIVOTE <= t:
            i, p = suelos[isu]
            isu += 1
            if ult_s is not None:
                etiqueta_s = "HL" if p > ult_s[1] else "LL"
                if abs(p - ult_s[1]) <= tol:
                    eq_bajos = (min(p, ult_s[1]), t)
                if i - ult_s[0] <= _MAX_DIVERGENCIA and p < ult_s[1] and r[i] > r[ult_s[0]]:
                    sen["divergencia"][t] = 1  # precio hace suelo más bajo, RSI más alto
            ult_s, roto_s, barrido_s = (i, p), False, False

        # --- rupturas (BOS / CHoCH) y barridas de liquidez ---
        if ult_t is not None and not roto_t:
            if c[t] > ult_t[1]:
                (sen["bos"] if estado >= 0 else sen["choch"])[t] = 1
                estado, roto_t = 1, True
                retests.append((1, ult_t[1], t))
                _nuevo_order_block(obs, 1, o, h, l, c, t, ult_s)
            elif h[t] > ult_t[1] and not barrido_t:
                sen["barrida"][t] = -1  # mecha por encima del techo y cierre por debajo
                barrido_t = True
        if ult_s is not None and not roto_s:
            if c[t] < ult_s[1]:
                (sen["bos"] if estado <= 0 else sen["choch"])[t] = -1
                estado, roto_s = -1, True
                retests.append((-1, ult_s[1], t))
                _nuevo_order_block(obs, -1, o, h, l, c, t, ult_t)
            elif l[t] < ult_s[1] and not barrido_s:
                sen["barrida"][t] = 1
                barrido_s = True

        # --- retesteo del nivel roto ---
        quedan = []
        for d, nivel, t0 in retests:
            if t == t0:
                quedan.append((d, nivel, t0))
            elif t - t0 > _MAX_RETEST or (d == 1 and c[t] < nivel - 5 * tol) or (d == -1 and c[t] > nivel + 5 * tol):
                continue  # caducado o ruptura fallida
            elif d == 1 and l[t] <= nivel + 2 * tol and c[t] > nivel and c[t] > o[t]:
                sen["ruptura"][t] = 1
            elif d == -1 and h[t] >= nivel - 2 * tol and c[t] < nivel and c[t] < o[t]:
                sen["ruptura"][t] = -1
            else:
                quedan.append((d, nivel, t0))
        retests = quedan

        # --- Fair Value Gaps: se forman con 3 velas y se usan al volver el precio ---
        quedan = []
        for d, abajo, arriba, t0 in fvgs:
            if t - t0 > _MAX_FVG or (d == 1 and c[t] < abajo) or (d == -1 and c[t] > arriba):
                continue  # caducado o invalidado
            if d == 1 and l[t] <= arriba and c[t] > abajo and c[t] > o[t]:
                sen["fvg"][t] = 1
            elif d == -1 and h[t] >= abajo and c[t] < arriba and c[t] < o[t]:
                sen["fvg"][t] = -1
            else:
                quedan.append((d, abajo, arriba, t0))
        fvgs = quedan
        if t >= 2 and a[t] > 0:
            if l[t] - h[t - 2] >= tol:
                fvgs.append((1, h[t - 2], l[t], t))
            elif l[t - 2] - h[t] >= tol:
                fvgs.append((-1, h[t], l[t - 2], t))

        # --- Order Blocks ---
        quedan = []
        for d, abajo, arriba, t0 in obs:
            if t == t0:
                quedan.append((d, abajo, arriba, t0))
            elif t - t0 > _MAX_OB or (d == 1 and c[t] < abajo) or (d == -1 and c[t] > arriba):
                continue
            elif d == 1 and l[t] <= arriba and c[t] > abajo and c[t] > o[t]:
                sen["order_block"][t] = 1
            elif d == -1 and h[t] >= abajo and c[t] < arriba and c[t] < o[t]:
                sen["order_block"][t] = -1
            else:
                quedan.append((d, abajo, arriba, t0))
        obs = quedan

        estado_s[t] = estado
        if ult_t is not None:
            ult_techo_s[t] = ult_t[1]
        if ult_s is not None:
            ult_suelo_s[t] = ult_s[1]

    series = {"estado": estado_s, "ult_techo": ult_techo_s, "ult_suelo": ult_suelo_s}
    contexto = {
        "estado": {1: "Alcista", -1: "Bajista", 0: "Sin definir"}[estado],
        "etiquetas": " · ".join(e for e in (etiqueta_t, etiqueta_s) if e) or "—",
        "max_iguales": eq_altos[0] if eq_altos and n - 1 - eq_altos[1] <= 300 else None,
        "min_iguales": eq_bajos[0] if eq_bajos and n - 1 - eq_bajos[1] <= 300 else None,
        "fvg": [(d, abajo, arriba) for d, abajo, arriba, _ in fvgs[-3:]],
        "order_blocks": [(d, abajo, arriba) for d, abajo, arriba, _ in obs[-3:]],
        "zona": _zona(c[-1], ult_techo_s[-1], ult_suelo_s[-1]),
    }
    return sen, series, contexto


def _nuevo_order_block(obs: list, d: int, o, h, l, c, t: int, origen) -> None:
    """Última vela contraria (bajista si la ruptura es alcista) entre el último pivote opuesto y la ruptura."""
    inicio = max(origen[0] if origen else 0, t - _BUSQUEDA_OB)
    for j in range(t - 1, inicio - 1, -1):
        if (d == 1 and c[j] < o[j]) or (d == -1 and c[j] > o[j]):
            obs.append((d, l[j], h[j], t))
            return


def _zona(precio: float, techo: float, suelo: float) -> str | None:
    """Premium (mitad alta del último rango) o discount (mitad baja)."""
    if np.isnan(techo) or np.isnan(suelo) or techo <= suelo:
        return None
    posicion = (precio - suelo) / (techo - suelo)
    return "premium" if posicion > 0.5 else "discount"
