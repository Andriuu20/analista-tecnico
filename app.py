"""Analista técnico: señales de compra/venta con su acierto medido en el histórico y en vivo."""
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
OTRO = "Otro símbolo…"

st.set_page_config(page_title="Analista técnico", page_icon="📈", layout="wide")


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
    if len(df) < 300:
        raise ValueError(f"Solo hay {len(df)} velas; hacen falta al menos 300 para analizar.")
    ind, senales, contexto = calcular(df)
    bt = backtest(df["Close"].to_numpy(), senales, coste)
    return df, origen, ind, senales, contexto, bt


def fmt_precio(p) -> str:
    if p is None or (isinstance(p, float) and np.isnan(p)):
        return "—"
    return f"{p:,.2f}" if p >= 1000 else f"{p:.3f}" if p >= 10 else f"{p:.5f}"


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def hora_local(ts) -> str:
    return pd.Timestamp(ts).tz_convert(ZONA).strftime("%d/%m %H:%M")


# --- Registro en vivo ---
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

# --- Selección de mercado ---
st.title("📈 Analista técnico")
c1, c2, c3 = st.columns([3, 2, 1], vertical_alignment="bottom")
nombre = c1.selectbox("Mercado", [*ACTIVOS, OTRO])
etiqueta = c2.selectbox("Velas de", list(INTERVALOS), index=2)
if c3.button("🔄 Actualizar", width="stretch"):
    st.cache_data.clear()
if nombre == OTRO:
    escrito = st.text_input("Símbolo de Yahoo (p. ej. NZDUSD=X, ^GSPC, AAPL) o de Binance (p. ej. DOGEUSDT)")
    if not escrito:
        st.stop()
    nombre, cfg = escrito.upper(), activo_personalizado(escrito)
else:
    cfg = ACTIVOS[nombre]
codigo, minutos = INTERVALOS[etiqueta]

try:
    with st.spinner("Descargando datos y calculando…"):
        df, origen, ind, senales, contexto, bt = analizar(cfg["fuente"], cfg["simbolo"], codigo, cfg["coste"])
except Exception as e:
    st.error(f"No se pudieron obtener datos de {nombre} en velas de {etiqueta}: {e}")
    st.stop()

senal = generar(senales, bt, estadisticas_vivo(registro, cfg["simbolo"], codigo), minutos)
ultima_vela = df.index[-1]
if senal["direccion"]:
    entrada = nueva_entrada(nombre, cfg, codigo, ultima_vela, float(df["Close"].iat[-1]), senal)
    if anadir(registro, entrada):
        guardar_registro()

st.caption(
    f"Datos: {origen} · {miles(len(df))} velas desde {hora_local(df.index[0])} · "
    f"última vela cerrada: {hora_local(ultima_vela)} (hora de España)"
)

tab_senal, tab_bt, tab_reg, tab_ayuda = st.tabs(["🎯 Señal", "🧪 Backtest", "📒 Registro", "❓ Ayuda"])

# ===================== SEÑAL =====================
with tab_senal:
    color = {"COMPRAR": "#26a69a", "VENDER": "#ef5350"}.get(senal["accion"], "#8a8f98")
    icono = {"COMPRAR": "⬆️", "VENDER": "⬇️"}.get(senal["accion"], "⏸️")
    with st.container(border=True):
        st.markdown(
            f"<div style='font-size:2.4rem;font-weight:700;color:{color}'>{icono} {senal['accion']}</div>",
            unsafe_allow_html=True,
        )
        if senal["direccion"]:
            vence = pd.Timestamp(entrada["vencimiento"])
            a, b = st.columns(2)
            a.metric("Plazo", senal["plazo"], help=f"{senal['horizonte']} velas de {etiqueta}")
            b.metric("Confianza", f"{senal['confianza'] * 100:.1f} %",
                     help="Acierto estimado según el backtest y el registro en vivo, ajustado hacia el 50 % "
                          "cuando hay pocas muestras.")
            st.write(f"Entrada al precio **{fmt_precio(float(df['Close'].iat[-1]))}** · vence a las "
                     f"**{hora_local(vence)}**.")
            if senal["confianza"] < UMBRAL_RENTABLE:
                st.warning(f"La confianza no llega al {UMBRAL_RENTABLE:.0%}: en binarias con pagos del 80-90 % "
                           "esto no sería rentable a la larga. Úsala solo para aprender o en demo.")
            st.caption("Señal guardada automáticamente en el Registro para comprobar si se cumple.")
        else:
            st.write(senal["motivo"])
            st.caption(f"Vuelve a mirar cuando cierre la próxima vela (cada {etiqueta}).")

    st.subheader("Situación del mercado")
    m = st.columns(3)
    m[0].metric("Precio", fmt_precio(contexto["precio"]))
    m[1].metric("Tendencia", contexto["tendencia"], help="EMA 50 frente a EMA 200 y pendiente de la EMA 50")
    m[2].metric("RSI", f"{contexto['rsi']:.0f}",
                help="Por encima de 70: sobrecompra. Por debajo de 30: sobreventa.")
    m = st.columns(3)
    m[0].metric("Soporte cercano", fmt_precio(contexto["soporte"]))
    m[1].metric("Resistencia cercana", fmt_precio(contexto["resistencia"]))
    m[2].metric("Patrón de vela", contexto["patron"] or "Ninguno")

    if senal["votos"]:
        st.subheader("Qué dice cada estrategia")
        filas = [{
            "Estrategia": v["descripcion"],
            "Dice": "Comprar" if v["direccion"] == 1 else "Vender",
            "Mejor plazo": texto_plazo(v["horizonte"] * minutos) if v["horizonte"] else "—",
            "Acierto estimado": f"{v['estimado'] * 100:.1f} %" if v["horizonte"] else "—",
            "Muestras": v["muestras"],
            "¿Cuenta?": "✅ Sí" if v["valida"] else f"❌ {v['motivo']}",
        } for v in senal["votos"]]
        st.dataframe(pd.DataFrame(filas), hide_index=True, width="stretch")

    st.plotly_chart(
        grafico(df, ind, contexto, senal, cierra_fines_de_semana=cfg["fuente"] == "yahoo"),
        width="stretch", config={"displayModeBar": False},
    )
    st.caption("Líneas punteadas: verde = soportes, roja = resistencias. Grises: niveles de Fibonacci del "
               "último impulso.")

# ===================== BACKTEST =====================
with tab_bt:
    st.write(
        f"Cada estrategia aplicada a las **{miles(len(df))} velas** del histórico de {nombre} en velas de "
        f"{etiqueta}. Se cuenta un acierto si, al cabo del plazo, el precio fue en la dirección de la "
        "señal (como una binaria a vencimiento)."
    )
    st.markdown("🟢 ≥ 55 % y claramente por encima del azar · 🟡 por encima del 52 % · ⚪ azar o pocas señales")

    def celda(f):
        if f["senales"] == 0:
            return "—"
        z = (f["acierto"] - 0.5) / (0.5 / np.sqrt(f["senales"]))
        marca = "🟢" if f["acierto"] >= 0.55 and z >= Z_SIGNIFICATIVO else "🟡" if f["acierto"] >= 0.52 else "⚪"
        return f"{marca} {f['acierto'] * 100:.1f} % · {f['senales']}"

    vista = bt.assign(celda=bt.apply(celda, axis=1))
    resumen = vista.pivot(index="estrategia", columns="horizonte", values="celda")
    resumen.columns = [texto_plazo(h * minutos) for h in resumen.columns]
    resumen.index = [ESTRATEGIAS[e] for e in resumen.index]
    st.dataframe(resumen, width="stretch")
    st.caption("Formato: acierto · número de señales. Columnas: plazo hasta el vencimiento.")

    with st.expander("Detalle completo"):
        st.write(
            "**Acierto neto**: descontando el coste aproximado de operar en forex/CFD "
            f"({cfg['coste'] * 100:.3f} % del precio). **Reciente**: solo el último 30 % del histórico, "
            "para ver si la estrategia sigue funcionando. **Mov. medio**: lo que se movió el precio a favor "
            "(+) o en contra (−) de media."
        )
        detalle = pd.DataFrame({
            "Estrategia": bt["estrategia"].map(ESTRATEGIAS),
            "Plazo": bt["horizonte"].map(lambda h: texto_plazo(h * minutos)),
            "Señales": bt["senales"],
            "Acierto %": (bt["acierto"] * 100).round(1),
            "Acierto neto %": (bt["acierto_neto"] * 100).round(1),
            "Reciente %": (bt["acierto_rec"] * 100).round(1),
            "Señales recientes": bt["senales_rec"],
            "Mov. medio %": (bt["mov_medio"] * 100).round(4),
        })
        st.dataframe(detalle, hide_index=True, width="stretch")
    st.info("Ojo: con pocas señales salen porcentajes altos por pura suerte (en datos aleatorios se ven "
            "casillas del 60 %). Un buen resultado en el pasado no garantiza el futuro; por eso existe el "
            "Registro, que comprueba las señales reales después de darlas.")

# ===================== REGISTRO =====================
with tab_reg:
    st.write("Cada señal de COMPRAR o VENDER se guarda sola y se comprueba al vencer. Es la prueba de "
             "verdad: lo que importa es este acierto, no el del backtest.")
    if not almacen.remoto:
        st.caption("⚠️ El registro se guarda en el servidor y puede borrarse al reiniciarse la app. "
                   "Configura GITHUB_TOKEN y GIST_ID (ver README) para guardarlo de forma permanente.")
    if st.button("🔄 Recargar registro"):
        st.session_state.pop("registro", None)
        st.rerun()

    if not registro:
        st.info("Todavía no hay señales registradas. Aparecerán aquí cuando la app dé su primera señal.")
    else:
        reg = pd.DataFrame(registro)
        resueltas = reg[reg["resultado"].isin(["acierto", "fallo"])]
        n_ok = int((resueltas["resultado"] == "acierto").sum())
        m = st.columns(3)
        m[0].metric("Señales", len(reg))
        m[1].metric("Pendientes", int((reg["resultado"] == "pendiente").sum()))
        m[2].metric("Acierto real", f"{n_ok / len(resueltas) * 100:.1f} %" if len(resueltas) else "—",
                    help=f"{n_ok} aciertos de {len(resueltas)} señales comprobadas")
        if len(resueltas) >= 1:
            tasa = n_ok / len(resueltas)
            if len(resueltas) < 100:
                st.caption(f"Con {len(resueltas)} señales comprobadas aún es pronto para sacar conclusiones; "
                           "hacen falta al menos 100.")
            elif tasa >= UMBRAL_RENTABLE:
                st.success(f"El acierto real ({tasa:.1%}) supera el {UMBRAL_RENTABLE:.0%} con "
                           f"{len(resueltas)} señales.")
            else:
                st.error(f"El acierto real ({tasa:.1%}) no supera el {UMBRAL_RENTABLE:.0%}: "
                         "con dinero real se perdería.")

        if len(resueltas):
            st.subheader("Por mercado y plazo")
            resueltas = resueltas.assign(ok=resueltas["resultado"] == "acierto",
                                         velas=resueltas["intervalo"].map(
                                             {c: e for e, (c, _) in INTERVALOS.items()}))
            por_mercado = (resueltas.groupby(["activo", "velas"])["ok"].agg(["count", "mean"]).reset_index()
                           .rename(columns={"activo": "Mercado", "velas": "Velas", "count": "Señales",
                                            "mean": "Acierto %"}))
            por_mercado["Acierto %"] = (por_mercado["Acierto %"] * 100).round(1)
            st.dataframe(por_mercado, hide_index=True, width="stretch")

            st.subheader("Por estrategia")
            por_est = (resueltas.explode("estrategias").groupby("estrategias")["ok"].agg(["count", "mean"])
                       .reset_index())
            por_est = pd.DataFrame({"Estrategia": por_est["estrategias"].map(ESTRATEGIAS),
                                    "Señales": por_est["count"],
                                    "Acierto %": (por_est["mean"] * 100).round(1)})
            st.dataframe(por_est, hide_index=True, width="stretch")

        st.subheader("Historial")
        hist = reg.iloc[::-1]
        st.dataframe(pd.DataFrame({
            "Hora": hist["entrada"].map(hora_local),
            "Mercado": hist["activo"],
            "Velas": hist["intervalo"].map({c: e for e, (c, _) in INTERVALOS.items()}),
            "Acción": hist["accion"],
            "Plazo": [texto_plazo(h * MINUTOS[i]) for h, i in zip(hist["horizonte"], hist["intervalo"])],
            "Confianza %": (hist["confianza"] * 100).round(1),
            "Entrada": hist["precio_entrada"].map(fmt_precio),
            "Salida": hist["precio_salida"].map(lambda p: fmt_precio(p) if p is not None else "—"),
            "Resultado": hist["resultado"].map({"acierto": "✅ Acierto", "fallo": "❌ Fallo",
                                                "pendiente": "⏳ Pendiente", "sin datos": "— Sin datos"}),
        }), hide_index=True, width="stretch")
        st.download_button("⬇️ Descargar CSV", reg.to_csv(index=False).encode("utf-8"),
                           "registro_senales.csv", "text/csv")

# ===================== AYUDA =====================
with tab_ayuda:
    st.markdown(f"""
**Cómo usarla**
1. Elige el **mercado** y el **tamaño de vela** (15 min es un buen punto de partida).
2. La pestaña **Señal** dice si **comprar, vender o esperar**, a qué **plazo** y con qué **confianza**.
3. Las señales se guardan solas en el **Registro** y se comprueban al vencer.

**Cómo decide**
- Calcula 6 estrategias: {", ".join(ESTRATEGIAS.values()).lower()}.
- Solo cuentan las que se han activado en la **última vela cerrada**.
- Divide el histórico en dos partes. Con el **70 % antiguo** elige el plazo en el que mejor ha funcionado cada
  estrategia, y solo la deja votar si ese acierto se distingue claramente del azar.
- La **confianza** se mide con el **30 % reciente**, que no se usó para elegir. Así no se engaña a sí misma
  escogiendo "el mejor resultado" a posteriori.
- Si las que votan coinciden, da la señal con el plazo de la más fiable. Si se contradicen, dice **esperar**.

**Cómo aprende**
- El backtest se recalcula con cada actualización, así que se adapta a cómo se mueve el mercado ahora.
- Los resultados reales del **Registro** se suman a los del backtest: si una estrategia falla en vivo,
  pierde peso y deja de votar.

**Lo importante**
- En binarias con pagos del 80-90 % hace falta acertar **más del 55 %** de forma sostenida para no perder.
- No te fíes del acierto hasta tener **al menos 100 señales comprobadas** en el Registro.
- "Esperar" es una respuesta válida: la mayoría del tiempo no hay ventaja clara.
""")
