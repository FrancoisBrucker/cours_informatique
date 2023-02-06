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

> TBD : à finir

Nous allons étudier le problème du [postier chinois](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_postier_chinois), proposé par le mathématicien chinois [管梅谷](https://fr.wikipedia.org/wiki/Meigu_Guan) en 1962 :

{% note "**Définition**" %}
Soit $G = (V, E, A)$ un [graphe mixte](../structure#definition-graphe-mixte) connexe, et $f: E \cup A \rightarrow \mathbb{R}^+$ une fonction de valuation des arcs et arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-circuit (des arêtes/arcs peuvent apparaître plusieurs fois) passant par toutes les arêtes et les arcs du graphe mixte de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Nous nous intéresserons ici à un cas particulier du problème où $G$ est juste un graphe :

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe connexe, et $f: E \rightarrow \mathbb{R}^+$ une fonction de valuation des arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-cycle (des arêtes peuvent apparaître plusieurs fois) passant par toutes les arêtes du graphe de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Le problème du postier chinois permet de modéliser les problèmes de tournées (poste, ramassage des ordures, ...) dans des villes.

{% info %}
On est obligé de  considérer des pseudo-cycles car le graphe considéré n'est pas forcément [eulérien](../parcours-eulériens) : il faut passer plusieurs fois par certaines arêtes pour en atteindre d'autres.
{% endinfo %}

## Données

> TBD : ici données = (trouver le jeu de données)
> 
> * les villes française et on en prend une par département/territoire.
> * Liens = les k plus proches

> TBD <http://biblos.hec.ca/biblio/memoires/m2001no11.pdf>