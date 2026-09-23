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

        return self


def d6(valeur=1):
    return DéGénérique(6, valeur)

def d20(valeur=1):
    return DéGénérique(20, valeur)
