---
layout: layout/post.njk
title: "exercices : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

À chaque fois, on vous demande d'écrire un algorithme puis de le prouver

## Arithmétique

### Entier vers décimal

{% faire %}

Écrivez un algorithme de signature `base10(entier) -> [entier]`{.language-} rendant la forme décimale (un tableau de chiffres allant de 0 à 9) d'un entier. On doit avoir :

```pseudocode
base10(123) = [3, 2, 1]
```

{% endfaire %}

### Décimal vers entier

{% faire %}

Écrivez un algorithme de signature `entier([entier]) -> entier`{.language-} rendant la valeur d'un entier écrit en forme décimale. On doit avoir :

```pseudocode
entier([3, 2, 1]) = 123
```

{% endfaire %}


### Somme

{% faire %}

Écrivez un algorithme permettant de calculer la somme de 2 nombre donné sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `somme([entier], [entier]) -> [entier]`{.language-}

{% endfaire %}

### Division euclidienne

{% faire %}

Écrivez un algorithme permettant de calculer la division euclidienne de 2 nombre donné sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `division(dividende: entier, diviseur: entier) -> [entier]`{.language-}.

{% endfaire %}

<!-- ### Puissance

> TBD à déplacer dans la partie complexité.

{% faire %}

Écrivez un algorithme de signature `puissance(n: entier, p: entier) -> entier` qui rend le plus grand entier $q$ tel que $p^q$ divise $n$.

{% endfaire %}

## Parenthèses

> TBD uniquement parenthèse itératif et récursif
> TBD parenthèse et crochets (faire monter i et descendre j) -->