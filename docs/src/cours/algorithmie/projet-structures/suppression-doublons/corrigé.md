---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

## Suppression de doublon en conservant l'ordre

```text
Nom : Algorithme-2
Entrées :
    L : une liste de n valeurs
Programme :
    création d’une liste L2 vide
    tant que L est non vide:
        x = L[0]
        ajoute x à la fin de L2
        L = algorithme-1(L, x)
    Retour L2
```

### complexité de l'algorithme 2

Commençons par compter le nombre de fois où la boucle `tant que`{.language-} sera exécutée. `L`{.language-} est modifiée à chaque fin de boucle `L = algorithme-1(L, x)`{.language-} avec `x = L[0]`{.language-}. Comme l'algorithme de la question 1 rend la restriction de de `L`{.language-} aux valeurs différentes de `x`{.language-}, elle va forcément être strictement plus petite (puisque `x=L[0]`{.language-} il est forcément dans la liste) : la longueur de la liste diminue strictement à chaque itération, on ne peut y rentrer que la longueur de `L`{.language-} initiale fois.

La seule ligne de l'algorithme qui n'est pas de complexité $\mathcal{O}(1)$ est : `L = algorithme-1(L, x)`{.language-}. Sa complexité est égale à une affectation ($\mathcal{O}(1)$) plus la complexité de l'algorithme de la question 1, qui vaut de l'ordre de la taille de la liste passée en entrée.

Cette taille diminue strictement à chaque itération : on peut utiliser l'astuce du cours pour ne garder que la complexité la plus importante, c'est à dire $\mathcal{O}(len(L))$ avec `L`{.language-} la liste initiale.

Notre complexité est donc de l'ordre : $\mathcal{O}(1) + A * (\mathcal{O}(1) + B)$ où :

- A est le nombre de fois où l'on rentre dans la boucle tant que : $\mathcal{O}(len(L))$
- B est la complexité maximale de l'algorithme de la question 1 : $\mathcal{O}(len(L))$

Notre algorithme est de complexité : $\mathcal{O}(len(L)^2)$

### preuve algorithme 2

La liste `L`{.language-} contient $k$ valeurs différentes que l'on note $v_1, \dots v_k$ dans l'ordre de la liste (le 1er indice où l'on rencontre $v_i$ est strictement plus petit que le 1er indice où l'on rencontre $v_j$ si $i < j$).

Notre invariant de boucle sera : au bout de la $i$ème itération :

- $L2 = [v_1, \dots, v_i]$.
- `L`{.language-} vaut la restriction de `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$.

- **initialisation** : comme $v_1= L[0]$ notre invariant est vrai puisque l'algorithme 1 rendra la restriction de `L`{.language-} initiale aux éléments différents de $v_1$.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. Au début de l'itération $i+1$, on a par hypothèse de récurrence que $L2 = [v_1, \dots, v_i]$ et que `L`{.language-} vaut la restriction de la liste `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$. Donc $L[0] = v_{i+1}$ et tout se passe comme à la 1ère itération.

A la fin de l'algorithme, notre invariant est toujours juste : $L2 = [v_1, \dots, v_k]$

## Suppression de doublon d'une liste ordonnée

Il suffit de parcourir tous les éléments de `L`{.language-} dans l'ordre :

```text
Nom : Algorithme-2'
Entrées :
    L : une liste de n valeurs
Programme :
    création d’une liste L2 contenant le premier élément de L
    pour i allant de 1 à n-1:
        si L[i] != L[i-1]:
            ajoute L[i] à la fin de L2
    Retour L2
```

### complexité de l'algorithme 2'

Clairement en $\mathcal{O}(n)$

### preuve de l'algorithme 2'

L'invariant de boucle et sa preuve est identique à celle de la preuve de l'algorithme 2 en tenant compte du fait que `L`{.language-} est trié.

## Suppression de doublon d'une liste sans ordre

On commence par trier la liste on utilise l'algorithme de la question précédente. Ceci fait passer la complexité de $\mathcal{O}(len(L)^2)$ à $\mathcal{O}(len(L)\log(len(L)))$
