import random


class Personnage:
    def __init__(self, vie, attaque):
        self._vie = vie
        self.attaque = attaque

    def se_faire_taper(self, personnage):
        self.vie -= personnage.attaque

    def taper(self, personnage):
        personnage.se_faire_taper(self)

    @property
    def vie(self):
        return self._vie

    @vie.setter
    def vie(self, valeur):
        self._vie = valeur
        if self._vie <= 0:
            self._vie = 0
            print("je suis mort")


class Guerriere(Personnage):
    def __init__(self, vie, attaque, blocage):
        super().__init__(vie, attaque)
        self.blocage = blocage

    def se_faire_taper(self, personnage):
        if self.blocage >= random.randint(0, 100):
            super().se_faire_taper(personnage)


class Magicien(Personnage):
    def __init__(self, vie, attaque, attaque_magique):
        super().__init__(vie, attaque)
        self.attaque_magique = attaque_magique

    def lancer_sort(self, personnage):
        personnage.vie -= self.attaque_magique

xena = Guerriere(10, 2, 50)
peon = Personnage(5, 1)
gandalf = Magicien(4, 1, 3)

while xena.vie > 0 and peon.vie > 0:
    print("xena : ", xena.vie, " peon : ", peon.vie)
    xena.taper(peon)
    peon.taper(xena)


print("xena : ", xena.vie, " peon : ", peon.vie)

if xena.vie > 0:
    surviant = xena
else:
    surviant = peon

while surviant.vie > 0:
    print("survivant : ", surviant.vie)
    gandalf.lancer_sort(surviant)
