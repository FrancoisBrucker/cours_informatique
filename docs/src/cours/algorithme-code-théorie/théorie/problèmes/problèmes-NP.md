---
layout: layout/post.njk 
title:  "Problèmes"

eleventyNavigation:
    order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> problème NP =  vérifiable = ceux qui sont utiles en pratique

1. algorithme = résout quelque chose et plein de façon de résoudre
2. définition d'un problème
3. facile à voir si ok ou pas
4. Complexité d'un programme :
   1. monter que selon la forme log, n n^k et 2^n c'est pas pareil
      1. nombre max / heure
      2. nombre max / puissance de machine
   2. déf et parler de O, Theta
5. ex : SAT
   1. def et utilisabilité
   2. SAT et 3-SAT : deux problèmes équivalent
6. classes de problèmes
