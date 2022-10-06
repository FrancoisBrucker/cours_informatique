from grille import Grille
from bateau import Bateau


def test_constructeur():
    g = Grille(4, 5)
    assert type(g) == Grille


def test_grille():
    g = Grille(2, 3)
    assert g.matrice == [[".", ".", "."], [".", ".", "."]]


def test_tirer():
    g = Grille(2, 3)

    g.tirer(1, 2)
    assert g.matrice == [[".", "o", "."], [".", ".", "."]]


def test_ajoute_ok():
    g = Grille(2, 3)
    g.ajoute(Bateau(2, 1, longueur=2, vertical=False))

    assert g.matrice == [[".", ".", "."], ["X", "X", "."]]


def test_ajoute_pas_ok():
    g = Grille(2, 3)

    g.ajoute(Bateau(2, 1, longueur=2, vertical=True))
    assert g.matrice == [[".", ".", "."], [".", ".", "."]]

    g.ajoute(Bateau(2, 1, longueur=4, vertical=True))
    assert g.matrice == [[".", ".", "."], [".", ".", "."]]
