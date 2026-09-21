---
layout: layout/post.njk
title: Chemin et cycles Hamiltonien

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



<div id="definition-graphe-hamiltonien"></div>
{% note2 "**Définition**" %}
Un graphe (_resp._ graphe dirigé) admet un **_cycle_** (_resp._ **_circuit_**) **_hamiltonien_** s'il existe un cycle (_resp._ un circuit) élémentaire passant par tous les sommets.

Un **_graphe est hamiltonien_** s'il possède un cycle hamiltonien.
{% endnote2 %}

On doit ce problème au mathématicien [Hamilton](https://en.wikipedia.org/wiki/William_Rowan_Hamilton) qui a proposé de le résoudre [sous la forme d'un casse tête](https://en.wikipedia.org/wiki/Icosian_game) qu'il commercialisa et correspond à l'exercice suivant :

{% exercice "Jeu du dodécaèdre" %}
Montrer que le graphe suivant possède un cycle hamiltonien
![dodécaèdre](dodécaèdre.png)
{% endexercice %}
{% details "corrigé" %}
Il existe plusieurs moyen de trouver un cycle hamiltonien. Le plus simple est de décomposer le graphe en parties qu'il faudra traverser un nombre paire de fois. Dans le cas du dodécaèdre on peut par exemple séparer le graphe en 3 :
![dodécaèdre](dodécaèdre_hamilton_couleurs.png)

Ici ça va aller vite. On commence par essayer de renter et sortir qu'une seule fois pour les sommets verts. On est alors que le cas suivant :

![dodécaèdre](dodécaèdre_hamilton_couleurs2.png)

Il nous reste à connecter les jaunes et les rouges, c'est la seule configuration possible à 2 arêtes :

![dodécaèdre](dodécaèdre_hamilton_couleurs3.png)

Et au final le cycle hamiltonien :

![dodécaèdre](dodécaèdre_hamilton.png)
{% enddetails %}

La définition suivante est également très utilisée :

{% note2 "**Définition**" %}
Un graphe (_resp._ graphe dirigé) admet un **_chemin hamiltonien_** s'il existe un chemin élémentaire passant par tous les sommets.

{% endnote2 %}

Tous les graphes ne possèdent cependant pas de cycle hamiltonien. Par exemple le graphe suivant, appelé [graphe de Petersen](https://fr.wikipedia.org/wiki/Graphe_de_Petersen) (que l'on est amené à revoir), n'en possède pas :

![graphe de Petersen](petersen.png)

{% info "tiré de Wikipédia" %}
Donald Knuth explique dans The Art of Computer Programming que le graphe de Petersen est _«une configuration remarquable qui sert de contre-exemple à de nombreuses prédictions optimistes sur ce qui devrait être vrai pour tous les graphes3 »_.
{% endinfo %}
{% exercice %}
Montrez que le graphe de Petersen ne possède pas de cycle hamiltonien.
{% endexercice %}
{% details "corrigé" %}
S'il suffit d'exhiber un exemple pour montrer qu'un graphe est hamiltonien, pour montrer qu'il ne l'est pas il faut en démontrer l'impossibilité.

On peut utiliser pour cela séparons les sommets du graphe en deux parties : les sommets rouges et les sommets verts :

![graphe de Petersen](petersen2.png)

Supposons qu'il existe un cycle hamiltonien $x_1\dots x_n$. Soit $x_ix_{i+1}$ est une arête dont les sommets sont de couleurs différentes. Si $j>i$ est le plus petit entier tel que $x_jx_{j+1}$ est une arête dont les sommets sont de couleurs différentes, alors la couleur de $x_{i+1}$ est identique à celle de $x_j$ et donc il ne peut y avoir qu'un nombre pair d'arêtes dont les sommets sont de couleurs différentes. Soit 0, 2 ou 4 arêtes ce qui, par symétrie, suppose qu'un des quatre graphes ci-après possède aussi un cycle hamiltonien avec les arêtes vertes (jonction entre couleur et sommets de degré 2), ce qui est impossible :

| :-: | :-: |
|![graphe A](./petersen-a.png)|![graphe B](./petersen-b.png)|
|![graphe C](./petersen-c.png)|![graphe D](./petersen-d.png)|

{% enddetails %}

Le problème du cycle ou du chemin hamiltonien est un problème classique en théorie des graphe et est présent dans nombre de problèmes concrets. C'est en particulier [le problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) qui est la base de toute optimisation de tournée ou de nombre de problèmes liés au transport.


## Chemin et cycles

Trouver un chemin ou un cycle hamiltonien sont deux problèmes similaires et que l'on peut résoudre l'un par l'autre. Montrons le en commençant par montrer que la recherche d'un chemin hamiltonion est quasi-identique à la recherche d'un cycle hamiltonien :

{% note "**Proposition**" %}
Trouver un chemin hamiltonien d'un graphe $G = (V, E)$ est équivalent à trouver un cycle hamiltonien du graphe $G' = (V \cup \\{\omega \\}, E \cup \\{ \omega x \mid x \in V\\})$.
{% endnote %}
{% details "preuve", "open" %}

- si $x_1 \dots x_n$ est un chemin hamiltonien de $G$ alors $\omega x_1 \dots x_n\omega$ est un cycle hamiltonien de $G'$
- si $\omega x_1 \dots x_n\omega$ est un cycle hamiltonien de $G'$ alors $x_1 \dots x_n$ est un chemin hamiltonien de $G$
{% enddetails %}

La réciproque est également vrai :

{% note "**Proposition**" %}
Trouver un cycle hamiltonien d'un graphe $G = (V, E)$ est équivalent à trouver un chemin hamiltonien du graphe $G' = (V', E')$ avec :

- $V' = (V \backslash \\{x^\star\\}) \cup \\{x_1, x_2, p_1, p_2\\}$ avec $x^\star$ un sommet quelconque de $V$,
- $E' = (E \backslash \\{ x^\star y \mid x^\star y \in E \\}) \cup \\{ x_i y \mid 1\leq i \leq 2, x^\star y \in E \\} \cup \\{x_1p_1, x_2, p_2\\}$
{% endnote %}
{% details "preuve", "open" %}

- si $x^\star \dots x^\star$ est un cycle hamiltonien de $G$ alors $p_1 x_1 \dots x_2 p_2$ est un chemin hamiltonien de $G'$
- si $x_1 \dots x_{n'}$ est un chemin hamiltonien de $G'$ alors forcément $\\{x_1, x_{n'}\\} = \\{p_1, p_2\\}$ puisque $\delta(p_1) = \delta(p_2) = 1$. On peut alors sans perte de généralité suppose que le chemin hamiltonien est : $p_1 x_1 y_1 \dots y_{n-1} x_2 p_2$ et $x^\star y_1 \dots y_{n-1} x^\star$ est un cycle hamiltonien de $G$.
{% enddetails %}

Ces résultats se transposent pour les graphes orientés :

{% exercice %}
Montrez que l'on peut résoudre le problème du chemin hamiltonien dans un graphe orienté par la recherche d'un circuit hamiltonien.
{% endexercice %}
{% details "corrigé" %}
On peut comme dans la proposition pour les graphes non orienté ajouter un somment ayant un arc entrant et un arc sortant pour tous les autres sommets.

On peut aussi, si on ne veut pas ajouter d'arc dans les deux direction créer le graphe orienté $G' = (V', E')$ tel que :

- $V' = V \cup \\{x^+, x^- \\}$,
- $E' = E \cup \\{ x^+ y \mid y \in V \\} \cup \\{ x^- y \mid y \in V \\} \cup \\{x^-x^+\\}$

De là :

- au chemin hamiltonien $x_1\dots x_n$ sur $G$ correspondra un circuit hamiltonien $x^+x_1\dots x_nx^-x^+$ sur $G'$
- au cycle hamiltonien $x^-x^+ y_1 \dots y_{n} x^-$ sur $G'$ ($x^+$ et $x^-$ sont forcément voisins puisque $x^-x^+$ est l'unique arête sortante de $x^-$) correspondra le chemin hamiltonien $y_1 \dots y_{n}$ sur $G$  
{% enddetails %}

{% exercice %}
Montrez que l'on peut résoudre le problème du circuit hamiltonien dans un graphe orienté par la recherche d'un chemin hamiltonien.
{% endexercice %}
{% details "corrigé" %}

On procède de la même manière que pour le cas orienté en :

- associant à $x_1$ les arc sortant de $x^\star$ et à $x_2$ les arc entrant,
- ajoutant les sommets $p_1$ $p_2$ avec les arcs $p_1x_1$ et $x_2p_2$.

{% enddetails %}


Selon les cas on préférera traiter un cas ou l'autre mais dans l'absolu ces problèmes sont de même complexité :

{% attention2 "**À retenir**" %}
Les problèmes de recherche d'un chemin ou d'un cycle hamiltonien dans des graphes (orienté ou non) sont identiques : on peut de plus résoudre un problème par un algorithme résolvant l'autre via une transformation linéaire d'une entrée dans l'autre.
{% endattention2 %}

## Densité d'arêtes des graphes hamiltoniens

Lorsque le graphe a beaucoup d'arêtes, il va être facile de trouver des chemin ou cycles/circuit hamiltonien.

{% note "**Proposition (Dirac, 1952)**" %}
Si $G=(V, E)$ est un graphe tel que $\delta(x) \geq \vert V \vert / 2$ pour tout sommet $x\in V$, alors $G$ est hamiltonien (_ie._ admet un cycle Hamiltonien).
{% endnote %}
{% details "preuve", "open" %}

Le graphe $G$ est connexe car s'il ne l'était pas sa plus petite composante connexe serait de taille inférieure ou égale à $\vert V \vert / 2$ et donc les sommets de cette composante ont tous un un degré strictement plus petit que $\vert V \vert / 2$ (on pourrait aussi utiliser [cette propriété](../chemins-cycles-connexite/#prop-connexe){.interne} et le fait que $\vert E \vert = \frac{1}{2}\sum_x\delta(x) \geq \frac{1}{4}\vert V \vert^2>  \frac{1}{2}(\vert V \vert-1)(\vert V \vert-2)$ pour $\vert V \vert \geq 3$).

Soit $C=x_0\dots x_k$ un chemin le plus long dans $G$. Si $x_0x_k \in E$, le cycle est hamiltonien. Sinon en effet, par connexité, il existerait une arête $yx_j$ avec $y\notin C$ et le chemin suivant serait strictement plus long que $C$ : $yx_j\dots x_kx_0\dots x_{j-1}$.

On suppose alors que $x_0x_k \notin E$.

Tous les voisins de $x_0$ et $x_k$ sont dans $C$ sinon on pourrait le prolonger.
De plus si pour tout $x_i$ tel que $x_ix_k \in E$ on a $x_{i+1}x_0 \notin E$, $C$ contiendrait $x_0$, tous les successeurs des voisins de $x_k$ (dont $x_k$ puisque $x_{k-1}x_k$) et il y en a au moins $\vert V \vert / 2$, plus tous les voisins de $x_0$, c'est à dire encore au moins $\vert V \vert / 2$ : $C$ posséderait au moins $\vert V \vert + 1$ élément, ce qui est impossible.

Il existe donc $x_i$ ($0 < i <k$) tel que $x_ix_k \in E$ et a $x_{i+1}x_0 \in E$ : le chemin $x_0\dots x_ix_k\dots x_{i+1} = x'_0\dots x'_k$ est alors de longueur maximum et comme $x'_kx'_0 \in E$ on est ramené au cas précédent et $x'_0\dots x'_kx'_0$ est un cycle hamiltonien.

{% enddetails %}

Et le pendant dirigé :

{% note "**Proposition (Ghouila-Houri, 1960)**" %}
Si $G=(V, E)$ est un graphe orienté tel que $\delta^+(x) + \delta^-(x) \geq \vert V \vert$ pour tout sommet $x\in V$, alors $G$ est hamiltonien (_ie._ admet un circuit Hamiltonien).
{% endnote %}
{% details "preuve", "open" %}

Soit $C$ un circuit de taille maximum de $G$. Commençons par montrer que $l = v(G) \geq n/2 + 1$ (avec $n = v(G)$), en considérant un chemin $x_1\dots x_p$ le plus long dans $G$. Tous les voisins sortants de $x_p$ sont forcément sur ce chemin sinon il ne serait pas de longueur maximum et il y en a au moins $n/2$. le cycle $x_i \dots x_p x_i$ avec $x_i$ le plus petit successeur de x_p$ sur le chemin possède donc au moins $n/2 +1$ sommet.

Soit maintenant $G'$ le graphe $G$ restreint aux sommets qui **ne sont pas** dans $C$ et $v_1\dots v_k$ un de ses chemin de longueur maximum. Comme $k + l \leq n$ on a que $k \leq n/2 -1$. Ceci implique que :

- l'ensemble $S$


{% enddetails %}


> TBD attention ce n'est ps une CNS : exemple du cycle. Juste que s'il y a beaucoup d'arêtes il en existe **forcément** un.

## Tournois

Commençons par un résultat surprenant sur les graphes orientés. S'il est évident que les graphes complets ont tous des chemins hamiltoniens, c'est également le cas pour les tournois !

<div id="tournoi-exercice"></div>
{% exercice %}
Montrez que tout [tournoi](../structure/#definition-tournoi) admet un chemin hamiltonien.
{% endexercice %}
{% details "corrigé" %}

On peut le démontrer par récurrence. Un tournoi à 1 sommet admet un chemin hamiltonien. Si on suppose cela vrai pour tout tournoi à moins de $n$ sommets, soit $T = (V, E)$ un tournoi à $n+1$ sommets.

On prend $x$ un sommet de ce tournoi. Le graphe $T$ privé de $T$ est un tournoi à $n$ sommets. Il existe alors un chemin hamiltonien $c_0\dots c_{n-1}$ dans la restriction de $T$.

Si $xc_{0}$ est un arc de $T$, alors $xc_0\dots c_{n-1}$ est un chemin hamiltonien. Sinon si $c_{n-1}x$ est un arc de $T$, alors $c_0\dots c_{n-1}x$ est un chemin hamiltonien.

Si on est dans aucun des cas précédents, il existe $0 <i<n-1$ tel que $c_{i}x$ et $xc_{i+1}$ sont deux arcs de $T$ : $c_0\dots c_{i}xc_{i+1}\dots c_{n-1}x$ est un chemin hamiltonien de $T$.
{% enddetails %}
{% details "corrigé alternatif" %}
Preuve un peu plus élégante que la précédente.

On peut le démontrer par récurrence. Un tournoi à 1 sommet admet un chemin hamiltonien. Si on suppose cela vrai pour tout tournoi à moins de $n$ sommets, soit $T = (V, E)$ un tournoi à $n+1$ sommets.

On prend $x$ un sommet de ce tournoi. On a alors que $N^+(x) \cup N^-(x) \cup \{ x \} = V$ et que les restrictions de $T$ à $N^+(x)$ ou à $N^-(x)$ restent des tournois et ont strictement moins de $n+1$ sommets.

Il existe alors :

- un chemin hamiltonien $c_0\dots c_k$ dans la restriction de $T$ à $N^+(x)$
- un chemin hamiltonien $c'_0\dots c'_l$ dans la restriction de $T$ à $N^-(x)$

On en conclut que le chemin $c'_0 \dots c'_l x c_0 \dots c_k$ est hamiltonien dans $T$, ce qui termine la preuve par récurrence.

{% enddetails %}

Ce résultat ne se généralise pas aux cycle hamiltonien. Il suffit de considérer le tournoi $G = (\{x_1,\dots, x_n\}, E)$ avec $x_ix_j \in E$ si et seulement si $i< j$. Ce tournoi ne peut clairement posséder aucun circuit.

> TBD il peut même y en avoir beaucoup ! Thm méthode probabiliste : premier exemple.
> TBD existence de ce que l'on cherche avec une forte proba mais impossible à trouver en pratique <https://www.youtube.com/watch?v=4weMmFZSBtI>

## Algorithme

On ne connaît pas d'algorithmes polynomiaux pour trouver un cycle hamiltonien.
> TBD ce qu'on a fait avec ds arêtes pourquoi pas le faire avec des sommets ? Voir la suite du cours (c'est un problème NP complet)

### Exact

> TBD ajouter algo en $2^n2^n$ qui est mieux que n! <https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm>

### Approché sans performance garantie

> TBD parler de 2-opt (dirigé ou pas) et de la 2-approximation si distance sur graphe complet.

### À performance garantie dans un cas particulier

> TBD ALM puis parcours DFS dessus : le parcours DFS et une 2-approximation.




