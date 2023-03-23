from random import randrange


class DéGénérique:
    def __init__(self, max, position=1):
        self._max = max
        self._position = position

    def position(self):
        return self._position

    def lancer(self):
        self._position = randrange(1, self._max + 1)

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)


class D6(DéGénérique):
    def __init__(self, position=1):
        super().__init__(6, position)


class D20(DéGénérique):
    def __init__(self, position=1):
        super().__init__(20, position)


class Cte(DéGénérique):
    def __init__(self, position):
        super().__init__(position, position)

    def lancer(self):
        pass


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def position(self):
        return self.gauche.position() + self.droite.position()

    def lancer(self):
        self.gauche.lancer()
        self.droite.lancer()

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)


class Fois:
    def __init__(self, dé, multiplicateur):
        self.dé = dé
        self.multiplicateur = multiplicateur

    def position(self):
        return self.multiplicateur * self.dé.position()

    def lancer(self):
        self.dé.lancer()

    def __add__(self, other):
        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self.dé, self.multiplicateur * multiplicateur)
