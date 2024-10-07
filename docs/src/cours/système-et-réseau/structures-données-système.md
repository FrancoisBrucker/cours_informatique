---
layout: layout/post.njk

title: Structures de données

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à faire bien : problème et structure de donnée solution

- factorisation : <https://www.youtube.com/watch?v=9ONm1od1QZo>
- pile/tas
- tableau (évite la faute de cache)
  - temporalité spatiale
  - tableau de tableaux en une dimension (ligne, index des caches)
  - flags (dirty bit)
- bitmatructure-de-donnéetructures-de-données/
  - utilité : une information booléenne oui/non, activé/non activé, ...
  - où :
    - file system (bloc, inode)
    - flags
- liste chaînée :
  - utilité : ordre linéaire ou un élément peut bouger
  - où :
    - FAT
    - ordonnancement
  - attention : faute de cache
- arbre :
  - de recherche nombre
  - arbre associatif pour mapper des données
  - arbre stockage de données
- file (FIFO) : gestion des communications, lecture/écriture fichier
- pile (LIFO) : stockage des variables
