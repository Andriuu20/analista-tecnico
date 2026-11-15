# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**922 señales** del 21/01/2025 al 15/11/2026. Acierto (precio a favor al vencer): **51,7 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 1.1).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 60,4 % en 154 | después 46,0 % en 87 casos | ❔ no se repite |
| temporalidad = **4h** | acierta | 59,8 % en 164 | pocos casos en la segunda mitad | ⏳ faltan datos |
| tendencia_txt = **a favor** | acierta | 56,9 % en 216 | después 51,6 % en 155 casos | ❔ no se repite |
| tendencia_txt = **en contra** | falla | 33,3 % en 39 | después 47,7 % en 151 casos | ❔ no se repite |
| zona_txt = **en contra** | acierta | 59,8 % en 179 | después 46,7 % en 75 casos | ❔ no se repite |
| estrategia = **velas** | acierta | 59,4 % en 160 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 558 | 50,7 % | -0.11 R |
| 52-55 % | 326 | 53,1 % | -0.18 R |
| 55-58 % | 36 | 55,6 % | -0.23 R |
| ≥58 % | 2 | 50,0 % | +0.15 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 241 | 55,2 % | -0.08 R |
| EUR/JPY | 139 | 46,0 % | -0.31 R |
| BTC/USDT | 93 | 47,3 % | -0.20 R |
| USD/CHF | 84 | 56,0 % | +0.00 R |
| SOL/USDT | 80 | 47,5 % | -0.28 R |
| EUR/GBP | 67 | 55,2 % | -0.22 R |
| Oro (XAU/USD) | 66 | 56,1 % | +0.00 R |
| XRP/USDT | 56 | 41,1 % | -0.18 R |
| GBP/JPY | 44 | 56,8 % | +0.04 R |
| ETH/USDT | 24 | 50,0 % | -0.31 R |
| AUD/USD | 14 | 64,3 % | -0.03 R |
| GBP/USD | 7 | 42,9 % | +0.32 R |
| USD/CAD | 7 | 71,4 % | +0.46 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 329 | 48,9 % | -0.10 R |
| 15m | 254 | 52,4 % | -0.11 R |
| 5m | 175 | 48,6 % | -0.30 R |
| 4h | 164 | 59,8 % | -0.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 530 | 53,8 % | -0.12 R |
| 1-2 h | 354 | 48,3 % | -0.16 R |
| 30-59 min | 38 | 55,3 % | -0.18 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 409 | 48,2 % | -0.19 R |
| velas | 162 | 58,6 % | -0.04 R |
| soportes | 96 | 47,9 % | -0.32 R |
| barrida | 70 | 61,4 % | +0.04 R |
| estocastico | 53 | 45,3 % | -0.14 R |
| bos | 52 | 55,8 % | +0.20 R |
| rsi | 51 | 56,9 % | -0.38 R |
| fibonacci | 28 | 39,3 % | -0.30 R |
| divergencia | 4 | 50,0 % | +0.90 R |
| order_block | 2 | 50,0 % | -0.56 R |
| medias | 1 | 100,0 % | +2.86 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 196 | 46,9 % | -0.17 R |
| 12-16 h | 183 | 53,0 % | -0.21 R |
| 20-24 h | 151 | 57,6 % | -0.15 R |
| 00-04 h | 150 | 51,3 % | -0.19 R |
| 08-12 h | 122 | 50,8 % | -0.19 R |
| 04-08 h | 120 | 51,7 % | +0.15 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 414 | 54,8 % | -0.16 R |
| lateral (<20) | 341 | 47,5 % | -0.09 R |
| débil (20-25) | 167 | 52,7 % | -0.20 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 506 | 51,8 % | -0.13 R |
| alta | 243 | 51,4 % | -0.09 R |
| baja | 173 | 52,0 % | -0.22 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 371 | 54,7 % | -0.04 R |
| sin tendencia | 361 | 52,4 % | -0.15 R |
| en contra | 190 | 44,7 % | -0.30 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 660 | 50,0 % | -0.20 R |
| en contra | 254 | 55,9 % | +0.00 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 649 | 51,3 % | -0.14 R |
| a favor | 273 | 52,7 % | -0.13 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 19/08 20:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -5.31 % |
| 25/08 00:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -3.12 % |
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 10/11 18:35 | XRP/USDT | 5m | VENDER | 100 min | bollinger | -2.33 % |
| 23/09 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.09 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 22/08 01:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -2.04 % |
| 13/11 03:15 | XRP/USDT | 5m | COMPRAR | 100 min | rsi | -2.00 % |
| 20/07 16:00 | SOL/USDT | 1h | VENDER | 120 min | fibonacci | -1.98 % |
| 07/10 02:45 | SOL/USDT | 15m | COMPRAR | 150 min | estocastico | -1.98 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**813 señales** del 08/01/2021 al 11/11/2026. Acierto (precio a favor al vencer): **53,0 %** · resultado medio con SL/TP tras costes: **-0.07 R** · no se distingue del azar todavía (z = 1.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| temporalidad = **1h** | acierta | 58,5 % en 142 | después 52,3 % en 193 casos | ❔ no se repite |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 409 | 56,0 % | -0.01 R |
| 52-55 % | 361 | 50,7 % | -0.15 R |
| 55-58 % | 43 | 44,2 % | -0.04 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 157 | 55,4 % | -0.15 R |
| SOL/USDT | 118 | 56,8 % | +0.03 R |
| Oro (XAU/USD) | 112 | 52,7 % | -0.02 R |
| GBP/USD | 86 | 51,2 % | -0.10 R |
| GBP/JPY | 85 | 62,4 % | -0.08 R |
| ETH/USDT | 67 | 43,3 % | -0.16 R |
| EUR/GBP | 59 | 47,5 % | -0.21 R |
| USD/JPY | 42 | 54,8 % | +0.16 R |
| AUD/USD | 38 | 52,6 % | +0.30 R |
| EUR/JPY | 33 | 48,5 % | -0.45 R |
| XRP/USDT | 15 | 33,3 % | -0.07 R |
| BTC/USDT | 1 | 0,0 % | -1.02 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 335 | 54,9 % | -0.09 R |
| 4h | 290 | 52,4 % | -0.11 R |
| 1d | 134 | 53,0 % | +0.04 R |
| 15m | 54 | 44,4 % | -0.09 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 310 | 51,6 % | -0.05 R |
| 12-24 h | 237 | 54,0 % | -0.14 R |
| 4-12 h | 209 | 52,6 % | -0.07 R |
| 1-2 días | 57 | 57,9 % | +0.05 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 307 | 53,4 % | -0.09 R |
| bollinger | 280 | 54,6 % | +0.00 R |
| estocastico | 97 | 51,5 % | -0.17 R |
| barrida | 92 | 52,2 % | -0.10 R |
| ruptura | 14 | 50,0 % | +0.38 R |
| order_block | 14 | 50,0 % | +0.00 R |
| fibonacci | 6 | 50,0 % | -0.70 R |
| bos | 5 | 40,0 % | +0.56 R |
| choch | 5 | 60,0 % | -0.73 R |
| velas | 4 | 0,0 % | -0.78 R |
| supertrend | 2 | 50,0 % | -1.03 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 221 | 51,1 % | -0.00 R |
| 16-20 h | 131 | 49,6 % | -0.08 R |
| 00-04 h | 127 | 54,3 % | -0.08 R |
| 08-12 h | 124 | 53,2 % | -0.23 R |
| 12-16 h | 111 | 56,8 % | -0.06 R |
| 20-24 h | 99 | 55,6 % | -0.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 334 | 52,1 % | -0.06 R |
| lateral (<20) | 310 | 52,6 % | -0.05 R |
| débil (20-25) | 169 | 55,6 % | -0.14 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 448 | 51,8 % | -0.07 R |
| baja | 194 | 55,2 % | -0.05 R |
| alta | 171 | 53,8 % | -0.11 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 304 | 50,0 % | -0.15 R |
| sin tendencia | 297 | 54,5 % | +0.06 R |
| en contra | 212 | 55,2 % | -0.15 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 592 | 52,4 % | -0.09 R |
| en contra | 217 | 54,4 % | -0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 523 | 51,8 % | -0.14 R |
| a favor | 290 | 55,2 % | +0.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 18/08 02:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -22.79 % |
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 30/01 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -11.95 % |
| 19/08 22:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.28 % |
| 29/06 14:00 | SOL/USDT | 4h | VENDER | 4800 min | barrida | -9.21 % |
| 25/08 06:00 | SOL/USDT | 4h | VENDER | 3600 min | estocastico | -9.14 % |
| 19/01 09:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -7.50 % |
| 12/01 05:00 | ETH/USDT | 4h | VENDER | 3600 min | bollinger | -7.40 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**78 señales** del 28/10/2026 al 15/11/2026. Acierto (precio a favor al vencer): **51,3 %** · resultado medio con SL/TP tras costes: **-0.18 R** · no se distingue del azar todavía (z = 0.2).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 53 | 56,6 % | -0.23 R |
| 52-55 % | 24 | 37,5 % | -0.01 R |
| 55-58 % | 1 | 100,0 % | -1.22 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/JPY | 25 | 72,0 % | +0.04 R |
| EUR/JPY | 21 | 38,1 % | -0.57 R |
| USD/CHF | 9 | 44,4 % | +0.17 R |
| BTC/USDT | 9 | 33,3 % | +0.29 R |
| EUR/GBP | 4 | 50,0 % | +0.04 R |
| XRP/USDT | 3 | 33,3 % | -0.18 R |
| ETH/USDT | 2 | 50,0 % | -1.14 R |
| GBP/JPY | 2 | 50,0 % | -1.22 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |
| SOL/USDT | 1 | 0,0 % | -1.12 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 36 | 61,1 % | -0.15 R |
| 15m | 33 | 45,5 % | -0.24 R |
| 1h | 9 | 33,3 % | +0.29 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 57 | 49,1 % | -0.10 R |
| 30-59 min | 15 | 53,3 % | -0.56 R |
| 2-4 h | 6 | 66,7 % | +0.41 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 27 | 33,3 % | -0.46 R |
| soportes | 25 | 72,0 % | +0.04 R |
| barrida | 10 | 40,0 % | +0.04 R |
| rsi | 10 | 50,0 % | -0.22 R |
| estocastico | 9 | 55,6 % | -0.48 R |
| velas | 2 | 100,0 % | +1.23 R |
| macd | 1 | 0,0 % | -1.20 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 23 | 73,9 % | +0.08 R |
| 04-08 h | 12 | 41,7 % | -0.19 R |
| 08-12 h | 12 | 50,0 % | +0.00 R |
| 16-20 h | 12 | 41,7 % | -0.18 R |
| 20-24 h | 11 | 27,3 % | -0.35 R |
| 12-16 h | 8 | 50,0 % | -0.83 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 40 | 47,5 % | +0.00 R |
| lateral (<20) | 21 | 61,9 % | -0.20 R |
| débil (20-25) | 17 | 47,1 % | -0.50 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 42 | 50,0 % | -0.22 R |
| alta | 23 | 47,8 % | -0.18 R |
| baja | 13 | 61,5 % | -0.04 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 27 | 37,0 % | -0.33 R |
| a favor | 26 | 61,5 % | -0.11 R |
| sin tendencia | 25 | 56,0 % | -0.11 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 58 | 46,6 % | -0.26 R |
| en contra | 20 | 65,0 % | +0.04 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 60 | 48,3 % | -0.24 R |
| a favor | 18 | 61,1 % | +0.02 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 15/11 00:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.38 % |
| 09/11 07:45 | ETH/USDT | 15m | COMPRAR | 30 min | bollinger | -1.17 % |
| 14/11 18:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi+bollinger | -0.51 % |
| 09/11 09:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.38 % |
| 30/10 14:25 | EUR/JPY | 5m | COMPRAR | 50 min | macd+estocastico | -0.32 % |
| 14/11 07:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.31 % |
| 05/11 15:50 | GBP/JPY | 5m | COMPRAR | 75 min | bollinger | -0.25 % |
| 30/10 23:30 | SOL/USDT | 15m | VENDER | 45 min | barrida | -0.23 % |
| 12/11 16:45 | EUR/JPY | 15m | COMPRAR | 75 min | bollinger | -0.23 % |
| 14/11 10:00 | BTC/USDT | 1h | COMPRAR | 60 min | rsi | -0.18 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**27 señales** del 28/10/2026 al 13/11/2026. Acierto (precio a favor al vencer): **25,9 %** · resultado medio con SL/TP tras costes: **-0.11 R** · claramente peor que el azar (z = -2.5).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 16 | 25,0 % | -0.04 R |
| <52 % | 11 | 27,3 % | -0.18 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 11 | 27,3 % | +0.11 R |
| USD/CHF | 7 | 28,6 % | +0.11 R |
| ETH/USDT | 4 | 25,0 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -1.05 R |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 19 | 26,3 % | -0.14 R |
| 15m | 6 | 33,3 % | +0.11 R |
| 1h | 2 | 0,0 % | -1.06 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 13 | 23,1 % | +0.30 R |
| 4-12 h | 11 | 36,4 % | -0.18 R |
| 12-24 h | 3 | 0,0 % | -1.06 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 13 | 30,8 % | +0.30 R |
| estocastico | 10 | 20,0 % | -0.18 R |
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
| 04-08 h | 2 | 0,0 % | -1.02 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 18 | 27,8 % | -0.16 R |
| débil (20-25) | 6 | 16,7 % | -0.24 R |
| lateral (<20) | 3 | 33,3 % | +0.29 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 21 | 19,0 % | +0.01 R |
| alta | 4 | 25,0 % | -1.07 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 22 | 27,3 % | -0.06 R |
| a favor | 3 | 33,3 % | +0.13 R |
| en contra | 2 | 0,0 % | -1.16 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 24 | 20,8 % | -0.25 R |
| en contra | 3 | 66,7 % | +0.92 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 22 | 22,7 % | -0.20 R |
| a favor | 5 | 40,0 % | +0.30 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 10/11 17:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.39 % |
| 09/11 13:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -5.20 % |
| 09/11 13:00 | ETH/USDT | 4h | COMPRAR | 3600 min | bollinger | -4.30 % |
| 10/11 17:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -3.89 % |
| 12/11 13:00 | ETH/USDT | 4h | COMPRAR | 720 min | barrida | -3.71 % |
| 29/10 15:00 | XRP/USDT | 1h | COMPRAR | 1200 min | estocastico | -3.36 % |
| 10/11 21:00 | SOL/USDT | 4h | COMPRAR | 3600 min | estocastico | -3.22 % |
| 29/10 09:00 | SOL/USDT | 4h | COMPRAR | 1200 min | soportes | -3.02 % |
| 30/10 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -2.54 % |
