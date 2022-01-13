---
layout: page
title:  "étude / algorithmes de tris"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [projet : algorithmes de tris]({% link cours/theorie-pratiques-algorithmique/coder/projet-tris.md %})
>
> prérequis :
>
>* [étude : trier un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %})
>* [projet : exponentiation]({% link cours/theorie-pratiques-algorithmique/coder/projet-exponentiation.md %})
>
{: .chemin}

Ce projet suit l'[étude des tris]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %}).

## mise en place

### structures

> 1. créez un dossier nommé *"tris"* où vous placerez vos fichiers
> 2. créez un projet vcode dans ce dossier
> 3. créez dans ce dossier les 2 fichiers de la trinité du code (on fera plusieurs *main* ensuite) :
>    * *"tris.py"*
>    * *"test_tris.py"*
>
{: .a-faire}

### vérifications

>
> * on vérifie que python est ok avec le terminal et avec vscode
> * on vérifie que le linter est actif dans vscode
>* on verifie que les tests fonctionnent (en créant un test bidon dans *"tests_tris"* et en vérifiant que `pytest` et vscode le trouvent)
>
{: .a-faire}

## implémentation des tris

En reprenant le code donné dans l'[étude des tris]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %}) implémentez :

* l'algorithme du tri `insertion` et ses tests
* l'algorithme du tri `selection` et ses tests
* l'algorithme du tri `rapide` et ses tests
* l'algorithme du tri `fusion` et ses tests (on n'oublie pas que le tri fusion possède une fonction annexe `colle` qu'il faut aussi tester)

## complexité

Nous allons (enfin plutôt, vous allez) afficher les complexités temporelle des différents algorithmes de tri que vous avez codé. 

POur faire cela, on utilisera ce que nous avons fait pendant le [projet exponentiation]({% link cours/theorie-pratiques-algorithmique/coder/projet-exponentiation.md %}).

### calcul des complexités temporelles

> Créez dans un fichier *"mesure.py"*
{: .a-faire}

### tri par selection

> Créez dans le fichier *"mesure.py"* une fonction `temps_selection`  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.
>
{: .a-faire}

> Dans un fichier *"main_selection"*, affichez le résultat des temps mis pour trier avec `selection` un tableau de taille inférieure à 2000 et par pas de 10.
{: .a-faire}

### tri par insertion

> Créez dans le fichier *"mesure.py"* une fonction `temps_insertion`  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.
>
{: .a-faire}

> Dans un fichier *"main_insertion"*, affichez sur un même graphique le résultat des temps minimum et maximum mis pour trier avec `insertion`  un tableau de taille inférieure à 2000 et par pas de 10.
{: .a-faire}

### tri fusion

Pour mesurer une complexité moyenne, il faut pouvoir créer un tableau aléatoire et calculer le temps mis pour le trier. Pour éviter tout cas particulier, on fait des moyennes de mesures.

> Créez dans le fichier *"mesure.py"* une fonction `temps_fusion` qui rend la moyenne de 10 temps pris pour trier avec `fusion` une permutation aléatoire du tableau en entrée.
{: .a-faire}

Pour mélanger une liste python, vous pouvez utiliser la fonction [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) du module random.

> Dans un fichier *"main_fusion"*, affichez sur un graphique le résultat des temps moyens mis pour trier avec `fusion` un tableau de taille inférieure à 2000 et par pas de 10 (vous utiliserez `temps_fusion`).
{: .a-faire}

### tri rapide

La complexité du tri rapide est différente pour pour des tableaux déjà triés et pour des tableaux mélangés.

> Dans un fichier *"main_rapide"*, , affichez sur un même graphique le résultat des temps maximum et moyen mis pour trier avec `rapide`  un tableau de taille inférieure à 2000 et par pas de 10.
>
> Pour cela, vous pourrez créer une fonction `temps_rapide` dans le fichier *"mesure.py"* qui rend les 2 résultats pour une taille de talbeau donnée.
{: .a-faire}

Vous allez atteindre la limite de récursion de python. Pour eviter les récursions infinies, python met une limite très basse au nombre de récursions possible d'un algorithme (1000 par défaut). Mais pas de panique, il est facile d'augmenter ce nombre.

> Suivez [ce tuto](https://www.pythoncentral.io/resetting-the-recursion-limit/) qui vous explique comment faire pour augmenter le nombre limite de récursion dans *"main_rapide"*.
{: .a-faire}

## visualisation

> Copiez le code suivant dans un ficheir *3main_visu.py"* :
{: .a-faire}

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
> 2. Ajoutez une modification du tri par `selection` pour le voir trier des tableaux et voir les différences entre les deux algorithmes.
>
{:.a-faire}

## autres tris

### tri à bulles

Le [tri à bulles](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) est un tri inefficace mais joli à regarder.

> Implementez le tri à bulles et vérifiez que son temps moyen d'exécution est $\mathcal{O}(n^2)$.
> Ajoutez le tri à bulles dans *"main_visu.py"* pur le voir trier des tableaux.
{: .a-faire}

### bogo sort

Implémentez le [tri stupide](https://fr.wikipedia.org/wiki/Tri_stupide) et vérifiez son temps moyen de tri (en espérant que vous n'atteignez jamais le temps max).
