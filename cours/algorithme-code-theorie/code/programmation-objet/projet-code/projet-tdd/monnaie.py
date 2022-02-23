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

    def __add__(self, other):
        return Somme(self, other)

    def conversion(self, banque, devise):
        return Monnaie(self.montant * banque.change(self.devise, devise), devise)


class Banque:
    def conversion(self, expression, devise):
        return expression.conversion(self, devise)

    def change(self, devise_depart, devise_arrivee):
        if devise_depart == devise_arrivee:
            return 1
        elif devise_depart == "USD":
            return 0.5
        else:
            return 2


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def conversion(self, banque, devise):
        gauche = banque.conversion(self.gauche, devise)
        droite = banque.conversion(self.droite, devise)
        return Monnaie(gauche.montant + droite.montant, devise)

    def __add__(self, other):
        return Somme(self, other)

    def __mul__(self, multiplier):
        return Somme(self.gauche * multiplier, self.droite * multiplier)
