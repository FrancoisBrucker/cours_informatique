from dice import Dice


def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1


def test_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_roll():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= 6
