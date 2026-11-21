# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1253 señales** del 16/01/2025 al 20/11/2026. Acierto (precio a favor al vencer): **52,4 %** · resultado medio con SL/TP tras costes: **-0.13 R** · no se distingue del azar todavía (z = 1.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,1 % en 148 | después 50,4 % en 135 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 60,4 % en 144 | pocos casos en la segunda mitad | ⏳ faltan datos |
| franja = **00-04 h** | acierta | 62,0 % en 79 | después 52,5 % en 118 casos | ❔ no se repite |
| dia = **jue** | acierta | 63,1 % en 122 | después 52,2 % en 136 casos | ❔ no se repite |
| zona_txt = **en contra** | acierta | 57,1 % en 203 | después 54,0 % en 291 casos | ✅ confirmado |
| estrategia = **velas** | acierta | 59,9 % en 207 | después 49,2 % en 59 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 765 | 52,8 % | -0.12 R |
| 52-55 % | 436 | 51,8 % | -0.15 R |
| 55-58 % | 44 | 54,5 % | +0.04 R |
| ≥58 % | 8 | 37,5 % | -0.80 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 283 | 55,5 % | -0.12 R |
| EUR/JPY | 157 | 43,9 % | -0.20 R |
| AUD/USD | 136 | 55,1 % | -0.08 R |
| SOL/USDT | 114 | 56,1 % | -0.16 R |
| EUR/GBP | 105 | 45,7 % | -0.20 R |
| USD/CAD | 104 | 55,8 % | -0.11 R |
| BTC/USDT | 86 | 52,3 % | -0.23 R |
| Oro (XAU/USD) | 71 | 47,9 % | -0.14 R |
| USD/CHF | 64 | 56,2 % | -0.00 R |
| GBP/JPY | 62 | 50,0 % | -0.16 R |
| XRP/USDT | 43 | 53,5 % | -0.17 R |
| ETH/USDT | 14 | 64,3 % | -0.09 R |
| EUR/USD | 11 | 63,6 % | +1.04 R |
| GBP/USD | 3 | 33,3 % | -0.18 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 393 | 49,6 % | -0.22 R |
| 5m | 360 | 52,2 % | -0.18 R |
| 15m | 356 | 52,5 % | -0.05 R |
| 4h | 144 | 60,4 % | +0.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 725 | 52,1 % | -0.11 R |
| 1-2 h | 423 | 54,1 % | -0.12 R |
| 30-59 min | 105 | 47,6 % | -0.31 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 409 | 48,9 % | -0.21 R |
| velas | 266 | 57,5 % | -0.01 R |
| soportes | 176 | 50,6 % | -0.21 R |
| fibonacci | 104 | 54,8 % | -0.02 R |
| order_block | 86 | 55,8 % | -0.09 R |
| estocastico | 67 | 49,3 % | -0.05 R |
| barrida | 37 | 67,6 % | +0.07 R |
| rsi | 36 | 44,4 % | -0.37 R |
| ruptura | 35 | 60,0 % | -0.08 R |
| bos | 27 | 48,1 % | -0.18 R |
| supertrend | 24 | 50,0 % | -0.24 R |
| fvg | 9 | 33,3 % | -0.33 R |
| divergencia | 3 | 66,7 % | +0.22 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 260 | 50,4 % | -0.14 R |
| 12-16 h | 251 | 52,6 % | -0.15 R |
| 00-04 h | 197 | 56,3 % | -0.08 R |
| 08-12 h | 193 | 49,2 % | -0.30 R |
| 04-08 h | 187 | 51,9 % | -0.07 R |
| 20-24 h | 165 | 55,2 % | -0.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 517 | 49,1 % | -0.24 R |
| lateral (<20) | 469 | 54,2 % | -0.04 R |
| débil (20-25) | 267 | 55,8 % | -0.08 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 707 | 53,2 % | -0.15 R |
| alta | 299 | 47,8 % | -0.16 R |
| baja | 247 | 55,9 % | -0.03 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 551 | 54,3 % | -0.08 R |
| sin tendencia | 479 | 50,1 % | -0.16 R |
| en contra | 223 | 52,9 % | -0.18 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 746 | 50,7 % | -0.19 R |
| en contra | 494 | 55,3 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 742 | 51,5 % | -0.11 R |
| a favor | 511 | 53,8 % | -0.15 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 16/11 15:30 | XRP/USDT | 15m | COMPRAR | 30 min | supertrend | -2.66 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 13/11 03:25 | SOL/USDT | 5m | COMPRAR | 50 min | bollinger | -1.36 % |
| 19/11 15:25 | BTC/USDT | 5m | COMPRAR | 100 min | fibonacci | -1.35 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**770 señales** del 08/01/2021 al 19/11/2026. Acierto (precio a favor al vencer): **52,9 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **mar** | acierta | 62,4 % en 85 | después 43,9 % en 66 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 432 | 54,9 % | -0.13 R |
| 52-55 % | 296 | 50,3 % | -0.17 R |
| 55-58 % | 42 | 50,0 % | +0.03 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 130 | 55,4 % | -0.07 R |
| USD/CHF | 129 | 58,1 % | -0.14 R |
| Oro (XAU/USD) | 113 | 51,3 % | -0.02 R |
| SOL/USDT | 108 | 55,6 % | -0.15 R |
| GBP/USD | 72 | 50,0 % | -0.11 R |
| EUR/GBP | 58 | 58,6 % | -0.36 R |
| ETH/USDT | 49 | 38,8 % | -0.33 R |
| USD/JPY | 41 | 46,3 % | -0.04 R |
| AUD/USD | 35 | 51,4 % | -0.06 R |
| EUR/JPY | 24 | 45,8 % | -0.54 R |
| XRP/USDT | 10 | 50,0 % | +0.29 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 329 | 53,2 % | -0.10 R |
| 4h | 289 | 52,6 % | -0.23 R |
| 1d | 134 | 52,2 % | +0.05 R |
| 15m | 18 | 55,6 % | -0.67 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 282 | 53,5 % | -0.10 R |
| 4-12 h | 217 | 53,5 % | -0.16 R |
| 12-24 h | 217 | 50,7 % | -0.20 R |
| 1-2 días | 54 | 55,6 % | -0.00 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 320 | 53,4 % | -0.16 R |
| bollinger | 259 | 54,8 % | -0.02 R |
| barrida | 80 | 50,0 % | -0.17 R |
| estocastico | 67 | 55,2 % | -0.14 R |
| order_block | 18 | 50,0 % | +0.06 R |
| fvg | 9 | 55,6 % | -0.20 R |
| ruptura | 7 | 28,6 % | -0.48 R |
| choch | 6 | 50,0 % | -0.96 R |
| rsi | 6 | 50,0 % | -1.16 R |
| fibonacci | 2 | 0,0 % | -1.02 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| velas | 1 | 0,0 % | -1.02 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 200 | 49,5 % | -0.04 R |
| 08-12 h | 125 | 52,8 % | -0.22 R |
| 12-16 h | 124 | 54,8 % | -0.11 R |
| 00-04 h | 120 | 55,0 % | -0.05 R |
| 16-20 h | 107 | 52,3 % | -0.19 R |
| 20-24 h | 94 | 55,3 % | -0.32 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 323 | 49,8 % | -0.16 R |
| lateral (<20) | 291 | 56,7 % | -0.10 R |
| débil (20-25) | 156 | 51,9 % | -0.16 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 442 | 52,0 % | -0.16 R |
| baja | 170 | 51,8 % | -0.12 R |
| alta | 158 | 56,3 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 291 | 50,9 % | -0.19 R |
| sin tendencia | 281 | 53,0 % | -0.11 R |
| en contra | 198 | 55,6 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 551 | 53,7 % | -0.13 R |
| en contra | 215 | 50,2 % | -0.17 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 498 | 52,6 % | -0.16 R |
| a favor | 272 | 53,3 % | -0.09 R |

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
| 13/11 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -6.32 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 19/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -5.99 % |

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
