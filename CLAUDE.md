# Contexto del proyecto (léelo antes de nada)

App web personal de análisis técnico, en español. Publicada en **https://tradeappnexus.streamlit.app**
(Streamlit Community Cloud, desplegada desde la rama `main` de este repo: cada push a `main` la actualiza sola).
Lista de pendientes e ideas: **PENDIENTES.md**.

## Sobre el usuario
- Habla español. No es programador: explícale todo paso a paso, en lenguaje sencillo, con enlaces directos.
- Usa sobre todo un **iPhone** (Safari) y a veces un **PC de mesa con Windows**. Las instrucciones deben poder
  seguirse desde el móvil. Suele mandar capturas de pantalla.
- Vive en España. Tiene cuentas en GitHub (usuario `Andriuu20`), Binance y Streamlit. No tiene cuenta en brokers.
- **Seguridad:** nunca le pidas que pegue tokens, contraseñas o claves en el chat. Van en los Secrets de Streamlit
  o de GitHub. Si los pega por error, dile que los revoque y cree otros.

## Decisiones ya tomadas (no las reabras sin motivo)
- **Nada de Pocket Option ni Quotex**: sin API pública, automatizar su web va contra sus condiciones, la CNMV tiene
  advertencias contra ambos y sus mercados OTC usan precios generados por el propio broker.
- Las **binarias para minoristas están prohibidas en la UE** (ESMA/CNMV). Registrarse en brokers de EE. UU. con VPN
  no es viable (exigen residencia y el KYC lo detecta). Alternativa legal: forex/CFD con brokers regulados en la UE
  (XTB, IG, Darwinex, Pepperstone, Interactive Brokers), primero en **demo**.
- **TradingView no tiene API pública de datos**; las librerías no oficiales van contra sus condiciones o están
  abandonadas. Como mucho, un botón que abra el gráfico en TradingView (pendiente).
- Regla: **no usar dinero real** hasta tener ≥ 100 señales comprobadas con > 55 % de acierto en «Mis resultados»
  (con pagos de binarias del 80-90 % hace falta ~53-55 % solo para no perder).
- MetaTrader 5 / bot automático: aplazado. Iría en el PC de Windows del usuario, en cuenta demo.
- Avisos por Telegram: aplazado (ver PENDIENTES.md).

## Qué hace la app
Pantalla pensada para móvil: eliges mercado (o «Buscar en todos») y plazo (Cualquiera / Minutos / Horas / Días),
pulsas **Analizar** y responde **COMPRAR / VENDER / ESPERAR**, durante cuánto tiempo, confianza y hora de
vencimiento. Detalles plegados debajo: ¿Por qué?, Gráfico, Backtest, Mis resultados, Cómo funciona.

- **Datos** (sin claves de API): Binance público `data-api.binance.vision` para cripto (fallback a Yahoo
  `BTC-USD`); Yahoo Finance vía `yfinance` para forex y oro. Solo velas cerradas.
- **Temporalidades** analizadas solas: 5m, 15m, 1h, 4h (Yahoo: remuestreo de 1h) y 1d. Gana la mejor señal.
- **Filtro de tendencia medido** (`tendencia.py`): tendencia = EMA 50 vs EMA 200 + pendiente, de la temporalidad
  superior (alineada sin mirar al futuro; 1d usa la suya). Las señales en contra se descartan por defecto; para
  cada mercado y estrategia el filtro solo se desactiva si en el 70 % antiguo las señales en contra (≥ 30) no
  acertaron menos que el resto. La confianza se mide siempre con el backtest completo: juzgar cada señal solo
  con las cifras de su situación (histórico troceado) se probó y más que duplicaba las señales falsas en datos
  aleatorios. Señales falsas en paseos aleatorios: sin filtro 3,8 %, filtro fijo 2,2 %, filtro medido 3,2 %.
- **6 estrategias** (`estrategias.py`): cruce EMA 9/21, RSI 30/70, cruce MACD, rebote en soporte/resistencia
  (pivotes confirmados k=5), Fibonacci 50-78,6 % a favor del impulso, patrones de velas.
- **Backtest** (`backtest.py`): acierto tipo binaria a vencimiento (precio a favor tras N velas, N en 1-20).
- **Anti-autoengaño** (`senal.py`), importante:
  - El plazo de cada estrategia se elige con el 70 % antiguo del histórico; la confianza se mide con el 30 %
    reciente (no usado para elegir) + resultados reales del registro, encogidos hacia el 50 % (prior 20).
  - Para votar, el acierto antiguo debe ser significativo: z ≥ 2,2 (corregido por probar 7 plazos).
  - Verificado: en paseos aleatorios casi nunca da señal; prueba de truncado sin fugas de futuro (0 diferencias).
  - Ojo: «Buscar en todos» se queda con la mejor de 5 temporalidades × 14 mercados, así que en datos
    aleatorios aparecen algunas señales del 55-58 %. El registro en vivo es el juez final.
- **Registro en vivo** (`registro.py`): cada COMPRAR/VENDER se guarda solo y se comprueba al vencer. Se guarda en
  un Gist secreto (Secrets de Streamlit `GITHUB_TOKEN` con permiso Gists RW y `GIST_ID`); sin ellos, en archivo
  local (se pierde al reiniciar). Los resultados reales se suman al cálculo de confianza («aprende»).
- `APP_CLAVE` en Secrets (opcional) protege la app con contraseña.

## Archivos
`app.py` (interfaz) · `datos.py` · `indicadores.py` · `estrategias.py` · `backtest.py` · `senal.py` · `tendencia.py` ·
`registro.py` · `graficos.py` · `.streamlit/config.toml` (tema oscuro) · `requirements.txt` (Python 3.12 en Cloud).

## Cómo probar
- El entorno en la nube de Claude Code **bloquea Yahoo y Binance**: prueba con `ANALISTA_DEMO=1` (datos
  aleatorios, distintos por símbolo) y `streamlit.testing.v1.AppTest`, o con Playwright a 390 px de ancho.
- La prueba con datos reales la hace el usuario en la app publicada.
