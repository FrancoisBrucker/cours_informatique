import random
import numpy as np

from mesure_temps import calcul, calcul_n_max, affiche_complexité


def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcule_max(n):
    T = list(range(n))
    return calcul(recherche, (T, -1), rep=5)

def calcule_min(n):
    T = list(range(n))
    return calcul(recherche, (T, 0))

def calcule_moyenne(n, rep=10):
    T = list(range(n))
    t = calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    for _ in range(rep-1):
        t += calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    return t / rep

N_min = 1

T_max = 10 ** 7  # 0.01s
N_max = calcul_n_max(calcule_max, N_min, T_max)
print("Pour", T_max / 10 **9, "seconde, N_max =", N_max)

# N_max = 2097152 # déterminé par le code précédent.

K = 6
Ns = [int(n) for n in np.linspace(N_min, N_max, K)]
print(Ns)

c_min = []
c_moy = []
c_max = []
for n in Ns:
    print("taille", n)
    c_max.append(calcule_max(n))
    print("     max :", c_max[-1])
    c_moy.append(calcule_moyenne(n))
    print("     moy :", c_moy[-1])
    c_min.append(calcule_min(n))
    print("     min :", c_min[-1])

affiche_complexité(Ns, c_min, c_moy, c_max)