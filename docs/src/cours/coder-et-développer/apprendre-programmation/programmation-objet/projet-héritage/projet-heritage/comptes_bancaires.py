class Compte:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def retire(self, montant):
        self.solde -= montant

    def dépose(self, montant):
        self.solde += montant


class CompteCourant(Compte):
    def __init__(self, titulaire, découvert_autorisé):
        super().__init__(titulaire)
        self.découvert_autorisé = découvert_autorisé

    def retire(self, montant):
        if self.découvert_autorisé > self.solde - montant:
            montant = self.solde - self.découvert_autorisé
        super().retire(montant)


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
        super().dépose(montant)

    def retire(self, montant):
        if montant > self.solde:
            montant = self.solde
        super().retire(montant)


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
        super().dépose(montant)

    def retire(self, montant):
        return
