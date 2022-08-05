from tapisvert import TapisVert


def test_init():
    tv = TapisVert()
    assert tv is not None


def test_somme():
    tv = TapisVert()

    assert tv.somme() == 5


def test_roll():
    tv = TapisVert()
    tv.roll()
    for d in tv.get_des():
        assert 1 <= d.get_position() <= 6
