"""Gráfico de velas con medias, soportes/resistencias, Fibonacci, RSI y MACD."""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

VERDE, ROJO, GRIS = "#26a69a", "#ef5350", "#8a8f98"
COLOR_MEDIAS = {"ema9": "#2a78d6", "ema21": "#e8a33c", "ema50": "#9b59b6"}


def grafico(df: pd.DataFrame, ind: pd.DataFrame, contexto: dict, senal: dict, cierra_fines_de_semana: bool,
            velas: int = 150) -> go.Figure:
    d, i = df.iloc[-velas:], ind.iloc[-velas:]
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.03,
                        row_heights=[0.62, 0.19, 0.19])
    fig.add_trace(go.Candlestick(
        x=d.index, open=d["Open"], high=d["High"], low=d["Low"], close=d["Close"], name="Precio",
        increasing_line_color=VERDE, decreasing_line_color=ROJO, showlegend=False,
    ), row=1, col=1)
    for col, color in COLOR_MEDIAS.items():
        fig.add_trace(go.Scatter(x=i.index, y=i[col], name=col.upper().replace("EMA", "EMA "),
                                 line=dict(color=color, width=1.5)), row=1, col=1)

    bajo, alto = d["Low"].min(), d["High"].max()
    margen = (alto - bajo) * 0.05
    visibles = lambda niveles: [p for p in niveles if bajo - margen <= p <= alto + margen]
    for p in visibles(contexto["suelos"])[-4:]:
        fig.add_hline(y=p, line=dict(color=VERDE, width=1, dash="dot"), opacity=0.6, row=1, col=1)
    for p in visibles(contexto["techos"])[:4]:
        fig.add_hline(y=p, line=dict(color=ROJO, width=1, dash="dot"), opacity=0.6, row=1, col=1)
    fibo = contexto.get("fibonacci")
    if fibo:
        for nivel, p in fibo["niveles"].items():
            if bajo - margen <= p <= alto + margen:
                fig.add_hline(y=p, line=dict(color=GRIS, width=1), opacity=0.5,
                              annotation_text=f"Fibo {nivel * 100:g}%", annotation_position="left",
                              annotation_font=dict(size=10, color=GRIS), row=1, col=1)
    if senal["direccion"]:
        compra = senal["direccion"] == 1
        fig.add_trace(go.Scatter(
            x=[d.index[-1]], y=[d["Low"].iat[-1] if compra else d["High"].iat[-1]],
            mode="markers", name=senal["accion"].capitalize(),
            marker=dict(symbol="triangle-up" if compra else "triangle-down", size=16,
                        color=VERDE if compra else ROJO, line=dict(width=2, color="white")),
        ), row=1, col=1)

    fig.add_trace(go.Scatter(x=i.index, y=i["rsi"], name="RSI", line=dict(color="#2a78d6", width=1.5),
                             showlegend=False), row=2, col=1)
    for nivel in (30, 70):
        fig.add_hline(y=nivel, line=dict(color=GRIS, width=1, dash="dot"), row=2, col=1)
    fig.add_trace(go.Bar(x=i.index, y=i["macd_hist"], name="Histograma MACD", showlegend=False,
                         marker_color=[VERDE if v >= 0 else ROJO for v in i["macd_hist"]]), row=3, col=1)
    fig.add_trace(go.Scatter(x=i.index, y=i["macd"], name="MACD", line=dict(color="#2a78d6", width=1.5),
                             showlegend=False), row=3, col=1)
    fig.add_trace(go.Scatter(x=i.index, y=i["macd_senal"], name="Señal MACD",
                             line=dict(color="#e8a33c", width=1.5), showlegend=False), row=3, col=1)

    fig.update_yaxes(title_text="RSI", range=[0, 100], row=2, col=1)
    fig.update_yaxes(title_text="MACD", row=3, col=1)
    if cierra_fines_de_semana:  # forex: sin huecos de fin de semana
        fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
    fig.update_layout(
        height=680, margin=dict(l=10, r=10, t=30, b=10), hovermode="x unified",
        xaxis_rangeslider_visible=False, legend=dict(orientation="h", y=1.04, x=0),
    )
    return fig
