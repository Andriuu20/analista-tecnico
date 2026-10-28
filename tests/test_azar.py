"""Con datos aleatorios no hay ventaja posible: el motor debe dar muy pocas señales y casi nunca con
confianza alta. Si se añaden estrategias, este test obliga a recalibrar el umbral de significación.

Se usan 30 series porque las señales falsas se concentran en unas pocas series con «suerte»: con
menos series el resultado depende demasiado de cuáles toquen. Valor medido: ~3 % de velas con
señal y ~1 % con confianza ≥ 55 %."""
from backtest import backtest
from conftest import paseo_aleatorio
from estrategias import calcular
from senal import generar


def test_pocas_senales_falsas_en_datos_aleatorios():
    total = con_senal = confianza_alta = 0
    for semilla in range(30):
        df = paseo_aleatorio(900 + semilla, n=5000)
        _, senales, _ = calcular(df)
        bt = backtest(df["Close"].to_numpy(), senales, 0.0001)
        for t in range(1000, 5000, 20):
            g = generar({k: v[: t + 1] for k, v in senales.items()}, bt, None, 15)
            total += 1
            if g["direccion"]:
                con_senal += 1
                confianza_alta += g["confianza"] >= 0.55
    assert con_senal / total < 0.05, f"demasiadas señales falsas: {con_senal / total:.1%}"
    assert confianza_alta / total < 0.02, f"demasiada confianza falsa: {confianza_alta / total:.1%}"
