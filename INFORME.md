# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**720 señales** del 16/09/2025 al 06/11/2026. Acierto (precio a favor al vencer): **51,5 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| confianza_tramo = **<52 %** | falla | 43,0 % en 214 | después 55,1 % en 178 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 392 | 48,5 % | -0.18 R |
| 52-55 % | 279 | 55,2 % | -0.16 R |
| 55-58 % | 44 | 56,8 % | -0.24 R |
| ≥58 % | 5 | 40,0 % | -0.31 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 165 | 49,1 % | -0.18 R |
| USD/JPY | 120 | 51,7 % | -0.21 R |
| USD/CHF | 109 | 61,5 % | +0.04 R |
| Oro (XAU/USD) | 106 | 44,3 % | -0.14 R |
| EUR/GBP | 82 | 51,2 % | -0.33 R |
| BTC/USDT | 39 | 53,8 % | -0.33 R |
| GBP/JPY | 31 | 54,8 % | -0.25 R |
| SOL/USDT | 27 | 37,0 % | -0.48 R |
| ETH/USDT | 24 | 50,0 % | -0.37 R |
| XRP/USDT | 15 | 66,7 % | +0.42 R |
| USD/CAD | 2 | 100,0 % | +0.85 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 256 | 52,3 % | -0.17 R |
| 1h | 229 | 48,0 % | -0.20 R |
| 15m | 206 | 53,9 % | -0.17 R |
| 4h | 29 | 55,2 % | -0.11 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 375 | 52,8 % | -0.21 R |
| 2-4 h | 243 | 48,6 % | -0.19 R |
| 30-59 min | 102 | 53,9 % | -0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 343 | 50,1 % | -0.26 R |
| velas | 90 | 44,4 % | -0.15 R |
| barrida | 76 | 64,5 % | +0.02 R |
| soportes | 75 | 48,0 % | -0.31 R |
| bos | 50 | 50,0 % | -0.09 R |
| rsi | 50 | 58,0 % | -0.05 R |
| estocastico | 35 | 60,0 % | +0.22 R |
| fibonacci | 9 | 33,3 % | -0.11 R |
| divergencia | 1 | 0,0 % | -1.12 R |
| macd | 1 | 0,0 % | -0.81 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 150 | 50,0 % | -0.19 R |
| 12-16 h | 145 | 51,7 % | -0.33 R |
| 08-12 h | 117 | 49,6 % | -0.11 R |
| 20-24 h | 110 | 52,7 % | -0.19 R |
| 00-04 h | 104 | 54,8 % | -0.21 R |
| 04-08 h | 94 | 51,1 % | +0.06 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 374 | 53,5 % | -0.12 R |
| lateral (<20) | 224 | 48,2 % | -0.27 R |
| débil (20-25) | 122 | 51,6 % | -0.18 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 377 | 48,5 % | -0.13 R |
| alta | 245 | 55,1 % | -0.17 R |
| baja | 98 | 54,1 % | -0.36 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 270 | 48,9 % | -0.24 R |
| a favor | 255 | 55,7 % | -0.14 R |
| en contra | 195 | 49,7 % | -0.14 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 530 | 52,5 % | -0.17 R |
| en contra | 183 | 48,1 % | -0.18 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 510 | 52,4 % | -0.21 R |
| a favor | 210 | 49,5 % | -0.08 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 15/10 06:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -1.23 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 02/10 16:30 | Oro (XAU/USD) | 5m | COMPRAR | 100 min | velas | -0.99 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**816 señales** del 08/01/2021 al 06/11/2026. Acierto (precio a favor al vencer): **52,8 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 67,8 % en 59 | después 55,2 % en 87 casos | ❔ no se repite |
| mercado = **ETH/USDT** | falla | 33,3 % en 45 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 435 | 52,4 % | -0.07 R |
| 52-55 % | 345 | 54,2 % | -0.13 R |
| 55-58 % | 36 | 44,4 % | -0.06 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 146 | 60,3 % | -0.05 R |
| USD/CHF | 136 | 51,5 % | -0.25 R |
| SOL/USDT | 124 | 56,5 % | +0.06 R |
| Oro (XAU/USD) | 116 | 52,6 % | +0.08 R |
| GBP/USD | 89 | 52,8 % | -0.16 R |
| ETH/USDT | 68 | 35,3 % | -0.27 R |
| EUR/GBP | 48 | 50,0 % | -0.31 R |
| AUD/USD | 39 | 53,8 % | +0.37 R |
| EUR/JPY | 23 | 69,6 % | -0.19 R |
| USD/JPY | 19 | 36,8 % | -0.55 R |
| XRP/USDT | 7 | 28,6 % | -0.69 R |
| EUR/USD | 1 | 100,0 % | -1.04 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 354 | 54,5 % | -0.17 R |
| 4h | 294 | 51,7 % | -0.12 R |
| 1d | 138 | 52,9 % | +0.13 R |
| 15m | 30 | 43,3 % | +0.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 281 | 50,9 % | -0.20 R |
| 2-5 días | 269 | 52,4 % | -0.05 R |
| 4-12 h | 197 | 54,8 % | -0.09 R |
| 1-2 días | 69 | 56,5 % | +0.17 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 306 | 50,0 % | -0.15 R |
| bollinger | 302 | 55,3 % | -0.03 R |
| barrida | 102 | 51,0 % | -0.20 R |
| estocastico | 52 | 57,7 % | -0.03 R |
| choch | 23 | 69,6 % | -0.19 R |
| ruptura | 15 | 53,3 % | +0.55 R |
| fibonacci | 6 | 66,7 % | +0.22 R |
| bos | 4 | 25,0 % | -0.84 R |
| rsi | 4 | 50,0 % | +0.09 R |
| order_block | 3 | 0,0 % | -0.35 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 219 | 53,9 % | +0.10 R |
| 08-12 h | 135 | 50,4 % | -0.43 R |
| 12-16 h | 128 | 53,9 % | +0.02 R |
| 00-04 h | 125 | 56,0 % | +0.02 R |
| 16-20 h | 117 | 44,4 % | -0.26 R |
| 20-24 h | 92 | 58,7 % | -0.17 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 347 | 53,9 % | -0.02 R |
| lateral (<20) | 305 | 52,5 % | -0.16 R |
| débil (20-25) | 164 | 51,2 % | -0.14 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 451 | 50,8 % | -0.10 R |
| baja | 190 | 54,2 % | -0.15 R |
| alta | 175 | 56,6 % | -0.02 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 309 | 55,3 % | -0.08 R |
| a favor | 285 | 49,5 % | -0.11 R |
| en contra | 222 | 53,6 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 595 | 53,1 % | -0.09 R |
| en contra | 217 | 51,2 % | -0.11 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 528 | 51,7 % | -0.10 R |
| a favor | 288 | 54,9 % | -0.09 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 20/07 18:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -9.85 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 2400 min | bollinger | -8.81 % |
| 21/04 18:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -8.22 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**31 señales** del 28/10/2026 al 06/11/2026. Acierto (precio a favor al vencer): **54,8 %** · resultado medio con SL/TP tras costes: **-0.48 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 21 | 57,1 % | -0.55 R |
| 52-55 % | 9 | 44,4 % | -0.22 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 11 | 45,5 % | -0.93 R |
| USD/JPY | 10 | 60,0 % | -0.39 R |
| EUR/GBP | 3 | 33,3 % | -0.37 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| USD/CHF | 2 | 100,0 % | +0.34 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 17 | 52,9 % | -0.61 R |
| 15m | 14 | 57,1 % | -0.32 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 20 | 45,0 % | -0.48 R |
| 30-59 min | 8 | 62,5 % | -0.86 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 10 | 30,0 % | -0.66 R |
| soportes | 10 | 60,0 % | -0.39 R |
| estocastico | 6 | 66,7 % | -0.74 R |
| barrida | 3 | 66,7 % | -0.15 R |
| rsi | 3 | 100,0 % | -0.43 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 9 | 22,2 % | -0.49 R |
| 00-04 h | 8 | 87,5 % | -0.36 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 4 | 50,0 % | +0.20 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 08-12 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 17 | 64,7 % | -0.08 R |
| lateral (<20) | 8 | 50,0 % | -1.18 R |
| débil (20-25) | 6 | 33,3 % | -0.68 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 15 | 46,7 % | -0.40 R |
| alta | 12 | 66,7 % | -0.30 R |
| baja | 4 | 50,0 % | -1.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 14 | 64,3 % | -0.42 R |
| en contra | 9 | 44,4 % | -0.31 R |
| sin tendencia | 8 | 50,0 % | -0.97 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 23 | 56,5 % | -0.44 R |
| en contra | 8 | 50,0 % | -0.60 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 22 | 54,5 % | -0.41 R |
| a favor | 9 | 55,6 % | -0.66 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 05/11 15:50 | EUR/JPY | 5m | COMPRAR | 75 min | bollinger | -0.16 % |
| 05/11 21:45 | USD/JPY | 5m | COMPRAR | 100 min | soportes | -0.12 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |
| 05/11 23:00 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.11 % |
| 05/11 21:15 | USD/JPY | 5m | COMPRAR | 100 min | soportes | -0.11 % |
| 05/11 23:15 | EUR/JPY | 5m | COMPRAR | 50 min | estocastico | -0.08 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**10 señales** del 28/10/2026 al 05/11/2026. Acierto (precio a favor al vencer): **30,0 %** · resultado medio con SL/TP tras costes: **+0.21 R** · no se distingue del azar todavía (z = -1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 7 | 42,9 % | +0.29 R |
| <52 % | 3 | 0,0 % | +0.10 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 5 | 40,0 % | +0.96 R |
| GBP/JPY | 2 | 50,0 % | — |
| USD/CHF | 2 | 0,0 % | +0.10 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 7 | 42,9 % | +0.96 R |
| 15m | 2 | 0,0 % | +0.10 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 4 | 25,0 % | +0.10 R |
| 2-5 días | 4 | 50,0 % | +0.96 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 6 | 50,0 % | +0.96 R |
| estocastico | 3 | 0,0 % | -0.29 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 20-24 h | 2 | 50,0 % | +2.14 R |
| 08-12 h | 1 | 0,0 % | — |
| 16-20 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 5 | 20,0 % | -0.26 R |
| lateral (<20) | 3 | 33,3 % | +2.96 R |
| fuerte (≥25) | 2 | 50,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 8 | 25,0 % | +1.07 R |
| baja | 1 | 100,0 % | -1.04 R |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 7 | 28,6 % | -0.07 R |
| a favor | 3 | 33,3 % | +1.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 10 | 30,0 % | +0.21 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 9 | 33,3 % | +0.21 R |
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
| 05/11 22:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.03 % |
