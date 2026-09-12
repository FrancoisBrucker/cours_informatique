from dé import Dé

valeur_initiale = int(input("valeur initiale du dé : "))
valeur_finale = int(input("valeur finale du dé : "))

dé = Dé()
dé.valeur = valeur_initiale

nombre_lancer = 0
while dé.valeur != valeur_finale:
    dé.lancer()
    nombre_lancer += 1

print("Il a fallu : ", nombre_lancer, "lancers")
