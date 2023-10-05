---
layout: layout/post.njk

title: DM

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

1. lib
  - liste python avec struct
  - compilation séparée
  - faire une lib statique
2. dico
  - utiliser liste pour déco avec modulo
  - nb random pour vérifier la taille des listes selon taille de dico
3. avec nb fixe d'élément en utilisant une fat
4. liste circulaire. Uniquement ajout
5. liste circulaire avec suppression et flag "a existé" en plus du flag "vide"


- exam ? [algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [listes chaînées intrusives](https://www.data-structures-in-practice.com/intrusive-linked-lists/)
- utiliser une fonction de hash puis dictionnaire circulaire de knuth
