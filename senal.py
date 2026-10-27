"""Combina las estrategias que se activan en la última vela, ponderadas por su acierto
histórico (backtest) y real (registro en vivo), en una única recomendación.

Para no engañarse eligiendo "el mejor plazo" a posteriori, el plazo de cada estrategia se
elige con el 70 % antiguo del histórico y la confianza se mide solo con el 30 % reciente
(que no se usó para elegir) más los resultados reales del registro."""
import numpy as np
import pandas as pd

from backtest import estimar
from estrategias import ESTRATEGIAS

UMBRAL_VOTO = 0.52  # acierto mínimo en la parte antigua para que una estrategia cuente
Z_SIGNIFICATIVO = 2.2  # y superar el 50 % de forma significativa (corregido por probar 7 plazos)
MIN_SENALES = 20  # muestras mínimas para elegir plazo y para medir la confianza
UMBRAL_RENTABLE = 0.55  # lo que hace falta en binarias con pagos del 80-90 %


def texto_plazo(minutos: int) -> str:
    if minutos < 60:
        return f"{minutos} min"
    if minutos < 1440:
        horas = minutos / 60
        return f"{horas:g} hora" + ("s" if horas != 1 else "")
    dias = minutos / 1440
    return f"{dias:g} día" + ("s" if dias != 1 else "")


def generar(senales: dict, bt: pd.DataFrame, vivo: pd.DataFrame | None, minutos_vela: int) -> dict:
    tabla = bt.copy()
    tabla[["vivo_aciertos", "vivo_total"]] = 0
    if vivo is not None and not vivo.empty:
        tabla = tabla.drop(columns=["vivo_aciertos", "vivo_total"]).merge(
            vivo, on=["estrategia", "horizonte"], how="left"
        ).fillna({"vivo_aciertos": 0, "vivo_total": 0})
    tabla["eleccion"] = estimar(tabla["aciertos_ant"], tabla["senales_ant"])
    tabla["total"] = tabla["senales_rec"] + tabla["vivo_total"]
    tabla["estimado"] = estimar(tabla["aciertos_rec"] + tabla["vivo_aciertos"], tabla["total"])

    votos = []
    for nombre, senal in senales.items():
        direccion = int(senal[-1])
        if direccion == 0:
            continue
        voto = {"estrategia": nombre, "descripcion": ESTRATEGIAS[nombre], "direccion": direccion,
                "valida": False, "horizonte": None, "estimado": np.nan, "muestras": 0, "motivo": ""}
        cand = tabla[(tabla["estrategia"] == nombre) & (tabla["senales_ant"] >= MIN_SENALES)]
        if cand.empty:
            voto["motivo"] = "pocas señales en el histórico para fiarse"
        else:
            mejor = cand.loc[cand["eleccion"].idxmax()]
            voto.update(horizonte=int(mejor["horizonte"]), estimado=float(mejor["estimado"]),
                        muestras=int(mejor["total"]))
            n_ant = mejor["senales_ant"]
            z = (mejor["aciertos_ant"] / n_ant - 0.5) / (0.5 / np.sqrt(n_ant))
            if mejor["eleccion"] < UMBRAL_VOTO or z < Z_SIGNIFICATIVO:
                voto["motivo"] = "su acierto histórico no se distingue del azar"
            elif mejor["total"] < MIN_SENALES:
                voto["motivo"] = "pocas señales recientes para comprobarla"
            elif mejor["estimado"] <= 0.5:
                voto["motivo"] = "no se confirma en los datos recientes"
            else:
                voto["valida"] = True
        votos.append(voto)

    validos = [v for v in votos if v["valida"]]
    peso = {1: 0.0, -1: 0.0}
    for v in validos:
        peso[v["direccion"]] += v["estimado"] - 0.5

    resultado = {"accion": "ESPERAR", "direccion": 0, "horizonte": None, "plazo": None,
                 "confianza": None, "votos": votos, "motivo": ""}
    if not votos:
        resultado["motivo"] = "Ninguna estrategia ha dado señal en la última vela cerrada."
        return resultado
    if not validos:
        resultado["motivo"] = "Hay señales, pero ninguna estrategia tiene un historial fiable en este mercado y plazo."
        return resultado
    direccion = 1 if peso[1] >= peso[-1] else -1
    a_favor, en_contra = peso[direccion], peso[-direccion]
    if en_contra > 0.5 * a_favor:
        resultado["motivo"] = "Las estrategias fiables se contradicen (unas dicen comprar y otras vender)."
        return resultado

    favor = [v for v in validos if v["direccion"] == direccion]
    principal = max(favor, key=lambda v: v["estimado"])
    confianza = sum(v["estimado"] * (v["estimado"] - 0.5) for v in favor) / a_favor - en_contra
    resultado.update(
        accion="COMPRAR" if direccion == 1 else "VENDER",
        direccion=direccion,
        horizonte=principal["horizonte"],
        plazo=texto_plazo(principal["horizonte"] * minutos_vela),
        confianza=confianza,
        estrategias=[v["estrategia"] for v in favor],
    )
    return resultado
