class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def __str__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    def __lt__(self, other):
        return self.valeur < other.valeur

    def ajoute(self):
        self.valeur = self.valeur + self.pas

    def donne_valeur(self):
        return self.valeur


c1 = Compteur(3)
c2 = Compteur()
c1.ajoute()
c2.ajoute()
c1.ajoute()

print(c1.donne_valeur(), c1)
print(c2.donne_valeur(), c2)

print(c1 < c2)
