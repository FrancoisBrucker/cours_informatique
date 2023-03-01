SEPT = "sept"
HUIT = "huit"
NEUF = "neuf"
DIX = "dix"
VALET = "valet"
DAME = "dame"
ROI = "roi"
AS = "as"

PIQUE = "pique"
COEUR = "cœur"
CARREAU = "carreau"
TREFLE = "trèfle"


VALEURS = [SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS]
COULEURS = [TREFLE, CARREAU, COEUR, PIQUE]


class Carte:
    def __init__(self, valeur, couleur):
        self._couleur = couleur
        self._valeur = valeur

    @property
    def couleur(self):
        return self._couleur

    @property
    def valeur(self):
        return self._valeur

    def __str__(self):
        return self.valeur + " de " + self.couleur

    def __repr__(self):
        return "Carte(" + repr(self.valeur) + ", " + repr(self.couleur) + ")"

    def __eq__(self, other):
        return (self.valeur == other.valeur) and (self.couleur == other.couleur)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if VALEURS.index(self.valeur) != VALEURS.index(other.valeur):
            return VALEURS.index(self.valeur) < VALEURS.index(other.valeur)

        return COULEURS.index(self.couleur) < COULEURS.index(other.couleur)

    def __le__(self, other):
        return (self == other) or (self < other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return (self == other) or (self > other)
