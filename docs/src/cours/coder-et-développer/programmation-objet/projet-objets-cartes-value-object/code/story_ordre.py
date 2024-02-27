import random

import carte
from carte import Carte

# créer un paquet de 32 cartes (sans joker)
paquet = []
for valeur in carte.VALEURS:
    for couleur in carte.COULEURS:
        paquet.append(Carte(valeur, couleur))
print(len(set([str(x) for x in paquet])))

# choisir au hasard 10 cartes du paquet
cartes_piochées = random.choices(paquet, k=10)

# afficher à l'écran les 10 cartes, dans l'ordre où elles ont été tirées
for carte in cartes_piochées:
    print(carte)
print("-" * 10)
# afficher à l'écran les 10 cartes, dans l'ordre croissant
cartes_piochées.sort()

for carte in cartes_piochées:
    print(carte)
