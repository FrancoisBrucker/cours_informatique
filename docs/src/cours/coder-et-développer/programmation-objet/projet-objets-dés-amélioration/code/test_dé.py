from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1
    assert Dé(position=4).position == 4


def test_lancer():
    dé = Dé()
    dé.lancer()
    assert Dé.MIN_VALEUR <= dé.position <= Dé.MAX_VALEUR


def test_str():
    dé = Dé()
    assert str(dé) == "⚀"
    dé.position = 4
    assert str(dé) == "⚃"
