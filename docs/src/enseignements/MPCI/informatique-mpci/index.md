---
layout: layout/post.njk 
title: "L'informatique en licence MPCI"

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---


> TBD la matière informatique. Matière "incarnée". 

Les UEes.

## L1
Les 4 UE de L1 sont des UEes de tronc commun. Elles ont pour but d'enseigner le _lire-écrire-compter_ de l'informatique :

- concevoir un algorithme résolvant un problème donné
- écrire un programme que l'on peut exécuter
### S1

- 18h _Données, calcul en informatique_ 
- 36h _Bases de programmation_

### S2

- 18h _Programmation objet_ 
- 36h _Algorithmie 1_

## L2

### S3

- 20h _Bases de données et Data science_
- 30h _Structure de données - arbres et graphes_

### S4

- 38h _Langages, Automates, Grammaires_
- 38h _Algorithmie 2, Reloaded_

## L3

### S5

- 40h _Intelligence Artificielle et Machine Learning_
- 40h _Algorithmie 3, Revolutions_

### S6

- 36h _Calculabilité et Sémantique_
- 24h _Logique_