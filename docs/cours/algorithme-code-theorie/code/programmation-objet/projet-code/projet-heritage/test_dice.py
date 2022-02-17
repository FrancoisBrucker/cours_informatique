from dice import Dice, StatDice


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


def test_statDice_init():
    dice = StatDice()
    assert dice.stats() == (0, 0, 0, 0, 0, 0)


def test_statDice_roll():
    dice = StatDice()
    dice.roll()
    assert sum(dice.stats()) == 1


def test_statDice_position():
    dice = StatDice()
    dice.set_position(4)
    assert dice.stats() == (0, 0, 0, 1, 0, 0)
