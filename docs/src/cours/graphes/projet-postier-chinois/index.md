---
layout: layout/post.njk

title: "Problème du postier chinois"
authors: 
    - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un problème d'optimisation où la théorie des graphes peut aider.

Nous allons étudier le problème du [postier chinois](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_postier_chinois), proposé par le mathématicien chinois [管梅谷](https://fr.wikipedia.org/wiki/Meigu_Guan) en 1962 :

{% note "**Définition**" %}
Soit $G = (V, E, A)$ un [graphe mixte](../structure#definition-graphe-mixte){.interne} connexe, et $f: E \cup A \rightarrow \mathbb{R}^+$ une fonction de valuation des arcs et arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-circuit (des arêtes/arcs peuvent apparaître plusieurs fois) passant par toutes les arêtes et les arcs du graphe mixte de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Nous ne donnerons pas ici les algorithmes exactes pour le résoudre mais donnerons les liens vers les parties (suivantes) de ce cours qui vous permettrons de le résoudre. Voyez ça comme une justification, un fil rouge, de ce qui va suivre.

> TBD à finir.
> TBD revue :
>
> - <https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/7d72c3b6-c1f3-4f71-87ef-54d32aad57c5/content>
> - <https://pubsonline.informs.org/doi/pdf/10.1287/opre.43.2.231>
> - <https://www.rand.org/content/dam/rand/pubs/reports/2007/R375.pdf> p70

Nous nous intéresserons ici à un cas particulier du problème où $G$ est juste un graphe :

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe connexe, et $f: E \rightarrow \mathbb{R}^+$ une fonction de valuation des arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-cycle (des arêtes peuvent apparaître plusieurs fois) passant par toutes les arêtes du graphe de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Le problème du postier chinois permet de modéliser les problèmes de tournées (poste, ramassage des ordures, ...) dans des villes.

{% info %}
On est obligé de  considérer des pseudo-cycles car le graphe considéré n'est pas forcément [eulérien](../parcours-eulériens){.interne} : il faut passer plusieurs fois par certaines arêtes pour en atteindre d'autres.
{% endinfo %}

## Éléments de résolution

Edmonds et Johnson en 1973 ont démontré que le problème du postier chinois était polynomial dans les cas suivant :

- graphe pondéré en $\mathcal{O}(n^3)$
- graphe orienté pondéré en $\mathcal{O}(n^3)$ également
- graphe mixte pair

Il est cependant NP-complet pour les graphes mixtes dans le cas général ([Papadimitriou](https://fr.wikipedia.org/wiki/Christos_Papadimitriou), 1976)

### Graphe simple

Si le graphe est eulérien, un cycle eulérien résout le problème. S'il ne l'est pas, on peut utiliser l'exercice suivant :

{% exercice %}
Montrer que tout graphe contient un nombre pair de sommets de degré impair.
{% endexercice %}
{% details "corrigé" %}
On a $\sum\delta(x) = 2 \cdot \vert E \vert$. De là, comme la somme des degrés des sommets de degré pair est paire, on en conclue que la somme des degrés des sommets de degré impair est également paire : il y a un nombre pair de sommet de degré impair.

{% enddetails %}

> TBD finir

### Graphe mixte

> TBD

## Projet

> TBD : ici données = (trouver le jeu de données)
> 
> * les villes française et on en prend une par département/territoire.
> * Liens = les k plus proches

> TBD <http://biblos.hec.ca/biblio/memoires/m2001no11.pdf>