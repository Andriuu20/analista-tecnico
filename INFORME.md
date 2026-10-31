# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**652 señales** del 15/09/2025 al 30/10/2026. Acierto (precio a favor al vencer): **50,6 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = 0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| confianza_tramo = **<52 %** | falla | 41,2 % en 160 | después 52,1 % en 165 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 325 | 46,8 % | -0.23 R |
| 52-55 % | 240 | 55,8 % | -0.12 R |
| 55-58 % | 84 | 51,2 % | -0.27 R |
| ≥58 % | 3 | 33,3 % | +0.25 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 174 | 53,4 % | -0.17 R |
| Oro (XAU/USD) | 155 | 51,0 % | -0.16 R |
| EUR/GBP | 90 | 42,2 % | -0.34 R |
| USD/CHF | 69 | 58,0 % | -0.13 R |
| USD/JPY | 52 | 51,9 % | -0.32 R |
| BTC/USDT | 29 | 58,6 % | -0.10 R |
| SOL/USDT | 29 | 37,9 % | -0.01 R |
| USD/CAD | 28 | 50,0 % | -0.37 R |
| GBP/JPY | 19 | 42,1 % | -0.16 R |
| XRP/USDT | 4 | 50,0 % | +0.79 R |
| ETH/USDT | 1 | 0,0 % | -1.13 R |
| EUR/USD | 1 | 100,0 % | +0.92 R |
| GBP/USD | 1 | 0,0 % | -1.19 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 247 | 52,2 % | -0.18 R |
| 5m | 238 | 55,0 % | -0.21 R |
| 1h | 167 | 41,9 % | -0.19 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 30-59 min | 233 | 55,8 % | -0.03 R |
| 1-2 h | 221 | 51,6 % | -0.27 R |
| 2-4 h | 198 | 43,4 % | -0.29 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 249 | 47,0 % | -0.26 R |
| velas | 153 | 51,0 % | -0.18 R |
| estocastico | 119 | 55,5 % | -0.07 R |
| soportes | 47 | 55,3 % | -0.28 R |
| barrida | 43 | 58,1 % | -0.01 R |
| bos | 36 | 44,4 % | -0.28 R |
| rsi | 22 | 50,0 % | -0.14 R |
| order_block | 1 | 0,0 % | -1.13 R |
| macd | 1 | 100,0 % | +1.81 R |
| divergencia | 1 | 0,0 % | -1.15 R |
| supertrend | 1 | 0,0 % | -1.16 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 138 | 52,9 % | -0.35 R |
| 16-20 h | 136 | 52,9 % | -0.14 R |
| 08-12 h | 127 | 45,7 % | -0.24 R |
| 00-04 h | 87 | 46,0 % | -0.08 R |
| 20-24 h | 83 | 65,1 % | -0.20 R |
| 04-08 h | 81 | 40,7 % | -0.04 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 296 | 53,0 % | -0.14 R |
| lateral (<20) | 225 | 48,0 % | -0.25 R |
| débil (20-25) | 131 | 49,6 % | -0.19 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 376 | 49,5 % | -0.16 R |
| alta | 194 | 53,6 % | -0.17 R |
| baja | 82 | 48,8 % | -0.40 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 272 | 50,7 % | -0.09 R |
| a favor | 258 | 51,2 % | -0.23 R |
| en contra | 122 | 49,2 % | -0.33 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 460 | 51,5 % | -0.11 R |
| en contra | 189 | 48,1 % | -0.40 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 426 | 51,2 % | -0.15 R |
| a favor | 226 | 49,6 % | -0.27 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 27/10 12:30 | Oro (XAU/USD) | 15m | VENDER | 225 min | velas | -1.24 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 14/10 22:00 | Oro (XAU/USD) | 15m | VENDER | 225 min | velas | -0.96 % |
| 18/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.96 % |
| 27/08 19:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -0.79 % |
| 08/05 15:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.75 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**796 señales** del 08/01/2021 al 30/10/2026. Acierto (precio a favor al vencer): **51,1 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 0.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 67,3 % en 49 | después 50,0 % en 84 casos | ❔ no se repite |
| mercado = **ETH/USDT** | falla | 32,6 % en 46 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **1h** | acierta | 58,6 % en 145 | después 50,0 % en 234 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 66,7 % en 45 | después 64,4 % en 45 casos | ✅ confirmado |
| volatilidad = **alta** | acierta | 62,9 % en 89 | después 48,9 % en 88 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 436 | 48,6 % | -0.10 R |
| 52-55 % | 325 | 54,5 % | -0.13 R |
| 55-58 % | 35 | 51,4 % | +0.16 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 175 | 53,1 % | -0.15 R |
| GBP/JPY | 133 | 56,4 % | -0.18 R |
| Oro (XAU/USD) | 117 | 50,4 % | +0.06 R |
| GBP/USD | 100 | 51,0 % | -0.19 R |
| SOL/USDT | 94 | 56,4 % | +0.06 R |
| ETH/USDT | 51 | 33,3 % | -0.27 R |
| AUD/USD | 45 | 51,1 % | +0.24 R |
| EUR/GBP | 43 | 39,5 % | -0.41 R |
| XRP/USDT | 17 | 52,9 % | +0.27 R |
| USD/JPY | 13 | 30,8 % | -0.75 R |
| EUR/JPY | 5 | 80,0 % | -0.45 R |
| EUR/USD | 2 | 100,0 % | +2.50 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 379 | 53,3 % | -0.16 R |
| 4h | 231 | 48,9 % | -0.12 R |
| 1d | 140 | 51,4 % | +0.10 R |
| 15m | 46 | 43,5 % | -0.16 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 292 | 53,1 % | -0.15 R |
| 2-5 días | 231 | 50,2 % | +0.01 R |
| 4-12 h | 212 | 49,1 % | -0.21 R |
| 1-2 días | 61 | 52,5 % | +0.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 322 | 50,9 % | -0.13 R |
| bollinger | 239 | 53,1 % | -0.06 R |
| barrida | 100 | 49,0 % | -0.23 R |
| estocastico | 62 | 54,8 % | +0.27 R |
| ruptura | 21 | 47,6 % | +0.22 R |
| order_block | 16 | 31,2 % | -0.48 R |
| macd | 13 | 46,2 % | -0.26 R |
| fibonacci | 9 | 66,7 % | +0.60 R |
| rsi | 9 | 33,3 % | -0.60 R |
| velas | 4 | 25,0 % | -0.78 R |
| choch | 3 | 100,0 % | -0.69 R |
| bos | 1 | 0,0 % | -1.05 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 218 | 50,0 % | +0.03 R |
| 08-12 h | 133 | 42,9 % | -0.35 R |
| 00-04 h | 124 | 50,8 % | -0.16 R |
| 12-16 h | 117 | 51,3 % | +0.00 R |
| 16-20 h | 114 | 51,8 % | -0.23 R |
| 20-24 h | 90 | 65,6 % | +0.04 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 341 | 51,3 % | -0.07 R |
| lateral (<20) | 292 | 50,3 % | -0.14 R |
| débil (20-25) | 163 | 52,1 % | -0.10 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 441 | 49,0 % | -0.13 R |
| baja | 178 | 51,7 % | -0.09 R |
| alta | 177 | 55,9 % | -0.05 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 299 | 52,2 % | -0.07 R |
| a favor | 283 | 49,1 % | -0.13 R |
| en contra | 214 | 52,3 % | -0.12 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 572 | 51,9 % | -0.11 R |
| en contra | 221 | 48,4 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 517 | 51,1 % | -0.13 R |
| a favor | 279 | 51,3 % | -0.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 18/09 13:00 | SOL/USDT | 1h | VENDER | 600 min | estocastico | -7.05 % |
| 16/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -7.01 % |
| 14/12 09:00 | SOL/USDT | 4h | COMPRAR | 4800 min | barrida | -6.91 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**8 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **62,5 %** · resultado medio con SL/TP tras costes: **-1.04 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 5 | 80,0 % | -0.91 R |
| 52-55 % | 3 | 33,3 % | -1.21 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 3 | 33,3 % | -1.20 R |
| USD/JPY | 2 | 100,0 % | -0.63 R |
| EUR/GBP | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | — |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 4 | 50,0 % | -1.22 R |
| 5m | 4 | 75,0 % | -0.90 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 4 | 75,0 % | -0.93 R |
| 30-59 min | 3 | 33,3 % | -1.18 R |
| 2-4 h | 1 | 100,0 % | -1.22 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| barrida | 2 | 50,0 % | -1.21 R |
| bollinger | 2 | 50,0 % | -1.23 R |
| estocastico | 2 | 50,0 % | -1.18 R |
| soportes | 2 | 100,0 % | -0.63 R |
| macd | 1 | 0,0 % | -1.20 R |
| rsi | 1 | 100,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 3 | 33,3 % | -1.21 R |
| 00-04 h | 2 | 100,0 % | -0.68 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 16-20 h | 1 | 100,0 % | -1.15 R |
| 20-24 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 3 | 33,3 % | -1.19 R |
| fuerte (≥25) | 3 | 66,7 % | -0.83 R |
| lateral (<20) | 2 | 100,0 % | -1.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 3 | 33,3 % | -1.17 R |
| alta | 3 | 100,0 % | -0.84 R |
| baja | 2 | 50,0 % | -1.22 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 5 | 60,0 % | -1.20 R |
| en contra | 2 | 50,0 % | -1.18 R |
| sin tendencia | 1 | 100,0 % | -0.13 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 7 | 57,1 % | -1.19 R |
| en contra | 1 | 100,0 % | -0.13 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 5 | 60,0 % | -1.19 R |
| a favor | 3 | 66,7 % | -0.67 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**5 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **20,0 %** · resultado medio con SL/TP tras costes: **-1.12 R** · no se distingue del azar todavía (z = -1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 3 | 33,3 % | — |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 2 | 50,0 % | — |
| GBP/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | — |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 3 | 33,3 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | — |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 2 | 0,0 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | — |
| 2-5 días | 1 | 100,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 2 | 50,0 % | — |
| estocastico | 2 | 0,0 % | -1.12 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 2 | 0,0 % | -1.12 R |
| 12-16 h | 2 | 50,0 % | — |
| 08-12 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 3 | 33,3 % | — |
| lateral (<20) | 1 | 0,0 % | — |
| fuerte (≥25) | 1 | 0,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 3 | 0,0 % | — |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 4 | 25,0 % | -1.12 R |
| a favor | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 5 | 20,0 % | -1.12 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 4 | 25,0 % | -1.12 R |
| a favor | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 30/10 01:00 | GBP/JPY | 4h | VENDER | 720 min | bollinger | -0.06 % |
