---
layout: layout/post.njk
title: "Structures de données linéaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD <https://www.youtube.com/watch?v=kPqk07Gpj0A>
>

> TBD implémentation avec python : pile avec listes possible mais complexité amortie, pas max (et insert en O(n), attention). On utilise la structure deques

> 
La [structure de tableau](../écrire-algorithmes/pseudo-code/#tableaux){.interne} est l'élément élémentaire de toute structure permettant de stocker des objets. Elle est puissante car elle permet d'accéder en temps constant à tout élément qu'elle stocke (via son index) mais également limitée car le nombre d'objet qu'un tableau peut stocker (sa taille) est déterminé à sa création et est non modifiable. Enfin, l'index pour retrouver l'objet stocké est forcément un entier entre 0 et sa taille moins un.

Nous verrons dans cette partie que l'on peut faire sauter toutes les limitations d'un tableau au prix d'un coût en complexité, souvent acceptable au vu du gain en maniabilité.

Nous allons commencer par aborder la première extension des tableaux, les listes dont le coût est presque tout le temps négligeable (c'est pourquoi certains langages comme le python utilisent cette structure en lieu et place des tableaux).

## Listes

{% aller %}
[liste](./liste/){.interne}
{% endaller %}

## Tableau associatifs

Aussi appelé dictionnaires

{% aller %}
[fonction de hachage](fonctions-hash){.interne}
{% endaller %}
{% aller %}
[tableau associatif](tableau-associatif){.interne}
{% endaller %}

### Dérivés

> ensembles
