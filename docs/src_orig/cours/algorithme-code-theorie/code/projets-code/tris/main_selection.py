
import matplotlib.pyplot as plt
from mesure import temps_selection

MAX = 2000
PAS = 10

taille = []
temps = []

for x in range(1, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    temps.append(temps_selection(tab))

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)

ax.set_title("complexité du tri par selection")


ax.plot(taille, temps)

plt.show()
