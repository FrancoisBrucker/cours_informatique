from carte import Carte


def test_constructeur():
    assert isinstance(Carte(Carte.VALEURS.Sept, Carte.COULEURS.Trèfle), Carte)


def test_str():
    assert str(Carte(Carte.VALEURS.Sept, Carte.COULEURS.Trèfle)) == "7♣︎"


def test_operator():
    dix_cœur = Carte(Carte.VALEURS.Dix, Carte.COULEURS.Cœur)
    dix_carreau = Carte(Carte.VALEURS.Dix, Carte.COULEURS.Carreau)
    
    assert dix_cœur == dix_cœur
    assert dix_cœur != dix_carreau
    assert dix_cœur <= dix_cœur
    assert dix_cœur > dix_carreau
    assert dix_carreau < dix_cœur
