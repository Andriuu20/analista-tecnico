# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado reciente
**188 señales** del 01/09/2026 al 27/10/2026. Acierto (precio a favor al vencer): **51,1 %** · resultado medio con SL/TP tras costes: **-0.19 R** · no se distingue del azar todavía (z = 0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 71 | 38,0 % | -0.41 R |
| 52-55 % | 67 | 56,7 % | +0.01 R |
| 55-58 % | 30 | 63,3 % | +0.10 R |
| ≥58 % | 20 | 60,0 % | -0.50 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| USD/CHF | 54 | 53,7 % | -0.16 R |
| ETH/USDT | 40 | 57,5 % | +0.39 R |
| EUR/JPY | 32 | 62,5 % | -0.13 R |
| Oro (XAU/USD) | 30 | 33,3 % | -0.93 R |
| EUR/GBP | 18 | 50,0 % | -0.40 R |
| GBP/JPY | 8 | 37,5 % | -0.75 R |
| SOL/USDT | 5 | 20,0 % | -0.14 R |
| USD/JPY | 1 | 100,0 % | +2.75 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 5m | 98 | 56,1 % | +0.09 R |
| 15m | 81 | 48,1 % | -0.44 R |
| 1h | 9 | 22,2 % | -1.05 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 103 | 53,4 % | +0.06 R |
| 30-59 min | 55 | 49,1 % | -0.45 R |
| 2-4 h | 30 | 46,7 % | -0.57 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| estocastico | 48 | 56,2 % | -0.23 R |
| barrida | 44 | 52,3 % | -0.21 R |
| soportes | 39 | 59,0 % | +0.43 R |
| bollinger | 27 | 51,9 % | -0.07 R |
| velas | 18 | 38,9 % | -0.95 R |
| bos | 9 | 22,2 % | -1.05 R |
| divergencia | 3 | 33,3 % | -0.50 R |
| rsi | 1 | 100,0 % | +1.77 R |
| order_block | 1 | 0,0 % | -1.06 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 12-16 h | 41 | 51,2 % | -0.14 R |
| 16-20 h | 38 | 50,0 % | -0.37 R |
| 08-12 h | 35 | 45,7 % | -0.16 R |
| 00-04 h | 33 | 45,5 % | -0.22 R |
| 20-24 h | 21 | 66,7 % | -0.01 R |
| 04-08 h | 20 | 55,0 % | -0.18 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 88 | 55,7 % | -0.13 R |
| lateral (<20) | 64 | 43,8 % | -0.46 R |
| débil (20-25) | 36 | 52,8 % | +0.14 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 106 | 54,7 % | +0.01 R |
| alta | 60 | 50,0 % | -0.38 R |
| baja | 22 | 36,4 % | -0.62 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor | 74 | 43,2 % | -0.47 R |
| sin tendencia | 61 | 59,0 % | +0.20 R |
| en contra | 53 | 52,8 % | -0.25 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 130 | 54,6 % | -0.08 R |
| en contra | 55 | 43,6 % | -0.43 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 115 | 53,9 % | -0.14 R |
| a favor | 73 | 46,6 % | -0.27 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 21/10 15:50 | ETH/USDT | 5m | VENDER | 75 min | soportes | -1.58 % |
| 22/10 17:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.85 % |
| 21/10 12:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.77 % |
| 01/10 02:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.72 % |
| 21/10 08:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.59 % |
| 23/10 03:05 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.57 % |
| 06/10 06:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.47 % |
| 22/09 08:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.44 % |
| 20/10 10:35 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.37 % |
| 22/10 16:35 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.37 % |
