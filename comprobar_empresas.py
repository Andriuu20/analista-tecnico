"""Comprueba con datos reales que Yahoo Finance devuelve lo que necesita la sección «Análisis de inversión».

Se ejecuta en GitHub Actions (workflow «Comprobar empresas»), porque desde la nube de Claude Code no hay
acceso a Yahoo. Escribe una tabla con lo que llegó de cada empresa y el resultado del análisis.

Uso: python comprobar_empresas.py [--salida resultados/empresas_comprobacion.md]"""
import argparse
from pathlib import Path

from empresas import PAPEL, REFERENCIA, descargar_empresa, evaluar


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--salida", default="resultados/empresas_comprobacion.md")
    args = parser.parse_args()
    referencia = descargar_empresa(REFERENCIA)["precios"]
    filas = ["# Comprobación de la sección «Empresas» con datos reales", "",
             f"S&P 500 ({REFERENCIA}): {len(referencia)} cierres", "",
             "| Empresa | Ticker | Datos (info) | Cierres | Informes | Noticias | Próximo informe | Fuertes / débiles / riesgos | Reacción a informes (bate · decepciona) | Errores |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for ticker, (nombre, *_) in PAPEL.items():
        d = descargar_empresa(ticker)
        try:
            e = evaluar(d, referencia)
            prox = f"{e['proximo_informe']:%d/%m/%Y}" if e["proximo_informe"] is not None else "—"
            puntos = f"{len(e['fuertes'])} / {len(e['debiles'])} / {len(e['riesgos'])}"
            r = e["reaccion"] or {}
            reaccion = " · ".join(f"{r[k]['casos']} ({r[k]['exceso_medio']:+.1%})" if r.get(k, {}).get("casos") else "0"
                                  for k in ("bate", "decepciona"))
            fallo = ""
        except Exception as ex:
            prox = puntos = reaccion = "—"
            fallo = f"evaluar: {type(ex).__name__}: {ex}"
        informes = d["resultados"]["sorpresa"].notna().sum() if len(d["resultados"]) else 0
        campos = sum(d["info"].get(c) is not None for c in ("revenueGrowth", "profitMargins", "trailingPE",
                                                             "freeCashflow", "recommendationKey", "currentPrice"))
        errores = ", ".join(d["errores"] + ([fallo] if fallo else [])) or "—"
        filas.append(f"| {nombre} | {ticker} | {campos}/6 campos | {len(d['precios'])} | {informes} | "
                     f"{len(d['noticias'])} | {prox} | {puntos} | {reaccion} | {errores} |")
        print(nombre, "ok" if errores == "—" else errores, flush=True)
    Path(args.salida).parent.mkdir(parents=True, exist_ok=True)
    Path(args.salida).write_text("\n".join(filas) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
