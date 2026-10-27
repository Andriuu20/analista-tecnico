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

## Regla
No usar dinero real hasta tener al menos 100 señales comprobadas con más del 55 % de acierto
en «Mis resultados».
