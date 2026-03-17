import carte
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(carte.SEPT, carte.TREFLE), Carte)


def test_texte():
    assert Carte(carte.SEPT, carte.TREFLE).texte() == "sept de trèfle"

