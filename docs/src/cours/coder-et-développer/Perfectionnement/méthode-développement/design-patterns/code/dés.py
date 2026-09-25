from random import randrange


def d6(valeur=1):
    return DéGénérique(6, valeur)


def d20(valeur=1):
    return DéGénérique(20, valeur)


class Stat:
    def __init__(self):
        self.historique = []

    def update(self, dé):
        self.historique.append(dé.valeur)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))


class DéGénérique(Stat):
    MIN_VALEUR = 1

    def __init__(self, max, valeur=1):
        super().__init__()

        self.MAX_VALEUR = max
        self._valeur = valeur

        self._observateurs = []

    valeur = property(lambda self: self._valeur)

    def lancer(self):
        self._valeur = randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.notify()

        return self

    def add(self, observateur):
        self._observateurs.append(observateur)

    def remove(self, observateur):
        self._observateurs.remove(observateur)

    def notify(self):
        for o in self._observateurs:
            o.update(self)

    def __add__(self, other):
        return Somme(self, other)
    
    def __rmul__(self, x):
        return Multiplication(x , self)


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    valeur = property(
        lambda self: getattr(self.gauche, "valeur", self.gauche)
                     + getattr(self.droite, "valeur", self.droite)
    )

    def lancer(self):
        if hasattr(self.gauche, "lancer"):
            self.gauche.lancer()
        if hasattr(self.droite, "lancer"):
            self.droite.lancer()

        return self

    def __add__(self, other):
        return Somme(self, other)

    def __rmul__(self, x):
        return Multiplication(x, self)

class Multiplication:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    valeur = property(
        lambda self: self.gauche * getattr(self.droite, "valeur", self.droite)
    )

    def lancer(self):
        if hasattr(self.droite, "lancer"):
            self.droite.lancer()

        return self

    def __add__(self, other):
        return Somme(self, other)
    
    def __rmul__(self, x):
        return Multiplication(x * self.gauche, self.droite)
