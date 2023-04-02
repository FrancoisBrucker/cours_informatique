---
layout: layout/post.njk 
title: "Etude : enveloppe convexe"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../étude-tris/"
---

<!-- début résumé -->

Introduction aux algorithmes de recherche d'enveloppe convexe.
<!-- end résumé -->

1. tri = "petit plaisir coupable" d'un informaticien
2. enveloppe convexe = "petit plaisir coupable 2.0" (plein de façon différente de le faire, problèmes intéressant de complexités et jolis algorithmes)

plan :

1. en 2d. Utilité en info, mais aussi en math, en physique, etc
2. enveloppe convexe facile à savoir si :
   1. point dedans
   2. intersection droite convexe
   3. collision
3. marche de jarvis
4. complexité :
   1. jarvis depend de la sortie
   2. borne min avec tri (depend uniquement de l'entrée)
   3. jarvis pas borne min
5. intermède sur tangente, trouver le min
6. divide and conquer sur deux disjoint
7. on est en complexité min dans le pire des cas tout le temps. Peut-on faire mieux en prenand en compte la sortie ?
8. intermède de regroupement de polygone convexes
   1. on a vu 2 disjoint
   2. si 2 pas disjoint ?
   3. et m pas disjoints
9. chan

ressources :

* général :
  * <https://en.wikipedia.org/wiki/Convex_hull_algorithms>
  * <https://fr.wikipedia.org/wiki/Enveloppe_convexe>
* O(nh) : <https://fr.wikipedia.org/wiki/Marche_de_Jarvis>
* chan :
  * <https://fr.wikipedia.org/wiki/Algorithme_de_Chan>
  * <https://en.wikipedia.org/wiki/Chan%27s_algorithm>
  * <https://athena.nitc.ac.in/~kmurali/Courses/CombAlg2013/chan.pdf>
* 1er en nlog(h) : <https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Seidel_algorithm>
* diviser pour régner et enveloppe convexe :
  * <https://datamove.imag.fr/denis.trystram/SupportsDeCours/DivideConquer.pdf>
  * <https://www.geeksforgeeks.org/convex-hull-using-divide-and-conquer-algorithm/>