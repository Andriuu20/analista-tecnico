"""Noticias económicas de alto impacto (calendario semanal público de Forex Factory, sin clave).

No predice nada: solo avisa de que hay un dato importante (empleo, IPC, tipos de interés…) que
puede mover mucho el precio y ensanchar el spread. Si el calendario no responde, la app sigue
funcionando sin este aviso."""
import pandas as pd
import requests

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
MARGEN_ANTES = pd.Timedelta(minutes=30)


def descargar_calendario() -> list[dict] | None:
    try:
        r = requests.get(URL, timeout=8, headers={"User-Agent": "analista-tecnico"})
        r.raise_for_status()
        eventos = []
        for e in r.json():
            if e.get("impact") != "High" or not e.get("date"):
                continue
            eventos.append({"titulo": e.get("title", ""), "moneda": e.get("country", ""),
                            "hora": pd.Timestamp(e["date"]).tz_convert("UTC")})
        return eventos
    except Exception:
        return None


def monedas(nombre: str, cfg: dict) -> set[str]:
    """Monedas que afectan a un mercado: EUR/USD -> {EUR, USD}; oro y cripto -> {USD}."""
    if cfg["fuente"] == "binance" or "XAU" in nombre or "Oro" in nombre:
        return {"USD"}
    simbolo = cfg["simbolo"].replace("=X", "")
    if len(simbolo) == 6 and simbolo.isalpha():
        return {simbolo[:3], simbolo[3:]}
    if len(simbolo) == 3 and simbolo.isalpha():  # Yahoo: JPY=X es USD/JPY
        return {"USD", simbolo}
    return {m for m in nombre.replace(" ", "/").split("/") if len(m) == 3 and m.isalpha()}


def en_ventana(eventos: list[dict] | None, mon: set[str], desde: pd.Timestamp, hasta: pd.Timestamp) -> list[dict]:
    """Eventos de alto impacto de esas monedas entre `desde` - 30 min y `hasta`."""
    if not eventos:
        return []
    return [e for e in eventos if e["moneda"] in mon and desde - MARGEN_ANTES <= e["hora"] <= hasta]
