"""Estrategias. Cada una devuelve, por vela, +1 (compra), -1 (venta) o 0 (nada),
usando solo información disponible al cierre de esa vela."""
import numpy as np
import pandas as pd

from estructura import calcular_estructura
from indicadores import (adx, atr, bollinger, ema, estocastico, extensiones_fibonacci, macd, niveles_fibonacci,
                         pivotes, rsi, sma, supertrend)
from tendencia import serie_tendencia

ESTRATEGIAS = {
    "medias": "Cruce de medias móviles (EMA 9 / EMA 21)",
    "rsi": "RSI sale de sobreventa (<30) o sobrecompra (>70)",
    "macd": "Cruce del MACD con su línea de señal",
    "soportes": "Rebote en soporte o rechazo en resistencia",
    "fibonacci": "Rebote en la zona 50 %-78,6 % de Fibonacci a favor del impulso",
    "velas": "Patrones de velas (envolvente, martillo, estrella fugaz)",
    "supertrend": "Cambio de dirección del SuperTrend (10, 3)",
    "cruce_sma": "Cruce dorado o de la muerte (SMA 50 / SMA 200)",
    "bollinger": "Vuelta al interior de las Bandas de Bollinger (20, 2)",
    "estocastico": "Cruce del estocástico en sobreventa (<20) o sobrecompra (>80)",
    "divergencia": "Divergencia entre el precio y el RSI",
    "ruptura": "Ruptura y retesteo de un techo o suelo",
    "bos": "Ruptura de estructura a favor (BOS)",
    "choch": "Cambio de carácter de la estructura (CHoCH)",
    "barrida": "Barrida de liquidez (mecha más allá de un techo/suelo y cierre de vuelta)",
    "fvg": "Reacción en un Fair Value Gap (FVG)",
    "order_block": "Reacción en un Order Block",
}

# nombres cortos para las tablas en el móvil
NOMBRES_CORTOS = {
    "medias": "EMA 9/21", "rsi": "RSI", "macd": "MACD", "soportes": "Soportes/resist.", "fibonacci": "Fibonacci",
    "velas": "Velas japonesas", "supertrend": "SuperTrend", "cruce_sma": "SMA 50/200", "bollinger": "Bollinger",
    "estocastico": "Estocástico", "divergencia": "Divergencia RSI", "ruptura": "Ruptura+retest", "bos": "BOS",
    "choch": "CHoCH", "barrida": "Barrida liquidez", "fvg": "FVG", "order_block": "Order Block",
}

_CALENTAMIENTO = 60  # velas iniciales sin señal mientras se estabilizan los indicadores
_K_PIVOTE = 5
_MEMORIA_PIVOTES = 300  # velas hacia atrás en las que un techo/suelo sigue contando


def _cruce(a: pd.Series, b: pd.Series) -> np.ndarray:
    encima = (a > b).to_numpy()
    previo = np.r_[encima[0], encima[:-1]]
    return np.where(encima & ~previo, 1, np.where(~encima & previo, -1, 0))


def _velas(df: pd.DataFrame, ema21: pd.Series):
    o, h, l, c = (df[x] for x in ("Open", "High", "Low", "Close"))
    cuerpo = (c - o).abs()
    rango = (h - l).replace(0, np.nan)
    sombra_sup = h - np.maximum(o, c)
    sombra_inf = np.minimum(o, c) - l
    alcista, bajista = c > o, c < o
    env_alc = bajista.shift(1, fill_value=False) & alcista & (o <= c.shift(1)) & (c >= o.shift(1)) & (
        cuerpo > cuerpo.shift(1)
    )
    env_baj = alcista.shift(1, fill_value=False) & bajista & (o >= c.shift(1)) & (c <= o.shift(1)) & (
        cuerpo > cuerpo.shift(1)
    )
    martillo = (sombra_inf >= 2 * cuerpo) & (sombra_sup <= 0.25 * rango) & (cuerpo >= 0.05 * rango) & (c < ema21)
    estrella = (sombra_sup >= 2 * cuerpo) & (sombra_inf <= 0.25 * rango) & (cuerpo >= 0.05 * rango) & (c > ema21)

    senal = np.where(env_alc | martillo, 1, np.where(env_baj | estrella, -1, 0))
    senal[(env_alc | martillo).to_numpy() & (env_baj | estrella).to_numpy()] = 0
    nombre = np.select(
        [env_alc, env_baj, martillo, estrella],
        ["Envolvente alcista", "Envolvente bajista", "Martillo", "Estrella fugaz"],
        default="",
    )
    return senal, nombre


def _soportes_y_fibonacci(df: pd.DataFrame, atr_s: pd.Series):
    """Recorre las velas manteniendo los techos/suelos ya confirmados en cada momento."""
    n = len(df)
    o, h, l, c = (df[x].to_numpy() for x in ("Open", "High", "Low", "Close"))
    a = atr_s.to_numpy()
    techos, suelos = pivotes(df, _K_PIVOTE)
    sr = np.zeros(n, dtype=int)
    fib = np.zeros(n, dtype=int)
    it = isu = 0
    conf_t, conf_s = [], []  # pivotes confirmados hasta la vela actual

    for t in range(n):
        while it < len(techos) and techos[it][0] + _K_PIVOTE <= t:
            conf_t.append(techos[it])
            it += 1
        while isu < len(suelos) and suelos[isu][0] + _K_PIVOTE <= t:
            conf_s.append(suelos[isu])
            isu += 1
        if t < _CALENTAMIENTO or not conf_t or not conf_s or not a[t] > 0:
            continue

        # --- Soportes y resistencias ---
        tol = 0.3 * a[t]
        resist = [p for i, p in conf_t[-12:] if t - i <= _MEMORIA_PIVOTES and p >= c[t]]
        soport = [p for i, p in conf_s[-12:] if t - i <= _MEMORIA_PIVOTES and p <= c[t]]
        compra = venta = False
        if soport:
            s = min(soport, key=lambda p: abs(p - l[t]))
            compra = abs(l[t] - s) <= tol and c[t] > s and c[t] > o[t]
        if resist:
            r = min(resist, key=lambda p: abs(p - h[t]))
            venta = abs(h[t] - r) <= tol and c[t] < r and c[t] < o[t]
        sr[t] = 1 if compra and not venta else -1 if venta and not compra else 0

        # --- Fibonacci sobre el último impulso confirmado ---
        ih, maximo = conf_t[-1]
        il, minimo = conf_s[-1]
        rango = maximo - minimo
        if rango < 3 * a[t]:
            continue
        if il < ih:  # impulso alcista: buscamos compra en el retroceso
            retroceso = (maximo - l[t]) / rango
            sin_romper = h[ih + 1 : t + 1].max(initial=-np.inf) <= maximo and l[t] > minimo
            if 0.5 <= retroceso <= 0.786 and sin_romper and c[t] > o[t] and c[t] > maximo - 0.618 * rango:
                fib[t] = 1
        else:  # impulso bajista: buscamos venta en el rebote
            retroceso = (h[t] - minimo) / rango
            sin_romper = l[il + 1 : t + 1].min(initial=np.inf) >= minimo and h[t] < maximo
            if 0.5 <= retroceso <= 0.786 and sin_romper and c[t] < o[t] and c[t] < minimo + 0.618 * rango:
                fib[t] = -1
    return sr, fib, conf_t, conf_s


def calcular(df: pd.DataFrame):
    """Devuelve (indicadores, señales por estrategia, contexto para la vela actual)."""
    c = df["Close"]
    ind = pd.DataFrame(index=df.index)
    for n in (9, 21, 50, 200):
        ind[f"ema{n}"] = ema(c, n)
    ind["rsi"] = rsi(c)
    ind["macd"], ind["macd_senal"], ind["macd_hist"] = macd(c)
    ind["atr"] = atr(df)
    for n in (50, 100, 200):
        ind[f"sma{n}"] = sma(c, n)
    ind["bb_sup"], ind["bb_media"], ind["bb_inf"] = bollinger(c)
    ind["est_k"], ind["est_d"] = estocastico(df)
    ind["adx"], ind["di_mas"], ind["di_menos"] = adx(df)
    ind["supertrend"], ind["st_dir"] = supertrend(df)

    senales = {"medias": _cruce(ind["ema9"], ind["ema21"])}
    r = ind["rsi"]
    senales["rsi"] = np.where(
        (r.shift(1) < 30) & (r >= 30), 1, np.where((r.shift(1) > 70) & (r <= 70), -1, 0)
    )
    senales["macd"] = _cruce(ind["macd"], ind["macd_senal"])
    senales["soportes"], senales["fibonacci"], techos, suelos = _soportes_y_fibonacci(df, ind["atr"])
    senales["velas"], patron = _velas(df, ind["ema21"])
    st_dir = ind["st_dir"].to_numpy()
    senales["supertrend"] = np.r_[0, np.where(st_dir[1:] != st_dir[:-1], st_dir[1:], 0)]
    senales["cruce_sma"] = _cruce(ind["sma50"], ind["sma200"])
    senales["cruce_sma"][: 200 + 1] = 0  # sin SMA 200 completa no hay cruce real
    previo = c.shift(1)
    senales["bollinger"] = np.where(
        (previo < ind["bb_inf"].shift(1)) & (c > ind["bb_inf"]), 1,
        np.where((previo > ind["bb_sup"].shift(1)) & (c < ind["bb_sup"]), -1, 0))
    k, d = ind["est_k"], ind["est_d"]
    cruce_est = _cruce(k, d)
    senales["estocastico"] = np.where(
        (cruce_est == 1) & (d < 20), 1, np.where((cruce_est == -1) & (d > 80), -1, 0))
    sen_est, series_est, ctx_est = calcular_estructura(df, ind["atr"], r)
    senales.update(sen_est)
    ind["estructura"], ind["ult_techo"], ind["ult_suelo"] = (
        series_est["estado"], series_est["ult_techo"], series_est["ult_suelo"])
    for s in senales.values():
        s[:_CALENTAMIENTO] = 0

    # contexto de la última vela para mostrar en pantalla
    n, precio = len(df), c.iat[-1]
    recientes_t = sorted({round(p, 6) for i, p in techos if n - 1 - i <= _MEMORIA_PIVOTES})
    recientes_s = sorted({round(p, 6) for i, p in suelos if n - 1 - i <= _MEMORIA_PIVOTES})
    contexto = {
        "precio": precio,
        "resistencia": min((p for p in recientes_t if p > precio), default=None),
        "soporte": max((p for p in recientes_s if p < precio), default=None),
        "techos": recientes_t,
        "suelos": recientes_s,
        "patron": patron[-1],
        "rsi": r.iat[-1],
        "tendencia": _tendencia(ind),
        "fibonacci": None,
        "estructura": ctx_est,
        "regimen": _regimen(ind),
        "volatilidad": _volatilidad(ind["atr"]),
        "sobre_sma200": None if np.isnan(ind["sma200"].iat[-1]) else bool(precio > ind["sma200"].iat[-1]),
    }
    if techos and suelos:
        (ih, maximo), (il, minimo) = techos[-1], suelos[-1]
        alcista = il < ih
        contexto["fibonacci"] = {
            "alcista": alcista,
            "desde": df.index[min(ih, il)],
            "niveles": niveles_fibonacci(maximo, minimo, alcista),
            "extensiones": extensiones_fibonacci(maximo, minimo, alcista),
        }
    return ind, senales, contexto


def _tendencia(ind: pd.DataFrame) -> str:
    return {1: "Alcista", -1: "Bajista", 0: "Lateral"}[int(serie_tendencia(ind)[-1])]


def _regimen(ind: pd.DataFrame) -> str:
    """Fuerza de la tendencia según el ADX (umbrales clásicos 20 y 25)."""
    valor = ind["adx"].iat[-1]
    if np.isnan(valor):
        return "Sin datos"
    if valor < 20:
        return "Lateral"
    lado = "alcista" if ind["di_mas"].iat[-1] > ind["di_menos"].iat[-1] else "bajista"
    return f"Tendencia {'fuerte' if valor >= 25 else 'débil'} {lado}"


def _volatilidad(atr_s: pd.Series, ventana: int = 500) -> str:
    """Volatilidad actual comparada con la de las últimas `ventana` velas (percentil del ATR)."""
    reciente = atr_s.iloc[-ventana:]
    percentil = (reciente < atr_s.iat[-1]).mean()
    return "Baja" if percentil < 0.2 else "Alta" if percentil > 0.8 else "Normal"
