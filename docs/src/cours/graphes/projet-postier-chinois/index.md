---
layout: layout/post.njk

title: "Problème du postier chinois"
authors: 
    - François Brucker

eleventyNavigation:
  key: "Problème du postier chinois"
  parent: "Graphes"
---

<!-- début résumé -->

Un problème d'optimisation où la théorie des graphes peut aider.

<!-- fin résumé -->

Nous allons étudier le problème du [postier chinois](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_postier_chinois), proposé par le mathématicien chinois [管梅谷](https://fr.wikipedia.org/wiki/Meigu_Guan) en 1962 :

{% note "**Définition :**" %}
Soit $G = (V, E, A)$ un [graphe mixte](../structure#definition-graphe-mixte) connexe, et $f: E \cup A \rightarrow \mathbb{R}^+$ une fonction de valuation des arcs et arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-circuit (des arêtes/arcs peuvent apparaître plusieurs fois) passant par toutes les arêtes et les arcs du graphe mixte de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Nous nous intéresserons ici à un cas particulier du problème où $G$ est juste un graphe :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un graphe connexe, et $f: E \rightarrow \mathbb{R}^+$ une fonction de valuation des arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-cycle (des arêtes peuvent apparaître plusieurs fois) passant par toutes les arêtes du graphe de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Le problème du postier chinois permet de modéliser les problèmes de tournées (poste, ramassage des ordures, ...) dans des villes.

## Modélisation d'une ville par un graphe

Prenons l'exemple de la poste. Un facteur doit passer par chaque rue d'un quartier pour délivrer le courier, le départ et l'arrivée de sa tournée se faisant au bureau de poste du quartier. Pour que sa tournée soit la plus courte possible il faut qu'il repasse le moins possible par les même rues.

Pour modéliser cela informatiquement, il faut commencer par modéliser une ville ou un quartier par un graphe mixte. La façon classique de procéder est de considérer :

* que les croisements forment l'ensemble des sommets
* les routes à double sens forment les arêtes
* les routes à sens unique forment les arcs

> TBD : osmnx marseille (juste les commandes. Avec lien vers tuto plus complet si possible)

## Résolution du problème

si euler ok. 

Si graphe aussi ok avec couplage (on verra l'algo bien plus tard mais ca marche)

Si graphe mixte : np difficile.


## projet


1. OSM et Marseille : chemins
2. OSM et Marseille : circuit de ramassage des ordures [Et si l'on codait tout ça ?]({{ "/cours/graphes/circuits-euleriens" | url }})

> TBD :
>
> * utiliser OSM pour vérifier si marseille est connexe, trouver des chemin entre, etc.
> * utiliser networkx (ou autre pour ça)
