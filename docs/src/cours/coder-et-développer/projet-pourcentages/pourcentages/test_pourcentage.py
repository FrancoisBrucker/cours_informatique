from pytest import approx

from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == approx(0)


def test_pourcent_1():
    assert pourcent('00') == approx(100)


def test_pourcent_01():
    assert pourcent('101') == approx(100 / 3)
