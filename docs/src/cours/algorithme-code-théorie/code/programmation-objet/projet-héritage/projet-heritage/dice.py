import random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def roll(self):
        self.set_position(random.randint(1, self.NUMBER_FACES))


class StatDice(Dice):
    def __init__(self, position=1):
        super().__init__(position)
        self.mémoire = [0] * (self.NUMBER_FACES)

    def set_position(self, new_position):
        super().set_position(new_position)
        self.mémoire[new_position - 1] += 1

    def stats(self):
        return tuple(self.mémoire)
