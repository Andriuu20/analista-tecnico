"""Analista técnico: eliges un mercado, pulsas Analizar y te dice comprar o vender y a qué plazo."""
import numpy as np
import pandas as pd
import streamlit as st

from backtest import backtest
from datos import ACTIVOS, INTERVALOS, MINUTOS, activo_personalizado, descargar
from estrategias import ESTRATEGIAS, calcular
from graficos import grafico
from registro import Almacen, anadir, estadisticas_vivo, nueva_entrada, resolver
from senal import UMBRAL_RENTABLE, Z_SIGNIFICATIVO, generar, texto_plazo

ZONA = "Europe/Madrid"
TODOS = "🔍 Buscar en todos"
OTRO = "✏️ Otro símbolo…"
# temporalidades que se analizan solas; cada una se confirma con la tendencia de la siguiente
TEMPORALIDADES = ["5m", "15m", "1h", "4h", "1d"]
SUPERIOR = {"5m": "15m", "15m": "1h", "1h": "4h", "4h": "1d", "1d": None}
# preferencia de plazo -> (mínimo, máximo) en minutos de la operación
PLAZOS = {"Cualquiera": (0, 10**9), "Minutos": (0, 59), "Horas": (60, 1439), "Días": (1440, 10**9)}
MAX_VELAS = 8000
NOMBRE_VELA = {c: e for e, (c, _) in INTERVALOS.items()}

st.set_page_config(page_title="Analista técnico", page_icon="📈", layout="centered")


def secreto(nombre: str):
    try:
        return st.secrets.get(nombre)
    except Exception:  # no hay archivo de secretos
        return None


# --- Acceso con contraseña (opcional, si se define APP_CLAVE en los secretos) ---
clave = secreto("APP_CLAVE")
if clave and not st.session_state.get("dentro"):
    st.title("📈 Analista técnico")
    intento = st.text_input("Contraseña", type="password")
    if intento == clave:
        st.session_state.dentro = True
        st.rerun()
    elif intento:
        st.error("Contraseña incorrecta")
    st.stop()


@st.cache_data(ttl=60, show_spinner=False)
def cargar_velas(fuente: str, simbolo: str, codigo: str):
    return descargar(fuente, simbolo, codigo)


@st.cache_data(ttl=60, show_spinner=False)
def analizar(fuente: str, simbolo: str, codigo: str, coste: float):
    df, origen = cargar_velas(fuente, simbolo, codigo)
    df = df.iloc[-MAX_VELAS:]
    if len(df) < 300:
        raise ValueError(f"solo hay {len(df)} velas; hacen falta al menos 300")
    ind, senales, contexto = calcular(df)
    bt = backtest(df["Close"].to_numpy(), senales, coste)
    return df, origen, ind, senales, contexto, bt


def fmt_precio(p) -> str:
    if p is None or (isinstance(p, float) and np.isnan(p)):
        return "—"
    return f"{p:,.2f}" if p >= 1000 else f"{p:.3f}" if p >= 10 else f"{p:.5f}"


def hora_local(ts, formato="%d/%m %H:%M") -> str:
    return pd.Timestamp(ts).tz_convert(ZONA).strftime(formato)


def texto_vencimiento(vence: pd.Timestamp, duracion_min: int) -> str:
    if pd.Timestamp(vence).tz_convert(ZONA).date() == pd.Timestamp.now(tz=ZONA).date():
        return f"a las <b>{hora_local(vence, '%H:%M')}</b>"
    aprox = " (aprox.)" if duracion_min >= 1440 else ""  # en forex los fines de semana no cuentan
    return f"el <b>{hora_local(vence, '%d/%m %H:%M')}</b>{aprox}"


# --- Registro en vivo (se comprueba solo cada vez que se abre la app) ---
almacen = Almacen(secreto("GITHUB_TOKEN"), secreto("GIST_ID"))
if "registro" not in st.session_state:
    try:
        st.session_state.registro = almacen.cargar()
    except Exception as e:
        st.session_state.registro = []
        st.warning(f"No se pudo cargar el registro: {e}")
registro = st.session_state.registro


def guardar_registro():
    try:
        almacen.guardar(registro)
    except Exception as e:
        st.warning(f"No se pudo guardar el registro: {e}")


if resolver(registro, cargar_velas):
    guardar_registro()


def analizar_mercado(nombre: str, cfg: dict, plazo: str = "Cualquiera") -> dict:
    """Analiza todas las temporalidades y se queda con la mejor señal confirmada del plazo pedido."""
    por_tf = {}
    for codigo in TEMPORALIDADES:
        try:
            df, origen, ind, senales, contexto, bt = analizar(cfg["fuente"], cfg["simbolo"], codigo, cfg["coste"])
        except Exception as e:
            por_tf[codigo] = {"error": str(e)}
            continue
        senal = generar(senales, bt, estadisticas_vivo(registro, cfg["simbolo"], codigo), MINUTOS[codigo])
        por_tf[codigo] = {"df": df, "origen": origen, "ind": ind, "contexto": contexto, "bt": bt, "senal": senal}

    # confirmación: no ir contra la tendencia de la temporalidad superior
    for codigo, r in por_tf.items():
        if "error" in r or not r["senal"]["direccion"]:
            continue
        sup = por_tf.get(SUPERIOR[codigo]) or r
        tendencia = (sup if "error" not in sup else r)["contexto"]["tendencia"]
        contraria = "Bajista" if r["senal"]["direccion"] == 1 else "Alcista"
        if tendencia == contraria:
            r["senal"] = {**r["senal"], "accion": "ESPERAR", "direccion": 0,
                          "motivo": f"La señal iba contra la tendencia {tendencia.lower()} de mayor plazo."}

    validos = [c for c, r in por_tf.items() if "error" not in r]
    if not validos:
        raise ValueError(next(iter(por_tf.values()))["error"])
    minimo, maximo = PLAZOS[plazo]
    con_senal = [c for c in validos if por_tf[c]["senal"]["direccion"]
                 and minimo <= por_tf[c]["senal"]["horizonte"] * MINUTOS[c] <= maximo]
    mejor = max(con_senal, key=lambda c: por_tf[c]["senal"]["confianza"]) if con_senal else None
    return {"nombre": nombre, "cfg": cfg, "por_tf": por_tf, "mejor": mejor,
            "principal": mejor or ("15m" if "15m" in validos else validos[0])}


def registrar(a: dict) -> None:
    if not a["mejor"]:
        return
    r = a["por_tf"][a["mejor"]]
    entrada = nueva_entrada(a["nombre"], a["cfg"], a["mejor"], r["df"].index[-1],
                            float(r["df"]["Close"].iat[-1]), r["senal"])
    if anadir(registro, entrada):
        guardar_registro()


def tarjeta(a: dict, compacta: bool = False) -> None:
    """El resultado principal: COMPRAR / VENDER / ESPERAR y durante cuánto tiempo."""
    with st.container(border=True):
        if not a["mejor"]:
            st.markdown(f"**{a['nombre']}**")
            st.markdown("<div style='font-size:2.6rem;font-weight:800;color:#8a8f98'>⏸️ ESPERAR</div>",
                        unsafe_allow_html=True)
            st.write("Ahora no hay una oportunidad clara. Mejor no entrar.")
            st.caption("Vuelve a analizar en 5-15 minutos o prueba «Buscar en todos».")
            return
        r = a["por_tf"][a["mejor"]]
        s, df = r["senal"], r["df"]
        compra = s["direccion"] == 1
        color = "#26a69a" if compra else "#ef5350"
        minutos = MINUTOS[a["mejor"]]
        vence = df.index[-1] + pd.Timedelta(minutes=minutos * (s["horizonte"] + 1))
        st.markdown(f"**{a['nombre']}**")
        st.markdown(
            f"<div style='font-size:2.6rem;font-weight:800;color:{color};line-height:1.1'>"
            f"{'⬆️ COMPRAR' if compra else '⬇️ VENDER'}</div>"
            f"<div style='font-size:1.6rem;font-weight:600;margin:.2rem 0 .6rem'>⏱️ {s['plazo']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(f"<div style='font-size:1.15rem'>Confianza <b>{s['confianza'] * 100:.0f} %</b> · "
                    f"Vence {texto_vencimiento(vence, minutos * s['horizonte'])}</div>", unsafe_allow_html=True)
        if not compacta:
            st.caption(f"Precio de entrada {fmt_precio(float(df['Close'].iat[-1]))} · "
                       f"analizado con velas de {NOMBRE_VELA[a['mejor']]}")
        if s["confianza"] < UMBRAL_RENTABLE:
            st.warning("Confianza baja (menos del 55 %): solo para practicar, no con dinero real.")


def detalles(a: dict) -> None:
    r = a["por_tf"][a["principal"]]
    minutos = MINUTOS[a["principal"]]

    with st.expander("🔎 ¿Por qué?"):
        filas = []
        for codigo in TEMPORALIDADES:
            x = a["por_tf"].get(codigo, {})
            if "error" in x:
                filas.append({"Velas": NOMBRE_VELA[codigo], "Resultado": "sin datos", "Plazo": "—", "Confianza": "—"})
                continue
            s = x["senal"]
            filas.append({"Velas": NOMBRE_VELA[codigo], "Resultado": s["accion"].capitalize(),
                          "Plazo": s["plazo"] if s["direccion"] else "—",
                          "Confianza": f"{s['confianza'] * 100:.0f} %" if s["direccion"] else "—"})
        st.dataframe(pd.DataFrame(filas), hide_index=True, width="stretch")
        ctx = r["contexto"]
        st.markdown(
            f"- Tendencia: **{ctx['tendencia']}** · RSI: **{ctx['rsi']:.0f}**\n"
            f"- Soporte: **{fmt_precio(ctx['soporte'])}** · Resistencia: **{fmt_precio(ctx['resistencia'])}**\n"
            f"- Patrón de vela: **{ctx['patron'] or 'ninguno'}**"
        )
        votos = r["senal"]["votos"]
        if votos:
            st.markdown(f"**Estrategias que se activaron (velas de {NOMBRE_VELA[a['principal']]}):**")
            for v in votos:
                marca = "✅" if v["valida"] else "❌"
                dice = "comprar" if v["direccion"] == 1 else "vender"
                extra = "" if v["valida"] else f" — no cuenta: {v['motivo']}"
                st.markdown(f"{marca} {v['descripcion']}: dice **{dice}**{extra}")
        if r["senal"]["motivo"]:
            st.caption(r["senal"]["motivo"])

    with st.expander("📊 Gráfico"):
        st.plotly_chart(
            grafico(r["df"], r["ind"], r["contexto"], r["senal"],
                    cierra_fines_de_semana=a["cfg"]["fuente"] == "yahoo", velas=90),
            width="stretch", config={"displayModeBar": False},
        )
        st.caption(f"Velas de {NOMBRE_VELA[a['principal']]}. Punteadas: verde = soportes, roja = resistencias. "
                   "Grises: Fibonacci.")

    with st.expander("🧪 Acierto en el histórico (backtest)"):
        bt = r["bt"]

        def celda(f):
            if f["senales"] == 0:
                return "—"
            z = (f["acierto"] - 0.5) / (0.5 / np.sqrt(f["senales"]))
            marca = "🟢" if f["acierto"] >= 0.55 and z >= Z_SIGNIFICATIVO else "🟡" if f["acierto"] >= 0.52 else "⚪"
            return f"{marca} {f['acierto'] * 100:.0f} %"

        tabla = bt.assign(celda=bt.apply(celda, axis=1)).pivot(index="estrategia", columns="horizonte",
                                                                values="celda")
        tabla.columns = [texto_plazo(h * minutos) for h in tabla.columns]
        tabla.index = [e.capitalize() for e in tabla.index]
        st.dataframe(tabla, width="stretch")
        st.caption(f"Velas de {NOMBRE_VELA[a['principal']]}, {len(r['df'])} velas de histórico. "
                   "🟢 ≥ 55 % y claramente mejor que el azar · 🟡 > 52 % · ⚪ azar.")


def mis_resultados() -> None:
    with st.expander("📒 Mis resultados"):
        if not almacen.remoto:
            st.caption("⚠️ Sin configurar el Gist (ver README), el registro puede borrarse al reiniciar la app.")
        if not registro:
            st.write("Aún no hay señales. Cada COMPRAR o VENDER se guarda solo y se comprueba al vencer.")
            return
        reg = pd.DataFrame(registro)
        resueltas = reg[reg["resultado"].isin(["acierto", "fallo"])]
        n_ok = int((resueltas["resultado"] == "acierto").sum())
        c1, c2, c3 = st.columns(3)
        c1.metric("Señales", len(reg))
        c2.metric("Pendientes", int((reg["resultado"] == "pendiente").sum()))
        c3.metric("Acierto real", f"{n_ok / len(resueltas) * 100:.0f} %" if len(resueltas) else "—")
        if len(resueltas) < 100:
            st.caption(f"{len(resueltas)} de 100 señales comprobadas necesarias para fiarse del acierto.")
        elif n_ok / len(resueltas) >= UMBRAL_RENTABLE:
            st.success("El acierto real supera el 55 %.")
        else:
            st.error("El acierto real no supera el 55 %: con dinero real se perdería.")
        hist = reg.iloc[::-1].head(50)
        st.dataframe(pd.DataFrame({
            "Hora": hist["entrada"].map(lambda t: hora_local(t)),
            "Mercado": hist["activo"],
            "Acción": hist["accion"].str.capitalize(),
            "Plazo": [texto_plazo(h * MINUTOS[i]) for h, i in zip(hist["horizonte"], hist["intervalo"])],
            "Resultado": hist["resultado"].map({"acierto": "✅", "fallo": "❌", "pendiente": "⏳",
                                                "sin datos": "—"}),
        }), hide_index=True, width="stretch")
        st.download_button("⬇️ Descargar todo (CSV)", reg.to_csv(index=False).encode("utf-8"),
                           "registro_senales.csv", "text/csv")


# ============================ PANTALLA ============================
st.markdown("## 📈 Analista técnico")
nombre = st.selectbox("¿Qué mercado analizo?", [TODOS, *ACTIVOS, OTRO], index=1)
plazo = st.segmented_control("¿Para cuánto tiempo?", list(PLAZOS), default="Cualquiera") or "Cualquiera"
cfg = None
if nombre == OTRO:
    escrito = st.text_input("Símbolo (Yahoo: NZDUSD=X, AAPL… · Binance: DOGEUSDT…)")
    if escrito:
        nombre, cfg = escrito.upper(), activo_personalizado(escrito)
elif nombre != TODOS:
    cfg = ACTIVOS[nombre]

if st.button("Analizar", type="primary", width="stretch", disabled=nombre == OTRO):
    st.cache_data.clear()  # datos frescos en cada pulsación
    if nombre == TODOS:
        encontrados, barra = [], st.progress(0.0, "Buscando oportunidades…")
        for i, (n, c) in enumerate(ACTIVOS.items()):
            barra.progress((i + 1) / len(ACTIVOS), f"Analizando {n}…")
            try:
                a = analizar_mercado(n, c, plazo)
            except Exception:
                continue
            registrar(a)
            if a["mejor"]:
                encontrados.append(a)
        barra.empty()
        encontrados.sort(key=lambda a: -a["por_tf"][a["mejor"]]["senal"]["confianza"])
        st.session_state.resultado = ("todos", encontrados)
    else:
        try:
            with st.spinner(f"Analizando {nombre}…"):
                a = analizar_mercado(nombre, cfg, plazo)
            registrar(a)
            st.session_state.resultado = ("uno", a)
        except Exception as e:
            st.session_state.resultado = None
            st.error(f"No se pudieron obtener datos de {nombre}: {e}")

resultado = st.session_state.get("resultado")
if resultado:
    tipo, contenido = resultado
    if tipo == "uno":
        tarjeta(contenido)
        r = contenido["por_tf"][contenido["principal"]]
        st.caption(f"Fuente: {r['origen']} · última vela cerrada {hora_local(r['df'].index[-1], '%H:%M')}")
        detalles(contenido)
    elif not contenido:
        with st.container(border=True):
            st.markdown("<div style='font-size:2.2rem;font-weight:800;color:#8a8f98'>⏸️ ESPERAR</div>",
                        unsafe_allow_html=True)
            st.write("Ningún mercado tiene ahora una oportunidad clara.")
            st.caption("Vuelve a buscar en 5-15 minutos.")
    else:
        st.markdown(f"**{len(contenido)} mercado(s) con señal**, de más a menos confianza:")
        for a in contenido:
            tarjeta(a, compacta=True)

mis_resultados()
with st.expander("❓ Cómo funciona"):
    st.markdown(f"""
- Analiza el mercado con velas de **5 min, 15 min, 1 hora, 4 horas y 1 día** y se queda con la mejor
  oportunidad. Por eso unas veces te dirá minutos, otras horas y otras días. Si quieres un plazo concreto,
  elígelo en «¿Para cuánto tiempo?».
- Los plazos largos (horas, días) suelen ser más fiables: hay menos «ruido» y los costes pesan menos, pero
  dan menos señales.
- Usa {len(ESTRATEGIAS)} estrategias: medias móviles, RSI, MACD, soportes y resistencias, Fibonacci y
  patrones de velas. Solo cuentan las que **han funcionado de verdad** en el histórico de ese mercado.
- Descarta señales que van **contra la tendencia** del plazo mayor.
- **Aprende**: cada señal se guarda y se comprueba al vencer. Si una estrategia falla en real, pierde peso.
- **ESPERAR** es una respuesta normal: la mayor parte del tiempo no hay ventaja clara.
- No uses dinero real hasta que «Mis resultados» muestre **más del 55 % con al menos 100 señales**.
""")
