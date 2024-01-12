---
layout: layout/post.njk
templateEngineOverride: njk, md

title: Algorithm design
tags: ['enseignement', 'ECM']
authors: 
  - Pascal Préa
  - François Brucker

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---
{% prerequis "**Prérequis** :" %}

* [Avoir un python qui fonctionne]({{ '/tutoriels/installation-python'  }})
* [Avoir un éditeur de texte opérationnel]({{ '/tutoriels/vsc-installation-et-prise-en-main'  }})
* [Et qui fonctionne avec python]({{ '/tutoriels/vsc-python'  }})

{% endprerequis %}

<!-- début résumé -->

Le but de cette UEes est de montrer les principales stratégies de conception algorithmiques pour résoudre de grandes familles de problèmes concrets (problèmes d'optimisation, de construction de solutions exactes, parcours, …). Chaque stratégie sera illustrée par plusieurs exemples et plusieurs séances seront consacrées à leurs implémentations.

<!-- fin résumé -->

## Programme

1. divide & conquer (2h, Pascal Préa)
2. problème de l'alignement de séquences (3h, François Brucker) (**venez avec votre ordinateur**)
   * [étude de l'alignement de séquences]({{ '/cours/algorithme-code-théorie/algorithme/étude-alignement-séquences'  }})
   * [code alignement de séquences]({{ '/cours/algorithme-code-théorie/code/projet-alignement-séquences'  }})
3. programmation dynamique et NP-complétude (3h, PAscal Préa)
4. [algorithmes gloutons, principes]({{ '/cours/algorithme-code-théorie/algorithme/algorithmes-gloutons'  }}) (2h, François Brucker)
5. [algorithmes gloutons, mises en œuvres]({{ '/cours/algorithme-code-théorie/code/projet-gloutons-voyageur-de-commerce'  }}) (3h, François Brucker) (**venez avec votre ordinateur**). [Une idée du code corrigé (sans le recuit simulé)](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithme-code-th%C3%A9orie/code/projet-gloutons-voyageur-de-commerce/projet)
6. problèmes d'énumération (2h, Pascal Préa)
7. Exposés (2h+, Note)

## Notes

La note sera une donné à l'issue d'une présentation (par groupes de 1 à 3 élèves) d'une algorithme ou d'une méthode qui aura lieu la dernière séance.

### Soutenance

Lors de la soutenance qui devra durer 10min (exactement) vous devrez :

1. définir la problématique
2. montrer des cas d'usages pratiques
3. exposer le design de l'algorithme de résolution
4. exposer le fonctionnement de l'algorithme ainsi que sa complexité
5. dire pourquoi c'est un bel algorithme

### Projets

{% info %}
Les projets ont des difficultés, allant de 1 à 3 ☆. A qualité d'exposé égale, un groupe ayant choisi un  projet plus dure aura une meilleure note. Mais un projet raté aura de toute façon une note en dessous de la moyenne.
{% endinfo %}
{% attention %}
Il faut que l'exposé ait une valeur ajoutée par rapport à ce que l'on peut trouver en gougueulant l'énoncé.
{% endattention %}

Chaque groupe doit prendre un algorithme parmi :

1. [☆] Problème de matching et résolution dans le cadre d'un graphe bi-parti
2. [☆☆☆] Alignement de séquences linéaire en mémoire
3. [☆] Algorithme glouton pour la coloration de graphes
4. [☆☆] Algorithme du calcul de la médiane d'un ensemble de de nombre de complexité **en moyenne** linéaire
5. [☆☆☆] Algorithme du calcul de la médiane d'un ensemble de de nombre de complexité **maximale** linéaire
6. [☆☆] Algorithme de GRAHAM pour le calcul d'une enveloppe convexe d'un ensemble de points du plan
7. [☆☆] Algorithme 2-opt pour la résolution du problème du voyageur de commerce
8. [☆☆] Algorithme de JARVIS pour le calcul d'une enveloppe convexe d'un ensemble de points du plan
9. [☆] Algorithme de Ford & Fulkerson pour la résolution de flot.
10. [☆] Algorithme quad-tree pour gérer la collision d'objets du plan
11. [☆☆] Gestion de file de priorité
12. [☆☆] FIFO (définition, usage et implémentation avec un tableau circulaire)
13. [☆☆] Calcul de l'élément majoritaire d'un ensemble s'il existe, en complexité linéaire
14. [☆☆] Arbres lexicographiques
15. [☆] Algorithme $A^\star$ pour la recherche de chemins
16. [☆☆] Triangulation de Delaunay & diagrammes de Voronoï
17. [☆☆] algorithme de Knuth pour mélanger un tableau d'entier
18. [☆☆] Alignement local de 2 séquences de caractères
19. [☆☆] Maximum de parcimonie en phylogénie
20. [☆☆] AABB-tree pour la détection de collisions d'objet du plan

Choix des projet : [google sheet](https://docs.google.com/spreadsheets/d/1Ur5QfYY4XxE3v3X6nZlfCYmhYw-9xuE9Em2qIgiXh9o/edit#gid=0)
