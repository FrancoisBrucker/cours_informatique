import random


class Dice:
    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, nouvelle_position):
        self._position = nouvelle_position

    def roll(self):
        self._position = random.randint(1, 6)

    def __str__(self):
        return str(self.get_position())
