from bateau import Bateau
from grille import Grille


def test_constructeur():
    b = Bateau(2, 3)
    assert type(b) == Bateau


def test_paramètre_par_défaut():
    b = Bateau(2, 3)

    assert b.longueur == 1
    assert not b.vertical


def test_paramètres():
    b = Bateau(2, 3, 4, True)

    assert b.longueur == 4
    assert b.vertical


def test_positions():
    assert [(2, 3), (2, 4), (2, 5)] == Bateau(2, 3, longueur=3).positions
    assert [(2, 3), (3, 3), (4, 3)] == Bateau(2, 3, longueur=3, vertical=True).positions


def test_coulé():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2)

    print(b.coulé(g))
    assert not b.coulé(g)

    g.tirer(1, 0)
    assert not b.coulé(g)

    g.tirer(1, 1)
    assert b.coulé(g)
