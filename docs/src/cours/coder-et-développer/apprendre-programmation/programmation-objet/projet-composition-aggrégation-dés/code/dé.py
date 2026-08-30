import random

class Dé:
    MIN_VALEUR = 1
    MAX_VALEUR = 6

    def __init__(self, valeur=1):
        self.valeur = valeur

    def lancer(self):
        self.valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)

        return self

    def __str__(self):
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


class MementoDé:
    def __init__(self, dé):
        self.dé = dé
        self.valeur_sauvée = dé.valeur

    def restore(self):
        self.dé.valeur = self.valeur_sauvée


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

    def _nombre_valeurs(self):
        count = [0] * 7
        for dé in self.dés:
            count[dé.valeur] += 1
        return count

    def nb_dés_valeurs_identiques(self, nb):
        comptes = self._nombre_valeurs()

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


class MementoTapisVert:
    def __init__(self, tapis_vert):
        self.tapis_vert = tapis_vert
        self.valeur_sauvée = [dé.valeur for dé in tapis_vert.dés]

    def restore(self):
        for dé, valeur_sauvée in zip(self.tapis_vert.dés, self.valeur_sauvée):
            dé.valeur = valeur_sauvée
