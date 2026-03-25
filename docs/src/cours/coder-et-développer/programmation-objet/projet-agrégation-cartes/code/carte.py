from enum import Enum


class Carte:
    VALEURS = Enum(
        "valeur",
        [
            ("sept", 7),
            ("huit", 8),
            ("neuf", 9),
            ("dix", 10),
            ("valet", 11),
            ("dame", 12),
            ("roi", 13),
            ("as", 14),
        ],
    )
    COULEURS = Enum(
        "Couleur", [("pique", 4), ("cœur", 3), ("carreau", 2), ("trèfle", 1)]
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
        return (self._valeur.value >= other._valeur.value) or (
            (self._valeur.value == other._valeur.value)
            and (self._couleur.value >= other._couleur.value)
        )

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return (self != other) and (self <= other)

    def __le__(self, other):
        return other >= self

    def __lt__(self, other):
        return other > self


class Deck:
    pass