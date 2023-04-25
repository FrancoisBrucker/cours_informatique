---
layout: layout/post.njk
title: "Projet : bataille de la Marne"

eleventyNavigation:
  key: "Projet : bataille de la Marne"
  parent: "Graphes"
---

<!-- début résumé -->

Un exercice de modélisation complexe.

<!-- end résumé -->

On va optimiser l'arrivée des [taxis à la bataille de la marne de 1914](https://fr.wikipedia.org/wiki/Taxis_de_la_Marne).

On a un ensemble $S$ de villes, et des routes reliant certaines villes entre elles (il peut exister plusieurs routes entre deux villes), décrites dans un graphe non orienté $G$.

* chaque ville $i$ est caractérisée par un nombre $p[i]$ de places de parking,
* chaque route $(i, j)$ est caractérisée par le temps $tv[(i, j)]$ qu'il faut pour aller de la ville $i$ à la ville $j$
* chaque route $(i, j)$ a une capacité $ct[(i, j)]$ qui correspond  au nombre de véhicules qui peuvent l’emprunter par unité de temps

Au temps $t = 0$, on a un certain nombre de véhicules stationnés dans différentes villes et il faut qu’au temps $t = K$, le plus possible de véhicules soient arrivés à une ville donnée (la Marne).

Il est possible que des véhicules arrivent avant cette date butoir, mais après la date K, c’est
trop tard.

{% note "**Problème**" %}
Est-il possible de déplacer des taxis initialement placées dans $T$ villes vers la marne en moins de $K$ unités de temps ?
{% endnote %}

## Modélisation

On va modéliser ce problème comme un problème de flots. Le problème est :

* qu'une route possède à la fois une capacité et une longueur, qui sont des caractéristiques très différentes
* qu'il faut gérer le temps

On considère le temps comme étant une valeur discrète prenant 0, 1, 2, ..., K comme valeur.

On peut alors représenter chaque ville par $K+1$ sommets représentant chacun la ville à un temps donné. La ville $v$ sera ainsi représentée par les sommets $(v, 0)$, ...,  $(v, K)$, le sommet $(v, i)$ représentant la ville au temps $i$.

De là, une route de temps 5 (et de capacité $ct[(v1, v2)]$) de v1 vers v2 va être représentée par :

* un arc de $(v1, 0)$ vers $(v2, 5)$ de capacité $ct[(v1, v2)]$
* un arc de $(v1, 1)$ vers $(v2, 6)$ de capacité $ct[(v1, v2)]$
* ...
* un arc de $(v1, K-5)$ vers $(v2, K)$ de capacité $ct[(v1, v2)]$

Une voiture qui reste dans la ville $v1$ au temps $i$ emprunte un arc de $(v1, i)$ vers $(v1, i+1)$ dont la capacité est le nombre de places de parking $p[v1]$ de la ville v1.

Le sommets spéciaux sont :

* le puits est la Marne au temps K: $(Marne, K)$
* la source est un sommet fictif que l'on relie aux sommets $(v, 0)$ correspondant aux villes où il y a des taxis au temps 0. La capacité de ses arcs est le nombre de taxis disponibles.

## Données

On reprend le graphe des villes de plus de 10000 habitants en France métropolitaine, déjà utilisé lors du [projet : chemin de poids minimum](../projet-chemins-min/).

{% faire %}
Reprenez la [partie Données](../projet-chemins-min#données){.interne} du [projet : recherche de chemins de poids minimum](../projet-chemins-min/){.interne} et stockez :

* les données du fichier json dans la variable `villes`{.language-}
* le graphe produit à partir des données brutes dans la variable `france`{.language-}
{% endfaire %}

Il nous reste à placer les différents paramètres du problèmes :

* les villes de départ, disons $T = 5$ prisent au hasard `TAXI_DÉPART = random.sample(list(france), T)`{.language-} (on utilise lma fonction sample du module random)
* nombre de taxis par villes : une constante valant `NOMBRE_TAXI`{.language-}
* la ville de destination, nommé `LA_MARNE`{.language-} qu'on a qu'à dire que c'est la ville de `Reims`{.language-}
* temps final : $K = 20$
* capacité des routes (nombre de taxis par unité de temps) : dictionnaire `ct`{.language-}
* le nombre de places de parking par villes : dictionnaire `p`{.language-}
* le temps de parcours de chaque route : dictionnaire `tv`{.language-}

### Capacité des routes

On va donner une capacité aléatoire de taxi par route. On borne cependant ce nombre par `MAX_TAXI_ROUTE`{.language-}, disons égal à 20.

{% faire %}
Créez le dictionnaire `ct`{.language-} en donnant une capacité égale à un entier aléatoire entre 1 et `MAX_TAXI_ROUTE`{.language-}.

Attention, notre graphe est non orienté. Les capacités des arcs $(x, y)$ et $(y, x)$ doivent êtres identiques.
{% endfaire %}

### Places de parking

Comme les capacités des routes, on va prendre un entier aléatoire entre 1 et `MAX_PARKING`{.language-}.

{% faire %}
Créez le dictionnaire `p`{.language-} en donnant une capacité égale à un entier aléatoire entre 1 et `MAX_PARKING`{.language-} à chaque ville.

{% endfaire %}

### Temps de parcours des routes

Pour homogénéiser les temps de parcours, on aimerait faire en sorte qu'ils soient compris entre 1 et `MAX_DIST`{.language-} (disons 5) et soit dépendant de la distance GPS entre les deux villes.

Nous allons créer cette distance en plusieurs temps
{% faire %}
Créez une fonction `d_GPS(uv)`{.language-} qui prend **1** paramètre égal à un couple $(u, v)$ et qui rend la distance GPS au carré entre les deux villes de nom $u$ et $v$.
{% endfaire %}

{% faire %}
Créez une liste `distances_villes`{.language-} contenant tous les couples **unique** d'arcs du graphe. **Attention**, si $(u, v)$ est dans la liste, $(v, u)$ ne doit pas y être.
{% endfaire %}

{% faire %}
Triez la liste `distances_villes`{.language-} par distance.

Vous pourrez utiliser pour cela la fonction `d_GPS(uv)`{.language-} que vous avez créée et l'[attribut `key`{.language-}](https://docs.python.org/fr/3/howto/sorting.html#key-functions) de la méthode de liste `sort`{.language-}
{% endfaire %}

Enfin :

{% faire %}
Créez le dictionnaire `tv`{.language-} où la valeur associée à la clé $(u, v)$ vaut `int(MAX_DIST * i / len(distances_villes))`{.language-}
{% endfaire %}

## Modèle

Il faut transformer les données du problème en une instance de notre modélisation.

{% faire %}
Créez, à partir des données, un graphe $G$ et une capacité $c$ associée représentant notre modélisation. Vous pourrez :

1. commencer par créer les sommets du graphe,
2. puis créez les arêtes et les capacités correspondant au parking
3. ajoutez les arcs des routes
4. ajoutez la source et ses poids au graphe
5. finissez par ajouter un sommet fictif puits `'p'`{.language-} dont le seul arc est `((la_marne, K), 'p')`{.language-} de capacité égale à la totalité des taxis. Cela permettra de facilement connaître le nombre de taxi arrivés à destination

{% endfaire %}

## Résolution

{% exercice %}
Utilisez l'algorithme de [Ford et Fulkerson](../flots/#ford-fulkerson){.interne} pour résoudre le système. Quel pourcentage de Taxis a atteint la marne ? Faites plusieurs essais en fonction des villes de départ et du temps total $K$ alloué.
{% endexercice %}

### Nombre de Taxis à un instant donné

A un instant donné, un taxi peut être dans une ville donnée ou sur la route.

{% exercice %}
à $t$, combien de taxis sont dans la ville v ?
{% endexercice %}
{% details "solution" %}
C'est la somme des flots $f[(u, (v, t))]$.
{% enddetails %}
{% faire %}
Codez une fonction `taxi_dans_ville_a_t(v, t)`{.language-} qui rend le nombre de taxi dans la ville $v$ au temps $t$.

Vous aurez certainement besoin de coder le graphe $G'$, opposé à $G$ ($xy$ est un arc de *G'$ si et seulement si $yx$ est un arc de $G$).
{% endfaire %}

### Nombre de taxi en transit sur une route

{% exercice %}
à $t$, combien de taxis sont en transit entre les villes u et v ?
{% endexercice %}
{% details "solution" %}
A un instant donné, le nombre de taxis sur une route $(u, v)$ est :

$$
\sum_{1 \leq k < tv[(u, v)]} f[(u, t - k), (v, t - k + tv[(u, v)])] + f[(v, t - tv[(u, v)] + k), (u, t + k)]
$$

Le premier élément de la somme correspondant aux taxis allant de $u$ à $v$ et le second élément à ceux allant de $v$ à $u$.

Attention aux bornes également, il faut que tout reste entre 0 et K.

Le paramètre $k$ correspond à l'endroit sur l'arc où sont sont les taxis avec les bornes $k=0$ (en u) et $k = tv[(u, v)]$ (en v).
{% enddetails %}
{% faire %}
Codez une fonction `taxi_entre_villes_a_t(u,v, t, k)`{.language-} qui rend le nombre de taxi dans la ville $v$ au temps $t$ et à la position $1 \leq k < tv[(u, v)]$.

Faites attention aux bornes et rendez 0 si les bornes sont dépassées.
{% endfaire %}

### Représentation graphique

Le code suivant représente la carte de France avec les différentes données du problème représentées :

```python
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


fig, ax = plt.subplots(figsize=(10, 10))

for u in france:
    ax.text(villes[u]["longitude"], villes[u]["latitude"], u)
    for v in france[u]:
        if v > u:  # évite de tracer 2 fois le même arc
            continue

        ax.add_line(
            mlines.Line2D(
                (villes[u]["longitude"], villes[v]["longitude"]),
                (villes[u]["latitude"], villes[v]["latitude"]),
            )
        )

ax.plot(
    [villes[x]["longitude"] for x in france],
    [villes[x]["latitude"] for x in france],
    "o",
    color="black",
    markersize=2,
)
ax.plot(
    [villes[LA_MARNE]["longitude"]],
    [villes[LA_MARNE]["latitude"]],
    "*",
    color="red",
    markersize=20,
)
ax.plot(
    [villes[x]["longitude"] for x in TAXI_DÉPART],
    [villes[x]["latitude"] for x in TAXI_DÉPART],
    "o",
    color="red",
    markersize=10,
)
```

{% faire %}
En utilisant [les cercles en matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html) :

```python
circle = plt.Circle((x, y), r)
ax.add_patch(circle)
```

Ajoutez à un instant donné les taxis. Sur le graphique.
{% endfaire %}

{% faire %}
<https://courspython.com/animation-matplotlib.html#animation-sans-le-module-animation>

Vous donne une idée d'animation de vos graphiques.

Il vous faudra après chaque pause supprimer les cercles des taxis pour dessiner ceux du temps suivant. Ceci peut se faire avec la commande : `[p.remove() for p in reversed(ax.patches)]`{.language-}.

{% endfaire %}
