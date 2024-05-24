---
layout: layout/post.njk 
title: "S5 : Algorithmie avancée"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

## TBD

> MIT algo. <https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp>

## Randomized algorithms

- Hasard ?
- regarder dans le Kleinberg/Tardos
- cours Dieter Kratch
- <https://www.youtube.com/watch?v=0r2D32esF3Y> et <https://www.youtube.com/watch?v=GS2MxmorEzc>
- ? <https://www.youtube.com/watch?v=bsZXgXdSomc&list=PLOMwD5hwqoJ_slbq9iSE6tURVqX5eLKq8>

## Cryptographie

- reprendre cours 23-24

## C et structures de données

- modèle von Neumann pour un ordinateur
- gestion de la mémoire :
  - noyau programme et mémoire
  - données : dépend du type des données.

- C : compilation et pointeurs
- binary search <https://www.youtube.com/watch?v=GU7DpgHINWQ&list=PLl0KD3g-oDOHpWRyyGBUJ9jmul0lUOD80&index=3>
- python et C
- structures de données en C :

  - <https://www.youtube.com/watch?v=VOpjAHCee7c&list=PL9IEJIKnBJjFiudyP6wSXmykrn67Ykqib>
  - pile/file : pointeur et à la Knuth
  - graphes et arbres : exemple de la FAT

## Graphes

- bi-parti
- planaire
- coloration
- arbres : propriété, code Prüfer
- k-connectivité
- flots
- postier chinois
- couplage
- Hamilton
- graphes infinis
- random graphs
- union-find

## Complexité

- languages
- P et NP
- réductions
- Cook et Turing
