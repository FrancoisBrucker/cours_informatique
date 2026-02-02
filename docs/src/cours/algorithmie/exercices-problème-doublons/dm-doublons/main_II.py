import time

from doppelganger import doppelganger_naif, doppelganger_entrée, doppelganger_tri, doppelganger_bool

n = int(input("Entrez un entier positif ou 0 pour sortir :"))

while n > 0:
    T1 = doppelganger_entrée(n)
    T2 = list(range(1, n))
    T2.append(n-1)

    for T in [T1, T2]:
        t1 = time.perf_counter()
        v = doppelganger_naif(T)
        t2 = time.perf_counter()
        d1 = t2 - t1

        T_prim = list(T)
        t1 = time.perf_counter()
        v2 = doppelganger_tri(T_prim)
        t2 = time.perf_counter()
        d2 = t2 - t1

        t1 = time.perf_counter()
        v3 = doppelganger_bool(T)
        t2 = time.perf_counter()
        d3 = t2 - t1

        print("tableau :", T)
        print("valeur :", v, v2, v3)
        print("temps en ms naif :", 10**6 * d1)
        print("temps en ms tri :", 10**6 * d2)
        print("temps en ms bool :", 10**6 * d3)

    n = int(input("Entrez un entier positif ou 0 pour sortir :"))
