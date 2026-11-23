# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1132 señales** del 16/01/2025 al 22/11/2026. Acierto (precio a favor al vencer): **52,4 %** · resultado medio con SL/TP tras costes: **-0.13 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 61,6 % en 151 | después 46,3 % en 123 casos | ❔ no se repite |
| mercado = **AUD/USD** | acierta | 66,7 % en 45 | después 53,5 % en 43 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 61,6 % en 146 | pocos casos en la segunda mitad | ⏳ faltan datos |
| franja = **00-04 h** | acierta | 64,4 % en 73 | después 50,5 % en 105 casos | ❔ no se repite |
| dia = **jue** | acierta | 65,0 % en 120 | después 52,7 % en 110 casos | ❔ no se repite |
| fuerza_adx = **débil (20-25)** | acierta | 60,5 % en 114 | después 47,6 % en 124 casos | ❔ no se repite |
| volatilidad = **baja** | acierta | 59,3 % en 145 | después 51,1 % en 94 casos | ❔ no se repite |
| tendencia_txt = **a favor** | acierta | 57,1 % en 261 | después 51,2 % en 252 casos | ❔ no se repite |
| zona_txt = **en contra** | acierta | 59,3 % en 177 | después 53,6 % en 239 casos | ✅ confirmado |
| estrategia = **velas** | acierta | 62,1 % en 190 | después 50,0 % en 42 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 710 | 53,7 % | -0.07 R |
| 52-55 % | 370 | 50,3 % | -0.25 R |
| 55-58 % | 45 | 53,3 % | -0.07 R |
| ≥58 % | 7 | 28,6 % | -0.39 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 274 | 54,7 % | -0.12 R |
| EUR/JPY | 137 | 45,3 % | -0.20 R |
| SOL/USDT | 126 | 56,3 % | +0.03 R |
| EUR/GBP | 103 | 46,6 % | -0.31 R |
| USD/CAD | 101 | 55,4 % | -0.05 R |
| AUD/USD | 88 | 60,2 % | +0.06 R |
| USD/CHF | 66 | 56,1 % | -0.06 R |
| Oro (XAU/USD) | 65 | 47,7 % | -0.27 R |
| GBP/JPY | 58 | 50,0 % | -0.14 R |
| BTC/USDT | 38 | 55,3 % | -0.38 R |
| ETH/USDT | 33 | 39,4 % | -0.62 R |
| XRP/USDT | 24 | 41,7 % | -0.35 R |
| EUR/USD | 15 | 66,7 % | +0.51 R |
| GBP/USD | 4 | 50,0 % | +0.61 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 372 | 50,3 % | -0.16 R |
| 5m | 314 | 49,4 % | -0.17 R |
| 15m | 300 | 53,7 % | -0.14 R |
| 4h | 146 | 61,6 % | +0.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 645 | 54,1 % | -0.09 R |
| 1-2 h | 401 | 51,4 % | -0.14 R |
| 30-59 min | 86 | 44,2 % | -0.37 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 362 | 49,2 % | -0.23 R |
| velas | 232 | 59,9 % | +0.04 R |
| soportes | 162 | 46,9 % | -0.32 R |
| estocastico | 105 | 50,5 % | -0.10 R |
| order_block | 90 | 55,6 % | -0.07 R |
| fibonacci | 44 | 59,1 % | +0.14 R |
| rsi | 36 | 52,8 % | -0.11 R |
| barrida | 36 | 63,9 % | +0.09 R |
| bos | 27 | 44,4 % | -0.18 R |
| ruptura | 23 | 56,5 % | +0.18 R |
| supertrend | 19 | 42,1 % | -0.42 R |
| fvg | 9 | 33,3 % | -0.34 R |
| divergencia | 5 | 60,0 % | +0.50 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 235 | 52,3 % | -0.12 R |
| 12-16 h | 235 | 55,3 % | -0.09 R |
| 00-04 h | 178 | 56,2 % | -0.12 R |
| 04-08 h | 169 | 52,7 % | +0.06 R |
| 08-12 h | 162 | 45,7 % | -0.39 R |
| 20-24 h | 153 | 50,3 % | -0.18 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 472 | 49,4 % | -0.22 R |
| lateral (<20) | 422 | 55,0 % | -0.02 R |
| débil (20-25) | 238 | 53,8 % | -0.17 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 616 | 51,6 % | -0.14 R |
| alta | 277 | 50,9 % | -0.10 R |
| baja | 239 | 56,1 % | -0.14 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 513 | 54,2 % | -0.11 R |
| sin tendencia | 447 | 51,0 % | -0.14 R |
| en contra | 172 | 50,6 % | -0.17 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 705 | 50,1 % | -0.20 R |
| en contra | 416 | 56,0 % | -0.01 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 701 | 51,2 % | -0.11 R |
| a favor | 431 | 54,3 % | -0.17 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 16/11 15:30 | XRP/USDT | 15m | COMPRAR | 30 min | supertrend | -2.66 % |
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 75 min | estocastico | -2.45 % |
| 21/11 13:35 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -2.32 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 22/11 09:40 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -1.83 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 22/11 09:40 | ETH/USDT | 5m | VENDER | 100 min | rsi | -1.33 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 22/11 07:50 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -1.23 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**718 señales** del 16/12/2020 al 17/11/2026. Acierto (precio a favor al vencer): **53,5 %** · resultado medio con SL/TP tras costes: **-0.13 R** · no se distingue del azar todavía (z = 1.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 411 | 55,0 % | -0.13 R |
| 52-55 % | 273 | 51,6 % | -0.15 R |
| 55-58 % | 34 | 50,0 % | -0.01 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| Oro (XAU/USD) | 143 | 53,1 % | -0.04 R |
| USD/CHF | 120 | 58,3 % | -0.16 R |
| GBP/JPY | 110 | 54,5 % | -0.20 R |
| SOL/USDT | 92 | 53,3 % | -0.05 R |
| USD/JPY | 58 | 53,4 % | +0.03 R |
| EUR/GBP | 52 | 59,6 % | -0.40 R |
| GBP/USD | 43 | 46,5 % | -0.24 R |
| ETH/USDT | 38 | 34,2 % | -0.40 R |
| AUD/USD | 32 | 56,2 % | +0.17 R |
| EUR/JPY | 22 | 50,0 % | -0.48 R |
| XRP/USDT | 8 | 62,5 % | +0.62 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 270 | 54,4 % | -0.11 R |
| 4h | 268 | 51,9 % | -0.23 R |
| 1d | 164 | 53,7 % | +0.02 R |
| 15m | 16 | 62,5 % | -0.43 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 307 | 54,4 % | -0.12 R |
| 4-12 h | 180 | 52,8 % | -0.21 R |
| 12-24 h | 173 | 52,0 % | -0.14 R |
| 1-2 días | 58 | 55,2 % | +0.07 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 334 | 53,9 % | -0.13 R |
| bollinger | 223 | 54,7 % | -0.03 R |
| estocastico | 69 | 55,1 % | -0.20 R |
| barrida | 45 | 44,4 % | -0.28 R |
| order_block | 16 | 56,2 % | +0.04 R |
| fvg | 14 | 57,1 % | -0.61 R |
| ruptura | 8 | 37,5 % | -0.54 R |
| bos | 5 | 40,0 % | +0.56 R |
| choch | 4 | 75,0 % | -0.88 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| rsi | 2 | 100,0 % | +0.87 R |
| fibonacci | 1 | 0,0 % | -1.01 R |
| velas | 1 | 0,0 % | -1.02 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 221 | 51,6 % | -0.05 R |
| 00-04 h | 109 | 54,1 % | -0.04 R |
| 12-16 h | 109 | 56,0 % | -0.14 R |
| 08-12 h | 104 | 56,7 % | -0.16 R |
| 16-20 h | 91 | 47,3 % | -0.22 R |
| 20-24 h | 84 | 57,1 % | -0.33 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 298 | 50,3 % | -0.13 R |
| lateral (<20) | 270 | 58,5 % | -0.14 R |
| débil (20-25) | 150 | 50,7 % | -0.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 432 | 52,8 % | -0.18 R |
| baja | 147 | 55,1 % | -0.01 R |
| alta | 139 | 54,0 % | -0.11 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 262 | 54,2 % | -0.03 R |
| a favor | 257 | 50,6 % | -0.21 R |
| en contra | 199 | 56,3 % | -0.18 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 491 | 53,6 % | -0.12 R |
| en contra | 225 | 52,9 % | -0.16 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 450 | 54,2 % | -0.16 R |
| a favor | 268 | 52,2 % | -0.09 R |

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
| 07/10 22:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.54 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**103 señales** del 28/10/2026 al 23/11/2026. Acierto (precio a favor al vencer): **53,4 %** · resultado medio con SL/TP tras costes: **-0.25 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 69 | 53,6 % | -0.36 R |
| 52-55 % | 33 | 51,5 % | -0.01 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 23 | 34,8 % | -0.45 R |
| BTC/USDT | 18 | 55,6 % | -0.26 R |
| USD/CHF | 12 | 50,0 % | -0.17 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| USD/CAD | 3 | 66,7 % | +0.15 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| SOL/USDT | 2 | 0,0 % | -1.14 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 54 | 61,1 % | -0.21 R |
| 15m | 38 | 47,4 % | -0.26 R |
| 1h | 11 | 36,4 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 75 | 53,3 % | -0.14 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 8 | 62,5 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 30 | 33,3 % | -0.38 R |
| soportes | 30 | 66,7 % | -0.08 R |
| barrida | 13 | 46,2 % | -0.24 R |
| estocastico | 12 | 50,0 % | -0.66 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 3 | 66,7 % | +0.15 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 30 | 73,3 % | -0.18 R |
| 08-12 h | 24 | 54,2 % | +0.00 R |
| 20-24 h | 15 | 40,0 % | -0.36 R |
| 04-08 h | 14 | 35,7 % | -0.40 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 52 | 46,2 % | -0.18 R |
| lateral (<20) | 31 | 64,5 % | -0.18 R |
| débil (20-25) | 20 | 55,0 % | -0.56 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 58 | 53,4 % | -0.35 R |
| alta | 26 | 50,0 % | -0.25 R |
| baja | 19 | 57,9 % | +0.03 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 38 | 60,5 % | -0.29 R |
| sin tendencia | 33 | 57,6 % | -0.04 R |
| en contra | 32 | 40,6 % | -0.43 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 73 | 49,3 % | -0.39 R |
| en contra | 30 | 63,3 % | +0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 77 | 48,1 % | -0.28 R |
| a favor | 26 | 69,2 % | -0.19 R |

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
**41 señales** del 28/10/2026 al 21/11/2026. Acierto (precio a favor al vencer): **26,8 %** · resultado medio con SL/TP tras costes: **-0.54 R** · claramente peor que el azar (z = -3.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 24 | 33,3 % | -0.51 R |
| <52 % | 17 | 17,6 % | -0.58 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 17 | 41,2 % | -0.46 R |
| USD/CHF | 11 | 18,2 % | -0.18 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| EUR/GBP | 1 | 0,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 32 | 28,1 % | -0.64 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 3 | 0,0 % | -1.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 23 | 21,7 % | -0.63 R |
| 4-12 h | 12 | 33,3 % | -0.23 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 3 | 66,7 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 22 | 36,4 % | -0.47 R |
| estocastico | 17 | 29,4 % | -0.51 R |
| soportes | 4 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.06 R |
| 12-16 h | 8 | 25,0 % | -0.75 R |
| 20-24 h | 8 | 37,5 % | +0.43 R |
| 16-20 h | 6 | 16,7 % | -0.36 R |
| 04-08 h | 5 | 20,0 % | -1.02 R |
| 08-12 h | 5 | 40,0 % | -0.48 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 31 | 29,0 % | -0.69 R |
| débil (20-25) | 7 | 14,3 % | -0.36 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 30 | 23,3 % | -0.40 R |
| alta | 9 | 22,2 % | -1.04 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 29 | 20,7 % | -0.58 R |
| en contra | 7 | 42,9 % | -1.08 R |
| a favor | 5 | 40,0 % | +0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 37 | 21,6 % | -0.61 R |
| en contra | 4 | 75,0 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 35 | 22,9 % | -0.59 R |
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
