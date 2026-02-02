from doppelganger import doppelganger_entrée
from point_fixe import lièvre_tortue, mu

n = int(input("Entrez un entier positif ou 0 pour sortir :"))

while n > 0:
    T = doppelganger_entrée(n + 1)
    x = lièvre_tortue(T)
    print("tableau :", T)
    print("valeur :", x)

    x = mu(T)
    P = [x]
    P.append(T[x])
    while P[0] != P[-1]:
        P.append(T[P[-1]])

    print("Période :", P)
    n = int(input("Entrez un entier positif ou 0 pour sortir :"))
