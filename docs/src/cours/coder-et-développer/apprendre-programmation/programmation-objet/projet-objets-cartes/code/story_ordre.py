import random

import carte
from carte import Carte

# créer un paquet de 32 cartes (sans joker)
paquet = []
for valeur in carte.VALEURS:
    for couleur in carte.COULEURS:
        paquet.append(Carte(valeur, couleur))

# choisir au hasard 10 cartes du paquet
cartes_piochées = random.choices(paquet, k=10)

# afficher à l'écran les 10 cartes, dans l'ordre où elles ont été tirées
min_carte = cartes_piochées[0]
max_carte = cartes_piochées[0]

for carte in cartes_piochées:
    print(carte.texte())
    if min_carte.plus_grande_ou_égale_que(carte):
        min_carte = carte
    if carte.plus_grande_ou_égale_que(max_carte):
        max_carte = carte

# afficher à l'écran le min et le max des 10 cartes 
print("min :", min_carte.texte())
print("max :", max_carte.texte())
