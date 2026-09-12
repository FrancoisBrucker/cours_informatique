import random
from carte import Carte


def jeu32():
    deck = Deck()
    for c in Carte.COULEURS:
        for v in Carte.VALEURS:
            deck.ajoute(Carte(v, c))
    return deck

class Deck:
    def __init__(self):
        self.cartes = []

    def ajoute(self, carte):
        return self.cartes.append(carte)

    def pioche(self):
        return self.cartes.pop()

    def mélange(self):
        random.shuffle(self.cartes)
