# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**897 señales** del 21/01/2025 al 13/11/2026. Acierto (precio a favor al vencer): **53,2 %** · resultado medio con SL/TP tras costes: **-0.11 R** · no se distingue del azar todavía (z = 1.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 58,4 % en 154 | después 52,1 % en 96 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 58,2 % en 158 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 60,7 % en 107 | después 47,0 % en 115 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 59,9 % en 172 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 536 | 52,8 % | -0.10 R |
| 52-55 % | 323 | 54,5 % | -0.09 R |
| 55-58 % | 38 | 47,4 % | -0.42 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 250 | 56,0 % | -0.08 R |
| EUR/JPY | 143 | 46,2 % | -0.16 R |
| EUR/GBP | 96 | 51,0 % | -0.20 R |
| USD/CHF | 94 | 58,5 % | +0.09 R |
| GBP/JPY | 70 | 55,7 % | -0.15 R |
| Oro (XAU/USD) | 65 | 53,8 % | -0.04 R |
| SOL/USDT | 49 | 49,0 % | -0.48 R |
| XRP/USDT | 41 | 46,3 % | -0.08 R |
| EUR/USD | 39 | 59,0 % | +0.24 R |
| BTC/USDT | 27 | 51,9 % | -0.42 R |
| AUD/USD | 16 | 50,0 % | -0.16 R |
| ETH/USDT | 4 | 50,0 % | -1.13 R |
| USD/CAD | 3 | 100,0 % | +1.40 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 303 | 55,8 % | -0.04 R |
| 1h | 258 | 48,4 % | -0.10 R |
| 5m | 178 | 51,1 % | -0.22 R |
| 4h | 158 | 58,2 % | -0.12 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 489 | 52,8 % | -0.08 R |
| 1-2 h | 368 | 53,0 % | -0.15 R |
| 30-59 min | 40 | 60,0 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 340 | 48,2 % | -0.18 R |
| velas | 174 | 59,2 % | -0.08 R |
| soportes | 98 | 53,1 % | -0.27 R |
| barrida | 77 | 62,3 % | +0.06 R |
| fibonacci | 64 | 53,1 % | -0.09 R |
| rsi | 59 | 50,8 % | -0.22 R |
| bos | 52 | 55,8 % | +0.15 R |
| estocastico | 27 | 48,1 % | -0.01 R |
| supertrend | 6 | 66,7 % | +0.22 R |
| divergencia | 5 | 40,0 % | +0.94 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 179 | 49,2 % | -0.19 R |
| 12-16 h | 174 | 54,6 % | -0.18 R |
| 00-04 h | 151 | 53,6 % | -0.13 R |
| 20-24 h | 142 | 59,9 % | -0.10 R |
| 08-12 h | 135 | 49,6 % | -0.09 R |
| 04-08 h | 116 | 52,6 % | +0.12 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 411 | 55,0 % | -0.12 R |
| lateral (<20) | 324 | 53,1 % | -0.06 R |
| débil (20-25) | 162 | 48,8 % | -0.17 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 484 | 51,9 % | -0.13 R |
| alta | 252 | 54,4 % | -0.05 R |
| baja | 161 | 55,3 % | -0.16 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 402 | 53,5 % | -0.12 R |
| a favor | 344 | 53,8 % | -0.03 R |
| en contra | 151 | 51,0 % | -0.27 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 597 | 52,6 % | -0.14 R |
| en contra | 291 | 54,3 % | -0.05 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 586 | 52,7 % | -0.11 R |
| a favor | 311 | 54,0 % | -0.12 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 03:15 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -2.00 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.80 % |
| 13/11 06:50 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -1.79 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 08/07 02:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.34 % |
| 09/11 06:45 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 08/10 13:15 | SOL/USDT | 15m | COMPRAR | 150 min | estocastico | -1.21 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**847 señales** del 08/01/2021 al 09/11/2026. Acierto (precio a favor al vencer): **52,2 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 439 | 54,0 % | -0.04 R |
| 52-55 % | 363 | 50,7 % | -0.16 R |
| 55-58 % | 45 | 46,7 % | -0.25 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 158 | 56,3 % | -0.18 R |
| SOL/USDT | 136 | 55,1 % | -0.06 R |
| Oro (XAU/USD) | 114 | 51,8 % | -0.03 R |
| GBP/JPY | 106 | 56,6 % | -0.11 R |
| GBP/USD | 85 | 51,8 % | -0.09 R |
| ETH/USDT | 71 | 38,0 % | -0.18 R |
| EUR/GBP | 57 | 47,4 % | -0.21 R |
| USD/JPY | 43 | 53,5 % | +0.17 R |
| EUR/JPY | 36 | 50,0 % | -0.40 R |
| AUD/USD | 34 | 52,9 % | +0.22 R |
| XRP/USDT | 5 | 20,0 % | -0.47 R |
| BTC/USDT | 2 | 50,0 % | -0.54 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 346 | 54,9 % | -0.13 R |
| 4h | 291 | 50,2 % | -0.13 R |
| 1d | 136 | 52,2 % | +0.03 R |
| 15m | 74 | 47,3 % | -0.10 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 298 | 50,3 % | -0.06 R |
| 12-24 h | 247 | 53,0 % | -0.20 R |
| 4-12 h | 245 | 52,2 % | -0.09 R |
| 1-2 días | 57 | 57,9 % | +0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 322 | 52,2 % | -0.14 R |
| bollinger | 288 | 53,5 % | -0.02 R |
| estocastico | 112 | 50,9 % | -0.15 R |
| barrida | 92 | 52,2 % | -0.10 R |
| order_block | 13 | 46,2 % | -0.06 R |
| ruptura | 10 | 50,0 % | +0.16 R |
| choch | 9 | 55,6 % | -0.22 R |
| fibonacci | 5 | 60,0 % | -0.63 R |
| bos | 4 | 50,0 % | +0.16 R |
| velas | 4 | 0,0 % | -0.78 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 228 | 50,4 % | -0.05 R |
| 08-12 h | 140 | 49,3 % | -0.24 R |
| 00-04 h | 135 | 57,8 % | +0.02 R |
| 12-16 h | 129 | 52,7 % | -0.14 R |
| 16-20 h | 119 | 49,6 % | -0.14 R |
| 20-24 h | 96 | 55,2 % | -0.09 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 353 | 51,3 % | -0.04 R |
| lateral (<20) | 318 | 51,9 % | -0.12 R |
| débil (20-25) | 176 | 54,5 % | -0.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 465 | 51,0 % | -0.09 R |
| baja | 193 | 53,9 % | -0.15 R |
| alta | 189 | 53,4 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 313 | 50,5 % | -0.11 R |
| sin tendencia | 306 | 51,3 % | -0.02 R |
| en contra | 228 | 55,7 % | -0.20 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 618 | 51,5 % | -0.13 R |
| en contra | 224 | 54,0 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 556 | 51,4 % | -0.19 R |
| a favor | 291 | 53,6 % | +0.07 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**70 señales** del 28/10/2026 al 13/11/2026. Acierto (precio a favor al vencer): **55,7 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 47 | 61,7 % | -0.21 R |
| 52-55 % | 22 | 40,9 % | -0.05 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 24 | 75,0 % | +0.04 R |
| EUR/JPY | 21 | 38,1 % | -0.57 R |
| USD/CHF | 9 | 44,4 % | +0.17 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| BTC/USDT | 3 | 66,7 % | -0.05 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| XRP/USDT | 2 | 50,0 % | +0.28 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 34 | 64,7 % | -0.13 R |
| 15m | 33 | 45,5 % | -0.24 R |
| 1h | 3 | 66,7 % | -0.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 52 | 53,8 % | -0.10 R |
| 30-59 min | 15 | 53,3 % | -0.56 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 24 | 75,0 % | +0.04 R |
| bollinger | 23 | 34,8 % | -0.46 R |
| barrida | 10 | 40,0 % | +0.04 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| rsi | 6 | 83,3 % | -0.28 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 21 | 76,2 % | +0.08 R |
| 08-12 h | 11 | 54,5 % | -0.10 R |
| 04-08 h | 10 | 50,0 % | -0.19 R |
| 16-20 h | 10 | 50,0 % | -0.09 R |
| 20-24 h | 10 | 30,0 % | -0.35 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 32 | 56,2 % | +0.01 R |
| lateral (<20) | 21 | 61,9 % | -0.20 R |
| débil (20-25) | 17 | 47,1 % | -0.50 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 41 | 51,2 % | -0.22 R |
| alta | 16 | 62,5 % | -0.19 R |
| baja | 13 | 61,5 % | -0.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 26 | 61,5 % | -0.11 R |
| sin tendencia | 24 | 58,3 % | -0.11 R |
| en contra | 20 | 45,0 % | -0.36 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 51 | 51,0 % | -0.26 R |
| en contra | 19 | 68,4 % | +0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 52 | 53,8 % | -0.25 R |
| a favor | 18 | 61,1 % | +0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 12/11 16:45 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 09/11 07:15 | USD/CHF | 15m | COMPRAR | 75 min | estocastico+barrida | -0.16 % |
| 05/11 15:50 | EUR/JPY | 5m | COMPRAR | 75 min | bollinger | -0.16 % |
| 13/11 09:00 | USD/CHF | 15m | VENDER | 75 min | barrida | -0.14 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**25 señales** del 28/10/2026 al 12/11/2026. Acierto (precio a favor al vencer): **28,0 %** · resultado medio con SL/TP tras costes: **+0.02 R** · claramente peor que el azar (z = -2.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 16 | 25,0 % | +0.10 R |
| <52 % | 9 | 33,3 % | -0.06 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 10 | 30,0 % | +0.30 R |
| USD/CHF | 7 | 28,6 % | +0.11 R |
| ETH/USDT | 4 | 25,0 % | — |
| GBP/JPY | 3 | 33,3 % | -1.05 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 18 | 27,8 % | +0.11 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 12 | 25,0 % | +0.57 R |
| 4-12 h | 11 | 36,4 % | -0.06 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 12 | 33,3 % | +0.30 R |
| estocastico | 10 | 20,0 % | -0.06 R |
| barrida | 2 | 50,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 6 | 33,3 % | +1.89 R |
| 12-16 h | 6 | 33,3 % | -1.05 R |
| 16-20 h | 5 | 20,0 % | +0.98 R |
| 00-04 h | 4 | 25,0 % | -1.09 R |
| 08-12 h | 3 | 33,3 % | -0.29 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 16 | 31,2 % | +0.18 R |
| débil (20-25) | 6 | 16,7 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 19 | 21,1 % | +0.10 R |
| alta | 4 | 25,0 % | -1.12 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 20 | 30,0 % | +0.11 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 2 | 0,0 % | -1.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 23 | 21,7 % | -0.13 R |
| en contra | 2 | 100,0 % | +0.92 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 20 | 25,0 % | -0.13 R |
| a favor | 5 | 40,0 % | +0.96 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 10/11 17:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.39 % |
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 10/11 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.89 % |
| 12/11 13:00 | ETH/USDT | 4h | COMPRAR | 720 min | barrida | -3.71 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 10/11 21:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -3.22 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 06/11 21:00 | USD/CHF | 4h | VENDER | 4800 min | estocastico | -1.47 % |
