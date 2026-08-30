from random import randrange

import random

class Stat:
    def __init__(self):
        self.valeur = 1
        self.historique = []

    def sauve(self):
        self.historique.append(self.valeur)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))

class DéGénérique(Stat):
    MIN_VALEUR = 1

    def __init__(self, max, valeur=1):
        super().__init__()

        self.MAX_VALEUR = max
        self.valeur = valeur

    def lancer(self):
        self.valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.sauve()


class D6(DéGénérique):
    def __init__(self, valeur=1):
        super().__init__(6, valeur)


class D20(DéGénérique):
    def __init__(self, valeur=1):
        super().__init__(20, valeur)
