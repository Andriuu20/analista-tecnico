# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**714 señales** del 18/03/2026 al 29/10/2026. Acierto (precio a favor al vencer): **52,0 %** · resultado medio con SL/TP tras costes: **-0.11 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **15m** | acierta | 57,8 % en 185 | después 47,1 % en 102 casos | ❔ no se repite |
| plazo = **30-59 min** | acierta | 58,3 % en 175 | después 51,9 % en 135 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 63,8 % en 58 | después 66,7 % en 42 casos | ✅ confirmado |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 359 | 50,7 % | -0.09 R |
| 52-55 % | 265 | 53,6 % | -0.12 R |
| 55-58 % | 84 | 52,4 % | -0.20 R |
| ≥58 % | 6 | 50,0 % | +0.86 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 167 | 49,7 % | -0.10 R |
| Oro (XAU/USD) | 163 | 54,0 % | -0.11 R |
| USD/CHF | 89 | 57,3 % | -0.17 R |
| ETH/USDT | 68 | 55,9 % | +0.19 R |
| EUR/GBP | 61 | 39,3 % | -0.41 R |
| USD/JPY | 53 | 54,7 % | -0.13 R |
| BTC/USDT | 44 | 56,8 % | -0.01 R |
| SOL/USDT | 34 | 47,1 % | -0.16 R |
| USD/CAD | 12 | 41,7 % | -0.47 R |
| GBP/JPY | 11 | 27,3 % | -0.61 R |
| EUR/USD | 5 | 100,0 % | +0.93 R |
| GBP/USD | 5 | 60,0 % | +1.05 R |
| XRP/USDT | 2 | 50,0 % | -0.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 287 | 54,0 % | -0.17 R |
| 5m | 271 | 53,5 % | -0.09 R |
| 1h | 156 | 45,5 % | -0.02 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 30-59 min | 310 | 55,5 % | -0.11 R |
| 1-2 h | 230 | 52,6 % | -0.12 R |
| 2-4 h | 174 | 44,8 % | -0.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 196 | 43,9 % | -0.26 R |
| estocastico | 143 | 54,5 % | -0.12 R |
| velas | 134 | 54,5 % | -0.16 R |
| soportes | 87 | 55,2 % | +0.17 R |
| barrida | 75 | 58,7 % | -0.15 R |
| bos | 46 | 50,0 % | -0.01 R |
| rsi | 27 | 51,9 % | -0.10 R |
| macd | 8 | 50,0 % | +0.23 R |
| fvg | 7 | 28,6 % | -0.71 R |
| fibonacci | 5 | 60,0 % | +1.05 R |
| order_block | 3 | 33,3 % | -0.47 R |
| medias | 2 | 50,0 % | -0.12 R |
| divergencia | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 150 | 57,3 % | -0.17 R |
| 16-20 h | 142 | 51,4 % | -0.06 R |
| 08-12 h | 127 | 44,1 % | -0.21 R |
| 00-04 h | 105 | 48,6 % | -0.16 R |
| 20-24 h | 100 | 65,0 % | -0.03 R |
| 04-08 h | 90 | 44,4 % | +0.04 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 338 | 54,7 % | -0.04 R |
| lateral (<20) | 230 | 46,5 % | -0.24 R |
| débil (20-25) | 146 | 54,1 % | -0.04 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 434 | 50,7 % | -0.02 R |
| alta | 193 | 54,4 % | -0.20 R |
| baja | 87 | 52,9 % | -0.34 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 308 | 53,6 % | -0.02 R |
| a favor | 281 | 49,5 % | -0.21 R |
| en contra | 125 | 53,6 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 503 | 50,9 % | -0.11 R |
| en contra | 207 | 54,6 % | -0.11 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 462 | 52,2 % | -0.09 R |
| a favor | 252 | 51,6 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.79 % |
| 18/05 14:00 | SOL/USDT | 1h | COMPRAR | 180 min | macd | -1.60 % |
| 21/10 15:50 | ETH/USDT | 5m | VENDER | 75 min | soportes | -1.58 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 18/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.96 % |
| 15/10 18:30 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.88 % |
| 22/10 17:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.85 % |
| 21/10 12:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.77 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**816 señales** del 08/01/2021 al 28/10/2026. Acierto (precio a favor al vencer): **52,1 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **ETH/USDT** | falla | 31,0 % en 42 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **1h** | acierta | 58,9 % en 158 | después 51,9 % en 243 casos | ❔ no se repite |
| plazo = **4-12 h** | acierta | 60,3 % en 121 | después 44,8 % en 143 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 67,3 % en 52 | después 48,0 % en 50 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 423 | 49,6 % | -0.08 R |
| 52-55 % | 345 | 55,1 % | -0.13 R |
| 55-58 % | 47 | 53,2 % | -0.03 R |
| ≥58 % | 1 | 0,0 % | -1.11 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 172 | 52,3 % | -0.29 R |
| GBP/JPY | 134 | 57,5 % | -0.03 R |
| Oro (XAU/USD) | 117 | 50,4 % | +0.07 R |
| GBP/USD | 98 | 54,1 % | -0.12 R |
| SOL/USDT | 93 | 53,8 % | -0.09 R |
| ETH/USDT | 49 | 30,6 % | -0.27 R |
| EUR/GBP | 45 | 53,3 % | -0.23 R |
| AUD/USD | 44 | 52,3 % | +0.27 R |
| USD/JPY | 32 | 50,0 % | -0.07 R |
| XRP/USDT | 28 | 57,1 % | +0.08 R |
| EUR/JPY | 3 | 66,7 % | +0.21 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 401 | 54,6 % | -0.10 R |
| 4h | 237 | 51,1 % | -0.15 R |
| 1d | 140 | 51,4 % | +0.11 R |
| 15m | 38 | 34,2 % | -0.48 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 264 | 51,9 % | -0.20 R |
| 12-24 h | 251 | 51,4 % | -0.11 R |
| 2-5 días | 237 | 52,3 % | -0.03 R |
| 1-2 días | 64 | 54,7 % | +0.14 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 323 | 52,3 % | -0.14 R |
| bollinger | 249 | 52,2 % | -0.05 R |
| barrida | 95 | 52,6 % | -0.13 R |
| estocastico | 60 | 55,0 % | -0.11 R |
| order_block | 34 | 47,1 % | -0.12 R |
| ruptura | 20 | 50,0 % | +0.29 R |
| macd | 19 | 42,1 % | -0.31 R |
| fibonacci | 9 | 66,7 % | +0.76 R |
| rsi | 8 | 25,0 % | -0.86 R |
| choch | 2 | 100,0 % | +0.85 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 208 | 51,0 % | +0.14 R |
| 08-12 h | 143 | 47,6 % | -0.31 R |
| 12-16 h | 128 | 50,0 % | -0.12 R |
| 00-04 h | 121 | 54,5 % | -0.19 R |
| 16-20 h | 114 | 54,4 % | -0.14 R |
| 20-24 h | 102 | 57,8 % | -0.09 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 351 | 50,4 % | -0.07 R |
| lateral (<20) | 297 | 54,5 % | -0.14 R |
| débil (20-25) | 168 | 51,2 % | -0.08 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 457 | 51,9 % | -0.12 R |
| baja | 181 | 54,1 % | -0.02 R |
| alta | 178 | 50,6 % | -0.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 307 | 54,4 % | -0.04 R |
| a favor | 282 | 48,9 % | -0.07 R |
| en contra | 227 | 52,9 % | -0.22 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 584 | 51,4 % | -0.16 R |
| en contra | 231 | 53,7 % | +0.06 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 523 | 50,3 % | -0.18 R |
| a favor | 293 | 55,3 % | +0.04 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 01/06 18:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.84 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 16/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -7.01 % |
| 14/12 09:00 | SOL/USDT | 4h | COMPRAR | 4800 min | barrida | -6.91 % |
| 10/07 10:00 | ETH/USDT | 4h | VENDER | 720 min | bollinger | -6.21 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 27/08 06:00 | Oro (XAU/USD) | 1d | COMPRAR | 4320 min | soportes | -5.74 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**4 señales** del 28/10/2026 al 29/10/2026. Acierto (precio a favor al vencer): **75,0 %** · resultado medio con SL/TP tras costes: **-0.93 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 2 | 100,0 % | -0.64 R |
| 52-55 % | 2 | 50,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 2 | 50,0 % | -1.19 R |
| USD/CHF | 1 | 100,0 % | -1.21 R |
| USD/JPY | 1 | 100,0 % | -0.13 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 2 | 50,0 % | -1.22 R |
| 5m | 2 | 100,0 % | -0.64 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 3 | 66,7 % | -0.86 R |
| 30-59 min | 1 | 100,0 % | -1.15 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| barrida | 1 | 100,0 % | -1.21 R |
| bollinger | 1 | 0,0 % | -1.24 R |
| estocastico | 1 | 100,0 % | -1.15 R |
| rsi | 1 | 100,0 % | -1.15 R |
| soportes | 1 | 100,0 % | -0.13 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 2 | 50,0 % | -1.22 R |
| 00-04 h | 1 | 100,0 % | -0.13 R |
| 16-20 h | 1 | 100,0 % | -1.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 2 | 100,0 % | -0.64 R |
| lateral (<20) | 1 | 100,0 % | -1.21 R |
| débil (20-25) | 1 | 0,0 % | -1.24 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| baja | 2 | 50,0 % | -1.22 R |
| alta | 2 | 100,0 % | -0.64 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 2 | 50,0 % | -1.22 R |
| en contra | 1 | 100,0 % | -1.15 R |
| sin tendencia | 1 | 100,0 % | -0.13 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 3 | 66,7 % | -1.20 R |
| en contra | 1 | 100,0 % | -0.13 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 2 | 100,0 % | -0.67 R |
| en contra | 2 | 50,0 % | -1.19 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)

Todavía no hay señales comprobadas (4 señales apuntadas, esperando a vencer).
