---
layout: layout/post.njk 
title:  "Structures de données avancée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD reprendre les objets de base et dire tous de taille fixe. Idem tableau = n * taille du type de sa structure + 1 entier.
> TBD dire entier = tableau de bits. Par défaut 26b = 2^64 entier. Par défaut on dira que pas de débordement. Parler des négatif avec le complément à 2. Dire qu'on verra ça précisément plus tard et juste donner les bornes

> TDB ici
> TBD parler de pointeur directement dans les structures.
> TBD dire que pour python tout est pointeur.
> TBD à refaire bien propre.

> TBD voir si toutes les structures de <https://www.youtube.com/watch?v=6fnmXX8RK0s> y sont.

## Complexité amortie

> TBD 


## Structures arborées

{% lien %}
[Structures arborées](structures-arborées){.interne}
{% endlien %}

## hash 2.0 améliorations

- hash :
  - _open addressing_
  - perfect
  - universal

{% lien %}
[Universal & Perfect Hashing](https://www.youtube.com/watch?v=z0lJ2k0sl1g)
{% endlien %}

### Hash universel

Pour que notre structure de dictionnaire soit de complexité $\mathcal{O}(1)$ en moyenne, on a supposé que nos fonction de hachage étaient utiles : les probabilités sont uniformes si les clés sont choisies aléatoirement.

Cette hypothèse est cependant tres rarement vérifiée en pratique, les clés ont souvent quelque chose en commun (numéro de téléphones, noms d'utilisateurs, etc). Pour palier ce problème épineux on renverse le problème et plutôt que de choisir des clés aléatoire, on choisi aléatoirement une fonction de hash !

### perfect hashing

> - <https://en.wikipedia.org/wiki/Dynamic_perfect_hashing>
>  - chichelli : <https://courses.cs.vt.edu/~cs3114/Summer13/Notes/T12.PerfectHashFunctions.pdf>
>  - <https://www.cs.otago.ac.nz/cosc242/pdf/L11.pdf> 

