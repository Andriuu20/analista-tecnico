# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado reciente
**181 señales** del 12/08/2026 al 27/10/2026. Acierto (precio a favor al vencer): **51,4 %** · resultado medio con SL/TP tras costes: **-0.17 R** · no se distingue del azar todavía (z = 0.4).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 52-55 % | 65 | 60,0 % | +0.01 R |
| <52 % | 62 | 38,7 % | -0.31 R |
| 55-58 % | 30 | 60,0 % | +0.08 R |
| ≥58 % | 24 | 50,0 % | -0.62 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 55 | 54,5 % | -0.13 R |
| ETH/USDT | 40 | 57,5 % | +0.39 R |
| EUR/JPY | 31 | 64,5 % | -0.09 R |
| EUR/GBP | 23 | 39,1 % | -0.60 R |
| Oro (XAU/USD) | 17 | 29,4 % | -1.04 R |
| GBP/JPY | 8 | 37,5 % | -0.75 R |
| SOL/USDT | 5 | 20,0 % | -0.14 R |
| USD/JPY | 2 | 100,0 % | +0.77 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 97 | 57,7 % | +0.11 R |
| 15m | 68 | 47,1 % | -0.37 R |
| 4h | 10 | 30,0 % | -1.03 R |
| 1h | 6 | 33,3 % | -1.04 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 111 | 54,1 % | +0.04 R |
| 30-59 min | 36 | 55,6 % | -0.18 R |
| 2-4 h | 34 | 38,2 % | -0.85 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| soportes | 49 | 53,1 % | +0.13 R |
| estocastico | 48 | 58,3 % | -0.18 R |
| barrida | 46 | 52,2 % | -0.25 R |
| bollinger | 31 | 41,9 % | -0.32 R |
| bos | 6 | 33,3 % | -1.04 R |
| order_block | 1 | 0,0 % | -1.06 R |
| rsi | 1 | 100,0 % | +1.77 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 40 | 47,5 % | -0.40 R |
| 12-16 h | 38 | 55,3 % | -0.09 R |
| 08-12 h | 34 | 50,0 % | -0.14 R |
| 00-04 h | 30 | 43,3 % | -0.18 R |
| 20-24 h | 21 | 61,9 % | -0.00 R |
| 04-08 h | 18 | 55,6 % | -0.07 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 92 | 53,3 % | -0.22 R |
| lateral (<20) | 58 | 48,3 % | -0.37 R |
| débil (20-25) | 31 | 51,6 % | +0.36 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 105 | 55,2 % | -0.03 R |
| alta | 56 | 48,2 % | -0.29 R |
| baja | 20 | 40,0 % | -0.56 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 64 | 45,3 % | -0.35 R |
| sin tendencia | 63 | 57,1 % | +0.13 R |
| en contra | 54 | 51,9 % | -0.31 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 139 | 53,2 % | -0.15 R |
| en contra | 40 | 45,0 % | -0.23 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 122 | 51,6 % | -0.21 R |
| a favor | 59 | 50,8 % | -0.09 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 21/10 15:50 | ETH/USDT | 5m | VENDER | 75 min | soportes | -1.58 % |
| 22/10 17:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.85 % |
| 21/10 12:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.77 % |
| 21/10 08:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.59 % |
| 23/10 03:05 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.57 % |
| 27/08 02:00 | Oro (XAU/USD) | 4h | COMPRAR | 240 min | soportes | -0.55 % |
| 27/10 14:35 | Oro (XAU/USD) | 5m | VENDER | 75 min | barrida | -0.54 % |
| 28/08 22:00 | Oro (XAU/USD) | 4h | COMPRAR | 240 min | soportes | -0.49 % |
| 22/09 08:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.43 % |
| 04/09 06:00 | Oro (XAU/USD) | 4h | COMPRAR | 240 min | soportes | -0.38 % |
