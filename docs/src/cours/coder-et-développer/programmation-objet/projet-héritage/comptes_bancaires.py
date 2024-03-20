class Compte:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def retire(self, montant):
        self.solde -= montant
        return montant

    def dépose(self, montant):
        self.solde += montant
        return montant


class CompteCourant(Compte):
    def __init__(self, titulaire, découvert_autorisé):
        super().__init__(titulaire)
        self.découvert_autorisé = découvert_autorisé

    def retire(self, montant):
        if self.découvert_autorisé > self.solde - montant:
            montant = self.solde - self.découvert_autorisé
        return super().retire(montant)


class CompteÉpargne(Compte):
    def __init__(self, titulaire, taux_intérêt, plafond):
        super().__init__(titulaire)
        self.taux_intérêt = taux_intérêt
        self.plafond = plafond

    def calcule_intérêts(self):
        return self.taux_intérêt * self.solde

    def dépose(self, montant):
        if self.solde + montant > self.plafond:
            montant = self.plafond - self.solde
        return super().dépose(montant)

    def retire(self, montant):
        if montant > self.solde:
            montant = self.solde
        return super().retire(montant)


class LivretA(CompteÉpargne):
    def __init__(self, titulaire):
        super().__init__(titulaire, taux_intérêt=0.03, plafond=22950)


class PEL(CompteÉpargne):
    def __init__(self, titulaire, année_ouverture):
        super().__init__(titulaire, taux_intérêt=0.02, plafond=61200)
        self.année_ouverture = année_ouverture

    def dépose(self, montant, année):
        if année > self.année_ouverture + 10:
            montant = 0
        return super().dépose(montant)

    def retire(self, montant):
        return 0


if __name__ == "__main__":

    cc = CompteCourant("M. X", -1000)
    print(cc)
    print("Dépot", cc.dépose(100))
    print(cc.solde)
    print("Retrait", cc.retire(700))
    print(cc.solde)
    print("Retrait", cc.retire(600))
    print(cc.solde)

    a = LivretA("Mme T")
    print(a)
    print("Dépot", a.dépose(1000))
    print(a.solde)
    print("Dépot", a.dépose(25000))
    print(a.solde)
    print("Intérêts", a.calcule_intérêts())
    print(a.solde)
    print("Retrait", a.retire(15000))
    print(a.solde)
    print("Retrait", a.retire(15000))
    print(a.solde)

    p = PEL("Mme Z", année_ouverture=2011)
    print(p)
    print("Dépot (2017)", p.dépose(1000, 2017))
    print(p.solde)
    print("Dépot (2022)", p.dépose(1000, 2022))
    print(p.solde)
    print("Intérêts", p.calcule_intérêts())
    print(p.solde)
    print("Retrait", p.retire(700))
    print(p.solde)
    print("Retrait", p.retire(700))
    print(p.solde)
