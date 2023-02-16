from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert type(c) == Compteur


def test_valeur_initiale():
    c = Compteur()
    assert c.valeur == 0


def test_incrémente():
    c = Compteur()

    c.incrémente()
    assert c.valeur == 1

    c.incrémente()
    assert c.valeur == 2
