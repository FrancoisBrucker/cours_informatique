from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1

def test_lancer():
    dé = Dé()
    dé.lancer()
    assert 1 <= dé.position <= 6
