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
        valeur = ["sept", "huit", "neuf", "dix", "valet", "dame", "roi", "as"]
        couleur = ["trèfle", "carreau", "cœur", "pique", ]
        return valeur[self.valeur-7] + " de " + couleur[self.couleur - 1]

