class Compteur:
    def __init__(self):
        self.valeur = 0

    def donne_valeur(self):
        return self.valeur

    def incrémente(self):
        self.valeur += 1