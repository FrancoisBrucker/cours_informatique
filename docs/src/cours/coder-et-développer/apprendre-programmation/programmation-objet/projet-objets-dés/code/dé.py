import random

class Dé:
    def __init__(self):
        self.valeur = 1 

    def lancer(self):
        self.valeur = random.randrange(1, 6 + 1)
    
    def texte(self):
        if self.valeur == 1:
            return "⚀"
        elif self.valeur == 2:
            return "⚁"
        elif self.valeur == 3:
            return "⚂"
        elif self.valeur == 4:
            return "⚃"
        elif self.valeur == 5:
            return "⚄"
        else:
            return "⚅"

