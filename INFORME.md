# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1096 señales** del 22/01/2025 al 19/11/2026. Acierto (precio a favor al vencer): **52,9 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 59,6 % en 156 | después 50,0 % en 94 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 58,0 % en 169 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 61,2 % en 116 | después 48,6 % en 105 casos | ❔ no se repite |
| tendencia_txt = **a favor** | acierta | 58,0 % en 255 | después 54,8 % en 221 casos | ✅ confirmado |
| zona_txt = **en contra** | acierta | 57,6 % en 177 | después 56,0 % en 243 casos | ✅ confirmado |
| estrategia = **velas** | acierta | 58,5 % en 183 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 688 | 53,5 % | -0.08 R |
| 52-55 % | 374 | 51,9 % | -0.14 R |
| 55-58 % | 34 | 52,9 % | -0.10 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 250 | 56,0 % | -0.09 R |
| EUR/GBP | 123 | 43,9 % | -0.13 R |
| BTC/USDT | 106 | 50,0 % | -0.25 R |
| SOL/USDT | 99 | 59,6 % | -0.08 R |
| USD/CHF | 92 | 55,4 % | -0.12 R |
| USD/CAD | 89 | 57,3 % | -0.11 R |
| GBP/JPY | 83 | 47,0 % | -0.04 R |
| EUR/JPY | 75 | 46,7 % | -0.17 R |
| AUD/USD | 69 | 60,9 % | +0.29 R |
| Oro (XAU/USD) | 49 | 46,9 % | -0.56 R |
| XRP/USDT | 35 | 45,7 % | -0.09 R |
| EUR/USD | 14 | 64,3 % | +0.36 R |
| GBP/USD | 8 | 62,5 % | +0.05 R |
| ETH/USDT | 4 | 75,0 % | +0.91 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 354 | 49,4 % | -0.14 R |
| 5m | 329 | 52,6 % | -0.17 R |
| 15m | 244 | 54,9 % | +0.05 R |
| 4h | 169 | 58,0 % | -0.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 597 | 52,9 % | -0.09 R |
| 1-2 h | 428 | 55,1 % | -0.10 R |
| 30-59 min | 71 | 39,4 % | -0.17 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 347 | 50,1 % | -0.11 R |
| velas | 210 | 58,6 % | +0.09 R |
| soportes | 132 | 50,0 % | -0.39 R |
| fibonacci | 120 | 52,5 % | -0.13 R |
| order_block | 78 | 56,4 % | -0.10 R |
| estocastico | 78 | 48,7 % | -0.08 R |
| barrida | 64 | 62,5 % | -0.02 R |
| rsi | 25 | 52,0 % | -0.02 R |
| bos | 24 | 54,2 % | -0.04 R |
| ruptura | 20 | 60,0 % | -0.16 R |
| fvg | 11 | 18,2 % | -0.11 R |
| divergencia | 5 | 60,0 % | +0.50 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 228 | 49,1 % | -0.15 R |
| 12-16 h | 225 | 52,4 % | -0.16 R |
| 08-12 h | 172 | 55,8 % | -0.08 R |
| 04-08 h | 164 | 50,6 % | +0.00 R |
| 00-04 h | 157 | 59,9 % | -0.01 R |
| 20-24 h | 150 | 51,3 % | -0.16 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 448 | 53,6 % | -0.12 R |
| lateral (<20) | 406 | 52,2 % | -0.05 R |
| débil (20-25) | 242 | 52,9 % | -0.15 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 617 | 54,0 % | -0.10 R |
| alta | 257 | 49,4 % | -0.02 R |
| baja | 222 | 54,1 % | -0.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 476 | 56,5 % | -0.10 R |
| sin tendencia | 445 | 48,1 % | -0.12 R |
| en contra | 175 | 55,4 % | -0.06 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 666 | 50,5 % | -0.14 R |
| en contra | 420 | 56,7 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 661 | 51,4 % | -0.07 R |
| a favor | 435 | 55,2 % | -0.15 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 100 min | estocastico | -2.19 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 04/08 22:00 | Oro (XAU/USD) | 4h | VENDER | 240 min | soportes | -1.40 % |
| 15/11 14:45 | BTC/USDT | 5m | COMPRAR | 100 min | fibonacci | -1.36 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**745 señales** del 08/01/2021 al 16/11/2026. Acierto (precio a favor al vencer): **53,8 %** · resultado medio con SL/TP tras costes: **-0.11 R** · claramente mejor que el azar (z = 2.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | acierta | 59,5 % en 116 | después 52,3 % en 193 casos | ❔ no se repite |
| tendencia_txt = **sin tendencia** | acierta | 60,8 % en 125 | después 52,7 % en 148 casos | ❔ no se repite |
| zona_txt = **a favor (barato al comprar / caro al vender)** | acierta | 56,4 % en 250 | después 52,5 % en 295 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 400 | 55,8 % | -0.11 R |
| 52-55 % | 301 | 51,5 % | -0.14 R |
| 55-58 % | 44 | 52,3 % | +0.09 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 126 | 57,9 % | -0.16 R |
| Oro (XAU/USD) | 113 | 51,3 % | -0.02 R |
| SOL/USDT | 101 | 56,4 % | -0.06 R |
| GBP/JPY | 93 | 54,8 % | -0.16 R |
| GBP/USD | 88 | 53,4 % | -0.07 R |
| EUR/GBP | 60 | 60,0 % | -0.34 R |
| USD/JPY | 53 | 47,2 % | -0.01 R |
| ETH/USDT | 52 | 38,5 % | -0.26 R |
| AUD/USD | 28 | 57,1 % | +0.05 R |
| EUR/JPY | 21 | 61,9 % | -0.20 R |
| XRP/USDT | 9 | 55,6 % | +0.43 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 309 | 55,0 % | -0.09 R |
| 4h | 284 | 53,9 % | -0.19 R |
| 1d | 134 | 52,2 % | +0.05 R |
| 15m | 18 | 44,4 % | -0.34 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 285 | 52,6 % | -0.10 R |
| 12-24 h | 215 | 52,6 % | -0.19 R |
| 4-12 h | 187 | 56,1 % | -0.09 R |
| 1-2 días | 58 | 56,9 % | +0.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 312 | 53,2 % | -0.16 R |
| bollinger | 232 | 55,6 % | +0.01 R |
| barrida | 96 | 53,1 % | -0.11 R |
| estocastico | 70 | 58,6 % | -0.11 R |
| order_block | 12 | 58,3 % | +0.40 R |
| fvg | 8 | 37,5 % | -0.36 R |
| bos | 7 | 42,9 % | +0.10 R |
| choch | 5 | 60,0 % | -0.73 R |
| rsi | 5 | 60,0 % | -1.15 R |
| fibonacci | 2 | 0,0 % | -1.02 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| ruptura | 1 | 0,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 204 | 51,5 % | +0.06 R |
| 12-16 h | 118 | 56,8 % | -0.19 R |
| 08-12 h | 113 | 54,9 % | -0.12 R |
| 00-04 h | 112 | 56,2 % | -0.02 R |
| 16-20 h | 105 | 50,5 % | -0.23 R |
| 20-24 h | 93 | 54,8 % | -0.34 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 311 | 53,1 % | -0.08 R |
| lateral (<20) | 281 | 54,4 % | -0.14 R |
| débil (20-25) | 153 | 54,2 % | -0.13 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 423 | 54,8 % | -0.09 R |
| baja | 167 | 55,1 % | -0.08 R |
| alta | 155 | 49,7 % | -0.19 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 273 | 50,2 % | -0.23 R |
| sin tendencia | 273 | 56,4 % | +0.01 R |
| en contra | 199 | 55,3 % | -0.11 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 545 | 54,3 % | -0.11 R |
| en contra | 198 | 52,0 % | -0.12 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 472 | 53,8 % | -0.13 R |
| a favor | 273 | 53,8 % | -0.08 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 17/08 18:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -18.07 % |
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 13/11 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -6.32 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**95 señales** del 28/10/2026 al 19/11/2026. Acierto (precio a favor al vencer): **52,6 %** · resultado medio con SL/TP tras costes: **-0.22 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 63 | 54,0 % | -0.30 R |
| 52-55 % | 31 | 48,4 % | -0.01 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 22 | 36,4 % | -0.42 R |
| BTC/USDT | 13 | 46,2 % | -0.06 R |
| USD/CHF | 11 | 54,5 % | -0.07 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| SOL/USDT | 2 | 0,0 % | -1.14 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| USD/CAD | 2 | 50,0 % | -0.19 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 49 | 59,2 % | -0.16 R |
| 15m | 37 | 48,6 % | -0.23 R |
| 1h | 9 | 33,3 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 72 | 51,4 % | -0.13 R |
| 30-59 min | 17 | 52,9 % | -0.62 R |
| 2-4 h | 6 | 66,7 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 29 | 69,0 % | -0.04 R |
| bollinger | 28 | 32,1 % | -0.38 R |
| barrida | 12 | 50,0 % | -0.16 R |
| estocastico | 11 | 45,5 % | -0.61 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 4 | 75,0 % | +0.88 R |
| velas | 2 | 100,0 % | +1.23 R |
| order_block | 2 | 50,0 % | -0.19 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 28 | 75,0 % | -0.11 R |
| 08-12 h | 21 | 52,4 % | +0.12 R |
| 04-08 h | 13 | 38,5 % | -0.40 R |
| 20-24 h | 13 | 30,8 % | -0.39 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 46 | 45,7 % | -0.11 R |
| lateral (<20) | 30 | 63,3 % | -0.15 R |
| débil (20-25) | 19 | 52,6 % | -0.56 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 52 | 53,8 % | -0.30 R |
| alta | 25 | 48,0 % | -0.25 R |
| baja | 18 | 55,6 % | +0.10 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 32 | 59,4 % | -0.25 R |
| sin tendencia | 32 | 56,2 % | -0.00 R |
| en contra | 31 | 41,9 % | -0.41 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 67 | 47,8 % | -0.34 R |
| en contra | 28 | 64,3 % | +0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 73 | 47,9 % | -0.25 R |
| a favor | 22 | 68,2 % | -0.10 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 19/11 09:35 | BTC/USDT | 5m | VENDER | 100 min | fibonacci | -0.34 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**37 señales** del 28/10/2026 al 16/11/2026. Acierto (precio a favor al vencer): **21,6 %** · resultado medio con SL/TP tras costes: **-0.36 R** · claramente peor que el azar (z = -3.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 21 | 23,8 % | -0.41 R |
| <52 % | 16 | 18,8 % | -0.28 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 14 | 28,6 % | -0.23 R |
| USD/CHF | 11 | 18,2 % | -0.06 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 29 | 20,7 % | -0.44 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 22 | 18,2 % | -0.36 R |
| 4-12 h | 11 | 36,4 % | -0.15 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 1 | 0,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 18 | 27,8 % | -0.20 R |
| estocastico | 15 | 20,0 % | -0.35 R |
| soportes | 4 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.09 R |
| 12-16 h | 7 | 28,6 % | -0.64 R |
| 20-24 h | 7 | 28,6 % | +0.43 R |
| 16-20 h | 6 | 16,7 % | -0.22 R |
| 04-08 h | 4 | 0,0 % | -1.02 R |
| 08-12 h | 4 | 25,0 % | -0.29 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 27 | 22,2 % | -0.53 R |
| débil (20-25) | 7 | 14,3 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 26 | 15,4 % | -0.27 R |
| alta | 9 | 22,2 % | -1.06 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 29 | 20,7 % | -0.40 R |
| en contra | 5 | 20,0 % | -1.11 R |
| a favor | 3 | 33,3 % | +0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 34 | 17,6 % | -0.45 R |
| en contra | 3 | 66,7 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 32 | 18,8 % | -0.40 R |
| a favor | 5 | 40,0 % | -0.24 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 14/11 09:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.78 % |
| 10/11 17:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.39 % |
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 14/11 05:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.92 % |
| 10/11 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.89 % |
| 12/11 13:00 | ETH/USDT | 4h | COMPRAR | 720 min | barrida | -3.71 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 10/11 21:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -3.22 % |
