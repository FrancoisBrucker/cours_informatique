import random


def affiche_plateau(piste):
    return "".join(piste) + " " + "01234"


piste = (
    ["B"] * 9 + ["R"] * 9 + ["J"] * 9 + ["V"] * 9 + ["U"] * 9 + ["X"] * 5 + ["O"] * 5
)


r = ""
random.shuffle(piste)

while r != "stop":
    print(affiche_plateau(piste))
    r = input("Commande (stop, i) : ")
    if r == "i":
        random.shuffle(piste)
