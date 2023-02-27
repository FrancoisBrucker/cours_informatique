from random import randint

from grille import Grille
from bateau import Bateau

grille = Grille(8, 10)

porte_avion = Bateau(2, 4, 4, True, "🚢")
croiseur = Bateau(4, 0, 3, False, "⛴")
torpilleur = Bateau(5, 8, 2, True, "🚣")
sous_marin = Bateau(7, 9, 1, True, "🐟")

bateaux = [porte_avion, croiseur, torpilleur, sous_marin]
# bateaux = [sous_marin]

grille_visuelle = Grille(8, 10)


for b in bateaux:
    grille_visuelle.ajoute(b)

print("====== CHEAT ======")
print(grille_visuelle)
print("===================")

N = 0


while True:
    N += 1
    print(grille)

    utilisateur = input("donnez une coordonnée x, y :")

    if utilisateur == "quit":
        break

    l, c = eval(utilisateur)

    grille.tirer(l, c)
    for b in bateaux:
        if (l, c) in b.positions:
            print("bateau touché !")
            grille.tirer(l, c, "💣")

    tous_coulés = True
    for b in bateaux:
        if b.coulé(grille):
            grille.ajoute(b)
            print(b.type, "coulé !")
        else:
            print(b.type, "encore en vie.")
            tous_coulés = False
    if tous_coulés:
        break            

print(grille)
print("fini en", N, "coups.")