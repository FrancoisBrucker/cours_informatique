SEPT = 7
HUIT = 8
NEUF = 9
DIX = 10
VALET = 11
DAME = 12
ROI = 13
AS = 14

PIQUE = 4
COEUR = 3
CARREAU = 2
TREFLE = 1


VALEURS = (SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS)
COULEURS = (TREFLE, CARREAU, COEUR, PIQUE)


class Carte:
    def __init__(self, valeur, couleur):
        self.couleur = couleur
        self.valeur = valeur

    def texte(self):
        valeur = ["7", "8", "9", "10", "V", "D", "R", "1"]
        couleur = ["♣︎", "♦", "♥", "♠"]
        return valeur[self.valeur - 7] + couleur[self.couleur - 1]

    def plus_grande_ou_égale_que(self, other):
        return (self.valeur > other.valeur) or (
            (self.valeur == other.valeur) and (self.couleur >= other.couleur)
        )
