# 📈 Analista técnico

App web personal en español, pensada para el móvil. Eliges un mercado (EUR/USD, USD/JPY, BTC…) o
«Buscar en todos», pulsas **Analizar** y te dice **si comprar, vender o esperar**, **durante cuántos minutos u
horas** y **con qué confianza**. Analiza sola velas de 5 min, 15 min, 1 h, 4 h y 1 día y se queda con la mejor oportunidad (o la del plazo que elijas: minutos, horas o días). La confianza se basa en cómo le
ha ido a cada estrategia en el histórico de ese mercado y en las señales reales que ya ha dado.

- **17 estrategias**: medias móviles (EMA y SMA), SuperTrend, RSI y divergencias, MACD, Bollinger, estocástico,
  soportes y resistencias, ruptura y retesteo, Fibonacci, velas japonesas y estructura de mercado (BOS, CHoCH,
  barridas de liquidez, FVG, order blocks). Detalle en `docs/AUDITORIA_MOTOR.md`.
- **Plan de operación**: entrada, Stop Loss, Take Profit y riesgo-beneficio, con su resultado en el histórico
  tras costes, y motivos a favor y en contra.
- **Backtest**: el porcentaje de acierto de cada estrategia y plazo sobre el histórico.
- **Registro en vivo**: cada señal se guarda sola y se comprueba al vencer. Muestra si se supera el 55 %.
- **Datos gratuitos sin registro**: Yahoo Finance (forex y oro) y Binance (cripto).

## Publicarla gratis (Streamlit Community Cloud)

1. Sube esta carpeta a un repositorio de GitHub (puede ser privado).
2. Entra en <https://share.streamlit.io> con tu cuenta de GitHub.
3. Pulsa **Create app**, elige el repositorio, la rama `main` y el archivo `app.py`.
4. Abre la URL en el móvil. En iPhone (Safari): botón **Compartir → Añadir a pantalla de inicio** y tendrás
   un icono como si fuera una app.

## Guardar el registro de forma permanente (recomendado)

El disco de Streamlit Cloud se borra al reiniciar la app, así que el registro se guarda en un **Gist
secreto** de tu GitHub:

1. Crea un Gist secreto en <https://gist.github.com> con un archivo llamado `registro.json` cuyo contenido
   sea `[]`. El ID es la última parte de la URL del Gist.
2. Crea un token en GitHub: **Settings → Developer settings → Personal access tokens → Fine-grained tokens**,
   con el permiso de cuenta **Gists: Read and write**.
3. En Streamlit Cloud, en tu app: **⋮ → Settings → Secrets**, pega:

   ```toml
   GITHUB_TOKEN = "github_pat_..."
   GIST_ID = "el_id_del_gist"
   APP_CLAVE = "una contraseña para entrar"   # opcional: protege la app
   ```

## Probarla en tu ordenador

```bash
pip install -r requirements.txt
streamlit run app.py
```

Sin conexión: `ANALISTA_DEMO=1 streamlit run app.py` usa datos aleatorios de prueba.

## Cómo decide (resumen)

1. Calcula las 6 estrategias. Solo cuentan las que dan señal en la **última vela cerrada**.
2. Para cada estrategia elige su mejor plazo con el **70 % antiguo** del histórico. Solo la deja votar si ese
   acierto se distingue claramente del azar.
3. La **confianza** se mide con el **30 % reciente** (que no se usó para elegir) más los resultados reales
   del registro. Así no se engaña eligiendo el mejor resultado a posteriori. Con datos aleatorios casi nunca
   da señal.
4. Si las estrategias fiables coinciden, da la señal. Si se contradicen, dice **esperar**.

> Esto es una herramienta de aprendizaje, no asesoramiento financiero. No operes con dinero real hasta que
> el Registro muestre más de un 55 % de acierto con al menos 100 señales comprobadas.
