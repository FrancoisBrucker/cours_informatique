from bateau import Bateau
from grille import Grille


def test_constructeur():
    b = Bateau(2, 3)
    assert type(b) == Bateau


def test_paramètre_par_défaut():
    b = Bateau(2, 3)

    assert b.longueur == 1
    assert b.vertical


def test_touché_vertical():
    b = Bateau(2, 3, longueur=3)

    assert not b.touché(2, 4)
    assert b.touché(2, 3)
    assert b.touché(3, 3)
    assert b.touché(4, 3)
    assert not b.touché(5, 3)


def test_touché_horizontal():
    b = Bateau(2, 3, longueur=3, vertical=False)

    assert b.touché(2, 3)
    assert b.touché(2, 4)
    assert b.touché(2, 5)
    assert not b.touché(2, 6)


def test_coulé():
    b = Bateau(2, 1, longueur=2, vertical=False)
    g = Grille(2, 3)

    assert not b.coulé(g)

    g.tirer(2, 1)
    assert not b.coulé(g)

    g.tirer(2, 2)
    assert b.coulé(g)
