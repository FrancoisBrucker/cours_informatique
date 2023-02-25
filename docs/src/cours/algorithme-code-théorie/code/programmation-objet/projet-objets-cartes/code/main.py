import random

import carte
from carte import Carte


paquet = []
for valeur in carte.VALEURS:
    for couleur in carte.COULEURS:
        paquet.append(Carte(valeur, couleur))

random.shuffle(paquet)

pioche1 = paquet[:16]
défausse1 = []
pioche2 = paquet[16:]
défausse2 = []

MAX_TOUR = 1000

N = 1

while N <= MAX_TOUR and min(len(pioche1), len(pioche2)) > 0:
    print(
        "Tour ",
        N,
        "1 : ",
        len(pioche1),
        "/",
        len(défausse1),
        " ; 2 : ",
        len(pioche2),
        "/",
        len(défausse2),
    )

    carte1 = pioche1.pop()
    carte2 = pioche2.pop()

    print("    1 : ", carte1)
    print("    2 : ", carte2)

    if carte1 > carte2:
        défausse1.extend([carte1, carte2])
        print("    Joueur 1 gagne la carte de l'adversaire")
    else:
        défausse2.extend([carte1, carte2])
        print("    Joueur 2 gagne la carte de l'adversaire")

    if not pioche1:
        pioche1 = défausse1
        random.shuffle(pioche1)
        défausse1 = []

    if not pioche2:
        pioche2 = défausse2
        random.shuffle(pioche2)
        défausse2 = []

    print(pioche1, pioche2)
    N += 1

    # input()

print(N, MAX_TOUR)
if not pioche1:
    print("joueur 1 gagne.")
elif not pioche2:
    print("joueur 2 gagne.")
else:
    print("match nul.")