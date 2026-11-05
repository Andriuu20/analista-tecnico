# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**785 señales** del 15/09/2025 al 04/11/2026. Acierto (precio a favor al vencer): **48,5 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = -0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | falla | 22,0 % en 41 | después 48,4 % en 95 casos | ❔ no se repite |
| temporalidad = **1h** | falla | 41,0 % en 173 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **5m** | falla | 32,6 % en 43 | después 51,1 % en 264 casos | ❔ no se repite |
| plazo = **2-4 h** | falla | 41,7 % en 199 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **lun** | falla | 34,5 % en 84 | después 57,7 % en 71 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | falla | 39,6 % en 134 | después 51,6 % en 122 casos | ❔ no se repite |
| volatilidad = **normal** | falla | 41,7 % en 230 | después 54,5 % en 200 casos | ❔ no se repite |
| zona_txt = **a favor (barato al comprar / caro al vender)** | falla | 43,3 % en 289 | después 52,1 % en 292 casos | ❔ no se repite |
| estructura_txt = **en contra** | falla | 42,9 % en 275 | después 52,3 % en 281 casos | ❔ no se repite |
| confianza_tramo = **<52 %** | falla | 40,6 % en 234 | después 50,3 % en 197 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 431 | 45,0 % | -0.24 R |
| 52-55 % | 306 | 55,2 % | -0.05 R |
| 55-58 % | 47 | 38,3 % | -0.52 R |
| ≥58 % | 1 | 0,0 % | -1.17 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 200 | 51,0 % | -0.08 R |
| Oro (XAU/USD) | 137 | 46,7 % | -0.12 R |
| USD/JPY | 136 | 40,4 % | -0.42 R |
| USD/CHF | 133 | 57,1 % | -0.00 R |
| EUR/GBP | 83 | 45,8 % | -0.34 R |
| GBP/JPY | 24 | 54,2 % | -0.21 R |
| SOL/USDT | 22 | 31,8 % | -0.49 R |
| BTC/USDT | 21 | 52,4 % | +0.08 R |
| GBP/USD | 12 | 50,0 % | -0.29 R |
| ETH/USDT | 9 | 66,7 % | -0.06 R |
| XRP/USDT | 6 | 33,3 % | -1.21 R |
| AUD/USD | 1 | 0,0 % | -1.07 R |
| EUR/USD | 1 | 100,0 % | +0.92 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 307 | 48,5 % | -0.26 R |
| 15m | 284 | 53,5 % | -0.06 R |
| 1h | 184 | 41,3 % | -0.19 R |
| 4h | 10 | 40,0 % | -1.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 378 | 49,5 % | -0.25 R |
| 2-4 h | 221 | 43,4 % | -0.22 R |
| 30-59 min | 186 | 52,7 % | -0.00 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 323 | 48,9 % | -0.16 R |
| soportes | 135 | 43,7 % | -0.45 R |
| estocastico | 98 | 43,9 % | -0.21 R |
| velas | 90 | 48,9 % | +0.04 R |
| barrida | 60 | 63,3 % | +0.04 R |
| bos | 42 | 47,6 % | -0.10 R |
| rsi | 39 | 59,0 % | -0.03 R |
| macd | 13 | 30,8 % | -0.22 R |
| fibonacci | 5 | 40,0 % | -1.08 R |
| divergencia | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 157 | 48,4 % | -0.15 R |
| 12-16 h | 154 | 50,0 % | -0.22 R |
| 08-12 h | 145 | 51,0 % | -0.21 R |
| 00-04 h | 118 | 43,2 % | -0.33 R |
| 04-08 h | 109 | 43,1 % | -0.01 R |
| 20-24 h | 102 | 54,9 % | -0.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 380 | 50,8 % | -0.15 R |
| lateral (<20) | 256 | 45,3 % | -0.25 R |
| débil (20-25) | 149 | 48,3 % | -0.16 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 430 | 47,7 % | -0.10 R |
| alta | 241 | 51,0 % | -0.27 R |
| baja | 114 | 46,5 % | -0.31 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 328 | 47,9 % | -0.10 R |
| a favor | 281 | 50,9 % | -0.21 R |
| en contra | 176 | 46,0 % | -0.30 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 581 | 47,7 % | -0.17 R |
| en contra | 202 | 50,5 % | -0.22 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 556 | 47,7 % | -0.20 R |
| a favor | 229 | 50,7 % | -0.15 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 04/08 22:00 | Oro (XAU/USD) | 4h | VENDER | 240 min | soportes | -1.40 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 27/10 12:30 | Oro (XAU/USD) | 15m | VENDER | 225 min | fibonacci | -1.24 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**788 señales** del 08/01/2021 al 03/11/2026. Acierto (precio a favor al vencer): **52,4 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = 1.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 65,6 % en 61 | después 53,4 % en 103 casos | ❔ no se repite |
| temporalidad = **1h** | acierta | 61,2 % en 134 | después 50,9 % en 220 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 65,9 % en 44 | después 54,0 % en 50 casos | ❔ no se repite |
| estructura_txt = **a favor** | acierta | 59,8 % en 132 | después 50,8 % en 124 casos | ❔ no se repite |
| confianza_tramo = **52-55 %** | acierta | 58,5 % en 171 | después 51,1 % en 141 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 429 | 50,3 % | -0.02 R |
| 52-55 % | 312 | 55,1 % | -0.15 R |
| 55-58 % | 47 | 53,2 % | +0.07 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 164 | 57,9 % | -0.11 R |
| USD/CHF | 116 | 56,0 % | -0.13 R |
| Oro (XAU/USD) | 115 | 51,3 % | +0.09 R |
| SOL/USDT | 113 | 52,2 % | -0.02 R |
| GBP/USD | 86 | 53,5 % | -0.14 R |
| ETH/USDT | 67 | 40,3 % | -0.21 R |
| EUR/GBP | 49 | 55,1 % | -0.07 R |
| AUD/USD | 39 | 53,8 % | +0.37 R |
| USD/JPY | 31 | 35,5 % | -0.29 R |
| XRP/USDT | 8 | 37,5 % | -0.38 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 354 | 54,8 % | -0.14 R |
| 4h | 280 | 49,6 % | -0.11 R |
| 1d | 138 | 52,2 % | +0.12 R |
| 15m | 16 | 50,0 % | +0.61 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 249 | 53,0 % | +0.01 R |
| 12-24 h | 247 | 51,0 % | -0.16 R |
| 4-12 h | 215 | 54,0 % | -0.08 R |
| 1-2 días | 77 | 50,6 % | +0.03 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 309 | 54,7 % | -0.08 R |
| soportes | 298 | 52,0 % | -0.07 R |
| barrida | 97 | 52,6 % | -0.14 R |
| estocastico | 53 | 54,7 % | +0.17 R |
| ruptura | 15 | 53,3 % | +0.55 R |
| order_block | 14 | 28,6 % | -0.05 R |
| fibonacci | 6 | 50,0 % | +0.22 R |
| bos | 3 | 0,0 % | -0.77 R |
| supertrend | 1 | 0,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 210 | 53,8 % | +0.12 R |
| 08-12 h | 132 | 52,3 % | -0.32 R |
| 12-16 h | 125 | 48,8 % | +0.01 R |
| 00-04 h | 121 | 52,9 % | -0.03 R |
| 16-20 h | 106 | 47,2 % | -0.24 R |
| 20-24 h | 94 | 59,6 % | -0.08 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 332 | 51,5 % | -0.07 R |
| lateral (<20) | 285 | 53,3 % | -0.09 R |
| débil (20-25) | 171 | 52,6 % | -0.03 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 430 | 51,2 % | -0.08 R |
| alta | 184 | 53,8 % | -0.06 R |
| baja | 174 | 54,0 % | -0.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 295 | 54,2 % | -0.10 R |
| a favor | 268 | 51,1 % | -0.05 R |
| en contra | 225 | 51,6 % | -0.05 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 584 | 53,3 % | -0.09 R |
| en contra | 200 | 49,0 % | -0.01 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 532 | 50,9 % | -0.12 R |
| a favor | 256 | 55,5 % | +0.04 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 2400 min | bollinger | -8.81 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**17 señales** del 28/10/2026 al 04/11/2026. Acierto (precio a favor al vencer): **58,8 %** · resultado medio con SL/TP tras costes: **-0.39 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 10 | 70,0 % | -0.29 R |
| 52-55 % | 6 | 33,3 % | -0.41 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 5 | 60,0 % | -0.37 R |
| EUR/JPY | 4 | 50,0 % | -0.63 R |
| EUR/GBP | 3 | 33,3 % | -0.37 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 9 | 66,7 % | -0.49 R |
| 15m | 8 | 50,0 % | -0.28 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 9 | 44,4 % | -0.47 R |
| 30-59 min | 5 | 60,0 % | -0.72 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 5 | 40,0 % | -0.25 R |
| soportes | 5 | 60,0 % | -0.37 R |
| estocastico | 3 | 66,7 % | -0.43 R |
| rsi | 3 | 100,0 % | -0.43 R |
| barrida | 2 | 50,0 % | -1.16 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 6 | 83,3 % | -0.36 R |
| 16-20 h | 4 | 50,0 % | +0.20 R |
| 12-16 h | 3 | 33,3 % | -1.21 R |
| 20-24 h | 3 | 33,3 % | -0.15 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 9 | 77,8 % | +0.32 R |
| lateral (<20) | 4 | 50,0 % | -1.19 R |
| débil (20-25) | 4 | 25,0 % | -1.19 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| alta | 8 | 75,0 % | -0.08 R |
| normal | 6 | 50,0 % | -0.39 R |
| baja | 3 | 33,3 % | -1.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 10 | 60,0 % | -0.41 R |
| en contra | 5 | 60,0 % | -0.21 R |
| sin tendencia | 2 | 50,0 % | -0.69 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 14 | 64,3 % | -0.29 R |
| en contra | 3 | 33,3 % | -0.85 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 13 | 61,5 % | -0.23 R |
| a favor | 4 | 50,0 % | -0.91 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |
| 02/11 19:05 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.07 % |
| 04/11 02:45 | EUR/GBP | 15m | VENDER | 75 min | bollinger | -0.04 % |
| 03/11 17:15 | EUR/GBP | 15m | VENDER | 75 min | bollinger | -0.01 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**9 señales** del 28/10/2026 al 04/11/2026. Acierto (precio a favor al vencer): **33,3 %** · resultado medio con SL/TP tras costes: **-1.09 R** · no se distingue del azar todavía (z = -1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 7 | 42,9 % | -1.06 R |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 5 | 40,0 % | — |
| GBP/JPY | 2 | 50,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 7 | 42,9 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 4 | 50,0 % | — |
| 4-12 h | 3 | 33,3 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 6 | 50,0 % | — |
| estocastico | 2 | 0,0 % | -1.09 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 3 | 66,7 % | -1.06 R |
| 08-12 h | 1 | 0,0 % | — |
| 16-20 h | 1 | 0,0 % | — |
| 20-24 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 4 | 25,0 % | -1.06 R |
| lateral (<20) | 3 | 33,3 % | — |
| fuerte (≥25) | 2 | 50,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 7 | 28,6 % | -1.06 R |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 7 | 28,6 % | -1.09 R |
| a favor | 2 | 50,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 9 | 33,3 % | -1.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 8 | 37,5 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 30/10 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -0.54 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
