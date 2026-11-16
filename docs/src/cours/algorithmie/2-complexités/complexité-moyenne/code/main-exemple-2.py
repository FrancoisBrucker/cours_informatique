from time import perf_counter_ns
import random
import gc
import numpy as np


def maximum(T):
    m = T[0]
    for x in T:
        if m < x:
            m = x
    return m

def maximum_compte(T):
    m = T[0]
    c = 1
    for x in T:
        if m < x:
            c += 1
            m = x
    return m, c


def calcule_moyenne(n, rep=10):
    T = list(range(n))
    random.shuffle(T)
    t = maximum_compte(T)[1]
    for _ in range(rep-1):
        t += maximum_compte(T)[1]
    return t / rep


x = np.linspace(1000, 1000000, 10)
n_moy = []

print("calculs pour :")
for n in x:
    print(n)
    n_moy.append(calcule_moyenne(int(n), 20))
    print("    ", n_moy[-1])
print()


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("Maximum d'un tableau")
ax.set_xlabel("taille du tableau")
ax.set_ylabel("nombre de mise à jour moyenne")

p1, =  ax.plot(x, n_moy, 'o-', label="moyenne")

ax.legend(handles=(p1, ))

plt.show()