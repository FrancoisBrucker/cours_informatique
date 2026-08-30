from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_valeur():
    assert Dé().valeur == 1
    assert Dé(valeur=4).valeur == 4


def test_lancer():
    dé = Dé()
    dé.lancer()
    assert Dé.MIN_VALEUR <= dé.valeur <= Dé.MAX_VALEUR


def test_str():
    dé = Dé()
    assert str(dé) == "⚀"
    dé.valeur = 4
    assert str(dé) == "⚃"

def test_repr():
    assert repr(Dé()) == "Dé(valeur=1)"

def test_lt():
    d1 = Dé()
    d2 = Dé()
    assert not d1 < d2

    d2.valeur = 5
    assert d1 < d2
    assert not d2 < d1
