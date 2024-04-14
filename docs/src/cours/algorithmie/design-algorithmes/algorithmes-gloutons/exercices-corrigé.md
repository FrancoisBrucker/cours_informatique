---
layout: layout/post.njk
title: "Exercices gloutons : corrigé"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Glouton optimal

### Recouvrement

<https://algo.gricad-pages.univ-grenoble-alpes.fr/L3I-S5-algo/TD1-10-corrige.pdf>
> recouvrement de points par des intervalles exo 3

On classe les réels par ordre croissants puis pour chaque réel $x_i$, s'il n'est pas couvert par un intervalle on ajoute l'intervalle $[x_i, x_i + 1]$.

#### Initialisation de la récurrence

Il existe bien une solution optimale avec $[x_1, x_1 +1]$ comme plus petit intervalle :
    - $x_1$ est couvert et soit l'intervalle le plus à gauche aui le couvre. Il n'y a aucun réel à gauche de $x_1$ donc aucun intervalle nécessaire à gauche de cet intervalle
    - si l'intervalle min ne commence pas en $x_1$ on le remplace par $[x_1, x_1 +1]$ et la solution continue d'être optimale 

#### Récurrence

Soit $[x_i, x_i +1]$ le plus petit intervalle qui n'est pas dans la solution optimale.

Comme $x_i$ doit être couvert, il existe un intervalle qui le couvre. Comme tout $x_j$, avec $j < i$ est couvert (les deux solutions coincident), on peut remplacer l'intervalle le plus à gauche couvrant $x_i$ dans la solution optimale par $[x_i, x_i +1]$ et la solution reste optimale.

### réservation SNCF

#### solution possible ?

Une solution en $\mathcal{O}(n+K)$ : 

```python
d = [0] * K

for i in range(n):
    d[t[i]] += 1

for t in range(K):
    if d[t] > P:
        print("le train", t, "contient", d[t] - P, "passagers de trop.")
```

#### solution approchée

```python
for i in range(n):
    while d[t[i]] > P:
        d[t[i]] -= 1
        t[i] += 1
```

A la fin de l'itération, les passagers surnuméraires ont été déplacés dans le premier train disponible.

Cette solution est optimale pour la fonction $\sum_{i\geq 1}(t'[i] - t[i])$ où $t'[i]$ est le train effectivement pris par le passager $i$.

### Une quête d'essence

> TBD
> la seconde partie ressemble au recouvrement.

## Problèmes d'ordonnancements

### Ordonnancement avec pénalité

Tout pareil. On dit que la pénalité est un gain cu'on cherche à maximiser : on réalisera en priorité les tâches avec la plus grande pénalité et donc on minimisera les pénalités des tâches non effectuées.

### Ordonnancement avec départ différé

#### Formalisation du problème

- la tâche $\sigma_1$ a commencé en 0 et a finie en $p_{\sigma_1}$
- la tâche $\sigma_2$ a commencé en $p_{\sigma_1}$ et a finie en $p_{\sigma_1} + p_{\sigma_2}$
- la tâche $\sigma_3$ a commencé en $p_{\sigma_1} + p_{\sigma_2}$ et a finie en $p_{\sigma_1} + p_{\sigma_2} + p_{\sigma_3}$

On a donc la formule suivante pour donner la somme de toutes les fins de tâches :

<div>
$$
   T = \sum_{1\leq i \leq n}( \sum_{1\leq j < i}p_{\sigma_j}) = \sum_i(n-i)p_{\sigma_i}
$$
</div>

Pour 3 tâches, il y a 6 ordonnancements possibles qui donnent respectivement :

- 1 puis 3 puis 5 : $T = 2 \cdot 1 + 2 \cdot 3 = 5$
- 1 puis 5 puis 3 : $T = 2 \cdot 1 + 2 \cdot 5 = 12$
- 3 puis 1 puis 5 : $T = 2 \cdot 3 + 2 \cdot 1 = 8$
- 3 puis 5 puis 1 : $T = 2 \cdot 3 + 2 \cdot 5 = 16$
- 5 puis 1 puis 3 : $T = 2 \cdot 5 + 2 \cdot 1 = 12$
- 5 puis 3 puis 1 : $T = 2 \cdot 5 + 2 \cdot 3 = 16$

#### Algorithme

Minimiser la valeur moyenne des débuts de réalisation minimise $T/n$. Il suffit donc de minimiser $T$.

L'ordre selon lequel il faut ordonner les tâches est par début décroissant. S'il existait en effet $i < j$ tel que $p_{\sigma_i} > p_{\sigma_j}$ changer les deux tâches diminuerait strictement $T$ puisque $n-i > n-j$. Cet ordre donne directement l'algorithme glouton :

```text
On trie les tâches par temps croissant
pour chache tache dans cet ordre:
    réalise cette tache
```

#### Dates de disponibilité

Le même raisonnement que précédemment montre que l'on peut ordonner les les tâches par $d_i + p_i$ croissants.


#### Interruption de tâches

On peut à chaque unité réaliser une unité de temps de la tâche qui se finie au plus tôt parmi les tâches que l'on peut réaliser. Ceci garanti que les tâches sont bien réalisées par de la plus rapide à la plus lente.



### Ordonnancement avec retard
 > TBD
