"""Informe de aciertos y errores de las señales simuladas o del laboratorio en directo.

Busca PATRONES en los fallos (por mercado, temporalidad, hora, estrategia, situación del mercado…), no
explicaciones caso a caso: un fallo suelto casi siempre es ruido. Para no engañarse, los resultados se
parten en dos mitades por fecha: un patrón encontrado en la primera mitad solo se da por bueno si se
repite en la segunda («confirmado»). Así se evita corregir la app para que acierte el pasado y falle
el futuro.

Uso: python informe.py resultados/simulacion.csv [resultados/vivo.csv] --salida resultados/INFORME.md"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from motor import ZONA

MIN_GRUPO = 30  # casos mínimos en cada mitad para opinar sobre un grupo
Z_PATRON = 2.0


def _z(aciertos: float, n: int) -> float:
    return (aciertos / n - 0.5) / (0.5 / np.sqrt(n)) if n else 0.0


def _pct(x: float) -> str:
    return "—" if pd.isna(x) else f"{x * 100:.1f} %".replace(".", ",")


def preparar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    vela = pd.to_datetime(df["vela"], utc=True).dt.tz_convert(ZONA)
    df["fecha"] = vela
    df["franja"] = (vela.dt.hour // 4 * 4).map(lambda h: f"{h:02d}-{h + 4:02d} h")
    df["dia"] = vela.dt.dayofweek.map(dict(enumerate(["lun", "mar", "mié", "jue", "vie", "sáb", "dom"])))
    df["plazo"] = pd.cut(df["plazo_min"], [0, 59, 119, 240], labels=["30-59 min", "1-2 h", "2-4 h"])
    df["fuerza_adx"] = pd.cut(df["adx"], [-1, 20, 25, 1000], labels=["lateral (<20)", "débil (20-25)", "fuerte (≥25)"])
    df["volatilidad"] = pd.cut(df["volatilidad_pct"], [-0.01, 0.2, 0.8, 1.01], labels=["baja", "normal", "alta"])
    df["confianza_tramo"] = pd.cut(df["confianza"], [0, 0.52, 0.55, 0.58, 1], labels=["<52 %", "52-55 %", "55-58 %", "≥58 %"])
    df["tendencia_txt"] = df["tendencia"].map({1: "a favor", -1: "en contra", 0: "sin tendencia"})
    compra = df["direccion"] == 1
    df["zona_txt"] = np.where(df["zona"].isna(), None,
                              np.where((df["zona"] == "discount") == compra, "a favor (barato al comprar / caro al vender)",
                                       "en contra"))
    df["estructura_txt"] = np.where(df["estructura"] == 0, "sin definir",
                                    np.where(df["estructura"] == df["direccion"], "a favor", "en contra"))
    # mitades por fecha: exploración (antigua) y validación (reciente)
    corte = df["fecha"].sort_values().iloc[len(df) // 2] if len(df) else None
    df["mitad"] = np.where(df["fecha"] < corte, "exploración", "validación")
    return df


def tabla(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    g = df.groupby(columna, observed=True)
    t = pd.DataFrame({
        "casos": g["acierto"].size(),
        "acierto": g["acierto"].mean(),
        "resultado_medio_R": g["resultado_r"].mean(),
    })
    t["z"] = [_z(a * n, n) for a, n in zip(t["acierto"], t["casos"])]
    return t.sort_values("casos", ascending=False)


def patrones(df: pd.DataFrame, columnas: list[str]) -> list[str]:
    """Grupos que en la mitad antigua aciertan claramente menos (o más) que el 50 %, y si se repite después."""
    salida = []
    explor, valid = df[df["mitad"] == "exploración"], df[df["mitad"] == "validación"]
    for col in columnas:
        te, tv = tabla(explor, col), tabla(valid, col)
        for grupo, fila in te.iterrows():
            if fila["casos"] < MIN_GRUPO or abs(fila["z"]) < Z_PATRON:
                continue
            tipo = "falla" if fila["z"] < 0 else "acierta"
            if grupo in tv.index and tv.loc[grupo, "casos"] >= MIN_GRUPO:
                v = tv.loc[grupo]
                mismo = (v["acierto"] < 0.5) == (fila["acierto"] < 0.5)
                estado = "✅ confirmado" if mismo and abs(v["z"]) >= 1 else "❔ no se repite"
                detalle = f"después {_pct(v['acierto'])} en {int(v['casos'])} casos"
            else:
                estado, detalle = "⏳ faltan datos", "pocos casos en la segunda mitad"
            salida.append(f"| {col} = **{grupo}** | {tipo} | {_pct(fila['acierto'])} en {int(fila['casos'])} | "
                          f"{detalle} | {estado} |")
    return salida


def _md(t: pd.DataFrame) -> str:
    filas = ["| Grupo | Casos | Acierto | Resultado medio SL/TP |", "|---|---|---|---|"]
    for grupo, f in t.iterrows():
        r = "—" if pd.isna(f["resultado_medio_R"]) else f"{f['resultado_medio_R']:+.2f} R"
        filas.append(f"| {grupo} | {int(f['casos'])} | {_pct(f['acierto'])} | {r} |")
    return "\n".join(filas)


def informe(df: pd.DataFrame, titulo: str) -> str:
    if df.empty:
        return f"## {titulo}\n\nTodavía no hay resultados.\n"
    df = preparar(df)
    n, aciertos = len(df), int(df["acierto"].sum())
    z = _z(aciertos, n)
    partes = [
        f"## {titulo}",
        f"**{n} señales** del {df['fecha'].min():%d/%m/%Y} al {df['fecha'].max():%d/%m/%Y}. "
        f"Acierto (precio a favor al vencer): **{_pct(aciertos / n)}** · "
        f"resultado medio con SL/TP tras costes: **{df['resultado_r'].mean():+.2f} R** · "
        f"{'claramente mejor que el azar' if z >= 2 else 'claramente peor que el azar' if z <= -2 else 'no se distingue del azar todavía'} (z = {z:.1f}).",
        "",
        "### Patrones (encontrados en la primera mitad y comprobados en la segunda)",
    ]
    columnas = ["mercado", "temporalidad", "plazo", "franja", "dia", "fuerza_adx", "volatilidad",
                "tendencia_txt", "zona_txt", "estructura_txt", "confianza_tramo"]
    exp = df.assign(estrategia=df["estrategias"].str.split("+")).explode("estrategia")
    lista = patrones(df, columnas) + patrones(exp, ["estrategia"])
    if lista:
        partes += ["| Grupo | Qué hace | Primera mitad | Segunda mitad | Estado |", "|---|---|---|---|---|", *lista]
    else:
        partes.append("Ningún grupo se aparta claramente del 50 % todavía (o faltan casos).")
    partes += ["", "### ¿La confianza sirve? (si funciona, los tramos altos deberían acertar más)",
               _md(tabla(df, "confianza_tramo"))]
    for titulo_t, col, datos in [("Por mercado", "mercado", df), ("Por temporalidad", "temporalidad", df),
                                 ("Por plazo", "plazo", df), ("Por estrategia", "estrategia", exp),
                                 ("Por franja horaria (hora de España)", "franja", df),
                                 ("Por fuerza de la tendencia (ADX)", "fuerza_adx", df),
                                 ("Por volatilidad", "volatilidad", df),
                                 ("A favor o en contra de la tendencia del plazo mayor", "tendencia_txt", df),
                                 ("Zona premium/discount", "zona_txt", df),
                                 ("Estructura de mercado", "estructura_txt", df)]:
        partes += ["", f"### {titulo_t}", _md(tabla(datos, col))]
    peores = df[~df["acierto"]].nsmallest(10, "movimiento_pct")
    partes += ["", "### Los 10 fallos más grandes (para revisar a mano en el gráfico)",
               "| Fecha (España) | Mercado | Velas | Acción | Plazo | Estrategias | Movimiento |", "|---|---|---|---|---|---|---|"]
    for _, f in peores.iterrows():
        partes.append(f"| {f['fecha']:%d/%m %H:%M} | {f['mercado']} | {f['temporalidad']} | {f['accion']} | "
                      f"{int(f['plazo_min'])} min | {f['estrategias']} | {f['movimiento_pct']:+.2f} % |")
    return "\n".join(partes) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archivos", nargs="+")
    parser.add_argument("--salida", default="resultados/INFORME.md")
    args = parser.parse_args()
    secciones = ["# Informe de aciertos y errores",
                 "Generado automáticamente. Un patrón solo cuenta si aparece en la primera mitad de los datos y "
                 "se repite en la segunda; los fallos sueltos son normales y no se corrigen uno a uno.\n"]
    for archivo in args.archivos:
        ruta = Path(archivo)
        titulo = "Laboratorio en directo" if "vivo" in ruta.name else "Simulación sobre el pasado reciente"
        try:
            datos = pd.read_csv(ruta)
        except (FileNotFoundError, pd.errors.EmptyDataError):  # aún no hay señales comprobadas
            datos = pd.DataFrame()
        if datos.empty:
            pendientes = ruta.with_suffix(".json")
            extra = ""
            if pendientes.exists():
                extra = f" ({len(json.loads(pendientes.read_text()))} señales apuntadas, esperando a vencer)"
            secciones.append(f"## {titulo}\n\nTodavía no hay señales comprobadas{extra}.\n")
            continue
        if "acierto" in datos:
            datos = datos[datos["acierto"].notna()]
            datos["acierto"] = datos["acierto"].astype(str).str.lower().isin(["true", "1"])
        secciones.append(informe(datos, titulo))
    Path(args.salida).parent.mkdir(parents=True, exist_ok=True)
    Path(args.salida).write_text("\n".join(secciones), encoding="utf-8")
    print(f"Informe -> {args.salida}")


if __name__ == "__main__":
    main()
