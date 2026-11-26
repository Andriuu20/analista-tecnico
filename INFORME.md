# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**803 señales** del 28/10/2025 al 25/11/2026. Acierto (precio a favor al vencer): **52,4 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 1.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 484 | 54,3 % | -0.03 R |
| 52-55 % | 267 | 47,6 % | -0.39 R |
| 55-58 % | 42 | 61,9 % | +0.30 R |
| ≥58 % | 10 | 50,0 % | -0.29 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 172 | 46,5 % | -0.22 R |
| AUD/USD | 115 | 60,9 % | -0.07 R |
| BTC/USDT | 113 | 49,6 % | -0.17 R |
| USD/CHF | 83 | 56,6 % | -0.10 R |
| SOL/USDT | 81 | 63,0 % | -0.06 R |
| EUR/GBP | 59 | 54,2 % | -0.17 R |
| USD/JPY | 58 | 46,6 % | -0.22 R |
| XRP/USDT | 42 | 35,7 % | -0.15 R |
| USD/CAD | 29 | 55,2 % | -0.21 R |
| GBP/JPY | 27 | 55,6 % | -0.03 R |
| Oro (XAU/USD) | 17 | 58,8 % | +0.16 R |
| EUR/USD | 3 | 33,3 % | +1.51 R |
| ETH/USDT | 2 | 50,0 % | -0.50 R |
| GBP/USD | 2 | 0,0 % | -1.15 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 339 | 49,3 % | -0.17 R |
| 15m | 289 | 56,4 % | -0.11 R |
| 5m | 130 | 52,3 % | -0.14 R |
| 4h | 45 | 51,1 % | -0.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 469 | 52,9 % | -0.13 R |
| 1-2 h | 258 | 53,9 % | -0.08 R |
| 30-59 min | 76 | 44,7 % | -0.35 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 377 | 48,5 % | -0.19 R |
| estocastico | 141 | 58,2 % | +0.05 R |
| velas | 116 | 57,8 % | +0.01 R |
| barrida | 53 | 58,5 % | -0.00 R |
| fibonacci | 38 | 52,6 % | -0.06 R |
| rsi | 28 | 46,4 % | -0.62 R |
| order_block | 27 | 59,3 % | -0.14 R |
| soportes | 14 | 50,0 % | -0.46 R |
| bos | 11 | 54,5 % | -0.20 R |
| ruptura | 2 | 0,0 % | -1.16 R |
| divergencia | 2 | 50,0 % | -1.11 R |
| supertrend | 2 | 0,0 % | -1.13 R |
| choch | 1 | 0,0 % | -1.18 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 173 | 51,4 % | -0.13 R |
| 12-16 h | 167 | 52,7 % | -0.24 R |
| 08-12 h | 136 | 47,1 % | -0.24 R |
| 20-24 h | 115 | 57,4 % | -0.16 R |
| 04-08 h | 113 | 50,4 % | +0.08 R |
| 00-04 h | 99 | 57,6 % | -0.05 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 351 | 50,7 % | -0.22 R |
| lateral (<20) | 290 | 54,5 % | -0.00 R |
| débil (20-25) | 162 | 52,5 % | -0.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 461 | 52,1 % | -0.17 R |
| alta | 191 | 50,8 % | -0.12 R |
| baja | 151 | 55,6 % | -0.06 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 357 | 53,2 % | -0.05 R |
| sin tendencia | 311 | 52,4 % | -0.19 R |
| en contra | 135 | 50,4 % | -0.25 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 630 | 51,3 % | -0.19 R |
| en contra | 165 | 56,4 % | +0.05 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 577 | 51,8 % | -0.13 R |
| a favor | 226 | 54,0 % | -0.15 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 75 min | estocastico | -2.45 % |
| 21/11 13:35 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -2.32 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 22/11 09:40 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -1.83 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 13/11 21:50 | XRP/USDT | 5m | COMPRAR | 50 min | estocastico | -1.54 % |
| 17/11 16:15 | BTC/USDT | 5m | COMPRAR | 100 min | estocastico | -1.51 % |
| 29/06 06:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.45 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**845 señales** del 16/12/2020 al 23/11/2026. Acierto (precio a favor al vencer): **50,7 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| plazo = **2-5 días** | acierta | 59,2 % en 169 | después 51,9 % en 129 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 64,6 % en 48 | después 54,4 % en 57 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 499 | 50,3 % | -0.10 R |
| 52-55 % | 307 | 51,8 % | -0.15 R |
| 55-58 % | 39 | 46,2 % | -0.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 157 | 51,6 % | -0.22 R |
| GBP/JPY | 145 | 45,5 % | -0.26 R |
| Oro (XAU/USD) | 142 | 53,5 % | +0.03 R |
| SOL/USDT | 96 | 54,2 % | -0.05 R |
| EUR/GBP | 61 | 62,3 % | +0.07 R |
| ETH/USDT | 59 | 47,5 % | -0.21 R |
| GBP/USD | 51 | 45,1 % | -0.13 R |
| AUD/USD | 39 | 48,7 % | -0.17 R |
| USD/JPY | 35 | 45,7 % | +0.04 R |
| USD/CAD | 33 | 45,5 % | -0.17 R |
| EUR/JPY | 14 | 50,0 % | -0.52 R |
| BTC/USDT | 8 | 50,0 % | -0.12 R |
| XRP/USDT | 5 | 60,0 % | +0.83 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 327 | 51,7 % | -0.08 R |
| 1h | 311 | 48,6 % | -0.25 R |
| 1d | 164 | 53,7 % | +0.08 R |
| 15m | 43 | 46,5 % | -0.30 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 298 | 56,0 % | +0.01 R |
| 4-12 h | 295 | 47,1 % | -0.17 R |
| 12-24 h | 194 | 47,4 % | -0.29 R |
| 1-2 días | 58 | 51,7 % | +0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 361 | 51,5 % | -0.07 R |
| bollinger | 269 | 50,6 % | -0.08 R |
| estocastico | 69 | 59,4 % | -0.16 R |
| barrida | 56 | 42,9 % | -0.22 R |
| velas | 27 | 48,1 % | -0.10 R |
| fibonacci | 22 | 40,9 % | -0.45 R |
| bos | 11 | 54,5 % | +0.04 R |
| rsi | 8 | 37,5 % | -1.15 R |
| ruptura | 8 | 37,5 % | -0.54 R |
| choch | 7 | 42,9 % | -0.67 R |
| divergencia | 4 | 50,0 % | -0.50 R |
| medias | 4 | 75,0 % | -0.10 R |
| order_block | 4 | 75,0 % | +1.29 R |
| supertrend | 4 | 50,0 % | -0.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 238 | 51,3 % | +0.01 R |
| 12-16 h | 140 | 50,0 % | -0.18 R |
| 08-12 h | 126 | 45,2 % | -0.22 R |
| 00-04 h | 120 | 54,2 % | +0.08 R |
| 16-20 h | 116 | 44,8 % | -0.33 R |
| 20-24 h | 105 | 59,0 % | -0.21 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 355 | 47,9 % | -0.10 R |
| lateral (<20) | 309 | 56,6 % | -0.19 R |
| débil (20-25) | 181 | 45,9 % | -0.04 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 498 | 49,0 % | -0.16 R |
| baja | 180 | 53,9 % | +0.06 R |
| alta | 167 | 52,1 % | -0.19 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 331 | 48,0 % | -0.13 R |
| sin tendencia | 302 | 51,3 % | -0.05 R |
| en contra | 212 | 53,8 % | -0.20 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 568 | 50,4 % | -0.15 R |
| en contra | 272 | 50,7 % | -0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 544 | 51,5 % | -0.13 R |
| a favor | 301 | 49,2 % | -0.10 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 22/08 10:00 | ETH/USDT | 4h | VENDER | 480 min | soportes | -13.06 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**125 señales** del 28/10/2026 al 25/11/2026. Acierto (precio a favor al vencer): **53,6 %** · resultado medio con SL/TP tras costes: **-0.27 R** · no se distingue del azar todavía (z = 0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 84 | 52,4 % | -0.41 R |
| 52-55 % | 35 | 54,3 % | +0.01 R |
| 55-58 % | 6 | 66,7 % | -0.07 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 31 | 41,9 % | -0.53 R |
| USD/JPY | 29 | 69,0 % | -0.04 R |
| BTC/USDT | 23 | 47,8 % | -0.23 R |
| USD/CHF | 12 | 50,0 % | -0.17 R |
| EUR/GBP | 7 | 57,1 % | -0.29 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| ETH/USDT | 5 | 60,0 % | -0.63 R |
| USD/CAD | 4 | 75,0 % | +0.32 R |
| GBP/JPY | 3 | 33,3 % | -1.22 R |
| SOL/USDT | 3 | 33,3 % | -0.31 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 69 | 62,3 % | -0.21 R |
| 15m | 41 | 48,8 % | -0.29 R |
| 1h | 15 | 26,7 % | -0.57 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 94 | 55,3 % | -0.17 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 11 | 45,5 % | -0.35 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 38 | 65,8 % | -0.22 R |
| bollinger | 37 | 32,4 % | -0.45 R |
| estocastico | 18 | 55,6 % | -0.32 R |
| barrida | 13 | 46,2 % | -0.24 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 4 | 75,0 % | +0.32 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 35 | 68,6 % | -0.26 R |
| 08-12 h | 29 | 55,2 % | -0.07 R |
| 20-24 h | 19 | 47,4 % | -0.12 R |
| 04-08 h | 18 | 38,9 % | -0.32 R |
| 12-16 h | 12 | 50,0 % | -0.94 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 57 | 45,6 % | -0.17 R |
| lateral (<20) | 39 | 64,1 % | -0.32 R |
| débil (20-25) | 29 | 55,2 % | -0.42 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 71 | 52,1 % | -0.37 R |
| alta | 32 | 50,0 % | -0.33 R |
| baja | 22 | 63,6 % | +0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 45 | 57,8 % | -0.28 R |
| sin tendencia | 44 | 59,1 % | -0.17 R |
| en contra | 36 | 41,7 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 89 | 49,4 % | -0.36 R |
| en contra | 36 | 63,9 % | -0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 89 | 48,3 % | -0.33 R |
| a favor | 36 | 66,7 % | -0.12 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 25/11 09:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -0.90 % |
| 24/11 05:10 | ETH/USDT | 5m | VENDER | 100 min | estocastico | -0.61 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 25/11 22:00 | BTC/USDT | 1h | VENDER | 120 min | bollinger | -0.37 % |
| 24/11 05:10 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -0.36 % |
| 19/11 09:35 | BTC/USDT | 5m | VENDER | 100 min | fibonacci | -0.34 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**50 señales** del 28/10/2026 al 25/11/2026. Acierto (precio a favor al vencer): **36,0 %** · resultado medio con SL/TP tras costes: **-0.60 R** · no se distingue del azar todavía (z = -2.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 25 | 36,0 % | -0.64 R |
| 52-55 % | 25 | 36,0 % | -0.56 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 18 | 44,4 % | -0.46 R |
| USD/CHF | 16 | 37,5 % | -0.35 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| EUR/GBP | 4 | 50,0 % | -1.15 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 38 | 36,8 % | -0.67 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 6 | 33,3 % | -1.12 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 27 | 33,3 % | -0.66 R |
| 4-12 h | 15 | 40,0 % | -0.37 R |
| 1-2 días | 5 | 60,0 % | — |
| 12-24 h | 3 | 0,0 % | -1.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 26 | 42,3 % | -0.54 R |
| estocastico | 20 | 40,0 % | -0.58 R |
| soportes | 6 | 16,7 % | -1.07 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 10 | 30,0 % | -0.84 R |
| 00-04 h | 9 | 22,2 % | -1.06 R |
| 20-24 h | 9 | 44,4 % | +0.22 R |
| 16-20 h | 8 | 37,5 % | -0.36 R |
| 04-08 h | 7 | 42,9 % | -1.02 R |
| 08-12 h | 7 | 42,9 % | -0.48 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 37 | 37,8 % | -0.74 R |
| débil (20-25) | 7 | 14,3 % | -0.36 R |
| lateral (<20) | 6 | 50,0 % | -0.07 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 38 | 34,2 % | -0.50 R |
| alta | 10 | 30,0 % | -1.04 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 32 | 25,0 % | -0.61 R |
| en contra | 11 | 63,6 % | -1.07 R |
| a favor | 7 | 42,9 % | +0.01 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 43 | 27,9 % | -0.67 R |
| en contra | 4 | 75,0 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 42 | 33,3 % | -0.65 R |
| a favor | 8 | 50,0 % | -0.24 R |

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
