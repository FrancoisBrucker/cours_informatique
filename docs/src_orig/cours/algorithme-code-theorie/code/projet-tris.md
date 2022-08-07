---
layout: page
title:  "projet / algorithmes de tris"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [projet : algorithmes de tris]({% link cours/algorithme-code-theorie/code/projet-tris.md %})
>
> prérequis :
>
>* [étude : trier un tableau]({% link cours/algorithme-code-theorie/algorithme/etude-tris.md %})
>* [projet : exponentiation]({% link cours/algorithme-code-theorie/code/projet-exponentiation.md %})
>
{.chemin}

Ce projet suit l'[étude des tris]({% link cours/algorithme-code-theorie/algorithme/etude-tris.md %}).

## mise en place

### structures

> 1. créez un dossier nommé *"tris"* où vous placerez vos fichiers
> 2. créez un projet vcode dans ce dossier
> 3. créez dans ce dossier les 2 fichiers de la trinité du code (on fera plusieurs *main* ensuite) :
>    * *"tris.py"*
>    * *"test_tris.py"*
>
{.a-faire}

### vérifications

>
> * on vérifie que python est ok avec le terminal et avec vscode
> * on vérifie que le linter est actif dans vscode
>* on vérifie que les tests fonctionnent (en créant un test bidon dans *"tests_tris"* et en vérifiant que `pytest` et vscode le trouvent)
>
{.a-faire}

## implémentation des tris

En reprenant le code donné dans l'[étude des tris]({% link cours/algorithme-code-theorie/algorithme/etude-tris.md %}) :

> Implémentez :
>
> * l'algorithme du tri `insertion` et ses tests
> * l'algorithme du tri `selection` et ses tests
> * l'algorithme du tri `rapide` et ses tests
> * l'algorithme du tri `fusion` et ses tests (on n'oublie pas que le tri fusion possède une fonction annexe `colle` qu'il faut aussi tester)
>
{:.a-faire}

Pour les tests des algorithmes de tri, vous pouvez par exemple utiliser 3 tableaux différents :

* le tableau des $5$ premiers entiers triés par ordre croissant
* le tableau des $5$ premiers entiers triés par ordre décroissant
* le tableau des $5$ premiers entiers mélangé (choisissez une permutation)

## complexité

Nous allons (enfin plutôt, vous allez) afficher les complexités temporelle des différents algorithmes de tri que vous avez codés.

Pour faire cela, on utilisera ce que nous avons fait pendant le [projet exponentiation]({% link cours/algorithme-code-theorie/code/projet-exponentiation.md %}).

### calcul des complexités temporelles

> Créez un fichier *"mesure.py"*
{.a-faire}

### tri par sélection

> Créez dans le fichier *"mesure.py"* une fonction `temps_selection`  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.
>
{.a-faire}

> Dans un fichier *"main_selection"*, affichez sur un graphique courbe du temps mis (axe des ordonnées) pour trier avec `selection` le tableau des $n$ premiers entiers triés, pour une taille $n$ (axe des abcisses) allant de 1 à 2000 par pas de 10.
>
> A quel type de complexité correpond cette mesure ?
{.a-faire}

### tri par insertion

> Créez dans le fichier *"mesure.py"* une fonction `temps_insertion`  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.
>
{.a-faire}

> * pour quel type de tableau est atteint la complexité minimale de l'algorithme `insertion` ?
> * pour quel type de tableau est atteint la complexité maximale de l'algorithme `insertion` ?
{.a-faire}

Utilisez ces tableaux pour :

> Dans un fichier *"main_insertion"*, affichez sur un même graphique :
>
> * la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion des tableaux de taille $n$ (axe des abcisses) réalisant la complexité minimale
> * la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion  des tableaux de taille $n$ (axe des abcisses) réalisant la complexité maximale
>
> Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{.a-faire}

Comme la complexité minimale et maximale du tri par insertion sont différentes, les deux courbes doivent être distinctes.

> l'allure des 2 courbes est-elle conforme aux résultats théorique de complexité ?
{.a-faire}

Pour connaitre l'espérance de la complexité, il faut calculer la complexité en moyenne de l'algorithme. Pour cela il faut pouvoir créer un tableau aléatoire et calculer le temps mis pour le trier. Pour éviter tout cas particulier, on fait des moyennes de mesures.

> Créez dans le fichier *"mesure.py"* la fonction `temps_insertion_moyen` qui rend la moyenne de 10 temps pris pour trier avec `insertion` une permutation aléatoire du tableau en entrée.
{.a-faire}

Pour mélanger une liste python, vous pouvez utiliser la fonction [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) du module random.

On peut maintenant visualiser les temps minimum, maximum et moyen de notre algorithme :

> Dans le fichier *"main_insertion"*, en utilisant `temps_insertion_moyen`, ajoutez au graphique la courbe de la moyenne des temps mis (axe des ordonnées) pour trier 10 tableaux aléatoire de taille $n$ (axe des abcisses) avec l'algorithme `insertion`.
>
> Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{.a-faire}

### tri fusion

La complexité minimum et maximum du tri fusion est la même. On peut juste tracer la complexité moyenne de l'algorithme :

> Créez dans le fichier *"mesure.py"* une fonction `temps_fusion` qui rend la moyenne de 10 temps pris pour trier avec `fusion` une permutation aléatoire du tableau en entrée.
{.a-faire}

Pour ne pas refaire la même chose que pour le calcul de la complexité en moyenne du tri par `insertion`, vous pourrez utiliser le fait que l'on peut passer une fonction en paramètre d'une autre !

Vous pourrez ainsi modifier l'exemple ci-dessous pour forger une fonction qui rend le temps moyen pris pour trier 10 listes de taille $n$.

```python
import random, time

def temps_tri(f, n):
    L = list(range(n))
    random.shuffle(L)
    d = time.time()
    f(L)
    f = time.time()
 
    return f - d

# en supposant qu'une fonction instertion existe
delta = tri(insertion, 10)  # delta est le temps mis par insertion pour trier une liste de taille 10
```

Si on doit choisir une complexité à afficher, on préfèrera toujours la complexité en moyenne, car elle est simple à mesurer (on fait des moyennes de temps d'exécution) sans analyse au préalable de l'algorithme.

> Dans le fichier *"main_fusion"*, en utilisant `temps_fusion`, ajoutez au graphique la courbe de la moyenne des temps mis (axe des ordonnées) pour trier 10 tableaux aléatoire de taille $n$ (axe des abcisses) avec l'algorithme `fusion`.
>
> Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10.
{.a-faire}

> l'allure de la courbe est-elle conforme aux résultats théorique de complexité ?
{.a-faire}

### tri rapide

La complexité du tri rapide est différente pour des tableaux déjà triés (la complexité est alors maximum) et pour des tableaux mélangés (ou la complexité moyenne est égale à la complexité minimale).

> Dans un fichier *"main_rapide"*, affichez sur un même graphique :
>
> * la courbe du temps mis (axe des ordonnées) pour trier avec le tri rapide des tableaux triés par ordre croissant de taille $n$ (axe des abcisses)
> * la courbe du temps mis (axe des ordonnées) pour trier avec le tri rapide des tableaux aléatoire de taille $n$ (axe des abcisses).
>
> Faites varier la taille $n$ des tableaux de 1 à 2000 par pas de 10. Pour chaque taille vous ferez une moyenne de 10 mesures.
{.a-faire}

Vous allez atteindre la limite de récursion de python. Pour éviter les récursions infinies, python met une limite très basse au nombre de récursions possible d'un algorithme (1000 par défaut). Mais pas de panique, il est facile d'augmenter ce nombre.

> Suivez [ce tuto](https://www.pythoncentral.io/resetting-the-recursion-limit/) qui vous explique comment faire pour augmenter le nombre limite de récursions dans *"main_rapide"*.
{.a-faire}

## visualisation

> Copiez le code suivant dans un fichier *"main_visu.py"* :
{.a-faire}

```python
import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    ax.cla()  # on efface le dessin
    ax.plot(tab, 'ro')
    plt.pause(0.1)  # on pause le dessin


def insertion(tableau):
    for i in range(1, len(tableau)):
        courant = tableau[i]
        j = i
        while (j > 0) and (courant < tableau[j - 1]):
            tableau[j] = tableau[j - 1]
            tableau[j - 1] = courant
            j -= 1

            draw_tab(tab)  # on affiche le tableau


fig, ax = plt.subplots(figsize=(20, 5))

tab = list(range(30))
random.shuffle(tab)

print(tab)

ax.plot(tab, 'ro')
insertion(tab)

print(tab)
```

Le code précédent modifie l'algorithme `insertion` pour qu'il affiche dans un graphique le tableau après chaque modification.

>
> 1. Exécutez le code précédent, et comprenez pourquoi il fonctionne.
> 2. Ajoutez une modification du tri par `selection` pour le voir trier un tableau et voir les différences entre les deux algorithmes.
>
{:.a-faire}

## autres tris

### tri à bulles

Le [tri à bulles](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) est un tri inefficace mais joli à regarder.

> Implémentez le tri à bulles et vérifiez que son temps moyen d'exécution est $\mathcal{O}(n^2)$.
> Ajoutez le tri à bulles dans *"main_visu.py"* pour le voir trier un tableau.
{.a-faire}

### bogo sort

> Implémentez le [tri stupide](https://fr.wikipedia.org/wiki/Tri_stupide) et vérifiez son temps moyen de tri.
{:.a-faire}
