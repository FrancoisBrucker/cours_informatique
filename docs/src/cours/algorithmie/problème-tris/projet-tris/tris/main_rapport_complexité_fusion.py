
from math import log

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from mesure import temps_générique
from tris import fusion

MIN, MAX = 50, 20000
PAS = 50

taille = []
rapport = []

for x in range(MIN, MAX, PAS):
    taille.append(x)

    tab = list(range(x))
    
    rapport.append(temps_générique(fusion, tab) / (x * log(x)))
    


fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)

sns.regplot(ax=ax, x=taille, y=rapport, label="rapport")


ax.set_title("rapport de complexité")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
