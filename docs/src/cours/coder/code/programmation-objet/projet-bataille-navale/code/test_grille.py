from grille import Grille
from bateau import Bateau


def test_constructeur():
    g = Grille(4, 5)
    assert isinstance(g, Grille)


def test_grille():
    g = Grille(2, 3)
    assert ["∿"] * (2 * 3) == g.matrice


def test_tirer():
    g = Grille(2, 3)

    g.tirer(0, 0)
    assert ["o", "∿", "∿", "∿", "∿", "∿"] == g.matrice

    g.tirer(1, 2)
    assert ["o", "∿", "∿", "∿", "∿", "o"] == g.matrice
    g.tirer(2, 0)
    assert ["o", "∿", "∿", "∿", "∿", "o"] == g.matrice


def test_ajoute_ok():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))

    assert ["∿", "∿", "∿", "⛵", "⛵", "∿"] == g.matrice

def test_ajoute_type_special():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False, type="T"))

    assert ["∿", "∿", "∿", "T", "T", "∿"] == g.matrice


def test_ajoute_pas_ok():
    g = Grille(2, 3)

    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]

    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]
