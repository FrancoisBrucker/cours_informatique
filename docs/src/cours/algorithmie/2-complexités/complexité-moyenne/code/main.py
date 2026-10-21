from time import perf_counter
import random

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcule_max(n, rep=5):
    T = list(range(n))
    # random.shuffle(T)

    s = 0
    for _ in range(rep):
        début = perf_counter()
        recherche(T, n)
        fin = perf_counter()
        s += fin - début
    return s / rep


def calcule_min(n, rep=5):
    T = list(range(n))
    # random.shuffle(T)

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



x = []
t_min = []
t_max = []
t_moy = []

step = 1000000
print("calculs pour", end=" ")
for n in range(1, 10 * step, step):
    print(n, end=" ")
    x.append(x)
    t_min.append(calcule_min(n))
    t_max.append(calcule_max(n))
    t_moy.append(calcule_moyenne(n))
print()

# for n in range(1, 10 * step, step):
#     print(calcule_max(n) / calcule_moyenne(n), calcule_moyenne(n) / n, calcule_max(n) / n)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel("valeur de l'exposant")
ax.set_ylabel("temps de calcul")

ax.plot(x, t_min, 'o-')
ax.plot(x, t_max, 'o-')
ax.plot(x, t_moy, 'o-')

plt.show()