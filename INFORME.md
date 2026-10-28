# Informe de aciertos y errores
Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.

## Simulación sobre el pasado reciente
**546 señales** del 28/01/2026 al 27/10/2026. Acierto (precio a favor al vencer): **50,7 %** · resultado medio con SL/TP tras costes: **-0.14 R** · no se distingue del azar todavía (z = 0.3).

### Patrones (encontrados en la primera mitad y comprobados en la segunda)
Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).

### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| <52 % | 183 | 47,0 % | -0.13 R |
| 52-55 % | 179 | 53,6 % | -0.09 R |
| 55-58 % | 113 | 50,4 % | -0.10 R |
| ≥58 % | 71 | 53,5 % | -0.33 R |

### Por mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| EUR/JPY | 104 | 54,8 % | -0.09 R |
| USD/CHF | 95 | 54,7 % | -0.17 R |
| Oro (XAU/USD) | 89 | 44,9 % | -0.31 R |
| ETH/USDT | 83 | 55,4 % | +0.09 R |
| EUR/GBP | 51 | 39,2 % | -0.42 R |
| BTC/USDT | 47 | 57,4 % | -0.07 R |
| GBP/JPY | 36 | 38,9 % | -0.14 R |
| SOL/USDT | 28 | 42,9 % | -0.09 R |
| USD/JPY | 8 | 50,0 % | -0.21 R |
| EUR/USD | 5 | 100,0 % | +0.93 R |

### Por temporalidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 15m | 223 | 51,1 % | -0.23 R |
| 5m | 212 | 53,3 % | -0.08 R |
| 1h | 101 | 46,5 % | +0.05 R |
| 4h | 10 | 30,0 % | -1.03 R |

### Por plazo
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 1-2 h | 221 | 53,4 % | -0.02 R |
| 30-59 min | 194 | 50,5 % | -0.27 R |
| 2-4 h | 131 | 46,6 % | -0.14 R |

### Por estrategia
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| bollinger | 169 | 49,7 % | -0.14 R |
| soportes | 106 | 51,9 % | +0.00 R |
| estocastico | 88 | 53,4 % | -0.21 R |
| barrida | 87 | 54,0 % | -0.22 R |
| velas | 42 | 40,5 % | -0.35 R |
| bos | 35 | 54,3 % | -0.03 R |
| rsi | 14 | 50,0 % | +0.32 R |
| order_block | 5 | 20,0 % | -0.69 R |
| divergencia | 2 | 50,0 % | +0.89 R |
| fvg | 1 | 100,0 % | +2.75 R |

### Por franja horaria (hora de España)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| 16-20 h | 117 | 47,0 % | -0.12 R |
| 12-16 h | 116 | 56,9 % | -0.18 R |
| 08-12 h | 95 | 49,5 % | -0.16 R |
| 00-04 h | 90 | 46,7 % | -0.20 R |
| 04-08 h | 67 | 44,8 % | +0.05 R |
| 20-24 h | 61 | 60,7 % | -0.14 R |

### Por fuerza de la tendencia (ADX)
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| fuerte (≥25) | 250 | 54,8 % | -0.09 R |
| lateral (<20) | 192 | 45,3 % | -0.29 R |
| débil (20-25) | 104 | 51,0 % | +0.04 R |

### Por volatilidad
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| normal | 339 | 51,3 % | -0.07 R |
| alta | 149 | 50,3 % | -0.14 R |
| baja | 58 | 48,3 % | -0.53 R |

### A favor o en contra de la tendencia del plazo mayor
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| sin tendencia | 241 | 52,7 % | -0.01 R |
| a favor | 199 | 47,2 % | -0.18 R |
| en contra | 106 | 52,8 % | -0.32 R |

### Zona premium/discount
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| a favor (barato al comprar / caro al vender) | 404 | 51,0 % | -0.13 R |
| en contra | 140 | 50,0 % | -0.15 R |

### Estructura de mercado
| Grupo | Casos | Acierto | Resultado medio SL/TP |
|---|---|---|---|
| en contra | 365 | 50,4 % | -0.17 R |
| a favor | 181 | 51,4 % | -0.06 R |

### Los 10 fallos más grandes (para revisar a mano en el gráfico)
| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |
|---|---|---|---|---|---|---|
| 30/09 14:15 | SOL/USDT | 15m | VENDER | 45 min | barrida | -2.16 % |
| 21/10 15:50 | ETH/USDT | 5m | VENDER | 75 min | soportes | -1.58 % |
| 15/09 17:00 | SOL/USDT | 1h | COMPRAR | 180 min | bollinger | -1.17 % |
| 25/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -1.11 % |
| 18/10 14:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -1.07 % |
| 18/08 02:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.96 % |
| 22/10 17:50 | ETH/USDT | 5m | COMPRAR | 75 min | soportes | -0.85 % |
| 21/10 12:35 | ETH/USDT | 5m | VENDER | 75 min | soportes | -0.77 % |
| 08/05 15:00 | Oro (XAU/USD) | 1h | COMPRAR | 180 min | bos | -0.75 % |
| 07/04 03:00 | Oro (XAU/USD) | 1h | VENDER | 180 min | bos | -0.74 % |
