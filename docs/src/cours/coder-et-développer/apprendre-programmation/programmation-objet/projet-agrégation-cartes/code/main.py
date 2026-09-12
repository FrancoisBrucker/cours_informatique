import random

from carte import Carte
from deck import Deck, jeu32


paquet = jeu32()
paquet.mélange()

pioche1 = Deck()
défausse1 = Deck()
pioche2 = Deck()
défausse2 = Deck()

for _ in range(16):
    pioche1.ajoute(paquet.pioche())
    pioche2.ajoute(paquet.pioche())

MAX_TOUR = 1000

N = 1

while N <= MAX_TOUR and min(len(pioche1.cartes), len(pioche2.cartes)) > 0:
    print(
        "Tour ",
        N,
        "1 : ",
        len(pioche1.cartes),
        "/",
        len(défausse1.cartes),
        " ; 2 : ",
        len(pioche2.cartes),
        "/",
        len(défausse2.cartes),
    )

    carte1 = pioche1.pioche()
    carte2 = pioche2.pioche()

    print("    1 : ", carte1)
    print("    2 : ", carte2)

    if carte2 <= carte1:
        défausse1.ajoute(carte1)
        défausse1.ajoute(carte2)
        print("    Joueur 1 gagne la carte de l'adversaire")
    else:
        défausse2.ajoute(carte1)
        défausse2.ajoute(carte2)
        print("    Joueur 2 gagne la carte de l'adversaire")

    if len(pioche1.cartes) == 0:
        pioche1 = défausse1
        pioche1.mélange()
        défausse1 = Deck()

    if len(pioche2.cartes) == 0:
        pioche2 = défausse2
        pioche2.mélange()
        défausse2 = Deck()

    N += 1

    # input()

print(N, MAX_TOUR)
if len(pioche1.cartes) == 0:
    print("joueur 1 gagne.")
elif len(pioche2.cartes) == 0:
    print("joueur 2 gagne.")
else:
    print("match nul.")