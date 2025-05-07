---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Tri par paquets (bucket sort)

> TBD

Utile si on doit trier des objets via un id borné pas trop grand. C'est souvent le cas lorsque l'on utilise des données complexes, pensez à un tableau excel où nos données sont les lignes et l'index le numéro de la ligne (ou une colonne spécifique dont la valeur va de 1 au nombre de lignes)On peut alors s'arranger pour que $k \geq n$ ce qui rend ce tri très efficace.

## Tri par base

> TBD pseudo-code. [Wikipedia](https://fr.wikipedia.org/wiki/Tri_par_base)

Si la taille des entiers est fixée, ce qui est le cas au niveau du processeur où tous les entiers sonts codés sur 64bits, ce tri est le plus efficace possible.
