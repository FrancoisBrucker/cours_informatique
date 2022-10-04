from dice import Dice, TapisVert


def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1


def test_dice_creation_argument():
    dice = Dice(4)
    assert dice.get_position() == 4


def test_dice_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_dice_roll():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= 6


def test_tapis_vert_creation():
    tapis_vert = TapisVert()

    for d in tapis_vert.get_des():
        assert d.get_position() == 1


def test_tapis_vert_modification():
    tapis_vert = TapisVert()
    tapis_vert.get_des()[2].set_position(5)

    assert tapis_vert.get_des()[2].get_position() == 5


def test_tapis_vert_roll():
    tapis_vert = TapisVert()
    tapis_vert.roll()

    for d in tapis_vert.get_des():
        assert 1 <= d.get_position() <= 6
