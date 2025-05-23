---
layout: layout/post.njk

title: Utilisation des listes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


- skip list
- listes triées : ens complexité amortie.

> TBD refaire listes de façon simple dans un seul fichier

## Matrices

> - **Utilité** : à connaître car exercice classique réduction de complexité spatiale.
> - **Difficulté** : facile

{% aller %}

[Triangle de Pascal](./triangle-pascal){.interne}

{% endaller %}

## Suppression d'éléments

### Suppression de valeurs

> - **Utilité** : utilisation d'une liste
> - **Difficulté** : facile.

On a déjà vu comment faire avec un tableau.

#### Liste

Regardons comment tout ceci peut fonctionner avec une liste :

{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}

### Suppression de doublons

> - **Utilité** : classique et simple.
> - **Difficulté** : facile

{% aller %}
[Suppression des doublons](suppression-doublons){.interne}
{% endaller %}


{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}


## Piles

> - **Utilité** : les piles ça sert toujours. Ces exercices vous montrerons des cas classiques d'utilisation
> - **Difficulté** : dur

### File avec pile

On reprend l'[exercice sur la création d'une file avec 2 piles](../structure-pile-file/#file-avec-pile){.interne}.

{% exercice %}
Montrer que la complexité amortie d'ajout et de suppression d'un élément dans la structure de file créée avec 2 pile est en $\mathcal{O}(1)$
{% endexercice %}
{% details "corrigé" %}
On procède comme pour le compteur, on associe une complexité amortie de +2 lorsque l'on empile dans P1 et de 0 lorsque l'on empile dans P2.

{% enddetails %}

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
