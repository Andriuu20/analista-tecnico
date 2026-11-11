# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**719 señales** del 30/12/2025 al 10/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.15 R** · no se distingue del azar todavía (z = 1.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **jue** | acierta | 64,7 % en 68 | después 50,5 % en 91 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 437 | 50,8 % | -0.18 R |
| 52-55 % | 238 | 56,3 % | -0.08 R |
| 55-58 % | 41 | 56,1 % | -0.15 R |
| ≥58 % | 3 | 0,0 % | -0.56 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 176 | 52,8 % | -0.17 R |
| USD/JPY | 131 | 51,9 % | +0.02 R |
| Oro (XAU/USD) | 99 | 46,5 % | -0.31 R |
| USD/CHF | 93 | 62,4 % | +0.06 R |
| EUR/GBP | 68 | 51,5 % | -0.26 R |
| BTC/USDT | 42 | 52,4 % | -0.35 R |
| GBP/JPY | 41 | 53,7 % | -0.21 R |
| XRP/USDT | 39 | 46,2 % | -0.18 R |
| SOL/USDT | 26 | 53,8 % | -0.18 R |
| GBP/USD | 2 | 50,0 % | +0.12 R |
| ETH/USDT | 1 | 100,0 % | -1.19 R |
| USD/CAD | 1 | 100,0 % | +1.85 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 239 | 49,0 % | -0.14 R |
| 15m | 212 | 54,7 % | -0.22 R |
| 5m | 208 | 55,3 % | -0.08 R |
| 4h | 60 | 51,7 % | -0.14 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 334 | 53,3 % | -0.10 R |
| 2-4 h | 294 | 50,7 % | -0.15 R |
| 30-59 min | 91 | 57,1 % | -0.29 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 324 | 51,5 % | -0.20 R |
| velas | 110 | 49,1 % | -0.26 R |
| soportes | 75 | 53,3 % | -0.14 R |
| barrida | 73 | 64,4 % | +0.06 R |
| bos | 59 | 52,5 % | -0.01 R |
| estocastico | 55 | 50,9 % | -0.15 R |
| rsi | 25 | 56,0 % | -0.36 R |
| divergencia | 6 | 33,3 % | +1.00 R |
| fibonacci | 6 | 16,7 % | -1.11 R |
| choch | 2 | 0,0 % | -1.17 R |
| macd | 2 | 100,0 % | +0.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 150 | 54,0 % | -0.16 R |
| 12-16 h | 143 | 48,3 % | -0.31 R |
| 20-24 h | 117 | 58,1 % | -0.11 R |
| 08-12 h | 115 | 49,6 % | -0.29 R |
| 00-04 h | 99 | 57,6 % | -0.01 R |
| 04-08 h | 95 | 49,5 % | +0.11 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 330 | 56,4 % | -0.07 R |
| lateral (<20) | 246 | 47,6 % | -0.17 R |
| débil (20-25) | 143 | 53,1 % | -0.28 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 389 | 50,4 % | -0.15 R |
| alta | 215 | 58,1 % | -0.02 R |
| baja | 115 | 50,4 % | -0.36 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 299 | 54,5 % | -0.14 R |
| sin tendencia | 275 | 52,0 % | -0.15 R |
| en contra | 145 | 50,3 % | -0.14 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 507 | 53,5 % | -0.18 R |
| en contra | 206 | 50,5 % | -0.06 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 479 | 53,9 % | -0.18 R |
| a favor | 240 | 50,4 % | -0.08 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 17/06 17:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.79 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 08/07 02:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.34 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 09/11 15:50 | XRP/USDT | 5m | VENDER | 50 min | bollinger | -1.07 % |
| 07/11 03:55 | XRP/USDT | 5m | COMPRAR | 50 min | bollinger | -1.04 % |
| 30/07 06:00 | Oro (XAU/USD) | 4h | VENDER | 240 min | soportes | -0.97 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**898 señales** del 08/01/2021 al 10/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = 1.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 488 | 52,9 % | -0.06 R |
| 52-55 % | 372 | 54,8 % | -0.04 R |
| 55-58 % | 38 | 28,9 % | -0.37 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 174 | 54,6 % | -0.01 R |
| GBP/JPY | 165 | 57,0 % | -0.12 R |
| SOL/USDT | 131 | 55,7 % | +0.10 R |
| Oro (XAU/USD) | 117 | 51,3 % | +0.03 R |
| GBP/USD | 90 | 54,4 % | -0.15 R |
| ETH/USDT | 72 | 40,3 % | -0.23 R |
| EUR/GBP | 48 | 52,1 % | -0.36 R |
| AUD/USD | 34 | 52,9 % | +0.22 R |
| USD/JPY | 34 | 41,2 % | -0.15 R |
| EUR/JPY | 23 | 60,9 % | -0.19 R |
| XRP/USDT | 8 | 25,0 % | -0.70 R |
| BTC/USDT | 2 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 364 | 54,9 % | -0.17 R |
| 4h | 308 | 50,3 % | -0.12 R |
| 1d | 139 | 51,8 % | +0.09 R |
| 15m | 87 | 52,9 % | +0.29 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 289 | 51,6 % | -0.05 R |
| 4-12 h | 273 | 53,8 % | +0.01 R |
| 12-24 h | 273 | 52,0 % | -0.19 R |
| 1-2 días | 63 | 55,6 % | +0.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 322 | 55,3 % | +0.02 R |
| soportes | 310 | 51,3 % | -0.13 R |
| estocastico | 115 | 55,7 % | +0.19 R |
| barrida | 100 | 53,0 % | -0.21 R |
| choch | 23 | 60,9 % | -0.19 R |
| ruptura | 10 | 50,0 % | +0.16 R |
| velas | 6 | 0,0 % | -0.86 R |
| fibonacci | 6 | 33,3 % | -0.69 R |
| order_block | 6 | 50,0 % | -0.70 R |
| rsi | 5 | 40,0 % | -0.65 R |
| bos | 4 | 25,0 % | -0.84 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 239 | 51,5 % | -0.00 R |
| 08-12 h | 149 | 51,0 % | -0.19 R |
| 12-16 h | 149 | 51,0 % | -0.08 R |
| 00-04 h | 139 | 58,3 % | +0.06 R |
| 16-20 h | 127 | 49,6 % | -0.16 R |
| 20-24 h | 95 | 56,8 % | -0.09 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 382 | 52,9 % | -0.01 R |
| lateral (<20) | 324 | 52,2 % | -0.14 R |
| débil (20-25) | 192 | 53,1 % | -0.06 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 491 | 51,3 % | -0.08 R |
| baja | 204 | 55,4 % | -0.06 R |
| alta | 203 | 53,2 % | -0.06 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 336 | 54,2 % | -0.03 R |
| a favor | 331 | 49,5 % | -0.10 R |
| en contra | 231 | 55,0 % | -0.07 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 662 | 52,9 % | -0.06 R |
| en contra | 232 | 51,7 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 590 | 52,2 % | -0.08 R |
| a favor | 308 | 53,6 % | -0.04 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**54 señales** del 28/10/2026 al 11/11/2026. Acierto (precio a favor al vencer): **57,4 %** · resultado medio con SL/TP tras costes: **-0.21 R** · no se distingue del azar todavía (z = 1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 37 | 64,9 % | -0.28 R |
| 52-55 % | 16 | 37,5 % | +0.02 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 19 | 68,4 % | -0.09 R |
| EUR/JPY | 15 | 46,7 % | -0.62 R |
| USD/CHF | 5 | 60,0 % | +0.64 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| BTC/USDT | 2 | 50,0 % | +0.94 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| XRP/USDT | 2 | 50,0 % | -1.21 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 29 | 58,6 % | -0.31 R |
| 15m | 23 | 56,5 % | -0.13 R |
| 1h | 2 | 50,0 % | +0.94 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 37 | 54,1 % | -0.08 R |
| 30-59 min | 14 | 57,1 % | -0.69 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 19 | 68,4 % | -0.09 R |
| bollinger | 17 | 41,2 % | -0.60 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| barrida | 6 | 50,0 % | +0.35 R |
| rsi | 5 | 80,0 % | -0.09 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 19 | 78,9 % | +0.09 R |
| 20-24 h | 10 | 30,0 % | -0.35 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 7 | 71,4 % | +0.14 R |
| 04-08 h | 6 | 50,0 % | -0.66 R |
| 08-12 h | 4 | 25,0 % | +0.37 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 26 | 61,5 % | -0.02 R |
| débil (20-25) | 15 | 53,3 % | -0.40 R |
| lateral (<20) | 13 | 53,8 % | -0.33 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 30 | 53,3 % | -0.19 R |
| alta | 13 | 61,5 % | -0.19 R |
| baja | 11 | 63,6 % | -0.29 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 19 | 57,9 % | -0.36 R |
| sin tendencia | 19 | 63,2 % | -0.01 R |
| en contra | 16 | 50,0 % | -0.29 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 40 | 55,0 % | -0.23 R |
| en contra | 14 | 64,3 % | -0.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 40 | 57,5 % | -0.24 R |
| a favor | 14 | 57,1 % | -0.13 R |

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
**17 señales** del 28/10/2026 al 10/11/2026. Acierto (precio a favor al vencer): **41,2 %** · resultado medio con SL/TP tras costes: **-0.04 R** · no se distingue del azar todavía (z = -0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 10 | 40,0 % | -0.24 R |
| <52 % | 7 | 42,9 % | +0.12 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 7 | 42,9 % | -0.24 R |
| USD/CHF | 5 | 40,0 % | +0.36 R |
| GBP/JPY | 3 | 33,3 % | — |
| ETH/USDT | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 11 | 45,5 % | -0.24 R |
| 15m | 5 | 40,0 % | +0.36 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 9 | 44,4 % | +0.36 R |
| 2-5 días | 6 | 50,0 % | -0.03 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 8 | 50,0 % | -0.03 R |
| estocastico | 7 | 28,6 % | +0.12 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 4 | 25,0 % | -1.10 R |
| 20-24 h | 4 | 50,0 % | +1.89 R |
| 16-20 h | 3 | 33,3 % | -1.02 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 08-12 h | 2 | 50,0 % | +0.14 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 8 | 62,5 % | -0.31 R |
| débil (20-25) | 6 | 16,7 % | -0.08 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 12 | 33,3 % | +0.05 R |
| alta | 3 | 33,3 % | -1.12 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 14 | 42,9 % | -0.18 R |
| a favor | 3 | 33,3 % | +1.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 15 | 33,3 % | +0.07 R |
| en contra | 2 | 100,0 % | -1.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 13 | 38,5 % | +0.06 R |
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
