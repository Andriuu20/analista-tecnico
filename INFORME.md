# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**1045 señales** del 27/01/2025 al 16/11/2026. Acierto (precio a favor al vencer): **52,3 %** · resultado medio con SL/TP tras costes: **-0.13 R** · no se distingue del azar todavía (z = 1.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,7 % en 150 | después 48,6 % en 111 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 60,1 % en 158 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 61,3 % en 106 | después 45,5 % en 121 casos | ❔ no se repite |
| tendencia_txt = **a favor** | acierta | 57,5 % en 240 | después 54,4 % en 182 casos | ✅ confirmado |
| zona_txt = **en contra** | acierta | 59,5 % en 190 | después 52,7 % en 112 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 59,6 % en 156 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 619 | 51,7 % | -0.11 R |
| 52-55 % | 377 | 54,4 % | -0.13 R |
| 55-58 % | 45 | 46,7 % | -0.32 R |
| ≥58 % | 4 | 25,0 % | +0.15 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 261 | 55,6 % | -0.07 R |
| EUR/JPY | 139 | 46,8 % | -0.28 R |
| BTC/USDT | 98 | 45,9 % | -0.27 R |
| SOL/USDT | 92 | 53,3 % | -0.23 R |
| XRP/USDT | 86 | 48,8 % | -0.09 R |
| USD/CHF | 84 | 57,1 % | +0.03 R |
| EUR/GBP | 82 | 48,8 % | -0.18 R |
| GBP/JPY | 79 | 57,0 % | -0.07 R |
| Oro (XAU/USD) | 66 | 56,1 % | +0.00 R |
| USD/CAD | 30 | 53,3 % | -0.13 R |
| AUD/USD | 14 | 64,3 % | -0.03 R |
| ETH/USDT | 7 | 42,9 % | -0.25 R |
| GBP/USD | 7 | 42,9 % | +0.32 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 373 | 50,4 % | -0.12 R |
| 5m | 260 | 49,6 % | -0.23 R |
| 15m | 254 | 53,1 % | -0.10 R |
| 4h | 158 | 60,1 % | +0.00 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 523 | 54,1 % | -0.10 R |
| 1-2 h | 455 | 50,5 % | -0.15 R |
| 30-59 min | 67 | 50,7 % | -0.15 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 472 | 48,9 % | -0.18 R |
| velas | 158 | 59,5 % | +0.05 R |
| soportes | 134 | 49,3 % | -0.34 R |
| barrida | 78 | 59,0 % | -0.02 R |
| estocastico | 56 | 50,0 % | +0.09 R |
| bos | 54 | 55,6 % | +0.16 R |
| rsi | 46 | 60,9 % | -0.18 R |
| fibonacci | 36 | 52,8 % | -0.27 R |
| order_block | 17 | 52,9 % | -0.20 R |
| divergencia | 4 | 50,0 % | -0.09 R |
| medias | 1 | 100,0 % | +2.86 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 219 | 48,9 % | -0.17 R |
| 12-16 h | 203 | 51,2 % | -0.21 R |
| 00-04 h | 172 | 54,1 % | -0.10 R |
| 20-24 h | 166 | 54,8 % | -0.17 R |
| 08-12 h | 146 | 56,2 % | -0.14 R |
| 04-08 h | 139 | 50,4 % | +0.10 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 456 | 53,9 % | -0.14 R |
| lateral (<20) | 387 | 50,9 % | -0.07 R |
| débil (20-25) | 202 | 51,5 % | -0.21 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 587 | 52,1 % | -0.10 R |
| alta | 270 | 53,0 % | -0.09 R |
| baja | 188 | 52,1 % | -0.27 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 427 | 51,1 % | -0.15 R |
| a favor | 422 | 56,2 % | -0.02 R |
| en contra | 196 | 46,9 % | -0.33 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 734 | 50,3 % | -0.19 R |
| en contra | 302 | 57,0 % | +0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 722 | 51,8 % | -0.12 R |
| a favor | 323 | 53,6 % | -0.14 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -2.33 % |
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 23/09 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.09 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 13/11 03:15 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -2.00 % |
| 13/11 06:25 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -1.86 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**931 señales** del 08/01/2021 al 13/11/2026. Acierto (precio a favor al vencer): **52,0 %** · resultado medio con SL/TP tras costes: **-0.09 R** · no se distingue del azar todavía (z = 1.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | acierta | 60,4 % en 164 | después 51,2 % en 258 casos | ❔ no se repite |
| volatilidad = **alta** | acierta | 60,4 % en 101 | después 48,5 % en 99 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 485 | 53,8 % | -0.07 R |
| 52-55 % | 403 | 50,9 % | -0.11 R |
| 55-58 % | 43 | 41,9 % | -0.00 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 175 | 55,4 % | -0.16 R |
| GBP/JPY | 151 | 55,6 % | -0.07 R |
| SOL/USDT | 113 | 54,0 % | -0.03 R |
| Oro (XAU/USD) | 112 | 51,8 % | -0.01 R |
| GBP/USD | 88 | 53,4 % | -0.13 R |
| EUR/GBP | 81 | 46,9 % | -0.17 R |
| USD/JPY | 72 | 47,2 % | +0.02 R |
| ETH/USDT | 62 | 41,9 % | -0.17 R |
| AUD/USD | 39 | 51,3 % | +0.26 R |
| EUR/JPY | 29 | 55,2 % | -0.45 R |
| XRP/USDT | 6 | 33,3 % | +0.25 R |
| EUR/USD | 2 | 50,0 % | +0.97 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 422 | 54,7 % | -0.08 R |
| 4h | 329 | 48,9 % | -0.14 R |
| 1d | 134 | 52,2 % | +0.05 R |
| 15m | 46 | 47,8 % | -0.15 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 310 | 49,7 % | -0.04 R |
| 4-12 h | 300 | 51,0 % | -0.13 R |
| 12-24 h | 264 | 54,5 % | -0.12 R |
| 1-2 días | 57 | 57,9 % | +0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 355 | 52,4 % | -0.04 R |
| soportes | 350 | 52,0 % | -0.09 R |
| barrida | 91 | 52,7 % | -0.16 R |
| estocastico | 89 | 53,9 % | -0.18 R |
| ruptura | 16 | 43,8 % | +0.20 R |
| velas | 12 | 25,0 % | -0.27 R |
| order_block | 8 | 62,5 % | +0.44 R |
| bos | 7 | 42,9 % | +0.10 R |
| choch | 7 | 57,1 % | -0.24 R |
| fibonacci | 5 | 60,0 % | -0.63 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 231 | 50,6 % | +0.01 R |
| 08-12 h | 160 | 49,4 % | -0.23 R |
| 12-16 h | 149 | 55,0 % | -0.09 R |
| 00-04 h | 143 | 54,5 % | -0.07 R |
| 16-20 h | 135 | 48,9 % | -0.07 R |
| 20-24 h | 113 | 54,9 % | -0.10 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 380 | 51,8 % | -0.02 R |
| lateral (<20) | 351 | 51,9 % | -0.11 R |
| débil (20-25) | 200 | 52,5 % | -0.16 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 522 | 50,4 % | -0.06 R |
| baja | 209 | 53,6 % | -0.11 R |
| alta | 200 | 54,5 % | -0.12 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 354 | 48,6 % | -0.16 R |
| sin tendencia | 347 | 53,9 % | +0.01 R |
| en contra | 230 | 54,3 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 683 | 52,0 % | -0.11 R |
| en contra | 243 | 51,9 % | -0.02 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 614 | 51,8 % | -0.13 R |
| a favor | 317 | 52,4 % | +0.00 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 17/08 18:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -18.07 % |
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 13/11 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -6.32 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**82 señales** del 28/10/2026 al 16/11/2026. Acierto (precio a favor al vencer): **51,2 %** · resultado medio con SL/TP tras costes: **-0.24 R** · no se distingue del azar todavía (z = 0.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 57 | 56,1 % | -0.29 R |
| 52-55 % | 24 | 37,5 % | -0.09 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 26 | 69,2 % | +0.02 R |
| EUR/JPY | 21 | 38,1 % | -0.57 R |
| USD/CHF | 9 | 44,4 % | +0.17 R |
| BTC/USDT | 9 | 33,3 % | -0.47 R |
| XRP/USDT | 6 | 50,0 % | -0.57 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 39 | 59,0 % | -0.18 R |
| 15m | 34 | 47,1 % | -0.27 R |
| 1h | 9 | 33,3 % | -0.47 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 59 | 49,2 % | -0.17 R |
| 30-59 min | 17 | 52,9 % | -0.59 R |
| 2-4 h | 6 | 66,7 % | +0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 27 | 33,3 % | -0.51 R |
| soportes | 26 | 69,2 % | +0.02 R |
| rsi | 11 | 54,5 % | -0.53 R |
| barrida | 10 | 40,0 % | +0.04 R |
| estocastico | 10 | 50,0 % | -0.48 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 24 | 75,0 % | +0.02 R |
| 04-08 h | 13 | 38,5 % | -0.40 R |
| 20-24 h | 13 | 30,8 % | -0.32 R |
| 08-12 h | 12 | 50,0 % | -0.09 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 42 | 47,6 % | -0.14 R |
| lateral (<20) | 23 | 60,9 % | -0.24 R |
| débil (20-25) | 17 | 47,1 % | -0.50 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 45 | 51,1 % | -0.26 R |
| alta | 23 | 47,8 % | -0.34 R |
| baja | 14 | 57,1 % | -0.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 28 | 39,3 % | -0.47 R |
| sin tendencia | 28 | 53,6 % | -0.16 R |
| a favor | 26 | 61,5 % | -0.11 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 60 | 46,7 % | -0.33 R |
| en contra | 22 | 63,6 % | -0.03 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 63 | 47,6 % | -0.31 R |
| a favor | 19 | 63,2 % | -0.03 R |

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
**29 señales** del 28/10/2026 al 14/11/2026. Acierto (precio a favor al vencer): **24,1 %** · resultado medio con SL/TP tras costes: **-0.11 R** · claramente peor que el azar (z = -2.8).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 17 | 23,5 % | -0.04 R |
| <52 % | 12 | 25,0 % | -0.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 11 | 27,3 % | +0.11 R |
| USD/CHF | 8 | 25,0 % | +0.11 R |
| ETH/USDT | 5 | 20,0 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -1.05 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 21 | 23,8 % | -0.14 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 15 | 20,0 % | +0.30 R |
| 4-12 h | 11 | 36,4 % | -0.18 R |
| 12-24 h | 3 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 14 | 28,6 % | +0.30 R |
| estocastico | 11 | 18,2 % | -0.18 R |
| barrida | 2 | 50,0 % | -1.02 R |
| soportes | 2 | 0,0 % | -1.06 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 6 | 16,7 % | -1.09 R |
| 12-16 h | 6 | 33,3 % | -1.05 R |
| 20-24 h | 6 | 33,3 % | +1.17 R |
| 16-20 h | 5 | 20,0 % | +0.98 R |
| 04-08 h | 3 | 0,0 % | -1.02 R |
| 08-12 h | 3 | 33,3 % | -0.29 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 19 | 26,3 % | -0.16 R |
| débil (20-25) | 7 | 14,3 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 21 | 19,0 % | +0.01 R |
| alta | 6 | 16,7 % | -1.07 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 24 | 25,0 % | -0.06 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 2 | 0,0 % | -1.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 26 | 19,2 % | -0.25 R |
| en contra | 3 | 66,7 % | +0.92 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 24 | 20,8 % | -0.20 R |
| a favor | 5 | 40,0 % | +0.30 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 10/11 17:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.39 % |
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 14/11 05:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.92 % |
| 10/11 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.89 % |
| 12/11 13:00 | ETH/USDT | 4h | COMPRAR | 720 min | barrida | -3.71 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 10/11 21:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -3.22 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
