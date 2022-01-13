
import matplotlib.pyplot as plt
from mesure import temps_insertion

MAX = 2000
PAS = 10

taille = []
temps_max = []
temps_min = []

for x in range(1, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    temps_min.append(temps_insertion(tab))

    tab.reverse()
    temps_max.append(temps_insertion(tab))

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)
ax.set_title("complexité du tri par insertion")


ax.plot(taille, temps_min)
ax.plot(taille, temps_max)

plt.show()
