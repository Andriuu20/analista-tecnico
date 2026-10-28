import numpy as np

from plan import riesgo, simular


def _plano(n=200):
    c = np.full(n, 100.0)
    return c + 0.1, c - 0.1, c


def test_take_profit_antes_que_stop():
    h, l, c = _plano()
    h[12] = 103.5
    res, dur = simular(h, l, c, [10], [1], [1.0], 3.0, 0.0)
    assert res[0] == 3.0 and dur[0] == 2


def test_stop_antes_que_take_profit_y_empate_cuenta_como_perdida():
    h, l, c = _plano()
    l[11] = 98.9
    assert simular(h, l, c, [10], [1], [1.0], 3.0, 0.0)[0][0] == -1
    h[11] = 103.5  # toca los dos en la misma vela: se asume lo peor
    assert simular(h, l, c, [10], [1], [1.0], 3.0, 0.0)[0][0] == -1


def test_coste_se_descuenta_en_r():
    h, l, c = _plano()
    h[12] = 103.5
    res, _ = simular(h, l, c, [10], [1], [1.0], 3.0, 0.01)  # 1 % de 100 = 1 R
    assert np.isclose(res[0], 2.0)


def test_sin_futuro_suficiente_no_se_cuenta():
    h, l, c = _plano(30)
    assert np.isnan(simular(h, l, c, [10], [1], [1.0], 2.0, 0.0)[0][0])


def test_regla_del_stop():
    # suelo a 1 ATR por debajo: stop estructural = 1 + 0,1 ATR
    assert np.isclose(riesgo(1, 100.0, 1.0, 105.0, 99.0), 1.1)
    # suelo demasiado lejos (5 ATR): se usa 1,5 ATR
    assert np.isclose(riesgo(1, 100.0, 1.0, 105.0, 95.0), 1.5)
    # sin suelo conocido: 1,5 ATR
    assert np.isclose(riesgo(1, 100.0, 1.0, np.nan, np.nan), 1.5)
