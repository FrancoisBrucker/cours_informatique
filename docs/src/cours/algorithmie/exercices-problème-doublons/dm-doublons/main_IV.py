import time
import random

from doppelganger import doppelganger_naif, doppelganger_tri, doppelganger_entrée, doppelganger_optimal

n = int(input("Entrez un entier positif ou 0 pour sortir :"))

while n > 0:
    T1 = doppelganger_entrée(n)
    T2 = list(range(1, n))
    random.shuffle(T2)
    T2.append(n-1)

    for T in [T1, T2]:
        t1 = time.perf_counter()
        v = doppelganger_naif(T)
        t2 = time.perf_counter()
        d1 = t2 - t1

        t1 = time.perf_counter()
        v2 = doppelganger_optimal(T)
        t2 = time.perf_counter()
        d2 = t2 - t1

        t1 = time.perf_counter()
        v3 = doppelganger_tri(T)
        t2 = time.perf_counter()
        d3 = t2 - t1

        print("valeur :", v, v3, v2)
        print("temps en ms naif :", 10**6 * d1)
        print("temps en ms tri :", 10**6 * d3)
        print("temps en ms optimal :", 10**6 * d2)

    n = int(input("Entrez un entier positif ou 0 pour sortir :"))
