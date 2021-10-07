---
layout: page
title:  "Théorie des graphes : chemins"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [chemins]({% link cours/graphes/chemins.md %})
{: .chemin}

## But

Chemins entre deux sommets.

[éléments de corrigé]({% link cours/graphes/chemins-corrige.md %})

## définitions

Un chemin d'un graphe $G=(V,E)$ (orienté ou non) est une suite de sommets $s_0 \dots s_k$ telle que :

* $s_is_{i+1}$ est une arête
* $s_is_{i+1} \neq s_js_{j+1}$ si $i\neq j$

Si le graphe possède de plus une valuation qui associe un réel à toute arête, la **longueur d'un chemin** est la somme des valuations de ses arêtes.

## Dijkstra

L'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) permet, à partir d'un graphe orienté valué, de trouver un chemin de longueur minimum entre deux sommets $d$ (départ) et $a$ (arrivée).

Il ressemble beaucoup à l'[algorithme de Prim]({% link cours/graphes/arbres.md %}#algo-prim) que l'on a vu précédemment.

### pseudo-code

```text
Entrée :
    * un graphe orienté G = (V, E)
    * une valuation f qui associe un réel positif à toute arête de G
    * deux sommets d et a de V
Initialisation :
    * cout_entree(x) = +∞ pour tout sommet x
    * predecesseur(x) = x pour tout sommet x
    * V' = {}, E' = {}
Algorithme :
    * cout_entree(d) = 0
    * ajoute d à V' 
    * r = d   
    * tant que a n'est pas dans V':
        * pour tous les voisins sortant x de r qui ne sont pas dans V':
            * si cout_entree(x) >= cout_entree(r) + f(rx):
                cout_entree(x) = cout_entree(r) + f(rx)
                predecesseur(x) = r
        * soit x le sommet de V qui n'est pas dans V' minimisant cout_entree(x)
        * r = x
        * cout_entree(r) = 0
        * ajoute r à V' et (predecesseur(r), r) à E'
    * chemin = [a]
    * x = a
    * tant que x est différent de d:
        * x = predecesseur(x)
        * ajoute x au début de chemin        
Retour :
    chemin
```

> Notez que la valuation d'une arête est positive ou nulle.

### test

>Allez de Paris à Rana en moins de temps possible en utilisant l'algorithme de Dijkstra sur le graphe ci-après, qui représente les différents vols et leurs durées entre différentes villes d'Europe.
{:.a-faire}

![Paris à Rana]({{ "/assets/cours/graphes/chemin_paris_rana.png" | relative_url }}){:style="margin: auto;display: block;"}

### preuve {#preuve-dijkstra}

>En utilisant la preuve de l'algorithme de Prim, montrez que l'algorithme de Dijkstra rend un chemin de longueur minimum entre $d$ et $a$
{:.a-faire}

### complexité

> Quelle est la complexité de l'algorithme de Disjkstra ?
{:.a-faire}

## arborescence

On peut continuer l'algorithme de Diskstra après que $a$ ait été rentré dans $V'$, jusqu'à ce que l'on ait plus que des éléments de coût infini à faire rentrer dans $V'$ ou que $V'$ soit égal à $V$.

> Montrez que pour tous les sommets $x$ qui ne peuvent pas entrer dans $V'$, il n'existe pas de chemin entre $d$ et $x$ dans $G$
{: .a-faire}

### preuve {#preuve-dijkstra-arborescence}

> Montrez que si l'on peut continuer l'algorithme de Dijkstra jusqu'à ce que $V'$ soit égal à $V$ on obtient un graphe $G' = (V, E')$ tel que :
>
> * $\vert E' \vert = \vert V \vert -1$
> * il existe un unique chemin entre $d$ et tout autre sommet
> * le chemin entre $d$ et $x$ dans $G'$ est de poids minimum dans $G$
{: .a-faire}

### Prim vs Dijkstra

> Quelle est la différence entre Prim et Dijsktra ?
> Montrez que les problèmes qu'ils résolvent sont différents et en déduire que l'arborescence obtenue par l'algorithme de Dijsktra pour un graphe non orienté peut être différente de l'arbre de poids minimum obtenu par Prim
{: .a-faire}

## chemin le plus long

L'algorithme de Dijkstra permet de répondre à la question : *quelle est la longueur des chemins les plus courts partant d'un sommet*. Mais qu'en est-il du pendant : *quelle est la longueur des chemins les plus longs partant d'un sommet* ?

On suppose que le problème est maintenant : quel est la longueur maximale d'un chemin passant une unique fois par chaque sommet ?

C'est le problème du **plus long chemin élémentaire** (les sommets n'apparaissent qu'une unique fois).

### algorithme ?

Une idée serait de renverser les inégalités dans l'algorithme (de rentrer dans la structure à chaque fois l'élément de plus grand coût), puis de faire l'arborescence de Dijkstra pour chaque sommet de $V$ et enfin de prendre le chemin le plus long obtenu pour toutes les arborescences.

>Montrez que cette approche ne fonctionne pas.
{: .a-faire}

### chemin hamiltonien

Il est illusoire de tenter de trouver un algorithme pour résoudre le problème du chemin le plus long dans le cas général car il permettrait de résoudre le problème du [chemin hamiltonien](https://fr.wikipedia.org/wiki/Graphe_hamiltonien) qui peut s'écrire ainsi : existe-t-il un chemin élémentaire passant par tous les sommets d'un graphe G donné ?

> Montrer que si l'on pouvait résoudre le problème d'un chemin le plus long dans un graphe, on pourrait résoudre le problème du chemin hamiltonien.
{: .a-faire}

Ce problème est [NP-complet](https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet), c'est à dire qu'il fait parti des problèmes algorithmiques les plus durs à résoudre (et que le résoudre facilement permettrait de résoudre facilement tous les problèmes algorithmiques qu'on peut se poser).

> Notez comment une petite différence — remplacer sommet (hamiltonien) par arête (eulérien) — rend un problème soit très simple soit très compliqué à résoudre.

### graphes particuliers

Il existe tout de même 2 classes de graphes particulières qui admettent des solutions faciles pour le problème du chemin élémentaire le plus long :

* les [graphes orientés sans circuits](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9_acyclique)
* les [tournois](https://fr.wikipedia.org/wiki/Tournoi_(th%C3%A9orie_des_graphes))

#### graphe sans circuit

Un graphe orienté qui ne contient pas de circuit est souvent appelé *DAG* (direct acyclic graph).

On appelle **tri topologique** d'un graphe orienté $G = (V, E)$ un ordre total $<$ sur les sommets du graphe tel que $xy \in E$ implique $x < y$ dans l'ordre.

> Montrer que :
>
> 1. un graphe ne peut admettre de tri topologique que s'il n'a pas de cycle
> 2. pour un DAG, il existe toujours un sommet qui n'a pas de voisins entrant (*resp.* sortant)
> 3. en déduire qu'un DAG admet un tri topologique
> 4. conclure sur le fait qu'un graphe est un DAG si et seulement s'il admet un tri topologique
{: .a-faire}

On utilisera souvent ce tri pour résoudre des problèmes d'ordonnancement (on le verra tout à l'heure dans un cas d'importance certaine).

> Utiliser le tri pour trouver un chemin élémentaire de longueur maximum dans un DAG.
{: .a-faire}

#### tournoi

Un [tournoi](https://fr.wikipedia.org/wiki/Tournoi_(th%C3%A9orie_des_graphes)) est un graphe orienté $T = (V, E)$  tel que quelque soit $x \neq y \in V$ soit $xy$ soit $yx$ est une arête, mais pas les deux.

Un tournoi est très utilisé en théorie du choix social et en théorie des votes car il modélise bien les choix et les soucis entre choix locaux (quelque soit une alternative on en préfère l'une à l'autre) et optimum global (existe-t-il un choix qui est préféré à tous les autres).

Dans ce champ applicatif, les cycles sont problématiques (A est préféré à B qui est préféré à C qui est préféré à A).

> Montrer qu'un tournoi n'admet pas de cycle si et seulement si il est transitif
{: .a-faire}

Mais pour ce qui nous intéresse, il est rigolo de voir qu'un tournoi admet toujours un chemin qui passe par tous les sommets une unique fois.

> Montrez le
{: .a-faire}

Donc quelles que soient les préférences, on peut toujours ordonner les préférences selon un ordre total (même s'il y en a plusieurs) localement cohérent (pour chaque élément il est préféré à celui d'avant et on lui préfèrera celui d'après dans l'ordre).

### ordonnancement

Un [problème d'ordonnancement](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_l%27ordonnancement) peut se modéliser par un DAG nommé graphe de dépendances où si $xy$ est une arête alors il faut faire $x$ avant de pouvoir faire $y$.

> Pourquoi ne doit-il pas y avoir de cycles dans un graphe de dépendance ?
{: .a-faire}

Vous résolvez des problèmes d'ordonnancement tous les jours comme par exemple comment s'habiller le matin (voir graphe ci-après)

![habillage]({{ "/assets/cours/graphes/chemin_habillage.png" | relative_url }}){:style="margin: auto;display: block;"}

> Montrer que le tri topologique est une solution au problème d'ordonnancement. Appliquez le au problème de s'habiller le matin.
{: .a-afaire}

C'est encore un exemple où les contraintes sont locales et ou l'on cherche une solution globale.

## variantes

On va montrer trois variantes de la recherche d'un chemin de longueur minimale entre deux sommets pour des graphes valués d'intérêt pratique.

### poids négatifs

> Montrez que si le graphe peut avoir des valuations positives et négatives, l'algorithme de Dijkstra ne garantit pas de trouver un chemin de longueur minimum
{: .a-faire}

D'ailleurs, un tel chemin existe-t-il ?

> Montrez que s'il existe un circuit de valuation strictement négative (on appelle ces circuit **circuits absorbant**), la notion même de chemin de valuation minimum cesse d'exister
{: .a-faire}

Pour régler ce problème, on utilise l'algorithme de [Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall) qui trouve, en $\mathcal{O}(\vert V \vert ^3)$ :

* les circuits absorbant s'il y en a
* tous les chemins de longueur minimum allant de $x$ à $y$ pour tous les sommets $x$ et $y$.

> Si les poids sont positifs, il vaut mieux utiliser Dijkstra pour trouver 1 chemin entre $x$ et $y$ ou tous les chemins de $x$ à tous les autres sommets, mais si l'on cherche  tous les chemins, il vaut mieux utiliser Floyd-Warshall.

### graphe inconnu ou changeant

Un algorithme beaucoup utilisé lorsque le graphe peut changer ou s'il est très grand, voir inconnu (un terrain de jeu) est l'algorithme $A^*$.

Son principe est identique à celui de Dijkstra, mais plutôt que de prendre à chaque fois l'élément de coût minimum, on choisit un élément dont le `cout_entree` + une distance heuristique sur sa distance à l'arrivée est minimum.

Si l'heuristique est valide, l'algorithme va considérer moins de sommets que Dijkstra.

On l'utilise aussi souvent pour avancer directement à cet élément dans les algorithme de pathfinding par exemple.

> Proposez une implémentation de l'algorithme $A^*$ pour le parcours dans une salle d'un petit robot (un étudiant lambda un jeudi matin par exemple).
{: .a-faire}

On peut aussi montrer que si l'algorithme $A^*$ a une heuristique qui ne surestime pas la distance finale, il va bien trouver un chemin de poids minimum.

> Donner un exemple qui montre que si l'algorithme $A^*$ a une heuristique qui surestime le coût du chemin réel il se peut qu'il ne rende pas le bon chemin.
{: .a-faire}

### grand graphes

C'est la technique utilisée par google maps. Pour le graphe de google maps, il est impossible de faire un algorithme de Dijkstra à chaque requête, cela prendrait bien trop de temps !

On ne peut pas non plus mettre les chemins en dur, car il faudrait une base de donnée gigantesque. Comment résoudre ce problème épineux ?

En utilisant des hubs ! On remarque en effet que lorsque l'on fait un plus court chemin entre 2 sommets quelconques sur un graphe de google maps les débuts de chemins sont souvent identiques (on prend les grandes routes) et divergent fortement à la fin (petites routes jusqu'à la destination).

On procède alors à un pré-traitement en calculant pour chaque sommet $x$ tous les chemins les plus courts (on crée l'arborescence de ce sommet). Et pour chaque chemin ainsi crée, on choisit la ville avec le plus d'habitants qui se trouve sur le second tiers du chemin. Toutes ces villes constituent les *hubs* de ce sommet $x$.

> Notez que si l'on va de A à B sur des routes à double sens, le hub pour le chemin allant de A à B est le même que le hub pour le chemin allant de B à A.

Sur une carte de géographie, on remarque qu'il y a très peu de hubs !

Une fois ce pré-traitement effectué, lorsqu'un utilisateur veut aller de A à B :

1. google choisi un hub commun H1 à A et B et crée 2 routes, une allant de A à H1 et l'autre allant de H1 à B
2. on récurse pour les chemins créés en cherchant un hub commun H2 à A et H1 et un hub commun H2' à H1 et B et ainsi de suite jusqu'à arriver à des chemins *"courts"*.
3. jusqu'à arriver à des chemins courts où l'on peut faire un dijkstra entre les deux sommets rapidement.

Le temps de calcul en est très réduit puisque les hubs sont calculés en amont de la requête.

> Montrez avec les 3 (plus belles) villes (de France) que sont Marseille, Strasbourg et Brest comment les choix de hubs peuvent drastiquement influencer le chemin proposé.
{: .a-faire}