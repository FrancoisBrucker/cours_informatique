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

#### Admissibilité

Il faut et il suffit que les stations services soient éloignées de moins de $L$ kilomètres.
#### Algorithme

Il faut aller le plus loin possible à chaque fois : la prochaine station est la station la plus éloignée dont la distance est inférieure à $L$. 

Soit $s_i$ la première station d'une solution optimale qui ne correspond pas avec la station $g_i$ choisie par le glouton . On a :

- $i>1$ puisque la première station est la station de départ
- $s_{i-1} = g_{i-1}$

On en conclut que $s_i < g_i$ et que l'on peut choisir $g_i$ comme $i$ ème choix pour la solution optimale et que, comme justement la solution est optimale, $s_{i+1} > g_i$ sinon on aurait pu s'en passer.

Le raisonnement précédent montre que l'on peut construire une solution optimale qui coïncide avec le glouton : le glouton est optimal.

#### Prix fluctuants

On considère les stations par prix croissants et on leur associe à chacune un recouvrement de taille $L$. 

Dans l'exemple ci-dessous on considère que l'ordre de prix croissant est le nombre, que chaque case fait 1km et que $L=10$ :

```text
1111111111
               2222222222
      3333333333
         4444444444
1     3  4     2        5   : ordre des prix
1     2  3     4        5   : ordre dans le parcours
```

On découpe ensuite les intervalles pour qu'ils partitionnent l'espace en ne conservant que la partie la plus petite.

```
On suppose que les intervalles I[i] sont rangés par prix croissant

pour i allant de 1 à n-1:
    pour j allant de i+1 à n-1:
        I[j] = I[j] privé de I[i]
```

L'intervalle restant est la quantité d'essence mettre dans le réservoir :


```text
1111111111
               2222222222
          33333 
                   
1     3  4     2        5
1     2  3     4        5
```

On voit dans l'exemple que la station 4 est inutile et qu'il faut tout de même mettre de l'essence en passant à la station 3.

La preuve de l'optimalité vient du fait que l'essence mise à la station $i$ permet de faire la distance allant de $d_i$ à $d_i + L$. On a gardé que les kilomètres ne pouvant pas être couvert par une station ayant un prix inférieur.

## Problèmes d'ordonnancements

### Ordonnancement avec pénalité

Tout pareil. On dit que la pénalité est un gain qu'on cherche à maximiser : on réalisera en priorité les tâches avec la plus grande pénalité et donc on minimisera les pénalités des tâches non effectuées.

### Ordonnancement avec départ différé

#### Formalisation du problème

- la tâche $\sigma_1$ a commencé en 0 et a fini en $p_{\sigma_1}$
- la tâche $\sigma_2$ a commencé en $p_{\sigma_1}$ et a fini en $p_{\sigma_1} + p_{\sigma_2}$
- la tâche $\sigma_3$ a commencé en $p_{\sigma_1} + p_{\sigma_2}$ et a fini en $p_{\sigma_1} + p_{\sigma_2} + p_{\sigma_3}$

On a donc la formule suivante pour donner la somme de toutes les débuts de tâches :

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
Pour chaque tâche dans cet ordre:
    réaliser cette tache
```

#### Dates de disponibilité

Le même raisonnement que précédemment montre que l'on peut ordonner les tâches par $d_i + p_i$ croissants.

#### Interruption de tâches

On peut à chaque unité réaliser une unité de temps de la tâche qui se finit au plus tôt parmi les tâches que l'on peut réaliser. Ceci garantit que les tâches sont bien réalisées de la plus rapide à la plus lente.


### Ordonnancement avec retard

#### Premières propriétés

Si l'on réduit l'inactivité de l'ouvrier, les tâches vont commencer plus tôt, donc $s_i$ va diminuer et donc $r_i$ aussi : $R$ ne peut que diminuer.

La remarque précédente nous indique que l'ouvrier doit commencer une nouvelle tâche immédiatement après avoir fini la précédente.

#### Mauvais ordres

Durée croissante : 

- $d_1 = 1$, $f_1 = 11$
- $d_2 = 10$, $f_2 = 10$

Durée décroissante : 

- $d_1 = 10$, $f_1 = 11$
- $d_2 = 1$, $f_2 = 1$

#### Ordre optimal

On a $r_{i+1} = s_{i+1} + d_{i+1} - f_{i+1} = s_{i} + d_{i} + d_{i+1} - f_{i+1}$, donc :

- $r_{i+1} \geq s_{i} + d_{i+1} - f_{i+1}$
- $r_{i+1} \geq s_{i} + d_{i+1} + d_{i} - f_{i}$, si $f_{i}> f_{i+1}$

L'échange des deux tâches n'augmente pas le retard maximal.

Si l'on range les éléments par taille de fin demandée croissante, on est alors minimal car $f_{i}< f_{i+1}$ pour tout $i$ est  équivalent à $f_{i}< f_{j}$ pour tout $i<j$.


## Glouton pas optimal mais pas mal

### Empaquetage

#### Applications

Le transport de marchandises, le déchargement d'un cargo dans des camions, ...

#### Solution optimale

Si l'on a $m$ ensembles, on peut ranger au maximum une somme valant $K\cdot m$ qui doit donc être supérieure à la somme de tous les entiers.

#### Propriétés


On crée un nouvel ensemble que si l'entier courant ne tient pas dans l'ensemble considéré : la somme de ces deux ensembles consécutifs est donc strictement plus grande que $K$.

Dans le cas où $m$ est pair on a alors :

- `somme(E[0]) + somme(E[1]) > K`{.language-}
- `somme(E[2]) + somme(E[3]) > K`{.language-}
- `somme(E[4]) + somme(E[5]) > K`{.language-}
- ...

Et on en déduit, si $m$ est pair, que : `somme(E[0]) + ... + somme(E[m-1]) > K * m / 2`{.language-}. Le calcul est identique si $m$ est impair.

#### Performance garantie

Clair en utilisant les 2 questions précédentes.

De plus ceci montre  que c'est vrai quel que soit l'ordre utilisé

#### Cas le pire

On suppose une alternance d'entiers valant $\frac{K}{2}$ et $1$.

### Équilibrage de charge

#### Quelques propriétés

La première inégalité vient du fait que toute tâche doit être effectuée par une machine : la machine $i$ qui réalisera la tâche de plus longue durée aura un $T_i$ plus grand que cette durée.

La seconde inégalité découle du fait que $\min T_i \leq \frac{1}{m}\sum_i T_i \leq \max_i T_i$, et que $\sum_i T_i = \sum_j t_j$. L'inégalité est ainsi vraie pour toute assignation donc également pour l'assignation optimale.

#### Un algorithme glouton

Il vaut mieux répartir les tâches longues sur plusieurs machines, par exemples pour trois machines la répartition $[(4,), (4,), (1, 1, 1)]$ est préférable à la répartition $[(1, 4), (1, 4), (1,)]$ de 5 tâches de durée 4, 4, 1, 1 et 1.

On rangera donc les tâches par durées décroissantes.

Il est clair que s'il y a moins de $m$ tâches à ranger chaque machine aura au plus 1 tâche : la répartition sera optimale.

#### Propriétés

1. avant l'affectation de la tâche $j$ à la machine, son temps total était le plus faible. S'il y a eu des tâches d'affectées après la tâche $j$ elles l'ont été à d'autres machines qui ont augmenté leur temps total d'exécution, la propriété est donc toujours vrai à la fin de l'algorithme.
2. En sommant l'inégalité précédente pour toutes les machines on obtient : $m\cdot(T_{i^\star} -t_j)\leq \sum_{1\leq k\leq m}T_k$
3. vient directement du fait que $T^\star \geq \frac{1}{m}\sum_{1 \leq j\leq n} t_j$
4. clair puisque $t_j \leq \max t_k \leq T^\star$

##### Performances 

La première partie est évidente et comme les inégalités ne dépendent pas de l'ordre choisit la seconde également.

### Plan de tables

> TBD

