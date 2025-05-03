from rich import print
from classes import Plateau

plateau = Plateau()

r = ""

while r != "stop":
    print(str(plateau))
    r = input("Commande (stop, i, r, v, b, j, u) : ")
    if r == "i":
        plateau.piste.melange()
    elif r in ["r", "v", "b", "j", "u"]:
        plateau.deplace(r.upper())
