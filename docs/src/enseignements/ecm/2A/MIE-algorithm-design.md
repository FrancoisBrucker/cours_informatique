---
layout: layout/post.njk
templateEngineOverride: njk, md

title: Algorithm design
tags: ['enseignement', 'ECM']
authors: 
  - Pascal Préa
  - François Brucker

eleventyNavigation:
  key: "approfondissement MIE : Algorithm design"
  parent: 2A
  order: 1

---
{% prerequis "**Prérequis** :" %}

* [Avoir un python qui fonctionne]({{ '/tutoriels/installation-python' | url }})
* [Avoir un éditeur de texte opérationnel]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
* [Et qui fonctionne avec python]({{ '/tutoriels/vsc-python' | url }})

{% endprerequis %}

<!-- début résumé -->

Le but de cette UEes est de montrer les principales stratégies de conception algorithmiques pour résoudre de grandes familles de problèmes concrets (problèmes d'optimisation, de construction de solutions exactes, parcours, …). Chaque stratégie sera illustrée par plusieurs exemples et plusieurs séances seront consacrées à leurs implémentations.

<!-- fin résumé -->

## Programme

1. divide & conquer (2h, Pascal Préa)
2. problème de l'alignement de séquences (4h, François Brucker) (**venez avec votre ordinateur**)
3. programmation dynamique et NP-complétude (3h, PAscal Préa)
4. algorithmes gloutons, principes (2h, François Brucker)
5. algorithmes gloutons, mises en œuvres (3h, François Brucker) (**venez avec votre ordinateur**)
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
Il faut que l'exposé ait une valeur ajoutée par rapport à ce que l'on peut trouver en gouguelant l'énoncé.
{% endattention %}

Chaque groupe doit prendre un algorithme parmi :

* [☆] Problème de matching et résolution dans le cadre d'un graphe bi-parti
* [☆☆☆] Alignement de séquences linéaire en mémoire
* [☆] Algorithme glouton pour la coloration de graphes
* [☆☆] Algorithme du calcul de la médiane d'un ensemble de de nombre de complexité **en moyenne** linéaire
* [☆☆☆] Algorithme du calcul de la médiane d'un ensemble de de nombre de complexité **maximale** linéaire
* [☆☆] Algorithme de GRAHAM pour le calcul d'une enveloppe convexe d'un ensemble de points du plan
* [☆☆] Algorithme 2-opt pour la résolution du problème du voyageur de commerce
* [☆☆] Algorithme de JARVIS pour le calcul d'une enveloppe convexe d'un ensemble de points du plan
* [☆] Algorithme de Ford & Fulkerson pour la résolution de flot.
* [☆] Algorithme quad-tree pour gérer la collision d'objets du plan
* [☆☆] Gestion de file de priorité
* [☆☆] FIFO (définition, usage et implémentation avec un tableau circulaire)
* [☆☆] Calcul de l'élément majoritaire d'un ensemble s'il existe, en complexité linéaire
* [☆☆] Arbres lexicographiques
* [☆] Algorithme $A^\star$ pour la recherche de chemins
* [☆☆] Triangulation de Delaunay & diagrammes de Voronoï
* [☆☆] algorithme de Knuth pour mélanger un tableau d'entier
* [☆☆] Alignement local de 2 séquences de caractères
* [☆☆] Maximum de parcimonie en phylogénie
* [☆☆] AABB-tree pour la détection de collisions d'objet du plan
  