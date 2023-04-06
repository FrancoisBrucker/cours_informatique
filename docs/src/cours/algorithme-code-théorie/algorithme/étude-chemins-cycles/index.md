---
layout: layout/post.njk 
title: "étude : chemins et cycles"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../algorithmes-gloutons/"
---

<!-- début résumé -->

Utilisation d'algorithmes gloutons pour résoudre des problèmes de cheminement.

<!-- end résumé -->

{% info %}
Les différents algorithmes que nous allons voir sont pour la plupart des cas particuliers d'algorithmes plus généraux de la théorie des graphes.

Les algorithmes présentés sont de plus pas forcément les meilleurs en terme de complexité.
{% endinfo %}

Le problème que nous voulons résoudre est :

{% note "**Problème**" %}
étant donné un ensemble de villes $V$ décrites par leurs coordonnées GPS et un prix de construction de route proportionnelle au kilomètre comment relier les villes entres-elles au prix le plus bas ?
{% endnote %}

Par exemple les 5 villes ci-dessous :

![5 villes](./5-villes-discret.png)

Aucune route n'a été construite et on ne peut voyager de ville en ville.

Dans la figure ci-dessous un réseau routier a été construit. À gauche toutes les routes possibles ont été construites, ce qui est pratique si ont veut voyager vite entre deux villes mais c'est beaucoup trop cher (et dangereux, regardez le nombre de croisements !). À droite seul le nombre minimum de routes entre villes voisines pour pouvoir aller de n'importe quelle ville à n'importe quelle autre ville en suivant le réseau routier ont été construite.

![5 villes arbres](5-villes-complet-arbre.png)

{% exercice %}
Pourquoi est-on sur que la figure de droite possède le nombre minimum de routes ?
{% endexercice %}
{% details "corrigé" %}
Si on supprime une route (n'importe laquelle) dans la figure de droite, on déconnecte le réseau en deux.

Alors que dans la figure de gauche on peu au minimum supprimer 4 routes (tous les routes partant d'une ville) et au mieux 6 (pour arriver à la figure de droite).
{% enddetails %}

## Nuages de points

Nous allons dans les exemples qui suivent utiliser le même jeu de données. Nous avons généré en python 100 points en deux dimensions dont les abscisses et ordonnées sont entre 0 et 1.

![100 villes](100_points.png)
{% details "code python" %}
Code python pour générer les 100 villes que l'on stocke dans un [dictionnaire](../structure-dictionnaire) :

```python
import random

villes = dict()

for nom in range(100):
    villes[str(nom)] = (random.random(), random.random())

return villes
```

Puis que l'on affiche avec matplotlib :

```python
import matplotlib.pyplot as plt

TAILLE = 10

x = []
y = []
label = []
for nom, (long, lat) in villes.items():
    x.append(long)
    y.append(lat)

    label.append(nom)

height = max(y) - min(y)
width = max(x) - min(x)

fig, ax = plt.subplots(figsize=(TAILLE, TAILLE * height / width))
ax.set_title("Les villes")

ax.scatter(x, y)
for i in range(len(x)):
    ax.text(x[i], y[i], label[i])

for x, y in segments:
    ax.plot(
        [villes[x][0], villes[y][0]],
        [villes[x][1], villes[y][1]],
        color=mcolors.CSS4_COLORS["brown"],
    )
plt.show()
```

{% enddetails %}

Pour ce qui va suivre, une hypothèse souvent utilisée est :

{% note %}
L'ensemble des points est en [position générale](https://fr.wikipedia.org/wiki/Position_g%C3%A9n%C3%A9rale), c'est à dire que **3 points ne sont jamais alignés**.
{% endnote %}

Ce n'est pas une contrainte forte puisque la probabilité que ça arrive est nulle (si on tire au hasard des coordonnées réelles aux points), et – même si ça arrivait – il suffirait de déplacer un des trois points d'epsilon pour que ça n'arrive plus.

La raison fondamentale de cette hypothèse est que :

{% note %}
Si $P$ est un ensemble de points en ***position générale***, alors pour tout couple $x, y \in P$ aucun autre point de $P$ n'est sur le segment entre $x$ et $y$.
{% endnote %}

Ceci va simplifier nombre de preuves de ce qui va suivre.

## Routes et Connexité

Nous devons créer un réseau routier entre les villes pour les relier. Nous avons seulement besoin de créer des segments entre villes, ce qui minimisera le nombre de kilomètres de routes.

Analysons un peu ce que nous pouvons faire.

### Routes

{% note "**définition**" %}

Une ***route*** est le segment entre $x$ et $y$. Les routes se combinent en chemins. Un ***chemin*** entre deux villes $x$ et $y$ est soit :

* la ***route*** (le ***segment***) entre $x$ et $y$
* soit une suite $v_1\dots v_{i-1}v_i\dots v_n$ tel que :
  * $v_1 = x$, $v_n = y$
  * les villes $v_{i-1}$ et $v_{i}$ sont différentes et reliées par une route pour tout $1 < i \leq n$
  * pour un chemin $v_1\dots v_{i-1}v_i\dots v_n$ entre $v_1$ et $v_n$ les villes $v_2$ à $v_{n-1}$ sont dites ***villes de passage***
{% endnote %}

La notion de chemin s'écrit très bien sous la forme d'une relation $C$ sur un ensemble $V$ de villes. On dira que $xCy$ s'il existe un chemin entre $x$ et $y$. Cette relation est une [relation d'équivalence](https://fr.wikipedia.org/wiki/Relation_d%27%C3%A9quivalence) car elle est :

* réflexive $xCx$ (le singleton $x$ permet de relier $x$ à lui-même)
* symétrique $xCy$ implique $yRx$ (les chemins sont à double sens)
* transitive $xCy$ et $yCz$ implique $xCz$ (on colle la suite allant de $x$ à $y$ à la suite allant de $y$ à $z$)

L'intérêt de cette formalisation est qu'elle montre que la relation des chemins $R$ se crée :

1. en considérant la relation $R$ des routes du réseau routier ($xRy$ s'il existe une route entre $x$ et $y$ dans le réseau)
2. en fermant cette relation par transitivité

À première vue créer $C$ à partir de $R$ semble compliqué, mais l'exercice ci-après (qui explicite l'algorithme de [Algorithme de Roy](https://fr.wikipedia.org/wiki/Algorithme_de_Warshall)) montre qu'on peut le faire très simplement en utilisant le principe de la [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique).

{% exercice %}
Soit $V = \\{ v_1, \dots v_n \\}$ les villes d'un réseau routier et $R$ sa relation route associée.

Montrez que si on note $V_i \\{ v_1, \dots v_i \\}$ les chemins ayant comme villes de passage uniquement des éléments de $V_{i}$ peuvent de déduire des chemins routes ayant uniquement des villes de $V_{i-1}$ comme villes de passage.
{% endexercice %}
{% details "corrigé" %}
Il existe un chemin entre $x$ et $y$ ayant comme villes de passage uniquement des éléments de $V_{i}$ si :

* soit il existe un chemin entre $x$ et $y$ ayant comme villes de passage uniquement des éléments de $V_{i-1}$
* soit il existe les deux chemins suivants :
  * un chemin entre $x$ et $v_i$  ayant comme villes de passage uniquement des éléments de $V_{i-1}$
  * un chemin entre $v_i$ et $y$  ayant comme villes de passage uniquement des éléments de $V_{i-1}$

{% enddetails %}

{% exercice %}
Déduire de l'exercice précédent un algorithme en $\mathcal{O}(n^3)$ permettant de trouver la relation chemin à partir de la relation route.
{% endexercice %}
{% details "corrigé" %}

On utilise la représentation matricielle des relations. On dira que $R[i][j]$ (*resp.* $C[i][j]$) est vrai s'il existe une route (*resp.* un chemin) entre $v_i$ et $v_j$ dans le réseau et que $R[i][j]$ (*resp.* $C[i][j]$) est faux sinon.

L'équation précédente s'écrit alors :

$C_k[i][j]$ est vrai si l'une ou l'autre des assertions suivant est vrai :

* $C_{k-1}[i][j]$ est vrai
* $C_{k-1}[i][k]$ et $C_{k-1}[k][j]$ sont vrais

Qui se résume en :

$$
C_k[i][j] = C_{k-1}[i][j] \text{ ou } (C_{k-1}[i][k] \text{ et } C_{k-1}[k][j])$$

Ce que l'on peut écrire en ré-écrivant sur la même relation :

```python
for i in range(n):
    for j in range(n):
        C[i][j] = R[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            C[i][j] = C[i][j] or (C[i][k] and C[k][j])
```

{% enddetails %}

### Connexité

Le but final est d'obtenir un réseau routier où l'on puisse librement aller d'une ville à l'autre. Formalisons ceci en commençant par étudier des réseau routiers déjà constitués

{% note %}
Un réseau routier de villes est ***connexe*** si quelque soient deux villes $x$ et $y$, il existe un chemin entre $x$ et $y$.

{% endnote %}

Le fait que la notion de chemin (la relation $C$ de la partie précédente) soient une relation d'équivalence montre que le réseau routier est connexe si et seulement si cette relation n'admet qu'une seule classe d'équivalence ($C(x) = C(y)$ quelques soient les villes $x$ et $y$).

{% note "**définition**" %}
Si $C$ est une relation d'équivalence sur $V$, la ***classe d'équivalence*** de $x \in V$ est :

$$
C(x) = \\{ y | xCy, y \in V \\}
$$

{% endnote %}

Si un réseau routier n'est pas connexe, les classes d'équivalences de la relation chemin donnent les ***composantes connexes*** du réseau routier. Le réseau routier de la figure suivante contient 2 composantes connexes :

![2 composantes connexes](./2-composantes-connexes.png)

Notez que :

{% note %}
Si $V_1$ et $V_2$ sont deux composantes connexes d'un réseau routier alors :

* $V_1 \cap V_2 = \emptyset$
* si on ajoute **une** route entre une ville de $V_1$ et une ville de $V_2$, alors $V_1 \cup V_2$ devient une composantes connexe du nouveau réseau

{% endnote %}

Par exemple, en ajoutant la route entre B et P, on obtient un réseau routier connexe :

![1 partie connexe](./1-composantes-connexes.png)

La propriété ci-dessus nous permet de créer un algorithme glouton permettant de trouver toutes les parties connexes d'un réseau routier uniquement à partir de sa relation route.

Algorithme composante connexe :

```text#
pour chaque ville v : R(v) = v
pour chaque route (x, y):
    si R(x) ≠ R(y):
        pour chaque ville z telle que R(z) = R(y):
            R(z) = R(x)
```

{% attention %}
Lorsque l'on code l'algorithme il arrive souvent que l'on écrive changement de marques :

```text
pour chaque ville u:
    si R(u) == R(x) alors:
        R(u) = R(y)
```

Qui est faux.
{% endattention %}
{% exercice %}
Pourquoi est-ce faux ?
{% endexercice %}
{% details "solution" %}
Si u vaut x, on change sa marque et plus aucun changements ne sera effectué pour les villes suivantes.

Il faut stocker la valeur test :

```text
à_changer = R(x)
pour chaque ville u:
    si R(u) == à_changer alors:
        R(u) = R(y)
```

{% enddetails %}

Cet algorithme fonctionne grâce à la marque R qui défini le représentant de chaque ville. Montrons ça sur un exemple en reprenant le réseau ci-après et en affectant une couleur à chaque ville comme représentant :

![2 composantes connexes](./algo-connexe-début.png)

Et en étudiant les routes dans l'ordre $(L, S)$, $(B, M)$, $(P, S)$ et enfin $(L, P)$ on obtient :

![Algorithmes composantes connexes](./algo-connexe.png)

Notez que l'étude de la route $(L, P)$ ne produit aucun changement dans les représentants car la couleur de $L$ est déjà égale à la couleur de $P$.

{% note %}
A la fin de l'algorithme composantes connexes les villes ayant même valeur de $R$ forment une composante connexe.
{% endnote %}
{% details "preuve", "open" %}

On le prouve par récurrence sur le nombre de segments examinés :

> Apres $k$ routes examinés,  les composantes connexes du réseau formé de ces $k$ routes sont les ensembles de villes ayant même valeur de $R$

1. Lorsqu'il n'y aucune route examinée chaque ville a un représentant différent ce qui représente bien les composantes connexes
2. À chaque fois que l'on ajoute une route :
   * soit les deux villes ont même représentant et l'hypothèse de récurrence stipulent qu'ils sont dans la même composante connexe
   * soit les deux villes ont un représentant différent et l'hypothèse de récurrence stipulent qu'ils sont dans deux composantes connexes différentes. L'ajout de la route regroupe les deux composantes en une seule composante, ce que l'on fait en leur associant un même représentant

{% enddetails %}

{% exercice %}
Montrez qu'il ne peut y avoir plus de $n-1$ fois où la ligne 3 de l'algorithme est vérifiée.
{% endexercice %}
{% details "corrigé" %}
À chaque fois que la ligne 3 de l'algorithme est vérifiée on regroupe deux composantes connexes. Or au départ il y en a $n$ et à la fin il ne peut y en avoir au minimum 1.
{% enddetails %}
{% exercice %}
En déduire que la complexité d l'algorithme est en $\mathcal{O}(n^2)$
{% endexercice %}
{% details "corrigé" %}
Il y a au pire $\frac{n(n-1)}{2}$ segments (un pour chaque couple) et la condition de la ligne 3 n'est vrai qu'au maximum $n-1$ fois.
{% enddetails %}

## Création du réseau routier

{% note "**définition**" %}

* le ***coût de construction*** d'une route entre deux villes $x$ et $y$ est $K \cdot d(x, y)$ où $d(x, y)$ est la distance entre les coordonnées géographiques de $x$ et de $y$
* le ***coût de construction*** d'un réseau routier est la somme des coûts de constructions des routes qui le composent.

{% endnote %}

On peut maintenant reformuler notre problème d'optimisation :

{% note "**Problème**" %}
Trouver un réseau routier de coût de construction minimum pour notre ensemble de villes.
{% endnote %}

L'analyse préliminaire précédente nous permet d'aborder sereinement ce problème d'optimisation. On peut utiliser l'algorithme "composante connexe" en choisissant l'ordre dans lequel examiner les routes.

Cet ordre semble évident puisque l'on veut minimiser le coût : on examine les routes par coût croissant.

Commençons par écrire cet algorithme, initialement proposé par [Kruskal](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal)

```text#
pour chaque ville v : R(v) = v
pour chaque route (x, y) examiné par distance croissante:
    si R(x) ≠ R(y):
        on ajoute (x, y) aux routes choisis
        pour chaque ville z telle que R(z) = R(y):
            R(z) = R(x)
```

L'étude précédente nous indique d'ores et déjà que :

1. on choisira exactement $n-1$ routes
2. le reseau routier formé des routes choisies sera connexe

Pour nos 100 villes, on trouve :

![kruskal](./kruskal.png)
{% details "code python de l'affichage" %}

On suppose que l'algorithme de Kruskal nous rend une liste `routes`{.language-} dont les éléments sont des couples $(v1, v2)$ avec $v1$ et $v2$ des noms de villes.

Pour les prendre en compte dans le graphique, il faut créer des segments de coordonnées utilisable par la [fonction `plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).

{% info %}
 On en a aussi profité pour changer de couleur en utilisant [cette documentation](https://matplotlib.org/stable/gallery/color/named_colors.html)
{% endinfo %}

```python
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

TAILLE = 10

x = []
y = []
label = []
for nom, (long, lat) in villes.items():
    x.append(long)
    y.append(lat)

    label.append(nom)

height = max(y) - min(y)
width = max(x) - min(x)

fig, ax = plt.subplots(figsize=(TAILLE, TAILLE * height / width))
ax.set_title("Les villes")

ax.scatter(x, y)
for i in range(len(x)):
    ax.text(x[i], y[i], label[i])

for x, y in routes:
    ax.plot(
        [villes[x][0], villes[y][0]],
        [villes[x][1], villes[y][1]],
        color=mcolors.CSS4_COLORS["brown"],
    )
plt.show()
```

{% enddetails  %}

Avant de montrer que l'algorithme de Kruskal est optimal, commençons par montrer une propriété intéressante de ce réseau :

{% note "**Propriété**" %}
Le réseau routier donné par l'algorithme de Kruskal ne contient pas de cycle.
{% endnote %}
{% details "preuve" %}
S'il contenait un cycle, lors de l'ajout de la dernière route $(x, y)$ on aurait $R(x) = R(v)$ ce qui est impossible.

{% enddetails %}

Montrons que l'algorithme est bien optimal :

{% note %}
L'algorithme de Kruskal produit un réseau de construction connexe à coût de construction minimal.
{% endnote %}
{% details "preuve", "open" %}

L'algorithme de Kruskal est un algorithme glouton, prouver son optimalité se fait en utilisant les techniques du cours.

1. On suppose que l'algorithme n'est pas optimal
2. On se donne une solution optimale qui coincide le plus longtemps possible avec la solution donnée par l'algorithme glouton
3. on prouve que l'on peut échanger un élément de la solution optimale  par le choix du glouton pour forger une solution optimale coïncidant plus longtemps avec celui-ci
4. contradiction

Soit $[s_1, \dots, s_{n-1}]$ la liste des routes choisis dans cet ordre par Kruskal. On suppose que ce n'est pas optimal et qu'il existe un réseau routier de coût de construction strictement plus petit.

Parmi tous les réseaux optimaux, on en choisit un qui coincide le plus longtemps possible avec notre algorithme glouton : $[s'_1, \dots, s'_m]$

On commence par remarquer que :

* $m \geq n-1$ sinon le réseau ne peut être connexe
* si $s_i = s'_i$ pour $1\leq i \leq n-1$ alors le réseau optimal ne l'est pas puisque la solution donnée par Kruskal est connexe.

Les deux remarques précédentes nous indiquent qu'il existe $1 \leq i^\star < n-1$ tel que :

* $s_i = s'_i$ pour $1\leq i < i^\star$
* $s_{i^\star} \neq s'_{i^\star}$

Notons $s_{i^\star}=(x, y)$. Si l'on supprime $s_{i^\star}$ du réseau obtenu par Kruskal, on déconnecte le réseau en 2 composantes connexes $X$ et $Y$ avec $x \in X$ et $y\in Y$. Tout chemin du réseau de Kruskal reliant une ville de $X$ à une ville de $Y$ contient ainsi le segment $(x, y)$

En considérant un chemin reliant $x$ à $y$ dans le réseau optimal, il existe forcément une route $(u, v)$ tel que $u \in X$ et $v \in Y$. Par construction, cette route ne peut être dans la solution obtenue par l'algorithme de Kruskal. De plus lors du choix de $s_{i^\star}$, on avait $R(u) \neq R(v)$ (sinon il existerait un chemin reliant $u$ à $v$ pour le réseau de Kruskal ne passant pas par $(x, y)$ ce qui est impossible) : si l'algorithme a choisi $(x, y)$ plutôt que $(u, v)$ c'est que $d(u, v) \geq d(x, y)$.

Enfin, si l'on supprime la route $(u, v)$ du réseau optimal, on le déconnecte en 2 parties $U$ et $V$ avec $u, x \in U$ et $v, y \in V$.
On peut alors échanger la route $(u, v)$ et $(x, y)$ pour obtenir :

* un réseau connexe
* de coût inférieur

Ce qui est une contradiction puisque le nouveau réseau coïncide plus longtemps avec celui obtenu par Kruskal.

{% enddetails %}

Le réseau obtenu par l'algorithme de Kruskal est optimal ! Il a alors la propriété de ne pas contenir de croisements (de segments qui s'intersectent).

{% note %}
Un réseau routier de coût de construction minimal n'a pas d'intersection de routes
{% endnote %}
{% details "preuve", "open" %}
Supposons que la route $(u, v)$ croise la route $(x, y)$ dans une solution optimale. On se retrouve alors dans le cadre de la figure ci-dessous :

![croisement](./croisement-segment.png)

Avec $uxvy$ qui forme un [quadrilatère](https://fr.wikipedia.org/wiki/Quadrilat%C3%A8re) convexe.

En supprimant le segment $(x, y)$ du réseau on déconnecte $x$ de $y$. Les deux villes $u$ et $v$ se retrouvent alors dans la même composante connexe, disons celle de $y$. En supprimant ensuite le segment $(u, v)$ on déconnecte $u$ de $v$ et on peut supposer sans perte de généralité que $y$ se retrouve dans la composante connexe de $v$.

On en conclut que les 3 segments $(x, u)$, $(x, v)$ et $(y, u)$ ne font pas partie du réseau et qu'en supprimant les segments $(x, y)$ et $(u, v)$ de celui-ci on obtient 3 composantes connexes :

* la composante connexe $A$ contenant $x$
* la composante connexe $B$ contenant $u$
* la composante connexe $C$ contenant $y$ et $v$

![croisement](./croisement-segment-connexe.png)

Le quadrilatère $uxvy$ étant convexe, on a que $d(x, y) + d(u, v) > d(x, v) + d(u, y)$ et donc en ajoutant les segments $(x, v)$ et $(u, y)$ on reconnecte le réseau et il est de coût strictement inférieur.

{% enddetails %}

## Chemins

Le réseau de coût de construction minimal est connexe et ne contient pas de cycle. Il n'existe donc pour chaque couple de ville qu'un unique chemin.

<div id="profondeur"></div>
{% exercice %}
En utilisant la méthode du [backtracking](https://en.wikipedia.org/wiki/Backtracking) (on va le plus loin possible et dès que l'on se retrouve dans une impasse on rebrousse chemin), décrivez un algorithme permettant de trouver dans un réseau de coût de construction minimal du chemin entre deux villes $x$ et $y$
{% endexercice %}
{% details "corrigé" %}

L'idée est de partir de $x$ et de progresser de proche en proche par des routes jusqu'à :

* soit trouver $y$
* soit se retrouver bloqué

Si l'on est bloqué en revient en arrière pour choisir une autre route.

L'algorithme s'appelle [parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) et est récursif.

```python#
def chemins_rec(précédent, courant, y, routes):
    for u, v in routes:
        if v == courant:
            u, v = v, u

        if (u, v) == (courant, précédent):
            continue
        elif (u, v) == (courant, y):
            return [v]
        elif u == courant:
            fin_chemin = routes_rec(u, v, y, routes)

            if fin_chemin != None:
                fin_chemin.append(v)
                return fin_chemin

```

Pour que tout fonctionne sans soucis, il ne faut pas oublier de vérifier que l'on ne revient pas en arrière.

On utilise alors ce parcours en initialisant la récurrence :

```python
chemins = chemins_rec(None, origine, destination, routes)
```

{% enddetails %}

On affiche le chemin entre les villes 0 et 1 de l'exemple :

![chemins](./chemin-0-1.png)

## Cycles

Le réseau routier de coût de construction minimum est parfait pour relier les villes à moindre coût. En revanche, il n'est pas robuste aux pannes ou au blocage. Une seule route de bloquée et le réseau n'est plus connexe.

L'idée est alors de chercher un cycle reliant toutes les villes. Pour tout couple de ville, il existe alors deux chemins disjoints permettant de les relier.

Ce problème est cependant souvent vu sous un autre angle, celui d'un [voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) voulant visiter toutes les villes :

{% note "**Problème du voyageur de commerce**" %}
Étant donné un ensemble de villes, trouver l'itinéraire le plus court passant par chaque ville une et une seule fois.
{% endnote %}

Sous la forme d'un problème d'optimisation on cherche, pour un ensemble de villes $V$ donné, un cycle $v_1 v_2\dots v_1$ passant par toutes les villes 1 fois minimisant la quantité :

$$
\sum_{i=1}^nd(v_i, v_{i+1}) + d(v_n, v_1)
$$

{% exercice %}
Combien de solutions possibles possède un problème du voyageur de commerce à $n$ villes ?
{% endexercice %}
{% details "Solution :" %}
Pour un départ fixé, une permutation des $n - 1$ villes restante produit une solution. Comme la permutation opposée revient à parcourir le cycle dans l'autre sens, il y a $\frac{(n-1)!}{2}$ solutions possibles.

Pour nos 100 ville, cela fit de l'ordre de $4.66\cdot 10^{155}$ solutions possibles.

{% enddetails %}

### Algorithme glouton

Le nombre astronomique de solutions possibles nous empêche de toutes les essayer. De plus, on peut montrer (nous ne le ferons pas ici) qu'il est illusoire de trouver une solution exacte (du moins pendant une séance de code) car le problème du voyageur de commerce est [NP-complet](https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet) (plus précisément NP-difficile, mais ne chipotons pas).

Couramment, l'algorithme glouton utilisé pour approximer ce problème est :

1. choisir une ville de départ qui constitue le départ du cycle
2. tant que toutes les villes n'ont pas été ajoutée au cycle : on ajoute la ville la plus proche du dernier élément de celui-ci.

Pour notre exemple, on trouve, en partant de la ville $0$ (la dernière ville traversée est la $17$):

![glouton voyageur](./glouton-voyageur.png)

> On obtient, pour K =1, un coût de construction de : 10.475838825929351

On voit bien que l'algorithme n'est pas vraiment optimal...

{% exercice %}
Exhibez un exemple simple pour lequel l'algorithme glouton ne trouvera jamais la solution optimale.
{% endexercice %}
{% details "Solution" %}

En utilisant la distance euclidienne, l'algorithme glouton ne trouvera jamais la bonne solution pour les 6 points de la figure suivante :

![glouton pas optimal](glouton-pas-optimal.png)

{% enddetails %}

### Optimisation

La représentation graphique de la solution montre de nombreux croisements, ce qui prouve que notre solution est bien améliorable :

{% note "**Proposition**" %}
Une solution du problème du voyageur de commerce n'a pas de croisements.
{% endnote %}
{% details "preuve", "open" %}

Supposons qu'un cycle comporte un croisement. On peut alors sans perte de généralité considérer que l'on est dans le cas ci-après :

![cycle croisement](./cycle-croisement.png)

Le quadrilatère $xvyu$ est alors convexe et en supprimant les segments $(x, y)$ et $(u, v)$ on obtient les composantes connexes $A$ et $B$.
Le cycle ci-après, obtenu en changeant les diagonales du quadrilatère par deux de ses côtés, est alors strictement meilleur :

![cycle décroisement](./cycle-décroisement.png)

{% enddetails %}

C'est l'idée sous-jacente de la méthode d'optimisation [2-opt](https://fr.wikipedia.org/wiki/2-opt) :

1. trouver un cycle potentiel
2. chercher un croisement et le supprimer
3. retour en 2

On peut itérativement chercher les croisements jusqu'à leurs disparitions complète, ou prendre un certain nombre de couples de segments et le décroiser si nécessaire. C'est cette dernière façon de faire qui est privilégiée pour de grands cycles.

Par exemple ci-dessous, on a décroisé les segment $(0, 17)$ et $(37, 50)$ :

![1 décroisement](cycle-décroisement-17-37.png)

Notre cycle étant très petit, on peut se permettre de faire tous les cas. La figure suivante montre le résultat de 100 itérations de tous les cas possibles (on exécute 100 fois un test de tous les décroisements possibles) :

![1 décroisement](cycle-décroisement-100-passes.png)

> On obtient, pour K =1, un coût de construction de : 8.606090557637186

C'est bien mieux, et il n'y a plus de croisements.

{% attention %}
Sans croisement ne veut pas forcément dire optimal !
{% endattention %}

## Algorithmes à performances garanties

L'algorithme glouton précédent ainsi que son optimisation ne garantissent rien sur la solution. Il existe cependant des algorithmes heuristiques dont on peut garantir la performance.

On peut commencer par donner une borne min du coût du voyageur de commerce :

{% exercice %}
Montrer que le coût du voyageur de commerce est plus grand que le coût du réseau connexe optimal
{% endexercice %}
{% details "preuve" %}
Le cycle est est réseau connexe, son coût est donc forcément plus important.
{% enddetails %}

### Du réseau au cycle

L'idée est de reprendre le réseau optimal et de le parcourir entièrement en suivant ses routes. Par exemple, en considérant le réseau ci-dessous :

![performance garantie 1](./performance-garantie-1.png)

On peut le parcourir en suivant ses routes de cette façon par exemple :

![performance garantie 2](./performance-garantie-2.png)

Ce qui donne le cycle :

$$
[1, 2, 3, 2, 4, 2, 1, 5, 1, 6]
$$

Il parcours 2 fois le réseau son coût est donc de deux fois le coût du réseau connexe optimal.

En supprimant les sommets déjà parcourus, on obtient le cycle :

$$
[1, 2, 3, 4, 5, 6]
$$

{% exercice %}
Montrez qu'une adaptation de l'[algorithme du parcours en profondeur](./#profondeur) utilisé dans la partie sur le calcul des chemins permet de trouver un parcours.
{% endexercice %}
{% details "corrigé" %}

Si l'on supprime la condition d'arrêt de la ligne 8 de l'algorithme, il va parcourir tout le réseau.

On peut alors construire petit à petit le parcours en stockant la ville dans le parcours la première fois qu'on la voit.

Ceci donne :

```python
def parcours_rec(précédent, courant, routes, parcours):
    if courant not in parcours:
        parcours.append(courant)

    for u, v in routes:
        if v == courant:
            u, v = v, u

        if (u, v) == (courant, précédent):
            continue
        elif u == courant:
            parcours_rec(u, v, routes, parcours)

```

Qu'on exécute avec les commandes :

```python
parcours = []
parcours_rec(None, une_ville, routes, parcours)
```

{% enddetails %}

Le coût de ce parcours est plus faible que le parcours précédent (on a une distance, donc elle respecte l'inégalité triangulaire). On en conclut que :

{% note "**propriété**" %}
Le coût du cycle issu du parcours du réseau optimal est au pire deux fois plus grans que le cycle optimal.
{% endnote %}

Le parcours donne, sur nos 100 villes :

![100 villes](./performance-garantie-villes.png)

> On obtient, pour K =1, un coût de construction de : 10.608836994373258

Ce qui après optimisation (100 passes) devient :

![100 villes](./performance-garantie-villes-100.png)

> On obtient, pour K =1, un coût de construction de : 8.596669623756684

### Algorithme de Christofides

L'[algorithme de Christofides](https://fr.wikipedia.org/wiki/Algorithme_de_Christofides) est une amélioration de l'algorithme précédent. On peut montrer qu'il est au pire 1.5 fos plus mauvais que le cycle optimal.

C'est d plus la meilleure approximation connue.
