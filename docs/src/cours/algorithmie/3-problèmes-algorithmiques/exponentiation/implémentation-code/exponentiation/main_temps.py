import time
import numpy as np
from exponentiation import puissance_naif, puissance_rapide
from mesure_temps import calcul, calcul_n_max, affiche_complexité, affiche_complexité_2, affiche_complexité_twinx

def calcule_max_naif(n):
    return calcul(puissance_naif, (3, n), rep=5)


def calcule_max_rapide(n):
    return calcul(puissance_rapide, (3, n), rep=5)



N_min = 1

T_max = 10**8  # 0.1s
N_max = calcul_n_max(calcule_max_naif, N_min, T_max)
print("Pour", T_max / 10**9, "seconde, N_max =", N_max)


K = 10
Ns = [int(n) for n in np.linspace(N_min, N_max, K)]
print(Ns)

c_naif = []
c_rapide = []
for n in Ns:
    print("taille", n)
    c_naif.append(calcule_max_naif(n))
    print("     max naif :", c_naif[-1])
    c_rapide.append(calcule_max_rapide(n))
    print("     max naif :", c_rapide[-1])

# affiche_complexité(Ns, c_naif)
# affiche_complexité(Ns, c_rapide)

# affiche_complexité_2(Ns, c_naif, c_rapide)

affiche_complexité_twinx(Ns, c_naif, c_rapide)