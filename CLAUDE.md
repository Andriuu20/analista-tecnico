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
- **17 estrategias** (`estrategias.py`; auditoría completa en `docs/AUDITORIA_MOTOR.md`): cruce EMA 9/21, RSI
  30/70, cruce MACD, rebote en soporte/resistencia (pivotes confirmados k=5), Fibonacci 50-78,6 % a favor del
  impulso, patrones de velas, SuperTrend (10,3), cruce SMA 50/200, Bollinger (20,2), estocástico (14,3,3), y de
  `estructura.py` (SMC, mismos pivotes): BOS, CHoCH, barrida de liquidez, ruptura+retest, FVG, order block,
  divergencia RSI. Una sola implementación por indicador (`indicadores.py`); EMA 20 no se añade (redundante
  con EMA 21). ADX, volatilidad (percentil ATR), SMA 200, HH/HL, máximos/mínimos iguales y premium/discount son
  solo contexto: no cambian la decisión hasta que se demuestre con el histórico que mejoran el acierto.
- **Backtest** (`backtest.py`): acierto tipo binaria a vencimiento (precio a favor tras N velas, N en 1-20).
- **Anti-autoengaño** (`senal.py`), importante:
  - El plazo de cada estrategia se elige con el 70 % antiguo del histórico; la confianza se mide con el 30 %
    reciente (no usado para elegir) + resultados reales del registro, encogidos hacia el 50 % (prior 20).
  - Para votar, el acierto antiguo debe ser significativo: z ≥ 2,4 (calibrado con datos aleatorios para 17
    estrategias × 7 plazos: ~3 % de velas con señal, ~1 % con confianza ≥ 55 %; test en `tests/test_azar.py`).
    Si se añaden estrategias, recalibrar. La confianza es una media ponderada, no una suma: más estrategias
    parecidas no la inflan.
  - Verificado: en paseos aleatorios casi nunca da señal; prueba de truncado sin fugas de futuro (0 diferencias).
  - Ojo: «Buscar en todos» se queda con la mejor de 5 temporalidades × 14 mercados, así que en datos
    aleatorios aparecen algunas señales del 55-58 %. El registro en vivo es el juez final.
- **Plan SL/TP** (`plan.py`): entrada = cierre; SL tras el último suelo/techo confirmado + 0,1 ATR (0,5-3 ATR, si
  no 1,5 ATR); TP = R × riesgo, R ∈ {1; 1,5; 2; 3} elegido con el 70 % antiguo; se informa del 30 % reciente
  (operaciones, TP alcanzados, resultado medio en R tras costes, duración). Empate SL/TP en la misma vela = pérdida.
- **No operar**: si el coste se come > 25 % del riesgo, o (forex/oro, plazos < 1 día) si hay una noticia de alto
  impacto antes del vencimiento (`noticias.py`, calendario público de Forex Factory; si falla, se ignora).
- **Explicación** (`factores.py`): motivos a favor / en contra; 📏 = medido, el resto orientativo. No inventar
  probabilidades.
- **Registro en vivo** (`registro.py`): cada COMPRAR/VENDER se guarda solo y se comprueba al vencer. Se guarda en
  un Gist secreto (Secrets de Streamlit `GITHUB_TOKEN` con permiso Gists RW y `GIST_ID`); sin ellos, en archivo
  local (se pierde al reiniciar). Los resultados reales se suman al cálculo de confianza («aprende»).
- `APP_CLAVE` en Secrets (opcional) protege la app con contraseña.
- **Motor compartido** (`motor.py`): `preparar`, `juzgar`, `filtrar_noticias`, `analizar_mercado`. Lo usan la app,
  la simulación y el laboratorio, para que decidan exactamente igual. No duplicar lógica de decisión en otro sitio.

## Laboratorio de pruebas (corto plazo, 30 min - 4 h)
Para acumular resultados rápido y aprender de los errores sin dinero. Todo corre en **GitHub Actions** (aquí no
hay acceso a datos reales) y guarda en la rama **`resultados`** (no en `main`, para no reiniciar Streamlit):
- `simulacion.py` + workflow «Simulación» (botón manual y cada día): revive las últimas semanas vela a vela con
  el motor recortado a los datos de cada momento; sin solapar operaciones; sin filtro de noticias (no hay
  calendario histórico). Un trabajo por mercado en paralelo.
- `laboratorio.py` + workflow «Laboratorio en directo» (cada 30 min): resuelve vencidas (binaria y SL/TP),
  apunta señales nuevas de todas las temporalidades con plazo 30-240 min (marca cuál elegiría la app).
- `informe.py` → `resultados/INFORME.md`: aciertos por mercado, temporalidad, plazo, estrategia, hora, ADX,
  volatilidad, tendencia, zona, estructura y tramo de confianza.
- **Cómo aprender de los errores sin sobreajustar:** solo cuentan patrones de ≥ 30 casos que aparecen en la
  primera mitad (por fecha) y se repiten en la segunda («✅ confirmado»). Cualquier cambio al motor que salga de
  ahí debe comprobarse después con datos nuevos (laboratorio en directo) antes de darlo por bueno. No corregir
  fallos sueltos uno a uno.
- Para leer los resultados en una sesión nueva: `git fetch origin resultados && git show origin/resultados:INFORME.md`.

## Archivos
`app.py` (interfaz) · `datos.py` · `indicadores.py` · `estrategias.py` · `estructura.py` · `backtest.py` · `senal.py` ·
`tendencia.py` · `plan.py` · `factores.py` · `noticias.py` · `registro.py` · `graficos.py` · `motor.py` · `simulacion.py` ·
`laboratorio.py` · `informe.py` · `.github/workflows/` · `.streamlit/config.toml`
(tema oscuro) · `requirements.txt` (Python 3.12 en Cloud) · `requirements-dev.txt` (pytest, solo para pruebas).

## Cómo probar
- `python -m pytest tests` (instalar antes `pip install -r requirements.txt -r requirements-dev.txt`). Incluye la
  prueba de truncado (nada mira al futuro) y la de señales falsas con datos aleatorios. Deben pasar antes de subir.
- El entorno en la nube de Claude Code **bloquea Yahoo y Binance**: prueba con `ANALISTA_DEMO=1` (datos
  aleatorios, distintos por símbolo) y `streamlit.testing.v1.AppTest`, o con Playwright a 390 px de ancho.
- La prueba con datos reales la hace el usuario en la app publicada.
