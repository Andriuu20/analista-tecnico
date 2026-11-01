# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**624 señales** del 15/09/2025 al 30/10/2026. Acierto (precio a favor al vencer): **49,4 %** · resultado medio con SL/TP tras costes: **-0.21 R** · no se distingue del azar todavía (z = -0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | falla | 40,3 % en 129 | pocos casos en la segunda mitad | ⏳ faltan datos |
| plazo = **2-4 h** | falla | 40,8 % en 130 | después 55,2 % en 67 casos | ❔ no se repite |
| franja = **04-08 h** | falla | 36,4 % en 55 | después 43,3 % en 30 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | falla | 37,4 % en 99 | después 53,4 % en 103 casos | ❔ no se repite |
| confianza_tramo = **<52 %** | falla | 38,4 % en 138 | después 53,7 % en 175 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 313 | 47,0 % | -0.23 R |
| 52-55 % | 243 | 54,3 % | -0.16 R |
| 55-58 % | 64 | 42,2 % | -0.35 R |
| ≥58 % | 4 | 50,0 % | +0.42 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 167 | 53,3 % | -0.09 R |
| Oro (XAU/USD) | 166 | 50,0 % | -0.20 R |
| USD/CHF | 72 | 56,9 % | -0.13 R |
| USD/JPY | 65 | 43,1 % | -0.55 R |
| EUR/GBP | 58 | 46,6 % | -0.28 R |
| SOL/USDT | 33 | 30,3 % | -0.17 R |
| USD/CAD | 30 | 46,7 % | -0.41 R |
| GBP/JPY | 18 | 44,4 % | -0.10 R |
| BTC/USDT | 10 | 50,0 % | -0.04 R |
| XRP/USDT | 3 | 66,7 % | -0.81 R |
| EUR/USD | 1 | 100,0 % | +0.92 R |
| GBP/USD | 1 | 0,0 % | -1.19 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 256 | 51,6 % | -0.31 R |
| 15m | 222 | 52,3 % | -0.18 R |
| 1h | 146 | 41,1 % | -0.07 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 231 | 50,6 % | -0.34 R |
| 2-4 h | 197 | 45,7 % | -0.16 R |
| 30-59 min | 196 | 51,5 % | -0.12 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 206 | 46,6 % | -0.14 R |
| velas | 156 | 51,3 % | -0.22 R |
| estocastico | 116 | 53,4 % | -0.15 R |
| soportes | 63 | 44,4 % | -0.59 R |
| barrida | 41 | 53,7 % | -0.10 R |
| bos | 36 | 44,4 % | -0.28 R |
| rsi | 24 | 58,3 % | -0.22 R |
| fibonacci | 6 | 33,3 % | -0.02 R |
| macd | 1 | 100,0 % | +1.81 R |
| supertrend | 1 | 100,0 % | +0.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 129 | 53,5 % | -0.38 R |
| 16-20 h | 126 | 54,0 % | -0.13 R |
| 08-12 h | 121 | 45,5 % | -0.18 R |
| 04-08 h | 85 | 38,8 % | -0.22 R |
| 00-04 h | 84 | 42,9 % | -0.15 R |
| 20-24 h | 79 | 59,5 % | -0.16 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 293 | 52,6 % | -0.13 R |
| lateral (<20) | 202 | 45,5 % | -0.29 R |
| débil (20-25) | 129 | 48,1 % | -0.27 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 348 | 47,7 % | -0.17 R |
| alta | 190 | 52,1 % | -0.18 R |
| baja | 86 | 50,0 % | -0.43 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 253 | 49,4 % | -0.12 R |
| a favor | 243 | 50,6 % | -0.21 R |
| en contra | 128 | 46,9 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 426 | 49,3 % | -0.15 R |
| en contra | 195 | 49,2 % | -0.35 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 394 | 50,0 % | -0.19 R |
| a favor | 230 | 48,3 % | -0.24 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 27/10 12:30 | Oro (XAU/USD) | 15m | VENDER | 225 min | fibonacci+velas | -1.24 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 25/08 04:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -0.96 % |
| 14/10 22:00 | Oro (XAU/USD) | 15m | VENDER | 225 min | velas | -0.96 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**783 señales** del 08/01/2021 al 30/10/2026. Acierto (precio a favor al vencer): **50,3 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 0.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **ETH/USDT** | falla | 33,3 % en 51 | pocos casos en la segunda mitad | ⏳ faltan datos |
| mercado = **GBP/JPY** | acierta | 66,0 % en 47 | después 51,2 % en 86 casos | ❔ no se repite |
| temporalidad = **1h** | acierta | 59,0 % en 134 | después 48,3 % en 232 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 65,9 % en 44 | después 54,2 % en 48 casos | ❔ no se repite |
| volatilidad = **alta** | acierta | 63,2 % en 87 | después 47,7 % en 86 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 431 | 47,3 % | -0.09 R |
| 52-55 % | 316 | 54,7 % | -0.14 R |
| 55-58 % | 36 | 47,2 % | +0.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 181 | 52,5 % | -0.09 R |
| GBP/JPY | 133 | 56,4 % | -0.18 R |
| Oro (XAU/USD) | 117 | 50,4 % | +0.06 R |
| GBP/USD | 92 | 51,1 % | -0.17 R |
| SOL/USDT | 88 | 58,0 % | -0.01 R |
| ETH/USDT | 55 | 30,9 % | -0.34 R |
| EUR/GBP | 43 | 39,5 % | -0.41 R |
| AUD/USD | 39 | 53,8 % | +0.37 R |
| XRP/USDT | 17 | 41,2 % | +0.18 R |
| USD/JPY | 13 | 30,8 % | -0.75 R |
| EUR/USD | 3 | 33,3 % | +0.95 R |
| EUR/JPY | 1 | 0,0 % | -1.08 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 366 | 52,2 % | -0.17 R |
| 4h | 239 | 48,1 % | -0.15 R |
| 1d | 140 | 51,4 % | +0.10 R |
| 15m | 38 | 42,1 % | +0.11 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 289 | 51,9 % | -0.14 R |
| 2-5 días | 231 | 49,8 % | -0.02 R |
| 4-12 h | 202 | 48,0 % | -0.19 R |
| 1-2 días | 61 | 52,5 % | +0.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 330 | 50,9 % | -0.13 R |
| bollinger | 234 | 53,8 % | -0.05 R |
| barrida | 101 | 48,5 % | -0.24 R |
| estocastico | 67 | 47,8 % | +0.18 R |
| ruptura | 15 | 53,3 % | +0.55 R |
| order_block | 14 | 28,6 % | -0.54 R |
| rsi | 8 | 37,5 % | -0.53 R |
| fibonacci | 6 | 50,0 % | +0.23 R |
| macd | 5 | 40,0 % | +0.01 R |
| velas | 4 | 25,0 % | -0.78 R |
| bos | 1 | 0,0 % | -1.05 R |
| choch | 1 | 0,0 % | -1.08 R |
| supertrend | 1 | 0,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 221 | 48,9 % | +0.02 R |
| 08-12 h | 127 | 40,2 % | -0.40 R |
| 12-16 h | 120 | 50,8 % | -0.00 R |
| 00-04 h | 117 | 53,8 % | -0.09 R |
| 16-20 h | 106 | 52,8 % | -0.23 R |
| 20-24 h | 92 | 59,8 % | +0.03 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 331 | 50,5 % | -0.09 R |
| lateral (<20) | 289 | 49,5 % | -0.12 R |
| débil (20-25) | 163 | 51,5 % | -0.09 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 432 | 48,4 % | -0.13 R |
| baja | 178 | 50,0 % | -0.07 R |
| alta | 173 | 55,5 % | -0.07 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 298 | 51,3 % | -0.06 R |
| a favor | 270 | 48,5 % | -0.12 R |
| en contra | 215 | 51,2 % | -0.14 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 571 | 51,1 % | -0.11 R |
| en contra | 209 | 47,4 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 513 | 50,3 % | -0.12 R |
| a favor | 270 | 50,4 % | -0.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 16/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -7.01 % |
| 14/12 09:00 | SOL/USDT | 4h | COMPRAR | 4800 min | barrida | -6.91 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**8 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **62,5 %** · resultado medio con SL/TP tras costes: **-1.05 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 5 | 80,0 % | -0.95 R |
| 52-55 % | 3 | 33,3 % | -1.21 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 3 | 33,3 % | -1.20 R |
| USD/JPY | 2 | 100,0 % | -0.63 R |
| EUR/GBP | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 4 | 50,0 % | -1.20 R |
| 5m | 4 | 75,0 % | -0.90 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 4 | 75,0 % | -0.93 R |
| 30-59 min | 3 | 33,3 % | -1.16 R |
| 2-4 h | 1 | 100,0 % | -1.22 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| barrida | 2 | 50,0 % | -1.16 R |
| bollinger | 2 | 50,0 % | -1.23 R |
| estocastico | 2 | 50,0 % | -1.18 R |
| soportes | 2 | 100,0 % | -0.63 R |
| macd | 1 | 0,0 % | -1.20 R |
| rsi | 1 | 100,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 3 | 33,3 % | -1.21 R |
| 00-04 h | 2 | 100,0 % | -0.68 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 16-20 h | 1 | 100,0 % | -1.15 R |
| 20-24 h | 1 | 0,0 % | -1.12 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 3 | 33,3 % | -1.16 R |
| fuerte (≥25) | 3 | 66,7 % | -0.83 R |
| lateral (<20) | 2 | 100,0 % | -1.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 3 | 33,3 % | -1.15 R |
| alta | 3 | 100,0 % | -0.84 R |
| baja | 2 | 50,0 % | -1.22 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 5 | 60,0 % | -1.18 R |
| en contra | 2 | 50,0 % | -1.18 R |
| sin tendencia | 1 | 100,0 % | -0.13 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 7 | 57,1 % | -1.18 R |
| en contra | 1 | 100,0 % | -0.13 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 5 | 60,0 % | -1.19 R |
| a favor | 3 | 66,7 % | -0.82 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**7 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **28,6 %** · resultado medio con SL/TP tras costes: **-1.09 R** · no se distingue del azar todavía (z = -1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 5 | 40,0 % | -1.06 R |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 4 | 50,0 % | — |
| GBP/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 5 | 40,0 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 3 | 66,7 % | — |
| 4-12 h | 2 | 0,0 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 4 | 50,0 % | — |
| estocastico | 2 | 0,0 % | -1.09 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 2 | 50,0 % | -1.06 R |
| 08-12 h | 1 | 0,0 % | — |
| 20-24 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| lateral (<20) | 3 | 33,3 % | — |
| débil (20-25) | 3 | 33,3 % | -1.06 R |
| fuerte (≥25) | 1 | 0,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 5 | 20,0 % | -1.06 R |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 6 | 33,3 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 7 | 28,6 % | -1.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 6 | 33,3 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
