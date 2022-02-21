class Monnaie:
    def __init__(self, montant):
        self.montant = montant

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.montant == other.montant


class Dollar(Monnaie):
    def __mul__(self, multiplicateur):
        return Dollar(self.montant * multiplicateur)


class Franc(Monnaie):
    def __mul__(self, multiplicateur):
        return Franc(self.montant * multiplicateur)
