---
layout: layout/post.njk

title: Projet chemins de longueur minimum
authors: 
    - François Brucker

eleventyNavigation:
  key: "Projet chemins de longueur minimum"
  parent: "Graphes"
---

<!-- début résumé -->

Application du problème de la recherche de chemins de longueur minimum à la création de trajets routiers.

<!-- fin résumé -->

## Modélisation d'une ville par un graphe

Prenons l'exemple de la poste. Un facteur doit passer par chaque rue d'un quartier pour délivrer le courier, le départ et l'arrivée de sa tournée se faisant au bureau de poste du quartier. Pour que sa tournée soit la plus courte possible il faut qu'il repasse le moins possible par les même rues.

Pour modéliser cela informatiquement, il faut commencer par modéliser une ville ou un quartier par un graphe mixte. La façon classique de procéder est de considérer :

* que les croisements forment l'ensemble des sommets
* les routes à double sens forment les arêtes
* les routes à sens unique forment les arcs

Dans ce qui suivra :

* on considérera ue toutes les routes sont à double-sens (non orienté)
* qu'il ne peux exister qu'une route entre deux croisement (pas de multi-graphe)

Un quartier, une ville ou la partie du monde considéré est un graphe $G=(V, E)$ connexe où :

* les rues sont les arêtes
* les croisements sont les sommets

## Projets

1. [Projet openstreetmap](chemin-OSM)
2. [Chemins et Hub](chemin-OSM)
