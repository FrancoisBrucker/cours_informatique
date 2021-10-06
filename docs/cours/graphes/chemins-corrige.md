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

[les exercices]({% link cours/graphes/chemins.md %})

## Dijkstra

La seule différence entre l'algorithme de Prim et et l'algorithme de Dijkstra est l'évaluation du coût d'entrée :

* dans l'algorithme de Prim il est égal à la valuation de l'arête rx
* dans l'algorithme de Diskstra il vaut l'addition de cout_entree(r) plus la valuation de l'arête rx.

Cette différence s'explique parce que le poids d'un arbre est la somme des valuations des arêtes qui le constitue alors que pour un chemin, avant d'aller en x, il faut déjà aller en r (dont le coût est cout_entree(x) ) puis de r à x (dont le coût est f(rx)).

### test

Les différentes étapes de l'algorithme sont représentées dans les graphes ci-dessous.

* La figure se lit de gauche à droite et de haut en bas.
* $V'$ est en vert
* en magenta $r$ et les modification des prédécesseur et du cout d'entrée s'il y en a
* en orange le prédécesseur et le cout d'entrée.

![Dijkstra Paris à Rana]({{ "/assets/cours/graphes/chemin_dijkstra_paris_rana.png" | relative_url }}){:style="margin: auto;display: block;"}

### preuve

On montre par récurrence que le chemin de x à r en remontant les prédécesseurs de r jusqu'à arriver à d est de longueur minimale et de coût cout_entree(r).

Au départ `r = d`, la propriété est donc vraie. On la suppose vrai jusqu'à l'étape $i$. A l'étape $i+1$, on a choisi `r` qui minimise le coût d'entrée parmi tous les éléments de `V` qui ne sont pas encore dans `V'`. Comme tous les chemins alternatifs entre `d` et `r` commencent en `d`, il existe une arête de ce chemin dont le départ  (disons $u$) est dans `V'` et l'arrivée (disons $v$) n'y est pas. Prenons la première arête $uv$ pour laquelle ça arrive.

Par hypothèse de récurrence, `cout_entree(u)` est le cout minimum d'un chemin entre `d` et $u$ et `cout_entree(v)` est donc plus grand que `cout_entree(u) + f(uv)` (on a examiné ce cas lorsque l'on a fait rentrer $u$ dans `V'`) et de `cout_entree(r)` (car c'est le min).

De là, le coût du chemin alternatif est plus grand également que `cout_entree(r)` **car toutes les valuations sont positives** : notre hypothèse est vérifiée.

### complexité

On ajoute à chaque étape un élément, donc il y a au pire $\vert V \vert$ étapes. A chaque choix on compare les voisins de `r`. Ces comparaisons sont donc de l'ordre de $\mathcal{O}(\delta(r))$ opérations. Comme `r` est différent à chaque étapes, toutes ces comparaisons sont de l'ordre de $\mathcal{O}(\sum\delta(r)) = \mathcal{O}(\vert E \vert)$ opérations.

On prend ensuite le minimum parmi les éléments de `V'`, ce qui prend $\mathcal{O}(\vert V \vert)$ opérations.

La complexité totale est alors en $\mathcal{O}(\vert E\vert + (\vert V \vert)^2)$.

On voit qu'elle dépend entièrement de la prise du minimum de `cout_entree`. En optimisant cette opération, on peut drastiquement diminuer la complexité de l'algorithme

Si l'on utilise un tas pour prendre le min, on doit au pire mettre à jour le tas pour chaque arête. Comme il va y a voir au maximum `V` éléments dans ce tas, la complexité de mise à jour est de $\mathcal{O}(\log_2(\vert V \vert))$, donc le coût total des mises à jour sera de $\mathcal{O}(\vert E \vert \log_2(\vert V \vert))$.

Enfin, comme on prend $\vert V \vert$ fois le minimum du tas, la complexité de trouver tous les `r` est de $\mathcal{O}(\vert V \vert \log_2(\vert V \vert))$. La complexité de Dijkstra avec un tas est donc de : $\mathcal{O}((\vert E \vert + \vert V \vert)\log_2(\vert V \vert))$.

Ceci est mieux de prendre le minimum si le graphe ne contient pas énormément d'arêtes : $(\vert E \vert + \vert V \vert) \log_2(\vert V \vert) \leq \vert E\vert + (\vert V \vert)^2$, ce qui donne asymptotiquement $\vert E \vert \leq \frac{\vert V \vert^2}{\log_2(\vert V \vert)}$.

La [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra#Complexit%C3%A9_de_l'algorithme) précise qu'en utilisant un tas amélioré, dit tas de fibonnaci, on arrive même à faire descendre la complexité à $\mathcal{O}(\vert E \vert + \vert V \vert\log_2(\vert V \vert))$, ce qui est toujours mieux que la prise de minimum naïve.

## arborescence

A chaque fois que l'on ajoute un élément dans `V'` on vérifie tous ses voisins pour mettre à jour le coût d'entrée dans la structure. On procède comme le parcours en largeur et on a montré qu'il trouvait la composante connexe de sa racine.

### preuve {#preuve-dijkstra-arborescence}

Cette preuve dérive directement de la preuve de l'algorithme de Dijkstra que l'on a fait précédemment.

### Prim vs Dijkstra

Le graphe suivant montre que l'arborescence de Disjkstra sera différente de l'arbre de poids minimum donné par Prim.

![Prim vs Dijkstra]({{ "/assets/cours/graphes/chemin_prim_vs_dijkstra.png" | relative_url }}){:style="margin: auto;display: block;"}

> Ne confondez pas les 2 problèmes !
{: .attention}

## chemin le plus long

### algorithme ?

Même si l'on met à jour en cherchant à prendre le plus grand coût d'entrée à chaque fois, l'algorithme ne fonctionne pas. Prenez par exemple le graphe suivant :

![Dijkstra pas hamilton]({{ "/assets/cours/graphes/chemin_pas_hamilton.png" | relative_url }}){:style="margin: auto;display: block;"}

Le chemin de longueur maximum $132$ ne sera jamais trouvé si les sommets sont rentré dans l'ordre 1, 2, 3.

### chemin hamiltonien

Le plus long chemin élémentaire possible dans un graphe passe par tous les sommets. Donc un chemin élémentaire de longueur $\vert V \vert -1$ est hamiltonien.

### graphes particuliers

#### graphe sans circuit

1 :

Soit $c_0\dots c_k$ un cycle ($c_k = c_0$), quelque soit l'ordre total entre les sommets du graphe, il existe $i$ tel que $c_{i+1} < c_i$ ce qui est impossible si un tel ordre était topologique.

2 :

Supposons que tout sommet d'un DAG admette un voisin entrant et un voisin sortant, et prenons une arête $x_0x_1$ de ce graphe. Il existe donc une arête $x_1x_2$. Si $x_2 = x_0$ il existe un cycle dans le graphe, sinon il existe un chemin $x_0x_1x_2$. Il existe donc une arête $x_2x_3$. Si $x_3 \in \{x_0, x_1 \}$ il existe un cycle et sinon on a un chemin $x_0x_1x_2x_3$. On peut ainsi recommencer jusqu'à tomber sur un cycle par finitude du graphe. Ce n'est pas un DAG.

Le raisonnement est identique pour les voisins entrant.

3 :

en supprimant itérativement les sommets sans voisins rentrant d'un DAG (le graphe obtenu en supprimant un sommet d'un DAG est toujours un DAG puisque supprimer un sommet ne rajoute pas de cycle), on obtient un tri topologique.

> On peut aussi le faire de façon optimale en utilisant un [parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

4 :

On a montré que :

* cycle implique non tri topologique
* DAG (non cycle) implique tri topologique

On a donc bien l'équivalence : tri topologique est équivalent à DAG.

algorithme sur tri topologique :

```text
Entrée :
    * un graphe orienté G = (V, E)
    * un tri V0 < ... < Vn des éléments de V
Initialisation :
    * longueur(x) = 0 pour tout sommet x
    * predecesseur(x) = x pour tout sommet x
    * V' = {}, E' = {}
Algorithme :
    * pour v allant de V0 à Vn:
        * pour chaque voisin sortant w de v:
            * si longueur(w) < longueur(v) + 1:
                * longueur(w) = longueur(v) + 1
                * predecesseur(w) = v
    * soit a l'élément de V ayant la plus grande longueur
    * chemin = [a]
    * x = a
    * tant que x est différent de predecesseur(x):
        * x = predecesseur(x)
        * ajoute x au début de chemin        
Retour :
    chemin
```

La complexité est de $\mathcal{O}(\vert E \vert + \vert V \vert)$, ce qui est optimal.

Pour prouver l'algorithme, on montre par récurrence sur $\vert V \vert$ que `longueur(x)` est la longueur d'un plus long chemin finissant en `x`.

Si $\vert V \vert = 1$, c'est Ok. On suppose la propriété vraie à $\vert V \vert = n$. Pour $\vert V \vert = n +1$ on remarque que `longueur(Vi)` est la même pour le graphe $G$ et pour le graphe $G$ auquel on a enlevé $v_{n+1}$ pour tout $i \neq n+1$. Comme tous les prédécesseurs de $v_{n+1}$ seront vus pour l'algorithme et que `longueur(Vi)` ne change pas après l'étape $i$ on en conclut que la récurrence est vraie à $\vert V \vert = n +1$.

#### tournoi

##### cycles

Si le tournoi n'est pas transitif il existe $x$, $y$ et $z$  tels que $xy$ et $yz$ mais pas $xz$ : $xyzx$ est un cycle.

Réciproquement, s'il existe un cycle, prenons en un de longueur minimum : $c_0c_1c_2 \dots c_k$. Comme le cycle est de longueur minimum, $c_0c_2$ n'est pas une arête : le tournoi n'est pas transitif.

##### chemin hamiltonien

Par récurrence, un tournoi à 1 sommet admet un chemin hamiltonien. Si on suppose cela vrai pour tout tournoi à moins de $n$ sommets, soit $T = (V, E)$ un tournoi à $n+1$ sommets.

On prend $x$ un sommet de ce tournoi. On a alors que $N^+(x) \cup N^-(x) \cup \{ x \} = V$ et que la restriction de $T$ à $N^+(x)$ ou à $N^-(x)$ restent des tournois et ont strictement moins de $n+1$ sommets.

Il existe alors :

* un chemin hamiltonien $c_0\dots c_k$ dans la restriction de $T$ à $N^+(x)$
* un chemin hamiltonien $c'_0\dots c'_l$ dans la restriction de $T$ à $N^-(x)$

On en conclut que le chemin $c'_0 \dots c'_l x c_0 \dots c_k$ est hamiltonien dans $T$, ce qui termine la preuve par récurrence.

### ordonnancement

Il est clair que s'il y a un cycle on ne peut réaliser le projet. De plus un tri topologique fait que lorsque l'on s'attelle à la tache $v_i$ on a déjà fait tous ses prédécesseurs (ses prés-requis).

## variantes

### poids négatifs

![chemin poids négatif]({{ "/assets/cours/graphes/chemin_poids_negatif.png" | relative_url }}){:style="margin: auto;display: block;"}

Il suffit de pouvoir aller de $d$ au circuit absorbant puis du circuit à $a$ pour que la longueur minimale d'un chemin allant de $d$ à $a$ soit $-\infty$ (on repasse beaucoup de fois par le circuit absorbant qui va diminuer à chaque fois la longueur du chemin).

![circuit absorbant]({{ "/assets/cours/graphes/chemin_absorbant.png" | relative_url }}){:style="margin: auto;display: block;"}

### graphe inconnu ou changeant

#### exemple sur la grille

* On peut prendre comme graphe la grille 2D carré de pas 1m par exemple
* s'il y a des murs on ne mets pas d'arêtes
* l'euristique sera la distance L1 entre la position et l'arrivée.

On peut même se déplacer à chaque itération et se rapprocher normalement du but petit à petit.

#### attention à l'heuristique utilisée

Pour montrer qu'il peut se tromper, on donne une estimation de coût 0 à un chemin qui n'est pas de longueur minimale et $+\infty$ à sous les autres.

### grand graphes

* Marseille a Dijon et Paris dans ses hub. Le premier pour aller de Marseille à Strabourg et le second pour aller de Marseille à Brest
* Strasbourg à également Dijon et Paris dans ses hubs le premier pour aller à Marseille (c'est symétrique) et le second pour aller à Brest.

![chemin hubs]({{ "/assets/cours/graphes/chemin_hubs.png" | relative_url }}){:style="margin: auto;display: block;"}

Google maps peut alors vous proposer deux grands chemins pour aller de Marseille à Strasbourg, soit en passant par Dijon soit par Paris (bon il ne le fait pas car un chemin est bien plus long que l'autre, mais c'est l'idée).

Les hubs, en plus d'être efficaces en temps de calculs sont aussi une chouette solution pour proposer des itinéraires différents pour aller entre 2 villes.
