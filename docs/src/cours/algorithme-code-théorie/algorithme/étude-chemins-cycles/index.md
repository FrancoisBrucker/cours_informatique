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

Aucune route n'a été construite et on ne peut voyage d'une route à l'autre et dans la figure ci-dessous on a construit soit toutes les routes possibles (à gauche), ce qui est pratique si ont veut voyager vite entre deux villes mais c'est beaucoup trop cher (et dangereux, regardez le nombre de croisements !) ou construire uniquement le nombre minimum de routes (droite), remarquez au'il n'y a pas de croisements.

![5 villes arbres](5-villes-complet-arbre.png)

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
TAILLE = 10

x = []
y = []
label = []
for (nom, (long, lat)) in villes.items():
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

plt.show()
```

{% enddetails %}

Pour ce qui va suivre, une hypothèse souvent utilisée est que l'ensemble des points est en [position générale](https://fr.wikipedia.org/wiki/Position_g%C3%A9n%C3%A9rale), c'est à dire que **3 points ne sont jamais alignés**.

Ce n'est pas une contrainte forte puisque la probabilité que ça arrive est nulle (si on tire au hasard des coordonnées réelles aux points), et – même si ça arrivait, il suffirait de déplacer un des trois points d'epsilon pour que ça n'arrive plus.

La raison fondamentale de cette hypothèse est :

{% note %}
Si $P$ est un ensemble de points en ***position générale***, alors pour tout couple $x, y \in P$ aucun autre point de $P$ n'est sur le segment entre $x$ et $y$.
{% endnote %}

## Routes et Connexité

Nous devons créer un réseau routier entre les villes pour les relier.

### Routes

{% note %}
Une ***route*** entre deux villes $x$ et $y$ est soit :

* le ***segment*** entre $x$ et $y$
* soit une suite $v_1, \dots, v_{i-1}, v_i, \dots, v_n$ tel que :
  * $v_1 = x$, $v_n = y$
  * les villes $v_{i-1}$ et $v_{i}$ sont différentes et reliées par un segment pour tout $1 < i \leq n$
{% endnote %}

La notion de route s'écrit très bien sous la forme d'une relation $R$ sur un ensemble $V$ de villes. On dira que $xRy$ s'il existe une route entre $x$ et $y$. Cette relation est une [relation d'équivalence](https://fr.wikipedia.org/wiki/Relation_d%27%C3%A9quivalence) car elle est :

* réflexive $xRx$ (le singleton $x$ permet de relier $x$ à lui-même)
* symétrique $xRy$ implique $yRx$ (les routes sont à double sens)
* transitive $xRy$ et $yRz$ implique $xRz$ (on colle la suite allant de $x$ à $y$ à la suite allant de $y$ à $z$)

L'intérêt de cette formalisation est qu'elle montre que la notion de route se crée :

1. en considérant les segments entre deux villes
2. en fermant la relation par transitivité

{% exercice %}
Écrivez un algorithme utilisant la programmation dynamique créant la fermeture transitive de la relation S telle que $xSy$ s'il existe un segment entre $x$ et $y$.
{% endexercice %}
{% details "corrigé" %}

C'est l'[Algorithme de Roy](https://fr.wikipedia.org/wiki/Algorithme_de_Warshall) improprement appelé algorithme de Warshall par les américains.

On suppose que l'on considère un ensemble $\\{v_1, \dots, v_n \\}$ de villes et une relation $R$ telle que
L'idée est considérer des relations $R_k$ tels que :

* $R_0 = S$
* $R_k$ la relation telle que $xR_ky$ s'il existe une route entre $x$ et $y$ passant (hors $x$ et $y$) uniquement par les villes $\\{v_1, \dots, v_k \\}$

On a alors (clairement) le fait que : $xR_ky$ si :

* $xR_{k-1}y$
* ou si $xR_{k-1}v_k$ et $v_kR_{k-1}y$

Ceci peut s'écrire de la façon suivante :

```python
de k=1 à n:
    de i=1 à n:
        de j=1 à n:
            v_iRv_j = v_iRv_j OR (v_iRv_k AND v_kRv_j)
```

La complexité de cet algorithme est en $\mathcal{O}(n^3)$
{% enddetails %}

### Connexité

{% note %}
Un réseau routier de villes est ***connexe*** si quelque soient deux villes $x$ et $y$, il existe une route entre $x$ et $y$.

{% endnote %}

Le fait que la notion de routes soient ue relation d'équivalence montre que le réseau routier est connexe si et seulement si la relation route (la relation $R$ de la partie précédente) n'admet qu'une seule classe d'équivalence ($R(x) = R(y)$ quelques soient les villes $x$ et $y$).

{% note %}
Si $R$ est une relation d'équivalence sur $V$, la classes d'équivalence de $x \in V$ est :

$$
R(x) = \\{ y | xRy, y \in V \\}
$$

{% endnote %}

Si un réseau routier n'est pas connexe, les classes d'équivalences de la relation routes donnent les ***composantes connexes*** du réseau routier. Le réseau routier de la figure suivante contient 2 composantes connexes :

![2 composantes connexes](./2-composantes-connexes.png)

Notez que :

{% note %}
Si $V_1$ et $V_2$ sont deux composantes connexes d'un réseau routier alors :

* $V_1 \cap V_2 = \emptyset$
* si on ajoute **un** segment entre une ville de $V_1$ et une ville de $V_2$, alors $V_1 \cup V_2$ devient une composantes connexe du nouveau réseau

{% endnote %}

En ajoutant le segment de route entre B et P, on obtient un réseau routier connexe :

![1 partie connexe](./1-parties-connexes.png)

La propriété ci-dessus nous permet de créer un algorithme permettant de trouver toutes les parties connexes d'un réseau routier.

> TBD algo
> complexité

algo connexité

### Connexe min de routes

algo connexité nous dit n-1 a chaque etape on supprime une composante connexe
algo connexité + pas ajout

connexe min si supprime une route et toujours connexe

### min coût de construction

* le ***coût de construction*** d'une route entre deux villes $x$ et $y$ est $K \cdot d(x, y)$ où $d(x, y)$ est la distance entre les coordonnées géographiques de $x$ et de $y$
* le ***coût de construction*** d'un ensemble de villes $V$ est la somme des coûts de constructions des routes qui le compose

algo connexité + pas ajout + ordre des arêtes


exemple sur le précédent

composante connexe : ensemble de villes telle que je peux aller de l'une à l'autre.

symétrique (route à double sens)
transitif

relation d'équivalence pour R : ligne droite entre x et y

aller d
xRy : route entre x et y
transitive
connexité : classe d'équivalences

algo composantes connexes: liste de routes et couleurs aux composantes. 

si couleur différentes on rassemble
sinon on ne fait rien


xy et xz => yz

algo si connexe :
il existe un chemin et connexité
< n-1 impossible et = n-1 ok

on appelle ça un arbre

## Arbres

connexe minimal :

1. supprime une route déconnecte
2. connexe et Pas de cycle
3. connexe et n-1 routes

supprime une route : 2 parties connexes minimales
il existe un élément avec 1 seule route d'accès

1. un chemin ok : toutes les routes

algo :

1. juste plus proche ou k-plus proche marche pas forcement. il faut 
2. tant que pas connexe on continue ( Kruskal)
3. pas de croisements d'arêtes
4. ajouter au plus proche de ceux qu'on a déjà (prim) : ne pas faire laisser en info.

## Chemins

trouver le chemin avec largeur (gloutons like) et profondeur (backtracking) sur un arbre

algo : marquage pour optimalité
python : dict et ensemble pour efficacité (complexité en moyenne)

on peut partir d'un point pour tout connaître. algo prédécesseur

## cycles

si route unique alors soucis si manif ou tremblement de terre

### problème

cercle : voyageur de commerce

### glouton

### glouton pas optimal

Et aucun de connu. C'est un problème NP-difficile.

1 cycle ok, le plus petit dur.

principe du 2-opt (ils auront à le coder dans le projet)

## algo à performances garanties

### 2x arbres

### Christofides

les cycles se combinent entre eux comme la connexité @ cycles qui se touchent forment un gros cycle

On prend pas tout sinon trop donc on ajoute juste ce qu'il faut à un arbre

si pair => cycles. Donc ajouter 1 arêtes à ceux qui sont impair.

