import pandas as pd

from datos import ACTIVOS
from noticias import en_ventana, monedas


def test_monedas_de_cada_mercado():
    assert monedas("EUR/USD", ACTIVOS["EUR/USD"]) == {"EUR", "USD"}
    assert monedas("USD/JPY", ACTIVOS["USD/JPY"]) == {"USD", "JPY"}
    assert monedas("Oro (XAU/USD)", ACTIVOS["Oro (XAU/USD)"]) == {"USD"}
    assert monedas("BTC/USDT", ACTIVOS["BTC/USDT"]) == {"USD"}


def test_ventana_de_noticias():
    ahora = pd.Timestamp("2026-01-05 13:00", tz="UTC")
    eventos = [{"titulo": "Non-Farm Payrolls", "moneda": "USD", "hora": ahora + pd.Timedelta(minutes=20)},
               {"titulo": "ECB", "moneda": "EUR", "hora": ahora + pd.Timedelta(hours=5)}]
    assert [e["titulo"] for e in en_ventana(eventos, {"USD"}, ahora, ahora + pd.Timedelta(hours=1))] == ["Non-Farm Payrolls"]
    assert en_ventana(eventos, {"JPY"}, ahora, ahora + pd.Timedelta(days=1)) == []
    assert en_ventana(None, {"USD"}, ahora, ahora) == []
