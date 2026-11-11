# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**875 señales** del 12/08/2025 al 11/11/2026. Acierto (precio a favor al vencer): **52,2 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **jue** | acierta | 62,6 % en 99 | después 46,9 % en 98 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 547 | 50,8 % | -0.12 R |
| 52-55 % | 286 | 55,2 % | -0.10 R |
| 55-58 % | 39 | 51,3 % | -0.18 R |
| ≥58 % | 3 | 33,3 % | -0.53 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 203 | 55,2 % | -0.02 R |
| EUR/JPY | 168 | 44,6 % | -0.23 R |
| EUR/GBP | 126 | 47,6 % | -0.22 R |
| USD/CHF | 102 | 59,8 % | -0.10 R |
| Oro (XAU/USD) | 89 | 55,1 % | -0.08 R |
| XRP/USDT | 71 | 54,9 % | -0.06 R |
| GBP/JPY | 46 | 56,5 % | -0.00 R |
| BTC/USDT | 28 | 50,0 % | -0.37 R |
| SOL/USDT | 27 | 55,6 % | -0.12 R |
| ETH/USDT | 10 | 30,0 % | -0.37 R |
| USD/CAD | 3 | 100,0 % | +1.40 R |
| EUR/USD | 1 | 0,0 % | -1.14 R |
| GBP/USD | 1 | 0,0 % | +1.82 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 265 | 48,3 % | -0.09 R |
| 5m | 260 | 51,5 % | -0.20 R |
| 15m | 232 | 54,3 % | -0.10 R |
| 4h | 118 | 58,5 % | -0.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 400 | 51,0 % | -0.17 R |
| 2-4 h | 396 | 51,0 % | -0.09 R |
| 30-59 min | 79 | 64,6 % | -0.01 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 383 | 49,9 % | -0.19 R |
| velas | 138 | 55,8 % | +0.03 R |
| soportes | 102 | 50,0 % | -0.29 R |
| barrida | 80 | 66,2 % | +0.07 R |
| bos | 63 | 58,7 % | +0.20 R |
| estocastico | 56 | 41,1 % | -0.22 R |
| rsi | 36 | 50,0 % | +0.08 R |
| fibonacci | 29 | 37,9 % | -0.52 R |
| divergencia | 5 | 40,0 % | +0.94 R |
| macd | 5 | 60,0 % | -0.67 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 198 | 52,0 % | -0.11 R |
| 12-16 h | 179 | 52,0 % | -0.28 R |
| 20-24 h | 140 | 55,0 % | -0.09 R |
| 00-04 h | 123 | 56,1 % | -0.13 R |
| 08-12 h | 122 | 49,2 % | -0.20 R |
| 04-08 h | 113 | 48,7 % | +0.19 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 403 | 53,3 % | -0.10 R |
| lateral (<20) | 312 | 51,9 % | -0.15 R |
| débil (20-25) | 160 | 50,0 % | -0.10 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 483 | 51,1 % | -0.14 R |
| alta | 244 | 52,9 % | -0.06 R |
| baja | 148 | 54,7 % | -0.14 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 354 | 55,6 % | -0.03 R |
| sin tendencia | 344 | 50,9 % | -0.19 R |
| en contra | 177 | 48,0 % | -0.17 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 599 | 51,3 % | -0.16 R |
| en contra | 268 | 53,7 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 585 | 51,5 % | -0.17 R |
| a favor | 290 | 53,8 % | -0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.80 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 50 min | bollinger | -1.47 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 08/07 02:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.34 % |
| 09/11 06:45 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 05/11 16:15 | XRP/USDT | 5m | COMPRAR | 50 min | bollinger | -1.20 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**922 señales** del 08/01/2021 al 10/11/2026. Acierto (precio a favor al vencer): **50,8 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 62,5 % en 64 | después 52,5 % en 101 casos | ❔ no se repite |
| temporalidad = **1h** | acierta | 58,8 % en 165 | después 51,2 % en 215 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 64,7 % en 51 | después 49,0 % en 49 casos | ❔ no se repite |
| confianza_tramo = **52-55 %** | acierta | 57,3 % en 213 | después 48,2 % en 168 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 503 | 50,1 % | -0.11 R |
| 52-55 % | 381 | 53,3 % | -0.07 R |
| 55-58 % | 38 | 34,2 % | -0.32 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 173 | 51,4 % | -0.07 R |
| GBP/JPY | 165 | 56,4 % | -0.19 R |
| SOL/USDT | 129 | 52,7 % | -0.00 R |
| Oro (XAU/USD) | 114 | 51,8 % | -0.03 R |
| GBP/USD | 94 | 55,3 % | -0.11 R |
| EUR/GBP | 75 | 48,0 % | -0.22 R |
| ETH/USDT | 75 | 37,3 % | -0.23 R |
| AUD/USD | 38 | 52,6 % | +0.30 R |
| USD/JPY | 35 | 31,4 % | -0.33 R |
| EUR/JPY | 15 | 66,7 % | +0.15 R |
| XRP/USDT | 7 | 28,6 % | -0.65 R |
| BTC/USDT | 2 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 380 | 54,5 % | -0.14 R |
| 4h | 322 | 47,8 % | -0.16 R |
| 1d | 136 | 52,2 % | +0.03 R |
| 15m | 84 | 42,9 % | +0.08 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 295 | 50,2 % | -0.05 R |
| 12-24 h | 291 | 51,2 % | -0.21 R |
| 4-12 h | 272 | 50,0 % | -0.09 R |
| 1-2 días | 64 | 54,7 % | +0.09 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 338 | 53,8 % | -0.03 R |
| soportes | 335 | 49,0 % | -0.19 R |
| estocastico | 106 | 48,1 % | +0.01 R |
| barrida | 104 | 53,8 % | -0.17 R |
| ruptura | 14 | 50,0 % | +0.38 R |
| choch | 9 | 66,7 % | +0.22 R |
| fibonacci | 7 | 28,6 % | -0.74 R |
| bos | 4 | 25,0 % | -0.84 R |
| rsi | 4 | 50,0 % | +0.07 R |
| order_block | 3 | 0,0 % | -0.35 R |
| velas | 3 | 0,0 % | -0.70 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 232 | 50,0 % | -0.05 R |
| 08-12 h | 155 | 50,3 % | -0.24 R |
| 00-04 h | 153 | 49,7 % | -0.13 R |
| 12-16 h | 153 | 50,3 % | -0.06 R |
| 16-20 h | 129 | 49,6 % | -0.13 R |
| 20-24 h | 100 | 57,0 % | -0.00 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 396 | 50,8 % | -0.06 R |
| lateral (<20) | 335 | 50,1 % | -0.14 R |
| débil (20-25) | 191 | 51,8 % | -0.14 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 498 | 50,2 % | -0.08 R |
| alta | 217 | 52,5 % | -0.13 R |
| baja | 207 | 50,2 % | -0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 345 | 47,0 % | -0.15 R |
| sin tendencia | 339 | 52,5 % | -0.06 R |
| en contra | 238 | 53,8 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 694 | 50,7 % | -0.10 R |
| en contra | 224 | 50,0 % | -0.12 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 627 | 49,9 % | -0.16 R |
| a favor | 295 | 52,5 % | +0.01 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**56 señales** del 28/10/2026 al 11/11/2026. Acierto (precio a favor al vencer): **55,4 %** · resultado medio con SL/TP tras costes: **-0.15 R** · no se distingue del azar todavía (z = 0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 38 | 63,2 % | -0.16 R |
| 52-55 % | 17 | 35,3 % | -0.05 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 19 | 68,4 % | -0.09 R |
| EUR/JPY | 16 | 43,8 % | -0.45 R |
| USD/CHF | 6 | 50,0 % | +0.64 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| BTC/USDT | 2 | 50,0 % | -0.05 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| XRP/USDT | 2 | 50,0 % | +0.28 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 29 | 58,6 % | -0.24 R |
| 15m | 25 | 52,0 % | -0.05 R |
| 1h | 2 | 50,0 % | -0.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 39 | 51,3 % | -0.06 R |
| 30-59 min | 14 | 57,1 % | -0.52 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 19 | 68,4 % | -0.09 R |
| bollinger | 18 | 38,9 % | -0.31 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| barrida | 7 | 42,9 % | +0.35 R |
| rsi | 5 | 80,0 % | -0.28 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 19 | 78,9 % | +0.17 R |
| 20-24 h | 10 | 30,0 % | -0.35 R |
| 16-20 h | 8 | 62,5 % | +0.38 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 04-08 h | 6 | 50,0 % | -0.66 R |
| 08-12 h | 5 | 20,0 % | +0.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 27 | 59,3 % | +0.08 R |
| débil (20-25) | 16 | 50,0 % | -0.40 R |
| lateral (<20) | 13 | 53,8 % | -0.33 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 31 | 51,6 % | -0.12 R |
| alta | 13 | 61,5 % | -0.25 R |
| baja | 12 | 58,3 % | -0.10 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 20 | 55,0 % | -0.24 R |
| sin tendencia | 19 | 63,2 % | -0.01 R |
| en contra | 17 | 47,1 % | -0.21 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 42 | 52,4 % | -0.15 R |
| en contra | 14 | 64,3 % | -0.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 42 | 54,8 % | -0.16 R |
| a favor | 14 | 57,1 % | -0.13 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 09/11 07:15 | USD/CHF | 15m | COMPRAR | 75 min | estocastico+barrida | -0.16 % |
| 05/11 15:50 | EUR/JPY | 5m | COMPRAR | 75 min | bollinger | -0.16 % |
| 05/11 21:45 | USD/JPY | 5m | COMPRAR | 100 min | soportes | -0.12 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**18 señales** del 28/10/2026 al 11/11/2026. Acierto (precio a favor al vencer): **38,9 %** · resultado medio con SL/TP tras costes: **-0.13 R** · no se distingue del azar todavía (z = -0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 10 | 40,0 % | -0.37 R |
| <52 % | 8 | 37,5 % | +0.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 7 | 42,9 % | -0.24 R |
| USD/CHF | 6 | 33,3 % | +0.36 R |
| GBP/JPY | 3 | 33,3 % | -1.05 R |
| ETH/USDT | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 11 | 45,5 % | -0.37 R |
| 15m | 6 | 33,3 % | +0.36 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 10 | 40,0 % | +0.12 R |
| 2-5 días | 6 | 50,0 % | -0.03 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 8 | 50,0 % | -0.24 R |
| estocastico | 8 | 25,0 % | +0.12 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 4 | 25,0 % | -1.09 R |
| 20-24 h | 4 | 50,0 % | +1.89 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 08-12 h | 3 | 33,3 % | +0.14 R |
| 16-20 h | 3 | 33,3 % | -1.02 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 9 | 55,6 % | -0.31 R |
| débil (20-25) | 6 | 16,7 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 13 | 30,8 % | -0.08 R |
| alta | 3 | 33,3 % | -1.12 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 14 | 42,9 % | -0.18 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 16 | 31,2 % | -0.03 R |
| en contra | 2 | 100,0 % | -1.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 14 | 35,7 % | -0.04 R |
| a favor | 4 | 50,0 % | -1.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 30/10 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -0.54 % |
| 11/11 09:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.32 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 06/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -0.09 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
| 06/11 17:00 | GBP/JPY | 4h | COMPRAR | 720 min | bollinger | -0.04 % |
| 05/11 22:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.03 % |
