---
layout: layout/post.njk
title: Couplages de poids maximum bi-parti

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Le problème que l'on veut maintenant résoudre est de trouver un couplage maximum de poids maximum dans les graphes bi-partis. Par exemple en reprenant l'exemple du transport amoureux, on peut quantifier l'amour entre les différents héros de roman et chercher, par tous les couplages maximaux ceux qui maximisent le contentement.

On peut alors, sans perte de généralité se restreindre à la recherche des couplage parfait de poids maximum de $K_{n,n}$ puisqu'il suffit de mettre des poids nuls pour chercher des couplages maximaux dans des graphes bi-partis nom complets.

{% note "**Problème du couplage biparti de poids maximum**" %}
Soit $K_{n,n}=(V, E)$ le graphe biparti complet valué par une fonction de préférence $p:E\to \mathbb{R}^+$.

On cherche un couplage parfait $M$ tel que **_le poids du couplage_** $p(M) = \sum_{xy\in M}p(xy)$ soit maximum.
{% endnote %}

Notez que l'on sait déjà résoudre ce problème par une modélisation part flot et en cherchant un flot max de coût maximum. Nous allons voir ici une autre méthode appelé primal/dual qui va se généraliser aux graphes quelconques.

## Dualité couverture/couplage

On va généraliser ici [le théorème de König-Egerváry](../couplage-bi-parti/#König-Egerváry){.interne} pour montrer que couverture de poids minimal va être égal à couplage de poids maximal. Cette dualité rappelle la dualité coupe minimale et flot maximum.

{% note "**définition**" %}
Une **_couverture valuée_** d'un graphe $G=(V, E)$ valué par $p$ est une fonction $c:V\to \mathbb{R}^+$ telle que : $c(x) + c(y)\geq p(xy)$ pour tout $xy \in E$.

Le **_coût_** d'une couverture valué est $c(V) = \sum_{x\in V}c(x)$.
{% endnote %}

{% note "**Proposition**" %}
Soit $G=(v, E)$ un graphe valué par $p$, $c$ une de ses couverture valuée et $M$ un de ses couplages. On a :

<div>
$$
c(V) \geq p(M)
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Pour toute arête $xy$ de $M$ on a $c(x)+c(y)\geq p(xy)$ et comme chaque sommet apparaît au plus une fois dans le couplage on a bien l'inégalité demandée.
{% enddetails %}

> TBD égalité si optimalité sans avoir besoin de l'algorithme ?

## Résolution par Primal/Dual

Le principe de l'algorithme que l'on va utiliser pour résoudre le problème utilise le principe de dualité entre couverture et couplage pour les graphes bipartis et implémente une méthode fondamentale en optimisation appelée primal/dual (très utilisée en programmation linéaire et qui s'applique à de nombreux autres cas, comme ici) : une solution augmente pendant que l'autre diminue, la solution étant trouvée lorsque les deux coïncident.

L'algorithme va petit à petit augmenter un couplage en diminuant une couverture valuée jusqu'à arriver à une valuation égale ce qui prouvera l'optimalité.

### Algorithme

- Donnée : une valuation $p$ du graphe biparti complet $K_{n,n} =(A\cup B, E)$ (avec $A$ et $B$ ses 2 stables)
- algorithme
   1. on note $c$ la valuation des sommets telle que :
      - $c(x) = \max(\\{ p(xy) \vert xy \in E \\})$ si $x\in A$
      - $c(x) = 0$ si $x\in B$
   2. soit $G[c] = (A\cup B, E[c])$ le graphe tel que $xy \in E$ si et seulement si $c(x) + c(y) - p(xy) = 0$
   3. Soit $M$ un couplage maximum de $G[c]$
   4. **si** $M$ couvre $A$ **rendre** $M$ et $c$
   5. soit $C$ une couverture de taille $\vert M \vert$. On pose :
      - $A' = A \cap C$
      - $B' = B \cap C$
      - $\lambda = \min(\\{c(x) + c(y) - p(xy) \vert x\in A\backslash A', y\in B\backslash B' \\})$
      - $c(x) = c(x) -\lambda$ si $x \in A\backslash A'$
      - $c(x) = c(x)  + \lambda$ si $x \in B\backslash B'$
   6. retour à l'étape 2.

### Optimalité

L'algorithme va forcément trouver un couplage parfait car à chaque étape $G[c]$ va avoir strictement plus d'arête :

- si $c(x) + c(y) - p(xy) = 0$ à une étape donné c'est vrai aussi à l'étape suivante
- à l'étape 5. aucune arête $xy$ avec $x\in A\backslash A'$ et $y \in B\backslash B'$ n'est dans $G[c]$, ce qui implique que $\lambda > 0$

De plus, à la fin on a clairement que $c(A\cup B) = p(M)$ ce qui montre que le couplage est bien de poids maximum et la couverture valuée de poids minimum.

### Complexité

Tout ce fait de façon polynomiale puisque :

- l'on peut trouver polynomialement un couplage de taille maximum dans un graphe bi-parti
- l'on peut trouver polynomialement une couverture de taille minimum dans un graphe bi-parti à partir d'un de ses couplages de taille maximum

## Méthode hongroise

{% lien %}

- [Méthode hongroise](https://www.youtube.com/watch?v=fMAmtE0UyzI)
- [Algorithme hongrois](https://fr.wikipedia.org/wiki/Algorithme_hongrois)

{% endlien %}

La méthode hongroise est l'application de la méthode du primal dual en utilisant des matrices de coûts, sans aucune considération de graphes. Elle se décrit plus facilement lorsque l'on cherche à minimiser le coût plutôt que de maximiser la satisfaction et c'est pourquoi nous la décrirons ainsi :

{% note "**Problème**" %}
Soit une matrice carrée $C = (c_{i, j})_{1\leq i \leq n, 1\leq i \leq m}$ de coût. On cherche à associer chaque ligne (une heroine de roman, un ouvrier, etc) à une colonne (un héros de roman, une tâche, etc) de telle sorte que la somme des coûts choisis soit minimal.
{% endnote %}

Ce problème s'écrit facilement comme la recherche d'un couplage parfait dans $K_{n, n}$ à coût minimal.

Si l'on cherche à maximiser des préférences rangées dans une matrice $P = (p_{i, j})_{1\leq i \leq n, 1\leq i \leq m}$, il suffit de considérer la matrices $C = (K - p_{i, j})_{1\leq i \leq n, 1\leq i \leq m}$, avec $K = \sum_{u, v}p_{u, v}$. Comme on cherche un couplage parfait son poids sera de $nK-\sum_{im j /in I} p_{i, j}$ ce qui correspond bien à la maximisation des préférences.

### Algorithme de la méthode hongroise

> TBD pourquoi est-ce que le choix des 0 à encadrer marche (prendre le min) ?

{% info %}

On reprend ici l'exemple de <http://optimisons.free.fr/Cours%20M%C3%A9thode%20Hongroise.pdf> qui est une version un peut différente de celle de Wikipédia pour le choix des 0 à encadrer.

{% endinfo %}

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
17&15&9&5&12\\
\hline
16&16&10&5&10\\
\hline
12&15&14&11&5\\
\hline
4&8&14&17&13\\
\hline
13&9&8&12&17\\
\hline
\end{array}
$$
</div>

#### 0. Créations de zéros

1. pour chaque ligne de $C$, prendre le plus petit élément et le soustraire à l’ensemble de la ligne.
2. pour chaque colonne de $C$, prendre le plus petit élément et le soustraire à l’ensemble de la colonne.

{% info %}
On est maintenant assuré d'avoir au moins un 0 par ligne et par colonne.
{% endinfo %}

Cette étape se réalise en $\mathcal{O}(n^2)$ opérations.

Après l'étape sur les lignes :

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
12&10&4&0&7\\
\hline
11&11&5&0&5\\
\hline
7&10&9&6&0\\
\hline
0&4&10&13&9\\
\hline
5&1&0&4&9\\
\hline
\end{array}
$$
</div>

Puis après l'étape sur les colonnes :

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
12&9&4&0&7\\
\hline
11&10&5&0&5\\
\hline
7&9&9&6&0\\
\hline
0&3&10&13&9\\
\hline
5&0&0&4&9\\
\hline
\end{array}
$$
</div>

#### 1. Encadrer et barrer des zéros

On utilise deux marques différentes :

- **_encadrer_** un zéro de la matrice
- **_barrer_** un zéro de la matrice

1. on cherche une ligne avec le moins de 0 non barrés ou encadré
2. on encadre un de ses zéros non barré
3. on barre tous les autres zéros sur la ligne ou la colonne du zéro encadré

Si à la fin de cette étape on a encadré $n$ zéros c'est qu'on on a encadré un 0 par ligne et par colonne et on a trouvé une solution optimale $I$ qui consiste aux $n$ couples lignes colonnes des 0 encadrés.

> TBD pourquoi est-ce que l'on trouve couplage max ? Est lié au [théorème de König-Egerváry](../couplage-bi-parti/#König-Egerváry){.interne}

{% info %}

À la fin de cette itération :

- ne peut pas barrer de 0 encadré,
- ne peut encadrer qu'au maximum un 0 par ligne et par colonne,
- pour tout zéro barré, il existe un zéro encadré soit sur sa ligne soit sur sa colonne

{% endinfo %}

Cette étape se réalise en $\mathcal{O}(n^2)$ opérations.

On commençant par créer un tableau $T_L$ de taille $n+1$ contenant le nombre de zéros non barrés ou encadré de chaque ligne en parcourant toute les cases de la matrice ce prétraitement se fait en $\mathcal{O}(n^2)$ opérations.

Puis on répète au pire $\mathcal{O}(n)$ fois les 3 opérations (choix de la ligne en prenant le min de $T_L$, barrage et encadrement des 0) qui s'effectuent chacune en $\mathcal{O}(n)$. Il faut aussi mettre à jour $T_L$, ce qui se fait également en $\mathcal{O}(n)$ opérations.

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
12&9&4&\cellcolor{gray}0&7\\
\hline
11&10&5&\cancel{0}&5\\
\hline
7&9&9&6&\cellcolor{gray}0\\
\hline
\cellcolor{gray}0&3&10&13&9\\
\hline
5&\cellcolor{gray}0&\cancel{0}&4&9\\
\hline
\end{array}
$$
</div>

#### 3. Marquer et barrer des lignes et des colonnes

On va **_marquer_** les lignes et les colonnes de la matrice

1. **_marque_** chaque ligne ne possédant **aucun** _0 encadré_
2. **_marque_** chaque colonne possédant un _0 barré_ sur une _ligne marquée_
3. **_marque_** chaque ligne possédant un _0 encadré_ **dans** une _colonne marquée_

On répète cette étapes (on a besoin que de répéter les paries 2 et 3) jusqu'à ne plus pouvoir marquer de lignes ou de colonnes.

{% info %}

À la fin de cette étape tous les 0 sont :

- soit une ligne non marquée
- soit sur une colonne marquée

{% endinfo %}

Cette étape se réalise aussi $\mathcal{O}(n^2)$ opérations en conservant deux tableaux $T_C$ et $T_L$ de $n+1$ booléens tels que :

- $T_C[i]$ est vrai s'il existe une ligne marquée ayant un zéro barré à la colonne $i$
- $T_L[i]$ est vrai s'il existe une colonne marquée ayant un zéro encadré à la ligne $i$

On initialise ces tableaux en $\mathcal{O}(n^2)$ puisque chaque ligne ou colonne ajoutée mettra à jour ces tableaux en $\mathcal{O}(n)$ opération. Comme on ne peut ajouter une ligne ou une colonne qu'une seule fois, il y aura au pire $\mathcal{O}(n)$ itérations.

<div>
$$
\begin{array}{|c|c|c|c|c|r}
&&&X&&\\
\hline
12&9&4&\cellcolor{gray}0&7&X\\
\hline
11&10&5&\cancel{0}&5&X\\
\hline
7&9&9&6&\cellcolor{gray}0\\
\hline
\cellcolor{gray}0&3&10&13&9\\
\hline
5&\cellcolor{gray}0&\cancel{0}&4&9\\
\hline
\end{array}
$$
</div>

#### 4. Mise à jour

On sépare les cases de la matrices en 3 :

- 2B : les cases qui sont sur une ligne non marquée et sur une colonne marquée
- 1B : les cases qui sont sur une ligne non marquée ou exclusivement sur une colonne marquée
- 0B : les cases qui sont sur une ligne marquée et sur une colonne non  marquée

Soit $\lambda >0 $ la plus petite valeur de des cases 0B.

1. On supprime cette valeur de toutes les cases 0B
2. On ajoute cette valeur de toutes les cases 2B

{% info %}

À la fin de cette étape, la nouvelle matrice on a strictement plus de 0 que la précédente.

{% endinfo %}

Cette étape est aussi clairement en $\mathcal{O}(n^2)$ opérations.

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
8&5&0&0&3\\
\hline
7&6&1&0&1\\
\hline
7&9&9&10&0\\
\hline
0&3&10&17&9\\
\hline
5&0&0&8&9\\
\hline
\end{array}
$$
</div>

#### 5. retour

On supprime toutes les marques (de cases, de lignes et de colonnes) et on recommence à l'étape 1 avec la nouvelle matrice

Dans notre exemple, la prochaine étape 2 va s'arrêter sur :

<div>
$$
\begin{array}{|c|c|c|c|c|}
\hline
8&5&\cellcolor{gray}0&0&3\\
\hline
7&6&1&\cellcolor{gray}0&1\\
\hline
7&9&9&10&\cellcolor{gray}0\\
\hline
\cellcolor{gray}0&3&10&17&9\\
\hline
5&\cellcolor{gray}0&0&8&9\\
\hline
\end{array}
$$
</div>

### Complexité totale de la méthode hongroise

Chaque étape se fait en $\mathcal{O}(n^2)$ opérations  et il faut au pire les répéter $\mathcal{O}(n^2)$ fois (jusqu'à ce qu'il n'y ait plus que des 0). La complexité totale est donc en $\mathcal{O}(n^4)$, qui est quadratique par rapport à la taille des données (une matrice $n\times n$).
