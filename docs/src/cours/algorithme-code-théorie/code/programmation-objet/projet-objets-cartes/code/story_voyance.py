import random

import carte
from carte import Carte

# création d'un paquet de 32 cartes
paquet = []
for valeur in carte.VALEURS:
    for couleur in carte.COULEURS:
        paquet.append(Carte(valeur, couleur))

# prendre au hasard 3 cartes du paquet
cartes_piochées = random.sample(paquet, k=3)

# afficher à l'écran les trois cartes, dans l'ordre où elles ont été tirées
for carte in cartes_piochées:
    print(carte)