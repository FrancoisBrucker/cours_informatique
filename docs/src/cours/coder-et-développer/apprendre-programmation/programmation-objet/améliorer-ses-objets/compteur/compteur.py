class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas