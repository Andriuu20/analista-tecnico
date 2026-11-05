# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**723 señales** del 18/03/2026 al 05/11/2026. Acierto (precio a favor al vencer): **51,6 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = 0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | falla | 27,5 % en 40 | después 59,4 % en 106 casos | ❔ no se repite |
| dia = **lun** | falla | 36,5 % en 74 | después 58,3 % en 60 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | falla | 40,4 % en 114 | después 54,5 % en 112 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 391 | 49,1 % | -0.18 R |
| 52-55 % | 276 | 56,2 % | -0.16 R |
| 55-58 % | 52 | 48,1 % | -0.35 R |
| ≥58 % | 4 | 25,0 % | -0.71 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 181 | 51,9 % | -0.15 R |
| USD/JPY | 146 | 50,7 % | -0.32 R |
| USD/CHF | 132 | 56,1 % | -0.05 R |
| Oro (XAU/USD) | 103 | 46,6 % | -0.17 R |
| EUR/GBP | 70 | 55,7 % | -0.32 R |
| GBP/JPY | 36 | 61,1 % | -0.05 R |
| SOL/USDT | 25 | 32,0 % | -0.42 R |
| ETH/USDT | 15 | 53,3 % | -0.10 R |
| BTC/USDT | 14 | 42,9 % | -0.01 R |
| GBP/USD | 1 | 0,0 % | -1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 320 | 54,1 % | -0.21 R |
| 15m | 226 | 54,0 % | -0.16 R |
| 1h | 174 | 43,7 % | -0.18 R |
| 4h | 3 | 66,7 % | -0.04 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 383 | 53,5 % | -0.21 R |
| 2-4 h | 198 | 44,4 % | -0.15 R |
| 30-59 min | 142 | 56,3 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 335 | 50,7 % | -0.19 R |
| soportes | 105 | 52,4 % | -0.36 R |
| estocastico | 76 | 50,0 % | -0.13 R |
| velas | 71 | 47,9 % | -0.20 R |
| barrida | 63 | 61,9 % | -0.01 R |
| bos | 43 | 44,2 % | -0.21 R |
| rsi | 34 | 73,5 % | +0.04 R |
| macd | 5 | 20,0 % | -0.61 R |
| divergencia | 2 | 0,0 % | +0.91 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 148 | 55,4 % | -0.18 R |
| 16-20 h | 145 | 52,4 % | -0.15 R |
| 08-12 h | 124 | 49,2 % | -0.17 R |
| 00-04 h | 110 | 49,1 % | -0.31 R |
| 04-08 h | 100 | 45,0 % | -0.02 R |
| 20-24 h | 96 | 57,3 % | -0.32 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 354 | 54,5 % | -0.07 R |
| lateral (<20) | 226 | 47,3 % | -0.29 R |
| débil (20-25) | 143 | 51,0 % | -0.31 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 409 | 50,1 % | -0.10 R |
| alta | 220 | 55,0 % | -0.26 R |
| baja | 94 | 50,0 % | -0.40 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 301 | 50,2 % | -0.15 R |
| a favor | 240 | 52,1 % | -0.15 R |
| en contra | 182 | 53,3 % | -0.29 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 540 | 51,3 % | -0.17 R |
| en contra | 182 | 52,2 % | -0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 511 | 52,4 % | -0.19 R |
| a favor | 212 | 49,5 % | -0.19 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 25/08 04:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -0.96 % |
| 18/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.96 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**784 señales** del 08/01/2021 al 05/11/2026. Acierto (precio a favor al vencer): **53,6 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = 2.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 66,0 % en 53 | después 56,2 % en 89 casos | ✅ confirmado |
| estructura_txt = **a favor** | acierta | 58,9 % en 141 | después 58,3 % en 132 casos | ✅ confirmado |
| confianza_tramo = **52-55 %** | acierta | 59,9 % en 172 | después 56,6 % en 145 casos | ✅ confirmado |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 431 | 50,6 % | -0.08 R |
| 52-55 % | 317 | 58,4 % | -0.05 R |
| 55-58 % | 36 | 47,2 % | -0.08 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 142 | 59,9 % | -0.09 R |
| USD/CHF | 121 | 53,7 % | -0.14 R |
| SOL/USDT | 120 | 59,2 % | +0.13 R |
| Oro (XAU/USD) | 116 | 52,6 % | +0.08 R |
| GBP/USD | 73 | 54,8 % | -0.13 R |
| ETH/USDT | 66 | 36,4 % | -0.32 R |
| EUR/GBP | 48 | 52,1 % | -0.25 R |
| USD/JPY | 33 | 39,4 % | -0.15 R |
| AUD/USD | 31 | 51,6 % | +0.09 R |
| EUR/JPY | 22 | 68,2 % | -0.15 R |
| XRP/USDT | 9 | 44,4 % | -0.09 R |
| EUR/USD | 3 | 33,3 % | -0.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 325 | 55,4 % | -0.16 R |
| 4h | 300 | 52,0 % | -0.10 R |
| 1d | 138 | 52,9 % | +0.13 R |
| 15m | 21 | 52,4 % | +0.38 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 255 | 53,7 % | -0.01 R |
| 12-24 h | 247 | 51,8 % | -0.18 R |
| 4-12 h | 198 | 55,6 % | -0.07 R |
| 1-2 días | 84 | 53,6 % | +0.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 300 | 51,0 % | -0.07 R |
| bollinger | 294 | 56,1 % | -0.03 R |
| barrida | 83 | 54,2 % | -0.14 R |
| estocastico | 64 | 54,7 % | +0.13 R |
| choch | 22 | 68,2 % | -0.15 R |
| bos | 8 | 37,5 % | -0.44 R |
| ruptura | 7 | 42,9 % | -0.48 R |
| fibonacci | 6 | 66,7 % | +0.22 R |
| order_block | 3 | 0,0 % | -0.35 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 217 | 53,9 % | +0.06 R |
| 08-12 h | 126 | 53,2 % | -0.25 R |
| 00-04 h | 121 | 54,5 % | -0.01 R |
| 12-16 h | 120 | 53,3 % | +0.05 R |
| 16-20 h | 103 | 48,5 % | -0.27 R |
| 20-24 h | 97 | 57,7 % | -0.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 329 | 53,8 % | -0.04 R |
| lateral (<20) | 297 | 53,2 % | -0.10 R |
| débil (20-25) | 158 | 53,8 % | -0.06 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 436 | 52,8 % | -0.06 R |
| baja | 182 | 53,3 % | -0.08 R |
| alta | 166 | 56,0 % | -0.07 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 289 | 55,4 % | -0.05 R |
| a favor | 272 | 52,6 % | -0.06 R |
| en contra | 223 | 52,5 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 563 | 53,6 % | -0.08 R |
| en contra | 215 | 52,6 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 511 | 50,9 % | -0.11 R |
| a favor | 273 | 58,6 % | +0.01 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 2400 min | bollinger | -8.81 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 19/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -5.99 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**24 señales** del 28/10/2026 al 05/11/2026. Acierto (precio a favor al vencer): **54,2 %** · resultado medio con SL/TP tras costes: **-0.40 R** · no se distingue del azar todavía (z = 0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 17 | 58,8 % | -0.34 R |
| 52-55 % | 6 | 33,3 % | -0.41 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 8 | 62,5 % | -0.18 R |
| EUR/JPY | 7 | 42,9 % | -0.74 R |
| EUR/GBP | 3 | 33,3 % | -0.37 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 14 | 57,1 % | -0.47 R |
| 15m | 10 | 50,0 % | -0.28 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 15 | 40,0 % | -0.46 R |
| 30-59 min | 6 | 66,7 % | -0.72 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 8 | 25,0 % | -0.53 R |
| soportes | 8 | 62,5 % | -0.18 R |
| estocastico | 4 | 75,0 % | -0.43 R |
| rsi | 3 | 100,0 % | -0.43 R |
| barrida | 2 | 50,0 % | -1.16 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 8 | 50,0 % | -0.78 R |
| 00-04 h | 6 | 83,3 % | -0.36 R |
| 20-24 h | 5 | 20,0 % | -0.15 R |
| 16-20 h | 4 | 50,0 % | +0.20 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 13 | 69,2 % | +0.20 R |
| lateral (<20) | 6 | 50,0 % | -1.19 R |
| débil (20-25) | 5 | 20,0 % | -1.19 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 10 | 50,0 % | -0.07 R |
| alta | 10 | 60,0 % | -0.30 R |
| baja | 4 | 50,0 % | -1.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 13 | 61,5 % | -0.55 R |
| en contra | 7 | 57,1 % | +0.13 R |
| sin tendencia | 4 | 25,0 % | -0.86 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 18 | 55,6 % | -0.40 R |
| en contra | 6 | 50,0 % | -0.38 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 17 | 52,9 % | -0.36 R |
| a favor | 7 | 57,1 % | -0.50 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 05/11 15:50 | EUR/JPY | 5m | COMPRAR | 75 min | bollinger | -0.16 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |
| 05/11 21:15 | USD/JPY | 5m | COMPRAR | 100 min | soportes | -0.11 % |
| 02/11 19:05 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.07 % |
| 04/11 02:45 | EUR/GBP | 15m | VENDER | 75 min | bollinger | -0.04 % |
| 05/11 20:30 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.03 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**9 señales** del 28/10/2026 al 04/11/2026. Acierto (precio a favor al vencer): **33,3 %** · resultado medio con SL/TP tras costes: **-1.09 R** · no se distingue del azar todavía (z = -1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 7 | 42,9 % | -1.06 R |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 5 | 40,0 % | — |
| GBP/JPY | 2 | 50,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 7 | 42,9 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 4 | 50,0 % | — |
| 4-12 h | 3 | 33,3 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 6 | 50,0 % | — |
| estocastico | 2 | 0,0 % | -1.09 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 3 | 66,7 % | -1.06 R |
| 08-12 h | 1 | 0,0 % | — |
| 16-20 h | 1 | 0,0 % | — |
| 20-24 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 4 | 25,0 % | -1.06 R |
| lateral (<20) | 3 | 33,3 % | — |
| fuerte (≥25) | 2 | 50,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 7 | 28,6 % | -1.06 R |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 7 | 28,6 % | -1.09 R |
| a favor | 2 | 50,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 9 | 33,3 % | -1.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 8 | 37,5 % | -1.09 R |
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
