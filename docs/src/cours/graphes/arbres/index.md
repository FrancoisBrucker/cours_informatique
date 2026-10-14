---
layout: layout/post.njk

title: Arbres

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Explorer les propriétés et l'intérêt de l'arbre.

## Définitions et propriétés

{% aller %}

[Définitions et premières propriétés](définitions)

{% endaller %}

### Représentation graphique

{% aller %}

[Tracés d'arbre](tracés)

{% endaller %}

### Problème de l'arbre couvrant

{% aller %}

[Arbres couvrants](arbres-couvrants)

{% endaller %}

### Arbres de Cayley

{% aller %}

[Arbres de Cayley](cayley)

{% endaller %}

## Arbres plantés

{% lien %}
[Arbre pour l'algorithmique](https://chauvin.perso.math.cnrs.fr/book.pdf){.externe}
{% endlien %}

{% aller %}

[Arbres plantés](arbres-plantés)

{% endaller %}

### Arbres planaires

{% aller %}

[Arbres planaires](arbres-planaires)

{% endaller %}

### Arbres de Catalan

{% aller %}

[Arbres de Catalan](arbres-catalan)

{% endaller %}

### Arbres de Galton-Watson

{% aller %}

[Arbres de Galton-Watson](arbre-galton-watson)

{% endaller %}

## Isomorphisme d'arbres

{% exercice %}
Montrez que tout automorphisme d'arbre laisse invariant au moins un sommet ou une arête.

{% endexercice %}
{% details "solution" %}

> TBD écrire propre

1. vrai à 1 ou 2 sommets
2. les feuilles sont envoyées sur les feuilles par automorphisme
3. on supprime les feuilles
4. la restriction de l'automorphisme est un automorphisme de l'arbre effeuillé et la récursion passe.

{% enddetails %}

### Arbres de Pólya

> TBD def par par bijection d'arbres plantés
> TBD def ensembliste avec multi set : ensemble avec répétitions possibles (faire dessin)
> TBD def ensembliste se binarise en prenant juste des multi-set de taille 2.
>
> isomorphisme Arbres planté :
>
> - Aho, Hopcroft and Ullman <https://hal.science/hal-04232137/document>{.externe}
> - <https://info.faidherbe.org/MPII/11.pdf>{.externe}

### Arbres non plantés

> TBD <https://perso.ens-lyon.fr/eric.thierry/Graphes2010/marthe-bonamy.pdf>{.externe} on peut le faire de façon linéaire.
