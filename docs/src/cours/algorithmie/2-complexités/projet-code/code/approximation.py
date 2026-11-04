import sys
sys.setrecursionlimit(20010)

import numpy as np

from mesure_temps import calcul, calcul_n_max, affiche_complexité_vs_théorique

def somme(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(1, n+1):
            s += i + j
    return s


def somme_rec(n):
    if n <= 1:
        return 2
    return n * (3 * n - 1) + somme_rec(n-1)


def somme2(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i, n+1):
            s += i + j
    return s


def calcule_complexité(n):
    # return calcul(somme, (n, ), rep=5)
    # return calcul(somme2, (n, ), rep=5)
    return calcul(somme_rec, (n, ), rep=5)


N_min = 1
N_max = 20000

# T_max = 10**6
# N_max = calcul_n_max(calcule_complexité, N_min, T_max)
# print("Pour", T_max / 10**9, "seconde, N_max =", N_max)

K = 10
Ns = [int(n) for n in np.linspace(N_min, N_max, K)]
print(Ns)

c_mesure = []
c_théorie = []

for n in Ns:
    print("taille", n)
    c_mesure.append(calcule_complexité(n))

# affiche_complexité_vs_théorique(Ns, c_mesure, 2)
affiche_complexité_vs_théorique(Ns, c_mesure, 1)