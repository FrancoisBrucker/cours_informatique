---
layout: layout/post.njk
title: "Projet : tris"

eleventyNavigation:
  prerequis:
    - /cours/coder-et-développer/bases-python/
    - /cours/coder-et-développer/développement/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On code des tris et on vérifie que nos algorithmes fonctionnent.

## Mise en place

### Structures

{% faire %}

1. créez un dossier nommé `tris`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier
3. créez dans ce dossier les 2 fichiers de la trinité du code (on fera plusieurs `main`{.fichier} ensuite) :
   - `tris.py`{.fichier} : où vous placez les algorithmes de tris
   - `test_tris.py`{.fichier} : où vous placez les tests des algorithmes de tris

{% endfaire %}

### Vérifications

{% faire %}

- on vérifie que python est OK avec le terminal et avec vscode
- on vérifie que le linter est actif dans vscode
- on vérifie que les tests fonctionnent (en créant un test bidon dans `tests_tris.py`{.fichier} et en vérifiant que `pytest` et vscode le trouvent)

{% endfaire %}

## Tris basiques

En reprenant le code du cours :

{% faire %}
Implémentez :

- l'algorithme du tri `sélection`{.language-} et ses tests
- l'algorithme du tri `insertion`{.language-} et ses tests

{% endfaire %}

Pour les tests des algorithmes de tri, vous pouvez par exemple utiliser 3 tableaux différents :

- le tableau des $3$ premiers entiers triés par ordre croissant
- le tableau des $3$ premiers entiers triés par ordre décroissant
- le tableau des $3$ premiers entiers mélangé (choisissez une permutation)

{% attention %}
les deux fonctions [`sélection`{.language-}](../algorithme-sélection){.interne} et [`insertion`{.language-}](../algorithme-insertion){.interne} du cours sur les tris ne rendent rien. Elles **modifient** leurs paramètres. Pour tester de telles fonctions, il faut créer un objet dont on va tester s'il est bien modifié après être passé en paramètre de la fonction à tester. Le test suivant par exemple vérifie que la fonction `sélection`{.language-} trie bien un tableau trié par ordre décroissant :

```python
def test_sélection_décroissant():
    t = [3, 2, 1]
    sélection(t)
    assert t = [1, 2, 3]
```

{% endattention %}

### Complexités min et max

Nous allons (enfin plutôt, vous allez) afficher les complexités temporelles des différents algorithmes de tri que vous avez codés.

Pour faire cela, on utilisera ce que nous avons fait pendant [le projet exponentiation](../../projet-exponentiation/implémentation-code/){.interne}. Donc :

{% aller %}

Relisez [le projet exponentiation](../../projet-exponentiation/implémentation-code/){.interne} pour pouvoir rapidement trouver les informations nécessaires pour résoudre les questions suivantes.

{% endaller %}

Maintenant que vous êtes prêt, on peut commencer :

{% faire %}
Créez un fichier `mesure.py`{.fichier} et recodez-y la fonction `donne_pas` de [la partie mesure du temps](../../projet-exponentiation/implémentation-code/#mesure-temps){.interne} (vous n'oublierez pas ses tests).
{% endfaire %}

Pour étudier les complexités de ces deux tris, on va créer un fichier à part :

{% faire %}
Créez un fichier `main_tris_basiques.py`{.fichier}.
{% endfaire %}

#### Tri par sélection

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_sélection(T: [int]) -> float`{.language-} qui, à partir d'un tableau $T$ en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.

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

Puis on va adapter ce que l'on a fait pour l'exponentiation. Comme le tri par par sélection prend le même nombre d'opérations pour trier tous les tableaux de même taille, cela va être facile.

{% faire %}
Vérifiez qu'il faut environ 1 seconde pour trier un tableau de taille $N = 8000$ avec le tri par sélection.
{% endfaire %}

Puis on procède aux mesures :

{% faire %}
Ajoutez au programme du fichier `main_tris_basiques.py`{.fichier} deux nouvelles listes :

- la liste `taille_tableau`{.language-} qui est le retour de la fonction `donne_pas(20, 1, N)`{.language-} (avec $N=8000$)
- la liste `mesures_temps_sélection`{.language-} telle que `mesures_temps_sélection[i]`{.language-} corresponde au temps mis pour exécuter le tri sélection avec le tableau `list(range(taille_tableau[i]))`{.language-}
  {% endfaire %}

Affichez le tableau `mesures_temps_sélection`{.language-} et vérifiez que le temps augmente bien lorsque la taille augmente. Précisons un peu cette augmentation :

{% faire %}
Vérifiez que le rapport `mesures_temps_sélection[i] / (taille_tableau[i]) ** 2`{.language-} reste à peut prêt constant
{% endfaire %}

#### Tri par insertion

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_insertion(T: [int]) -> float`{.language-} qui, à partir d'un tableau $T$ en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.

{% endexercice %}

Le tri par insertion ne prend pas le même nombre d'opérations quelque soit le tableau :

- les tableaux triés par ordre croissant prendrons de l'ordre de $\mathcal{O}(n)$ opérations où $n$ est la taille du tableau
- les tableaux triés par ordre décroissant prendrons de l'ordre de $\mathcal{O}(n^2)$ opérations où $n$ est la taille du tableau

Vérifiez le expérimentalement :

{% faire %}
Ajoutez au programme du fichier `main_tris_basiques.py`{.fichier} deux nouvelles listes :

- la liste `taille_tableau`{.language-} qui est le retour de la fonction `donne_pas(20, 1, N)`{.language-} (avec $N=8000$)
- la liste `mesures_temps_insertion_croissant`{.language-} telle que `mesures_temps_insertion_croissant[i]`{.language-} corresponde au temps mis pour exécuter le tri insertion avec le tableau `list(range(taille_tableau[i]))`{.language-}
- la liste `mesures_temps_insertion_décroissant`{.language-} telle que `mesures_temps_instertion_décroissant[i]`{.language-} corresponde au temps mis pour exécuter le tri insertion avec le tableau `list(range(taille_tableau[i] - 1, -1, -1))`{.language-}
  {% endfaire %}

Affichez les tableaux `mesures_temps_insertion_croissant`{.language-} et `mesures_temps_insertion_décroissant`{.language-}. Le premier doit augmenter moins vite que le second :

{% faire %}
Vérifiez que :

- le rapport `mesures_temps_insertion_croissant[i] / (taille_tableau[i])`{.language-} reste à peut prêt constant
- le rapport `mesures_temps_insertion_décroissant[i] / (taille_tableau[i] ** 2)`{.language-} reste à peut prêt constant
  {% endfaire %}

### Complexité en moyenne

Pour connaître l'espérance de la complexité, il faut calculer la complexité en moyenne de l'algorithme. Pour cela il faut pouvoir créer un tableau aléatoire et calculer le temps mis pour le trier. Pour éviter tout cas particulier, on fait des moyennes de mesures.

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} la fonction `tableau_aléatoire(n)`{.language-} qui rend un tableau de taille $n$ contenant les $n$ premiers entiers placé à des positions aléatoires.
{% endexercice %}
{% info %}
Vous pourrez utiliser les techniques de [création de listes classiques](/cours/coder-et-développer/bases-python/structurer-son-code/conteneurs/listes/#listes-classiques){.interne} pour créer ces listes.
{% endinfo %}

Nous allons utiliser cette fonction pour mesurer le temps moyen du tri insertion :
{% faire %}
Ajoutez au programme du fichier `main_tris_basiques.py`{.fichier} la liste `mesures_temps_insertion_moyen`{.language-} telle que `mesures_temps_insertion_moyen[i]`{.language-} corresponde au temps mis pour exécuter le tri insertion avec le tableau `tableau_aléatoire(taille_tableau[i])`{.language-}.
{% endfaire %}

Le temps moyen du tri insertion doit être comparable au temps maximum. Vérifiez le :

{% faire %}
Vérifiez que le rapport `mesures_temps_insertion_décroissant[i] / mesures_temps_insertion_moyen[i]`{.language-} reste à peut prêt constant
{% endfaire %}

### Graphiques

Nous allons faire comme pour [le projet exponentiation](../../projet-exponentiation/implémentation-code/){.interne} et afficher nos mesures de temps. Si vous n'aviez pas fait la partie graphique de ce projet, commencez par lire [la partie consacré à Matplotlib](../../projet-exponentiation/implémentation-code/#Matplotlib){.interne} pour installer la bibliothèque et faire son tutoriel.

{% exercice %}
En utilisant le code du projet exponentiel, affichez sur un même graphique (l'abscisse est le tableau `taille_tableau`{.language-}) :

- le tableau `mesures_temps_insertion_croissant`{.language-}
- le tableau `mesures_temps_insertion_décroissant`{.language-}
- le tableau `mesures_temps_insertion_moyen`{.language-}

{% endexercice %}

L'allure des 3 courbes est-elle conforme aux résultats théoriques de complexité ?

## Tri à bulles

{% exercice %}
Implémentez [le tri à bulle optimisé](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles) dans le fichier `tris.py`{.fichier} (nommez l'algorithme `bulles`) et ses tests dans le fichier `test_tris.py`{.fichier}.

{% endexercice %}

### Complexités du tri à bulle

{% exercice %}
Créez dans le fichier `mesure.py`{.fichier} une fonction `temps_bulles(T: [int]) -> float`{.language-} qui, à partir d'un tableau $T$ en entrée, rend le temps mis pour exécuter cet algorithme avec le tableau donné.

{% endexercice %}
{% info %}
Pour ne pas refaire la même chose que pour le calcul de la complexité en moyenne du tri par `insertion`{.language-}, vous pourrez utiliser le fait que l'on peut passer une fonction en paramètre d'une autre !

Vous pourrez ainsi utiliser l'exemple ci-dessous qui crée une fonction de mesure de temps générique :

```python
import random
import time

def temps_tri(fonction_tri, T):
    d = time.perf_counter()
    fonction_tri(T)
    f = time.perf_counter()

    return f - d


def temps_insertion(T):
    return temps_tri(insertion, T)  # en supposant qu'une fonction insertion existe


def temps_sélection(T):
    return temps_tri(sélection, T)  # en supposant qu'une fonction sélection existe


def temps_bulles(T):
    return temps_tri(bulles, T)  # en supposant qu'une fonction bulles existe
```

{% endinfo %}

Les complexités maximales (pour les tableau triés par ordre décroissant) et moyenne du tri à bulles sont de $\mathcal{O}(n^2)$ opérations où $n$ est la taille du tableau et la complexité minimale (pour les tableau triés par ordre croissant) de $\mathcal{O}(n^2)$ opérations. Vérifiez le expérimentalement :

{% exercice %}

Dans un fichier `main_bulles`{.fichier}, affichez le graphique des complexités minimales, maximales et moyenne pour le tri à bulle.

{% endexercice %}

## Visualisation

Cette partie va vous montrer comment un tri se trie. Chaque tri est différent et vous allez le _voir_.
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

- l'algorithme du tri `rapide`{.language-} et ses tests
- l'algorithme du tri `fusion`{.language-} et ses tests

{% endfaire %}
{% info %}
N'oubliez pas que le tri fusion possède une fonction annexe `combiner`{.language-} qu'il faut aussi tester
{% endinfo %}

Les complexités des tris rapide et fusion sont identiques en moyenne.

{% exercice %}
En utilisant ce que vous avez appris avec les tris simples, vérifiez que les complexités en moyennes des tris rapide et fusion sont similaires et correspondent bien à $\mathcal{n\ln(n)}$ où $n$ est la taille du tableau.
{% endexercice %}
{% info %}
Vous pouvez suivre [ce tutoriel](https://www.pythoncentral.io/resetting-the-recursion-limit/) qui vous explique comment faire pour augmenter le nombre limite de récursions dans `main_rapide.py`{.fichier}.
{% endinfo %}
