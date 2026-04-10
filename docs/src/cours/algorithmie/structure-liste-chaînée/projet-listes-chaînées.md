---
layout: layout/post.njk
title: "Projet : listes Chaînées"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices de manipulation de listes chaînées et doublement chaînées

## Retournement

{% exercice %}
Donnez un algorithme récursif et sa complexité linéaire permettant de retourner une liste chaînée.
{% endexercice %}

{% details "corrigé" %}

Utilisons la concaténation :

```pseudocode
algorithme retourne(L: ListeChaînée<T>) → ListeChaînée<T>:
    si L == ∅:
        rendre ∅
    
    (L2 := ListeChaînée<T>) ← retourne(L.queue)
    L.queue ← ∅
    L2.concatène(L)
    rendre L2
```

La complexité vaut :

$C(n) = \mathcal{O}(n) + C(n-1)$ où $n$ est la taille de la liste. ce qui donne une complexité de $\mathcal{O}(n^2)$ ce qui est un peut trop.

La complexité importante est due au fait que l'on fait trop de concaténations inutiles. Pour palier ça, utilisons les accumulateurs !

```pseudocode
algorithme retourne(L: Maillon<T>, acc: Maillon<T>) → Maillon<T>:
    si L == ∅:
        rendre acc
    L2 ← L.pop()
    L.append(acc)
    rendre retourne(L2, L)
```

Et on retourne la liste en commençant par un accumulateur vide. Par exemple si on cherche à retourne la liste `[1, 2, 3]`{.language-} :

```pseudocode
retourne([1, 2, 3], ∅)  = 
retourne([2, 3], [1])   =
retourne([3], [2, 1])   =
retourne([], [3, 2, 1]) = [3, 2, 1]
```

La complexité est maintenant à nouveau de $C(n) = \mathcal{O}(1) + C(n-1)$ donc bien linéaire en la taille de la liste chaînée.
{% enddetails %}

## Deque 

{% exercice %}
Créez une structure de Deque en utilisant une liste doublement chaînée. Toutes les opérations doivent être en temps constant.
{% endexercice %}

{% details "corrigé" %}

> TBD il faut garder un lien vers le dernier.

{% enddetails %}

## Liste circulaire

On modélise un roulement entre $n$ personne par une liste circulaire où l'on peut passer du dernier élément au premier.

{% exercice %}
Montrez que l'on peut créer une structure de liste circulaire avec une liste doublement chaînée.
{% endexercice %}
{% details "corrigé" %}

> TBD il faut garder un lien vers le dernier.

{% enddetails %}


{% exercice %}
Proposez un algorithme linéaire permettant de changer le sens de rotation de la liste circulaire.
{% endexercice %}
{% details "corrigé" %}

> TBD 

{% enddetails %}

{% exercice %}
Montrez que l'on peut créer une structure de liste circulaire avec une liste chaînée, et proposez un algorithme linéaire permettant de changer le sens de rotation de la liste circulaire.
{% endexercice %}
{% details "corrigé" %}


p -> q -> r

1. q -> p
2. p = q
3. q = r
4. r = q. suivant
5. on continue tant que p ≠ r

{% enddetails %}
