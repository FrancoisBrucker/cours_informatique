---
layout: layout/post.njk
title: Chemins, cycles et connexité
authors: 
    - François Brucker

eleventyNavigation:
  key: "Chemins, cycles et connexité"
  parent: "Graphes"
---

<!-- début résumé -->

Chemins, cycle et connexité dans les graphes : définitions et premières propriétés.

<!-- fin résumé -->

Un graphe $G=(V, E)$ rend compte d'une *relation* (les arêtes) entre des objets (les sommets). Une grande part des applications des graphes viennent du fait que l'on cherche à décrire ou parcourir objets en suivant localement les relations. Cette curte partie vise à poser les diverses définitions relatives à ces notions et à exhiber quelques propriétés soit utiles, soit belles à démontrer, soit les deux.

> TBD : dessins exemples.

## Définitions

### Chemin, cycles et circuits

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe (non) orienté. Un **chemin** est une suite :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que :

1. $v_iv_{i+1}$ soit une arête (*resp.* arc) du graphe quelque soit $0 \leq i < k$
2. les arêtes (*resp.* arcs) sont deux à deux distinctes.
  
Le chemin $C$ à une **longueur** de $k$ (c'est le nombre d'arêtes). Un chemin de longueur $0$ est le chemin vide, sans arête (*resp.* arc).

{% endnote %}

On peut affaiblir la notion de chemin pour les graphes orienté :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Une **chaîne** est une suite :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que :

1. soit $v_iv_{i+1}$ soit $v_{i+1}v_i$ est un arc du graphe pour tout $0 \leq i < k$
2. les arcs sont deux à deux distinctes.
  
La chaîne $C$ à une **longueur** de $k$ (c'est le nombre d'arcs). Un chemin de longueur $0$ est le chemin vide, sans arête (*resp.* arc).

{% endnote %}

Un chemin nous permet de définir un cycle pour les graphes non-orientés :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe non orienté. Un **cycle** est un chemin

$$C = v_0v_1\dots v_i \dots v_k$$

tel que $v_0 = v_k$
  
{% endnote %}

Pour les graphes orientés, ça se complique un peu car on a coutume de différentier cycle (le sens de l'arc est indifférent) de circuit (on peut parcourir le cycle dans l'ordre) :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Un **cycle**  est une suite :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que :

1. soit $v_iv_{i+1}$ soit $v_{i+1}v_i$ est un arc du graphe quelque soit $0 \leq i < k$
2. les arcs sont deux à deux distinctes.
3. $v_0 = v_k$

{% endnote %}

{% note "**Définition :**" %}
Soit $G = (V, E)$ un (multi-)graphe orienté. Un **circuit** est un cycle :

$$C = v_0v_1\dots v_i \dots v_k$$

de sommets du graphe telle que $v_iv_{i+1}$ est un arc du graphe quelque soit $0 \leq i < k$

{% endnote %}

Enfin, certains problèmes nécessitent de passer plusieurs fois par les même arêtes (*resp.* arcs), on parle alors de **pseudo-chemin**, **pseudo-chaîne**, **pseudo-cycle** et de **pseudo-circuit**.

### Connexité

{% note "**Définition :**" %}
Un graphe est dit **connexe** si pour toute paire de sommets $x$ et $y$ il existe un chemin allant de $x$ à $y$ dans $G$.

Si le graphe est orienté :

* il est **connexe** si pour toute paire de sommets $x$ et $y$ il existe un chemin allant de $x$ à $y$ ou un chemin allant de $y$ à $x$ dans $G$.
* il est dit **fortement connexe** s'il existe pour toute paire $x$ et $y$ de sommet un chemin allant de $x$ à $y$ et un chemin allant de $y$ à $x$.
{% endnote %}

La connexité est une notion très importante en théorie des graphes. Elle permet de relier deux sommets entre eux par des relations. D'un point de vue pratique on aime bien les graphes connexes, pensez à *google maps* où l'on aime bien pouvoir faire des aller-retours.

{% note "**Définition :**" %}
> TBD : composantes connexes
{% endnote %}

> TD on aime les geaphes connexe. Souvent (toujours) si un graphe n'est pas connexe on le partitionnera en ses composantes connexes qui peuvent être vues comme des graphes distincts. pour les analyser séparément (il n'y a aucun lien entre les composantes connexes)
Du point de vue de la connexité, certains sommet ou arêtes sont plus important que d'autres :

{% note "**Définition :**" %}
> TBD :  isthme et point d'articulation
{% endnote %}


## Propriétés

- chemin, chemin élémentaire
- algo est-ce chemin 
- chemin élémentaire
déf, exemple + code

existe-t-il un chemin entre a et b ? algo complexité

## algo Connexité

simple, forte

algo bourrin, algo Kruskal.

connexe => >m-1 
>(m-1(m-2/2)) => connexe

## Cycle

existe-t-il un cycle entre a et b ? algo complexité

lien à garder car référencé. :

existence de cycles <div id="prop-cycles-graphe"></div>

