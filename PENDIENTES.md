# Pendientes e ideas

Estado actual: app publicada en https://tradeappnexus.streamlit.app con registro permanente en un Gist
(secretos `GITHUB_TOKEN` y `GIST_ID` en Streamlit). Datos: Binance (cripto) y Yahoo Finance (forex/oro).

## Para más adelante
- **Botón "Ver en TradingView"** junto al resultado (abrir el gráfico del mismo mercado).
- **Avisos por Telegram**: escanear todos los mercados cada ~15 min y avisar de señales de 1 h o más.
  - Opción A: GitHub Actions (gratis, repo público; el reloj puede retrasarse unos minutos).
  - Opción B: script en el PC de mesa (más preciso, solo con el PC encendido).
  - También guardaría las señales en el registro, para que aprenda sin abrir la app.
  - Decidir: horario (p. ej. 8:00–23:00) y plazos (solo horas/días).
- **MetaTrader 5 / bot**: en el PC de mesa (Windows), primero en cuenta demo. MT5 tiene librería
  oficial de Python. Brokers regulados con MT5: Darwinex (CNMV), Pepperstone, IG.
- Comprobar que la escritura en el Gist funciona con la primera señal real.
- Registro en vivo: comprobar también si se tocó antes el SL o el TP (ya se guardan en cada señal).
- Medir con el histórico si el ADX o la zona premium/discount mejoran el acierto antes de que influyan en la
  decisión (como se hizo con el filtro de tendencia).

- **Laboratorio de corto plazo** (en marcha): revisar `INFORME.md` de la rama `resultados` cuando haya ≥ 100
  señales y corregir solo patrones confirmados. Después, pasar a operaciones de más plazo.
- Estrategias de traders que el usuario encuentre en vídeos: convertir sus reglas en reglas medibles y
  probarlas con la simulación antes de añadirlas.

## Regla
No usar dinero real hasta tener al menos 100 señales comprobadas con más del 55 % de acierto
en «Mis resultados».
