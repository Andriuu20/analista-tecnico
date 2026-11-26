# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**870 señales** del 29/10/2025 al 26/11/2026. Acierto (precio a favor al vencer): **52,1 %** · resultado medio con SL/TP tras costes: **-0.11 R** · no se distingue del azar todavía (z = 1.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **SOL/USDT** | acierta | 62,7 % en 75 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 61,8 % en 89 | después 58,0 % en 81 casos | ✅ confirmado |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 555 | 53,9 % | -0.06 R |
| 52-55 % | 267 | 47,9 % | -0.20 R |
| 55-58 % | 37 | 54,1 % | -0.19 R |
| ≥58 % | 11 | 54,5 % | -0.45 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 127 | 45,7 % | -0.25 R |
| USD/CAD | 109 | 55,0 % | -0.08 R |
| USD/CHF | 105 | 50,5 % | -0.04 R |
| USD/JPY | 99 | 58,6 % | -0.11 R |
| SOL/USDT | 86 | 64,0 % | -0.10 R |
| EUR/GBP | 81 | 48,1 % | -0.21 R |
| Oro (XAU/USD) | 63 | 46,0 % | -0.15 R |
| BTC/USDT | 60 | 51,7 % | -0.18 R |
| AUD/USD | 47 | 55,3 % | -0.24 R |
| XRP/USDT | 46 | 37,0 % | +0.19 R |
| GBP/JPY | 38 | 52,6 % | +0.09 R |
| EUR/USD | 9 | 77,8 % | +0.49 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 367 | 49,9 % | -0.15 R |
| 5m | 240 | 54,2 % | -0.03 R |
| 15m | 192 | 51,0 % | -0.15 R |
| 4h | 71 | 59,2 % | -0.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 475 | 51,6 % | -0.18 R |
| 1-2 h | 279 | 55,6 % | -0.01 R |
| 30-59 min | 116 | 45,7 % | -0.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 342 | 51,2 % | -0.13 R |
| estocastico | 117 | 47,9 % | -0.04 R |
| order_block | 91 | 52,7 % | -0.11 R |
| velas | 86 | 59,3 % | -0.06 R |
| fibonacci | 75 | 56,0 % | -0.08 R |
| barrida | 51 | 51,0 % | -0.07 R |
| bos | 34 | 41,2 % | -0.30 R |
| ruptura | 33 | 54,5 % | -0.05 R |
| rsi | 31 | 54,8 % | +0.04 R |
| soportes | 26 | 57,7 % | -0.16 R |
| choch | 2 | 0,0 % | -1.20 R |
| divergencia | 2 | 50,0 % | -1.11 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 195 | 51,3 % | -0.13 R |
| 16-20 h | 187 | 49,7 % | -0.13 R |
| 08-12 h | 141 | 54,6 % | -0.21 R |
| 04-08 h | 129 | 51,2 % | +0.10 R |
| 20-24 h | 120 | 52,5 % | -0.26 R |
| 00-04 h | 98 | 55,1 % | +0.01 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 367 | 51,5 % | -0.14 R |
| lateral (<20) | 319 | 52,0 % | -0.05 R |
| débil (20-25) | 184 | 53,3 % | -0.15 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 477 | 52,8 % | -0.14 R |
| alta | 222 | 48,2 % | -0.10 R |
| baja | 171 | 55,0 % | -0.05 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 386 | 53,4 % | -0.07 R |
| sin tendencia | 337 | 52,8 % | -0.16 R |
| en contra | 147 | 46,9 % | -0.09 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 585 | 50,9 % | -0.12 R |
| en contra | 280 | 54,3 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 506 | 51,8 % | -0.07 R |
| a favor | 364 | 52,5 % | -0.16 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 75 min | estocastico | -2.45 % |
| 13/11 03:15 | SOL/USDT | 5m | COMPRAR | 75 min | estocastico | -2.13 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 13/11 21:50 | XRP/USDT | 5m | COMPRAR | 50 min | estocastico | -1.54 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**868 señales** del 16/12/2020 al 25/11/2026. Acierto (precio a favor al vencer): **49,3 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = -0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **Oro (XAU/USD)** | acierta | 59,3 % en 118 | pocos casos en la segunda mitad | ⏳ faltan datos |
| plazo = **2-5 días** | acierta | 60,3 % en 156 | después 49,6 % en 119 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 534 | 49,8 % | -0.18 R |
| 52-55 % | 317 | 48,6 % | -0.22 R |
| 55-58 % | 17 | 47,1 % | +0.03 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 194 | 49,5 % | -0.21 R |
| GBP/JPY | 147 | 46,9 % | -0.36 R |
| Oro (XAU/USD) | 142 | 53,5 % | +0.06 R |
| SOL/USDT | 80 | 55,0 % | -0.09 R |
| ETH/USDT | 77 | 48,1 % | -0.37 R |
| EUR/GBP | 66 | 59,1 % | -0.22 R |
| AUD/USD | 37 | 48,6 % | +0.15 R |
| USD/JPY | 35 | 31,4 % | -0.23 R |
| USD/CAD | 29 | 48,3 % | -0.29 R |
| GBP/USD | 27 | 37,0 % | -0.22 R |
| EUR/JPY | 23 | 43,5 % | -0.34 R |
| XRP/USDT | 11 | 36,4 % | -0.33 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 354 | 50,6 % | -0.21 R |
| 1h | 316 | 45,9 % | -0.30 R |
| 1d | 162 | 53,1 % | +0.13 R |
| 15m | 36 | 50,0 % | -0.39 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 361 | 46,5 % | -0.29 R |
| 2-5 días | 275 | 55,6 % | -0.03 R |
| 12-24 h | 183 | 44,3 % | -0.30 R |
| 1-2 días | 49 | 53,1 % | +0.14 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 411 | 48,9 % | -0.18 R |
| bollinger | 290 | 51,4 % | -0.14 R |
| estocastico | 56 | 55,4 % | -0.17 R |
| barrida | 29 | 34,5 % | -0.36 R |
| velas | 27 | 51,9 % | -0.22 R |
| fibonacci | 13 | 38,5 % | -0.56 R |
| order_block | 11 | 36,4 % | -0.33 R |
| ruptura | 10 | 50,0 % | +0.16 R |
| bos | 6 | 50,0 % | +0.29 R |
| rsi | 6 | 33,3 % | -1.16 R |
| choch | 4 | 50,0 % | -0.53 R |
| divergencia | 4 | 50,0 % | -0.50 R |
| supertrend | 4 | 50,0 % | -0.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 240 | 52,9 % | -0.04 R |
| 12-16 h | 148 | 52,0 % | -0.28 R |
| 08-12 h | 135 | 43,7 % | -0.37 R |
| 00-04 h | 122 | 45,9 % | -0.04 R |
| 16-20 h | 115 | 44,3 % | -0.33 R |
| 20-24 h | 108 | 53,7 % | -0.18 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 352 | 44,9 % | -0.21 R |
| lateral (<20) | 325 | 57,2 % | -0.22 R |
| débil (20-25) | 191 | 44,0 % | -0.09 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 508 | 47,0 % | -0.24 R |
| baja | 191 | 53,4 % | -0.02 R |
| alta | 169 | 51,5 % | -0.23 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 345 | 45,8 % | -0.23 R |
| sin tendencia | 310 | 50,3 % | -0.16 R |
| en contra | 213 | 53,5 % | -0.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 591 | 49,9 % | -0.17 R |
| en contra | 273 | 47,6 % | -0.22 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 561 | 50,8 % | -0.18 R |
| a favor | 307 | 46,6 % | -0.20 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 22/08 10:00 | ETH/USDT | 4h | VENDER | 480 min | soportes | -13.06 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**127 señales** del 28/10/2026 al 26/11/2026. Acierto (precio a favor al vencer): **54,3 %** · resultado medio con SL/TP tras costes: **-0.28 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 85 | 52,9 % | -0.42 R |
| 52-55 % | 35 | 54,3 % | +0.01 R |
| 55-58 % | 7 | 71,4 % | -0.07 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 31 | 41,9 % | -0.53 R |
| USD/JPY | 29 | 69,0 % | -0.04 R |
| BTC/USDT | 23 | 47,8 % | -0.23 R |
| USD/CHF | 12 | 50,0 % | -0.17 R |
| EUR/GBP | 7 | 57,1 % | -0.29 R |
| ETH/USDT | 6 | 66,7 % | -0.63 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| USD/CAD | 5 | 80,0 % | +0.32 R |
| GBP/JPY | 3 | 33,3 % | -1.18 R |
| SOL/USDT | 3 | 33,3 % | -0.31 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 71 | 63,4 % | -0.21 R |
| 15m | 41 | 48,8 % | -0.29 R |
| 1h | 15 | 26,7 % | -0.61 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 96 | 56,2 % | -0.18 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 11 | 45,5 % | -0.35 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 38 | 65,8 % | -0.22 R |
| bollinger | 37 | 32,4 % | -0.47 R |
| estocastico | 19 | 57,9 % | -0.32 R |
| barrida | 13 | 46,2 % | -0.24 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 4 | 75,0 % | +0.32 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| ruptura | 1 | 100,0 % | — |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 35 | 68,6 % | -0.26 R |
| 08-12 h | 31 | 58,1 % | -0.10 R |
| 20-24 h | 19 | 47,4 % | -0.12 R |
| 04-08 h | 18 | 38,9 % | -0.32 R |
| 12-16 h | 12 | 50,0 % | -0.94 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 58 | 46,6 % | -0.19 R |
| lateral (<20) | 40 | 65,0 % | -0.32 R |
| débil (20-25) | 29 | 55,2 % | -0.42 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 72 | 52,8 % | -0.37 R |
| alta | 32 | 50,0 % | -0.36 R |
| baja | 23 | 65,2 % | +0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 46 | 58,7 % | -0.30 R |
| sin tendencia | 45 | 60,0 % | -0.17 R |
| en contra | 36 | 41,7 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 90 | 50,0 % | -0.36 R |
| en contra | 37 | 64,9 % | -0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 90 | 48,9 % | -0.33 R |
| a favor | 37 | 67,6 % | -0.15 R |

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
