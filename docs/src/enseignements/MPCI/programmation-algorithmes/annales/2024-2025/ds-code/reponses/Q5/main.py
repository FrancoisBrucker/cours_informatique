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
        if plateau.pions[r.upper()] is not None:
            g, d = plateau.piste.gauche_droite(plateau.pions[r.upper()])
            print(str(plateau))
            ok = False
            while not ok:
                r2 = input("    prise (g, d) : ")
                if (r2 == "g") and g is not None:
                    ok = True
                    del plateau.piste.jetons[g]
                elif (r2 == "d") and d is not None:
                    del plateau.piste.jetons[d]
                    ok = True
                else:
                    print("non correct")
