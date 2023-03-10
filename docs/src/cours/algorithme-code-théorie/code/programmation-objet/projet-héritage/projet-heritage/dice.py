import random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1):
        self._position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    def roll(self):
        self.position = random.randint(1, self.NUMBER_FACES)


class StatDice(Dice):
    def __init__(self, position=1):
        super().__init__(position)
        self.mémoire = [0] * (self.NUMBER_FACES)

    @property
    def position(self):
        return super().position

    @position.setter
    def position(self, new_position):
        super(type(self), type(self)).position.fset(self, new_position)
        self.mémoire[new_position - 1] += 1

    def stats(self):
        return tuple(self.mémoire)
