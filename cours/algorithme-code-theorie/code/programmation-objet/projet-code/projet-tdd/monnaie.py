def dollar(montant):
    return Monnaie(montant, "USD")


def franc(montant):
    return Monnaie(montant, "CHF")


class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant
        self.devise = devise

    def __eq__(self, other):
        return self.devise == other.devise and self.montant == other.montant

    def __mul__(self, multiplicateur):
        return Monnaie(self.montant * multiplicateur, self.devise)
