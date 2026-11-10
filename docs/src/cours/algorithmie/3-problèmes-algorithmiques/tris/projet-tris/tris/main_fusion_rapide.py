
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from mesure import temps_générique_moyen
from tris import fusion, rapide

MAX = 2000
PAS = 10

taille = []
temps1 = []
temps2 = []

for x in range(1, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    temps1.append(temps_générique_moyen(fusion, tab))
    temps2.append(temps_générique_moyen(rapide, tab))

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)
ax.set_title("complexité du tri par fusion et du tri rapide")

sns.lineplot(ax=ax,
             x=taille,
             y=temps1, label="fusion")
sns.lineplot(ax=ax,
             x=taille,
             y=temps2, label="rapide")

plt.show()
