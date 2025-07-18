---
layout: layout/post.njk

title: Utilisation des listes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Tableaux et listes

### Matrices

> - **Utilité** : à connaître car exercice classique réduction de complexité spatiale.
> - **Difficulté** : facile

{% aller %}

[Triangle de Pascal](./triangle-pascal){.interne}

{% endaller %}

### Tri par monotonies

Utilisation des listes pour faire grossir des tableaux.

Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. Par exemple :
si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

Donnez un algorithme qui, étant donné un tableau $T$ construit une liste (de listes) $L$, chaque élément de $L$ étant une monotonie de $T$ (et vice versa). À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.

Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$ (ceci est aussi une question de cours).

Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.

En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.

Cet algorithme est en fait une variante d'un algorithme vu en cours. Lequel ?

## Piles

> - **Utilité** : les piles ça sert toujours. Ces exercices vous montrerons des cas classiques d'utilisation
> - **Difficulté** : dur

### Parenthésage

Soit $C$ une expression arithmétique avec des parenthèses et des crochets. On cherche à savoir si le parenthésage est équilibré :

- `[3 + 3 * (1 + 3)]` sera Ok
- `[3 + 3 * (1 + 3])` sera pas Ok

On ne vérifiera pas que l'expression est arithmétiquement correcte, c'est à dire que pour nous, `[3 + + 3 (1 + 3)]` sera Ok.

{% exercice %}

Montrer que l'on peut utiliser une pile pour savoir si un parenthésage est équilibré entre les `()` et les `[]`.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme parenthèse(C):
    P ← une nouvelle pile de caractères
    pour chaque c de C:
        si c == "(" ou c == "[":
            P.empile(c)
        sinon si c == ")":
            si P.vide() ou P.dépile() ≠ "(":
                rendre Faux
        sinon si c == "]":
            si P.vide() ou P.dépile() ≠ "[":
                rendre Faux
    rendre Vrai
```

{% enddetails %}

### Calcul d'une expression avec deux piles

Soit $C$ une expression arithmétique avec uniquement des parenthèses, des `+` et des `*`. On suppose qu'elle est arithmétiquement correcte, comme `(3 + 3 * (1 + 3))`

{% exercice %}

Montrer que l'on peut utiliser deux piles (une pour les opérateurs et les parenthèses et l'autre pour les nombres) pour calculer $C$.
{% endexercice %}
{% details "corrigé" %}

Il faut faire attention au fait que `*` a une priorité supérieure à `+` : `3 + 4 * 3 = 15`.

On lit l'expression de gauche à droite :

1. si le caractère lu est un nombre on le place dans la pile P2
2. sinon si le caractère lu est un opérateur O :
   1. on évalue l'expression comme on la fait avec la notation polonaise inversée :
      1. pop de P1 dans op
      2. pop de p2 dans y
      3. pop de p2 dans x
      4. x op y = z
      5. push de z dans P2
   2. jusqu'à ce que :
      1. P1 est vide ou
      2. l'opérateur O a une priorité supérieure à celle sur P1
   3. place O dans P1
3. sinon si le caractère lu est une parenthèse ouvrante : on la place dans P1
4. sinon si le caractère lu est une parenthèse fermante :
   1. on évalue l'expression jusqu'à trouver une parenthèse ouvrante
   2. on push le résultat dans P2

Si on a fini de lire l'expression on évalue le reste des deux piles.

{% lien %}
à 9min13  <https://www.youtube.com/watch?v=2vBVvQTTdXg>
{% endlien %}
{% enddetails %}

## Liste chaînée

> TBD dire base des algos récursifs.
> TBD donner le type récursif associé.

> TBD reprendre exercices suppression/ head, tail , rendre éléments pair et impair/ retournements

## Autre structures

- skip list
- listes triées : pas évident de pourquoi on fait ça : ie réduire le coup d'insertion. Reprendre l'idée du compteur. Exercice 3 : <https://perso.ens-lyon.fr/laureline.pinault/Algo1/TD06-correction.pdf>
