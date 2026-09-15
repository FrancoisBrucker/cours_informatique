class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        return n % self.dénominateur == 0

    def valeur(self, n):
        return (n // self.dénominateur) * self.numérateur


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        i = 0
        sortie = [n]
        while (len(sortie) < N) and (i < len(self.programme)):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                sortie.append(n)
                i = 0
            else:
                i += 1
        return sortie


class Facteur:
    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, exposants):
        valeur = 1
        for i in range(len(exposants)):
            valeur *= self.facteurs[i] ** exposants[i]
        return valeur

    def décomposition(self, n):
        facteurs = [0] * len(self.facteurs)
        for i in range(len(self.facteurs)):
            while n % self.facteurs[i] ** facteurs[i] == 0:
                facteurs[i] += 1
            facteurs[i] -= 1
        return facteurs

