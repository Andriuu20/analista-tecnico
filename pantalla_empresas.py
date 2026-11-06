"""Pantalla de la sección «Análisis de inversión» (largo plazo). La lógica está en empresas.py."""
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from empresas import (CADENAS, MARCA_FINAL, PAPEL, RECOMENDACION, REFERENCIA, UNIVERSO, descargar_empresa, evaluar,
                      fila_comparacion, rendimiento_cadena)

OTRA = "🔎 Otra empresa (escribir)"
TODA = "🔗 Ver la cadena completa"
TIPOS = {"EQUITY": "acción", "ETF": "fondo cotizado (ETF)"}


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def datos(ticker: str) -> dict:
    return descargar_empresa(ticker)


def _pct(x, signo=False) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return (f"{x * 100:+.1f} %" if signo else f"{x * 100:.1f} %").replace(".", ",")


def _dinero(x, moneda="USD") -> str:
    if not x:
        return "—"
    for limite, sufijo in ((1e12, " billones"), (1e9, " mil millones"), (1e6, " millones")):
        if abs(x) >= limite:
            return f"{x / limite:.1f}{sufijo} {moneda}".replace(".", ",")
    return f"{x:,.2f} {moneda}"


def _lista(titulo: str, elementos: list[str], vacio: str) -> None:
    st.markdown(f"**{titulo}**\n" + "\n".join(f"- {e}" for e in (elementos or [vacio])))


def _grafico(precios: pd.Series, referencia: pd.Series, nombre: str) -> go.Figure:
    """Evolución de 100 € invertidos en la empresa y en el S&P 500."""
    desde = max(precios.index[0], referencia.index[0])
    p, r = precios[precios.index >= desde], referencia[referencia.index >= desde]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=p.index, y=100 * p / p.iloc[0], name=nombre, line=dict(color="#26a69a", width=2)))
    fig.add_trace(go.Scatter(x=r.index, y=100 * r / r.iloc[0], name="S&P 500", line=dict(color="#8a8f98", width=1.5)))
    fig.update_layout(height=320, margin=dict(l=10, r=10, t=30, b=10), hovermode="x unified",
                      legend=dict(orientation="h", y=1.12, x=0), yaxis_title="100 € invertidos")
    return fig


def ficha(ticker: str, referencia: pd.Series) -> None:
    d = datos(ticker)
    info = d["info"]
    if not info and not len(d["precios"]):
        st.error(f"No se encontraron datos de «{ticker}» en Yahoo Finance. Revisa el símbolo (p. ej. NVDA, ASML, "
                 "SAP.DE, 0700.HK).")
        return
    nombre, papel, tema, eslabon = PAPEL.get(ticker, (info.get("longName") or ticker, "", "", ""))
    e = evaluar(d, referencia)
    moneda = info.get("currency", "")

    with st.container(border=True):
        st.markdown(f"### {nombre}")
        st.caption(" · ".join(x for x in (ticker, info.get("sector"), info.get("country"),
                                          TIPOS.get(info.get("quoteType"), "")) if x))
        if papel:
            st.markdown(f"🔗 **En la cadena ({eslabon.replace(MARCA_FINAL, '').strip().lower()}):** {papel}")
        precio = info.get("currentPrice") or (float(d["precios"].iloc[-1]) if len(d["precios"]) else None)
        c1, c2 = st.columns(2)
        c1.metric("Precio", f"{precio:.2f} {moneda}".replace(".", ",") if precio else "—")
        c2.metric("Tamaño (capitalización)", _dinero(info.get("marketCap"), moneda))
        if e["proximo_informe"] is not None:
            st.markdown(f"📅 **Próximo informe de resultados:** {e['proximo_informe']:%d/%m/%Y}")
        if e["cotiza_desde"] is not None:
            st.caption(f"Cotiza en bolsa desde {e['cotiza_desde']:%m/%Y}")

    _lista("✅ Puntos fuertes", e["fuertes"], "Nada destacable con los datos disponibles")
    _lista("⚠️ Puntos débiles", e["debiles"], "Nada destacable con los datos disponibles")
    _lista("🚩 Riesgos", e["riesgos"], "Ninguno especial con los datos disponibles")
    st.caption("Referencias orientativas con umbrales fijos (por ejemplo, «crecimiento rápido» = ventas +15 % o "
               "más). No es una recomendación de compra.")

    with st.expander("📏 ¿Qué pasa después de sus informes trimestrales?"):
        r = e["reaccion"]
        if not r or (r["bate"]["casos"] + r["decepciona"]["casos"]) == 0:
            st.write("No hay suficientes informes con precio posterior para medirlo.")
        else:
            st.write(f"Qué hizo la acción frente al S&P 500 en las {20} sesiones siguientes a cada informe, "
                     "contando desde el día después (cuando ya se sabe el resultado):")
            for clave, texto in (("bate", "Cuando batió las previsiones"), ("decepciona", "Cuando decepcionó")):
                g = r[clave]
                if g["casos"]:
                    st.markdown(f"- **{texto}** ({g['casos']} veces): de media {_pct(g['exceso_medio'], True)} frente "
                                f"al S&P 500; mejor que el índice {g['veces_mejor']} de {g['casos']} veces")
            st.caption("Con tan pocos informes (unos 4 al año) esto puede ser casualidad: tómalo como una pista, no "
                       "como una regla.")

    with st.expander("📈 Rentabilidad frente al S&P 500"):
        if len(d["precios"]) and len(referencia):
            st.plotly_chart(_grafico(d["precios"], referencia, nombre), width="stretch",
                            config={"displayModeBar": False}, key=f"rent_{ticker}")
        if len(e["rentabilidades"]):
            st.dataframe(pd.DataFrame({"Periodo": e["rentabilidades"]["periodo"],
                                       nombre: e["rentabilidades"]["empresa"].map(lambda x: _pct(x, True)),
                                       "S&P 500": e["rentabilidades"]["sp500"].map(lambda x: _pct(x, True))}),
                         hide_index=True, width="stretch")
        st.caption(f"Peor caída desde máximos en este periodo: {_pct(e['caida_maxima'])}. "
                   "Rentabilidades pasadas no garantizan las futuras.")

    with st.expander("🧾 Números del negocio"):
        filas = [("Crecimiento de ventas (anual)", _pct(info.get("revenueGrowth"), True)),
                 ("Crecimiento de beneficios (anual)", _pct(info.get("earningsGrowth"), True)),
                 ("Margen de beneficio", _pct(info.get("profitMargins"))),
                 ("Margen operativo", _pct(info.get("operatingMargins"))),
                 ("Flujo de caja libre", _dinero(info.get("freeCashflow"), moneda)),
                 ("Deuda / patrimonio", f"{info['debtToEquity'] / 100:.2f}".replace(".", ",") if info.get("debtToEquity") else "—"),
                 ("PER (precio / beneficios)", f"{info['trailingPE']:.1f}".replace(".", ",") if info.get("trailingPE") else "—"),
                 ("PER esperado próximo año", f"{info['forwardPE']:.1f}".replace(".", ",") if info.get("forwardPE") else "—")]
        st.dataframe(pd.DataFrame(filas, columns=["Dato", "Valor"]), hide_index=True, width="stretch")
        res = d["resultados"].dropna(subset=["sorpresa"]).tail(8).iloc[::-1]
        if len(res):
            st.markdown("**Últimos informes trimestrales** (beneficio por acción)")
            st.dataframe(pd.DataFrame({
                "Fecha": res.index.strftime("%d/%m/%Y"), "Esperado": res["estimado"].round(2),
                "Real": res["real"].round(2),
                "Sorpresa": res["sorpresa"].map(lambda x: f"{'✅' if x > 0 else '❌'} {x:+.1f} %".replace(".", ","))}),
                hide_index=True, width="stretch")

    with st.expander("👥 Qué opinan los analistas"):
        n = info.get("numberOfAnalystOpinions")
        objetivo, precio = info.get("targetMeanPrice"), info.get("currentPrice")
        if not n:
            st.write("Yahoo no tiene opiniones de analistas para esta empresa.")
        else:
            st.markdown(f"- Consenso de **{n} analistas**: **{RECOMENDACION.get(info.get('recommendationKey', 'none'), '—')}**")
            if objetivo and precio:
                st.markdown(f"- Precio objetivo medio: **{objetivo:.2f} {moneda}**".replace(".", ",") +
                            f" ({_pct(objetivo / precio - 1, True)} "
                            "sobre el precio actual)")
            st.caption("Ojo: los analistas tienden a ser optimistas y rara vez dicen «vender».")

    with st.expander("📰 Noticias recientes"):
        if not d["noticias"]:
            st.write("No hay noticias recientes en Yahoo Finance.")
        for n in d["noticias"]:
            fecha = pd.to_datetime(n["fecha"], utc=True, errors="coerce", unit="s" if isinstance(n["fecha"], (int, float)) else None)
            fecha_txt = f" · {fecha:%d/%m}" if pd.notna(fecha) else ""
            enlace = f"[{n['titulo']}]({n['enlace']})" if n["enlace"] else n["titulo"]
            st.markdown(f"- {enlace}  \n  <small>{n['fuente']}{fecha_txt}</small>", unsafe_allow_html=True)
        st.caption("Titulares tal cual los publica Yahoo Finance (normalmente en inglés). Cuando una noticia llega a "
                   "nosotros, el precio suele haberla tenido ya en cuenta.")
    if info.get("longBusinessSummary"):
        with st.expander("ℹ️ A qué se dedica (descripción de Yahoo, en inglés)"):
            st.write(info["longBusinessSummary"])
    if d["errores"]:
        st.caption("No se pudieron cargar algunos datos: " + ", ".join(d["errores"]))


def comparar(tema: str, referencia: pd.Series) -> None:
    """La cadena completa: cómo le ha ido a cada eslabón (medido) y la tabla de sus empresas."""
    lista = UNIVERSO[tema]
    barra = st.progress(0.0, "Cargando empresas…")
    for i, (ticker, nombre, *_) in enumerate(lista):
        barra.progress((i + 1) / len(lista), f"Cargando {nombre}…")
        datos(ticker)
    barra.empty()
    st.markdown(f"**{tema}.** {CADENAS[tema]['idea']}")

    rend = rendimiento_cadena(tema, datos, referencia)
    if len(CADENAS[tema]["eslabones"]) > 1:
        st.markdown("📏 **¿Qué eslabón ha rendido más?** Rentabilidad media de sus empresas, al año")
        periodos = [p for p in ("1 año", "3 años (al año)", "5 años (al año)") if p in rend]
        tabla = pd.DataFrame({"Eslabón": rend["Eslabón"].str.replace(MARCA_FINAL, "(marca final)", regex=False)})
        for p in periodos:
            tabla[p] = [f"{_pct(v, True)} ({int(n)})" if pd.notna(n) else _pct(v, True)
                        for v, n in zip(rend[p], rend.get(f"n {p}", pd.Series([np.nan] * len(rend))))]
        st.dataframe(tabla, hide_index=True, width="stretch")
        st.caption("Entre paréntesis, cuántas empresas tienen datos de ese periodo. ⚠️ Sesgo de supervivencia: "
                   "estas empresas se han elegido hoy, sabiendo cuáles son las grandes de cada sector; las que "
                   "quebraron por el camino no están, así que el pasado sale mejor de lo que fue. Úsalo para "
                   "comparar eslabones entre sí, no como promesa de rentabilidad.")

    df = pd.DataFrame([fila_comparacion(t, datos(t), referencia) for t, *_ in lista])
    for col in ("Ventas (crec.)", "1 año", "S&P 500 (1 año)"):
        df[col] = df[col].map(lambda x: _pct(x, True))
    df["Margen"] = df["Margen"].map(_pct)
    df["PER"] = df["PER"].map(lambda x: "—" if x is None or pd.isna(x) else f"{x:.0f}")
    st.dataframe(df.drop(columns=["Papel"]), hide_index=True, width="stretch")
    st.caption("PER = cuántas veces sus beneficios anuales cuesta la empresa (el S&P 500 suele estar entre 15 y 25). "
               "Elige una empresa en «¿Qué empresa?» para ver su ficha completa.")


def mostrar() -> None:
    st.caption("Análisis con datos de Yahoo Finance para invertir a largo plazo, organizado por cadenas: de la materia "
               "prima a la marca final («picos y palas»: invertir en los proveedores de una tendencia, no solo en la "
               "marca famosa). No es una recomendación de compra: muestra lo que hace bien y mal cada empresa y la "
               "compara con el S&P 500.")
    tema = st.selectbox("Temática", [*UNIVERSO, OTRA])
    if tema == OTRA:
        ticker = st.text_input("Símbolo de Yahoo Finance (p. ej. NVDA, ASML, SAP.DE, 0700.HK)").strip().upper()
    else:
        nombres = {f"{n} · {e.replace(MARCA_FINAL, '(marca final)').lower()}": t for t, n, _, e in UNIVERSO[tema]}
        eleccion = st.selectbox("¿Qué empresa?", [TODA, *nombres])
        ticker = None if eleccion == TODA else nombres[eleccion]
    if st.button("Analizar", type="primary", width="stretch", key="analizar_empresa", disabled=tema == OTRA and not ticker):
        st.session_state.empresa = (tema, ticker)
    elegido = st.session_state.get("empresa")
    if not elegido:
        return
    tema, ticker = elegido
    with st.spinner("Descargando datos…"):
        referencia = datos(REFERENCIA)["precios"]
    if ticker:
        ficha(ticker, referencia)
    else:
        comparar(tema, referencia)
