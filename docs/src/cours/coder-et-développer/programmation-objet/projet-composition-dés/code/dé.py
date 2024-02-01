import random

MIN_VALEUR = 1
MAX_VALEUR = 6


class Dé:
    def __init__(self, position=1):
        self._positon = 1  # init
        self.position = position  # utilisation du mutateur

    def lancer(self):
        self.position = random.randrange(MIN_VALEUR, MAX_VALEUR + 1)

        return self

    def __str__(self):
        if self.position == 1:
            return "⚀"
        elif self.position == 2:
            return "⚁"
        elif self.position == 3:
            return "⚂"
        elif self.position == 4:
            return "⚃"
        elif self.position == 5:
            return "⚄"
        else:
            return "⚅"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, nouvelle_position):
        if nouvelle_position < MIN_VALEUR:
            nouvelle_position = MIN_VALEUR
        elif nouvelle_position > MAX_VALEUR:
            nouvelle_position = MAX_VALEUR

        self._position = nouvelle_position


class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dé())

        self._dés = tuple(temp)

    def __str__(self):
        return " - ".join([str(x) for x in self.dés])

    @property
    def dés(self):
        return self._dés

    def lancer(self):
        for dé in self.dés:
            dé.lancer()

    def nombre_positions(self):
        count = [0] * 7
        for dé in self.dés:
            count[dé.position] += 1
        return count

    def nb_dés_valeurs_identiques(self, nb):
        comptes = self.nombre_positions()

        for i in range(len(comptes)):
            if comptes[i] >= nb:
                return True
        return False

    def possède_paire(self):
        return self.nb_dés_valeurs_identiques(2)

    def possède_brelan(self):
        return self.nb_dés_valeurs_identiques(3)

    def possède_carre(self):
        return self.nb_dés_valeurs_identiques(4)
