from random import randint

from grille import Grille
from bateau import Bateau

grille = Grille(5, 8)

longueur = 4
if randint(0, 1) == 0:
    bateau = Bateau(randint(1, 5), randint(1, 5), longueur=longueur, vertical=False)
else:
    bateau = Bateau(randint(1, 2), randint(1, 8), longueur=longueur, vertical=True)

print(bateau.ligne, bateau.colonne, bateau.vertical)

while True:
    for ligne in grille.matrice:
        print("".join(ligne))

    utilisateur = input("donnez une coordonnée x, y :")

    if utilisateur == "quit":
        break

    l, c = eval(utilisateur)

    grille.tirer(l, c)
    if bateau.touché(l, c):
        print("bateau touché !")
    else:
        print("raté")
    
    if bateau.coulé(grille):
        print("bateau coulé.")
        grille.ajoute(bateau)

        for ligne in grille.matrice:
            print("".join(ligne))

        break
