# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**611 señales** del 19/03/2026 al 06/11/2026. Acierto (precio a favor al vencer): **51,4 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 364 | 48,6 % | -0.23 R |
| 52-55 % | 220 | 55,0 % | -0.06 R |
| 55-58 % | 23 | 69,6 % | -0.26 R |
| ≥58 % | 4 | 0,0 % | -0.71 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 137 | 47,4 % | -0.23 R |
| USD/CHF | 122 | 58,2 % | +0.03 R |
| USD/JPY | 102 | 51,0 % | -0.18 R |
| Oro (XAU/USD) | 74 | 48,6 % | -0.41 R |
| EUR/GBP | 54 | 50,0 % | -0.24 R |
| BTC/USDT | 43 | 55,8 % | -0.06 R |
| GBP/JPY | 39 | 53,8 % | -0.10 R |
| SOL/USDT | 31 | 45,2 % | -0.36 R |
| XRP/USDT | 7 | 57,1 % | +0.23 R |
| ETH/USDT | 1 | 0,0 % | -1.14 R |
| USD/CAD | 1 | 0,0 % | -1.16 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 214 | 47,7 % | -0.17 R |
| 5m | 205 | 51,2 % | -0.14 R |
| 15m | 146 | 56,2 % | -0.14 R |
| 4h | 46 | 54,3 % | -0.45 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 313 | 53,4 % | -0.11 R |
| 2-4 h | 242 | 48,3 % | -0.26 R |
| 30-59 min | 56 | 53,6 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 279 | 49,1 % | -0.19 R |
| soportes | 81 | 49,4 % | -0.40 R |
| barrida | 74 | 63,5 % | -0.03 R |
| rsi | 49 | 55,1 % | -0.07 R |
| estocastico | 43 | 53,5 % | +0.16 R |
| velas | 43 | 51,2 % | -0.21 R |
| bos | 36 | 52,8 % | -0.05 R |
| medias | 9 | 33,3 % | -0.65 R |
| choch | 2 | 0,0 % | -1.21 R |
| divergencia | 1 | 0,0 % | -1.12 R |
| order_block | 1 | 100,0 % | -1.16 R |
| ruptura | 1 | 0,0 % | -1.16 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 139 | 49,6 % | -0.18 R |
| 12-16 h | 115 | 53,0 % | -0.25 R |
| 08-12 h | 95 | 45,3 % | -0.20 R |
| 20-24 h | 91 | 51,6 % | -0.40 R |
| 00-04 h | 89 | 56,2 % | -0.10 R |
| 04-08 h | 82 | 53,7 % | +0.12 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 316 | 54,1 % | -0.11 R |
| lateral (<20) | 185 | 47,6 % | -0.26 R |
| débil (20-25) | 110 | 50,0 % | -0.23 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 336 | 47,9 % | -0.13 R |
| alta | 199 | 55,3 % | -0.16 R |
| baja | 76 | 56,6 % | -0.41 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 233 | 49,8 % | -0.28 R |
| a favor | 227 | 52,9 % | -0.16 R |
| en contra | 151 | 51,7 % | -0.04 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 461 | 52,3 % | -0.15 R |
| en contra | 144 | 47,9 % | -0.27 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 446 | 52,5 % | -0.17 R |
| a favor | 165 | 48,5 % | -0.19 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 05/11 15:25 | ETH/USDT | 5m | COMPRAR | 75 min | rsi | -4.44 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 15/10 06:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -1.23 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 24/08 15:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.10 % |
| 25/08 04:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -0.96 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**782 señales** del 08/01/2021 al 06/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| franja = **20-24 h** | acierta | 64,6 % en 48 | después 53,3 % en 45 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 417 | 51,1 % | -0.11 R |
| 52-55 % | 325 | 54,5 % | -0.12 R |
| 55-58 % | 40 | 55,0 % | +0.20 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 156 | 59,0 % | -0.09 R |
| USD/CHF | 143 | 52,4 % | -0.19 R |
| SOL/USDT | 118 | 55,9 % | +0.03 R |
| Oro (XAU/USD) | 116 | 52,6 % | +0.08 R |
| ETH/USDT | 74 | 43,2 % | -0.26 R |
| GBP/USD | 73 | 56,2 % | -0.05 R |
| EUR/GBP | 49 | 49,0 % | -0.33 R |
| AUD/USD | 28 | 46,4 % | +0.06 R |
| USD/JPY | 18 | 33,3 % | -0.46 R |
| XRP/USDT | 6 | 16,7 % | -0.63 R |
| EUR/USD | 1 | 100,0 % | +2.94 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 312 | 53,8 % | -0.20 R |
| 4h | 294 | 53,1 % | -0.13 R |
| 1d | 138 | 52,9 % | +0.13 R |
| 15m | 38 | 39,5 % | +0.18 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 278 | 52,5 % | -0.01 R |
| 12-24 h | 237 | 50,2 % | -0.26 R |
| 4-12 h | 205 | 54,1 % | -0.08 R |
| 1-2 días | 62 | 58,1 % | +0.11 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 319 | 51,1 % | -0.17 R |
| bollinger | 292 | 55,8 % | -0.02 R |
| barrida | 87 | 52,9 % | -0.13 R |
| estocastico | 66 | 54,5 % | +0.14 R |
| fibonacci | 6 | 66,7 % | +0.22 R |
| rsi | 5 | 40,0 % | -0.18 R |
| bos | 4 | 25,0 % | -0.84 R |
| ruptura | 4 | 0,0 % | -1.05 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| order_block | 1 | 0,0 % | -1.01 R |
| medias | 1 | 0,0 % | -1.13 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 218 | 52,8 % | +0.03 R |
| 08-12 h | 127 | 48,8 % | -0.33 R |
| 00-04 h | 119 | 56,3 % | -0.01 R |
| 12-16 h | 117 | 53,8 % | +0.01 R |
| 16-20 h | 108 | 46,3 % | -0.17 R |
| 20-24 h | 93 | 59,1 % | -0.22 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 329 | 52,6 % | -0.10 R |
| lateral (<20) | 288 | 54,2 % | -0.09 R |
| débil (20-25) | 165 | 50,3 % | -0.10 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 437 | 51,7 % | -0.09 R |
| baja | 181 | 54,1 % | -0.08 R |
| alta | 164 | 53,7 % | -0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 300 | 54,7 % | -0.10 R |
| a favor | 268 | 50,4 % | -0.10 R |
| en contra | 214 | 52,8 % | -0.09 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 595 | 53,1 % | -0.09 R |
| en contra | 183 | 50,3 % | -0.12 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 532 | 51,7 % | -0.11 R |
| a favor | 250 | 54,8 % | -0.07 R |

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
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**33 señales** del 28/10/2026 al 07/11/2026. Acierto (precio a favor al vencer): **57,6 %** · resultado medio con SL/TP tras costes: **-0.38 R** · no se distingue del azar todavía (z = 0.9).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 23 | 60,9 % | -0.46 R |
| 52-55 % | 9 | 44,4 % | -0.10 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 12 | 50,0 % | -0.79 R |
| USD/JPY | 10 | 60,0 % | -0.16 R |
| EUR/GBP | 3 | 33,3 % | -0.37 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| USD/CHF | 2 | 100,0 % | +0.34 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| ETH/USDT | 1 | 100,0 % | — |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 17 | 52,9 % | -0.46 R |
| 15m | 16 | 62,5 % | -0.29 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 20 | 45,0 % | -0.39 R |
| 30-59 min | 10 | 70,0 % | -0.65 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 11 | 36,4 % | -0.71 R |
| soportes | 10 | 60,0 % | -0.16 R |
| estocastico | 7 | 71,4 % | -0.47 R |
| barrida | 3 | 66,7 % | -0.15 R |
| rsi | 3 | 100,0 % | -0.43 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 10 | 30,0 % | -0.49 R |
| 00-04 h | 8 | 87,5 % | -0.30 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 5 | 60,0 % | +0.20 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 08-12 h | 1 | 100,0 % | +1.91 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 17 | 64,7 % | -0.08 R |
| lateral (<20) | 9 | 55,6 % | -0.79 R |
| débil (20-25) | 7 | 42,9 % | -0.68 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 16 | 50,0 % | -0.32 R |
| alta | 12 | 66,7 % | -0.19 R |
| baja | 5 | 60,0 % | -1.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 14 | 64,3 % | -0.42 R |
| en contra | 10 | 50,0 % | -0.31 R |
| sin tendencia | 9 | 55,6 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 24 | 58,3 % | -0.41 R |
| en contra | 9 | 55,6 % | -0.29 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 23 | 56,5 % | -0.38 R |
| a favor | 10 | 60,0 % | -0.38 R |

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
**12 señales** del 28/10/2026 al 05/11/2026. Acierto (precio a favor al vencer): **41,7 %** · resultado medio con SL/TP tras costes: **-0.15 R** · no se distingue del azar todavía (z = -0.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 8 | 50,0 % | -0.04 R |
| <52 % | 4 | 25,0 % | -0.29 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 6 | 50,0 % | -0.04 R |
| USD/CHF | 2 | 0,0 % | +0.10 R |
| GBP/JPY | 2 | 50,0 % | — |
| ETH/USDT | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 9 | 55,6 % | -0.04 R |
| 15m | 2 | 0,0 % | +0.10 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 5 | 40,0 % | +0.10 R |
| 2-5 días | 5 | 60,0 % | +0.30 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 7 | 57,1 % | +0.30 R |
| estocastico | 3 | 0,0 % | -0.29 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 3 | 0,0 % | -1.07 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 20-24 h | 3 | 66,7 % | +2.14 R |
| 16-20 h | 2 | 50,0 % | — |
| 08-12 h | 1 | 0,0 % | -1.06 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 5 | 20,0 % | -0.26 R |
| fuerte (≥25) | 4 | 75,0 % | -1.12 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 9 | 33,3 % | +0.23 R |
| alta | 2 | 50,0 % | -1.12 R |
| baja | 1 | 100,0 % | -1.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 9 | 44,4 % | -0.39 R |
| a favor | 3 | 33,3 % | +1.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 11 | 36,4 % | -0.15 R |
| en contra | 1 | 100,0 % | — |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 9 | 33,3 % | +0.00 R |
| a favor | 3 | 66,7 % | -1.06 R |

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
