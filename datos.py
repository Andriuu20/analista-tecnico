"""Descarga de velas de mercado (Yahoo Finance para forex/oro, Binance para cripto)."""
import os
import zlib

import numpy as np
import pandas as pd
import requests

# coste: spread + comisión aproximados de ida y vuelta, en fracción del precio
ACTIVOS = {
    "EUR/USD": {"fuente": "yahoo", "simbolo": "EURUSD=X", "coste": 0.0001},
    "USD/JPY": {"fuente": "yahoo", "simbolo": "JPY=X", "coste": 0.00012},
    "EUR/JPY": {"fuente": "yahoo", "simbolo": "EURJPY=X", "coste": 0.00015},
    "GBP/USD": {"fuente": "yahoo", "simbolo": "GBPUSD=X", "coste": 0.00012},
    "GBP/JPY": {"fuente": "yahoo", "simbolo": "GBPJPY=X", "coste": 0.0002},
    "AUD/USD": {"fuente": "yahoo", "simbolo": "AUDUSD=X", "coste": 0.00012},
    "USD/CAD": {"fuente": "yahoo", "simbolo": "CAD=X", "coste": 0.00015},
    "USD/CHF": {"fuente": "yahoo", "simbolo": "CHF=X", "coste": 0.00015},
    "EUR/GBP": {"fuente": "yahoo", "simbolo": "EURGBP=X", "coste": 0.00015},
    "Oro (XAU/USD)": {"fuente": "yahoo", "simbolo": "GC=F", "coste": 0.0003},
    "BTC/USDT": {"fuente": "binance", "simbolo": "BTCUSDT", "coste": 0.0005},
    "ETH/USDT": {"fuente": "binance", "simbolo": "ETHUSDT", "coste": 0.0005},
    "SOL/USDT": {"fuente": "binance", "simbolo": "SOLUSDT", "coste": 0.0008},
    "XRP/USDT": {"fuente": "binance", "simbolo": "XRPUSDT", "coste": 0.0008},
}

# etiqueta -> (código de intervalo, minutos por vela)
INTERVALOS = {
    "1 min": ("1m", 1),
    "5 min": ("5m", 5),
    "15 min": ("15m", 15),
    "30 min": ("30m", 30),
    "1 hora": ("1h", 60),
    "4 horas": ("4h", 240),
    "1 día": ("1d", 1440),
}
MINUTOS = {codigo: minutos for codigo, minutos in INTERVALOS.values()}

# máximo histórico intradía que da Yahoo por intervalo
_PERIODO_YAHOO = {"1m": "7d", "5m": "60d", "15m": "60d", "30m": "60d", "1h": "730d", "1d": "10y"}
_URLS_BINANCE = [
    "https://data-api.binance.vision/api/v3/klines",  # espejo público, sin bloqueo geográfico
    "https://api.binance.com/api/v3/klines",
]
_COLUMNAS = ["Open", "High", "Low", "Close", "Volume"]


def activo_personalizado(simbolo: str) -> dict:
    """Interpreta un símbolo escrito a mano: XXXUSDT -> Binance, el resto -> Yahoo."""
    simbolo = simbolo.strip().upper()
    if simbolo.endswith(("USDT", "USDC", "BTC")) and "=" not in simbolo and "-" not in simbolo:
        return {"fuente": "binance", "simbolo": simbolo, "coste": 0.0008}
    return {"fuente": "yahoo", "simbolo": simbolo, "coste": 0.0002}


def _yahoo(simbolo: str, codigo: str) -> pd.DataFrame:
    import yfinance as yf

    base = "1h" if codigo == "4h" else codigo
    df = yf.Ticker(simbolo).history(period=_PERIODO_YAHOO[base], interval=base, auto_adjust=False)
    if df is None or df.empty:
        raise ValueError(f"Yahoo no devolvió datos para {simbolo}")
    df = df[_COLUMNAS].copy()
    df.index = df.index.tz_localize("UTC") if df.index.tz is None else df.index.tz_convert("UTC")
    if codigo == "4h":
        df = df.resample("4h").agg(
            {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"}
        )
    return df.dropna(subset=["Open", "High", "Low", "Close"])


def _binance(simbolo: str, codigo: str, velas: int = 5000) -> pd.DataFrame:
    filas, fin = [], None
    while len(filas) < velas:
        params = {"symbol": simbolo, "interval": codigo, "limit": 1000}
        if fin is not None:
            params["endTime"] = fin
        lote = None
        for url in _URLS_BINANCE:
            try:
                r = requests.get(url, params=params, timeout=10)
                if r.status_code == 200:
                    lote = r.json()
                    break
            except requests.RequestException:
                continue
        if lote is None:
            raise ValueError(f"Binance no respondió para {simbolo}")
        if not lote:
            break
        filas = lote + filas
        fin = lote[0][0] - 1
        if len(lote) < 1000:
            break
    if not filas:
        raise ValueError(f"Binance no devolvió datos para {simbolo}")
    df = pd.DataFrame([f[:6] for f in filas[-velas:]], columns=["t"] + _COLUMNAS)
    df.index = pd.to_datetime(df.pop("t"), unit="ms", utc=True)
    return df.astype(float)


def _sinteticos(simbolo: str, codigo: str, n: int = 3000) -> pd.DataFrame:
    """Paseo aleatorio, solo para pruebas sin conexión (ANALISTA_DEMO=1)."""
    rng = np.random.default_rng(zlib.crc32(f"{simbolo}{codigo}".encode()))
    fin = pd.Timestamp.now(tz="UTC").floor(f"{MINUTOS[codigo]}min")
    idx = pd.date_range(end=fin, periods=n, freq=f"{MINUTOS[codigo]}min")
    cierre = 1.08 * np.exp(np.cumsum(rng.normal(0, 0.0008, n)))
    apertura = np.r_[cierre[0], cierre[:-1]]
    alto = np.maximum(apertura, cierre) * (1 + np.abs(rng.normal(0, 0.0004, n)))
    bajo = np.minimum(apertura, cierre) * (1 - np.abs(rng.normal(0, 0.0004, n)))
    return pd.DataFrame(
        {"Open": apertura, "High": alto, "Low": bajo, "Close": cierre, "Volume": 0.0}, index=idx
    )


def quitar_vela_abierta(df: pd.DataFrame, codigo: str) -> pd.DataFrame:
    """Deja solo velas cerradas: la señal se calcula siempre con la vela ya terminada."""
    ahora = pd.Timestamp.now(tz="UTC")
    return df[df.index + pd.Timedelta(minutes=MINUTOS[codigo]) <= ahora]


def descargar(fuente: str, simbolo: str, codigo: str) -> tuple[pd.DataFrame, str]:
    """Devuelve (velas cerradas, nombre de la fuente usada)."""
    if os.environ.get("ANALISTA_DEMO") == "1":
        return _sinteticos(simbolo, codigo), "datos de prueba"
    if fuente == "binance":
        try:
            return quitar_vela_abierta(_binance(simbolo, codigo), codigo), "Binance"
        except ValueError:
            # alternativa: el mismo par en Yahoo (BTCUSDT -> BTC-USD)
            alt = simbolo.removesuffix("USDT").removesuffix("USDC") + "-USD"
            return quitar_vela_abierta(_yahoo(alt, codigo), codigo), "Yahoo Finance"
    return quitar_vela_abierta(_yahoo(simbolo, codigo), codigo), "Yahoo Finance"
