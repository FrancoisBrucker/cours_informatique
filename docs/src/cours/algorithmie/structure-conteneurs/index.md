---
layout: layout/post.njk
title: "Structure de données linéaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La [structure de tableau](../écrire-algorithmes/pseudo-code/#tableaux){.interne} est l'élément élémentaire de toute structure permettant de stocker des objets. Elle est puissante car elle permet d'accéder en temps constant à tout élément qu'elle stocke (via son index) mais également limitée car le nombre d'objet qu'un tableau peut stocker (sa taille) est déterminé à sa création et est non modifiable. Enfin, l'index pour retrouver l'objet stocké est forcément un entier entre 0 et sa taille moins un.

Nous verrons dans cette partie que l'on peut faire sauter toutes les limitations d'un tableau au prix d'un coût en complexité, souvent acceptable au vu du gain en maniabilité.

Nous allons commencer par aborder la première extension des tableaux, les listes dont le coût est presque tout le temps négligeable (c'est pourquoi certains langages comme le python utilisent cette structure en lieu et place des tableaux).

## Listes

{% aller %}
[liste](./liste/){.interne}
{% endaller %}

### Dérivés

> listes chainées très utilisé en système et en algo lorsque l'on a besoin uniquement d'accéder au suivant
> TBD : pile/files
> TBD : bornées
> TBD : circulaires
> TBD : faire gain/perte

## Tableau associatifs

Aussi appelé dictionnaires

{% aller %}
[fonction de hachage](fonctions-hash){.interne}
{% endaller %}
{% aller %}
[dictionnaires](dictionnaire){.interne}
{% endaller %}

### Dérivés
> ensembles

