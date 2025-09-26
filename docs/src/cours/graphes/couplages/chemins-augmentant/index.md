---
layout: layout/post.njk
title: Chemins augmentant

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD outils fondamental pour la recherche de couplages optimaux.
> TBD refaire lien.

Dans les exercices de modélisation par des flots, [le problème du transport amoureux](../projet-flots-modélisation/#transport-amoureux){.interne} permettait de résoudre un problème de couplage.

En utilisant cette modélisation, et en augmentant les flots d'une valeur entière (toujours 1) une chaîne augmentante est un chemin tel que les arcs sont :

- têtes bêches de la source au puits
- les arcs allant vers le puits sont de flot 0 et peuvent être augmentés
- les arcs allant vers la source sont de flot 1 et peuvent être diminués.

Essayons d'adapter ceci à notre problème de couplage. Commençons par décrire le graphe des relations entre les deux couples de personnes. Marier le plus de héros de roman revient à trouver un couplage maximum dans le graphe suivant :

![couplage transport amoureux 1](../problème/couplage-transport-1.png)

On a pas besoin d'ajouter une source ou un puits. Ajoutons quelques arêtes au couplage :

![couplage transport amoureux 2](./couplage-transport-2.png)

Le graphe précédent admet le couplage $M = \\{ \\{\text{Cléopâtre},\text{Achille}\\}, \\{\text{Fanny},\text{Marius}\\} \\}$. Dans le cadre d'une modélisation par flot (avec des arcs, une source et un puits), il resterait encore des chaines augmentante comme : `source -> Juliette -> Rodrigue -> puits` ou encore `source -> Iphigénie -> Achille <- Cléopâtre -> César -> puits`.

Dans notre graphe de couplage ceci s'écrit comme un chemin de longueur impaire dont une arête est alternativement dans le couplage ou non et commence par un sommet qui n'est extrémité d'aucune arête du couplage.

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe et $M$ un de ses couplages.

- **_Un chemin alternant_** $x_0\dots x_k$ est tel que :
  - $x_0\dots x_k$ est un [chemin élémentaire](../chemins-cycles-connexite/#définition-élémentaire) de $G$
  - si $x_{i-1}x_{i} \in M$ alors $x_{i}x_{i+1} \notin M$ pour tout $i$
  - si $x_{i-1}x_{i} \notin M$ alors $x_{i}x_{i+1} \in M$ pour tout $i$
- **_Un chemin augmentant_** $x_0\dots x_k$ est un chemin alternant qui commence ($x_0$) et termine ($x_k$) par deux sommets libres.

{% endnote %}

Dans l'exemple précédent, `Cléopâtre - Achille - Iphigénie` est un chemin alternant mais pas augmentant, alors que `Juliette - Roméo` ou encore `César - Cléopâtre - Achille - Iphigénie` sont des chemins augmentant. On remarque que cette notion (de chemin augmentant) est similaire à celle de chaîne augmentante dans les flots :

{% note "**Proposition**" %}
Soit $G=(V, E)$ un graphe et $M$ un de ses couplages.

S'il existe un chemin augmentant $x_0\dots x_{2p+1}$ alors l'ensemble :

<div>
$$
M' = (M \backslash \{ x_{1+2i}x_{2i+2} \vert 0 \leq i < p\}) \cup \{ x_{2i}x_{2i+1} \vert 0\leq i \leq p\}
$$
</div>

Est un couplage tel que $\vert M' \vert = \vert M \vert +1$
{% endnote %}
{% details "preuve", "open" %}

Clair puisque $x_0$ et $x_{2p+1}$ sont libres.

{% enddetails %}

Comme on s'y attend, la réciproque est également vraie :

{% note "**Proposition**" %}
Soit $G=(V, E)$ un graphe et $M$ un de ses couplages.

S'il existe n'existe pas de chemin augmentant alors $M$ est un coupage maximum.

{% endnote %}
{% details "preuve", "open" %}

Soit $M$ (en vert) un couplage et $M^\star$ (en rouge un couplage optimal). Si $xy \in M$ et $xy' \in M^\star$ on est dans un des deux cas suivant :

![couplage optimal](couplage-opt-1.png)

Et les autres voisins de $x$ (les arêtes en pointillées) ne sont ni dans $M$ ni dans $M^\star$

De plus si l'arête $xy$ est dans un seul couplage ($M$ ou $M^\star$), au moins une de ses extrémité est couverte par l'autre couplage, sinon les deux sommets $x$ et $y$ seraient libre pour lui et $xy$ serait un chemin augmentant.

Soit alors le graphe $G'=(V, M \cup M^\star)$. Les remarques précédentes  est alors tel que tout sommet est au plus de degré 2 : ses composantes connexes sont soit des chemins soit des cycles alternants.

On conclut la preuve en remarquant que le fait qu'ils soient alternants impose que les cycles et les chemins soient de longueur pairs :

- les cycle car sinon on a deux arêtes du même couplage  qui se suivent
- les chemins sinon il existerait un chemin augmentant pour l'un ou l'autre couplage.

Si par exemple aucune des extrémité du chemin ci dessous ne se prolonge (qu'il y ait ou pas des voisins), alors il existe un chemin augmentant pour pour le couplage rouge :

![couplage optimal](couplage-opt-2.png)

La parité des cycles et des chemins montre que $\vert M^\star\vert = \vert M\vert$.

{% enddetails %}

On a alors l'équivalence suivante :

{% note "**Proposition (Berge)**" %}
Soit $G=(V, E)$ un graphe et $M$ un de ses couplages.

$M$ est maximum si et seulement si il existe n'existe pas de chemin augmentant.

{% endnote %}
