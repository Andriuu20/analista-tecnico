# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**670 señales** del 16/09/2025 al 09/11/2026. Acierto (precio a favor al vencer): **52,5 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 404 | 51,0 % | -0.09 R |
| 52-55 % | 228 | 56,1 % | -0.10 R |
| 55-58 % | 38 | 47,4 % | -0.50 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 151 | 48,3 % | -0.08 R |
| USD/JPY | 99 | 52,5 % | -0.06 R |
| USD/CHF | 97 | 64,9 % | -0.00 R |
| Oro (XAU/USD) | 85 | 50,6 % | -0.08 R |
| EUR/GBP | 69 | 47,8 % | -0.13 R |
| XRP/USDT | 58 | 46,6 % | -0.23 R |
| BTC/USDT | 47 | 59,6 % | -0.28 R |
| GBP/JPY | 37 | 48,6 % | -0.17 R |
| SOL/USDT | 20 | 50,0 % | -0.35 R |
| ETH/USDT | 6 | 83,3 % | -0.60 R |
| USD/CAD | 1 | 0,0 % | -1.16 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 284 | 47,2 % | -0.14 R |
| 5m | 173 | 56,6 % | -0.10 R |
| 15m | 170 | 57,1 % | -0.06 R |
| 4h | 43 | 53,5 % | -0.29 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 318 | 53,1 % | -0.11 R |
| 2-4 h | 292 | 49,7 % | -0.15 R |
| 30-59 min | 60 | 63,3 % | +0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 324 | 51,2 % | -0.19 R |
| barrida | 71 | 63,4 % | +0.04 R |
| soportes | 70 | 52,9 % | -0.17 R |
| bos | 60 | 51,7 % | -0.03 R |
| estocastico | 56 | 57,1 % | -0.13 R |
| velas | 54 | 50,0 % | +0.09 R |
| rsi | 22 | 45,5 % | -0.10 R |
| fibonacci | 13 | 46,2 % | -0.33 R |
| supertrend | 4 | 50,0 % | -0.14 R |
| divergencia | 2 | 0,0 % | +0.91 R |
| ruptura | 1 | 0,0 % | -1.16 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 156 | 54,5 % | -0.18 R |
| 12-16 h | 125 | 51,2 % | -0.31 R |
| 08-12 h | 110 | 47,3 % | -0.25 R |
| 20-24 h | 109 | 52,3 % | -0.14 R |
| 00-04 h | 92 | 55,4 % | +0.00 R |
| 04-08 h | 78 | 55,1 % | +0.41 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 333 | 54,4 % | -0.09 R |
| lateral (<20) | 216 | 46,8 % | -0.16 R |
| débil (20-25) | 121 | 57,9 % | -0.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 365 | 49,3 % | -0.12 R |
| alta | 191 | 58,1 % | -0.04 R |
| baja | 114 | 53,5 % | -0.25 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 272 | 49,3 % | -0.15 R |
| a favor | 262 | 53,4 % | -0.07 R |
| en contra | 136 | 57,4 % | -0.14 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 493 | 53,8 % | -0.17 R |
| en contra | 171 | 48,5 % | +0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 471 | 53,9 % | -0.17 R |
| a favor | 199 | 49,2 % | +0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.79 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 08/07 02:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.34 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 05/11 16:15 | XRP/USDT | 5m | COMPRAR | 50 min | bollinger | -1.20 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**842 señales** del 08/01/2021 al 09/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.09 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 64,3 % en 56 | después 55,3 % en 94 casos | ✅ confirmado |
| franja = **20-24 h** | acierta | 66,0 % en 50 | después 52,2 % en 46 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | acierta | 58,3 % en 163 | después 51,7 % en 143 casos | ❔ no se repite |
| tendencia_txt = **sin tendencia** | acierta | 60,0 % en 145 | después 51,4 % en 173 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 460 | 52,4 % | -0.09 R |
| 52-55 % | 343 | 53,9 % | -0.08 R |
| 55-58 % | 39 | 46,2 % | -0.14 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 150 | 58,7 % | -0.13 R |
| USD/CHF | 141 | 51,1 % | -0.12 R |
| SOL/USDT | 129 | 55,8 % | +0.02 R |
| Oro (XAU/USD) | 117 | 52,1 % | +0.05 R |
| GBP/USD | 89 | 52,8 % | -0.16 R |
| ETH/USDT | 78 | 44,9 % | -0.23 R |
| EUR/GBP | 49 | 59,2 % | -0.10 R |
| AUD/USD | 37 | 54,1 % | +0.34 R |
| USD/JPY | 29 | 31,0 % | -0.40 R |
| EUR/JPY | 15 | 73,3 % | -0.05 R |
| XRP/USDT | 6 | 0,0 % | -1.07 R |
| BTC/USDT | 2 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 339 | 54,3 % | -0.19 R |
| 4h | 318 | 53,1 % | -0.08 R |
| 1d | 139 | 52,5 % | +0.10 R |
| 15m | 46 | 39,1 % | +0.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 291 | 52,9 % | +0.01 R |
| 12-24 h | 270 | 52,6 % | -0.23 R |
| 4-12 h | 216 | 51,9 % | -0.08 R |
| 1-2 días | 65 | 55,4 % | +0.07 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 310 | 54,2 % | -0.11 R |
| bollinger | 298 | 55,7 % | +0.01 R |
| barrida | 100 | 51,0 % | -0.22 R |
| estocastico | 86 | 46,5 % | -0.01 R |
| choch | 15 | 73,3 % | -0.05 R |
| ruptura | 13 | 53,8 % | +0.49 R |
| fibonacci | 7 | 28,6 % | -0.74 R |
| bos | 6 | 16,7 % | -0.91 R |
| rsi | 5 | 40,0 % | -0.18 R |
| velas | 3 | 0,0 % | -0.70 R |
| order_block | 3 | 0,0 % | -1.05 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| medias | 1 | 0,0 % | -1.13 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 223 | 53,4 % | +0.03 R |
| 08-12 h | 140 | 48,6 % | -0.30 R |
| 00-04 h | 137 | 54,7 % | -0.11 R |
| 16-20 h | 124 | 46,0 % | -0.12 R |
| 12-16 h | 122 | 55,7 % | +0.00 R |
| 20-24 h | 96 | 59,4 % | -0.06 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 363 | 51,5 % | -0.06 R |
| lateral (<20) | 306 | 55,2 % | -0.11 R |
| débil (20-25) | 173 | 50,9 % | -0.09 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 465 | 51,4 % | -0.06 R |
| baja | 193 | 54,9 % | -0.14 R |
| alta | 184 | 53,8 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 318 | 55,3 % | -0.08 R |
| a favor | 303 | 48,8 % | -0.12 R |
| en contra | 221 | 54,3 % | -0.06 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 617 | 52,8 % | -0.09 R |
| en contra | 220 | 51,4 % | -0.07 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 548 | 51,8 % | -0.11 R |
| a favor | 294 | 54,4 % | -0.05 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 13/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -10.51 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 2400 min | bollinger | -8.81 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**47 señales** del 28/10/2026 al 09/11/2026. Acierto (precio a favor al vencer): **55,3 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 32 | 62,5 % | -0.25 R |
| 52-55 % | 14 | 35,7 % | +0.09 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 16 | 68,8 % | +0.04 R |
| EUR/JPY | 14 | 42,9 % | -0.57 R |
| USD/CHF | 4 | 50,0 % | +0.85 R |
| EUR/GBP | 4 | 50,0 % | -0.37 R |
| BTC/USDT | 2 | 50,0 % | — |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| ETH/USDT | 2 | 50,0 % | -1.21 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 24 | 58,3 % | -0.21 R |
| 15m | 21 | 52,4 % | -0.15 R |
| 1h | 2 | 50,0 % | — |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 32 | 50,0 % | -0.12 R |
| 30-59 min | 12 | 58,3 % | -0.55 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 16 | 68,8 % | +0.04 R |
| bollinger | 14 | 35,7 % | -0.66 R |
| estocastico | 9 | 55,6 % | -0.28 R |
| barrida | 5 | 40,0 % | +0.35 R |
| rsi | 5 | 80,0 % | -0.43 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 15 | 80,0 % | -0.00 R |
| 20-24 h | 10 | 30,0 % | -0.35 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 6 | 66,7 % | -0.09 R |
| 04-08 h | 4 | 50,0 % | +0.34 R |
| 08-12 h | 4 | 25,0 % | +1.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 24 | 58,3 % | +0.03 R |
| lateral (<20) | 12 | 50,0 % | -0.17 R |
| débil (20-25) | 11 | 54,5 % | -0.80 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 26 | 53,8 % | -0.14 R |
| alta | 13 | 61,5 % | -0.19 R |
| baja | 8 | 50,0 % | -0.34 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 16 | 62,5 % | -0.27 R |
| sin tendencia | 16 | 56,2 % | +0.02 R |
| en contra | 15 | 46,7 % | -0.33 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 34 | 52,9 % | -0.25 R |
| en contra | 13 | 61,5 % | -0.06 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 33 | 54,5 % | -0.25 R |
| a favor | 14 | 57,1 % | -0.05 R |

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
**16 señales** del 28/10/2026 al 09/11/2026. Acierto (precio a favor al vencer): **37,5 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = -1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 10 | 40,0 % | -0.24 R |
| <52 % | 6 | 33,3 % | +0.13 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 7 | 42,9 % | -0.24 R |
| USD/CHF | 4 | 25,0 % | +0.53 R |
| GBP/JPY | 3 | 33,3 % | — |
| ETH/USDT | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 11 | 45,5 % | -0.24 R |
| 15m | 4 | 25,0 % | +0.53 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 8 | 37,5 % | +0.53 R |
| 2-5 días | 6 | 50,0 % | -0.03 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 8 | 50,0 % | -0.03 R |
| estocastico | 6 | 16,7 % | +0.13 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 4 | 50,0 % | +1.89 R |
| 00-04 h | 3 | 0,0 % | -1.07 R |
| 16-20 h | 3 | 33,3 % | -1.02 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 08-12 h | 2 | 50,0 % | -1.06 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 7 | 57,1 % | -1.12 R |
| débil (20-25) | 6 | 16,7 % | -0.08 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 11 | 27,3 % | +0.22 R |
| alta | 3 | 33,3 % | -1.12 R |
| baja | 2 | 100,0 % | -1.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 13 | 38,5 % | -0.25 R |
| a favor | 3 | 33,3 % | +1.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 15 | 33,3 % | -0.07 R |
| en contra | 1 | 100,0 % | — |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 12 | 33,3 % | +0.05 R |
| a favor | 4 | 50,0 % | -1.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 30/10 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -0.54 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 06/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -0.09 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
| 06/11 17:00 | GBP/JPY | 4h | COMPRAR | 720 min | bollinger | -0.04 % |
| 05/11 22:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.03 % |
| 06/11 21:00 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.00 % |
