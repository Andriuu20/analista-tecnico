# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**937 señales** del 21/01/2025 al 14/11/2026. Acierto (precio a favor al vencer): **51,7 %** · resultado medio con SL/TP tras costes: **-0.12 R** · no se distingue del azar todavía (z = 1.0).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,4 % en 154 | después 46,0 % en 87 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 60,3 % en 151 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 61,1 % en 90 | después 49,1 % en 106 casos | ❔ no se repite |
| tendencia_txt = **en contra** | falla | 33,3 % en 45 | después 48,7 % en 158 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 58,8 % en 177 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 575 | 51,7 % | -0.08 R |
| 52-55 % | 325 | 52,0 % | -0.17 R |
| 55-58 % | 37 | 48,6 % | -0.29 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 241 | 55,2 % | -0.08 R |
| EUR/JPY | 139 | 46,0 % | -0.31 R |
| BTC/USDT | 88 | 48,9 % | -0.24 R |
| USD/CHF | 84 | 57,1 % | +0.08 R |
| XRP/USDT | 82 | 45,1 % | -0.02 R |
| SOL/USDT | 74 | 48,6 % | -0.26 R |
| EUR/GBP | 67 | 55,2 % | -0.22 R |
| Oro (XAU/USD) | 66 | 48,5 % | +0.00 R |
| GBP/JPY | 44 | 56,8 % | +0.04 R |
| ETH/USDT | 24 | 50,0 % | -0.48 R |
| AUD/USD | 14 | 64,3 % | -0.03 R |
| GBP/USD | 7 | 42,9 % | +0.32 R |
| USD/CAD | 7 | 71,4 % | +0.46 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 319 | 48,0 % | -0.18 R |
| 15m | 286 | 52,8 % | -0.05 R |
| 5m | 181 | 49,2 % | -0.23 R |
| 4h | 151 | 60,3 % | -0.01 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 520 | 53,1 % | -0.11 R |
| 1-2 h | 364 | 49,2 % | -0.15 R |
| 30-59 min | 53 | 54,7 % | -0.07 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 421 | 48,5 % | -0.19 R |
| velas | 182 | 57,7 % | -0.01 R |
| soportes | 83 | 47,0 % | -0.20 R |
| barrida | 70 | 61,4 % | +0.04 R |
| estocastico | 51 | 51,0 % | +0.05 R |
| bos | 45 | 48,9 % | -0.07 R |
| rsi | 45 | 57,8 % | -0.30 R |
| fibonacci | 27 | 40,7 % | -0.42 R |
| supertrend | 13 | 53,8 % | +0.23 R |
| divergencia | 4 | 50,0 % | +0.90 R |
| order_block | 2 | 50,0 % | -0.56 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 194 | 49,0 % | -0.12 R |
| 12-16 h | 188 | 51,6 % | -0.19 R |
| 00-04 h | 153 | 50,3 % | -0.18 R |
| 20-24 h | 150 | 55,3 % | -0.19 R |
| 08-12 h | 127 | 51,2 % | -0.14 R |
| 04-08 h | 125 | 53,6 % | +0.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 412 | 54,4 % | -0.13 R |
| lateral (<20) | 355 | 47,6 % | -0.08 R |
| débil (20-25) | 170 | 53,5 % | -0.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 512 | 51,2 % | -0.13 R |
| alta | 245 | 52,2 % | -0.09 R |
| baja | 180 | 52,2 % | -0.16 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 374 | 53,7 % | -0.03 R |
| sin tendencia | 360 | 53,1 % | -0.13 R |
| en contra | 203 | 45,3 % | -0.28 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 661 | 50,4 % | -0.16 R |
| en contra | 268 | 54,5 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 655 | 51,3 % | -0.13 R |
| a favor | 282 | 52,5 % | -0.10 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -2.33 % |
| 23/09 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.09 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 13/11 03:15 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -2.00 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 13/11 06:50 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -1.79 % |
| 14/10 12:00 | ETH/USDT | 15m | COMPRAR | 225 min | estocastico | -1.76 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**827 señales** del 08/01/2021 al 11/11/2026. Acierto (precio a favor al vencer): **53,2 %** · resultado medio con SL/TP tras costes: **-0.08 R** · no se distingue del azar todavía (z = 1.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 408 | 54,2 % | -0.06 R |
| 52-55 % | 367 | 52,9 % | -0.11 R |
| 55-58 % | 52 | 48,1 % | +0.01 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 159 | 56,6 % | -0.15 R |
| SOL/USDT | 132 | 56,1 % | -0.01 R |
| Oro (XAU/USD) | 114 | 51,8 % | -0.04 R |
| GBP/USD | 86 | 51,2 % | -0.10 R |
| GBP/JPY | 85 | 62,4 % | -0.08 R |
| ETH/USDT | 73 | 46,6 % | -0.03 R |
| EUR/GBP | 59 | 47,5 % | -0.21 R |
| USD/JPY | 41 | 51,2 % | +0.10 R |
| AUD/USD | 37 | 51,4 % | +0.23 R |
| EUR/JPY | 33 | 48,5 % | -0.45 R |
| XRP/USDT | 7 | 28,6 % | +0.06 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 327 | 55,7 % | -0.11 R |
| 4h | 294 | 52,4 % | -0.08 R |
| 1d | 136 | 52,2 % | +0.03 R |
| 15m | 70 | 47,1 % | -0.10 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 309 | 51,5 % | -0.04 R |
| 12-24 h | 238 | 53,8 % | -0.18 R |
| 4-12 h | 223 | 53,8 % | -0.04 R |
| 1-2 días | 57 | 57,9 % | +0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 309 | 53,4 % | -0.10 R |
| bollinger | 289 | 55,0 % | +0.02 R |
| estocastico | 103 | 51,5 % | -0.16 R |
| barrida | 92 | 52,2 % | -0.10 R |
| order_block | 14 | 57,1 % | +0.28 R |
| ruptura | 13 | 46,2 % | +0.18 R |
| fibonacci | 6 | 50,0 % | -0.70 R |
| choch | 5 | 60,0 % | -0.73 R |
| bos | 4 | 50,0 % | +0.16 R |
| velas | 4 | 0,0 % | -0.78 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 222 | 50,9 % | -0.03 R |
| 00-04 h | 133 | 56,4 % | -0.09 R |
| 08-12 h | 131 | 51,9 % | -0.24 R |
| 16-20 h | 128 | 50,0 % | -0.02 R |
| 12-16 h | 116 | 56,0 % | -0.12 R |
| 20-24 h | 97 | 56,7 % | +0.05 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 338 | 51,8 % | -0.06 R |
| lateral (<20) | 317 | 52,4 % | -0.10 R |
| débil (20-25) | 172 | 57,6 % | -0.05 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 458 | 51,3 % | -0.06 R |
| baja | 194 | 56,7 % | -0.04 R |
| alta | 175 | 54,3 % | -0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 306 | 51,0 % | -0.13 R |
| sin tendencia | 302 | 56,0 % | +0.08 R |
| en contra | 219 | 52,5 % | -0.22 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 605 | 52,9 % | -0.09 R |
| en contra | 218 | 53,7 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 537 | 52,7 % | -0.13 R |
| a favor | 290 | 54,1 % | +0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 19/05 02:00 | ETH/USDT | 4h | VENDER | 1200 min | soportes | -5.99 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**74 señales** del 28/10/2026 al 14/11/2026. Acierto (precio a favor al vencer): **52,7 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 0.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 49 | 59,2 % | -0.21 R |
| 52-55 % | 24 | 37,5 % | -0.05 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 25 | 72,0 % | +0.04 R |
| EUR/JPY | 21 | 38,1 % | -0.57 R |
| USD/CHF | 9 | 44,4 % | +0.17 R |
| BTC/USDT | 6 | 33,3 % | -0.05 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| XRP/USDT | 2 | 50,0 % | +0.28 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 35 | 62,9 % | -0.13 R |
| 15m | 33 | 45,5 % | -0.24 R |
| 1h | 6 | 33,3 % | -0.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 55 | 50,9 % | -0.10 R |
| 30-59 min | 15 | 53,3 % | -0.56 R |
| 2-4 h | 4 | 75,0 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 25 | 72,0 % | +0.04 R |
| bollinger | 24 | 33,3 % | -0.46 R |
| barrida | 10 | 40,0 % | +0.04 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| rsi | 8 | 62,5 % | -0.28 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 21 | 76,2 % | +0.08 R |
| 04-08 h | 12 | 41,7 % | -0.19 R |
| 08-12 h | 12 | 50,0 % | -0.10 R |
| 20-24 h | 11 | 27,3 % | -0.35 R |
| 16-20 h | 10 | 50,0 % | -0.09 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 36 | 50,0 % | +0.01 R |
| lateral (<20) | 21 | 61,9 % | -0.20 R |
| débil (20-25) | 17 | 47,1 % | -0.50 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 42 | 50,0 % | -0.22 R |
| alta | 19 | 52,6 % | -0.19 R |
| baja | 13 | 61,5 % | -0.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 26 | 61,5 % | -0.11 R |
| sin tendencia | 25 | 56,0 % | -0.11 R |
| en contra | 23 | 39,1 % | -0.36 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 54 | 48,1 % | -0.26 R |
| en contra | 20 | 65,0 % | +0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 56 | 50,0 % | -0.25 R |
| a favor | 18 | 61,1 % | +0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 12/11 16:45 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.23 % |
| 14/11 10:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.18 % |
| 30/10 21:55 | USD/JPY | 5m | VENDER | 100 min | soportes | -0.17 % |
| 09/11 07:15 | USD/CHF | 15m | COMPRAR | 75 min | estocastico+barrida | -0.16 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**26 señales** del 28/10/2026 al 13/11/2026. Acierto (precio a favor al vencer): **26,9 %** · resultado medio con SL/TP tras costes: **-0.05 R** · claramente peor que el azar (z = -2.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 16 | 25,0 % | +0.10 R |
| <52 % | 10 | 30,0 % | -0.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 10 | 30,0 % | +0.30 R |
| USD/CHF | 7 | 28,6 % | +0.11 R |
| ETH/USDT | 4 | 25,0 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -1.05 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 18 | 27,8 % | -0.04 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 12 | 25,0 % | +0.57 R |
| 4-12 h | 11 | 36,4 % | -0.18 R |
| 12-24 h | 3 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 12 | 33,3 % | +0.30 R |
| estocastico | 10 | 20,0 % | -0.06 R |
| barrida | 2 | 50,0 % | -1.02 R |
| soportes | 2 | 0,0 % | -1.06 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 20-24 h | 6 | 33,3 % | +1.17 R |
| 12-16 h | 6 | 33,3 % | -1.05 R |
| 16-20 h | 5 | 20,0 % | +0.98 R |
| 00-04 h | 5 | 20,0 % | -1.09 R |
| 08-12 h | 3 | 33,3 % | -0.29 R |
| 04-08 h | 1 | 0,0 % | — |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 17 | 29,4 % | -0.02 R |
| débil (20-25) | 6 | 16,7 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 20 | 20,0 % | +0.10 R |
| alta | 4 | 25,0 % | -1.07 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 21 | 28,6 % | +0.02 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 2 | 0,0 % | -1.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 23 | 21,7 % | -0.20 R |
| en contra | 3 | 66,7 % | +0.92 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 21 | 23,8 % | -0.13 R |
| a favor | 5 | 40,0 % | +0.30 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 10/11 17:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.39 % |
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 10/11 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.89 % |
| 12/11 13:00 | ETH/USDT | 4h | COMPRAR | 720 min | barrida | -3.71 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 10/11 21:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -3.22 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
| 06/11 21:00 | USD/CHF | 4h | VENDER | 4800 min | estocastico | -1.47 % |
