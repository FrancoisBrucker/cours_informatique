from enum import Enum

class Carte:
    VALEURS = Enum(
        "valeur",
        [
            ("Sept", 7),
            ("Huit", 8),
            ("Neuf", 9),
            ("Dix", 10),
            ("Valet", 11),
            ("Dame", 12),
            ("Roi", 13),
            ("As", 14),
        ],
    )
    COULEURS = Enum(
        "Couleur", [("Pique", 4), ("Cœur", 3), ("Carreau", 2), ("Trèfle", 1)]
    )

    def __init__(self, valeur, couleur):
        self._couleur = couleur
        self._valeur = valeur

    def __str__(self):
        valeur = ["7", "8", "9", "10", "V", "D", "R", "1"]
        couleur = ["♣︎", "♦", "♥", "♠"]
        return valeur[self._valeur.value - 7] + couleur[self._couleur.value - 1]

    def __eq__(self, other):
        return (self._valeur == other._valeur) and (self._couleur == other._couleur)

    def __ge__(self, other):
        return (self._valeur.value > other._valeur.value) or (
            (self._valeur.value == other._valeur.value)
            and (self._couleur.value >= other._couleur.value)
        )

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return (self != other) and (self >= other)

    def __le__(self, other):
        return other >= self

    def __lt__(self, other):
        return (other > self)
