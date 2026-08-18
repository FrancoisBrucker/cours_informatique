from compteur import Compteur


def test_lt():
    assert Compteur(valeur=3) < Compteur(valeur=4)
