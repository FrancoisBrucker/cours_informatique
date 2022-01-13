
import sys

import matplotlib.pyplot as plt

from mesure import temps_rapide

sys.setrecursionlimit(2000)

MAX = 2000
PAS = 10

taille = []
temps = []
temps_max = []

for x in range(1, MAX, PAS):
    taille.append(x)

    t_max, t_moy = temps_rapide(x)
    temps.append(t_moy)
    temps_max.append(t_max)

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)
ax.set_title("complexité du tri par fusion")


ax.plot(taille, temps)
ax.plot(taille, temps_max)

plt.show()
