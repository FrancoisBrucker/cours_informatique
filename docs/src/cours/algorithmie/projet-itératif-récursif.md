---
layout: layout/post.njk
title: "Projet : Écrire et prouver des algorithmes Itératif et récursif"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Écrire des algorithmes (simples) en pseudo-code pour résoudre des problèmes algorithmiques.

## Maximum d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
maximum(t: [réel], i: entier) → entier
```

Qui rend l'indice $0 \leq j \leq i$ tel que $t[j] = \min(\{t[k] \vert 0\leq k \leq i\})$.
{% endexercice %}
{% details "corrigé" %}

> TBD algorithme
> TBD finitude
> TBD correction

{% enddetails %}

## Concaténation

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
concaténation(début: [entier], fin: [entier]) → [entier]
```

Qui rend **un nouveau tableau** contenant la concaténation de `début`{.language-} et de `fin`{.language-}.
{% endexercice %}
{% details "corrigé" %}

> TBD algorithme
> TBD : doit commencer par créer un tableau.
> TBD finitude
> TBD correction

{% enddetails %}

## Suppression de valeurs

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
supprime(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}. Le nouveau tableau aura la même taille que le tableau `t`{.language-} passé en premier paramètre.
{% endexercice %}
{% details "corrigé" %}

> TBD algorithme
> TBD : doit commencer par créer un tableau et une boucle sur i avec incrément de j.
> TBD finitude
> TBD correction

{% enddetails %}

Utilisez l'algorithme concaténation de la question précédente pour résoudre l'exercice suivant :

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
supprime(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}. Le nouveau tableau aura la même taille que le tableau `t`{.language-} passé en premier paramètre.
{% endexercice %}
{% details "corrigé" %}

> TBD algorithme
> TBD : doit commencer par créer un tableau.
> TBD finitude
> TBD correction

{% enddetails %}

## Retournement d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
reverse_indice(t: [entier], i: entier) → vide
```

Qui **modifie le tableau** passé en entrée (il ne rend rien !) de telle sorte que les éléments $t[j]$ et $t[t.longueur - 1 - j]$ soit échangés pour tous $i \leq j < t.longueur - i$
{% endexercice %}
{% details "corrigé" %}

> TBD algorithme récursion terminale
> TBD finitude
> TBD correction

{% enddetails %}

Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Par exemple si l'on veut retourner complètement un tableau il faudrait écrire `reverse_indice(t: [entier], 0)`{.language-}. Le paramètre $i$ est un paramètre important pour la récursion mais inutile pour l'appel global. Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion. Pour le retournement d'un tableau, l'algorithme sera :

```pseudocode
fonction reverse_indice(t: [entier], i: entier) → vide
    ...  # code de la fonction récursive

algorithme reverse(t: [entier]) → vide
    reverse_indice(t, 0)
```

## Récursion terminale

> TBD on voit que la récursion est le dernier calcul dans l'exemple précédent. On appelle ça récursion terminale. Ceci permet de créer des algorithmes itératif. Le faire là avant de généraliser.

> TBD factorielle pas terminale. Le rendre terminale
> 
> terminale/ pas terminale. <https://web4.ensiie.fr/~dubois/recursivite.pdf>
> 
> récursivité terminale = qu'une suite d'égalité. C'est donc super.

## Dichotomie

> TBD est présent tableau trié.
> TBD récursif -> récursif terminal -> itératif
> <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration>

## Fibonacci

> Marche pas toujours ex : Fibonacci. On ruse.
> On peut montrer que toutes les fonctions récursives ne peuvent pas être terminale.

## Fonction 91 de McCarty

Mais parfois on crois que c´st pas possible alors que ça l'est.

Dans le même ordre d'idée que la fonction de Takeuchi.

> inventeur du lisp.

> TBD : <https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy>
>
> TBD a écrire algo avec récursion puis : essayer de se passer de f(f(x))
>
> 1. écrire comme récursion terminale (cf. wikipédia pour la fonction et <https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale> pour la définition)

<https://www.corsi.univr.it/documenti/OccorrenzaIns/matdid/matdid779820.pdf>
> 

> TBD et quelle est sa valeur ?

## Pair et impair

> TBD Récursion croisée
