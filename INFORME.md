# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**648 señales** del 19/03/2026 al 07/11/2026. Acierto (precio a favor al vencer): **52,2 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 362 | 51,1 % | -0.20 R |
| 52-55 % | 242 | 55,8 % | -0.11 R |
| 55-58 % | 40 | 45,0 % | -0.32 R |
| ≥58 % | 4 | 0,0 % | -0.71 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 132 | 49,2 % | -0.17 R |
| USD/CHF | 120 | 59,2 % | +0.01 R |
| USD/JPY | 102 | 51,0 % | -0.18 R |
| Oro (XAU/USD) | 68 | 50,0 % | -0.41 R |
| BTC/USDT | 62 | 58,1 % | -0.13 R |
| EUR/GBP | 54 | 50,0 % | -0.24 R |
| XRP/USDT | 42 | 50,0 % | -0.18 R |
| GBP/JPY | 36 | 52,8 % | -0.12 R |
| SOL/USDT | 31 | 41,9 % | -0.46 R |
| USD/CAD | 1 | 0,0 % | -1.16 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 239 | 51,5 % | -0.13 R |
| 1h | 230 | 48,7 % | -0.20 R |
| 15m | 134 | 58,2 % | -0.13 R |
| 4h | 45 | 55,6 % | -0.43 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 314 | 53,2 % | -0.11 R |
| 2-4 h | 253 | 50,2 % | -0.28 R |
| 30-59 min | 81 | 54,3 % | -0.15 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 330 | 50,9 % | -0.19 R |
| soportes | 80 | 50,0 % | -0.39 R |
| barrida | 72 | 62,5 % | -0.01 R |
| rsi | 46 | 56,5 % | -0.09 R |
| estocastico | 44 | 52,3 % | +0.05 R |
| velas | 37 | 56,8 % | -0.10 R |
| bos | 36 | 52,8 % | -0.05 R |
| supertrend | 4 | 25,0 % | -1.18 R |
| fibonacci | 3 | 33,3 % | -1.12 R |
| choch | 2 | 0,0 % | -1.21 R |
| divergencia | 1 | 0,0 % | -1.12 R |
| medias | 1 | 0,0 % | -1.09 R |
| ruptura | 1 | 0,0 % | -1.16 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 154 | 52,6 % | -0.19 R |
| 12-16 h | 119 | 51,3 % | -0.23 R |
| 08-12 h | 104 | 47,1 % | -0.20 R |
| 20-24 h | 94 | 55,3 % | -0.35 R |
| 00-04 h | 91 | 57,1 % | -0.07 R |
| 04-08 h | 86 | 50,0 % | +0.01 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 339 | 55,5 % | -0.11 R |
| lateral (<20) | 188 | 46,8 % | -0.28 R |
| débil (20-25) | 121 | 51,2 % | -0.22 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 354 | 49,2 % | -0.14 R |
| alta | 213 | 55,4 % | -0.14 R |
| baja | 81 | 56,8 % | -0.43 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 249 | 50,6 % | -0.27 R |
| a favor | 245 | 53,9 % | -0.16 R |
| en contra | 154 | 51,9 % | -0.06 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 501 | 52,9 % | -0.16 R |
| en contra | 141 | 48,9 % | -0.25 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 478 | 53,6 % | -0.19 R |
| a favor | 170 | 48,2 % | -0.16 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 29/10 15:25 | BTC/USDT | 5m | VENDER | 75 min | estocastico | -1.64 % |
| 21/08 08:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.60 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 15/10 06:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -1.23 % |
| 05/11 16:15 | XRP/USDT | 5m | COMPRAR | 50 min | bollinger | -1.20 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**828 señales** del 08/01/2021 al 06/11/2026. Acierto (precio a favor al vencer): **53,0 %** · resultado medio con SL/TP tras costes: **-0.11 R** · no se distingue del azar todavía (z = 1.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 65,3 % en 72 | después 52,1 % en 96 casos | ❔ no se repite |
| plazo = **4-12 h** | acierta | 64,4 % en 87 | después 47,0 % en 132 casos | ❔ no se repite |
| franja = **04-08 h** | acierta | 59,3 % en 145 | después 43,6 % en 78 casos | ❔ no se repite |
| franja = **20-24 h** | acierta | 66,0 % en 47 | después 48,9 % en 45 casos | ❔ no se repite |
| tendencia_txt = **sin tendencia** | acierta | 60,3 % en 146 | después 53,1 % en 177 casos | ❔ no se repite |
| confianza_tramo = **52-55 %** | acierta | 58,5 % en 207 | después 52,8 % en 144 casos | ❔ no se repite |
| estrategia = **bollinger** | acierta | 59,5 % en 163 | después 51,8 % en 166 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 435 | 49,7 % | -0.12 R |
| 52-55 % | 351 | 56,1 % | -0.14 R |
| 55-58 % | 42 | 61,9 % | +0.31 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 168 | 57,7 % | -0.12 R |
| USD/CHF | 147 | 54,4 % | -0.14 R |
| SOL/USDT | 123 | 53,7 % | -0.02 R |
| Oro (XAU/USD) | 115 | 53,0 % | +0.06 R |
| ETH/USDT | 76 | 44,7 % | -0.18 R |
| GBP/USD | 73 | 56,2 % | -0.05 R |
| EUR/GBP | 48 | 50,0 % | -0.31 R |
| AUD/USD | 28 | 46,4 % | +0.06 R |
| EUR/JPY | 24 | 66,7 % | -0.23 R |
| USD/JPY | 18 | 22,2 % | -0.86 R |
| XRP/USDT | 7 | 28,6 % | -0.63 R |
| EUR/USD | 1 | 100,0 % | +2.94 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 361 | 55,1 % | -0.19 R |
| 4h | 300 | 52,0 % | -0.13 R |
| 1d | 137 | 53,3 % | +0.11 R |
| 15m | 30 | 36,7 % | +0.13 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 279 | 52,0 % | -0.04 R |
| 12-24 h | 266 | 52,3 % | -0.21 R |
| 4-12 h | 219 | 53,9 % | -0.12 R |
| 1-2 días | 64 | 57,8 % | +0.10 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 329 | 55,6 % | -0.05 R |
| soportes | 312 | 51,6 % | -0.14 R |
| barrida | 85 | 51,8 % | -0.16 R |
| estocastico | 66 | 53,0 % | +0.04 R |
| choch | 24 | 66,7 % | -0.23 R |
| fibonacci | 5 | 60,0 % | -0.03 R |
| ruptura | 4 | 0,0 % | -1.05 R |
| order_block | 3 | 0,0 % | -1.05 R |
| bos | 2 | 0,0 % | -0.65 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 223 | 53,8 % | +0.06 R |
| 08-12 h | 145 | 50,3 % | -0.28 R |
| 00-04 h | 131 | 56,5 % | -0.08 R |
| 16-20 h | 120 | 48,3 % | -0.18 R |
| 12-16 h | 117 | 52,1 % | -0.13 R |
| 20-24 h | 92 | 57,6 % | -0.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 350 | 52,6 % | -0.10 R |
| lateral (<20) | 310 | 53,5 % | -0.15 R |
| débil (20-25) | 168 | 53,0 % | -0.05 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 458 | 51,7 % | -0.09 R |
| baja | 193 | 53,9 % | -0.12 R |
| alta | 177 | 55,4 % | -0.14 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 323 | 56,3 % | -0.10 R |
| a favor | 281 | 48,8 % | -0.13 R |
| en contra | 224 | 53,6 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 615 | 53,2 % | -0.11 R |
| en contra | 209 | 51,7 % | -0.11 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 560 | 51,1 % | -0.13 R |
| a favor | 268 | 57,1 % | -0.06 R |

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
| 19/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -5.99 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**40 señales** del 28/10/2026 al 09/11/2026. Acierto (precio a favor al vencer): **60,0 %** · resultado medio con SL/TP tras costes: **-0.32 R** · no se distingue del azar todavía (z = 1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 28 | 64,3 % | -0.36 R |
| 52-55 % | 11 | 45,5 % | -0.10 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 15 | 66,7 % | +0.01 R |
| EUR/JPY | 12 | 50,0 % | -0.79 R |
| USD/CHF | 3 | 66,7 % | +0.34 R |
| EUR/GBP | 3 | 33,3 % | -0.37 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| BTC/USDT | 1 | 100,0 % | — |
| ETH/USDT | 1 | 100,0 % | -1.21 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 22 | 59,1 % | -0.30 R |
| 15m | 17 | 58,8 % | -0.35 R |
| 1h | 1 | 100,0 % | — |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 27 | 51,9 % | -0.26 R |
| 30-59 min | 10 | 70,0 % | -0.71 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 15 | 66,7 % | +0.01 R |
| bollinger | 11 | 36,4 % | -0.75 R |
| estocastico | 7 | 71,4 % | -0.47 R |
| barrida | 4 | 50,0 % | -0.15 R |
| rsi | 4 | 100,0 % | -0.43 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 15 | 80,0 % | -0.05 R |
| 20-24 h | 10 | 30,0 % | -0.49 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 5 | 60,0 % | -0.09 R |
| 04-08 h | 1 | 100,0 % | -1.13 R |
| 08-12 h | 1 | 100,0 % | +1.91 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 21 | 66,7 % | +0.02 R |
| lateral (<20) | 10 | 50,0 % | -0.79 R |
| débil (20-25) | 9 | 55,6 % | -0.76 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 22 | 59,1 % | -0.16 R |
| alta | 12 | 66,7 % | -0.19 R |
| baja | 6 | 50,0 % | -1.21 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 15 | 66,7 % | -0.27 R |
| en contra | 13 | 53,8 % | -0.33 R |
| sin tendencia | 12 | 58,3 % | -0.40 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 28 | 60,7 % | -0.36 R |
| en contra | 12 | 58,3 % | -0.23 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 28 | 60,7 % | -0.33 R |
| a favor | 12 | 58,3 % | -0.31 R |

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
**14 señales** del 28/10/2026 al 06/11/2026. Acierto (precio a favor al vencer): **35,7 %** · resultado medio con SL/TP tras costes: **-0.26 R** · no se distingue del azar todavía (z = -1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 9 | 44,4 % | -0.24 R |
| <52 % | 5 | 20,0 % | -0.29 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 7 | 42,9 % | -0.24 R |
| USD/CHF | 3 | 0,0 % | +0.10 R |
| GBP/JPY | 2 | 50,0 % | — |
| ETH/USDT | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 10 | 50,0 % | -0.24 R |
| 15m | 3 | 0,0 % | +0.10 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 6 | 33,3 % | +0.10 R |
| 2-5 días | 6 | 50,0 % | -0.03 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 7 | 57,1 % | -0.03 R |
| estocastico | 5 | 0,0 % | -0.29 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 4 | 50,0 % | +2.14 R |
| 00-04 h | 3 | 0,0 % | -1.07 R |
| 12-16 h | 3 | 66,7 % | -1.05 R |
| 16-20 h | 2 | 50,0 % | -1.02 R |
| 04-08 h | 1 | 0,0 % | — |
| 08-12 h | 1 | 0,0 % | -1.06 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| débil (20-25) | 6 | 16,7 % | -0.45 R |
| fuerte (≥25) | 5 | 60,0 % | -1.12 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 11 | 27,3 % | +0.02 R |
| alta | 2 | 50,0 % | -1.12 R |
| baja | 1 | 100,0 % | -1.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 11 | 36,4 % | -0.48 R |
| a favor | 3 | 33,3 % | +1.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 13 | 30,8 % | -0.26 R |
| en contra | 1 | 100,0 % | — |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 11 | 27,3 % | -0.14 R |
| a favor | 3 | 66,7 % | -1.06 R |

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
| 05/11 22:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.03 % |
| 06/11 21:00 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.00 % |
