---
layout: layout/post.njk
title: "Exercices gloutons : corrigé"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## réservation SNCF

On suppose que $n$ personnes veulent voyager en train un
jour donné. La personne $i$ veut prendre le train train[i].

Il y a $k$ trains qui partent dans la journée, le train $j$ partant avant le train $j+1$, chaque train ne pouvant contenir plus de $K$ passagers.

### solution possible ?

Proposez un algorithme qui vérifie que pour un nombre de train donné et une liste de trains choisi, il est possible de faire voyager tout le monde.

### solution approchée

On suppose maintenant que la personne $i$, si elle ne peut
pas prendre le train train[i] parce qu’il est complet, accepte
de prendre un des trains suivants (s’il y en a un).

Proposez un algorithme minimisant l'attente globale pour faire voyager tous les voyageurs.

## Le plein de sens

## 2. Algorithme glouton

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ de la station $i$ est rangée dans la liste `d` (la station $i$ est à `d[i]` kilomètres du départ). Le but est d'atteindre la dernière station de la route.

### écart

Ecrivez un algorithme qui, à partir de la liste `d` des stations rend une liste `delta` où :

- `delta[0]` est la distance du départ de la station $0$,
- `delta[i]` pour $i > 0$ est la distance de la station $i-1$ à la station $i$.

```python
def ecart(d):
    delta = [d[0]]

    for i in range(1, len(d)):
        delta.append(d[i] - d[i - 1])

    return delta
```

#### complexité

Une boucle en $\mathcal{O}(len(d))$, les autres lignes sont en $\mathcal{O}(1)$ puisqu'elles consistent à trouver un élément d'indice donné dans une liste, faire des opérations arithmétiques et à ajouter des éléments à la fin d'une liste.

La complexité totale de l'algorithme est donc de : $\mathcal{O}(len(d))$

#### preuve

A la fin de l'étape $i$ de la boucle, on prouve que `delta[j]` vaut la distance entre les stations d'indice $j$ et $j-1$ quelque soit $0<j \leq i$.

- _initialisation_. A la fin de la première itération, on a bien $delta[1] = d[1] -d[0]$, et $delta$ est une liste à 2 éléments.
- _récurrence_. On suppose la propriété vraie pour $i$. Pour $i + 1$, on a bien ajouté un élément à `delta`, il y a donc $i + 2$ éléments (par hypothèse de récurrence, il y en a $i + 1$ à la fin de l'étape $i$) et le dernier élément est bien $d[i+1] - d[i]$.

### Reservoir plein

Un automobiliste prend le départ de la route avec une voiture dont le réservoir d’essence est plein. Sa voiture
est capable de parcourir une distance r (mais pas plus !) avec un plein.

On cherche une liste `s` d'indices croissante de station telle que si l'on fait le plein à chacune de ces stations on peut parcourir toute la route.

#### Admissibilité

Il faut et il suffit que $delta[i] \leq r$ quelque soit $i$ :

- si $delta[i] \leq r$ quelque soit i, on peut faire le plein à chaque station et on arrive au bout de la route
- s'il existe $j$ tel que $delta[j] > r$, on ne pourra jamais atteindre la station j à partir de la station j-1.

##### Algorithme 1

Algorithme qui vérifie, à partir d'une liste `d` de stations et d'un nombre maximum de kilomètres `r` possible que le problème admet une solution.

exemple : Pour une liste `d` de stations valant : `d = [2, 5, 6, 10, 12, 13]`, il devra répondre `True` pour un `r = 4` et `False` pour `r = 3`.

```python
def admissible(d, r):
    delta = ecart(d)
    for x in delta:
        if x > r:
            return False
    return True
```

L'algorithme vérifie clairement que la condition nécessaire et suffisante précédente est vérifieé. Sa complexité est gale à la création de la liste `delta`, en $\mathcal{O}(len(d))$, plus une boucle qui parcourt la liste `delta`, donc également en $\mathcal{O}(len(d))$. Au final, la complexité est en $\mathcal{O}(len(d))$.

##### Algorithme 2

Algorithme qui vérifie, à partir d'une liste `s` d'indices de stations (que l'on supposera croissante) où faire le plein, d'une liste `d` de stations et d'un nombre maximum de kilomètres par plein `r`, si `s` est une solution (ou pas) du problème

exemple : Pour une liste `d` de stations valant : `d = [2, 5, 6, 10, 12, 13]`, un réservoir de `r = 4` et une liste `s = [0, 2, 3, 4]` il devra répondre `True` et pour une liste `d` et un réservoir identique, il devra répondre `False` pour `s = [0, 1, 3, 4]`.

```python
def est_solution(d, r, s):
    d2 = []
    for i in s:
        d2.append(d[i])

    d2.append(d[-1])

    return admissible(d2, r)
```

La complexité est en $\mathcal{O}(len(s))$ : il y a une boucle en $\mathcal{O}(len(s))$, l'utilisation de l'algorithme `admissible` qui est également en $\mathcal{O}(len(s))$ et le reste des lignes est en $\mathcal{O}(1)$.

Le problème revient à vérifier sur un sous ensemble de `d` (les station de `s` plus la dernière station de `d` à ne pas oublier) si la solution est admissible.

#### algorithme

Écrivez un algorithme qui, à partir d'un liste `d` de stations et d'un nombre maximum de kilomètres `r` possibles rend une liste `s` de stations où faire le plein de longueur minimale.

```python
def soution_minimale(d, r):
    if not admissible(d, r):
        return []

    station_precedente = 0
    s = []

    for i in range(1, len(d)):
        if d[i] - station_precedente > r:
            s.append(i - 1)
            station_precedente = d[i - 1]
    return s
```

L'algorithme commence par vérifier s'il existe une solution admissible ($\mathcal{O}(len(d))$) puis dans une boucle (répétée $\mathcal{O}(len(d))$ fois) on compare des valeurs et on ajoute des éléments à la fin d'une liste qui sont des opérations en $\mathcal{O}(1)$. La complexité de cet algorithme est donc en $\mathcal{O}(len(d))$.

On peut montrer facilement par récurrence sur $i$ que le `s` rendu par l'algorithme possède les trois propriétés suivantes :

- `s[0]` est le plus grand indice $j$ de $d$ tel que $d[j] \leq r$
- les éléments de `s` sont rangés par ordre strictement croissant
- pour tout indice `j > 0` on a $d[s[j]] - d[s[j-1]] \leq r$ et $d[s[j] + 1] - d[s[j-1]] > r$. Donc pour tout indice $k > s[j]$ on a $d[k] - d[s[j-1]] > r$.

On montre maintenant que la solution donnée par l'algorithme est minimale en nombre de stations. Soit `s'` une solution minimale en nombre de station et qui coïncide avec `s` le plus longtemps possible. On suppose que `s` n'est pas minimale, il existe donc `j`, le premier indice tel que $s[j] \neq s'[j]$.

Tout d'abord on a $s[j] > s'[j]$, car :

- si j = 0 $s[0]$ est l'indice $i$ le plus grand tel que $d[i] <= r$ et donc on aurait $d[s'[0]] > r$ ce qui est impossible
- si j > 0 : $d[s[j]] - d[s[j-1]] \leq r$ et $d[k] - d[s[j-1]] > r$ pour $k > s[j]$ et donc on aurait $d[s'[j]] - d[s'[j-1]] > r$ ce qui est impossible.

On note alors `j'` le premier indice de `s'` tel que $s'[j'] > s[j]$ on a alors que la liste `s'' = s'[:j] + [s[j]] + s'[j':]` est une solution au problème car $r \geq d[s'[j']] - d[s[j' - 1]] \geq d[s'[j']] - d[s[j]]$ puisque $s[j' - 1] \leq s[j]$.

Ceci est impossible car `s''` a au plus un nombre de station égal à `s'` et elle coïncide plus longtemps avec `s` que `s'`. Notre hypothèse était fausse, la solution `s` est optimale.

### Reservoir vide

On suppose que chaque litre d'essence permet de parcourir 1km. On essaye de minimiser le coût d'achat d'essence

#### Nombre de stations minimale

Comme le prix de l'essence est constant, la station où l'on fait le plein n'est pas importante. De plus, le nombre minimum d'essence que l'on peut mettre correspond à la distance de la route.

De là si on a une solution optimale, il suffit de mettre assez d'essence pour atteindre la station suivante : on aura mis juste assez d'essence pour parcourir toute la route.

#### Algorithme

Il suffit d'utiliser l'algorithme solution optimale et de mettre juste assez d'essence pour atteindre la station suivante :

```python
def soution_minimale_essence(d, r):
    s = solution_minimale(d, r)

    s2 = []

    for i in range(len(s) - 1):
        s2.append((s[i], d[s[i] + 1] - d[s[i]]))
    s2.append(s[-1], d[-1] - d[s[-1]])

    return s2
```
