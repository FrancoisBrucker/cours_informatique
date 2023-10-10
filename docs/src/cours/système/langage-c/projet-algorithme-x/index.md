---
layout: layout/post.njk

title: "Projet : Algorithme X"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but de ce projet est l'implémentation du célèbre [Algorithme X](https://fr.wikipedia.org/wiki/Algorithme_X_de_Knuth) de Knuth.

Vous créerez un programme complet géré avec un `Makefile`{.fichier} et autant d'unités fonctionnelles que nécessaire. 

Le projet doit contenir :

- un fichier `Makefile`{.fichier} qui doit contenir :
  - une règle par défaut `all` qui créera tous les exécutables
  - une règle par exécutable
- un dossier `src/`{.fichier} contentant les sources de votre projet
- un dossier `dist/`{.fichier} qui contiendra les fichiers exécutables de votre projet
- un fichier `readme.md`{.fichier} explicatif contenant les différentes règles du makefile permettant de générer les exécutables particuliers et la documentation pour les utiliser.

## Problème

L'algorithme X permet de résoudre optimalement un problème NP-complet nommé [problème de la couverture exacte](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_couverture_exacte). Il admet une formulation ensembliste et une formulation matricielle.

{% note "**formulation ensembliste**" %}

Soient $X$ un ensemble fini et $\mathcal{A}$ un ensemble de sous-ensembles de $X$

Une ***couverture exacte*** est un sous-ensemble $\mathcal{A}'$ de $\mathcal{A}$ tel que tout élément de $X$ se retrouve dans **exactement** un ensemble de $\mathcal{A}'$.
{% endnote %}

Notez, que l'on ne suppose pas qu'il existe ue solution au problème.

Informatiquement parlant, on préfère une formulation matricielle, utilisant des matrices binaires.

{% note "**définition**" %}

Une ***matrice binaire*** est une matrice à $n$ lignes et $m$ colonnes
<div>
$$
M = (m_{i,j})_{1\leq i \leq n, 1\leq j \leq m}
$$
</div>

dont les éléments sont soient 0 soit 1 ($m_{i,j} \in \\{0, 1\\}$ pour toutes ligne $i$ et colonne $j$).

{% endnote %}

On peut alors définir le problème de la couverture exacte matricielle :

{% note "**formulation matricielle**" %}

Soit $M$ une matrice binaire à $n$ lignes et $m$ colonnes. Une ***couverture exacte*** de $M$ est un ensemble $I$ de lignes tel que pour toute colonne $1 \leq j \leq m$, il existe exactement un élément $i$ de $I$ tel que $m_{i, j} = 1$.
{% endnote %}

Ce problème est NP-complet, c'est à dire qu'on ne connaît pas d'autre algorithme que de tester toutes les solutions possible.

## Génération d'instances

Vous allez créez une unité fonctionnelle dont le but est de générer des instances matricielle au problème.

Vous créerez également un fichier `main_instance.c`{.fichier} (avec une règle spéciale dans la `Makefile`) permettant de créer un exécutable qui affiche le résultat de chacune de vos fonctions de créations d'instances.

### Instance quelconque

{% faire %}
En utilisant l'implémentation sous la forme d'un pointeur opaque de l'[exercice matrice](../exercices/#matrice){.interne} créez une fonction permettant de créer une instance du problème. Sa signature doit être :

```c
matrice_t instance_generale(size_t nombre_ligne, size_t nombre_colonnes)
```

{% endfaire %}

Pour nos tests, il est important d'avoir des cas particuliers d'instances qui ont ou qui n'ont pas de solutions.

### Instances sans solution

Démontrez la proposition suivante :

{% note "**Proposition**"%}
Soit $M$ une matrice binaire. S'il existe $\\{j_1, \dots, j_p\\}$ et $\\{i_1, \dots, i_p\\}$ avec $p$ impair tel que : $m_{i, j_k} = 1$ si et seulement si $i = i_k$ ou $i = j_{k - 1 \text{mod} p}$, alors $M$ n'admet pas de couverture exacte.
{% endnote %}

On peut maintenant créer une instance de matrice sans solution :

{% faire %}
En utilisant le [mélange de Knuth](../exercices/#mélange){.interne} créez une fonction permettant de créer une matrice carrée à $p$ impaire lignes telle que il existe une permutation de lignes et de colonnes satisfaisant la proposition. La signature de cette fonction doit être :

```c
matrice_t instance_sans_solution(size_t p)
```

{% endfaire %}

### Instances avec solution

Montrez que :

{% note "**Proposition**" %}

Pour qu'une matrice binaire $M$ à $n$ lignes et $m$ colonnes admette une couverture exacte, il faut et il suffit qu'il existe deux suites $1 \leq i_1 < \dots < i_k \leq n$ et $0 = j_0 < j_1 < \dots < j_k = n$ telles que pour tout $1 \leq l \leq k$ :

- $m_{i_l, j} = 1$ pour $j_{l-1} < j \leq j_l$
- $m_{i_l, j} = 0$ sinon

Les lignes solutions sont alors les lignes $i_1$ à $i_k$.
{% endnote %}

{% faire %}
En utilisant l'exercice [tirant des entiers aléatoire](../exercices/#entier-aléatoire){.interne} créez une fonction de signature :

```c
int *suite_croissante(size_t k, size_t n)
```

Qui rend un tableau $t$ de $k$ entiers tel que $1 \leq t[0] < \dots < t[k-1] \leq n$
{% endfaire %}
{% faire %}
Créer une matrice ayant une solution en :

1. utilisant la fonction ci-dessous pour créer les $k$ lignes solutions
2. remplir les autres lignes aléatoirement  de 0 ou de 1.

La fonction doit avoir la signature :

```c
matrice_t instance_avec_solution(size_t k, size_t nombre_lignes, size_t nombre_colonnes)
```

{% endfaire %}

## Algo

## Implémentation

### Une passe

### Récursion

### Pile

## Mesure du temps

- matrices aléatoires et mesure du temps avec shell


## Dancing links

### Liste doublement chaînée

### Implémentation

Attention 0 l'ordre des piles.

