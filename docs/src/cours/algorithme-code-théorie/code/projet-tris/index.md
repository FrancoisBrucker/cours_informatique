---
layout: layout/post.njk 
title: "Projet : tris"

eleventyNavigation:
  key: "Projet : tris"
  parent: Code
---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb(eleventyNavigation.key, { includeSelf: true}) -%}
{% if not loop.first %} / {%endif%} [{{page.title}}]({{ page.url | url }})
{%- endfor -%}
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Projet exponentiation](../projet-exponentiation)
* [étude : trier un tableau](../../algorithme/étude-tris)

{% endprerequis %}

<!-- début résumé -->

On code des tris et on vérifie que nos algorithmes fonctionnent.

<!-- end résumé -->

## Mise en place

### Structures

{% faire %}

1. créez un dossier nommé `tris`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier
3. créez dans ce dossier les 2 fichiers de la trinité du code (on fera plusieurs `main`{.fichier} ensuite) :
   * `tris.py`{.fichier} : où vous placez les algorithmes de tris
   * `test_tris.py`{.fichier}  : où vous placez les tests des algorithmes de tris

{% endfaire %}

### Vérifications

{% faire %}

* on vérifie que python est ok avec le terminal et avec vscode
* on vérifie que le linter est actif dans vscode
* on vérifie que les tests fonctionnent (en créant un test bidon dans `tests_tris.py`{.fichier} et en vérifiant que `pytest` et vscode le trouvent)

{% endfaire %}

## Tris basiques

En reprenant le code donné dans l'[étude des tris](../../algorithme/étude-tris) :

{% faire %}
Implémentez :

* l'algorithme du tri `insertion`{.language-} et ses tests
* l'algorithme du tri `sélection`{.language-} et ses tests

{% endfaire %}

Pour les tests des algorithmes de tri, vous pouvez par exemple utiliser 3 tableaux différents :

* le tableau des $5$ premiers entiers triés par ordre croissant
* le tableau des $5$ premiers entiers triés par ordre décroissant
* le tableau des $5$ premiers entiers mélangé (choisissez une permutation)

### Complexités

Nous allons (enfin plutôt, vous allez) afficher les complexités temporelles des différents algorithmes de tri que vous avez codés.

Pour faire cela, on utilisera ce que nous avons fait pendant le [projet exponentiation](..code/projet-exponentiation).

{% faire %}
Créez un fichier `mesure.py`{.fichier}
{% endfaire %}

#### Tri par sélection

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_sélection`{.language-} qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.

{% endexercice %}

{% exercice %}

Dans un fichier `main_sélection`{.fichier}, affichez sur un graphique courbe du temps mis (axe des ordonnées) pour trier avec `sélection`{.fichier} le tableau des $n$ premiers entiers triés, pour une taille $n$ (axe des abscisses) allant de 1 à 2000 par pas de 10.

A quel type de complexité correspond cette mesure ?
{% endexercice %}

#### Tri par insertion

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_insertion`{.language-}  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.
{% endexercice %}

{% exercice %}

* pour quel type de tableau est atteint la complexité minimale de l'algorithme `insertion`{.language-} ?
* pour quel type de tableau est atteint la complexité maximale de l'algorithme `insertion`{.language-} ?

Utilisez ces tableaux pour affichez sur un même graphique :

* la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion des tableaux de taille $n$ (axe des abscisses) réalisant la complexité minimale
* la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion  des tableaux de taille $n$ (axe des abscisses) réalisant la complexité maximale

Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{% endexercice %}

Comme la complexité minimale et maximale du tri par insertion sont différentes, les deux courbes doivent être distinctes.

{% exercice %}
L'allure des 2 courbes est-elle conforme aux résultats théoriques de complexité ?
{% endexercice %}

Pour connaître l'espérance de la complexité, il faut calculer la complexité en moyenne de l'algorithme. Pour cela il faut pouvoir créer un tableau aléatoire et calculer le temps mis pour le trier. Pour éviter tout cas particulier, on fait des moyennes de mesures.

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} la fonction `temps_insertion_moyen`{.language-} qui rend la moyenne de 10 temps pris pour trier avec `insertion`{.language-} une permutation aléatoire du tableau en entrée.
{% endexercice %}

Pour mélanger une liste python, vous pouvez utiliser la fonction [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) du module random.

On peut maintenant visualiser les temps minimum, maximum et moyen de notre algorithme :

{% exercice %}

Dans le fichier `main_insertion`{.fichier}, en utilisant `temps_insertion_moyen`{.language-}, ajoutez au graphique la courbe de la moyenne des temps mis (axe des ordonnées) pour trier 10 tableaux aléatoire de taille $n$ (axe des abscisses) avec l'algorithme `insertion`{.language-}.

Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{% endexercice %}

## Tri à bulles

{% exercice %}
Implémentez [le tri à bulle optimisé](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) dans le fichier `tris.py` (nommez l'algorithme `bulles`) et ses tests dans le fichier `test_tris.py`.

{% endexercice %}

### Complexités du tri à bulle

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_bulles_moyen`{.language-} qui rend la moyenne de 10 temps pris pour trier avec `bulles` une permutation aléatoire du tableau en entrée.
{% endexercice %}

Pour ne pas refaire la même chose que pour le calcul de la complexité en moyenne du tri par `insertion`{.language-}, vous pourrez utiliser le fait que l'on peut passer une fonction en paramètre d'une autre (comme on a fait dans l'[étude sur les mélange](../../étude-mélange#fonction-en-paramètre)) !

Vous pourrez ainsi modifier l'exemple ci-dessous pour forger une fonction qui rend le temps moyen pris pour trier 10 listes de taille $n$.

```python
import random, time

def temps_tri(tri, T):

    d = time.time()
    tri(T)
    f = time.time()
 
    return f - d

def temps_insertion(T):
    return temps_tri(insertion, T)  # en supposant qu'une fonction insertion existe

```

{% exercice %}

Dans le fichier `mesures.py`{.fichier} Créez une fonction :

* `temps_générique(algorithme, tableau)`{.language-} qui rend le temps mis par l'algorithme de nom `algorithme`{.language-} pour trier `tableau`{.language-}
* `temps_générique_moyen(algorithme, tableau)`{.language-} qui rend la moyenne de 10 temps pris pour trier avec l'algorithme de nom `algorithme`{.language-} une permutation aléatoire du tableau `tableau`{.language-} en entrée.

{% endexercice %}

{% exercice %}
Modifiez vos fonctions `temps_sélection`{.language-}, `temps_insertion`{.language-}, `temps_sélection_moyen`{.language-}, `temps_insertion_moyen`{.language-} et `temps_bulles_moyen`{.language-} pour qu'elles utilisent les fonctions `temps_générique`{.language-} et `temps_générique_moyen`{.language-}.
{% endexercice %}

### Adéquation à la théorie

{% exercice %}

Dans le fichier `main_bulles`{.fichier}, en utilisant `temps_générique`{.language-} et `temps_générique_moyen`{.language-}, créez le graphique des complexités minimales, maximales et moyenne pour le tri à bulle.

Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{% endexercice %}

## Comparaison

{% exercice %}
Dans le fichier `main_comparaison`{.fichier}, en utilisant `temps_bulles_moyen`{.language-}, `temps_insertion_moyen`{.language-} et `temps_sélection`{.language-} afficher simultanément les temps pris pour pour trier 10 tableaux aléatoire de taille $n$ (axe des abscisses) avec l'algorithme `bulles`{.language-}, `insertion`{.language-} et `sélection`{.language-}.

Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.

Quel est l'algorithme le plus efficace ?

{% endexercice %}

### Visualisation

{% faire %}
Copiez le code suivant dans un fichier `main_visu.py`{.fichier} :

```python
import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    ax.cla()  # on efface le dessin
    ax.plot(tab, 'ro')
    plt.pause(0.1)  # on pause le dessin


def insertion_visu(T):
    for i in range(1, len(T)):
        courant = T[i]
        j = i
        while (j > 0) and (courant < T[j - 1]):
            T[j] = T[j - 1]
            draw_tab(T)  # on affiche le tableau

            j -= 1
        T[j] = courant
        draw_tab(T)
    draw_tab(tab)


fig, ax = plt.subplots(figsize=(20, 5))

tab = list(range(30))
random.shuffle(tab)

print(tab)

ax.plot(tab, 'ro')
insertion_visu(tab)

print(tab)
```

{% endfaire %}

Le code précédent modifie l'algorithme `insertion`{.language-} pour qu'il affiche dans un graphique le tableau après chaque modification.

{% faire %}

1. Exécutez le code précédent, et comprenez pourquoi il fonctionne.
2. Ajoutez une modification du tri par `sélection` pour le voir trier le même tableau et voir les différences entre les deux algorithmes.
3. Ajoutez une modification du tri par `bulles` pour le voir trier le même tableau et voir les différences entre les trois algorithmes.

{% endfaire %}

## Pimp les dessins

Pour rende les dessins plus agréable à l'œil et — plus tard — nous permettre de créer des graphiques complexe, nous allons utiliser [seaborn](https://seaborn.pydata.org/).

### seaborn

Commençons installer la bibliothèque :

```shell
python -m pip install seaborn
```

{% info %}
Remplacez `python` par `python3` si vous êtes sour mac ou linux.
{% endinfo %}

Cette bibliothèque est une sur-couche de matplotlib qui apporte :

* des thèmes pour les graphiques
* ses propres méthodes de dessin.

Lorsque l'on commence à utiliser seaborn, il faut importer son module :

```python
import seaborn as sns
```

puis appliquer le thème par défaut :

```python
sns.set_theme()
```

{% info %}
Il existe plein de possibilités de modifier le thème, nous n'entrerons pas dans les détails ici
(assez jeter un coup d'œil [ici](https://seaborn.pydata.org/tutorial/aesthetics.html) ou [là](https://seaborn.pydata.org/tutorial/color_palettes.html) par exemple)
{% endinfo %}

Voyons un peu comment tout ça se comporte :

{% faire %}
Utilisez seaborn  `main_sélection.py` pour voir la différence !

Une fois convaincu, utilisez seaborn partout :-)

{% endfaire %}

A part l’esthétique, seaborn vient avec tout un tas de fonctions de dessin qui remplacent avantageusement celles de matplotlib car :

* leurs options sont rationnelles
* les valeurs par défaut sont ok
* c'est joli

On peut les utiliser de deux manières : soit sans soit avec matplotlib. Nous allons utiliser la seconde méthode qui nous permettra de paramétrer au mieux nos dessins.

Ci-après, on a repris l'exemple du [tutoriel matplotlib]({{ "/tutoriels/matplotlib/" | url }}) en ajoutant seaborn :

```python
# 0. import des bibliothèques
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# 1. création des données
x = []
y = []
for i in range(1000):
    x.append(i)
    y.append(i ** 2)

# 2. créer le dessin (ici ax)
fig, ax = plt.subplots(figsize=(20, 5))

# 2.1 limite des axes
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000000)

# 2.2 les légendes
ax.set_title("la courbe y=x^2")
ax.set_xlabel('x')
ax.set_ylabel('x^2')

# 3. ajouter des choses au dessin avec seaborn
sns.lineplot(ax=ax,
             x=x,
             y=y)

# 4. représenter le graphique
plt.show()
```

{% faire %}

Créez un fichier `essai_seaborn.py`{.fichier} où vous copiez le code précédent.

Vérifiez que tout fonctionne bien.
{% endfaire %}

On a utilisé [sns.lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot) pour représenter nos données sous la forme d'une courbe et le paramètre `ax`{.language} nous permet de dessiner dans la figure matplotlib.

{% note %}
Utilisez **toujours** les axes de matplotlib lorsque vous utilisez seaborn si c'est possible (quasiment toutes les fonctions seaborn le permettent). Cela vous permet d'avoir plus de contrôle sur vos figures.
{% endnote %}

A vous :

{% exercice %}
Utilisez [sns.scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) pour représenter nos données sous la forme de points dans le fichier `main_sélection.py`{.fichier}.
{% endexercice %}

## Régression

A priori la complexité en moyenne du tri par insertion est $\mathcal{O}(n^2)$. Le rapport entre le temps mis pour trier un tableau de longueur $n$ et $n^2$ devrait donc être plus ou moins une droite.

{% exercice %}
Dans un fichier nommé `main_rapport_complexité.py`{.fichier}, utilisez [sns.regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html?highlight=regplot#seaborn.regplot) pour vérifier que le rapport en temps mis pour trier un tableau aléatoire de taille $n$ et $n^2$ est plus ou moins une droite.

Vous ferez varier la longueur du tableau de 50 à 2000 par pas de 50.
{% endexercice %}

{% exercice %}
Faites de même que précédemment pour vérifier que le temps moyen et le temps maximum pour le tri à bulles sont comparables.
{% endexercice %}

## Tris complexes

{% faire %}
Implémentez (algorithmes et tests) :

* l'algorithme du tri `rapide`{.language-} et ses tests
* l'algorithme du tri `fusion`{.language-} et ses tests

{% endfaire %}
{% info %}
N'oubliez pas que le tri fusion possède une fonction annexe `combiner`{.language-} qu'il faut aussi tester
{% endinfo %}

### Fusion et rapide

Les complexités des tris rapide et fusion sont identiques en moyenne.

{% exercice %}
Dans un fichier `main_fusion_rapide.py`{.fichier}, en utilisant `temps_générique_moyen`{.language-}, `fusion`{.language-} et `rapide`{.language-} mesurer le temps moyen pris pour trier des tableau de taille 1 à 2000 par pas de 10.

Vous utiliserez [sns.lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot) de seaborn pour la représentation graphique.
{% endexercice %}

Vous allez atteindre la limite de récursion de python. Pour éviter les récursions infinies, python met une limite très basse au nombre de récursions possible d'un algorithme (1000 par défaut). Mais pas de panique, il est facile d'augmenter ce nombre.

{% info %}
Vous pouvez suivre [ce tuto](https://www.pythoncentral.io/resetting-the-recursion-limit/) qui vous explique comment faire pour augmenter le nombre limite de récursions dans *"main_rapide"*.
{% endinfo %}

{% exercice %}
Est-ce que la complexité du tri fusion est bien comparable à $\mathcal{n\ln(n)}$ ?

{% endexercice %}