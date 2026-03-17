from dé import Dé

position_initiale = int(input("valeur initiale du dé : "))
position_finale = int(input("position finale du dé : "))

dé = Dé()
dé.position = position_initiale

nombre_lancer = 0
while dé.position != position_finale:
    dé.lancer()
    nombre_lancer += 1

print("Il a fallu : ", nombre_lancer, "lancers")
