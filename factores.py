"""Motivos a favor y factores en contra de una señal, para explicarla.

Las líneas con 📏 están medidas con el histórico de ese mercado. El resto son referencias técnicas
clásicas (estructura, ADX, zona premium/discount…) que ayudan a entender la situación pero NO
cambian la decisión, porque no se ha demostrado que mejoren el acierto."""
from senal import texto_plazo

# estrategias que siguen la tendencia y estrategias de giro (para avisar si el entorno no les encaja)
TENDENCIALES = {"medias", "macd", "supertrend", "cruce_sma", "bos", "ruptura", "fibonacci"}
DE_GIRO = {"rsi", "bollinger", "estocastico", "divergencia", "choch", "barrida", "soportes"}


def factores(senal: dict, contexto: dict, minutos_vela: int, nombre_tf_tendencia: str,
             fmt_precio, hora) -> tuple[list[str], list[str]]:
    d = senal["direccion"]
    a_favor, en_contra = [], []
    compra = d == 1

    for v in senal["votos"]:
        if v.get("valida") and v["direccion"] == d:
            a_favor.append(f"📏 {v['descripcion']}: acierto medido {v['estimado']:.0%} a "
                           f"{texto_plazo(v['horizonte'] * minutos_vela)} ({v['muestras']} casos recientes)")
        elif v.get("valida"):
            en_contra.append(f"📏 {v['descripcion']} dice lo contrario")

    plan = senal.get("plan")
    if plan:
        if not plan["datos_suficientes"]:
            en_contra.append("📏 Pocos casos en el histórico para valorar este Stop Loss / Take Profit")
        elif plan["esperanza"] > 0:
            a_favor.append(f"📏 Con este SL/TP: TP antes que SL en {plan['tp_alcanzado']} de "
                           f"{plan['operaciones']} operaciones recientes; resultado medio "
                           f"{plan['esperanza']:+.2f} R tras costes")
        else:
            en_contra.append(f"📏 Con este SL/TP el resultado medio reciente fue {plan['esperanza']:+.2f} R "
                             f"tras costes ({plan['operaciones']} operaciones): no ha compensado")
        nivel = contexto["resistencia"] if compra else contexto["soporte"]
        if nivel is not None and min(plan["entrada"], plan["tp"]) < nivel < max(plan["entrada"], plan["tp"]):
            en_contra.append(f"{'Resistencia' if compra else 'Soporte'} en {fmt_precio(nivel)} antes del Take Profit")

    tendencia = senal.get("contexto")
    if tendencia == 1:
        a_favor.append(f"A favor de la tendencia de las velas de {nombre_tf_tendencia}")
    elif tendencia == -1:
        en_contra.append(f"En contra de la tendencia de las velas de {nombre_tf_tendencia}")

    estado = contexto["estructura"]["estado"]
    if estado != "Sin definir":
        texto = f"Estructura de mercado {estado.lower()} (última ruptura {'al alza' if estado == 'Alcista' else 'a la baja'})"
        (a_favor if (estado == "Alcista") == compra else en_contra).append(texto)

    regimen = contexto["regimen"]
    usadas = set(senal.get("estrategias", []))
    if regimen == "Lateral" and usadas & TENDENCIALES:
        en_contra.append("Mercado lateral (ADX < 20): poca fuerza para seguir una tendencia")
    elif regimen.startswith("Tendencia fuerte"):
        mismo_lado = regimen.endswith("alcista") == compra
        if mismo_lado:
            a_favor.append(f"{regimen} (ADX ≥ 25)")
        elif usadas & DE_GIRO:
            en_contra.append(f"{regimen} (ADX ≥ 25): ir contra ella es arriesgado")

    zona = contexto["estructura"]["zona"]
    if zona == "discount":
        (a_favor if compra else en_contra).append("Precio en zona de descuento (mitad baja del último rango)")
    elif zona == "premium":
        (en_contra if compra else a_favor).append("Precio en zona premium (mitad alta del último rango)")

    rsi = contexto["rsi"]
    if compra and rsi > 70:
        en_contra.append(f"RSI en sobrecompra ({rsi:.0f})")
    elif not compra and rsi < 30:
        en_contra.append(f"RSI en sobreventa ({rsi:.0f})")

    sobre = contexto["sobre_sma200"]
    if sobre is not None:
        (a_favor if sobre == compra else en_contra).append(
            f"Precio {'por encima' if sobre else 'por debajo'} de la SMA 200")

    if contexto["volatilidad"] == "Alta":
        en_contra.append("Volatilidad alta: movimientos bruscos, el Stop Loss se toca con más facilidad")
    elif contexto["volatilidad"] == "Baja":
        en_contra.append("Volatilidad baja: el precio puede no llegar al objetivo")

    for e in senal.get("noticias", []):
        en_contra.append(f"Noticia de alto impacto: {e['titulo']} ({e['moneda']}) a las {hora(e['hora'])}")
    return a_favor, en_contra
