# Auditoría y ampliación del motor de análisis

Revisión del código existente (no de lo que decía la documentación) y lo que se hizo con cada herramienta.

**Estados:** IMPLEMENTADA (funciona, no se toca) · INCOMPLETA (se mejoró solo lo necesario) ·
NO IMPLEMENTADA (se añadió) · REDUNDANTE (ya cubierta, no se duplica).

## Tendencias y medias móviles

| Herramienta | Estado encontrado | Qué se hizo | Prioridad | Beneficio analítico |
|---|---|---|---|---|
| EMA 9 / 21 y su cruce | IMPLEMENTADA | Nada | — | — |
| EMA 20 | REDUNDANTE | No se añade: la EMA 21 ya existe y la diferencia es mínima. Dos medias casi iguales solo duplicarían señales | — | Evita contradicciones |
| EMA 50 / 200 | IMPLEMENTADA (tendencia y filtro multitemporal) | Nada | — | — |
| SMA 50 / 100 / 200 | NO IMPLEMENTADA | Añadidas. SMA 200 como referencia (precio por encima/debajo), cruce SMA 50/200 como estrategia | Media | Tendencia de fondo clásica |
| SuperTrend (10, 3) | NO IMPLEMENTADA | Añadido; estrategia = cambio de dirección | Alta | Seguimiento de tendencia con ATR |
| ADX (14) | NO IMPLEMENTADA | Añadido como contexto: lateral (< 20), tendencia débil (20-25) o fuerte (≥ 25) | Alta | Distingue mercados laterales de tendencias |

## Análisis técnico

| Herramienta | Estado encontrado | Qué se hizo | Prioridad | Beneficio analítico |
|---|---|---|---|---|
| Fibonacci (retrocesos) | IMPLEMENTADA | Nada | — | — |
| Fibonacci (extensiones) | NO IMPLEMENTADA | Añadidas 127,2 % y 161,8 % (contexto y gráfico) | Baja | Objetivos de precio de referencia |
| Soportes y resistencias | IMPLEMENTADA | Nada | — | — |
| Price Action | INCOMPLETA (solo patrones de velas) | Cubierta con estructura, rupturas y barridas (abajo) | Alta | Lectura del movimiento sin indicadores |
| Breakout & Retest | NO IMPLEMENTADA | Añadida: cierre más allá de un techo/suelo y vuelta al nivel con rebote en ≤ 20 velas | Alta | Entradas tras confirmar la ruptura |
| Velas japonesas | IMPLEMENTADA | Nada | — | — |
| RSI | **INCOMPLETA: fallo real** | Sin bajadas daba un valor vacío en vez de 100 y la estrategia no podía activarse. Corregido | Alta | Señales que antes se perdían |
| Divergencias RSI | NO IMPLEMENTADA | Añadidas entre dos techos o dos suelos confirmados (≤ 60 velas) | Media | Agotamiento de tendencia |
| MACD | IMPLEMENTADA | Nada | — | — |
| Bandas de Bollinger (20, 2) | NO IMPLEMENTADA | Añadidas; estrategia = vuelta al interior tras cerrar fuera | Media | Reversión a la media |
| ATR | IMPLEMENTADA (uso interno) | Reutilizado para Stop Loss y volatilidad, sin duplicarlo | — | — |
| Estocástico (14, 3, 3) | NO IMPLEMENTADA | Añadido; estrategia = cruce %K/%D por debajo de 20 o por encima de 80 | Media | Giros en sobreventa/sobrecompra |

## Estructura de mercado y Smart Money Concepts (módulo nuevo `estructura.py`)

Todo usa los mismos techos y suelos confirmados que ya usaba la app (no se calculan dos veces).

| Herramienta | Estado encontrado | Qué se hizo | Prioridad | Beneficio analítico |
|---|---|---|---|---|
| HH / HL / LH / LL | NO IMPLEMENTADA | Etiquetas y estado de la estructura (contexto) | Alta | Base del resto de SMC |
| BOS | NO IMPLEMENTADA | Estrategia: cierre más allá del último techo/suelo a favor de la estructura | Alta | Continuación de tendencia |
| CHoCH | NO IMPLEMENTADA | Estrategia: misma ruptura pero en contra de la estructura | Alta | Posible cambio de tendencia |
| Order Blocks | NO IMPLEMENTADA | Última vela contraria antes de una ruptura; estrategia = reacción al volver a ella | Media | Zonas de entrada institucionales |
| Fair Value Gaps | NO IMPLEMENTADA | Hueco de 3 velas (≥ 0,1 ATR); estrategia = reacción al volver al hueco | Media | Desequilibrios de precio |
| Liquidity Sweeps | NO IMPLEMENTADA | Estrategia: mecha más allá de un techo/suelo y cierre de vuelta | Alta | Trampas de liquidez |
| Equal Highs / Lows | NO IMPLEMENTADA | Contexto: dos techos/suelos a menos de 0,1 ATR | Baja | Zonas de liquidez |
| Premium / Discount | NO IMPLEMENTADA | Contexto y factor: mitad alta o baja del último rango | Media | Comprar barato / vender caro |

## Análisis avanzado

| Herramienta | Estado encontrado | Qué se hizo | Prioridad | Beneficio analítico |
|---|---|---|---|---|
| Multitemporal | IMPLEMENTADA (5 temporalidades + filtro de tendencia medido) | Nada | — | — |
| Volatilidad | NO IMPLEMENTADA | Percentil del ATR en las últimas 500 velas: baja / normal / alta | Media | Avisa de entornos raros |
| Mercados laterales | INCOMPLETA (solo EMA 50/200) | Añadido el ADX | Alta | Mejor detección de rangos |
| Tendencia fuerte / débil | NO IMPLEMENTADA | ADX + dirección (+DI / −DI) | Alta | Fuerza del movimiento |
| Noticias económicas | NO IMPLEMENTADA | Calendario público de Forex Factory: en forex y oro, ESPERAR si hay una noticia de alto impacto antes del vencimiento (plazos < 1 día) | Alta | Evita los picos de volatilidad y spread |
| Análisis fundamental | NO IMPLEMENTADA | Solo el calendario: no hay una fuente gratuita y verificable con histórico para poder medirlo | — | — |
| Confluencias | IMPLEMENTADA | Nada. Ya era una media ponderada por la ventaja medida de cada estrategia, no una suma: añadir estrategias parecidas no infla la confianza | — | — |
| Evaluación histórica | IMPLEMENTADA (tipo binaria a vencimiento) | Añadido backtest de Stop Loss / Take Profit con costes | Alta | Plan de operación medido |
| Costes de operación | INCOMPLETA (solo informativos) | Ahora se descuentan en el plan SL/TP y bloquean la señal si se comen > 25 % del riesgo | Alta | No operar cuando el spread se lo come todo |
| Condiciones para no operar | INCOMPLETA (solo «sin ventaja») | Añadidas: coste > 25 % del riesgo y noticias de alto impacto | Alta | Menos operaciones malas |

## Decisión: entrada, Stop Loss, Take Profit (módulo nuevo `plan.py`)

- Entrada: cierre de la última vela. Stop Loss: tras el último suelo/techo confirmado + 0,1 ATR (entre 0,5 y
  3 ATR; si no, 1,5 ATR). Take Profit: R × riesgo, con R ∈ {1; 1,5; 2; 3}.
- Se simulan las señales pasadas de las mismas estrategias con la misma regla (si el SL y el TP se tocan en la
  misma vela, cuenta como pérdida). R se elige con el 70 % antiguo y los resultados se miden con el 30 %
  reciente. Se muestra: operaciones, veces que llegó al TP, resultado medio en R tras costes y duración típica.
- Motivos a favor y en contra (`factores.py`): los marcados con 📏 están medidos; el resto son referencias
  técnicas que explican la situación pero no cambian la decisión, porque no se ha demostrado que mejoren el
  acierto. Así no se inventan probabilidades.

## Validación

- **Sin mirar al futuro:** prueba de truncado (calcular con datos hasta la vela k y con todos) para las 17
  estrategias, la estructura, SuperTrend, ADX y RSI: 0 diferencias.
- **Calibración con datos aleatorios:** con 17 estrategias el umbral de significación pasa de z = 2,2 a 2,4.
  Señales falsas: 3 % de las velas (antes, con 6 estrategias, 4 %), ~1 % con confianza ≥ 55 %. Tener más
  estrategias no da más señales falsas ni más peso automático: cada una solo vota si demuestra ventaja.
- **Pruebas automáticas** (`tests/`, se ejecutan con `python -m pytest tests`): indicadores, ausencia de
  información futura, señales falsas en datos aleatorios, simulador de SL/TP, estructura, noticias y la app.

## Pendiente (siguientes pasos posibles)

- Comprobar en el registro en vivo si se tocó antes el SL o el TP (ahora se guardan, pero solo se evalúa el
  vencimiento).
- Medir con el histórico si el ADX o la zona premium/discount mejoran el acierto (como se hizo con la
  tendencia) antes de dejar que influyan en la decisión.
