

class Personnage:
    def __init__(self, pv=10, attaque=2):
        self.pv = pv
        self.attaque = attaque

    def get_pv(self):
        return self.pv

    def get_attaque(self):
        return self.attaque

    def set_attaque(self, attaque):
        self.attaque = attaque

    def tape(self, other):
        other.pv -= self.attaque

    def se_faire_taper_par(self, other):
        other.tape(self)


gandalf = Personnage(pv=4)
balrog = Personnage(20, 40)
balrog.tape(gandalf)

print("Le Balrog a donné", balrog.get_attaque(), "dégats à Gandalf")
print("il lui reste : ", gandalf.get_pv(), "pv (le pauvre)")
