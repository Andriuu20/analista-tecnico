# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1032 señales** del 29/10/2025 al 23/11/2026. Acierto (precio a favor al vencer): **51,6 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 61,2 % en 85 | después 46,9 % en 64 casos | ❔ no se repite |
| mercado = **SOL/USDT** | acierta | 63,2 % en 76 | después 43,4 % en 83 casos | ❔ no se repite |
| mercado = **AUD/USD** | acierta | 68,0 % en 50 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **4h** | acierta | 61,3 % en 80 | pocos casos en la segunda mitad | ⏳ faltan datos |
| plazo = **2-4 h** | acierta | 55,1 % en 410 | después 53,4 % en 88 casos | ❔ no se repite |
| dia = **jue** | acierta | 66,7 % en 108 | después 46,5 % en 86 casos | ❔ no se repite |
| zona_txt = **en contra** | acierta | 61,0 % en 123 | después 48,1 % en 162 casos | ❔ no se repite |
| estructura_txt = **a favor** | acierta | 59,1 % en 149 | después 48,7 % en 191 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 61,4 % en 132 | después 37,3 % en 59 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 635 | 53,2 % | -0.03 R |
| 52-55 % | 344 | 48,3 % | -0.27 R |
| 55-58 % | 42 | 54,8 % | -0.16 R |
| ≥58 % | 11 | 54,5 % | -0.41 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 159 | 52,8 % | -0.11 R |
| USD/JPY | 149 | 55,0 % | -0.08 R |
| EUR/JPY | 147 | 46,9 % | -0.15 R |
| BTC/USDT | 138 | 48,6 % | -0.11 R |
| EUR/GBP | 76 | 51,3 % | -0.32 R |
| AUD/USD | 68 | 61,8 % | +0.15 R |
| USD/CHF | 66 | 56,1 % | -0.04 R |
| ETH/USDT | 66 | 48,5 % | -0.43 R |
| GBP/JPY | 58 | 56,9 % | -0.12 R |
| USD/CAD | 43 | 51,2 % | -0.20 R |
| XRP/USDT | 36 | 30,6 % | -0.06 R |
| Oro (XAU/USD) | 17 | 58,8 % | +0.10 R |
| GBP/USD | 5 | 40,0 % | +0.28 R |
| EUR/USD | 4 | 75,0 % | +1.85 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 392 | 50,5 % | -0.15 R |
| 5m | 318 | 49,7 % | -0.20 R |
| 15m | 242 | 52,9 % | -0.04 R |
| 4h | 80 | 61,3 % | +0.13 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 498 | 54,8 % | -0.06 R |
| 1-2 h | 452 | 49,3 % | -0.20 R |
| 30-59 min | 82 | 45,1 % | -0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 418 | 49,5 % | -0.20 R |
| velas | 191 | 53,9 % | -0.01 R |
| estocastico | 155 | 54,8 % | -0.06 R |
| soportes | 79 | 49,4 % | -0.26 R |
| barrida | 46 | 52,2 % | +0.06 R |
| fibonacci | 45 | 60,0 % | +0.12 R |
| order_block | 41 | 51,2 % | -0.20 R |
| rsi | 23 | 47,8 % | -0.19 R |
| bos | 14 | 64,3 % | +0.19 R |
| fvg | 9 | 33,3 % | -0.34 R |
| supertrend | 8 | 37,5 % | -0.11 R |
| divergencia | 5 | 60,0 % | +0.50 R |
| ruptura | 5 | 80,0 % | +0.46 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 218 | 52,8 % | +0.03 R |
| 12-16 h | 216 | 53,7 % | -0.13 R |
| 08-12 h | 163 | 52,1 % | -0.36 R |
| 20-24 h | 152 | 50,0 % | -0.24 R |
| 04-08 h | 150 | 50,0 % | +0.06 R |
| 00-04 h | 133 | 49,6 % | -0.10 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 421 | 50,6 % | -0.17 R |
| lateral (<20) | 378 | 51,6 % | -0.07 R |
| débil (20-25) | 233 | 53,6 % | -0.09 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 571 | 50,3 % | -0.16 R |
| alta | 256 | 52,7 % | +0.01 R |
| baja | 205 | 54,1 % | -0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 473 | 53,7 % | -0.04 R |
| sin tendencia | 399 | 51,1 % | -0.18 R |
| en contra | 160 | 46,9 % | -0.18 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 738 | 50,7 % | -0.15 R |
| en contra | 285 | 53,7 % | -0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 692 | 50,9 % | -0.09 R |
| a favor | 340 | 53,2 % | -0.16 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 03:15 | SOL/USDT | 5m | COMPRAR | 100 min | velas | -3.02 % |
| 16/11 15:30 | XRP/USDT | 15m | COMPRAR | 30 min | supertrend | -2.66 % |
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 75 min | estocastico | -2.45 % |
| 21/11 13:35 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -2.32 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 22/11 09:40 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -1.83 % |
| 10/06 01:00 | XRP/USDT | 1h | COMPRAR | 180 min | velas | -1.77 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**698 señales** del 16/12/2020 al 20/11/2026. Acierto (precio a favor al vencer): **53,0 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/CHF** | acierta | 66,0 % en 47 | después 53,4 % en 73 casos | ❔ no se repite |
| dia = **mar** | acierta | 61,7 % en 81 | después 48,3 % en 58 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 381 | 55,4 % | -0.13 R |
| 52-55 % | 277 | 50,9 % | -0.18 R |
| 55-58 % | 40 | 45,0 % | -0.03 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| Oro (XAU/USD) | 141 | 52,5 % | -0.08 R |
| USD/CHF | 120 | 58,3 % | -0.21 R |
| SOL/USDT | 96 | 53,1 % | -0.06 R |
| GBP/JPY | 93 | 55,9 % | -0.24 R |
| USD/JPY | 59 | 52,5 % | +0.01 R |
| EUR/GBP | 53 | 54,7 % | -0.35 R |
| GBP/USD | 47 | 48,9 % | -0.25 R |
| ETH/USDT | 32 | 34,4 % | -0.21 R |
| EUR/JPY | 27 | 44,4 % | -0.31 R |
| AUD/USD | 26 | 57,7 % | +0.30 R |
| XRP/USDT | 3 | 66,7 % | +1.59 R |
| USD/CAD | 1 | 0,0 % | -1.08 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 279 | 50,9 % | -0.20 R |
| 1h | 237 | 55,3 % | -0.12 R |
| 1d | 163 | 52,8 % | -0.02 R |
| 15m | 19 | 57,9 % | -0.52 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 309 | 53,1 % | -0.11 R |
| 12-24 h | 184 | 52,7 % | -0.17 R |
| 4-12 h | 148 | 53,4 % | -0.21 R |
| 1-2 días | 57 | 52,6 % | -0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 329 | 53,5 % | -0.16 R |
| bollinger | 196 | 55,1 % | -0.00 R |
| estocastico | 72 | 54,2 % | -0.17 R |
| barrida | 48 | 47,9 % | -0.26 R |
| fibonacci | 14 | 35,7 % | -0.63 R |
| fvg | 14 | 57,1 % | -0.61 R |
| order_block | 11 | 54,5 % | +0.04 R |
| choch | 10 | 50,0 % | -0.22 R |
| bos | 5 | 40,0 % | +0.56 R |
| rsi | 2 | 100,0 % | +0.87 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| ruptura | 1 | 0,0 % | -1.03 R |
| velas | 1 | 0,0 % | -1.08 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 220 | 49,1 % | -0.14 R |
| 00-04 h | 106 | 54,7 % | +0.04 R |
| 08-12 h | 102 | 53,9 % | -0.20 R |
| 12-16 h | 95 | 57,9 % | -0.07 R |
| 20-24 h | 92 | 57,6 % | -0.28 R |
| 16-20 h | 83 | 49,4 % | -0.22 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 282 | 50,7 % | -0.12 R |
| lateral (<20) | 268 | 56,7 % | -0.15 R |
| débil (20-25) | 148 | 50,7 % | -0.15 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 424 | 51,9 % | -0.18 R |
| baja | 141 | 56,7 % | -0.01 R |
| alta | 133 | 52,6 % | -0.17 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 259 | 49,4 % | -0.28 R |
| sin tendencia | 249 | 54,6 % | +0.01 R |
| en contra | 190 | 55,8 % | -0.15 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 474 | 54,2 % | -0.13 R |
| en contra | 223 | 50,2 % | -0.16 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 425 | 53,9 % | -0.15 R |
| a favor | 273 | 51,6 % | -0.13 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |
| 27/08 06:00 | Oro (XAU/USD) | 1d | COMPRAR | 4320 min | soportes | -5.74 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**109 señales** del 28/10/2026 al 24/11/2026. Acierto (precio a favor al vencer): **53,2 %** · resultado medio con SL/TP tras costes: **-0.24 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 70 | 52,9 % | -0.36 R |
| 52-55 % | 35 | 54,3 % | +0.03 R |
| 55-58 % | 4 | 50,0 % | -0.51 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 23 | 34,8 % | -0.45 R |
| BTC/USDT | 19 | 52,6 % | -0.31 R |
| USD/CHF | 12 | 50,0 % | -0.17 R |
| EUR/GBP | 6 | 50,0 % | +0.04 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| ETH/USDT | 4 | 50,0 % | -0.50 R |
| SOL/USDT | 3 | 33,3 % | -0.31 R |
| USD/CAD | 3 | 66,7 % | +0.15 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 58 | 60,3 % | -0.19 R |
| 15m | 40 | 47,5 % | -0.26 R |
| 1h | 11 | 36,4 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 81 | 53,1 % | -0.13 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 8 | 62,5 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 32 | 34,4 % | -0.38 R |
| soportes | 30 | 66,7 % | -0.08 R |
| estocastico | 16 | 50,0 % | -0.46 R |
| barrida | 13 | 46,2 % | -0.24 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 3 | 66,7 % | +0.15 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 32 | 71,9 % | -0.18 R |
| 08-12 h | 24 | 54,2 % | +0.00 R |
| 04-08 h | 18 | 38,9 % | -0.28 R |
| 20-24 h | 15 | 40,0 % | -0.36 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 55 | 45,5 % | -0.19 R |
| lateral (<20) | 31 | 64,5 % | -0.18 R |
| débil (20-25) | 23 | 56,5 % | -0.46 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 62 | 53,2 % | -0.31 R |
| alta | 28 | 50,0 % | -0.25 R |
| baja | 19 | 57,9 % | +0.03 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 40 | 60,0 % | -0.27 R |
| sin tendencia | 37 | 56,8 % | -0.03 R |
| en contra | 32 | 40,6 % | -0.43 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 79 | 49,4 % | -0.36 R |
| en contra | 30 | 63,3 % | +0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 79 | 48,1 % | -0.28 R |
| a favor | 30 | 66,7 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 24/11 05:10 | ETH/USDT | 5m | VENDER | 100 min | estocastico | -0.61 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 24/11 05:10 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -0.36 % |
| 19/11 09:35 | BTC/USDT | 5m | VENDER | 100 min | fibonacci | -0.34 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**43 señales** del 28/10/2026 al 23/11/2026. Acierto (precio a favor al vencer): **27,9 %** · resultado medio con SL/TP tras costes: **-0.56 R** · claramente peor que el azar (z = -2.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 24 | 33,3 % | -0.51 R |
| <52 % | 19 | 21,1 % | -0.61 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 17 | 41,2 % | -0.46 R |
| USD/CHF | 12 | 25,0 % | -0.18 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| EUR/GBP | 2 | 0,0 % | -1.15 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 33 | 30,3 % | -0.64 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 4 | 0,0 % | -1.11 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 24 | 25,0 % | -0.63 R |
| 4-12 h | 13 | 30,8 % | -0.31 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 3 | 66,7 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 23 | 34,8 % | -0.51 R |
| estocastico | 18 | 33,3 % | -0.51 R |
| soportes | 4 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.06 R |
| 12-16 h | 9 | 22,2 % | -0.80 R |
| 20-24 h | 9 | 44,4 % | +0.43 R |
| 16-20 h | 6 | 16,7 % | -0.36 R |
| 04-08 h | 5 | 20,0 % | -1.02 R |
| 08-12 h | 5 | 40,0 % | -0.48 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 32 | 31,2 % | -0.71 R |
| débil (20-25) | 7 | 14,3 % | -0.36 R |
| lateral (<20) | 4 | 25,0 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 32 | 25,0 % | -0.43 R |
| alta | 9 | 22,2 % | -1.04 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 30 | 20,0 % | -0.58 R |
| en contra | 8 | 50,0 % | -1.08 R |
| a favor | 5 | 40,0 % | +0.01 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 38 | 21,1 % | -0.63 R |
| en contra | 4 | 75,0 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 37 | 24,3 % | -0.61 R |
| a favor | 6 | 50,0 % | -0.24 R |

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
