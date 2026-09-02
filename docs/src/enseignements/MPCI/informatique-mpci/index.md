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

## Programme

### L1
Les 4 UE de L1 sont des UEes de tronc commun. Elles ont pour but d'enseigner le _lire-écrire-compter_ de l'informatique :

- concevoir un algorithme résolvant un problème simple,
- écrire un programme en python,
- compter le nombre d'opérations que va effectuer un algorithme avant de s'arrêter

#### S1

##### _Données, calcul en informatique_ (18h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/UE/3SMP/SMP1U25?external=1)
{% endlien %}

On y verra comment l'informatique représente ses données à partir d'une suite de 0 et de 1 :

- entiers,
- approximation de réels,
- caractères

Et comment elle les manipule en utilisant le calcul booléen.

##### _Bases de programmation_ (36h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/UE/3SMP/SMP1U24?external=1)
{% endlien %}

On y verra les principe de programmation communs à tous les langages informatique (variable, tests et boucles) et comment créer des programmes python (itératifs et récursifs) à partir de ces briques élémentaires.

#### S2

##### _Programmation objet_ (18h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/UE/3SMP/SMP2U22?external=1)
{% endlien %}



##### _Algorithmie 1_ (36h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/fr/licence/3SMP/PRSMP3I1)
{% endlien %}


### L2

#### S3

##### _Bases de données et Data science_ (20h)
##### _Structure de données - arbres et graphes_ (30h)

#### S4

##### _Langages, Automates, Grammaires_ (38h)
##### _Algorithmie 2, Reloaded_ (38h)

### L3

#### S5

##### _Intelligence Artificielle et Machine Learning_ (40h)
##### _Algorithmie 3, Revolutions_ (40h)

#### S6

##### _Calculabilité et Sémantique_ (36h)
##### _Logique_ (24h)
