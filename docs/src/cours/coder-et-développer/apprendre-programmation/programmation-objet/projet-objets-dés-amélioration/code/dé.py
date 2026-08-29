import random

class Dé:
    MIN_VALEUR = 1
    MAX_VALEUR = 6

    def __init__(self, position=1):
        self.position = position

    def lancer(self):
        self.position = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)

    def __str__(self):
        if self.position == 1:
            return "⚀"
        elif self.position == 2:
            return "⚁"
        elif self.position == 3:
            return "⚂"
        elif self.position == 4:
            return "⚃"
        elif self.position == 5:
            return "⚄"
        else:
            return "⚅"

    def __repr__(self):
        return f"Dé(position={self.position})"

    def __lt__(self, other):
        return self.position < other.position

