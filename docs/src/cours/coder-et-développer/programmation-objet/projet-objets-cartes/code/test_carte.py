import carte
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(carte.SEPT, carte.TREFLE), Carte)


def test_texte():
    assert Carte(carte.SEPT, carte.TREFLE).texte() == "7♣︎"


def test_plus_grande_ou_égale_que():
    assert Carte(carte.AS, carte.TREFLE).plus_grande_ou_égale_que(Carte(carte.VALET, carte.PIQUE))
    assert Carte(carte.AS, carte.TREFLE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))
    assert Carte(carte.AS, carte.PIQUE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))
    assert not Carte(carte.VALET, carte.PIQUE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))
