# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**922 señales** del 31/10/2025 al 24/11/2026. Acierto (precio a favor al vencer): **49,5 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = -0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| dia = **jue** | acierta | 60,6 % en 94 | después 54,1 % en 74 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 548 | 52,2 % | -0.15 R |
| 52-55 % | 330 | 43,9 % | -0.26 R |
| 55-58 % | 33 | 57,6 % | -0.04 R |
| ≥58 % | 11 | 54,5 % | -0.41 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| BTC/USDT | 132 | 48,5 % | -0.24 R |
| EUR/JPY | 122 | 40,2 % | -0.28 R |
| SOL/USDT | 112 | 56,2 % | -0.13 R |
| USD/JPY | 100 | 53,0 % | -0.22 R |
| USD/CAD | 85 | 47,1 % | -0.18 R |
| EUR/GBP | 78 | 46,2 % | -0.29 R |
| Oro (XAU/USD) | 74 | 47,3 % | -0.51 R |
| USD/CHF | 58 | 53,4 % | -0.15 R |
| AUD/USD | 55 | 60,0 % | +0.15 R |
| GBP/JPY | 54 | 55,6 % | -0.00 R |
| XRP/USDT | 27 | 25,9 % | -0.03 R |
| ETH/USDT | 21 | 61,9 % | -0.30 R |
| EUR/USD | 3 | 66,7 % | +2.83 R |
| GBP/USD | 1 | 0,0 % | -1.11 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 371 | 48,2 % | -0.17 R |
| 5m | 286 | 47,9 % | -0.25 R |
| 15m | 193 | 50,8 % | -0.05 R |
| 4h | 72 | 58,3 % | -0.45 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 434 | 49,5 % | -0.22 R |
| 2-4 h | 432 | 50,7 % | -0.18 R |
| 30-59 min | 56 | 39,3 % | -0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 353 | 49,0 % | -0.18 R |
| estocastico | 151 | 49,0 % | -0.19 R |
| velas | 99 | 56,6 % | +0.01 R |
| soportes | 96 | 47,9 % | -0.60 R |
| order_block | 73 | 52,1 % | -0.11 R |
| barrida | 48 | 54,2 % | -0.08 R |
| bos | 38 | 44,7 % | -0.16 R |
| fibonacci | 25 | 44,0 % | -0.17 R |
| rsi | 18 | 50,0 % | -0.10 R |
| fvg | 10 | 40,0 % | -0.39 R |
| divergencia | 5 | 60,0 % | +0.50 R |
| ruptura | 4 | 0,0 % | -0.40 R |
| supertrend | 2 | 50,0 % | +0.88 R |
| choch | 1 | 0,0 % | -1.18 R |
| macd | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 195 | 49,2 % | -0.16 R |
| 12-16 h | 188 | 46,3 % | -0.22 R |
| 08-12 h | 148 | 46,6 % | -0.36 R |
| 04-08 h | 138 | 50,0 % | +0.04 R |
| 20-24 h | 129 | 51,2 % | -0.34 R |
| 00-04 h | 124 | 55,6 % | -0.11 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 395 | 47,1 % | -0.33 R |
| lateral (<20) | 321 | 48,6 % | -0.09 R |
| débil (20-25) | 206 | 55,3 % | -0.10 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 518 | 50,0 % | -0.13 R |
| alta | 211 | 47,9 % | -0.25 R |
| baja | 193 | 49,7 % | -0.31 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 435 | 52,9 % | -0.08 R |
| sin tendencia | 373 | 47,2 % | -0.27 R |
| en contra | 114 | 43,9 % | -0.38 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 656 | 49,2 % | -0.24 R |
| en contra | 259 | 49,8 % | -0.09 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 603 | 49,6 % | -0.18 R |
| a favor | 319 | 49,2 % | -0.22 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 03:15 | SOL/USDT | 5m | COMPRAR | 100 min | velas | -3.02 % |
| 13/11 06:55 | SOL/USDT | 5m | VENDER | 75 min | estocastico | -2.45 % |
| 21/11 13:35 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -2.32 % |
| 23/11 16:45 | SOL/USDT | 5m | COMPRAR | 100 min | estocastico | -2.13 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 23/11 17:05 | BTC/USDT | 5m | COMPRAR | 100 min | estocastico | -1.98 % |
| 22/11 09:40 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -1.83 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**757 señales** del 16/12/2020 al 23/11/2026. Acierto (precio a favor al vencer): **51,9 %** · resultado medio con SL/TP tras costes: **-0.08 R** · no se distingue del azar todavía (z = 1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 446 | 52,5 % | -0.06 R |
| 52-55 % | 275 | 51,6 % | -0.12 R |
| 55-58 % | 36 | 47,2 % | -0.04 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 162 | 54,9 % | -0.10 R |
| Oro (XAU/USD) | 142 | 53,5 % | +0.03 R |
| GBP/JPY | 113 | 50,4 % | -0.17 R |
| SOL/USDT | 99 | 53,5 % | -0.04 R |
| USD/JPY | 59 | 47,5 % | +0.04 R |
| EUR/GBP | 55 | 52,7 % | -0.44 R |
| GBP/USD | 34 | 47,1 % | -0.23 R |
| AUD/USD | 33 | 51,5 % | +0.14 R |
| ETH/USDT | 32 | 40,6 % | +0.07 R |
| EUR/JPY | 21 | 52,4 % | -0.22 R |
| XRP/USDT | 4 | 75,0 % | +1.91 R |
| BTC/USDT | 3 | 33,3 % | -1.15 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 307 | 50,8 % | -0.12 R |
| 1h | 272 | 52,2 % | -0.10 R |
| 1d | 164 | 53,7 % | +0.08 R |
| 15m | 14 | 50,0 % | -0.49 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 311 | 53,7 % | -0.07 R |
| 12-24 h | 200 | 50,5 % | -0.15 R |
| 4-12 h | 187 | 50,3 % | -0.04 R |
| 1-2 días | 59 | 52,5 % | +0.02 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 373 | 51,5 % | -0.06 R |
| bollinger | 221 | 52,9 % | -0.01 R |
| estocastico | 75 | 58,7 % | -0.10 R |
| barrida | 33 | 45,5 % | -0.34 R |
| fibonacci | 17 | 35,3 % | -0.72 R |
| order_block | 11 | 63,6 % | +0.62 R |
| fvg | 10 | 60,0 % | -0.22 R |
| ruptura | 9 | 44,4 % | -0.15 R |
| choch | 6 | 66,7 % | -0.13 R |
| bos | 5 | 40,0 % | +0.56 R |
| supertrend | 4 | 50,0 % | -0.03 R |
| rsi | 1 | 0,0 % | -1.15 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 233 | 52,4 % | -0.00 R |
| 12-16 h | 113 | 48,7 % | -0.23 R |
| 00-04 h | 109 | 55,0 % | +0.16 R |
| 08-12 h | 109 | 51,4 % | -0.20 R |
| 20-24 h | 97 | 57,7 % | -0.21 R |
| 16-20 h | 96 | 45,8 % | -0.08 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 313 | 50,8 % | -0.12 R |
| lateral (<20) | 277 | 56,0 % | -0.09 R |
| débil (20-25) | 167 | 47,3 % | +0.02 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 458 | 49,6 % | -0.13 R |
| baja | 158 | 58,2 % | +0.10 R |
| alta | 141 | 52,5 % | -0.09 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 272 | 55,1 % | +0.02 R |
| a favor | 267 | 47,2 % | -0.17 R |
| en contra | 218 | 53,7 % | -0.08 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 509 | 52,5 % | -0.10 R |
| en contra | 244 | 50,4 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 485 | 52,4 % | -0.09 R |
| a favor | 272 | 51,1 % | -0.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |
| 27/08 06:00 | Oro (XAU/USD) | 1d | COMPRAR | 4320 min | soportes | -5.74 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**121 señales** del 28/10/2026 al 25/11/2026. Acierto (precio a favor al vencer): **54,5 %** · resultado medio con SL/TP tras costes: **-0.25 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 80 | 53,8 % | -0.39 R |
| 52-55 % | 35 | 54,3 % | +0.01 R |
| 55-58 % | 6 | 66,7 % | -0.07 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 29 | 69,0 % | -0.04 R |
| EUR/JPY | 28 | 42,9 % | -0.44 R |
| BTC/USDT | 22 | 50,0 % | -0.23 R |
| USD/CHF | 12 | 50,0 % | -0.17 R |
| EUR/GBP | 7 | 57,1 % | -0.29 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| ETH/USDT | 5 | 60,0 % | -0.63 R |
| USD/CAD | 4 | 75,0 % | +0.15 R |
| GBP/JPY | 3 | 33,3 % | -1.22 R |
| SOL/USDT | 3 | 33,3 % | -0.31 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 66 | 63,6 % | -0.16 R |
| 15m | 41 | 48,8 % | -0.29 R |
| 1h | 14 | 28,6 % | -0.57 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 91 | 56,0 % | -0.13 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 10 | 50,0 % | -0.35 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 36 | 33,3 % | -0.45 R |
| soportes | 35 | 68,6 % | -0.10 R |
| estocastico | 18 | 55,6 % | -0.32 R |
| barrida | 13 | 46,2 % | -0.24 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 6 | 83,3 % | +0.21 R |
| order_block | 4 | 75,0 % | +0.15 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 35 | 68,6 % | -0.26 R |
| 08-12 h | 29 | 55,2 % | -0.04 R |
| 04-08 h | 18 | 38,9 % | -0.32 R |
| 20-24 h | 18 | 50,0 % | -0.12 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 9 | 55,6 % | -0.87 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 57 | 45,6 % | -0.17 R |
| lateral (<20) | 36 | 66,7 % | -0.25 R |
| débil (20-25) | 28 | 57,1 % | -0.42 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 68 | 52,9 % | -0.34 R |
| alta | 31 | 51,6 % | -0.30 R |
| baja | 22 | 63,6 % | +0.10 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 44 | 59,1 % | -0.28 R |
| sin tendencia | 41 | 61,0 % | -0.08 R |
| en contra | 36 | 41,7 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 87 | 50,6 % | -0.34 R |
| en contra | 34 | 64,7 % | -0.01 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 86 | 48,8 % | -0.30 R |
| a favor | 35 | 68,6 % | -0.13 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 25/11 09:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -0.90 % |
| 24/11 05:10 | ETH/USDT | 5m | VENDER | 100 min | estocastico | -0.61 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 16/11 22:50 | XRP/USDT | 5m | VENDER | 50 min | estocastico | -0.43 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 24/11 05:10 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -0.36 % |
| 19/11 09:35 | BTC/USDT | 5m | VENDER | 100 min | fibonacci | -0.34 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**47 señales** del 28/10/2026 al 24/11/2026. Acierto (precio a favor al vencer): **31,9 %** · resultado medio con SL/TP tras costes: **-0.57 R** · claramente peor que el azar (z = -2.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 24 | 33,3 % | -0.53 R |
| <52 % | 23 | 30,4 % | -0.61 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 17 | 41,2 % | -0.46 R |
| USD/CHF | 15 | 33,3 % | -0.28 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| EUR/GBP | 3 | 33,3 % | -1.15 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 36 | 33,3 % | -0.66 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 5 | 20,0 % | -1.11 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 25 | 28,0 % | -0.64 R |
| 4-12 h | 14 | 35,7 % | -0.31 R |
| 1-2 días | 5 | 60,0 % | — |
| 12-24 h | 3 | 0,0 % | -1.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 24 | 37,5 % | -0.51 R |
| estocastico | 19 | 36,8 % | -0.55 R |
| soportes | 6 | 16,7 % | -1.09 R |
| barrida | 2 | 50,0 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 10 | 30,0 % | -0.80 R |
| 00-04 h | 9 | 22,2 % | -1.06 R |
| 20-24 h | 9 | 44,4 % | +0.43 R |
| 16-20 h | 7 | 28,6 % | -0.36 R |
| 04-08 h | 6 | 33,3 % | -1.02 R |
| 08-12 h | 6 | 33,3 % | -0.48 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 35 | 34,3 % | -0.73 R |
| débil (20-25) | 7 | 14,3 % | -0.36 R |
| lateral (<20) | 5 | 40,0 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 35 | 28,6 % | -0.46 R |
| alta | 10 | 30,0 % | -1.04 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 31 | 22,6 % | -0.60 R |
| en contra | 10 | 60,0 % | -1.08 R |
| a favor | 6 | 33,3 % | +0.01 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 41 | 24,4 % | -0.64 R |
| en contra | 4 | 75,0 % | +0.24 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 40 | 30,0 % | -0.62 R |
| a favor | 7 | 42,9 % | -0.24 R |

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
