# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**677 señales** del 15/09/2025 al 03/11/2026. Acierto (precio a favor al vencer): **50,8 %** · resultado medio con SL/TP tras costes: **-0.20 R** · no se distingue del azar todavía (z = 0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **mié** | falla | 35,7 % en 70 | después 53,4 % en 58 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 308 | 48,4 % | -0.21 R |
| 52-55 % | 307 | 55,4 % | -0.15 R |
| 55-58 % | 61 | 41,0 % | -0.42 R |
| ≥58 % | 1 | 0,0 % | +2.94 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 185 | 54,6 % | -0.11 R |
| Oro (XAU/USD) | 117 | 46,2 % | -0.24 R |
| USD/CHF | 112 | 57,1 % | -0.04 R |
| EUR/GBP | 71 | 49,3 % | -0.36 R |
| USD/JPY | 58 | 53,4 % | -0.43 R |
| BTC/USDT | 30 | 56,7 % | +0.23 R |
| SOL/USDT | 26 | 30,8 % | -0.59 R |
| GBP/JPY | 23 | 56,5 % | -0.15 R |
| GBP/USD | 19 | 42,1 % | -0.44 R |
| ETH/USDT | 18 | 38,9 % | -0.29 R |
| USD/CAD | 7 | 14,3 % | -0.83 R |
| XRP/USDT | 7 | 28,6 % | -0.62 R |
| AUD/USD | 3 | 66,7 % | +1.28 R |
| EUR/USD | 1 | 100,0 % | +0.92 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 275 | 53,5 % | -0.22 R |
| 15m | 261 | 52,1 % | -0.19 R |
| 1h | 141 | 43,3 % | -0.17 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 298 | 53,4 % | -0.27 R |
| 30-59 min | 224 | 52,7 % | -0.12 R |
| 2-4 h | 155 | 43,2 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 255 | 49,8 % | -0.24 R |
| estocastico | 151 | 55,0 % | -0.13 R |
| velas | 79 | 43,0 % | -0.28 R |
| barrida | 64 | 59,4 % | -0.01 R |
| soportes | 61 | 49,2 % | -0.43 R |
| bos | 39 | 46,2 % | -0.23 R |
| rsi | 33 | 63,6 % | +0.13 R |
| fibonacci | 9 | 33,3 % | -0.66 R |
| fvg | 5 | 40,0 % | -0.36 R |
| macd | 1 | 100,0 % | +1.81 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 143 | 55,9 % | -0.09 R |
| 12-16 h | 140 | 50,7 % | -0.37 R |
| 08-12 h | 129 | 49,6 % | -0.22 R |
| 00-04 h | 91 | 45,1 % | -0.26 R |
| 04-08 h | 88 | 43,2 % | +0.07 R |
| 20-24 h | 86 | 58,1 % | -0.29 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 325 | 55,1 % | -0.11 R |
| lateral (<20) | 216 | 44,9 % | -0.30 R |
| débil (20-25) | 136 | 50,0 % | -0.23 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 369 | 50,4 % | -0.14 R |
| alta | 223 | 52,9 % | -0.23 R |
| baja | 85 | 47,1 % | -0.34 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 292 | 52,4 % | -0.08 R |
| a favor | 228 | 50,9 % | -0.24 R |
| en contra | 157 | 47,8 % | -0.36 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 512 | 51,6 % | -0.13 R |
| en contra | 164 | 48,2 % | -0.40 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 477 | 50,1 % | -0.17 R |
| a favor | 200 | 52,5 % | -0.25 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 22/10 18:25 | XRP/USDT | 5m | COMPRAR | 100 min | soportes | -1.63 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 27/10 12:30 | Oro (XAU/USD) | 15m | VENDER | 225 min | fibonacci | -1.24 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**805 señales** del 08/01/2021 al 03/11/2026. Acierto (precio a favor al vencer): **51,4 %** · resultado medio con SL/TP tras costes: **-0.09 R** · no se distingue del azar todavía (z = 0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 63,3 % en 60 | después 55,7 % en 88 casos | ✅ confirmado |
| franja = **20-24 h** | acierta | 74,0 % en 50 | después 56,0 % en 50 casos | ❔ no se repite |
| dia = **vie** | acierta | 64,2 % en 67 | después 55,2 % en 67 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 452 | 50,4 % | -0.04 R |
| 52-55 % | 323 | 53,6 % | -0.15 R |
| 55-58 % | 30 | 43,3 % | -0.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 188 | 50,0 % | -0.23 R |
| GBP/JPY | 148 | 58,8 % | -0.06 R |
| Oro (XAU/USD) | 115 | 52,2 % | +0.08 R |
| SOL/USDT | 103 | 57,3 % | +0.10 R |
| GBP/USD | 73 | 50,7 % | -0.28 R |
| ETH/USDT | 62 | 41,9 % | -0.22 R |
| EUR/GBP | 41 | 51,2 % | -0.16 R |
| AUD/USD | 40 | 52,5 % | +0.40 R |
| USD/JPY | 22 | 27,3 % | -0.29 R |
| XRP/USDT | 11 | 27,3 % | -0.57 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |
| EUR/USD | 1 | 0,0 % | -1.03 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 392 | 51,5 % | -0.19 R |
| 4h | 247 | 51,0 % | -0.05 R |
| 1d | 138 | 52,9 % | +0.12 R |
| 15m | 28 | 46,4 % | -0.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 258 | 47,3 % | -0.17 R |
| 4-12 h | 254 | 54,7 % | -0.18 R |
| 2-5 días | 226 | 51,8 % | +0.04 R |
| 1-2 días | 67 | 53,7 % | +0.09 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 344 | 50,9 % | -0.12 R |
| bollinger | 277 | 56,3 % | -0.02 R |
| barrida | 88 | 48,9 % | -0.27 R |
| estocastico | 54 | 44,4 % | -0.03 R |
| ruptura | 16 | 50,0 % | +0.62 R |
| order_block | 12 | 25,0 % | -0.21 R |
| rsi | 10 | 40,0 % | -0.56 R |
| fibonacci | 6 | 50,0 % | +0.23 R |
| bos | 1 | 0,0 % | -0.25 R |
| supertrend | 1 | 0,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 207 | 50,7 % | +0.05 R |
| 08-12 h | 135 | 47,4 % | -0.34 R |
| 12-16 h | 132 | 49,2 % | -0.10 R |
| 00-04 h | 118 | 50,8 % | -0.01 R |
| 16-20 h | 113 | 48,7 % | -0.17 R |
| 20-24 h | 100 | 65,0 % | -0.03 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 326 | 52,5 % | -0.07 R |
| lateral (<20) | 312 | 50,0 % | -0.13 R |
| débil (20-25) | 167 | 52,1 % | -0.06 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 438 | 50,9 % | -0.11 R |
| alta | 186 | 53,8 % | -0.06 R |
| baja | 181 | 50,3 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 296 | 51,0 % | -0.10 R |
| a favor | 265 | 50,6 % | -0.10 R |
| en contra | 244 | 52,9 % | -0.07 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 595 | 52,1 % | -0.13 R |
| en contra | 207 | 48,8 % | +0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 535 | 50,5 % | -0.16 R |
| a favor | 270 | 53,3 % | +0.04 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |
| 14/10 22:00 | BTC/USDT | 4h | COMPRAR | 4800 min | fibonacci | -5.63 % |
| 07/10 22:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.54 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**12 señales** del 28/10/2026 al 02/11/2026. Acierto (precio a favor al vencer): **58,3 %** · resultado medio con SL/TP tras costes: **-0.70 R** · no se distingue del azar todavía (z = 0.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 9 | 66,7 % | -0.52 R |
| 52-55 % | 3 | 33,3 % | -1.21 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 4 | 50,0 % | -0.92 R |
| EUR/JPY | 3 | 33,3 % | -1.20 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| EUR/GBP | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 6 | 66,7 % | -0.39 R |
| 5m | 6 | 50,0 % | -1.01 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 6 | 50,0 % | -1.02 R |
| 30-59 min | 3 | 33,3 % | -1.16 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 4 | 50,0 % | -0.92 R |
| bollinger | 2 | 50,0 % | -1.23 R |
| barrida | 2 | 50,0 % | -1.16 R |
| estocastico | 2 | 50,0 % | -1.18 R |
| velas | 2 | 100,0 % | +1.23 R |
| rsi | 1 | 100,0 % | -1.15 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 100,0 % | -0.27 R |
| 12-16 h | 3 | 33,3 % | -1.21 R |
| 20-24 h | 3 | 33,3 % | -0.15 R |
| 16-20 h | 2 | 50,0 % | -1.16 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 5 | 80,0 % | -0.01 R |
| débil (20-25) | 4 | 25,0 % | -1.19 R |
| lateral (<20) | 3 | 66,7 % | -1.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 5 | 40,0 % | -0.83 R |
| alta | 4 | 100,0 % | -0.15 R |
| baja | 3 | 33,3 % | -1.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 5 | 60,0 % | -1.18 R |
| en contra | 5 | 60,0 % | -0.21 R |
| sin tendencia | 2 | 50,0 % | -0.69 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 9 | 66,7 % | -0.65 R |
| en contra | 3 | 33,3 % | -0.85 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 8 | 62,5 % | -0.59 R |
| a favor | 4 | 50,0 % | -0.91 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |
| 02/11 19:05 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.07 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**8 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **25,0 %** · resultado medio con SL/TP tras costes: **-1.09 R** · no se distingue del azar todavía (z = -1.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 6 | 33,3 % | -1.06 R |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 5 | 40,0 % | — |
| GBP/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 6 | 33,3 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 4 | 50,0 % | — |
| 4-12 h | 2 | 0,0 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 5 | 40,0 % | — |
| estocastico | 2 | 0,0 % | -1.09 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 2 | 50,0 % | -1.06 R |
| 08-12 h | 1 | 0,0 % | — |
| 16-20 h | 1 | 0,0 % | — |
| 20-24 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 4 | 25,0 % | -1.06 R |
| lateral (<20) | 3 | 33,3 % | — |
| fuerte (≥25) | 1 | 0,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 6 | 16,7 % | -1.06 R |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 7 | 28,6 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 8 | 25,0 % | -1.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 7 | 28,6 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 30/10 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -0.54 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
