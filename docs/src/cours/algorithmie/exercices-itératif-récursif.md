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

### Somme

{% faire %}

Écrivez un algorithme permettant de calculer la somme de 2 nombre donné sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `somme([entier], [entier]) -> [entier]`{.language-}

{% endfaire %}

### Division euclidienne

{% faire %}

Écrivez un algorithme permettant de calculer la division euclidienne de 2 nombre donné sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `division(dividende: entier, diviseur: entier) -> [entier]`{.language-}.

{% endfaire %}

### Puissance

{% faire %}

Écrivez un algorithme de signature `puissance(n: entier, p: entier) -> entier` qui rend le plus grand entier $q$ tel que $p^q$ divise $n$.

{% endfaire %}

