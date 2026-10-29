---
layout: layout/post.njk 
title:  "Structures de données avancée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : Knuth dancing links <https://www.youtube.com/watch?v=_cR9zDlvP88>{.externe} avec pointeurs




> TBD <https://www.youtube.com/watch?v=TdtNViWk45I>{.externe} implémentation go

## hash 2.0 améliorations

- hash :
  - _open addressing_
  - perfect
  - universal

{% lien %}
[Universal & Perfect Hashing](https://www.youtube.com/watch?v=z0lJ2k0sl1g){.externe}
{% endlien %}

> TBD circulaire + Knutheries.

### Hash universel

Pour que notre structure de dictionnaire soit de complexité $\mathcal{O}(1)$ en moyenne, on a supposé que nos fonction de hachage étaient utiles : les probabilités sont uniformes si les clés sont choisies aléatoirement.

Cette hypothèse est cependant tres rarement vérifiée en pratique, les clés ont souvent quelque chose en commun (numéro de téléphones, noms d'utilisateurs, etc). Pour palier ce problème épineux on renverse le problème et plutôt que de choisir des clés aléatoire, on choisi aléatoirement une fonction de hash !

### perfect hashing

> - <https://en.wikipedia.org/wiki/Dynamic_perfect_hashing>{.externe}
>  - chichelli : <https://courses.cs.vt.edu/~cs3114/Summer13/Notes/T12.PerfectHashFunctions.pdf>{.externe}
>  - <https://www.cs.otago.ac.nz/cosc242/pdf/L11.pdf>{.externe} 

