
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from mesure import temps_selection

MIN, MAX = 1, 2000
PAS = 10

taille = []
temps = []

for x in range(MIN, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    temps.append(temps_selection(tab))


fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)

ax.set_title("complexité du tri par selection")

# ax.plot(taille, temps)
sns.scatterplot(ax=ax, 
                x=taille, 
                y=temps)

plt.show()
