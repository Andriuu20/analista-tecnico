# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1035 señales** del 27/01/2025 al 17/11/2026. Acierto (precio a favor al vencer): **51,6 %** · resultado medio con SL/TP tras costes: **-0.11 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,8 % en 120 | después 50,0 % en 134 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 60,9 % en 115 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 60,9 % en 110 | después 45,7 % en 105 casos | ❔ no se repite |
| tendencia_txt = **a favor** | acierta | 57,3 % en 239 | después 55,1 % en 207 casos | ✅ confirmado |
| tendencia_txt = **en contra** | falla | 37,5 % en 64 | después 49,6 % en 133 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 61,2 % en 129 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 611 | 52,7 % | -0.05 R |
| 52-55 % | 380 | 50,5 % | -0.18 R |
| 55-58 % | 38 | 50,0 % | -0.40 R |
| ≥58 % | 6 | 16,7 % | -0.40 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 254 | 55,1 % | -0.06 R |
| EUR/JPY | 157 | 47,1 % | -0.21 R |
| SOL/USDT | 116 | 53,4 % | -0.10 R |
| XRP/USDT | 100 | 46,0 % | +0.06 R |
| BTC/USDT | 99 | 46,5 % | -0.24 R |
| USD/CHF | 94 | 54,3 % | -0.04 R |
| EUR/GBP | 75 | 52,0 % | -0.26 R |
| Oro (XAU/USD) | 50 | 48,0 % | -0.14 R |
| USD/CAD | 37 | 56,8 % | -0.08 R |
| GBP/JPY | 31 | 51,6 % | -0.10 R |
| AUD/USD | 12 | 66,7 % | +0.16 R |
| EUR/USD | 8 | 75,0 % | +0.15 R |
| ETH/USDT | 2 | 50,0 % | -1.07 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 342 | 50,9 % | -0.13 R |
| 1h | 339 | 47,2 % | -0.20 R |
| 15m | 239 | 54,4 % | -0.07 R |
| 4h | 115 | 60,9 % | +0.13 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 507 | 51,3 % | -0.16 R |
| 2-4 h | 448 | 52,9 % | -0.09 R |
| 30-59 min | 80 | 46,2 % | +0.07 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 452 | 47,6 % | -0.19 R |
| velas | 147 | 61,2 % | +0.15 R |
| soportes | 137 | 51,1 % | -0.23 R |
| estocastico | 79 | 48,1 % | +0.05 R |
| barrida | 68 | 61,8 % | -0.00 R |
| rsi | 51 | 56,9 % | +0.02 R |
| fibonacci | 41 | 53,7 % | -0.37 R |
| order_block | 33 | 51,5 % | -0.24 R |
| bos | 32 | 43,8 % | -0.25 R |
| divergencia | 5 | 60,0 % | +0.50 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 223 | 48,9 % | -0.10 R |
| 12-16 h | 203 | 49,8 % | -0.19 R |
| 00-04 h | 162 | 53,7 % | -0.09 R |
| 20-24 h | 151 | 55,6 % | -0.09 R |
| 04-08 h | 150 | 50,7 % | -0.01 R |
| 08-12 h | 146 | 52,7 % | -0.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 442 | 53,4 % | -0.09 R |
| lateral (<20) | 386 | 50,3 % | -0.08 R |
| débil (20-25) | 207 | 50,2 % | -0.22 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 584 | 51,5 % | -0.11 R |
| alta | 280 | 51,4 % | -0.09 R |
| baja | 171 | 52,0 % | -0.14 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 446 | 56,3 % | +0.04 R |
| sin tendencia | 392 | 49,2 % | -0.20 R |
| en contra | 197 | 45,7 % | -0.27 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 730 | 50,5 % | -0.15 R |
| en contra | 297 | 53,9 % | -0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 718 | 52,1 % | -0.10 R |
| a favor | 317 | 50,5 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 05/11 15:25 | XRP/USDT | 5m | COMPRAR | 50 min | estocastico | -3.28 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 15/11 09:10 | SOL/USDT | 5m | VENDER | 50 min | velas | -2.78 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger+estocastico | -2.33 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 23/09 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.09 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**878 señales** del 08/01/2021 al 16/11/2026. Acierto (precio a favor al vencer): **51,6 %** · resultado medio con SL/TP tras costes: **-0.08 R** · no se distingue del azar todavía (z = 0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | acierta | 58,4 % en 149 | después 49,8 % en 219 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 64,3 % en 56 | después 45,5 % en 55 casos | ❔ no se repite |
| dia = **mar** | acierta | 61,8 % en 102 | después 45,2 % en 73 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 476 | 53,4 % | -0.09 R |
| 52-55 % | 356 | 50,0 % | -0.10 R |
| 55-58 % | 46 | 45,7 % | +0.13 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 170 | 57,1 % | -0.11 R |
| SOL/USDT | 131 | 54,2 % | +0.00 R |
| GBP/JPY | 122 | 56,6 % | -0.12 R |
| Oro (XAU/USD) | 111 | 51,4 % | -0.00 R |
| GBP/USD | 84 | 53,6 % | -0.13 R |
| USD/JPY | 73 | 42,5 % | -0.12 R |
| EUR/GBP | 69 | 46,4 % | -0.21 R |
| AUD/USD | 38 | 47,4 % | -0.01 R |
| ETH/USDT | 37 | 35,1 % | +0.02 R |
| EUR/JPY | 23 | 56,5 % | -0.17 R |
| XRP/USDT | 19 | 36,8 % | +0.04 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 368 | 53,3 % | -0.13 R |
| 4h | 316 | 49,4 % | -0.09 R |
| 1d | 136 | 52,2 % | +0.07 R |
| 15m | 58 | 51,7 % | -0.04 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 296 | 50,0 % | -0.04 R |
| 4-12 h | 263 | 51,3 % | -0.05 R |
| 12-24 h | 247 | 52,2 % | -0.20 R |
| 1-2 días | 72 | 56,9 % | +0.04 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 351 | 50,7 % | -0.11 R |
| bollinger | 297 | 52,2 % | -0.02 R |
| estocastico | 91 | 59,3 % | +0.03 R |
| barrida | 88 | 53,4 % | -0.13 R |
| order_block | 25 | 48,0 % | +0.09 R |
| ruptura | 7 | 28,6 % | -0.48 R |
| bos | 7 | 42,9 % | +0.10 R |
| velas | 7 | 14,3 % | -0.60 R |
| choch | 5 | 60,0 % | -0.73 R |
| fibonacci | 5 | 60,0 % | -0.63 R |
| rsi | 5 | 20,0 % | -1.15 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| fvg | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 220 | 49,1 % | +0.03 R |
| 08-12 h | 151 | 51,0 % | -0.15 R |
| 00-04 h | 145 | 56,6 % | -0.03 R |
| 12-16 h | 128 | 53,9 % | -0.12 R |
| 16-20 h | 123 | 45,5 % | -0.18 R |
| 20-24 h | 111 | 55,0 % | -0.13 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 355 | 51,5 % | -0.04 R |
| lateral (<20) | 342 | 51,5 % | -0.10 R |
| débil (20-25) | 181 | 51,9 % | -0.11 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 498 | 49,2 % | -0.07 R |
| baja | 198 | 56,1 % | -0.02 R |
| alta | 182 | 53,3 % | -0.16 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 344 | 48,8 % | -0.14 R |
| sin tendencia | 308 | 52,6 % | -0.00 R |
| en contra | 226 | 54,4 % | -0.09 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 627 | 51,5 % | -0.09 R |
| en contra | 247 | 51,4 % | -0.05 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 562 | 50,2 % | -0.11 R |
| a favor | 316 | 54,1 % | -0.02 R |

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
**91 señales** del 28/10/2026 al 18/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.24 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 62 | 54,8 % | -0.29 R |
| 52-55 % | 28 | 46,4 % | -0.09 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 22 | 36,4 % | -0.42 R |
| USD/CHF | 11 | 54,5 % | +0.17 R |
| BTC/USDT | 11 | 45,5 % | -0.47 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 2 | 0,0 % | -1.14 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 45 | 60,0 % | -0.25 R |
| 15m | 37 | 48,6 % | -0.18 R |
| 1h | 9 | 33,3 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 68 | 51,5 % | -0.16 R |
| 30-59 min | 17 | 52,9 % | -0.62 R |
| 2-4 h | 6 | 66,7 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 29 | 69,0 % | -0.04 R |
| bollinger | 28 | 32,1 % | -0.38 R |
| barrida | 12 | 50,0 % | +0.04 R |
| rsi | 11 | 54,5 % | -0.53 R |
| estocastico | 11 | 45,5 % | -0.61 R |
| velas | 2 | 100,0 % | +1.23 R |
| fibonacci | 2 | 100,0 % | — |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 27 | 74,1 % | -0.03 R |
| 08-12 h | 18 | 55,6 % | -0.04 R |
| 04-08 h | 13 | 38,5 % | -0.40 R |
| 20-24 h | 13 | 30,8 % | -0.39 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 43 | 46,5 % | -0.09 R |
| lateral (<20) | 30 | 63,3 % | -0.34 R |
| débil (20-25) | 18 | 50,0 % | -0.50 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 49 | 53,1 % | -0.27 R |
| alta | 25 | 48,0 % | -0.22 R |
| baja | 17 | 58,8 % | -0.19 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 31 | 41,9 % | -0.35 R |
| a favor | 30 | 60,0 % | -0.19 R |
| sin tendencia | 30 | 56,7 % | -0.19 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 66 | 48,5 % | -0.30 R |
| en contra | 25 | 64,0 % | -0.08 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 70 | 48,6 % | -0.29 R |
| a favor | 21 | 66,7 % | -0.09 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 12/11 16:45 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.23 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**36 señales** del 28/10/2026 al 16/11/2026. Acierto (precio a favor al vencer): **22,2 %** · resultado medio con SL/TP tras costes: **-0.20 R** · claramente peor que el azar (z = -3.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 20 | 25,0 % | -0.13 R |
| <52 % | 16 | 18,8 % | -0.28 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 14 | 28,6 % | -0.03 R |
| USD/CHF | 10 | 20,0 % | +0.11 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.41 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 28 | 21,4 % | -0.20 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 21 | 19,0 % | -0.03 R |
| 4-12 h | 11 | 36,4 % | -0.05 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 1 | 0,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 18 | 27,8 % | +0.08 R |
| estocastico | 14 | 21,4 % | -0.18 R |
| soportes | 3 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.09 R |
| 12-16 h | 7 | 28,6 % | -0.64 R |
| 20-24 h | 6 | 33,3 % | +1.17 R |
| 16-20 h | 6 | 16,7 % | +0.98 R |
| 04-08 h | 4 | 0,0 % | -1.02 R |
| 08-12 h | 4 | 25,0 % | -0.29 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 26 | 23,1 % | -0.31 R |
| débil (20-25) | 7 | 14,3 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 25 | 16,0 % | -0.13 R |
| alta | 9 | 22,2 % | -1.07 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 29 | 20,7 % | -0.25 R |
| en contra | 4 | 25,0 % | -1.16 R |
| a favor | 3 | 33,3 % | +0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 33 | 18,2 % | -0.27 R |
| en contra | 3 | 66,7 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 31 | 19,4 % | -0.29 R |
| a favor | 5 | 40,0 % | +0.30 R |

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
