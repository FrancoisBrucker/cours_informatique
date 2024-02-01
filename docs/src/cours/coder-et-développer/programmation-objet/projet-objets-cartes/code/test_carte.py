import carte
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(carte.SEPT, carte.TREFLE), Carte)


def test_str():
    assert str(Carte(carte.SEPT, carte.TREFLE)) == "sept de trèfle"


def test_repr():
    assert repr(Carte(carte.SEPT, carte.TREFLE)) == "Carte('sept', 'trèfle')"


def test_property():
    assert Carte(carte.SEPT, carte.TREFLE).valeur == carte.SEPT
    assert Carte(carte.SEPT, carte.TREFLE).couleur == carte.TREFLE


def test_operator():
    assert Carte(carte.DIX, carte.COEUR) == Carte(carte.DIX, carte.COEUR)
    assert Carte(carte.DIX, carte.COEUR) != Carte(carte.DIX, carte.CARREAU)
    assert Carte(carte.DIX, carte.COEUR) <= Carte(carte.DIX, carte.COEUR)
    assert Carte(carte.DIX, carte.COEUR) > Carte(carte.DIX, carte.CARREAU)
    assert Carte(carte.DIX, carte.CARREAU) < Carte(carte.DIX, carte.COEUR)
