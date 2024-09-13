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

> listes chaînées très utilisé en système et en algo lorsque l'on a besoin uniquement d'accéder au suivant
> TBD : pile/files : structure
> TBD : bornées : faire avec des listes + démo amortie
> TBD : decques circulaires
> TBD : faire gain/perte
> TBD : exo pile/file simple (jouer avec la structure) et usage dans des algos. Montrer aussi que la pile peut être utilisée pour stocker des variables : faire fibo et enfin dire que c'est comme ça en mémoire : heap et stack. Donner exemple de l'appel de fonction et de la recursion.

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

