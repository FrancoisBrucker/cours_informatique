---
layout: layout/post.njk

title: Propriétés

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Comptage des faces

{% note  "**Définition**" %}
Un ensemble $A \subseteq \mathcal{R}^2$ est connexe si pour tous $x, y \in A$ il existe une courbe $\gamma$ telle que :

- $\gamma(0) = x$, $\gamma(1) = y$
- $\gamma([0, 1]) \subseteq A$
{% endnote %}
{% note  "**Définition**" %}
Les **_faces_** d'un dessin planaire $(f, g)$ d'un graphe connexe $G=(V, E)$ sont les régions connexes de $\mathcal{R}^2 \backslash (\cup_{xy \in E}g(xy)([0, 1]))$.
{% endnote %}

Les faces sont bien ce que l'on pense qu'elles sont, si on n'oublie pas la face extérieur (infinie). Le graphe suivant à donc 3 faces :

![faces](./faces.png)

{% note  "**Proposition (formule d'Euler)**" %}
Soit $G = (V, E)$ un graphe et $(f, g)$ un de ses dessins planaires. Si $F$ est son nombre de faces, $n$ son nombre de sommets et $m$ son nombre d'arêtes, on a l'égalité :

<div>
$$
F = m - n + 2
$$
</div>
{% endnote %}
{% details "preuve", "open" %}
> TBD cours papier
{% enddetails %}

La formule d'Euler montre que le nombre de faces ne dépend pas de son dessin ! On peut donc parler du nombre de faces d'un graphe planaire indépendamment de son dessin planaire. L'exemple ci-après montre deux dessins planaires différents de $K_4$, les faces sont différentes, mais leur nombre (3) est le même :

![faces différentes](./faces-différentes.png)

## Degrés des graphes planaires

La formule d'Euler permet de borner le nombres d'arêtes d'un graphe planaire :

{% note  "**Proposition**" %}
Soit $G = (V, E)$ un graphe planaire à $n\geq 3$ sommets et $m$ arêtes. On a l'inégalité :

<div>
$$
m \leq 3\cdot n - 6
$$
</div>
{% endnote %}
{% details "preuve", "open" %}
Pour chacune des $F$ faces d'un dessin planaire de $G$, on note $f_i$ le nombre d'arêtes formant la frontière de la face $i$. Comme chaque arête est sur la frontière d'exactement 2 faces, on a $\sum f_i = 2m$ et comme chaque face a au moins 3 arêtes il vient l'inégalité : $3F\leq \sum f_i = 2m$. En injectant la formule d'Euler dans cette inégalité on obtient $3(m - n + 2)\leq 2m$ d'où le résultat.

{% enddetails %}

Un graphe planaire a donc très peu d'arêtes, au pire 3 fois plus que de sommets. Ceci implique qu'il existe un sommet de petit degré :

{% note  "**Proposition**" %}
Soit $G = (V, E)$ un graphe planaire. Il existe un sommet $x$ de degré inférieur ou égal à 5.
{% endnote %}
{% details "preuve", "open" %}

Si tous les sommets avaient un degré strictement plus grand que 5 on aurait : $2\cdot m = \sum\delta(x) \geq 6 \cdot n$, donc $m\geq 3\cdot n$. Ceci est cependant impossible puisque $m \leq 3\cdot n - 6 < 3\cdot n$.
{% enddetails %}

## Triangulation

Le nombre maximum d'arêtes pour un graphe planaire est m = 3n-6 dans ce cas la, toutes les faces sont des triangles.

> TBD <https://facultyweb.kennesaw.edu/mlavrov/courses/graph-theory/lecture21.pdf>

Donc trianguler une représentation planaire triangule toutes les autres, même si les faces sont différentes !

> TBD comment trianguler : <https://fr.wikipedia.org/wiki/Triangulation_d%27un_polygone>

## Nombre minimum de croisements de graphes non planaires

{% lien %}
<https://en.wikipedia.org/wiki/Crossing_number_inequality#Statement_and_history>
{% endlien %}

Enfin, une dernière propriété sur les graphes nom planaires.

{% note  "**Définition**" %}
POur tout graphe $G$, on note $\text{cr}(G)$ le nombre minimum de croisements d'arêtes qu'un dessin de $G$ peut avoir.
{% endnote %}

Les graphes planaires sont bien sur les graphes $G$ tels que $\text{cr}(G) = 0$. Et $\text{cr}(K_5) = 1$ (il n'est pas planaire et on l'a dessiné avec uniquement 1 croisement d'arête). Pour chaque graphe, il faudrait pouvoir trouver tous ses dessins possibles et compter pour chacun le nombre de croisements, ce qui est impossible à faire en pratique.

Il existe cependant des bornes dépendant uniquement du nombre de sommets et d'arêtes. Par exemple :

{% exercice %}
Montrez que pour tout graphe $G$ à $n$ sommets et $m$ arêtes on a $\text{cr}(G)\geq m-3n$.
{% endexercice %}
{% details "corrigé" %}
On sait que $m \leq 3n-6$ pur un graphe planaire. Tout graphe avec plus d'arêtes va donc avoir au moins 1 croisement par arête surnuméraire : on peut itérativement  supprimer une arête qui possède un croisement (il en existe forcément une si $m-3n+6>0$).

{% enddetails %}

Mais on peut faire bien mieux en utilisant la méthode probabiliste ! On a en effet la proposition suivante :

{% note  "**Proposition**" %}
Pour tout graphe $G = (V, E)$ à $n$ sommets et $m$ arêtes tel que $m\geq 4\cdot n$ on a :

<div>
$$
\text{cr}(G) \geq \frac{1}{64}\frac{m^3}{n^2}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Si on peut prouver cette inégalité en utilisant la méthode probabiliste, il faut pouvoir associer à un graphe $G=(V, E)$ un autre graphe, $H=(V', E\vert_{V'})$, aléatoire tel que $V'$ est un sous-ensemble de $V$ où tout élément a été choisi indépendamment des autres avec une propriété $p$. On a alors :

- $\mathbb{E}[v(H)] = p\cdot n$
- $\mathbb{E}[e(H)] = p^2\cdot m$

Si on dessine $H$ en prenant la restriction d'un dessin de $G$ minimisant son nombre de croisements. Le nombre moyen de croisements de ce dessin pour $H$ vaut $p^4\text{cr}(G)$ puisque chaque croisement est un formé de 2 arêtes de $G$ qui ont chacune une probabilité $p^2$ d'être dans $H$.

De là si $C(H)$ est le nombre de croisement de la restriction à $H$ d'un dessin de $G$ minimisant les croisement, on a : $C(H) \geq \text{cr}(H) \geq e(H) - 3 \cdot v(H)$. Donc par linéarité de l'espérance on a également :  $ \mathbb{E}[C(H)]\geq \mathbb{E}[e(H)] - 3 \cdot \mathbb{E}[v(H)]$ c'est à dire :

<div>
$$
p^4\text{cr}(G)\geq p^2\cdot m - 3\cdot p\cdot n
$$
</div>

Et donc :

<div>
$$
\text{cr}(G)\geq \frac{p\cdot m - 3\cdot n}{p^3}
$$
</div>

Comme on cherche une borne min, il faut maximiser la fonction $f(p)=\frac{p\cdot m - 3\cdot n}{p^3}$, ce qui est le cas pour $p = \frac{9}{2}\frac{n}{m}$, pour simplifier on prend $p=4n/m$, ce qui impose $m\geq 4n$ et donne le résultat.
{% enddetails %}

> TBD exemple.
