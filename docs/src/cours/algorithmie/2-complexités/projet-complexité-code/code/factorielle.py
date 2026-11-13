import sys
sys.setrecursionlimit(20010)

import numpy as np
import matplotlib.pyplot as plt
from math import log

from mesure_temps import calcul, calcul_n_max

def factorielle(n):
    s = 1
    for i in range(1, n+1):
        s *= i   
    return s


def factorielle_rec(n):
    if n<= 1:
        return 1
        
    return n * factorielle_rec(n-1)

def calcule_complexité(n):
    # return calcul(factorielle_rec, (n, ), rep=5)
    return calcul(factorielle, (n, ), rep=5)


N_min = 1

T_max = 10**7 # 0.01s
N_max = calcul_n_max(calcule_complexité, N_min, T_max)
print("Pour", T_max / 10**9, "seconde, N_max =", N_max)

K = 10
Ns = [int(n) for n in np.linspace(N_min, N_max, K)]
print(Ns)

c_mesure = []
c_théorie = []

for n in Ns:
    print("taille", n)
    c_mesure.append(calcule_complexité(n))




_, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel("taille du tableau")
ax.set_ylabel("temps de calcul en ns")

p1, = ax.plot(Ns, c_mesure, 'o-', label="mesurée")

coefs = np.polyfit([x*x * log(x) for x in Ns], c_mesure, 1)
c_théorique = np.polyval(coefs, [x*x * log(x) for x in Ns])


p2, = ax.plot(Ns, c_théorique, 'o-', label="théorique")
ax.legend(handles=(p1, p2))

plt.show()
