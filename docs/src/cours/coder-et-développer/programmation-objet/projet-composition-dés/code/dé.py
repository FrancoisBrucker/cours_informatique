import random

class Dé:
    MIN_VALEUR = 1
    MAX_VALEUR = 6

    def __init__(self, position=1):
        self.position = position

    def lancer(self):
        self.position = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)

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


class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dé())

        self.dés = tuple(temp)

    def __str__(self):
        return " - ".join([str(x) for x in self.dés])


    def lancer(self):
        for dé in self.dés:
            dé.lancer()

    def _nombre_positions(self):
        count = [0] * 7
        for dé in self.dés:
            count[dé.position] += 1
        return count

    def nb_dés_valeurs_identiques(self, nb):
        comptes = self._nombre_positions()

        for i in range(len(comptes)):
            if comptes[i] >= nb:
                return True
        return False

    def possède_paire(self):
        return self.nb_dés_valeurs_identiques(2)

    def possède_brelan(self):
        return self.nb_dés_valeurs_identiques(3)

    def possède_carré(self):
        return self.nb_dés_valeurs_identiques(4)
