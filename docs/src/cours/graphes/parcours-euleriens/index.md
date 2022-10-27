---
layout: layout/post.njk
title: Parcours Eulériens

authors: 
    - François Brucker

eleventyNavigation:
  key: "Parcours Eulériens"
  parent: "Graphes"
---

<!-- début résumé -->

Voir grâce à l'exemple des circuits eulériens ce qu'est un chemin, un cycle, et nos premiers algorithmes de graphes.

<!-- fin résumé -->

## Le problème concret ou *"comment ne pas aller se promener"*

C'est un retour aux sources s'il l'on peut dire puisqu'il s'agit du problème des [7 ponts de Königsberg](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_sept_ponts_de_K%C3%B6nigsberg), qui permit à [Euler](https://fr.wikipedia.org/wiki/Leonhard_Euler) d'inventer la théorie des graphes pour éviter d'aller se balader.

La ville de Kaliningrad (anciennement appelée Königsberg) possédait 7 ponts aux 18ème siècle qui enjambent la Pregel. Ca ressemblait un peu à ça (cliquez sur l'image pour voir les ponts en vrai sur google maps):

[![ponts de Königsberg](https://upload.wikimedia.org/wikipedia/commons/5/5d/Konigsberg_bridges.png)](https://www.google.com/maps/d/viewer?msa=0&mid=1eyTkT4J8X_GRGc1qccm-iDbdZQo&ll=54.708383%2C20.508084000000014&z=15)

L'histoire veut qu'une tradition bourgeoise (et noble) de l'époque soit de faire les ballades digestives autour de ces ponts en essayant de tous les traverser une fois et de  revenir à son point de départ.

Personne n'y arrivant, le jeu devint fort populaire. Sauf qu'Euler, s'il y a bien une chose qu'il n'aimait pas, c'était les ballades.

Du coup, un après-midi, plutôt que d'aller se balader il griffonna le schéma suivant sur un coin de nappe et démontra à l'assistance médusée qu'il était impossible de faire ce qu'ils voulaient faire et que donc il préférait reprendre un peu de tarte que d'essayer un truc impossible.

Euler avait d'un coup prix 1kg et inventé la théorie des graphes. Le dessin qu'Euler griffonna était celui-ci :

![graphe_7_ponts](./graphe_7_ponts.png)

C'est un multi-graphe non orienté et est une modélisation du problème, les sommets $A$, $B$, $C$ et $D$ représentant les quatre berges de la ville et les arêtes les 7 ponts.

Le problème revient maintenant de trouver un cycle qui passe par toutes les arêtes du multi-graphe.

## Retour au problème

{% note "**Définition :**" %}
Soit $G= (V, E)$ un multi-graphe non orienté. Un **cycle eulérien** de $G$ est un cycle passant par toutes les arêtes du graphe.
{% endnote %}
{% info %}
Comme les arêtes d'un cycle n'y apparaissent qu'une seule fois, un cycle eulérien passe exactement une fois par toutes les arêtes du graphe.
{% endinfo %}

### C'est impossible dans l'exemple

Avec notre graphe c'est **impossible** car il faut pouvoir repartir d'un sommet après en être arrivé. Si un tel cycle existait pour tout $u_i$ : $u_{i-1}u_i$ et $u_iu_{i+1}$ seraient des arêtes du graphes. Comme le chemin passe une seule fois par chaque arête du graphe on en conclut que $\delta(u_i)$ serait paire.

Comme $\delta(C) = 3$ et est impair, il est impossible de trouver un cycle eulérien dans notre graphe.

### Une implication

La remarque précédente nous donne une implication importante :

{% note "**Remarque :**" %}
S'il existe un cycle eulérien pour un multi-graphe non-orienté $G$, alors tout sommet de ce graphe est de degré pair.
{% endnote %}

### La réciproque sur un exemple ?

Le graphe suivant a tous ses degrés pair :

![est-ce possible](./possible_eulerien.png)

{% exercice %}
Pouvez-vous trouver un cycle eulérien ?
{% endexercice %}
{% details "solution" %}
Oui c'est possible avec l'ordre dans lequel examiner les sommets du chemin.

![une réponse possible](./possible_eulerien_!.png)

Mais il y en a plein d'autres possibles !

{% enddetails %}

## Equivalence

Ce qui est très beau c'est que la réciproque complète est vraie. On a le théorème suivant :

{% note "**Proposition :**" %}
Un multi-graphe non orienté connexe admet un cycle eulérien si et seulement si le degré de tout ses sommets est pair.
{% endnote %}
{% details "démonstration ⇒" %}
On l'a déjà prouvé, mais refaisons le pour la complétion.

Si un cycle Eulérien $u_0 \dots u_k$ existe, à chaque $u_i$ : $u_{i-1}u_i$ et $u_iu_{i+1}$ sont des arêtes du graphes.  Comme le chemin passe une seule fois par chaque arête du graphe, à chaque fois que l'on rencontre un sommet donné $x$, on lui trouve 2 nouvelles arêtes. On en conclut que $\delta(x)$ est égal au nombre de fois où $x$ apparaît dans le cycle fois 2 : c'est donc pair.
{% enddetails %}
{% details "démonstration ⇐" %}

1. Comme notre graphe est eulérien et connexe, les degrés de tous les sommets sont pairs et strictement positif : donc supérieur ou égal à 2. Il existe alors un cycle dans notre graphe.
2. en supprimant le cycle du graphe, on obtient toujours un graphe dont les degrés sont pairs (en supprimant un cycle on a supprimé un nombre pair d'arête pour chaque sommet apparaissant dans le cycle)
3. on supprime tous les sommets de degrés 0.
4. on est ramené à notre hypothèse de départ, c'est à dire un graphe où tous les sommets sont de degrés pairs et strictement positif.

L'algorithme ci-dessus nous permet de décomposer notre graphe en une série de cycles, disons qu'il y en a $m$. Il nous reste à former un énorme cycle à partir de ces petits cycle.

Pour cela, comme le graphe est connexe il va exister deux cycles $C_1$ et $C_2$ qui partagent un sommet $x$. On peut alors faire commencer les cycles $C_1$ et $C_2$ par $x$ et on peut coller les deux cycles ensemble en formant le cycle : $C_1 + C_2[1:]$. On est passé de $m$ cycles à $m-1$ cycles et on peut recommencer la procédure jusqu'à n'obtenir qu'un unique cycle qui est notre cycle eulérien.

{% enddetails %}

## Trouver un cycle Eulérien

Codons l'algorithme de cycle eulérien.

### Encodage

On va se restreindre aux graphes non-orienté. Pour cela, notre codage par dictionnaire fonctionne tout à fait. Prenons par exemple le graphe :

![exemple Euler](./euler_exemple_1.png)

Il se code en :

```python
G = {
    "1": {"2", "3"},
    "2": {"1", "3", "4", "5"},
    "3": {"1", "2", "4", "5"},
    "4": {"2", "3", "5", "6"},
    "5": {"2", "3", "4", "6"},
    "6": {"4", "5"},
}
```

Ajoutons tout de suite une fonction pour copier le graphe, puisque notre algorithme va petit à petit supprimer ses arêtes :

```python
def copie(G):
    G_copie = dict()

    for x in G:
        G_copie[x] = set(G[x])

    return G_copie

G2 = copie(G)
```

{% attention %}
Il faut **aussi** copier les valeurs du dictionnaire (les ensembles) !
{% endattention %}
{% info %}
On aurait pu faire la copie en une ligne avec les [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) de python : `G2 = {x: set(y) for x, y in G.items()}`{.language-}
{% endinfo %}

### Principe de l'Algorithme

La démonstration de la réciproque donne également un algorithme de construction d'un cycle Eulérien pour un multi-graphe $G = (V, E)$ vérifiant les conditions du théorème d'existence de cycle Eulérien :

```text
C = []
tant que G contient des sommets:
  soit c un cycle de G
  ajouter c à C
  supprimer les arêtes de c dans G
  supprimer les sommets sans arêtes de G

concaténez les différents cycles de C en un unique cycle
```

Sur le graphe précédant cela donne, en prenant $1231$ comme premier cycle :

![exemple Euler](./euler_exemple_2.png)

En prenant $35243$ comme second cycle :

![exemple Euler](./euler_exemple_3.png)

Enfin, le troisième cycle est $4564$ :

![exemple Euler](./euler_exemple_4.png)

Une fois le graphe vidé, on concatène les cycles ensemble en collant deux à deux des cycles ayant un élément en commun. Ici, en commençant par concaténer le second $43524$ et troisième cycle $4564$ ensemble en $43524564$. On peut ensuite rajouter le premier cycle faisant commencer le cycle $43524564$ par deux $24564352$ puis en les collant ensemble $24564352312$ pour donner le cycle eulérien final.

### Décomposition du graphe en cycles

Commençons par créer une fonction qui supprime un cycle du graphe :

```python
def supprime(G, c):
    x = c[0]
    for y in c[1:]:
        G[x].remove(y)
        if not G[x]:
            del G[x]

        G[y].remove(x)
        if not G[y]:
            del G[y]

        x = y
```

Cette fonction supprime également les sommets qui n'ont plus d'arêtes.

Puis l'algorithme général de décomposition :

```python
cycles = []
c = cycle(G2)

while c:
    supprime(G2, c)
    cycles.append(c)

    c = cycle(G2)

print(cycles)

```

Trouver un cycle peut se faire en utilisant l'algorithme du cours [`cycle_non_orienté(G,x)`{.language-}](../chemins-cycles-connexite#algo-cycle-non-oriente) (même s'il n'est pas optimal, pour de petits graphes le temps de calcul ne sera pas rédhibitoire). Il faut juste trouver un sommet de départ. Si on s'arrange pour supprimer du graphe les sommets sans arêtes, on peut prendre n'importe lequel :

```python
def cycle(G):
    a = list(G.keys()).pop()
    return cycle_non_orienté(G, a)
```

Pour l'exemple du graphe, j'obtiens par exemple (il y a d'autres possibilités) :

```python
[['1', '2', '5', '3', '1'], ['4', '2', '3', '4'], ['5', '4', '6', '5']]
```

### Concaténation de deux cycles

Pour concaténer deux cycles ensemble, il faut pouvoir faire commencer un cycle par un sommet donné `x`{.language-} :

```python
def décale(cycle, x):
    cycle = cycle[:-1]
    i = cycle.index(x)

    return cycle[i:] + cycle[:i] + [cycle[i]]
```

Puis coller deux cycles par un sommet commun `x`{.language-} :

```python
def concatène(c1, c2, x):
    c1 = décale(c1, x)
    c2 = décale(c2, x)

    return c1 + c2[1:]
```

### Concaténation de tous les cycles

Il suffit d'itérer le processus pour deux cycles en cherchant des cycles ayant un élément en commun :

```python
while len(cycles) > 1:
    c = cycles.pop()
    for i in range(len(cycles)):
        intersection = set(c).intersection(set(cycles[i]))
        if intersection:
            x = intersection.pop()
            cycles[i] = concatène(cycles[i], c, x)
            break

cycle_eulérien = cycles[0]
print(cycle_eulérien)
```

J'obtiens, avec les cycles précédents :

```python
['3', '1', '2', '5', '4', '6', '5', '3', '4', '2', '3']
```

## Généralisation

Il existe de nombreuses généralisations aux cycles eulérien. Citons en trois : les chemins eulériens, les circuits eulériens des graphes orientés et les cycles Eulérien des graphes mixtes.

### Chemin eulérien

{% note "**Définition :**" %}
Soit $G= (V, E)$ un multi-graphe non orienté. Un **chemin eulérien entre $x$ et $y$** est un chemin entre $x$ et $y$ qui prend toutes les arêtes du graphe
{% endnote %}

On prouve aisément que les graphes dont tous les sommets sont de degré pair sauf $x$ et $y$ qui doivent être de degré impair sont solutions de ce problème. En effet, on ajoute une arête entre $x$ et $y$ et on est ramené aux problème du cycle eulérien.

### Graphes orientés

{% note "**Définition :**" %}
Soit $G= (V, E)$ un multi-graphe. Un **circuit eulérien** de $G$ est un circuit passant par tous les arcs du graphe.
{% endnote %}

Les multi-graphe (orientés) qui possèdent un circuit eulérien sont exactement les multi-graphes où $\delta^+(x) = \delta^-(x)$ pour tout sommet $x$.

### Graphes mixtes

{% note "**Définition :**" %}
Soit $G= (V, E, A)$ un multi-graphe mixte. Un **circuit eulérien** de $G$ est alors un circuit de $G$ prenant tous les arc et toutes les arêtes de $G$.
{% endnote %}

Un (multi-)graphe mixte $G$ possède un circuit eulérien si et seulement si :

* il est **pair** : pour tout sommet $x$ le nombre $\delta_1(x) + \delta_2^+(x) + \delta_2^-(x)$ (pour les graphes $G_1$ et $G_2$) est pair
* il est **équilibré** : quelque soit $S \subseteq V$ :

$$
\vert \\{ xy \in A \mid x \in S, y \in V \backslash S\\} \vert - \vert \\{ yx \in A \mid x \in S, y \in V \backslash S\\} \vert \leq \vert \\{ xy \in E \mid x \in S, y \in V \backslash S\\} \vert
$$
