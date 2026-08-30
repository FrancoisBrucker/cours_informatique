from panier import Panier, Item

panier = Panier()

print(panier.montre_panier())

mac = Item("macbook", 1000)
print(mac)
panier.ajoute(mac)

print(panier.montre_panier())

panier.ajoute(Item("grosse Rolex", 50000))

print(panier.montre_panier())

panier.supprime(Item("grosse Rolex", 50000))
print(panier.montre_panier())
