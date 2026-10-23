from time import perf_counter_ns
import random
import gc
import numpy as np

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcul(f, param, rep=5):
    
    gc_actif = gc.isenabled()
    if gc_actif:
        gc.disable()

    t = None
    for _ in range(rep):
        début = perf_counter_ns()
        f(*param)
        fin = perf_counter_ns()

        if (t is None) or (t > fin - début):
            t = fin - début

    if gc_actif:
        gc.enable()
    
    return t

def calcule_max(n):
    T = list(range(n))
    return calcul(recherche, (T, n))

def calcule_min(n):
    T = list(range(n))
    return calcul(recherche, (T, 0))

def calcule_moyenne(n, rep=10):
    T = list(range(n))
    t = calcul(recherche, (T, random.randrange(n+1)))
    for _ in range(rep-1):
        t += calcul(recherche, (T, random.randrange(n+1)))
    return t / rep


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
ax.set_ylabel("temps de calcul en ns")

p1, = ax.plot(x, t_min, 'o-', label="min")
p2, = ax.plot(x, t_moy, 'o-', label="moyenne")
p3, = ax.plot(x, t_max, 'o-', label="max")


ax.legend(handles=(p1, p2, p3))

plt.show()