# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**641 señales** del 18/03/2026 al 30/10/2026. Acierto (precio a favor al vencer): **52,0 %** · resultado medio con SL/TP tras costes: **-0.15 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| franja = **20-24 h** | acierta | 66,7 % en 39 | después 68,3 % en 41 casos | ✅ confirmado |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 291 | 50,2 % | -0.20 R |
| 52-55 % | 257 | 54,5 % | -0.08 R |
| 55-58 % | 87 | 50,6 % | -0.24 R |
| ≥58 % | 6 | 50,0 % | +0.51 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 183 | 52,5 % | -0.16 R |
| Oro (XAU/USD) | 164 | 51,8 % | -0.08 R |
| USD/CHF | 66 | 63,6 % | -0.07 R |
| EUR/GBP | 65 | 41,5 % | -0.46 R |
| BTC/USDT | 50 | 58,0 % | -0.02 R |
| SOL/USDT | 44 | 40,9 % | -0.11 R |
| USD/JPY | 24 | 62,5 % | -0.18 R |
| USD/CAD | 21 | 42,9 % | -0.54 R |
| GBP/JPY | 9 | 44,4 % | -0.41 R |
| XRP/USDT | 7 | 42,9 % | +0.23 R |
| ETH/USDT | 4 | 25,0 % | +0.13 R |
| EUR/USD | 4 | 100,0 % | +0.93 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 279 | 54,1 % | -0.14 R |
| 5m | 206 | 53,9 % | -0.19 R |
| 1h | 156 | 45,5 % | -0.12 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 30-59 min | 272 | 55,1 % | -0.02 R |
| 2-4 h | 193 | 46,6 % | -0.22 R |
| 1-2 h | 176 | 52,8 % | -0.28 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 222 | 46,8 % | -0.27 R |
| velas | 147 | 50,3 % | -0.18 R |
| estocastico | 127 | 55,9 % | -0.10 R |
| barrida | 63 | 63,5 % | +0.07 R |
| bos | 46 | 50,0 % | -0.01 R |
| soportes | 28 | 57,1 % | -0.20 R |
| rsi | 20 | 50,0 % | -0.22 R |
| macd | 4 | 50,0 % | +0.27 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 139 | 54,7 % | -0.25 R |
| 08-12 h | 127 | 49,6 % | -0.20 R |
| 16-20 h | 125 | 51,2 % | -0.12 R |
| 00-04 h | 94 | 48,9 % | -0.13 R |
| 20-24 h | 80 | 67,5 % | -0.06 R |
| 04-08 h | 76 | 39,5 % | -0.05 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 302 | 51,7 % | -0.19 R |
| lateral (<20) | 219 | 51,1 % | -0.12 R |
| débil (20-25) | 120 | 54,2 % | -0.10 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 365 | 51,8 % | -0.03 R |
| alta | 199 | 51,8 % | -0.31 R |
| baja | 77 | 53,2 % | -0.33 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 267 | 53,2 % | -0.05 R |
| a favor | 252 | 52,0 % | -0.18 R |
| en contra | 122 | 49,2 % | -0.30 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 458 | 51,7 % | -0.11 R |
| en contra | 181 | 52,5 % | -0.26 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 413 | 51,3 % | -0.14 R |
| a favor | 228 | 53,1 % | -0.17 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.79 % |
| 18/10 23:20 | SOL/USDT | 5m | VENDER | 50 min | bollinger | -1.61 % |
| 18/05 14:00 | SOL/USDT | 1h | COMPRAR | 180 min | macd | -1.60 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 27/10 12:30 | Oro (XAU/USD) | 15m | VENDER | 225 min | velas | -1.24 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**830 señales** del 08/01/2021 al 29/10/2026. Acierto (precio a favor al vencer): **50,5 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 65,5 % en 55 | después 53,6 % en 69 casos | ❔ no se repite |
| mercado = **ETH/USDT** | falla | 28,3 % en 46 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **1h** | acierta | 61,1 % en 157 | después 48,2 % en 257 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 68,0 % en 50 | después 50,9 % en 55 casos | ❔ no se repite |
| volatilidad = **alta** | acierta | 62,2 % en 90 | después 46,2 % en 93 casos | ❔ no se repite |
| confianza_tramo = **52-55 %** | acierta | 59,8 % en 184 | después 52,7 % en 146 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 443 | 46,0 % | -0.20 R |
| 52-55 % | 330 | 56,7 % | -0.12 R |
| 55-58 % | 57 | 49,1 % | +0.14 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 202 | 51,5 % | -0.19 R |
| GBP/JPY | 124 | 58,9 % | -0.19 R |
| Oro (XAU/USD) | 118 | 50,0 % | +0.05 R |
| SOL/USDT | 114 | 49,1 % | -0.24 R |
| GBP/USD | 97 | 53,6 % | -0.12 R |
| ETH/USDT | 52 | 26,9 % | -0.36 R |
| EUR/GBP | 43 | 39,5 % | -0.41 R |
| AUD/USD | 40 | 52,5 % | +0.40 R |
| XRP/USDT | 23 | 60,9 % | +0.05 R |
| USD/JPY | 9 | 33,3 % | -0.61 R |
| EUR/JPY | 5 | 80,0 % | -0.45 R |
| EUR/USD | 2 | 100,0 % | +2.50 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 414 | 53,1 % | -0.18 R |
| 4h | 237 | 46,4 % | -0.22 R |
| 1d | 140 | 51,4 % | +0.10 R |
| 15m | 39 | 43,6 % | -0.21 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 300 | 52,3 % | -0.13 R |
| 2-5 días | 244 | 50,0 % | -0.04 R |
| 4-12 h | 222 | 48,2 % | -0.32 R |
| 1-2 días | 64 | 51,6 % | +0.04 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 325 | 48,6 % | -0.16 R |
| bollinger | 257 | 53,7 % | -0.13 R |
| barrida | 97 | 51,5 % | -0.16 R |
| estocastico | 83 | 50,6 % | -0.07 R |
| order_block | 16 | 31,2 % | -0.48 R |
| ruptura | 16 | 50,0 % | +0.62 R |
| macd | 13 | 46,2 % | -0.26 R |
| rsi | 10 | 40,0 % | -0.66 R |
| fibonacci | 8 | 62,5 % | +0.60 R |
| velas | 4 | 25,0 % | -0.78 R |
| choch | 3 | 100,0 % | -0.69 R |
| bos | 1 | 0,0 % | -1.05 R |
| supertrend | 1 | 0,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 214 | 49,5 % | -0.03 R |
| 08-12 h | 147 | 47,6 % | -0.34 R |
| 00-04 h | 125 | 52,0 % | -0.10 R |
| 12-16 h | 120 | 45,0 % | -0.12 R |
| 16-20 h | 119 | 52,1 % | -0.19 R |
| 20-24 h | 105 | 59,0 % | -0.11 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 350 | 48,9 % | -0.12 R |
| lateral (<20) | 316 | 51,6 % | -0.13 R |
| débil (20-25) | 164 | 51,8 % | -0.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 454 | 48,5 % | -0.17 R |
| baja | 193 | 51,8 % | -0.10 R |
| alta | 183 | 54,1 % | -0.11 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 298 | 52,0 % | -0.13 R |
| a favor | 281 | 49,1 % | -0.14 R |
| en contra | 251 | 50,2 % | -0.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 599 | 51,1 % | -0.16 R |
| en contra | 227 | 48,0 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 540 | 49,3 % | -0.21 R |
| a favor | 290 | 52,8 % | -0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 01/06 18:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.84 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 16/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -7.01 % |
| 14/12 09:00 | SOL/USDT | 4h | COMPRAR | 4800 min | barrida | -6.91 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 19/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -5.99 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**8 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **62,5 %** · resultado medio con SL/TP tras costes: **-1.04 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 5 | 80,0 % | -0.91 R |
| 52-55 % | 3 | 33,3 % | -1.21 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 3 | 33,3 % | -1.20 R |
| USD/JPY | 2 | 100,0 % | -0.63 R |
| EUR/GBP | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | — |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 4 | 50,0 % | -1.22 R |
| 5m | 4 | 75,0 % | -0.90 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 4 | 75,0 % | -0.93 R |
| 30-59 min | 3 | 33,3 % | -1.18 R |
| 2-4 h | 1 | 100,0 % | -1.22 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| barrida | 2 | 50,0 % | -1.21 R |
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
| 20-24 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 3 | 33,3 % | -1.19 R |
| fuerte (≥25) | 3 | 66,7 % | -0.83 R |
| lateral (<20) | 2 | 100,0 % | -1.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 3 | 33,3 % | -1.17 R |
| alta | 3 | 100,0 % | -0.84 R |
| baja | 2 | 50,0 % | -1.22 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 5 | 60,0 % | -1.20 R |
| en contra | 2 | 50,0 % | -1.18 R |
| sin tendencia | 1 | 100,0 % | -0.13 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 7 | 57,1 % | -1.19 R |
| en contra | 1 | 100,0 % | -0.13 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 5 | 60,0 % | -1.19 R |
| a favor | 3 | 66,7 % | -0.67 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**5 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **20,0 %** · resultado medio con SL/TP tras costes: **-1.12 R** · no se distingue del azar todavía (z = -1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 3 | 33,3 % | — |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 2 | 50,0 % | — |
| GBP/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | — |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 3 | 33,3 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | — |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 2 | 0,0 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | — |
| 2-5 días | 1 | 100,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 2 | 50,0 % | — |
| estocastico | 2 | 0,0 % | -1.12 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 2 | 0,0 % | -1.12 R |
| 12-16 h | 2 | 50,0 % | — |
| 08-12 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 3 | 33,3 % | — |
| lateral (<20) | 1 | 0,0 % | — |
| fuerte (≥25) | 1 | 0,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 3 | 0,0 % | — |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 4 | 25,0 % | -1.12 R |
| a favor | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 5 | 20,0 % | -1.12 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 4 | 25,0 % | -1.12 R |
| a favor | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
