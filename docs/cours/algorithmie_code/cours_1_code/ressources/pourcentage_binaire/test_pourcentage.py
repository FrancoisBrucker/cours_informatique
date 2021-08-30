from pytest import approx

from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == 0


def test_pourcent_1():
    assert pourcent('00') == 1


def test_pourcent_01():
    assert pourcent('01') == approx(.5)


def test_pourcent_vide():
    assert pourcent('') == 0
