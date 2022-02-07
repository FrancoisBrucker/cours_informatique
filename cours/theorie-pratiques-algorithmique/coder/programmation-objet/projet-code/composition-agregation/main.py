from panier import Panier

panier = Panier()

print(panier.montre_panier())

panier.ajoute("pomme")

print(panier.montre_panier())

panier.ajoute("pomme")
panier.ajoute("poire")

print(panier.montre_panier())

panier.supprime("pomme")
print(panier.montre_panier())
