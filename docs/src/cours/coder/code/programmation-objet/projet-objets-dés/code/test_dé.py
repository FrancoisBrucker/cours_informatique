from dé import Dé, MIN_VALEUR, MAX_VALEUR


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1
    assert Dé(position=3).position == 3


def test_lancer():
    assert MIN_VALEUR <= Dé().lancer().position <= MAX_VALEUR


def test_set_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == 4

    dé.position = 12
    assert dé.position == MAX_VALEUR

    dé.position = -1
    assert dé.position == MIN_VALEUR


def test_get_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == dé._position
