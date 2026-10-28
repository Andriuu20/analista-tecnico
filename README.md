# Resultados del laboratorio

Esta rama la rellena GitHub Actions automáticamente (no tocar a mano):

- `INFORME.md`: informe de aciertos y errores (empieza por aquí).
- `simulacion.csv`: señales simuladas sobre el pasado reciente (workflow «Simulación»).
- `vivo.json` / `vivo.csv`: señales del laboratorio en directo, cada 30 minutos (workflow «Laboratorio en directo»).

Está separada de `main` para que la app de Streamlit no se reinicie con cada actualización.
