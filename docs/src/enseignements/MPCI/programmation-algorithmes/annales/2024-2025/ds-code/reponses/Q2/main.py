from classes import Plateau

plateau = Plateau()

r = ""

while r != "stop":
    print(str(plateau))
    r = input("Commande (stop, i) : ")
    if r == "i":
        plateau.piste.melange()
