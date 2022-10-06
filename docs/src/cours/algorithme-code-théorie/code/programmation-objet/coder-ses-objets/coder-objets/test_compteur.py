from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert type(c) == Compteur


def test_valeur_initiale():
    c = Compteur()
    assert c.donne_valeur() == 0


def test_incrémente():
    c = Compteur()

    c.incrémente()
    assert c.donne_valeur() == 1

    c.incrémente()
    assert c.donne_valeur() == 2
