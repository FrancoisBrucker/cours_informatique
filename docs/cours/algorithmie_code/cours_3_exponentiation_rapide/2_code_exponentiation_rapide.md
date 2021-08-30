---
layout: page
title:  "Code Exponentiation rapide"
category: cours
tags: informatique cours 
author: "François Brucker"
---


## introduction

Vous allez implémenter les 2 algorithmes en vrai et en python. 

Vous vous concentrerez  sur 3 points :

* on veut que notre code soit juste
* on veut pouvoir le modifier/ajouter des fonctionnalités rapidement
* on veut pouvoir partager notre code avec soit-même dans d'autres projet, son équipe ou le monde)

## le projet exponentiation

suivez le guide.

### crée la structure du projet

* on crée le dossier de notre projet
* On le glisse dans vscode pour que l'éditeur le comprenne.
* on crée un fichier main.py et on vérifie en tapant `print("bonjour monde !")` :
  * que l'on utilise le bon interpréteur python en exécutant le programme
  * que le linter est opérationnel

### le code

On crée 2 fichiers :

* _"exponentielle.py"_
* _"test_exponentielle.py"_

#### exponentielle simple

1. Commencer par créer et tester le code de l'exponentielle simple.
2. Essayer de justifier les tests que vous avez utilisés pour tester votre code :
   * il doit y en avoir assez pour que vous soyez convaincu que votre code fonctionne
   * il ne doit pas y en avoir trop (c'est à dire tester plusieurs fos des  choses qui vont faire la même chose dans le code)
3. une fois que le code est opérationnel (dont les tests passent), créer un programme qui demande deux nombres séparés par une virgule à l'utilisateur et rend l'exponentielle de ces nombres.

#### exponentielle rapide

Faites de même avec l'exponentielle rapide.

Votre programme principale va rendre et le résultat obtenu par l'algorithme simple t par l'algorithme rapide (les deux résultats doivent bien sur coïncider...)

### complexité en temps

L'algorithme rapide doit aller bien plus vite de l'algorithme lent. Vous allez essayer de le voir.

#### se rendre compte du problème

Modifier votre programme principal pour qu'il calcul itérativement toutes les puissances de 2 de $2^1$ à $2^n$ où $n$ est un nombre donné (affecté au début du programme ou donné par un utilisateur).

Ces calculs doivent être fait pour les deux algorithmes : **vous pourrez faire deux fonctions différentes** dans le programme principal et les appeler l'une après l'autre.

Normalement la boucle qui calcule les puissances de 2 pour l'algorithme simple doit aller plus lentement que celle qui calcule toute les puissances de 2 pour l'algorithme rapide.

#### calcul du temps pris

mesurer le temps c'est pas simple parce que :

* notre programme python n'est pas seul sur la machine, tous les programmes actifs s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9)
* python fait des trucs sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)))

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ça ne prend pas tellement de temps que ça. On va utiliser les fonctions simple du module [time](https://docs.python.org/3/library/time.html). Faisons une petite fonction de validation dans un nouveau fichier (que vous pourrez appeler *"expérimentation.py"* par exemple) pour voir comment on peut utiliser la mesure du temps dans notre programme.

Utilisation de la fonction [time](https://docs.python.org/fr/3/library/time.html#time.time) du module [time](https://docs.python.org/3/library/time.html) de python :

```python
import time

depart = time.time()

# le code dont on veut mesurer le temps d'exécution

fin = time.time()

print(fin - depart)  # doit afficher environ 2
```

Testez le code ci-dessus en utilisant la fonction `sleep` (cherchez là dans la doc du [module time](https://docs.python.org/3/library/time.html)) du module time (que fait-elle ?)

Adaptez ensuite le code pour que le programme principal donne le temps mis pour faire tous les calculs avec simple et tous les calculs avec rapide.

## On raffine

### temps et complexité

Rendez deux listes : `temps_simple` et `temps_rapide` de longeur 2000 telle que `temps_simple[i]`  (*respectivement* `temps_rapide[i]`)contienne le temps mis par l'algorithme simple (*resp.* rapide) pour calculer $2^i$.

Comparez les deux listes :

* vers quoi doit tendre `temps_simple[i] / temps_rapide[i]` ?
* `log(temps_simple[i]) / temps_rapide[i]` ?

Vérifiez le expérimentalement.

### dessin des complexité

On va utiliser [matplotlib](https://matplotlib.org/) pour représenter graphiquement nos temps.

#### installation de matplotlib

Pour installer matplotlib plusieurs possibilités :

* directement via pip3/pip :
  * `pip install matplotlib` sous windows
  * `pip3 install matplotlib` sous mac/linux (voir `sudo pip3 install matplotlib` sur unix ou si vous n'avez pas installé python3 avec [brew](https://brew.sh/))
  * avec [anaconda](https://www.anaconda.com/), matplotlib est déjà installé.

#### utilisation basique de matplotlib

> **Remarque** : je vais utiliser les lignes de codes trouvées sur le net et je vais me conformer à l'usage en utilisant `import matplotlib.pyplot as plt` même si ça viole toutes les règles et bonnes pratiques en informatique.

Pour utiliser la  bibliothèque  :

```python
import matplotlib.pyplot as plt
```

Ensuite, la façon dont on procède pour dessier est la suivante :

1. on crée un dessin (composé) avec la commande [subplots](https://www.educative.io/edpresso/what-is-a-subplots-in-matplotlib)
2. on ajoute des éléments à notre dessin (points, courbe, rectangle, disque, etc)
3. on affiche le résultat (ou on le sauve)

exemple :

```python
import matplotlib.pyplot as plt

# 1. créer le dessin (ici ax)
fig, ax = plt.subplots(figsize=(20, 5)) 

#  2 ajouter des choses au dessin

# 2.1 on crée y  x ** 2
x = []
y = []
for i in range(1000):
  x.append(i)
  y.append(i ** 2)

# 2.2 on l'ajoute à notre dessin (l'ax)
ax.plot(x, y)

# 3. représenter le graphique
plt.show()
```

On peut ensuite raffiner en :

* choisissant des [limites aux axes](https://www.tutorialspoint.com/matplotlib/matplotlib_setting_limits.htm)
* ajoutant des [légendes](https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/figure_title.html)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 5)) 

# des axes 
ax.set_xlim(-100, 100)
ax.set_ylim(-1000, 1000)

# les légendes 
ax.set_title("la courbe y=x^2")
ax.set_xlabel('x')
ax.set_ylabel('x^2')


x = []
y = []
for i in range(1000):
  x.append(i)
  y.append(i ** 2)


ax.plot(x, y)

plt.show()
```

Enfin, on peut facilement superposer plusieurs courbes (les couleurs sont au format [rbg](https://fr.wikipedia.org/wiki/Rouge_vert_bleu)) :

```python
import matplotlib.pyplot as plt
  
from math import log

fig, ax = plt.subplots(figsize=(20, 5))

x = range(10, 101)

x_fois_2 = []
x_carre = []
x_log_x = []
for i in x:
    x_fois_2.append(i * 2)
    x_carre.append(i ** 2)
    x_log_x.append(i * log(i))

plt.plot(x, x_fois_2, color="#ff0000")
plt.plot(x, x_carre, color="#00ff00")
plt.plot(x, x_log_x, color="#0000ff")

plt.show()
```

#### à vous

Utilisez les codes précédents  pour superposer les deux listes de temps et voir si l'on obtient bien les courbes théoriques de complexité.
