from dé import Dé

position_initiale = int(input("valeur initiale du dé : "))
position_finale = int(input("position finale du dé : "))

nombre_lancer = 0
dé = Dé(position_initiale)

if position_initiale != position_finale:
    while position_finale != dé.lancer().position:
        nombre_lancer += 1

print("Il a fallu : ", nombre_lancer, "lancers")
