import time

from doppelganger import doppelganger_naif, doppelganger_entrée

n = int(input("Entrez un entier positif ou 0 pour sortir :"))

while n > 0:
    T = doppelganger_entrée(n)
    t1 = time.perf_counter()
    v = doppelganger_naif(T)
    t2 = time.perf_counter()
    print("tableau :", T)
    print("valeur :", v)
    print("temps en ms :", 10 ** 6 * (t2 - t1))

    n = int(input("Entrez un entier positif ou 0 pour sortir :"))
