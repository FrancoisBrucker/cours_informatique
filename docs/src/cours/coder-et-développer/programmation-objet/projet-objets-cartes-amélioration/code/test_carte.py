from carte import Carte


def test_constructeur():
    assert isinstance(Carte(Carte.VALEURS.sept, Carte.COULEURS.trèfle), Carte)


def test_str():
    assert str(Carte(Carte.VALEURS.sept, Carte.COULEURS.trèfle)) == "7♣︎"


def test_operator():
    dix_cœur = Carte(Carte.VALEURS.dix, Carte.COULEURS.cœur)
    dix_carreau = Carte(Carte.VALEURS.dix, Carte.COULEURS.carreau)
    
    assert dix_cœur == dix_cœur
    assert dix_cœur != dix_carreau
    assert dix_cœur <= dix_cœur
    assert dix_cœur > dix_carreau
    assert dix_carreau < dix_cœur
