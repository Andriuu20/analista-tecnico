# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1063 señales** del 22/01/2025 al 18/11/2026. Acierto (precio a favor al vencer): **52,5 %** · resultado medio con SL/TP tras costes: **-0.09 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 59,3 % en 150 | después 51,3 % en 115 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 657 | 53,6 % | -0.05 R |
| 52-55 % | 367 | 50,4 % | -0.15 R |
| 55-58 % | 39 | 53,8 % | -0.05 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 265 | 55,8 % | -0.13 R |
| SOL/USDT | 108 | 51,9 % | -0.14 R |
| EUR/JPY | 99 | 49,5 % | -0.19 R |
| XRP/USDT | 97 | 46,4 % | -0.06 R |
| USD/CHF | 91 | 58,2 % | +0.04 R |
| BTC/USDT | 83 | 50,6 % | -0.04 R |
| Oro (XAU/USD) | 70 | 45,7 % | -0.28 R |
| AUD/USD | 67 | 59,7 % | +0.19 R |
| GBP/JPY | 66 | 43,9 % | +0.02 R |
| USD/CAD | 57 | 57,9 % | -0.14 R |
| EUR/GBP | 48 | 47,9 % | -0.21 R |
| EUR/USD | 11 | 72,7 % | +0.60 R |
| GBP/USD | 1 | 0,0 % | -1.16 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 329 | 50,8 % | -0.09 R |
| 5m | 318 | 51,3 % | -0.16 R |
| 15m | 255 | 52,9 % | +0.02 R |
| 4h | 161 | 57,8 % | -0.10 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 549 | 54,1 % | -0.07 R |
| 1-2 h | 420 | 53,1 % | -0.09 R |
| 30-59 min | 94 | 40,4 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 344 | 49,1 % | -0.10 R |
| velas | 207 | 58,0 % | +0.04 R |
| soportes | 149 | 49,0 % | -0.38 R |
| estocastico | 74 | 48,6 % | +0.03 R |
| barrida | 70 | 61,4 % | -0.03 R |
| fibonacci | 68 | 58,8 % | +0.07 R |
| order_block | 52 | 57,7 % | -0.16 R |
| bos | 43 | 51,2 % | +0.04 R |
| rsi | 38 | 55,3 % | -0.03 R |
| fvg | 10 | 20,0 % | -0.60 R |
| supertrend | 6 | 33,3 % | -0.47 R |
| divergencia | 5 | 60,0 % | +0.50 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 231 | 48,5 % | -0.19 R |
| 12-16 h | 209 | 50,2 % | -0.07 R |
| 00-04 h | 170 | 57,6 % | -0.01 R |
| 04-08 h | 159 | 48,4 % | +0.03 R |
| 20-24 h | 152 | 56,6 % | -0.09 R |
| 08-12 h | 142 | 56,3 % | -0.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 443 | 53,7 % | -0.12 R |
| lateral (<20) | 396 | 52,3 % | -0.01 R |
| débil (20-25) | 224 | 50,4 % | -0.16 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 600 | 53,0 % | -0.09 R |
| alta | 264 | 50,4 % | -0.05 R |
| baja | 199 | 53,8 % | -0.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 464 | 55,2 % | -0.01 R |
| sin tendencia | 401 | 51,6 % | -0.13 R |
| en contra | 198 | 48,0 % | -0.18 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 669 | 50,5 % | -0.12 R |
| en contra | 385 | 55,6 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 678 | 50,7 % | -0.05 R |
| a favor | 385 | 55,6 % | -0.15 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 16/11 15:30 | XRP/USDT | 15m | COMPRAR | 30 min | supertrend | -2.66 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -2.33 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 13/11 03:15 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -2.00 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 17/11 16:15 | SOL/USDT | 5m | COMPRAR | 100 min | estocastico | -1.96 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**720 señales** del 08/01/2021 al 16/11/2026. Acierto (precio a favor al vencer): **52,6 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **mar** | acierta | 62,4 % en 85 | después 44,8 % en 58 casos | ❔ no se repite |
| tendencia_txt = **sin tendencia** | acierta | 60,2 % en 118 | después 52,0 % en 127 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 419 | 55,4 % | -0.07 R |
| 52-55 % | 268 | 48,9 % | -0.17 R |
| 55-58 % | 33 | 48,5 % | +0.10 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 151 | 57,6 % | -0.11 R |
| SOL/USDT | 118 | 55,1 % | -0.02 R |
| Oro (XAU/USD) | 110 | 51,8 % | -0.02 R |
| GBP/JPY | 74 | 58,1 % | -0.15 R |
| USD/JPY | 64 | 48,4 % | +0.09 R |
| EUR/GBP | 48 | 52,1 % | -0.46 R |
| ETH/USDT | 43 | 37,2 % | -0.01 R |
| GBP/USD | 43 | 46,5 % | -0.24 R |
| AUD/USD | 34 | 52,9 % | -0.01 R |
| EUR/JPY | 28 | 50,0 % | -0.51 R |
| XRP/USDT | 6 | 50,0 % | +0.92 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 295 | 52,9 % | -0.10 R |
| 1h | 243 | 52,3 % | -0.19 R |
| 1d | 135 | 52,6 % | +0.06 R |
| 15m | 47 | 53,2 % | -0.08 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 276 | 52,9 % | -0.09 R |
| 4-12 h | 191 | 52,4 % | -0.08 R |
| 12-24 h | 190 | 51,1 % | -0.20 R |
| 1-2 días | 63 | 57,1 % | +0.11 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 328 | 52,1 % | -0.13 R |
| bollinger | 231 | 54,5 % | +0.02 R |
| estocastico | 81 | 59,3 % | -0.10 R |
| barrida | 47 | 46,8 % | -0.24 R |
| order_block | 16 | 56,2 % | +0.30 R |
| rsi | 7 | 42,9 % | -1.15 R |
| bos | 5 | 40,0 % | +0.56 R |
| choch | 5 | 60,0 % | -0.73 R |
| fvg | 5 | 40,0 % | -0.47 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| fibonacci | 1 | 0,0 % | -1.02 R |
| ruptura | 1 | 0,0 % | -1.03 R |
| velas | 1 | 100,0 % | +1.98 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 199 | 50,3 % | +0.02 R |
| 00-04 h | 120 | 56,7 % | -0.11 R |
| 08-12 h | 109 | 52,3 % | -0.11 R |
| 12-16 h | 98 | 57,1 % | -0.09 R |
| 16-20 h | 98 | 46,9 % | -0.21 R |
| 20-24 h | 96 | 54,2 % | -0.20 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 308 | 51,6 % | -0.11 R |
| lateral (<20) | 261 | 54,4 % | -0.08 R |
| débil (20-25) | 151 | 51,7 % | -0.09 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 414 | 50,2 % | -0.07 R |
| baja | 158 | 60,1 % | -0.06 R |
| alta | 148 | 51,4 % | -0.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 274 | 48,2 % | -0.25 R |
| sin tendencia | 245 | 55,9 % | +0.03 R |
| en contra | 201 | 54,7 % | -0.04 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 518 | 53,5 % | -0.09 R |
| en contra | 200 | 50,0 % | -0.10 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 478 | 52,7 % | -0.10 R |
| a favor | 242 | 52,5 % | -0.09 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 17/08 18:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -18.07 % |
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 13/11 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -6.32 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**91 señales** del 28/10/2026 al 18/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.20 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 62 | 54,8 % | -0.29 R |
| 52-55 % | 28 | 46,4 % | +0.04 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 22 | 36,4 % | -0.42 R |
| USD/CHF | 11 | 54,5 % | -0.07 R |
| BTC/USDT | 11 | 45,5 % | +0.14 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 2 | 0,0 % | -1.14 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 45 | 60,0 % | -0.11 R |
| 15m | 37 | 48,6 % | -0.23 R |
| 1h | 9 | 33,3 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 68 | 51,5 % | -0.10 R |
| 30-59 min | 17 | 52,9 % | -0.62 R |
| 2-4 h | 6 | 66,7 % | -0.13 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 29 | 69,0 % | -0.04 R |
| bollinger | 28 | 32,1 % | -0.38 R |
| barrida | 12 | 50,0 % | -0.16 R |
| rsi | 11 | 54,5 % | -0.53 R |
| estocastico | 11 | 45,5 % | -0.61 R |
| velas | 2 | 100,0 % | +1.23 R |
| fibonacci | 2 | 100,0 % | +2.87 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 27 | 74,1 % | -0.07 R |
| 08-12 h | 18 | 55,6 % | +0.22 R |
| 04-08 h | 13 | 38,5 % | -0.40 R |
| 20-24 h | 13 | 30,8 % | -0.39 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 43 | 46,5 % | -0.09 R |
| lateral (<20) | 30 | 63,3 % | -0.15 R |
| débil (20-25) | 18 | 50,0 % | -0.53 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 49 | 53,1 % | -0.29 R |
| alta | 25 | 48,0 % | -0.25 R |
| baja | 17 | 58,8 % | +0.17 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 31 | 41,9 % | -0.41 R |
| a favor | 30 | 60,0 % | -0.19 R |
| sin tendencia | 30 | 56,7 % | +0.01 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 66 | 48,5 % | -0.33 R |
| en contra | 25 | 64,0 % | +0.15 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 70 | 48,6 % | -0.21 R |
| a favor | 21 | 66,7 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 12/11 16:45 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.23 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**36 señales** del 28/10/2026 al 16/11/2026. Acierto (precio a favor al vencer): **22,2 %** · resultado medio con SL/TP tras costes: **-0.20 R** · claramente peor que el azar (z = -3.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 20 | 25,0 % | -0.13 R |
| <52 % | 16 | 18,8 % | -0.28 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 14 | 28,6 % | -0.03 R |
| USD/CHF | 10 | 20,0 % | +0.11 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.41 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 28 | 21,4 % | -0.20 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 21 | 19,0 % | -0.03 R |
| 4-12 h | 11 | 36,4 % | -0.05 R |
| 12-24 h | 3 | 0,0 % | -1.08 R |
| 1-2 días | 1 | 0,0 % | — |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 18 | 27,8 % | +0.08 R |
| estocastico | 14 | 21,4 % | -0.18 R |
| soportes | 3 | 0,0 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 9 | 22,2 % | -1.09 R |
| 12-16 h | 7 | 28,6 % | -0.64 R |
| 20-24 h | 6 | 33,3 % | +1.17 R |
| 16-20 h | 6 | 16,7 % | +0.98 R |
| 04-08 h | 4 | 0,0 % | -1.02 R |
| 08-12 h | 4 | 25,0 % | -0.29 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 26 | 23,1 % | -0.31 R |
| débil (20-25) | 7 | 14,3 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 25 | 16,0 % | -0.13 R |
| alta | 9 | 22,2 % | -1.07 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 29 | 20,7 % | -0.25 R |
| en contra | 4 | 25,0 % | -1.16 R |
| a favor | 3 | 33,3 % | +0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 33 | 18,2 % | -0.27 R |
| en contra | 3 | 66,7 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 31 | 19,4 % | -0.29 R |
| a favor | 5 | 40,0 % | +0.30 R |

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
