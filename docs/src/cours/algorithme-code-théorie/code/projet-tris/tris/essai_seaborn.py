# 0. import des bibliothèques
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# 1. création des données
x = []
y = []
for i in range(1000):
    x.append(i)
    y.append(i**2)

# 2. créer le dessin (ici ax)
fig, ax = plt.subplots(figsize=(20, 5))

# 2.1 limite des axes
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000000)

# 2.2 les légendes
ax.set_title("la courbe y=x^2")
ax.set_xlabel("x")
ax.set_ylabel("x^2")

# 3. ajouter des choses au dessin avec seaborn
sns.lineplot(ax=ax,
             x=x,
             y=y)

# 4. représenter le graphique
plt.show()
