"""Registro de señales en vivo: se guardan al darlas y se comprueban al vencer.

Se guarda en un Gist privado de GitHub (si hay GITHUB_TOKEN y GIST_ID en los secretos)
porque el disco de Streamlit Cloud se borra al reiniciar; si no, en un archivo local."""
import json
from pathlib import Path

import pandas as pd
import requests

from datos import MINUTOS, descargar

_ARCHIVO_GIST = "registro.json"
_RUTA_LOCAL = Path(__file__).parent / "registro.json"


class Almacen:
    def __init__(self, token: str | None = None, gist_id: str | None = None):
        self.remoto = bool(token and gist_id)
        self._url = f"https://api.github.com/gists/{gist_id}"
        self._cabeceras = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

    def cargar(self) -> list[dict]:
        if not self.remoto:
            return json.loads(_RUTA_LOCAL.read_text()) if _RUTA_LOCAL.exists() else []
        r = requests.get(self._url, headers=self._cabeceras, timeout=15)
        r.raise_for_status()
        archivo = r.json()["files"].get(_ARCHIVO_GIST)
        if not archivo:
            return []
        contenido = archivo["content"]
        if archivo.get("truncated"):
            contenido = requests.get(archivo["raw_url"], headers=self._cabeceras, timeout=15).text
        return json.loads(contenido or "[]")

    def guardar(self, entradas: list[dict]) -> None:
        texto = json.dumps(entradas, ensure_ascii=False, indent=1)
        if not self.remoto:
            _RUTA_LOCAL.write_text(texto)
            return
        r = requests.patch(self._url, headers=self._cabeceras, timeout=15,
                           json={"files": {_ARCHIVO_GIST: {"content": texto}}})
        r.raise_for_status()


def nueva_entrada(activo: str, cfg: dict, codigo: str, vela: pd.Timestamp, precio: float, senal: dict) -> dict:
    minutos = MINUTOS[codigo]
    entrada = vela + pd.Timedelta(minutes=minutos)  # la operación empieza al cerrar la vela
    return {
        "id": f"{cfg['simbolo']}|{codigo}|{vela.isoformat()}",
        "activo": activo,
        "fuente": cfg["fuente"],
        "simbolo": cfg["simbolo"],
        "intervalo": codigo,
        "vela": vela.isoformat(),
        "entrada": entrada.isoformat(),
        "vencimiento": (entrada + pd.Timedelta(minutes=minutos * senal["horizonte"])).isoformat(),
        "accion": senal["accion"],
        "direccion": senal["direccion"],
        "horizonte": senal["horizonte"],
        "confianza": round(senal["confianza"], 4),
        "estrategias": senal["estrategias"],
        "precio_entrada": precio,
        "precio_salida": None,
        "resultado": "pendiente",
    }


def anadir(entradas: list[dict], entrada: dict) -> bool:
    """Añade la señal si no estaba ya (misma vela, activo e intervalo). Devuelve si se añadió."""
    if any(e["id"] == entrada["id"] for e in entradas):
        return False
    entradas.append(entrada)
    return True


def resolver(entradas: list[dict], descargar_fn=descargar) -> bool:
    """Comprueba las señales vencidas. Devuelve True si alguna cambió."""
    ahora = pd.Timestamp.now(tz="UTC")
    vencidas = [e for e in entradas if e["resultado"] == "pendiente" and pd.Timestamp(e["vencimiento"]) <= ahora]
    cambios = False
    grupos = {}
    for e in vencidas:
        grupos.setdefault((e["fuente"], e["simbolo"], e["intervalo"]), []).append(e)
    for (fuente, simbolo, codigo), lista in grupos.items():
        try:
            df, _ = descargar_fn(fuente, simbolo, codigo)
        except Exception:
            continue
        for e in lista:
            vela = pd.Timestamp(e["vela"])
            if vela not in df.index:
                if vela < df.index[0]:  # demasiado antigua: el proveedor ya no la ofrece
                    e["resultado"] = "sin datos"
                    cambios = True
                continue
            pos = df.index.get_loc(vela) + e["horizonte"]
            if pos >= len(df):
                continue  # el mercado aún no ha cerrado esas velas (p. ej. fin de semana)
            salida = float(df["Close"].iat[pos])
            e["precio_salida"] = salida
            e["resultado"] = "acierto" if (salida - e["precio_entrada"]) * e["direccion"] > 0 else "fallo"
            cambios = True
    return cambios


def estadisticas_vivo(entradas: list[dict], simbolo: str, codigo: str) -> pd.DataFrame:
    """Aciertos reales por estrategia y horizonte, para alimentar el cálculo de la señal."""
    filas = [
        {"estrategia": est, "horizonte": e["horizonte"], "acierto": e["resultado"] == "acierto"}
        for e in entradas
        if e["simbolo"] == simbolo and e["intervalo"] == codigo and e["resultado"] in ("acierto", "fallo")
        for est in e["estrategias"]
    ]
    if not filas:
        return pd.DataFrame(columns=["estrategia", "horizonte", "vivo_aciertos", "vivo_total"])
    df = pd.DataFrame(filas)
    return (df.groupby(["estrategia", "horizonte"])["acierto"]
              .agg(vivo_aciertos="sum", vivo_total="count").reset_index())
