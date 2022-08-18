
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from mesure import temps_générique_moyen, temps_générique
from tris import bulles, insertion, sélection

MIN, MAX = 1, 2000
PAS = 10

taille = []
temps1 = []
temps2 = []
temps3 = []

for x in range(MIN, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    temps1.append(temps_générique_moyen(bulles, tab))
    temps2.append(temps_générique_moyen(insertion, tab))
    temps3.append(temps_générique(sélection, tab))


fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)

ax.plot(taille, temps1, label="bulles")
ax.plot(taille, temps2, label="insertion")
ax.plot(taille, temps3, label="sélection")


ax.set_title("complexités de plusieurs tris")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
