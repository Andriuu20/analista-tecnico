# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**567 señales** del 26/03/2026 al 28/10/2026. Acierto (precio a favor al vencer): **50,8 %** · resultado medio con SL/TP tras costes: **-0.15 R** · no se distingue del azar todavía (z = 0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 316 | 49,4 % | -0.09 R |
| 52-55 % | 212 | 51,4 % | -0.19 R |
| 55-58 % | 38 | 60,5 % | -0.41 R |
| ≥58 % | 1 | 0,0 % | -1.17 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 134 | 54,5 % | -0.14 R |
| USD/CHF | 93 | 54,8 % | -0.18 R |
| Oro (XAU/USD) | 89 | 44,9 % | -0.31 R |
| ETH/USDT | 77 | 57,1 % | +0.11 R |
| EUR/GBP | 51 | 39,2 % | -0.42 R |
| BTC/USDT | 47 | 57,4 % | -0.07 R |
| GBP/JPY | 34 | 41,2 % | -0.15 R |
| SOL/USDT | 27 | 40,7 % | -0.14 R |
| USD/JPY | 10 | 30,0 % | -0.30 R |
| EUR/USD | 5 | 100,0 % | +0.93 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 223 | 50,7 % | -0.24 R |
| 5m | 197 | 53,8 % | -0.10 R |
| 1h | 137 | 48,2 % | -0.02 R |
| 4h | 10 | 30,0 % | -1.03 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 213 | 54,5 % | -0.00 R |
| 30-59 min | 186 | 49,5 % | -0.33 R |
| 2-4 h | 168 | 47,6 % | -0.15 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 204 | 50,0 % | -0.15 R |
| soportes | 99 | 53,5 % | +0.02 R |
| barrida | 85 | 52,9 % | -0.22 R |
| estocastico | 84 | 53,6 % | -0.30 R |
| velas | 42 | 40,5 % | -0.35 R |
| bos | 35 | 54,3 % | -0.03 R |
| rsi | 15 | 53,3 % | +0.32 R |
| order_block | 5 | 20,0 % | -0.69 R |
| fvg | 1 | 100,0 % | +2.75 R |
| divergencia | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 124 | 48,4 % | -0.10 R |
| 12-16 h | 118 | 55,9 % | -0.23 R |
| 08-12 h | 104 | 49,0 % | -0.19 R |
| 00-04 h | 87 | 46,0 % | -0.23 R |
| 04-08 h | 70 | 47,1 % | +0.04 R |
| 20-24 h | 64 | 59,4 % | -0.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 266 | 54,1 % | -0.15 R |
| lateral (<20) | 193 | 45,6 % | -0.24 R |
| débil (20-25) | 108 | 51,9 % | +0.01 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 354 | 51,4 % | -0.08 R |
| alta | 151 | 50,3 % | -0.20 R |
| baja | 62 | 48,4 % | -0.47 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 253 | 54,2 % | -0.09 R |
| a favor | 215 | 46,5 % | -0.16 R |
| en contra | 99 | 51,5 % | -0.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 427 | 50,8 % | -0.16 R |
| en contra | 138 | 50,7 % | -0.13 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 389 | 50,6 % | -0.18 R |
| a favor | 178 | 51,1 % | -0.08 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 21/10 15:50 | ETH/USDT | 5m | VENDER | 75 min | soportes | -1.58 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 18/10 14:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -1.07 % |
| 18/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.96 % |
| 22/10 17:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.85 % |
| 21/10 12:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.77 % |
| 08/05 15:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.75 % |
| 07/04 03:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.74 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**827 señales** del 08/01/2021 al 24/10/2026. Acierto (precio a favor al vencer): **53,6 %** · resultado medio con SL/TP tras costes: **-0.06 R** · claramente mejor que el azar (z = 2.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 67,9 % en 53 | después 53,8 % en 106 casos | ❔ no se repite |
| mercado = **ETH/USDT** | falla | 31,7 % en 41 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **1h** | acierta | 62,1 % en 174 | después 52,7 % en 264 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | acierta | 60,4 % en 169 | después 51,0 % en 147 casos | ❔ no se repite |
| tendencia_txt = **sin tendencia** | acierta | 58,4 % en 149 | después 56,4 % en 156 casos | ✅ confirmado |
| zona_txt = **a favor (barato al comprar / caro al vender)** | acierta | 56,2 % en 272 | después 50,5 % en 315 casos | ❔ no se repite |
| estructura_txt = **a favor** | acierta | 58,9 % en 158 | después 54,0 % en 137 casos | ❔ no se repite |
| estrategia = **soportes** | acierta | 57,4 % en 223 | después 47,4 % en 95 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 444 | 51,4 % | -0.03 R |
| 52-55 % | 342 | 56,4 % | -0.10 R |
| 55-58 % | 41 | 53,7 % | +0.09 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 159 | 58,5 % | -0.05 R |
| USD/CHF | 157 | 56,1 % | -0.10 R |
| Oro (XAU/USD) | 117 | 51,3 % | +0.09 R |
| GBP/USD | 102 | 54,9 % | -0.18 R |
| SOL/USDT | 93 | 51,6 % | -0.15 R |
| ETH/USDT | 50 | 30,0 % | -0.25 R |
| AUD/USD | 44 | 52,3 % | +0.27 R |
| EUR/GBP | 37 | 56,8 % | -0.11 R |
| XRP/USDT | 35 | 62,9 % | +0.12 R |
| USD/JPY | 29 | 51,7 % | +0.07 R |
| EUR/JPY | 3 | 66,7 % | -0.44 R |
| BTC/USDT | 1 | 0,0 % | -1.01 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 438 | 56,4 % | -0.06 R |
| 4h | 224 | 50,0 % | -0.13 R |
| 1d | 138 | 52,2 % | +0.15 R |
| 15m | 27 | 44,4 % | -0.45 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-24 h | 310 | 56,8 % | -0.05 R |
| 4-12 h | 227 | 49,3 % | -0.19 R |
| 2-5 días | 226 | 51,8 % | -0.01 R |
| 1-2 días | 64 | 59,4 % | +0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 318 | 54,4 % | -0.04 R |
| bollinger | 262 | 52,3 % | -0.06 R |
| barrida | 96 | 52,1 % | -0.20 R |
| estocastico | 69 | 63,8 % | +0.07 R |
| order_block | 34 | 44,1 % | -0.00 R |
| macd | 23 | 47,8 % | -0.41 R |
| ruptura | 20 | 50,0 % | +0.29 R |
| fibonacci | 6 | 66,7 % | +0.81 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| bos | 1 | 0,0 % | -1.05 R |
| choch | 1 | 100,0 % | -1.15 R |
| medias | 1 | 0,0 % | +0.94 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 211 | 51,7 % | +0.11 R |
| 08-12 h | 146 | 50,0 % | -0.23 R |
| 00-04 h | 127 | 55,9 % | -0.14 R |
| 12-16 h | 123 | 52,8 % | -0.05 R |
| 16-20 h | 113 | 56,6 % | -0.08 R |
| 20-24 h | 107 | 57,0 % | -0.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 350 | 50,9 % | -0.03 R |
| lateral (<20) | 316 | 56,0 % | -0.09 R |
| débil (20-25) | 161 | 54,7 % | -0.05 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 462 | 53,2 % | -0.07 R |
| baja | 184 | 55,4 % | -0.00 R |
| alta | 181 | 52,5 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 305 | 57,4 % | +0.03 R |
| a favor | 301 | 50,2 % | -0.07 R |
| en contra | 221 | 52,9 % | -0.17 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 587 | 53,2 % | -0.11 R |
| en contra | 237 | 54,0 % | +0.08 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 532 | 51,9 % | -0.15 R |
| a favor | 295 | 56,6 % | +0.11 R |

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
**2 señales** del 28/10/2026 al 28/10/2026. Acierto (precio a favor al vencer): **50,0 %** · resultado medio con SL/TP tras costes: **+nan R** · no se distingue del azar todavía (z = 0.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 2 | 50,0 % | — |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 1 | 0,0 % | — |
| USD/CHF | 1 | 100,0 % | — |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 2 | 50,0 % | — |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 2 | 50,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| barrida | 1 | 100,0 % | — |
| bollinger | 1 | 0,0 % | — |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 2 | 50,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| lateral (<20) | 1 | 100,0 % | — |
| débil (20-25) | 1 | 0,0 % | — |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| baja | 2 | 50,0 % | — |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 2 | 50,0 % | — |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 2 | 50,0 % | — |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 1 | 100,0 % | — |
| en contra | 1 | 0,0 % | — |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 28/10 13:15 | EUR/JPY | 15m | VENDER | 75 min | bollinger | -0.12 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)

Todavía no hay señales comprobadas (1 señales apuntadas, esperando a vencer).
