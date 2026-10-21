from time import perf_counter
import random
import numpy as np

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcule_max(n, rep=5):
    T = list(range(n))

    s = 0
    for _ in range(rep):
        début = perf_counter()
        recherche(T, n)
        fin = perf_counter()
        s += fin - début
    return s / rep


def calcule_min(n, rep=5):
    T = list(range(n))

    s = 0
    for _ in range(rep):
        début = perf_counter()
        recherche(T, T[0])
        fin = perf_counter()
        s += fin - début
    return s / rep


def calcule_moyenne(n, rep=5):
    T = list(range(n))

    s = 0
    for _ in range(rep):
        début = perf_counter()
        recherche(T, random.randrange(n+1))
        fin = perf_counter()
        s += fin - début
    return s / rep



x = np.linspace(1000, 1000000, 10)
t_min = []
t_max = []
t_moy = []

print("calculs pour", end=" ")
for n in x:
    print(n, end=" ")

    t_min.append(calcule_min(int(n)))
    t_max.append(calcule_max(int(n)))
    t_moy.append(calcule_moyenne(int(n)))
print()


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel("taille du tableau")
ax.set_ylabel("temps de calcul en s")

p1, = ax.plot(x, t_min, 'o-', label="min")
p2, = ax.plot(x, t_moy, 'o-', label="moyenne")
p3, = ax.plot(x, t_max, 'o-', label="max")


ax.legend(handles=(p1, p2, p3))

plt.show()