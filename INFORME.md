# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado — corto plazo (30 min a 4 h)
**698 señales** del 05/08/2025 al 27/11/2026. Acierto (precio a favor al vencer): **53,2 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = 1.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| mercado = **USD/JPY** | acierta | 63,6 % en 88 | pocos casos en la segunda mitad | ⏳ faltan datos |
| temporalidad = **4h** | acierta | 63,2 % en 87 | pocos casos en la segunda mitad | ⏳ faltan datos |
| dia = **jue** | acierta | 65,8 % en 76 | después 52,6 % en 78 casos | ❔ no se repite |
| fuerza_adx = **débil (20-25)** | acierta | 63,9 % en 61 | después 53,7 % en 82 casos | ❔ no se repite |
| volatilidad = **baja** | acierta | 61,5 % en 91 | después 58,0 % en 50 casos | ✅ confirmado |
| estrategia = **velas** | acierta | 62,5 % en 88 | pocos casos en la segunda mitad | ⏳ faltan datos |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 460 | 53,0 % | -0.17 R |
| 52-55 % | 203 | 53,7 % | -0.23 R |
| 55-58 % | 24 | 50,0 % | -0.18 R |
| ≥58 % | 11 | 54,5 % | -0.37 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 114 | 46,5 % | -0.35 R |
| USD/CHF | 107 | 56,1 % | -0.13 R |
| USD/JPY | 104 | 62,5 % | -0.11 R |
| SOL/USDT | 77 | 63,6 % | -0.04 R |
| Oro (XAU/USD) | 63 | 46,0 % | -0.15 R |
| BTC/USDT | 60 | 51,7 % | -0.14 R |
| EUR/GBP | 58 | 53,4 % | -0.23 R |
| XRP/USDT | 34 | 38,2 % | -0.17 R |
| GBP/JPY | 33 | 48,5 % | -0.24 R |
| USD/CAD | 24 | 45,8 % | -0.42 R |
| AUD/USD | 14 | 42,9 % | -0.87 R |
| EUR/USD | 7 | 85,7 % | +0.38 R |
| ETH/USDT | 3 | 33,3 % | -0.28 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1h | 308 | 49,7 % | -0.17 R |
| 5m | 159 | 54,1 % | -0.14 R |
| 15m | 144 | 53,5 % | -0.39 R |
| 4h | 87 | 63,2 % | -0.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-4 h | 408 | 52,9 % | -0.19 R |
| 1-2 h | 164 | 55,5 % | -0.18 R |
| 30-59 min | 126 | 50,8 % | -0.22 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 300 | 51,3 % | -0.22 R |
| fibonacci | 98 | 56,1 % | -0.13 R |
| velas | 88 | 62,5 % | -0.06 R |
| estocastico | 66 | 53,0 % | -0.00 R |
| barrida | 40 | 55,0 % | -0.32 R |
| bos | 34 | 41,2 % | -0.30 R |
| rsi | 27 | 55,6 % | -0.23 R |
| soportes | 17 | 52,9 % | -0.24 R |
| order_block | 15 | 40,0 % | -0.51 R |
| ruptura | 9 | 55,6 % | -0.28 R |
| medias | 4 | 50,0 % | -0.20 R |
| fvg | 2 | 0,0 % | -1.23 R |
| divergencia | 1 | 100,0 % | -1.11 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 158 | 52,5 % | -0.27 R |
| 16-20 h | 140 | 52,9 % | -0.15 R |
| 08-12 h | 110 | 52,7 % | -0.29 R |
| 04-08 h | 99 | 54,5 % | +0.14 R |
| 00-04 h | 98 | 56,1 % | -0.36 R |
| 20-24 h | 93 | 50,5 % | -0.19 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 301 | 51,2 % | -0.24 R |
| lateral (<20) | 254 | 52,8 % | -0.17 R |
| débil (20-25) | 143 | 58,0 % | -0.13 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 387 | 51,2 % | -0.22 R |
| alta | 170 | 51,8 % | -0.15 R |
| baja | 141 | 60,3 % | -0.17 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 323 | 51,7 % | -0.21 R |
| sin tendencia | 275 | 56,0 % | -0.20 R |
| en contra | 100 | 50,0 % | -0.10 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 487 | 51,3 % | -0.20 R |
| en contra | 206 | 57,3 % | -0.18 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 431 | 52,9 % | -0.16 R |
| a favor | 267 | 53,6 % | -0.25 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 08/10 16:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.12 % |
| 10/11 15:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -2.04 % |
| 15/11 03:00 | XRP/USDT | 15m | VENDER | 45 min | barrida | -1.91 % |
| 12/11 13:00 | BTC/USDT | 1h | COMPRAR | 120 min | bollinger | -1.73 % |
| 17/07 14:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -1.36 % |
| 20/07 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.32 % |
| 08/08 14:00 | SOL/USDT | 1h | VENDER | 180 min | bollinger | -1.29 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 03/11 13:40 | Oro (XAU/USD) | 5m | VENDER | 50 min | bollinger | -1.04 % |
| 21/11 12:35 | ETH/USDT | 5m | VENDER | 100 min | rsi | -1.01 % |

## Simulación sobre el pasado — medio plazo (más de 4 h a 5 días)
**859 señales** del 16/12/2020 al 26/11/2026. Acierto (precio a favor al vencer): **51,0 %** · resultado medio con SL/TP tras costes: **-0.16 R** · no se distingue del azar todavía (z = 0.6).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |
|---|---|---|---|---|
| plazo = **2-5 días** | acierta | 59,2 % en 169 | después 49,5 % en 111 casos | ❔ no se repite |
| dia = **mar** | acierta | 60,2 % en 98 | después 38,9 % en 72 casos | ❔ no se repite |
| fuerza_adx = **lateral (<20)** | acierta | 58,8 % en 187 | después 56,7 % en 134 casos | ✅ confirmado |

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 524 | 51,0 % | -0.17 R |
| 52-55 % | 314 | 51,3 % | -0.15 R |
| 55-58 % | 21 | 47,6 % | -0.25 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 190 | 53,2 % | -0.16 R |
| Oro (XAU/USD) | 142 | 53,5 % | +0.06 R |
| GBP/JPY | 135 | 47,4 % | -0.35 R |
| SOL/USDT | 97 | 54,6 % | -0.06 R |
| ETH/USDT | 74 | 45,9 % | -0.43 R |
| EUR/GBP | 62 | 59,7 % | -0.22 R |
| AUD/USD | 44 | 47,7 % | +0.05 R |
| USD/CAD | 33 | 51,5 % | -0.23 R |
| GBP/USD | 32 | 34,4 % | -0.26 R |
| USD/JPY | 21 | 52,4 % | +0.37 R |
| EUR/JPY | 20 | 55,0 % | -0.39 R |
| XRP/USDT | 9 | 22,2 % | -0.61 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 357 | 52,1 % | -0.18 R |
| 1h | 303 | 48,2 % | -0.28 R |
| 1d | 162 | 53,1 % | +0.13 R |
| 15m | 37 | 54,1 % | -0.30 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4-12 h | 316 | 49,4 % | -0.24 R |
| 2-5 días | 280 | 55,4 % | -0.03 R |
| 12-24 h | 211 | 47,9 % | -0.29 R |
| 1-2 días | 52 | 50,0 % | +0.12 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 421 | 52,5 % | -0.13 R |
| bollinger | 265 | 50,9 % | -0.15 R |
| estocastico | 46 | 60,9 % | -0.00 R |
| barrida | 38 | 34,2 % | -0.35 R |
| velas | 27 | 55,6 % | -0.18 R |
| ruptura | 15 | 40,0 % | +0.02 R |
| fibonacci | 13 | 38,5 % | -0.56 R |
| bos | 10 | 50,0 % | +0.15 R |
| choch | 9 | 55,6 % | -0.65 R |
| order_block | 8 | 25,0 % | -0.55 R |
| rsi | 8 | 50,0 % | -1.16 R |
| supertrend | 4 | 50,0 % | -0.03 R |
| medias | 1 | 100,0 % | +1.72 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 04-08 h | 241 | 50,6 % | -0.08 R |
| 12-16 h | 145 | 53,1 % | -0.17 R |
| 08-12 h | 133 | 50,4 % | -0.33 R |
| 00-04 h | 118 | 47,5 % | -0.09 R |
| 16-20 h | 117 | 48,7 % | -0.23 R |
| 20-24 h | 105 | 56,2 % | -0.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 359 | 48,5 % | -0.18 R |
| lateral (<20) | 321 | 57,9 % | -0.16 R |
| débil (20-25) | 179 | 43,6 % | -0.13 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 500 | 48,0 % | -0.21 R |
| baja | 195 | 57,9 % | -0.01 R |
| alta | 164 | 51,8 % | -0.20 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 335 | 47,5 % | -0.18 R |
| sin tendencia | 298 | 52,0 % | -0.12 R |
| en contra | 226 | 54,9 % | -0.20 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 562 | 51,1 % | -0.17 R |
| en contra | 293 | 50,5 % | -0.14 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 545 | 51,4 % | -0.16 R |
| a favor | 314 | 50,3 % | -0.16 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 04/02 01:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -14.77 % |
| 22/08 10:00 | ETH/USDT | 4h | VENDER | 480 min | soportes | -13.06 % |
| 25/08 10:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -10.69 % |
| 13/11 05:00 | SOL/USDT | 4h | COMPRAR | 3600 min | bollinger | -10.06 % |
| 30/06 02:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -8.99 % |
| 20/08 14:00 | SOL/USDT | 4h | VENDER | 3600 min | bollinger | -7.25 % |
| 26/03 05:00 | Oro (XAU/USD) | 1d | VENDER | 4320 min | soportes | -6.20 % |
| 07/08 14:00 | SOL/USDT | 4h | VENDER | 2400 min | bollinger | -5.94 % |
| 13/05 10:00 | XRP/USDT | 4h | COMPRAR | 3600 min | fibonacci | -5.87 % |
| 27/08 06:00 | Oro (XAU/USD) | 1d | COMPRAR | 4320 min | soportes | -5.74 % |

## Laboratorio en directo — corto plazo (30 min a 4 h)
**130 señales** del 28/10/2026 al 27/11/2026. Acierto (precio a favor al vencer): **53,1 %** · resultado medio con SL/TP tras costes: **-0.30 R** · no se distingue del azar todavía (z = 0.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 87 | 51,7 % | -0.45 R |
| 52-55 % | 36 | 52,8 % | -0.02 R |
| 55-58 % | 7 | 71,4 % | +0.13 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 31 | 41,9 % | -0.53 R |
| USD/JPY | 29 | 69,0 % | -0.04 R |
| BTC/USDT | 24 | 45,8 % | -0.34 R |
| USD/CHF | 13 | 46,2 % | -0.24 R |
| EUR/GBP | 7 | 57,1 % | -0.29 R |
| ETH/USDT | 6 | 66,7 % | -0.31 R |
| USD/CAD | 6 | 66,7 % | +0.00 R |
| XRP/USDT | 6 | 50,0 % | -0.67 R |
| GBP/JPY | 3 | 33,3 % | -1.18 R |
| SOL/USDT | 3 | 33,3 % | -0.31 R |
| Oro (XAU/USD) | 2 | 100,0 % | +1.23 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 73 | 61,6 % | -0.22 R |
| 15m | 42 | 47,6 % | -0.31 R |
| 1h | 15 | 26,7 % | -0.67 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 99 | 54,5 % | -0.19 R |
| 30-59 min | 20 | 50,0 % | -0.71 R |
| 2-4 h | 11 | 45,5 % | -0.49 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 38 | 65,8 % | -0.22 R |
| bollinger | 37 | 32,4 % | -0.50 R |
| estocastico | 19 | 57,9 % | -0.23 R |
| barrida | 14 | 42,9 % | -0.31 R |
| rsi | 11 | 54,5 % | -0.53 R |
| fibonacci | 7 | 71,4 % | +0.02 R |
| order_block | 4 | 75,0 % | +0.32 R |
| velas | 2 | 100,0 % | +1.23 R |
| ruptura | 2 | 50,0 % | -0.64 R |
| macd | 1 | 0,0 % | -1.20 R |
| supertrend | 1 | 100,0 % | -1.10 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 00-04 h | 36 | 66,7 % | -0.31 R |
| 08-12 h | 32 | 56,2 % | -0.12 R |
| 20-24 h | 20 | 45,0 % | -0.18 R |
| 04-08 h | 18 | 38,9 % | -0.32 R |
| 12-16 h | 12 | 50,0 % | -0.94 R |
| 16-20 h | 12 | 41,7 % | -0.25 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 59 | 45,8 % | -0.18 R |
| lateral (<20) | 41 | 63,4 % | -0.33 R |
| débil (20-25) | 30 | 53,3 % | -0.48 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 74 | 51,4 % | -0.41 R |
| alta | 32 | 50,0 % | -0.36 R |
| baja | 24 | 62,5 % | +0.13 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 47 | 57,4 % | -0.28 R |
| sin tendencia | 47 | 57,4 % | -0.21 R |
| en contra | 36 | 41,7 % | -0.43 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 92 | 48,9 % | -0.38 R |
| en contra | 38 | 63,2 % | -0.10 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 90 | 48,9 % | -0.33 R |
| a favor | 40 | 62,5 % | -0.22 R |

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
| 25/11 22:00 | BTC/USDT | 1h | VENDER | 120 min | bollinger | -0.37 % |
| 24/11 05:10 | BTC/USDT | 5m | VENDER | 100 min | estocastico | -0.36 % |
| 19/11 09:35 | BTC/USDT | 5m | VENDER | 100 min | fibonacci | -0.34 % |

## Laboratorio en directo — medio plazo (más de 4 h a 5 días)
**52 señales** del 28/10/2026 al 26/11/2026. Acierto (precio a favor al vencer): **38,5 %** · resultado medio con SL/TP tras costes: **-0.50 R** · no se distingue del azar todavía (z = -1.7).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 27 | 40,7 % | -0.61 R |
| 52-55 % | 25 | 36,0 % | -0.40 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| SOL/USDT | 18 | 44,4 % | -0.23 R |
| USD/CHF | 17 | 41,2 % | -0.42 R |
| ETH/USDT | 7 | 14,3 % | -1.02 R |
| GBP/JPY | 4 | 25,0 % | -0.56 R |
| EUR/GBP | 4 | 50,0 % | -0.64 R |
| GBP/USD | 1 | 100,0 % | — |
| XRP/USDT | 1 | 0,0 % | -1.06 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 4h | 39 | 38,5 % | -0.56 R |
| 1h | 7 | 42,9 % | -0.79 R |
| 15m | 6 | 33,3 % | +0.11 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 2-5 días | 27 | 33,3 % | -0.50 R |
| 4-12 h | 15 | 40,0 % | -0.34 R |
| 1-2 días | 6 | 66,7 % | -1.04 R |
| 12-24 h | 4 | 25,0 % | -1.08 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 26 | 42,3 % | -0.35 R |
| estocastico | 20 | 40,0 % | -0.36 R |
| soportes | 7 | 28,6 % | -1.06 R |
| barrida | 3 | 66,7 % | -1.02 R |
| rsi | 1 | 0,0 % | -1.12 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 11 | 36,4 % | -0.67 R |
| 20-24 h | 10 | 50,0 % | +0.22 R |
| 00-04 h | 9 | 22,2 % | -1.06 R |
| 16-20 h | 8 | 37,5 % | -0.36 R |
| 04-08 h | 7 | 42,9 % | -1.03 R |
| 08-12 h | 7 | 42,9 % | -0.01 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 38 | 39,5 % | -0.62 R |
| lateral (<20) | 7 | 57,1 % | -0.09 R |
| débil (20-25) | 7 | 14,3 % | -0.36 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 39 | 35,9 % | -0.39 R |
| alta | 11 | 36,4 % | -1.04 R |
| baja | 2 | 100,0 % | +0.15 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 32 | 25,0 % | -0.58 R |
| en contra | 12 | 66,7 % | -1.06 R |
| a favor | 8 | 50,0 % | +0.61 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 45 | 31,1 % | -0.65 R |
| en contra | 4 | 75,0 % | +0.92 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 43 | 34,9 % | -0.62 R |
| a favor | 9 | 55,6 % | +0.09 R |

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
