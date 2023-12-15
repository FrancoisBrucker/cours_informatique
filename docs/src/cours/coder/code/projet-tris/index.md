---
layout: layout/post.njk 
title: "Projet : tris"


eleventyNavigation:
    order: 6
    prerequis:
        - "../projet-exponentiation/"
        - "../../algorithme/tris/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

En reprenant le code donné dans l'[étude des tris](../../algorithme/tris){.interne} :

{% faire %}
Implémentez :

* l'algorithme du tri `sélection`{.language-} et ses tests
* l'algorithme du tri `insertion`{.language-} et ses tests

{% endfaire %}

Pour les tests des algorithmes de tri, vous pouvez par exemple utiliser 3 tableaux différents :

* le tableau des $5$ premiers entiers triés par ordre croissant
* le tableau des $5$ premiers entiers triés par ordre décroissant
* le tableau des $5$ premiers entiers mélangé (choisissez une permutation)

### Complexités

Nous allons (enfin plutôt, vous allez) afficher les complexités temporelles des différents algorithmes de tri que vous avez codés.

Pour faire cela, on utilisera ce que nous avons fait pendant le [projet exponentiation](../projet-exponentiation){.interne}. Donc :

{% faire %}

Relisez le [projet exponentiation](../projet-exponentiation){.interne} pour pouvoir rapidement trouver les informations nécessaires pour résoudre les questions suivantes.

{% endfaire %}

Maintenant que vous êtes prêt, on peut commencer :

{% faire %}
Créez un fichier `mesure.py`{.fichier}
{% endfaire %}

#### Tri par sélection

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_sélection(T)`{.language-} qui, à partir d'un tableau $T$ en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.

{% endexercice %}
{% details "solution" %}

```python
import time

def temps_sélection(T):
    t1 = time.perf_counter()
    sélection(T)
    t2 = time.perf_counter()

    delta = t2 - t1

    return delta
```

{% enddetails %}

Pour créer le graphique des complexités on va créer un fichier à part :

{% faire %}
Créez un fichier `main_sélection.py`{.fichier}.
{% endfaire %}

Puis on va préparer les fonction pour créer les tableaux à trier :

{% exercice %}
Créez dans le fichier `main_sélection.py`{.fichier} une fonction `tableau_max_sélection(n)`{.language-} qui, à partir d'une taille $n$ en entrée, rend un tableau de taille $n$ dont le tri par l'algorithme `sélection`{.language-} sera de complexité maximale (un tableau des $n$ premiers entiers trié fera l'affaire (`list(range(n)))`{.language-}), puisque les complexité min et max sont égale pour le tri par sélection).
{% endexercice %}
{% details "solution" %}

```python
def tableau_max_sélection(n):
    return list(range(n))
```

{% enddetails %}

{% exercice %}
Créez dans le fichier `main_sélection.py`{.fichier} une fonction `temps_max_sélection(d)`{.language-} qui, à partir d'une durée $d$ en entrée, rend la première puissance de $n = 2^k$ tel que le tableau issu de `tableau_max_sélection(n)`{.language-} prennent un temps supérieur à $d$ pour être trié par l'algorithme `sélection`{.language-}.

{% endexercice %}
{% details "solution" %}

```python
def temps_max_sélection(d):
    n = 1
    T = tableau_max_sélection(n)
    delta = temps_sélection(T)

    while delta < d:
        n = 2 * n
        T = tableau_max_sélection(n)
        delta = temps_sélection(T)

    return n
```

{% enddetails %}

{% exercice %}

On peut maintenant produire les données. Dans le fichier `main_sélection`{.fichier} :

1. trouvez $n = 2^k$ la première puissance de $2$ tel que le tableau issu de `tableau_max_sélection(n)`{.language-} prennent plus de 1 secondes à se faire trier par l'algorithme `sélection`{.language-}
2. créez une liste $x$ contenant environ $20$ nombre répartis entre $1$ et $n$
3. créez une liste $y$ tel que $y[i]$ corresponde au temps mis par l'algorithme `sélection`{.language-} pour trier un tableau issu de `tableau_max_sélection(x[i])`{.language-}
4. afficher sur un graphique la courbe du temps mis (axe des ordonnées) pour trier des tableau avec `sélection`{.fichier}. Vous pourrez utiliser les tableaux $x$ et $y$ précédemment calculés.
{% endexercice %}
{% info %}
Vous pourrez utiliser les techniques de [création de listes classiques]({{ "/cours/utiliser-python/listes" }}#listes-classiques){.interne} pour créer la liste du 2.
{% endinfo %}
{% details "solution" %}

```python
import time
import matplotlib.pyplot as plt

from tris import sélection
from mesure import temps_sélection


def tableau_max_sélection(n):
    return list(range(n))


def temps_max_sélection(d):
    n = 1
    T = tableau_max_sélection(n)
    delta = temps_sélection(T)

    while delta < d:
        n = 2 * n
        T = tableau_max_sélection(n)
        delta = temps_sélection(T)

    return n


d = 1
n = temps_max_sélection(d)
x = list(range(1, n, n // 20))

print("n =", n, " pour d =", d, " seconde ; len(x) =", len(x))

t1 = time.perf_counter()
y = [temps_sélection(tableau_max_sélection(i)) for i in x]
t2 = time.perf_counter()
print("temps total de calcul : ", t2 - t1, " secondes.")

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("complexité du tri par selection")

ax.plot(x, y)

plt.show()

```

{% enddetails %}

#### Tri par insertion

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_insertion(T)`{.language-}  qui, à partir d'un tableau en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau $T$ donné en paramètre.
{% endexercice %}

Pour créer le graphique associé au tri par insertion on crée un fichier dédié :

{% faire %}
Créez un fichier `main_insertion.py`{.fichier}.
{% endfaire %}

On produit ensuite les fonctions qui vont créer les tableaux à trier :

{% exercice %}

* pour quel type de tableau est atteint la complexité minimale de l'algorithme `insertion`{.language-} ?
* pour quel type de tableau est atteint la complexité maximale de l'algorithme `insertion`{.language-} ?

D ans le fichier `main_insertion.py`{.fichier}, créez deux fonctions `tableau_min_insertion(n)`{.language-} et `tableau_max_insertion(n)`{.language-} rendant respectivement tableau de taille $n$ dont le tri par l'algorithme `insertion`{.language-} sera de complexité minimale et un tableau de taille $n$ dont le tri par l'algorithme `insertion`{.language-} sera de complexité maximale.

{% endexercice %}
{% info %}
Vous pourrez utiliser les techniques de [création de listes classiques]({{ "/cours/utiliser-python/listes" }}#listes-classiques){.interne} pour créer ces listes.
{% endinfo %}

{% exercice %}
En utilisant les fonctions précédentes et en vous inspirant de ce que vous avez fait pour le tri par sélection, affichez sur un même graphique :

* la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion des tableaux de taille $n$ (axe des abscisses) réalisant la complexité minimale
* la courbe du temps mis (axe des ordonnées) pour trier avec le tri par insertion  des tableaux de taille $n$ (axe des abscisses) réalisant la complexité maximale

Vous prendrez les même tailles de tableaux que vous avez utilisées pour le tri par sélection.

{% endexercice %}

Comme la complexité minimale et maximale du tri par insertion sont différentes, les deux courbes doivent être distinctes.

{% exercice %}
L'allure des 2 courbes est-elle conforme aux résultats théoriques de complexité ?
{% endexercice %}

Pour connaître l'espérance de la complexité, il faut calculer la complexité en moyenne de l'algorithme. Pour cela il faut pouvoir créer un tableau aléatoire et calculer le temps mis pour le trier. Pour éviter tout cas particulier, on fait des moyennes de mesures.

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} la fonction `tableau_aléatoire(n)`{.language-} qui rend un tableau de taille $n$ contenant les $n$ premiers entiers placé à des positions aléatoires.
{% endexercice %}
{% info %}
Vous pourrez utiliser les techniques de [création de listes classiques]({{ "/cours/utiliser-python/listes" }}#listes-classiques){.interne} pour créer ces listes.
{% endinfo %}

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} la fonction `temps_insertion_moyen(n)`{.language-} qui rend la moyenne de 5 temps pris pour trier avec `insertion`{.language-} des tableaux issus de `tableau_aléatoire(n)`{.language-}.
{% endexercice %}

On peut maintenant visualiser les temps minimum, maximum et moyen de notre algorithme :

{% exercice %}

Dans le fichier `main_insertion`{.fichier}, en utilisant `temps_insertion_moyen`{.language-}, ajoutez au graphique la courbe de la moyenne des temps mis (axe des ordonnées) pour trier 10 tableaux aléatoire de taille $n$ (axe des abscisses) avec l'algorithme `insertion`{.language-}.

{% endexercice %}

### Sauvez les données

Commencer par lire le tutoriel suivant :

{% aller %}
[Suivre le tutoriel matplotlib]({{ "/tutoriels/matplotlib"  }}){.interne}.
{% endaller %}

Puis utilisez le pour :

{% faire %}

Utilisez le graphique où les trois courbes de complexité du tri par insertion sont superposées.

1. Zoomez (en changer les bornes des axes) sur l'endroit de la courbe où les courbes divergent.
2. sauvegardez cette nouvelle figure au format pdf

{% endfaire %}

## Tri à bulles

{% exercice %}
Implémentez [le tri à bulle optimisé](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) dans le fichier `tris.py`{.fichier} (nommez l'algorithme `bulles`) et ses tests dans le fichier `test_tris.py`{.fichier}.

{% endexercice %}

### Complexités du tri à bulle

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_bulles_moyen`{.language-} qui rend la moyenne de 5 temps pris pour trier avec `bulles`{.language-} des tableaux issus de `tableau_aléatoire(n)`{.language-}.
{% endexercice %}

Pour ne pas refaire la même chose que pour le calcul de la complexité en moyenne du tri par `insertion`{.language-}, vous pourrez utiliser le fait que l'on peut passer une fonction en paramètre d'une autre !

Vous pourrez ainsi modifier l'exemple ci-dessous pour forger une fonction qui rend le temps moyen pris pour trier 10 listes de taille $n$.

```python
import random
import time

def temps_tri(tri, T):

    d = time.perf_counter()
    tri(T)
    f = time.perf_counter()
 
    return f - d

def temps_insertion(T):
    return temps_tri(insertion, T)  # en supposant qu'une fonction insertion existe

```

{% exercice %}

Dans le fichier `mesures.py`{.fichier} Créez une fonction :

* `temps_générique(algorithme, tableau)`{.language-} qui rend le temps mis par l'algorithme de nom `algorithme`{.language-} pour trier `tableau`{.language-}
* `temps_générique_moyen(algorithme, tableau)`{.language-} qui rend la moyenne de 5 temps pris pour trier avec l'algorithme de nom `algorithme`{.language-} une permutation aléatoire du tableau `tableau`{.language-} en entrée.

{% endexercice %}

{% exercice %}
Modifiez vos fonctions `temps_sélection`{.language-}, `temps_insertion`{.language-}, `temps_insertion_moyen`{.language-} et `temps_bulles_moyen`{.language-} pour qu'elles utilisent les fonctions `temps_générique`{.language-} et `temps_générique_moyen`{.language-}.
{% endexercice %}

### Adéquation à la théorie

{% exercice %}

Dans le fichier `main_bulles`{.fichier}, en utilisant `temps_générique`{.language-} et `temps_générique_moyen`{.language-}, créez le graphique des complexités minimales, maximales et moyenne pour le tri à bulle.

{% endexercice %}

## Visualisation

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
2. Ajoutez une modification du tri par `sélection`{.language-} pour le voir trier le même tableau et voir les différences entre les deux algorithmes.
3. Ajoutez une modification du tri par `bulles`{.language-} pour le voir trier le même tableau et voir les différences entre les trois algorithmes.

{% endfaire %}

## Tris complexes

{% faire %}
Implémentez (algorithmes et tests) :

* l'algorithme du tri `rapide`{.language-} et ses tests
* l'algorithme du tri `fusion`{.language-} et ses tests

{% endfaire %}
{% info %}
N'oubliez pas que le tri fusion possède une fonction annexe `combiner`{.language-} qu'il faut aussi tester
{% endinfo %}

Les complexités des tris rapide et fusion sont identiques en moyenne.

{% exercice %}
Dans un fichier `main_fusion_rapide.py`{.fichier}, en utilisant `temps_générique_moyen`{.language-}, `fusion`{.language-} et `rapide`{.language-} mesurer le temps moyen pris pour trier des tableau de taille 1 à 2000 par pas de 10.

{% endexercice %}

Vous allez atteindre la limite de récursion de python. Pour éviter les récursions infinies, python met une limite très basse au nombre de récursions possible d'un algorithme (1000 par défaut). Mais pas de panique, il est facile d'augmenter ce nombre.

{% info %}
Vous pouvez suivre [ce tuto](https://www.pythoncentral.io/resetting-the-recursion-limit/) qui vous explique comment faire pour augmenter le nombre limite de récursions dans `main_rapide.py`{.fichier}.
{% endinfo %}

{% exercice %}
Est-ce que la complexité du tri fusion est bien comparable à $\mathcal{n\ln(n)}$ ?

{% endexercice %}
