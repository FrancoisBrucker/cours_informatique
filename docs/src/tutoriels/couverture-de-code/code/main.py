from compteur import Compteur

c1 = Compteur(3)
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c1.donne_valeur(), c1)
print(c2.donne_valeur(), c2)

print(c1 < c2)
