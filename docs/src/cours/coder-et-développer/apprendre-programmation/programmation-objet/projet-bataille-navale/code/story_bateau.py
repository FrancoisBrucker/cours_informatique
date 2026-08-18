from grille import Grille

grille = Grille(5, 8)

while True:
    print(grille)

    x = int(input(" x = "))
    y = int(input(" y = "))

    grille.tirer(y, x)