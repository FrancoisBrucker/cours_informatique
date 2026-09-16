from compteur import Compteur

c1 = Compteur()
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c1.valeur, c2.valeur)