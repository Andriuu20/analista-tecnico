# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**940 señales** del 11/08/2025 al 12/11/2026. Acierto (precio a favor al vencer): **52,4 %** · resultado medio con SL/TP tras costes: **-0.10 R** · no se distingue del azar todavía (z = 1.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,7 % en 122 | después 51,7 % en 87 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 61,3 % en 106 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 65,9 % en 88 | después 42,6 % en 108 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 59,7 % en 144 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 555 | 52,3 % | -0.05 R |
| 52-55 % | 331 | 54,1 % | -0.14 R |
| 55-58 % | 52 | 44,2 % | -0.47 R |
| ≥58 % | 2 | 50,0 % | -1.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 209 | 56,9 % | -0.02 R |
| EUR/JPY | 177 | 45,2 % | -0.24 R |
| USD/CHF | 102 | 58,8 % | -0.02 R |
| EUR/GBP | 94 | 52,1 % | -0.19 R |
| Oro (XAU/USD) | 85 | 52,9 % | +0.05 R |
| GBP/JPY | 69 | 55,1 % | -0.09 R |
| XRP/USDT | 67 | 49,3 % | +0.03 R |
| BTC/USDT | 49 | 49,0 % | -0.29 R |
| SOL/USDT | 43 | 48,8 % | -0.40 R |
| EUR/USD | 28 | 42,9 % | -0.26 R |
| AUD/USD | 13 | 61,5 % | +0.07 R |
| USD/CAD | 4 | 100,0 % | +1.26 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 369 | 53,7 % | -0.06 R |
| 1h | 252 | 49,2 % | -0.13 R |
| 5m | 213 | 49,8 % | -0.20 R |
| 4h | 106 | 61,3 % | +0.01 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 464 | 51,3 % | -0.13 R |
| 2-4 h | 441 | 53,1 % | -0.07 R |
| 30-59 min | 35 | 60,0 % | -0.22 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 449 | 50,1 % | -0.16 R |
| velas | 156 | 60,3 % | +0.01 R |
| barrida | 79 | 65,8 % | +0.02 R |
| soportes | 78 | 52,6 % | -0.04 R |
| fibonacci | 49 | 44,9 % | -0.41 R |
| rsi | 44 | 52,3 % | -0.01 R |
| bos | 43 | 48,8 % | -0.03 R |
| estocastico | 33 | 39,4 % | -0.14 R |
| macd | 13 | 38,5 % | -0.42 R |
| divergencia | 4 | 50,0 % | +0.90 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 191 | 52,4 % | -0.21 R |
| 16-20 h | 184 | 51,6 % | -0.12 R |
| 08-12 h | 156 | 45,5 % | -0.21 R |
| 20-24 h | 149 | 61,1 % | -0.04 R |
| 00-04 h | 146 | 52,1 % | -0.15 R |
| 04-08 h | 114 | 52,6 % | +0.20 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 426 | 51,9 % | -0.15 R |
| lateral (<20) | 333 | 52,0 % | -0.07 R |
| débil (20-25) | 181 | 54,7 % | -0.07 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 530 | 52,1 % | -0.09 R |
| alta | 251 | 51,0 % | -0.16 R |
| baja | 159 | 56,0 % | -0.06 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 389 | 53,2 % | -0.06 R |
| sin tendencia | 372 | 53,2 % | -0.11 R |
| en contra | 179 | 49,2 % | -0.19 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 668 | 51,9 % | -0.14 R |
| en contra | 261 | 54,0 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 641 | 52,4 % | -0.13 R |
| a favor | 299 | 52,5 % | -0.04 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -2.33 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 12/06 16:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.73 % |
| 08/11 22:35 | XRP/USDT | 5m | COMPRAR | 100 min | bollinger | -1.45 % |
| 05/11 16:15 | XRP/USDT | 5m | COMPRAR | 100 min | bollinger | -1.44 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 08/07 02:00 | XRP/USDT | 1h | COMPRAR | 60 min | bollinger | -1.34 % |
| 09/11 06:45 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**906 señales** del 08/01/2021 al 09/11/2026. Acierto (precio a favor al vencer): **52,1 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = 1.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **GBP/JPY** | acierta | 63,0 % en 73 | después 51,0 % en 96 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 475 | 52,4 % | -0.04 R |
| 52-55 % | 392 | 52,6 % | -0.11 R |
| 55-58 % | 39 | 43,6 % | -0.20 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| GBP/JPY | 169 | 56,2 % | -0.13 R |
| USD/CHF | 157 | 57,3 % | -0.12 R |
| SOL/USDT | 137 | 54,7 % | +0.06 R |
| Oro (XAU/USD) | 114 | 51,8 % | -0.03 R |
| GBP/USD | 85 | 52,9 % | -0.12 R |
| ETH/USDT | 79 | 40,5 % | -0.20 R |
| EUR/GBP | 71 | 47,9 % | -0.16 R |
| AUD/USD | 39 | 51,3 % | +0.26 R |
| USD/JPY | 37 | 37,8 % | +0.01 R |
| EUR/JPY | 12 | 66,7 % | +0.15 R |
| XRP/USDT | 4 | 0,0 % | -1.07 R |
| BTC/USDT | 2 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 387 | 55,3 % | -0.09 R |
| 4h | 323 | 49,5 % | -0.13 R |
| 1d | 136 | 52,2 % | +0.03 R |
| 15m | 60 | 45,0 % | +0.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 302 | 50,3 % | -0.04 R |
| 12-24 h | 278 | 53,2 % | -0.13 R |
| 4-12 h | 262 | 51,5 % | -0.09 R |
| 1-2 días | 64 | 57,8 % | +0.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 349 | 51,6 % | -0.10 R |
| bollinger | 347 | 54,8 % | +0.00 R |
| barrida | 95 | 51,6 % | -0.19 R |
| estocastico | 76 | 50,0 % | -0.02 R |
| ruptura | 15 | 46,7 % | +0.28 R |
| choch | 12 | 66,7 % | +0.15 R |
| fibonacci | 7 | 42,9 % | -0.74 R |
| velas | 4 | 0,0 % | -0.78 R |
| order_block | 3 | 0,0 % | -0.35 R |
| supertrend | 2 | 50,0 % | -1.03 R |
| bos | 1 | 0,0 % | -0.25 R |
| divergencia | 1 | 0,0 % | -0.60 R |
| rsi | 1 | 0,0 % | -1.17 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 229 | 52,4 % | +0.03 R |
| 12-16 h | 158 | 52,5 % | -0.06 R |
| 00-04 h | 148 | 54,1 % | -0.09 R |
| 08-12 h | 145 | 51,0 % | -0.13 R |
| 16-20 h | 130 | 47,7 % | -0.17 R |
| 20-24 h | 96 | 55,2 % | -0.11 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 390 | 51,8 % | -0.04 R |
| lateral (<20) | 338 | 51,5 % | -0.10 R |
| débil (20-25) | 178 | 53,9 % | -0.11 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 493 | 51,1 % | -0.04 R |
| alta | 209 | 53,6 % | -0.10 R |
| baja | 204 | 52,9 % | -0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 340 | 53,2 % | -0.04 R |
| a favor | 335 | 47,8 % | -0.14 R |
| en contra | 231 | 56,7 % | -0.04 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 679 | 51,7 % | -0.10 R |
| en contra | 224 | 52,7 % | -0.00 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 617 | 51,5 % | -0.14 R |
| a favor | 289 | 53,3 % | +0.06 R |

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
**60 señales** del 28/10/2026 al 12/11/2026. Acierto (precio a favor al vencer): **55,0 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 0.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 41 | 61,0 % | -0.22 R |
| 52-55 % | 18 | 38,9 % | -0.03 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 20 | 70,0 % | -0.02 R |
| EUR/JPY | 19 | 42,1 % | -0.51 R |
| USD/CHF | 6 | 50,0 % | +0.34 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| BTC/USDT | 2 | 50,0 % | -0.05 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| XRP/USDT | 2 | 50,0 % | +0.28 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 30 | 60,0 % | -0.19 R |
| 15m | 28 | 50,0 % | -0.18 R |
| 1h | 2 | 50,0 % | -0.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 43 | 51,2 % | -0.11 R |
| 30-59 min | 14 | 57,1 % | -0.52 R |
| 2-4 h | 3 | 100,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 21 | 38,1 % | -0.39 R |
| soportes | 20 | 70,0 % | -0.02 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| barrida | 7 | 42,9 % | +0.13 R |
| rsi | 5 | 80,0 % | -0.28 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 21 | 76,2 % | +0.08 R |
| 20-24 h | 10 | 30,0 % | -0.35 R |
| 04-08 h | 8 | 50,0 % | -0.33 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |
| 16-20 h | 8 | 62,5 % | +0.19 R |
| 08-12 h | 5 | 20,0 % | -0.23 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 29 | 55,2 % | +0.02 R |
| débil (20-25) | 16 | 50,0 % | -0.45 R |
| lateral (<20) | 15 | 60,0 % | -0.27 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 34 | 52,9 % | -0.14 R |
| alta | 14 | 57,1 % | -0.27 R |
| baja | 12 | 58,3 % | -0.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 22 | 59,1 % | -0.26 R |
| sin tendencia | 21 | 57,1 % | -0.03 R |
| en contra | 17 | 47,1 % | -0.26 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 45 | 51,1 % | -0.23 R |
| en contra | 15 | 66,7 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 46 | 54,3 % | -0.19 R |
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
**21 señales** del 28/10/2026 al 11/11/2026. Acierto (precio a favor al vencer): **33,3 %** · resultado medio con SL/TP tras costes: **-0.21 R** · no se distingue del azar todavía (z = -1.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 13 | 30,8 % | -0.37 R |
| <52 % | 8 | 37,5 % | -0.06 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 8 | 37,5 % | -0.24 R |
| USD/CHF | 7 | 28,6 % | +0.11 R |
| GBP/JPY | 3 | 33,3 % | -1.05 R |
| ETH/USDT | 2 | 50,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 14 | 35,7 % | -0.37 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 1 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 10 | 40,0 % | -0.06 R |
| 2-5 días | 9 | 33,3 % | -0.03 R |
| 12-24 h | 2 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 10 | 40,0 % | -0.24 R |
| estocastico | 9 | 22,2 % | -0.06 R |
| barrida | 1 | 100,0 % | — |
| rsi | 1 | 0,0 % | -1.12 R |
| soportes | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 5 | 40,0 % | +1.89 R |
| 12-16 h | 5 | 40,0 % | -1.05 R |
| 00-04 h | 4 | 25,0 % | -1.09 R |
| 08-12 h | 3 | 33,3 % | -0.29 R |
| 16-20 h | 3 | 33,3 % | -1.02 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 12 | 41,7 % | -0.52 R |
| débil (20-25) | 6 | 16,7 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 15 | 26,7 % | -0.18 R |
| alta | 4 | 25,0 % | -1.12 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 16 | 37,5 % | -0.18 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 2 | 0,0 % | -1.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 19 | 26,3 % | -0.13 R |
| en contra | 2 | 100,0 % | -1.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 16 | 31,2 % | -0.13 R |
| a favor | 5 | 40,0 % | -1.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 06/11 21:00 | USD/CHF | 4h | VENDER | 4800 min | estocastico | -1.47 % |
| 30/10 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -0.54 % |
| 11/11 09:30 | USD/CHF | 15m | VENDER | 300 min | estocastico | -0.32 % |
| 30/10 01:00 | USD/CHF | 15m | COMPRAR | 300 min | rsi+estocastico | -0.13 % |
| 06/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -0.09 % |
