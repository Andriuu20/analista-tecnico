# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1112 señales** del 16/01/2025 al 21/11/2026. Acierto (precio a favor al vencer): **52,8 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 1.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,3 % en 146 | después 47,2 % en 125 casos | ❔ no se repite |
| mercado = **AUD/USD** | acierta | 69,7 % en 33 | después 54,3 % en 35 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 58,6 % en 162 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 62,8 % en 113 | después 53,4 % en 118 casos | ❔ no se repite |
| zona_txt = **en contra** | acierta | 59,5 % en 168 | después 54,5 % en 211 casos | ✅ confirmado |
| estructura_txt = **a favor** | acierta | 58,0 % en 174 | después 54,1 % en 209 casos | ✅ confirmado |
| estrategia = **velas** | acierta | 61,5 % en 179 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 723 | 53,5 % | -0.07 R |
| 52-55 % | 337 | 51,0 % | -0.23 R |
| 55-58 % | 42 | 54,8 % | -0.07 R |
| ≥58 % | 10 | 50,0 % | -0.35 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 271 | 54,2 % | -0.13 R |
| EUR/JPY | 137 | 45,3 % | -0.20 R |
| SOL/USDT | 126 | 57,9 % | +0.09 R |
| EUR/GBP | 104 | 45,2 % | -0.30 R |
| USD/CAD | 84 | 52,4 % | -0.09 R |
| AUD/USD | 68 | 61,8 % | +0.15 R |
| Oro (XAU/USD) | 67 | 53,7 % | -0.43 R |
| GBP/JPY | 66 | 53,0 % | -0.12 R |
| USD/CHF | 65 | 56,9 % | -0.04 R |
| BTC/USDT | 56 | 53,6 % | -0.32 R |
| ETH/USDT | 33 | 45,5 % | -0.22 R |
| XRP/USDT | 16 | 43,8 % | -0.27 R |
| EUR/USD | 15 | 66,7 % | +0.51 R |
| GBP/USD | 4 | 50,0 % | +0.61 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 403 | 49,6 % | -0.18 R |
| 5m | 278 | 51,4 % | -0.11 R |
| 15m | 269 | 55,4 % | -0.07 R |
| 4h | 162 | 58,6 % | -0.10 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 647 | 53,3 % | -0.12 R |
| 1-2 h | 378 | 53,2 % | -0.10 R |
| 30-59 min | 87 | 47,1 % | -0.29 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 431 | 49,0 % | -0.23 R |
| velas | 202 | 58,9 % | +0.05 R |
| soportes | 176 | 48,3 % | -0.35 R |
| order_block | 85 | 51,8 % | -0.10 R |
| estocastico | 62 | 61,3 % | +0.37 R |
| fibonacci | 50 | 60,0 % | +0.08 R |
| rsi | 40 | 52,5 % | -0.07 R |
| barrida | 37 | 62,2 % | +0.12 R |
| bos | 19 | 63,2 % | +0.01 R |
| fvg | 9 | 33,3 % | -0.34 R |
| supertrend | 8 | 50,0 % | -0.61 R |
| divergencia | 2 | 50,0 % | -1.11 R |
| ruptura | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 242 | 51,2 % | -0.13 R |
| 12-16 h | 230 | 53,5 % | -0.07 R |
| 08-12 h | 168 | 45,2 % | -0.41 R |
| 00-04 h | 167 | 55,7 % | -0.10 R |
| 04-08 h | 162 | 54,9 % | +0.05 R |
| 20-24 h | 143 | 57,3 % | -0.10 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 454 | 51,3 % | -0.17 R |
| lateral (<20) | 412 | 56,1 % | -0.02 R |
| débil (20-25) | 246 | 50,0 % | -0.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 605 | 52,2 % | -0.13 R |
| alta | 268 | 50,7 % | -0.10 R |
| baja | 239 | 56,5 % | -0.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 483 | 54,7 % | -0.06 R |
| sin tendencia | 441 | 51,2 % | -0.20 R |
| en contra | 188 | 51,6 % | -0.13 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 724 | 50,6 % | -0.18 R |
| en contra | 379 | 56,7 % | -0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 729 | 51,2 % | -0.12 R |
| a favor | 383 | 55,9 % | -0.13 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 02:20 | SOL/USDT | 5m | VENDER | 100 min | velas | -3.90 % |
| 16/11 15:30 | XRP/USDT | 15m | COMPRAR | 30 min | supertrend | -2.66 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 100 min | estocastico | -2.19 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 04/08 22:00 | Oro (XAU/USD) | 4h | VENDER | 240 min | soportes | -1.40 % |
| 13/11 03:25 | SOL/USDT | 5m | COMPRAR | 50 min | bollinger | -1.36 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**700 señales** del 08/01/2021 al 20/11/2026. Acierto (precio a favor al vencer): **53,7 %** · resultado medio con SL/TP tras costes: **-0.16 R** · no se distingue del azar todavía (z = 2.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 401 | 56,9 % | -0.16 R |
| 52-55 % | 263 | 49,8 % | -0.18 R |
| 55-58 % | 36 | 47,2 % | +0.04 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 120 | 58,3 % | -0.16 R |
| Oro (XAU/USD) | 113 | 51,3 % | -0.02 R |
| GBP/JPY | 102 | 58,8 % | -0.23 R |
| SOL/USDT | 95 | 53,7 % | -0.15 R |
| EUR/GBP | 59 | 59,3 % | -0.36 R |
| USD/JPY | 58 | 53,4 % | +0.03 R |
| GBP/USD | 45 | 46,7 % | -0.28 R |
| ETH/USDT | 43 | 37,2 % | -0.39 R |
| AUD/USD | 32 | 56,2 % | +0.17 R |
| EUR/JPY | 22 | 50,0 % | -0.48 R |
| XRP/USDT | 9 | 55,6 % | +0.44 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |
| USD/CAD | 1 | 0,0 % | -1.08 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 276 | 52,2 % | -0.27 R |
| 1h | 273 | 55,7 % | -0.13 R |
| 1d | 134 | 52,2 % | +0.05 R |
| 15m | 17 | 58,8 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 279 | 52,3 % | -0.13 R |
| 4-12 h | 184 | 54,9 % | -0.18 R |
| 12-24 h | 180 | 53,9 % | -0.23 R |
| 1-2 días | 57 | 56,1 % | +0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 312 | 54,8 % | -0.15 R |
| bollinger | 223 | 56,1 % | -0.06 R |
| estocastico | 69 | 52,2 % | -0.20 R |
| barrida | 47 | 44,7 % | -0.31 R |
| order_block | 17 | 52,9 % | -0.02 R |
| fvg | 14 | 57,1 % | -0.61 R |
| ruptura | 8 | 37,5 % | -0.54 R |
| bos | 5 | 40,0 % | +0.56 R |
| choch | 4 | 75,0 % | -0.88 R |
| rsi | 2 | 100,0 % | +0.87 R |
| fibonacci | 2 | 0,0 % | -1.02 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| velas | 2 | 0,0 % | -1.05 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 196 | 49,5 % | -0.05 R |
| 12-16 h | 114 | 56,1 % | -0.18 R |
| 00-04 h | 112 | 53,6 % | -0.07 R |
| 08-12 h | 109 | 56,0 % | -0.20 R |
| 16-20 h | 87 | 51,7 % | -0.26 R |
| 20-24 h | 82 | 59,8 % | -0.34 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 298 | 50,7 % | -0.14 R |
| lateral (<20) | 264 | 57,6 % | -0.16 R |
| débil (20-25) | 138 | 52,9 % | -0.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 411 | 51,8 % | -0.22 R |
| baja | 147 | 58,5 % | -0.05 R |
| alta | 142 | 54,2 % | -0.11 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 267 | 51,3 % | -0.25 R |
| sin tendencia | 243 | 53,9 % | -0.07 R |
| en contra | 190 | 56,8 % | -0.14 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 487 | 54,0 % | -0.14 R |
| en contra | 212 | 52,8 % | -0.19 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 443 | 54,6 % | -0.17 R |
| a favor | 257 | 52,1 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**99 señales** del 28/10/2026 al 20/11/2026. Acierto (precio a favor al vencer): **53,5 %** · resultado medio con SL/TP tras costes: **-0.23 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 65 | 53,8 % | -0.33 R |
| 52-55 % | 33 | 51,5 % | -0.01 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 22 | 36,4 % | -0.42 R |
| BTC/USDT | 15 | 53,3 % | -0.20 R |
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
| 5m | 52 | 61,5 % | -0.18 R |
| 15m | 38 | 47,4 % | -0.26 R |
| 1h | 9 | 33,3 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 75 | 53,3 % | -0.14 R |
| 30-59 min | 18 | 50,0 % | -0.66 R |
| 2-4 h | 6 | 66,7 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 29 | 69,0 % | -0.04 R |
| bollinger | 28 | 32,1 % | -0.38 R |
| barrida | 13 | 46,2 % | -0.24 R |
| estocastico | 11 | 45,5 % | -0.61 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 3 | 66,7 % | +0.15 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 28 | 75,0 % | -0.11 R |
| 08-12 h | 23 | 52,2 % | +0.00 R |
| 20-24 h | 15 | 40,0 % | -0.36 R |
| 04-08 h | 13 | 38,5 % | -0.40 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 49 | 46,9 % | -0.14 R |
| lateral (<20) | 31 | 64,5 % | -0.18 R |
| débil (20-25) | 19 | 52,6 % | -0.56 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 56 | 55,4 % | -0.33 R |
| alta | 25 | 48,0 % | -0.25 R |
| baja | 18 | 55,6 % | +0.10 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 35 | 62,9 % | -0.27 R |
| en contra | 32 | 40,6 % | -0.43 R |
| sin tendencia | 32 | 56,2 % | -0.00 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 69 | 49,3 % | -0.36 R |
| en contra | 30 | 63,3 % | +0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 73 | 47,9 % | -0.25 R |
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
**39 señales** del 28/10/2026 al 19/11/2026. Acierto (precio a favor al vencer): **23,1 %** · resultado medio con SL/TP tras costes: **-0.39 R** · claramente peor que el azar (z = -3.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 22 | 27,3 % | -0.41 R |
| <52 % | 17 | 17,6 % | -0.36 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 15 | 33,3 % | -0.23 R |
| USD/CHF | 11 | 18,2 % | -0.06 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| EUR/GBP | 1 | 0,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 30 | 23,3 % | -0.48 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 3 | 0,0 % | -1.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 23 | 21,7 % | -0.36 R |
| 4-12 h | 12 | 33,3 % | -0.23 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 1 | 0,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 20 | 30,0 % | -0.20 R |
| estocastico | 16 | 25,0 % | -0.35 R |
| soportes | 4 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.09 R |
| 12-16 h | 8 | 25,0 % | -0.70 R |
| 20-24 h | 7 | 28,6 % | +0.43 R |
| 16-20 h | 6 | 16,7 % | -0.22 R |
| 08-12 h | 5 | 40,0 % | -0.29 R |
| 04-08 h | 4 | 0,0 % | -1.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 29 | 24,1 % | -0.56 R |
| débil (20-25) | 7 | 14,3 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 28 | 17,9 % | -0.31 R |
| alta | 9 | 22,2 % | -1.06 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 29 | 20,7 % | -0.43 R |
| a favor | 5 | 40,0 % | +0.40 R |
| en contra | 5 | 20,0 % | -1.11 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 35 | 17,1 % | -0.47 R |
| en contra | 4 | 75,0 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 33 | 18,2 % | -0.43 R |
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
