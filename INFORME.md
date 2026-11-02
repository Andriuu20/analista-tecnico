# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**686 señales** del 16/09/2025 al 02/11/2026. Acierto (precio a favor al vencer): **48,1 %** · resultado medio con SL/TP tras costes: **-0.21 R** · no se distingue del azar todavía (z = -1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **EUR/GBP** | falla | 35,4 % en 48 | después 47,1 % en 34 casos | ❔ no se repite |
| temporalidad = **1h** | falla | 38,7 % en 155 | pocos casos en la segunda mitad | ⏳ faltan datos |
| plazo = **2-4 h** | falla | 38,7 % en 155 | después 56,4 % en 55 casos | ❔ no se repite |
| franja = **04-08 h** | falla | 35,8 % en 53 | después 47,1 % en 34 casos | ❔ no se repite |
| dia = **lun** | falla | 31,7 % en 60 | después 54,1 % en 61 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | falla | 37,0 % en 108 | después 46,9 % en 113 casos | ❔ no se repite |
| zona_txt = **a favor (barato al comprar / caro al vender)** | falla | 42,7 % en 262 | después 51,2 % en 260 casos | ❔ no se repite |
| confianza_tramo = **<52 %** | falla | 41,2 % en 177 | después 54,8 % en 177 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 354 | 48,0 % | -0.26 R |
| 52-55 % | 270 | 49,6 % | -0.12 R |
| 55-58 % | 58 | 41,4 % | -0.49 R |
| ≥58 % | 4 | 50,0 % | +1.35 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 190 | 52,1 % | -0.13 R |
| Oro (XAU/USD) | 131 | 48,9 % | -0.13 R |
| USD/JPY | 86 | 44,2 % | -0.49 R |
| EUR/GBP | 82 | 40,2 % | -0.33 R |
| USD/CHF | 79 | 55,7 % | -0.21 R |
| SOL/USDT | 38 | 31,6 % | -0.28 R |
| BTC/USDT | 34 | 58,8 % | +0.07 R |
| GBP/USD | 17 | 41,2 % | -0.27 R |
| GBP/JPY | 15 | 46,7 % | -0.15 R |
| USD/CAD | 5 | 40,0 % | -0.39 R |
| ETH/USDT | 4 | 25,0 % | -0.64 R |
| XRP/USDT | 4 | 50,0 % | +0.11 R |
| EUR/USD | 1 | 100,0 % | +0.92 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 277 | 50,5 % | -0.28 R |
| 15m | 237 | 51,5 % | -0.12 R |
| 1h | 172 | 39,5 % | -0.23 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 250 | 48,4 % | -0.36 R |
| 30-59 min | 226 | 52,2 % | -0.02 R |
| 2-4 h | 210 | 43,3 % | -0.25 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 284 | 45,8 % | -0.26 R |
| estocastico | 169 | 49,1 % | -0.10 R |
| velas | 108 | 50,0 % | -0.12 R |
| soportes | 56 | 48,2 % | -0.60 R |
| barrida | 41 | 53,7 % | -0.12 R |
| bos | 23 | 43,5 % | -0.19 R |
| rsi | 19 | 52,6 % | -0.15 R |
| fibonacci | 5 | 40,0 % | -0.31 R |
| supertrend | 2 | 100,0 % | +1.46 R |
| macd | 1 | 100,0 % | +1.81 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 151 | 51,0 % | -0.17 R |
| 12-16 h | 142 | 52,1 % | -0.27 R |
| 08-12 h | 137 | 42,3 % | -0.25 R |
| 00-04 h | 91 | 42,9 % | -0.16 R |
| 04-08 h | 87 | 40,2 % | -0.09 R |
| 20-24 h | 78 | 60,3 % | -0.30 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 323 | 52,3 % | -0.13 R |
| lateral (<20) | 221 | 42,1 % | -0.36 R |
| débil (20-25) | 142 | 47,9 % | -0.17 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 386 | 47,4 % | -0.15 R |
| alta | 220 | 49,5 % | -0.27 R |
| baja | 80 | 47,5 % | -0.34 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 301 | 49,5 % | -0.14 R |
| a favor | 239 | 47,7 % | -0.25 R |
| en contra | 146 | 45,9 % | -0.29 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 522 | 46,9 % | -0.17 R |
| en contra | 162 | 51,9 % | -0.34 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 484 | 47,9 % | -0.20 R |
| a favor | 202 | 48,5 % | -0.25 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 13/10 15:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -1.07 % |
| 25/08 04:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -0.96 % |
| 30/10 15:45 | Oro (XAU/USD) | 15m | COMPRAR | 225 min | velas | -0.90 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**812 señales** del 08/01/2021 al 02/11/2026. Acierto (precio a favor al vencer): **51,6 %** · resultado medio con SL/TP tras costes: **-0.06 R** · no se distingue del azar todavía (z = 0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | acierta | 58,4 % en 154 | después 50,6 % en 231 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 64,6 % en 48 | después 54,2 % en 48 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 435 | 49,9 % | -0.01 R |
| 52-55 % | 326 | 54,3 % | -0.15 R |
| 55-58 % | 51 | 49,0 % | +0.17 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 195 | 52,3 % | -0.05 R |
| GBP/JPY | 125 | 55,2 % | -0.15 R |
| Oro (XAU/USD) | 118 | 51,7 % | +0.06 R |
| SOL/USDT | 96 | 58,3 % | +0.12 R |
| GBP/USD | 90 | 54,4 % | -0.11 R |
| ETH/USDT | 52 | 34,6 % | -0.30 R |
| AUD/USD | 44 | 52,3 % | +0.27 R |
| EUR/GBP | 44 | 43,2 % | -0.31 R |
| USD/JPY | 32 | 50,0 % | +0.03 R |
| XRP/USDT | 10 | 30,0 % | -0.22 R |
| EUR/JPY | 4 | 75,0 % | -0.79 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |
| EUR/USD | 1 | 0,0 % | -1.03 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 385 | 53,8 % | -0.11 R |
| 4h | 244 | 49,2 % | -0.09 R |
| 1d | 141 | 52,5 % | +0.10 R |
| 15m | 42 | 42,9 % | +0.13 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 288 | 53,8 % | -0.05 R |
| 2-5 días | 235 | 50,6 % | -0.02 R |
| 4-12 h | 227 | 49,3 % | -0.14 R |
| 1-2 días | 62 | 53,2 % | +0.09 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 334 | 51,5 % | -0.05 R |
| bollinger | 247 | 53,8 % | -0.07 R |
| barrida | 98 | 52,0 % | -0.14 R |
| estocastico | 63 | 47,6 % | +0.19 R |
| order_block | 29 | 48,3 % | +0.01 R |
| ruptura | 20 | 50,0 % | +0.29 R |
| rsi | 7 | 28,6 % | -0.81 R |
| fibonacci | 6 | 50,0 % | +0.23 R |
| macd | 5 | 40,0 % | +0.01 R |
| choch | 3 | 100,0 % | -0.69 R |
| velas | 3 | 0,0 % | -0.69 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 219 | 48,9 % | +0.01 R |
| 00-04 h | 136 | 51,5 % | +0.00 R |
| 08-12 h | 134 | 48,5 % | -0.26 R |
| 12-16 h | 118 | 50,8 % | -0.03 R |
| 16-20 h | 109 | 55,0 % | -0.12 R |
| 20-24 h | 96 | 59,4 % | +0.04 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 332 | 50,0 % | -0.11 R |
| lateral (<20) | 316 | 51,3 % | -0.04 R |
| débil (20-25) | 164 | 55,5 % | +0.02 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 447 | 50,6 % | -0.04 R |
| baja | 186 | 53,8 % | -0.01 R |
| alta | 179 | 52,0 % | -0.14 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 296 | 53,4 % | -0.05 R |
| a favor | 277 | 49,8 % | -0.07 R |
| en contra | 239 | 51,5 % | -0.05 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 587 | 51,1 % | -0.10 R |
| en contra | 221 | 52,0 % | +0.05 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 525 | 49,0 % | -0.14 R |
| a favor | 287 | 56,4 % | +0.09 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 16/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -7.01 % |
| 18/05 14:00 | ETH/USDT | 4h | COMPRAR | 1200 min | soportes | -6.26 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |
| 14/10 22:00 | BTC/USDT | 4h | COMPRAR | 4800 min | fibonacci | -5.63 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**11 señales** del 28/10/2026 al 02/11/2026. Acierto (precio a favor al vencer): **63,6 %** · resultado medio con SL/TP tras costes: **-0.65 R** · no se distingue del azar todavía (z = 0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 8 | 75,0 % | -0.45 R |
| 52-55 % | 3 | 33,3 % | -1.21 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 3 | 33,3 % | -1.20 R |
| USD/JPY | 3 | 66,7 % | -0.84 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| EUR/GBP | 1 | 100,0 % | -1.22 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 6 | 66,7 % | -0.39 R |
| 5m | 5 | 60,0 % | -0.97 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 5 | 60,0 % | -0.99 R |
| 30-59 min | 3 | 33,3 % | -1.16 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 3 | 66,7 % | -0.84 R |
| bollinger | 2 | 50,0 % | -1.23 R |
| barrida | 2 | 50,0 % | -1.16 R |
| estocastico | 2 | 50,0 % | -1.18 R |
| velas | 2 | 100,0 % | +1.23 R |
| rsi | 1 | 100,0 % | -1.15 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 100,0 % | -0.27 R |
| 12-16 h | 3 | 33,3 % | -1.21 R |
| 20-24 h | 3 | 33,3 % | -0.15 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 16-20 h | 1 | 100,0 % | -1.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 5 | 80,0 % | -0.01 R |
| débil (20-25) | 4 | 25,0 % | -1.19 R |
| lateral (<20) | 2 | 100,0 % | -1.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 5 | 40,0 % | -0.83 R |
| alta | 4 | 100,0 % | -0.15 R |
| baja | 2 | 50,0 % | -1.22 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 5 | 60,0 % | -1.18 R |
| en contra | 4 | 75,0 % | +0.03 R |
| sin tendencia | 2 | 50,0 % | -0.69 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 9 | 66,7 % | -0.65 R |
| en contra | 2 | 50,0 % | -0.69 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 8 | 62,5 % | -0.59 R |
| a favor | 3 | 66,7 % | -0.82 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**8 señales** del 28/10/2026 al 30/10/2026. Acierto (precio a favor al vencer): **25,0 %** · resultado medio con SL/TP tras costes: **-1.09 R** · no se distingue del azar todavía (z = -1.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 6 | 33,3 % | -1.06 R |
| <52 % | 2 | 0,0 % | -1.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 5 | 40,0 % | — |
| GBP/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 0,0 % | -1.12 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 6 | 33,3 % | — |
| 15m | 1 | 0,0 % | -1.12 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 4 | 50,0 % | — |
| 4-12 h | 2 | 0,0 % | -1.12 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 5 | 40,0 % | — |
| estocastico | 2 | 0,0 % | -1.09 R |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.12 R |
| 12-16 h | 2 | 50,0 % | -1.06 R |
| 08-12 h | 1 | 0,0 % | — |
| 16-20 h | 1 | 0,0 % | — |
| 20-24 h | 1 | 100,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 4 | 25,0 % | -1.06 R |
| lateral (<20) | 3 | 33,3 % | — |
| fuerte (≥25) | 1 | 0,0 % | -1.12 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 6 | 16,7 % | -1.06 R |
| baja | 1 | 100,0 % | — |
| alta | 1 | 0,0 % | -1.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 7 | 28,6 % | -1.09 R |
| a favor | 1 | 0,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 8 | 25,0 % | -1.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 7 | 28,6 % | -1.09 R |
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
