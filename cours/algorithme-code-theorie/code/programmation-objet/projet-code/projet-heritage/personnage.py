import random


class Personnage:
    def __init__(self, vie, attaque):
        self._vie = vie
        self.attaque = attaque

    def se_faire_taper(self, personnage):
        self.set_vie(self.get_vie() - personnage.attaque)

    def taper(self, personnage):
        personnage.se_faire_taper(self)

    def get_vie(self):
        return self._vie

    def set_vie(self, valeur):
        self._vie = valeur
        if self._vie <= 0:
            self._vie = 0


class Guerriere(Personnage):
    def __init__(self, vie, attaque, blocage):
        super().__init__(vie, attaque)
        self.blocage = blocage

    def se_faire_taper(self, personnage):
        if self.blocage < random.randint(0, 100):
            super().se_faire_taper(personnage)


class Magicien(Personnage):
    def __init__(self, vie, attaque, attaque_magique):
        super().__init__(vie, attaque)
        self.attaque_magique = attaque_magique

    def lancer_sort(self, personnage):
        personnage.set_vie(personnage.get_vie() - self.attaque_magique)


class Equipement:
    def has(self, event):
        return False

    def react(self, event):
        return None