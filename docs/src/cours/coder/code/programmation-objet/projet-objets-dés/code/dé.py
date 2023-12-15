import random

MIN_VALEUR = 1
MAX_VALEUR = 6


class Dé:
    def __init__(self, position=1):
        self._positon = 1  # init
        self.position = position  # utilisation du mutateur

    def lancer(self):
        self.position = random.randrange(MIN_VALEUR, MAX_VALEUR + 1)

        return self

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, nouvelle_position):
        if nouvelle_position < MIN_VALEUR:
            nouvelle_position = MIN_VALEUR
        elif nouvelle_position > MAX_VALEUR:
            nouvelle_position = MAX_VALEUR

        self._position = nouvelle_position
