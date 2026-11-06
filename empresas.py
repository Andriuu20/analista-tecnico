"""Análisis de empresas a largo plazo (sección «Empresas» de la app).

No da recomendaciones de compra: muestra datos verificables de Yahoo Finance (informes trimestrales,
márgenes, deuda, valoración, opinión de analistas, noticias) y los compara con el S&P 500. Lo único que se
mide con el histórico (📏) es cómo se movió la acción en las semanas siguientes a batir o decepcionar las
expectativas en sus resultados; el resto son referencias orientativas con umbrales fijos."""
import os
import zlib

import numpy as np
import pandas as pd

REFERENCIA = "SPY"  # fondo que replica el S&P 500
DIAS_TRAS_RESULTADOS = 20  # sesiones tras el informe en las que se mide la reacción
ANOS_RECIENTE = 2  # cotizando desde hace menos de esto = salida a bolsa reciente

# Cada temática es una cadena de valor, ordenada desde la materia prima hasta la marca final. La idea («picos y
# palas»): en una fiebre del oro, a quien vende los picos y las palas le va bien gane quien gane la carrera.
MARCA_FINAL = "(marcas finales)"
CADENAS = {
    "Inteligencia artificial": {
        "idea": "Toda la IA funciona con chips. Antes de la marca que la usa (Microsoft, Google…) están quien diseña "
                "los chips, quien los fabrica, quien hace las máquinas para fabricarlos y quien da energía a los "
                "centros de datos.",
        "eslabones": {
            "Máquinas para fabricar chips": [
                ("ASML", "ASML (Países Bajos)", "La única que hace las máquinas EUV para los chips más avanzados"),
                ("AMAT", "Applied Materials", "Máquinas y materiales para fabricar chips"),
                ("LRCX", "Lam Research", "Máquinas que graban y depositan las capas de los chips"),
                ("KLAC", "KLA", "Máquinas que inspeccionan los chips en busca de defectos"),
            ],
            "Fabrican los chips": [
                ("TSM", "TSMC (Taiwán)", "Fabrica los chips que diseñan NVIDIA, AMD, Apple y Broadcom"),
                ("005930.KS", "Samsung (Corea)", "Fabrica chips y memoria, para sí y para otros"),
                ("0981.HK", "SMIC (China)", "El mayor fabricante de chips de China"),
            ],
            "Memoria": [
                ("MU", "Micron", "Memoria (HBM) que va junto a los chips de IA"),
                ("000660.KS", "SK Hynix (Corea)", "Principal proveedor de memoria HBM para NVIDIA"),
            ],
            "Diseñan los chips": [
                ("NVDA", "NVIDIA", "Diseña los chips (GPU) con los que se entrena casi toda la IA. No los fabrica: lo hace TSMC"),
                ("AMD", "AMD", "Diseña chips para IA y ordenadores; principal rival de NVIDIA"),
                ("AVGO", "Broadcom", "Chips de IA a medida (Google, Meta) y redes para centros de datos"),
                ("ARM", "Arm", "Diseña la arquitectura de la mayoría de chips de móviles y de muchos servidores"),
            ],
            "Energía y refrigeración de los centros de datos": [
                ("VRT", "Vertiv", "Refrigeración y alimentación eléctrica de los centros de datos"),
                ("ETN", "Eaton", "Equipos eléctricos para centros de datos y la red"),
                ("GEV", "GE Vernova", "Turbinas y equipos de la red eléctrica que alimentan los centros de datos"),
            ],
            f"Usan la IA {MARCA_FINAL}": [
                ("MSFT", "Microsoft", "Nube Azure y socio de OpenAI (ChatGPT)"),
                ("GOOGL", "Alphabet (Google)", "Buscador, YouTube, nube y modelos de IA Gemini"),
                ("AMZN", "Amazon", "Comercio electrónico y la mayor nube del mundo (AWS)"),
                ("META", "Meta", "Facebook, Instagram y WhatsApp; gran comprador de chips de IA"),
                ("ORCL", "Oracle", "Bases de datos y centros de datos para IA"),
                ("PLTR", "Palantir", "Software de análisis de datos e IA para gobiernos y empresas"),
            ],
        },
    },
    "Energía solar": {
        "idea": "Antes de quien vende la electricidad solar están quien fabrica los paneles, quien hace los inversores "
                "y seguidores que los acompañan y quien produce el polisilicio del que están hechos.",
        "eslabones": {
            "Materia prima (polisilicio)": [
                ("DQ", "Daqo New Energy (China)", "Fabrica polisilicio, la materia prima de los paneles"),
                ("WCH.DE", "Wacker Chemie (Alemania)", "Polisilicio de alta pureza y química industrial"),
            ],
            "Fabrican los paneles": [
                ("FSLR", "First Solar", "El mayor fabricante de paneles de EE. UU."),
                ("JKS", "JinkoSolar (China)", "Uno de los mayores fabricantes de paneles del mundo"),
                ("CSIQ", "Canadian Solar", "Paneles, baterías y parques solares"),
            ],
            "Componentes (inversores y seguidores solares)": [
                ("ENPH", "Enphase", "Microinversores: convierten la electricidad de cada panel"),
                ("SEDG", "SolarEdge (Israel)", "Inversores y optimizadores para paneles"),
                ("NXT", "Nextracker", "Seguidores que orientan los paneles hacia el sol"),
                ("ARRY", "Array Technologies", "Seguidores solares para grandes parques"),
            ],
            f"Venden la energía e instalan {MARCA_FINAL}": [
                ("NEE", "NextEra Energy", "La mayor productora de energía solar y eólica de EE. UU."),
                ("RUN", "Sunrun", "Instala placas solares en casas"),
            ],
        },
    },
    "Coche eléctrico y baterías": {
        "idea": "Antes de la marca de coches están quien fabrica las baterías, quien extrae el litio y quien hace los "
                "chips de potencia que gestionan la energía del coche.",
        "eslabones": {
            "Materia prima (litio)": [
                ("ALB", "Albemarle", "El mayor productor de litio del mundo"),
                ("SQM", "SQM (Chile)", "Litio y otros minerales"),
            ],
            "Fabrican las baterías": [
                ("300750.SZ", "CATL (China)", "El mayor fabricante de baterías para coches del mundo"),
                ("373220.KS", "LG Energy Solution (Corea)", "Baterías para GM, Tesla, Hyundai…"),
                ("6752.T", "Panasonic (Japón)", "Baterías para Tesla, además de electrónica"),
            ],
            "Chips de potencia para coches": [
                ("ON", "onsemi", "Chips de potencia de carburo de silicio para coches eléctricos"),
                ("IFX.DE", "Infineon (Alemania)", "El mayor fabricante de chips para coches"),
                ("NXPI", "NXP (Países Bajos)", "Chips de control para coches"),
            ],
            f"Marcas de coches {MARCA_FINAL}": [
                ("TSLA", "Tesla", "Coches eléctricos, baterías y conducción autónoma"),
                ("1211.HK", "BYD (China)", "El mayor vendedor de coches eléctricos; también fabrica sus baterías"),
                ("RIVN", "Rivian", "Furgonetas y todoterrenos eléctricos"),
            ],
        },
    },
    "Medicamentos contra la obesidad": {
        "idea": "Los medicamentos tipo Ozempic se inyectan con plumas: antes de la farmacéutica están quien fabrica "
                "las plumas, viales y componentes para inyectables.",
        "eslabones": {
            "Plumas y componentes para inyectables": [
                ("WST", "West Pharmaceutical", "Tapones, viales y componentes para medicamentos inyectables"),
                ("BDX", "Becton Dickinson", "Jeringas, agujas y plumas de inyección"),
                ("YPSN.SW", "Ypsomed (Suiza)", "Plumas y autoinyectores para farmacéuticas"),
            ],
            f"Fabrican el medicamento {MARCA_FINAL}": [
                ("NVO", "Novo Nordisk (Dinamarca)", "Ozempic y Wegovy"),
                ("LLY", "Eli Lilly", "Mounjaro y Zepbound"),
            ],
        },
    },
    "Otras grandes empresas": {
        "idea": "Grandes empresas conocidas que no encajan en una sola cadena.",
        "eslabones": {
            "Empresas": [
                ("AAPL", "Apple", "iPhone, Mac y servicios; sus chips los fabrica TSMC"),
                ("NFLX", "Netflix", "Plataforma de series y películas"),
                ("MC.PA", "LVMH (Francia)", "Lujo: Louis Vuitton, Dior, Moët…"),
                ("SAP", "SAP (Alemania)", "Software de gestión para empresas"),
            ],
        },
    },
    "Salidas a bolsa recientes": {
        "idea": "Empresas que llevan poco tiempo en bolsa: más potencial, pero también más riesgo y poco historial.",
        "eslabones": {
            "Recién salidas a bolsa": [
                ("CRWV", "CoreWeave", "Nube especializada en IA, construida con chips de NVIDIA"),
                ("CRCL", "Circle", "Emite USDC, una criptomoneda estable ligada al dólar"),
                ("RDDT", "Reddit", "Red social de foros; vende sus datos para entrenar IA"),
                ("FIG", "Figma", "Programa de diseño de apps y webs"),
                ("KLAR", "Klarna (Suecia)", "Pagos aplazados al comprar online"),
            ],
        },
    },
}
# temática -> [(ticker, nombre, papel, eslabón)] y ticker -> (nombre, papel, temática, eslabón)
UNIVERSO = {tema: [(t, n, p, eslabon) for eslabon, lista in c["eslabones"].items() for t, n, p in lista]
            for tema, c in CADENAS.items()}
PAPEL = {t: (n, p, tema, eslabon) for tema, lista in UNIVERSO.items() for t, n, p, eslabon in lista}

RECOMENDACION = {"strong_buy": "Compra fuerte", "buy": "Comprar", "hold": "Mantener",
                 "underperform": "Peor que el mercado", "sell": "Vender", "none": "—"}


# ----------------------------------------------------------------------------- descarga
def descargar_empresa(ticker: str) -> dict:
    """Datos crudos de Yahoo Finance (o de prueba con ANALISTA_DEMO=1). Cada parte puede faltar."""
    if os.environ.get("ANALISTA_DEMO") == "1":
        return _datos_prueba(ticker)
    import yfinance as yf

    t = yf.Ticker(ticker)
    datos = {"ticker": ticker, "info": {}, "precios": pd.Series(dtype=float), "resultados": pd.DataFrame(),
             "noticias": [], "errores": []}
    for parte, funcion in (("info", lambda: t.get_info() or {}),
                           ("precios", lambda: t.history(period="5y", interval="1d", auto_adjust=True)["Close"]),
                           ("resultados", lambda: _resultados(t)),
                           ("noticias", lambda: _noticias(t))):
        try:
            datos[parte] = funcion()
        except Exception as e:  # una parte que falla no debe tumbar el resto
            datos["errores"].append(f"{parte}: {type(e).__name__}")
    if len(datos["precios"]):
        # fecha local de cada sesión (en Hong Kong o París la medianoche local es el día anterior en UTC)
        datos["precios"].index = pd.DatetimeIndex([d.date() for d in datos["precios"].index]).tz_localize("UTC")
    return datos


def descargar_referencia() -> pd.Series:
    return descargar_empresa(REFERENCIA)["precios"]


def _resultados(t) -> pd.DataFrame:
    """Informes trimestrales: fecha, beneficio por acción esperado y real, sorpresa (%)."""
    df = t.get_earnings_dates(limit=28)
    if df is None or df.empty:
        return pd.DataFrame(columns=["estimado", "real", "sorpresa"])
    df = df.rename(columns={"EPS Estimate": "estimado", "Reported EPS": "real", "Surprise(%)": "sorpresa"})
    df.index = pd.to_datetime(df.index, utc=True)
    return df[["estimado", "real", "sorpresa"]].sort_index()


def _noticias(t, maximo: int = 8) -> list[dict]:
    salida = []
    for n in (t.get_news(count=maximo) or [])[:maximo]:
        c = n.get("content", n)
        enlace = (c.get("canonicalUrl") or {}).get("url") or (c.get("clickThroughUrl") or {}).get("url") or c.get("link")
        salida.append({"titulo": c.get("title", ""), "fuente": (c.get("provider") or {}).get("displayName", c.get("publisher", "")),
                       "fecha": c.get("pubDate") or c.get("providerPublishTime"), "enlace": enlace})
    return [n for n in salida if n["titulo"]]


def _datos_prueba(ticker: str) -> dict:
    """Datos inventados y reproducibles para probar la pantalla sin conexión."""
    rng = np.random.default_rng(zlib.crc32(ticker.encode()))
    fechas = pd.bdate_range(end=pd.Timestamp.now(tz="UTC").normalize(), periods=1260)
    precios = pd.Series(100 * np.exp(np.cumsum(rng.normal(0.0004, 0.02, len(fechas)))), index=fechas)
    trimestres = pd.date_range(end=fechas[-1] + pd.Timedelta(days=45), periods=21, freq="91D", tz="UTC")
    estimado = np.abs(rng.normal(1.5, 0.3, len(trimestres)))
    real = estimado * (1 + rng.normal(0.03, 0.08, len(trimestres)))
    resultados = pd.DataFrame({"estimado": estimado, "real": real, "sorpresa": (real / estimado - 1) * 100},
                              index=trimestres)
    resultados.iloc[-1, 1:] = np.nan  # el próximo informe aún no se ha publicado
    nombre = PAPEL.get(ticker, (ticker,))[0]
    info = {"longName": nombre, "sector": "Technology", "industry": "Semiconductors", "country": "United States",
            "currency": "USD", "marketCap": float(rng.uniform(5e10, 3e12)), "currentPrice": float(precios.iloc[-1]),
            "trailingPE": float(rng.uniform(10, 70)), "forwardPE": float(rng.uniform(10, 50)),
            "revenueGrowth": float(rng.normal(0.12, 0.2)), "earningsGrowth": float(rng.normal(0.1, 0.3)),
            "profitMargins": float(rng.normal(0.18, 0.15)), "operatingMargins": float(rng.normal(0.22, 0.15)),
            "debtToEquity": float(rng.uniform(5, 250)), "freeCashflow": float(rng.normal(5e9, 8e9)),
            "recommendationKey": "buy", "numberOfAnalystOpinions": int(rng.integers(5, 60)),
            "targetMeanPrice": float(precios.iloc[-1] * rng.uniform(0.85, 1.35)),
            "firstTradeDateEpochUtc": int(pd.Timestamp("2025-03-28").timestamp()) if ticker == "CRWV" else 0,
            "longBusinessSummary": f"{nombre} (datos de prueba)."}
    noticias = [{"titulo": f"Noticia de prueba {i + 1} sobre {nombre}", "fuente": "Prueba",
                 "fecha": (fechas[-1] - pd.Timedelta(days=i)).isoformat(), "enlace": "https://finance.yahoo.com"}
                for i in range(3)]
    return {"ticker": ticker, "info": info, "precios": precios, "resultados": resultados, "noticias": noticias,
            "errores": []}


# ----------------------------------------------------------------------------- análisis
def rentabilidades(precios: pd.Series, referencia: pd.Series) -> pd.DataFrame:
    """Rentabilidad de la acción y del S&P 500 a 1, 3 y 5 años (anualizada a 3 y 5)."""
    filas = []
    for anos in (1, 3, 5):
        desde = precios.index[-1] - pd.DateOffset(years=anos)
        if precios.index[0] > desde + pd.Timedelta(days=10):
            continue
        p, r = precios[precios.index >= desde], referencia[referencia.index >= desde]
        if len(p) < 2 or len(r) < 2:
            continue
        a = (p.iloc[-1] / p.iloc[0]) ** (1 / anos) - 1
        b = (r.iloc[-1] / r.iloc[0]) ** (1 / anos) - 1
        filas.append({"periodo": f"{anos} año" + ("s (al año)" if anos > 1 else ""), "empresa": a, "sp500": b})
    return pd.DataFrame(filas)


def caida_maxima(precios: pd.Series) -> float:
    return float((precios / precios.cummax() - 1).min()) if len(precios) else np.nan


def reaccion_a_resultados(precios: pd.Series, referencia: pd.Series, resultados: pd.DataFrame) -> dict:
    """📏 Qué hizo la acción frente al S&P 500 en las 20 sesiones siguientes a cada informe.

    Se empieza a contar al cierre de la primera sesión DESPUÉS del informe (cuando ya se conoce el
    resultado), así que no incluye el salto del propio día: es lo que habría ganado alguien que compra
    al enterarse."""
    pasados = resultados.dropna(subset=["sorpresa"]) if not resultados.empty else resultados
    filas = []
    for fecha, f in pasados.iterrows():
        despues = precios.index[precios.index > fecha.normalize()]
        if len(despues) <= DIAS_TRAS_RESULTADOS:
            continue
        d0, d1 = despues[0], despues[DIAS_TRAS_RESULTADOS]
        r0, r1 = referencia.asof(d0), referencia.asof(d1)  # bolsas con otros festivos: último cierre conocido
        if pd.isna(r0) or pd.isna(r1):
            continue
        exceso = (precios[d1] / precios[d0] - 1) - (r1 / r0 - 1)
        filas.append({"fecha": fecha, "sorpresa": f["sorpresa"], "exceso": exceso})
    df = pd.DataFrame(filas)
    salida = {}
    for nombre, mascara in (("bate", lambda d: d["sorpresa"] > 0), ("decepciona", lambda d: d["sorpresa"] < 0)):
        grupo = df[mascara(df)] if len(df) else df
        salida[nombre] = {"casos": len(grupo),
                          "exceso_medio": float(grupo["exceso"].mean()) if len(grupo) else np.nan,
                          "veces_mejor": int((grupo["exceso"] > 0).sum()) if len(grupo) else 0}
    salida["detalle"] = df
    return salida


def proximo_informe(resultados: pd.DataFrame):
    if resultados.empty:  # Yahoo no siempre tiene informes (salidas a bolsa recientes, algunas extranjeras)
        return None
    futuros = resultados[resultados["real"].isna() & (resultados.index > pd.Timestamp.now(tz="UTC"))]
    return futuros.index.min() if len(futuros) else None


def cotiza_desde(info: dict, precios: pd.Series):
    epoch = info.get("firstTradeDateEpochUtc") or info.get("firstTradeDateMilliseconds", 0) / 1000
    if epoch:
        return pd.Timestamp(epoch, unit="s", tz="UTC")
    return precios.index[0] if len(precios) else None


def evaluar(datos: dict, referencia: pd.Series) -> dict:
    """Puntos fuertes, puntos débiles y riesgos con umbrales fijos (orientativos), más lo medido."""
    info, precios, resultados = datos["info"], datos["precios"], datos["resultados"]
    fuertes, debiles, riesgos = [], [], []

    crec = info.get("revenueGrowth")
    if crec is not None:
        if crec >= 0.15:
            fuertes.append(f"Las ventas crecen rápido: {crec:+.0%} frente al año anterior")
        elif crec < 0:
            debiles.append(f"Las ventas bajan: {crec:+.0%} frente al año anterior")
    margen = info.get("profitMargins")
    if margen is not None:
        if margen >= 0.20:
            fuertes.append(f"Muy rentable: gana {margen:.0%} de cada euro que vende")
        elif margen < 0:
            debiles.append("Pierde dinero: gasta más de lo que ingresa")
    flujo = info.get("freeCashflow")
    if flujo is not None:
        (fuertes if flujo > 0 else debiles).append(
            "Genera dinero en efectivo después de invertir" if flujo > 0 else "Consume más efectivo del que genera")
    deuda = info.get("debtToEquity")
    if deuda is not None and deuda > 200:
        debiles.append(f"Mucha deuda: {deuda / 100:.1f} veces su patrimonio")
    per, per_futuro = info.get("trailingPE"), info.get("forwardPE")
    if per is None or per <= 0:
        riesgos.append("Sin beneficios positivos: su precio se apoya en expectativas de futuro")
    elif per > 50:
        riesgos.append(f"Muy cara: cotiza a {per:.0f} veces sus beneficios (el S&P 500 suele estar entre 15 y 25); "
                       "el precio ya descuenta mucho crecimiento")
    if per and per_futuro and 0 < per_futuro < per * 0.8:
        fuertes.append("Los analistas esperan que sus beneficios crezcan bastante el próximo año")

    caida = caida_maxima(precios)
    if caida < -0.5:
        riesgos.append(f"Muy volátil: en los últimos años llegó a caer un {abs(caida):.0%} desde máximos")
    desde = cotiza_desde(info, precios)
    if desde is not None and desde > pd.Timestamp.now(tz="UTC") - pd.DateOffset(years=ANOS_RECIENTE):
        riesgos.append(f"Salió a bolsa hace poco ({desde:%m/%Y}): hay poco historial para juzgarla")
    pais = info.get("country", "")
    if pais in ("China", "Hong Kong") or datos["ticker"].endswith(".HK"):
        riesgos.append("Empresa china: riesgo regulatorio y de tensiones comerciales con EE. UU.")
    elif pais == "Taiwan":
        riesgos.append("Taiwán: riesgo geopolítico por la tensión con China")

    rent = rentabilidades(precios, referencia) if len(precios) and len(referencia) else pd.DataFrame()
    largo = rent.iloc[-1] if len(rent) else None
    if largo is not None:
        (fuertes if largo["empresa"] > largo["sp500"] else debiles).append(
            f"En {largo['periodo']} ha {'ganado' if largo['empresa'] > largo['sp500'] else 'quedado por detrás'} "
            f"al S&P 500 ({largo['empresa']:+.0%} frente a {largo['sp500']:+.0%})")

    pasados = resultados.dropna(subset=["sorpresa"]).tail(8)
    if len(pasados) >= 4:
        batidos = int((pasados["sorpresa"] > 0).sum())
        texto = f"Batió las previsiones de beneficio en {batidos} de sus últimos {len(pasados)} informes"
        if batidos >= 0.75 * len(pasados):
            fuertes.append(texto)
        elif batidos <= len(pasados) / 2:
            debiles.append(texto)

    return {"fuertes": fuertes, "debiles": debiles, "riesgos": riesgos, "rentabilidades": rent,
            "caida_maxima": caida, "cotiza_desde": desde, "proximo_informe": proximo_informe(resultados),
            "reaccion": reaccion_a_resultados(precios, referencia, resultados) if len(referencia) else None}


def fila_comparacion(ticker: str, datos: dict, referencia: pd.Series) -> dict:
    """Resumen de una empresa para la tabla de una temática."""
    info, precios = datos["info"], datos["precios"]
    nombre, papel, _, eslabon = PAPEL.get(ticker, (info.get("longName", ticker), "", "", ""))
    rent = rentabilidades(precios, referencia) if len(precios) and len(referencia) else pd.DataFrame()
    uno = rent[rent["periodo"] == "1 año"]
    return {
        "Eslabón": eslabon.replace(MARCA_FINAL, "").strip(), "Empresa": nombre, "Papel": papel,
        "Ventas (crec.)": info.get("revenueGrowth"), "Margen": info.get("profitMargins"),
        "PER": info.get("trailingPE"),
        "1 año": float(uno["empresa"].iat[0]) if len(uno) else np.nan,
        "S&P 500 (1 año)": float(uno["sp500"].iat[0]) if len(uno) else np.nan,
        "Analistas": RECOMENDACION.get(info.get("recommendationKey", "none"), "—"),
    }


def rendimiento_cadena(tema: str, datos_de, referencia: pd.Series) -> pd.DataFrame:
    """📏 Rentabilidad media anual de cada eslabón (sus empresas a partes iguales) frente al S&P 500.

    Ojo con el sesgo de supervivencia: las empresas se eligieron hoy, sabiendo cuáles son las grandes de cada
    sector; las que quebraron o se hundieron por el camino no están, así que el pasado sale mejor de lo que fue."""
    filas = []
    for eslabon, lista in CADENAS[tema]["eslabones"].items():
        por_periodo = {}
        for ticker, *_ in lista:
            precios = datos_de(ticker)["precios"]
            if not len(precios):
                continue
            for _, r in rentabilidades(precios, referencia).iterrows():
                por_periodo.setdefault(r["periodo"], []).append(r["empresa"])
        fila = {"Eslabón": eslabon, "marca_final": MARCA_FINAL in eslabon}
        for periodo, valores in por_periodo.items():
            fila[periodo] = float(np.mean(valores))
            fila[f"n {periodo}"] = len(valores)
        filas.append(fila)
    sp = {"Eslabón": "S&P 500 (referencia)", "marca_final": False}
    for _, r in rentabilidades(referencia, referencia).iterrows():
        sp[r["periodo"]] = r["sp500"]
    return pd.DataFrame([*filas, sp])
