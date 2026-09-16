---
layout: layout/post.njk
title: "Réduction de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une méthode classique de résoudre un problème algorithmique ($P_1$) est de le transformer en un autre problème ($P_1$) que l'on sait résoudre ($S_2$) puis de transformer sa solution en une solution du problème initial ($S_1$) :

<div>
$$
\begin{array}{ccc}
P_1 & \rightarrow & P_2\\
\Downarrow &  & \Downarrow\\
S_1 & \leftarrow & S_2
\end{array}
$$
</div>

La formalisation de cette opération s'appelle [une réduction](<https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)>) et peut prendre plusieurs formes. Nous en expliciterons certaines qui nous permettrons de :

1. comparer et classer les problèmes algorithmiques.
2. calculer ou estimer des complexités

{% info %}
Nous ne parlerons pas ici de la [Réduction de Turing](https://en.wikipedia.org/wiki/Turing_reduction), trop générale et demandant des connaissances comme [les machines à oracles](https://fr.wikipedia.org/wiki/Oracle_(machine_de_Turing)) dont nous ne parlerons pas dans ce cours d'algorithmie.
{% endinfo %}

Commençons par deux exemples.

## Exemples de réduction

Une réduction permet d'utiliser un problème pour en résoudre un autre. En ce sens, le premier problème est plus général que le second.

### Min et max d'un tableau d'entiers relatifs

Le problème de trouver un élément min et celui permettant de trouver un élément max d'un tableau d'entiers relatif sont liés. Si l'on cherche $\min(T)$ le minimum d'un tableau d'entiers relatifs $T$, en posant $T'$ le tableau de même longueur que $T$ tel que $T'[i] = -T[i]$ pour tout indice $i$ alors $\max(T')$ le maximum de $T'$ vaut $-\min(T)$.

La réduction entre les deux problèmes est constituée de deux algorithme :

- le premier, $E$, qui transforme une entrée du problème min (le tableau $T$) en une entrée du problème max (le tableau $T' =  E(T)$)
- le second, $S$,  qui associe une solution du problème max avec l'entrée transformée ($\max(T') = \max(E(T))$) en une solution du premier problème ($\min(T) = S(\max(E(T)))$).

On peut alors résoudre le problème de la recherche du min d'un tableau d'entier relatifs avec un algorithme permettant de résoudre le problème de la recherche du max d'un tableau d'entier relatifs : le problème du min est en ce sens un cas particulier du problème du max.

{% exercice %}
Montrez la réciproque : on peut résoudre le problème de la recherche du max d'un tableau d'entier relatifs avec un algorithme permettant de résoudre le problème de la recherche du min d'un tableau d'entier relatifs.
{% endexercice %}
{% details "corrigé" %}
On fait exactement la même chose.
{% enddetails %}

Cette procédure permet non seulement de résoudre un problème à partir d'un autre mais donne également des bornes sur la complexité du problème. Dans notre cas la complexité du problème $\min(T)$ est inférieure à la somme des complexités de :

1. transformer le tableau $T$ et $E(T)$, ici $\mathcal{O}(\vert T \vert)$,
2. la complexité du problèmes du maximum, ici encore $\mathcal{O}(\vert T \vert)$ ([on l'a vu](../complexité-problème/#problème-max-tableau-complexité){.interne}),
3. la complexité du passage de la solution du second problème à une solution du premier problème, ici $\mathcal{O}(1)$.

Comme la complexité de la recherche du minimum d'un tableau est au moins linéaire (il faut forcément regarder tous les éléments de $T$ avant de décider), on en déduit que sa complexité est bien linéaire.

### Min et max d'un tableau d'entiers positifs

Si l'on cherche maintenant à résoudre le problème de trouver un élément min en utilisant un algorithme permettant de trouver un élément max d'un tableau d'entiers positif, l'algorithme $\max(T)$, on ne peut plus prendre juste l'opposé du tableau initial.

Mais on peut utiliser l'algorithme $\max(T)$ plusieurs fois et poser $T'$ comme étant un tableau de même taille que $T$ tel que $T'[x] = \max(T)-T[x]$. Le min est alors : $\min(T) = \max(T)-\max(T')$.

Cette procédure, un peu plus complexe que la précédente, permet à nouveau de résoudre le problème du min avec le problème du max. 

## Définition

{% note2 "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction_** de $P_1$ en $P_2$ est un couple d'algorithmes $A_{1\rightarrow 2}$ et $A_{2\rightarrow 1}$ tels que :

- Si $E_1$ est une entrée du problème $P_1$ alors $A_{1\rightarrow 2}(E_1)$ est une entrée de du problème $P_2$
- Si $S_2$ est une solution au problème $P_2$ avec $A_{1\rightarrow 2}(E_1)$ comme entrée alors $A_{2\rightarrow 1}(E_1, S_2)$ est une solution au problème $P_1$ d'entrée $E_1$

Les réductions forment un ordre sur les problèmes algorithmiques : s'il existe une réduction de $P_1$ en $P_2$ on notera $P_1 \leq P_2$.
{% endnote2 %}

La définition formelle ci-dessus est équivalente à :

{% attention2 "**À retenir**" %}
Une réduction de $P_1$ en $P_2$ signifie  que l'on utilise le problème $P_2$ (potentiellement un nombre constant de fois) pour résoudre le problème $P_1$.
{% endattention2 %}

Pour qu'une réduction ait un sens, il faut que les passages entre les problème $P_1$ et $P_2$ soit de faible complexité. En effet, en notant $C_{P_1}(n)$, $C_{1\rightarrow 2}(n)$, $C_{P_2}(n)$ et $C_{2\rightarrow 1}(n)$ les complexités des algorithmes $P_1$, $A_{1\rightarrow 2}$, $P_2$ et $A_{2\rightarrow 1}$ respectivement on a :

<div>
$$
C_{P_1}(n) = C_{1\rightarrow 2}(n) + C_{P_2}(n') + C_{2\rightarrow 1}(n'' + n)
$$
</div>

Avec :

- $n$ la taille de l'entrée $E_1$ de $P_1$
- $n'$ la taille de l'entrée de $P_2$
- $n''$ la taille de la sortie de l'algorithme $P_2$

Notez bien que comme on cherche à borner la complexité du problème $P_1$, toutes nos complexité doivent dépendre uniquement de $n$ qui est la taille de l'entrée de $P_1$. Selon les complexités de l'aller retour entre $P_1$ et $P_2$ cela va être plus ou moins facile. On défini alors :

<span id="définition-réduction-polynomiale"></span>

{% note2 "**Définition**" %}

Une **_réduction polynomiale_** du problème algorithmique $P_1$ au problème algorithmique $P_2$ est une réduction où les passages du problème $P_1$ au problème $P_2$ et du problème $P_2$ au problème $P_1$ sont polynomiales.

{% endnote2 %}

On peut sur le même schéma définir une **_réduction linéaire_** (les passages sont de complexité linéaire), **_reduction logarithmique_** (les passages sont de complexité logarithmique par rapport à la aille de l'entrée), etc. Borner les passages nous permet de faire des démonstration de complexité en utilisant les complexités du problème $P_2$. Par exemple :

{% exercice %}
Donnez une réduction en temps constant du problème de recherche du maximum dans un tableau d'entiers au problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

- même entrée pour l'algorithme du max et du tri : $\mathcal{O}(1)$
- la sortie du max est le plus grand élément de la sortie du tri : $\mathcal{O}(1)$

{% enddetails %}

La réduction polynomiale permet de borner la complexité du problème $P_1$ si la complexité du problème $P_2$ est également polynomiale :

{% note "**Proposition**" %}
S'il existe une réduction polynomiale entre $P_1$ et $P_2$ et que la complexité du problème $P_2$ est polynomiale, alors la complexité du problème $P_1$ est également polynomiale.

{% endnote %}
{% details "preuve", "open" %}

En reprenant les notations précédentes :

- aller du problème $P_1$ au problème $P_2$ avec une complexité $C_{1\rightarrow 2}(n) = \mathcal{O}(n^k)$
- résoudre $P_2$ avec une complexité $C_{P_2}(f(n))$. Comme le problème $P_2$ est polynomial on a $C_{P_2}(f(n)) = \mathcal{O}(f(n)^{k'})$ et comme la taille de la sortie de l'algorithme $A_{1\rightarrow 2}$ est au plus $\mathcal{O}(n^k)$ on a : $C_{P_2}(f(n)) = \mathcal{O}(n^{k\cdot k'})$
- revenir au problème $P_1$ avec une complexité $C_{2\rightarrow 1}(g\circ f(n) + n)$. Comme cette complexité est aussi polynomiale, disons $C_{2\rightarrow 1}(g\circ f(n) + n) =  \mathcal{O}(f(n)^{k''})$, on a au final que $C_{2\rightarrow 1}(g\circ f(n)) =  \mathcal{O}(n^{k\cdot k'\cdot k''})$

La complexité totale est alors de : $\mathcal{O}(n^{k\cdot k'\cdot k''})$ ce qui est toujours polynomial.

{% enddetails %}

La proposition précédente donne le but de toute réduction. Si la complexité du problème $P_2$ est identique au type de réduction (polynomiale, linéaire, logarithmique, etc) **alors** la complexité du problème $P_1$ l'est aussi : c'est donc un outil de preuve de complexité puissant.

Entraînons nous sur un petit exemple qui va nécessiter d'utiliser et la sortie de $P_2$ et l'entrée $E_1$ pour trouver $S_1$ :

{% exercice %}
Montrez que le problème de la recherche de doublon dans un tableau d'entiers (on cherche deux indices différents de même valeur) est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

- même entrée pour l'algorithme du max et du tri : $\mathcal{O}(1)$
- on parcourt le tableau trié jusqu'à trouver deux éléments successifs égaux : $\mathcal{O}(n)$ avec $n$ taille du tableau en entrée. On note $\alpha$ cette valeur.

Il faut ensuite retrouver, **dans le tableau d'entrée** 2 indices différents valant la valeur $\alpha$, ce qui peut se faire en $\mathcal{O}(n)$ en parcourant tous les indices de $T$ :

```pseudocode

a, b <- 0
pour chaque i de [0 .. T.longueur]:
  si T[i] == α:
    b <- a
    b <- i

rendre b, a
```

Comme on sait que la valeur $\alpha$ va apparaître (au moins) 2 fois, le code précédent va donner deux indice différents de $T$ dont la valeur vaut $\alpha$.

{% enddetails %}

## Exemples et exercices

### Produit et carré

{% exercice %}
Montrer que le problème d'élever un entier au carré est équivalent au problème de multiplier deux entiers entres eux.
{% endexercice %}
{% details "corrigé" %}

Soit $C(x)$ un algorithme qui rend $x^2$ et $M(x, y)$ un algorithme qui rend $xy$.

Comme $C(x) = M(x, x)$ on a clairement $C \leq M$.

La réciproque vient du produit remarquable $(x + y)^2 = x^2 + y^2 + 2xy$ et donc $M(x, y) = \frac{1}{2}(C(x+y) - C(x) - C(y))$.

{% enddetails %}

### {2, 3}-SUM

Nous allons voir ici une chaîne de réductions, qui nous serons utiles plus tard. On reprend les problèmes [2-SUM](../projet-algorithmes-classiques/2_3-SUM/#problème-2-SUM){.interne} et [3-SUM](../projet-algorithmes-classiques/2_3-SUM/#problème-3-SUM){.interne} que l'on a déjà vu et on montre qu'ils sont équivalents à d'autres problèmes.

#### 2-SUM = crédit

Un petit échauffement :

{% exercice %}
Montrer que 2-SUM est équivalent [au problème crédit](../structure-dictionnaire/#problème-crédit){.interne} en prenant l'ordre des réductions linéaires
{% endexercice %}
{% details "corrigé" %}

- 2-SUM ≤ crédit : on prend C=0
- crédit ≤ 2-SUM : on retranche C/2 à tous les prix

{% enddetails %}

#### 2-SUM ≤ ÉGAL

Commençons par le problème 2-SUM et regardons un problème qui lui ressemble :

{% note "**Problème**" %}

- **nom** : ÉGAL
- **Entrées** :
  - $T$, $T'$ : deux tableaux d'entiers relatifs
- **question** : existe-t-il 2 indices tels que $T[i] = T'[j]$

{% endnote %}

Montrez que :

{% exercice %}
Montrer que 2-SUM ≤ ÉGAL pour l'ordre des réductions linéaires
{% endexercice %}
{% details "corrigé" %}

On prend $T'$ le tableau tel que $T'[k] = -T[k]$ pour tout indice $k$

{% enddetails %}

#### 3-SUM ≤ 3-SUM'

Continuons sur notre lancée avec 3-SUM en considérant le problème suivant :

<span id="problème-3-SUM'"></span>
{% note "**Problème**" %}

- **Nom** : 3-SUM'
- **Entrées** :
  - $T$, $T'$ et $T''$ : trois tableaux d'entiers relatifs
- **Question** : existe-t-il 3 indices tels que $T[i] + T'[j] = T''[k]$

{% endnote %}

Qui, selon toute logique doit être plus général que 3-SUM. Montrez le :

{% exercice %}
Montrer que 3-SUM ≤ 3-SUM' l'ordre des réductions linéaires
{% endexercice %}
{% details "corrigé" %}

On prend $T = T'$ et $T''[x] = -T[x]$

{% enddetails %}

#### Problèmes équivalents ?

Montrons que les versions alternatives des problèmes 2-SUM (ÉGAL) et 3-SUM (3-SUM') sont équivalents aux problèmes d'origine pour l'ordre des réductions linéaires. Ces réductions vont nécessiter un peu de travail.

{% exercice %}
Montrer que ÉGAL ≤ 2-SUM
{% endexercice %}
{% info %}
Il faudra placer les deux tableaux du problème ÉGAL dans l'unique tableau d'entrée de 2-SUM sans que les indices de la solution de 2-SUM ne correspondent au même tableau initial.

Vous pourrez procéder en 2 temps :

1. proposez une solution qui fonctionne **si** les 2 tableaux $T$ et $T'$ en entrée de ÉGAL sont tels que $T[i] + T[j] \neq 0$ et $T'[i] + T'[j] \neq 0$ pour tous $i$ et $j$
2. prouver que l'on peut toujours se ramener au cas précédent en ajoutant une valeur $A$ à chaque valeur de $T$ et en retranchant cette valeur $A$ à tous les éléments de $T'$
{% endinfo %}
{% details "corrigé" %}

Il faut commencer par mettre 2 tableaux dans un seul en définissant un tableau $T''$ dont les premiers éléments sont liés a $T$ et les derniers à $T'$. On ne peut prendre directement :

- $T''[i] = T[i]$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T''[T.\mbox{\small longueur} + j] = T'[j]$ pour $0 \leq j < T'.\mbox{\small longueur}$

Car l'égalité pourrait arriver pour deux indices du même tableau initial. On prend donc :

- $T''[i] = T[i] + A$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T''[T.\mbox{\small longueur} + j] = T'[j] - A$ pour $0 \leq j < T'.\mbox{\small longueur}$

Avec $A$ assez grand pour que $2A > T[i] + [j]$ et $2A > T'[i] + T'[j]$ pour tous $i$ et $j$ ce qui impliquera que si $T''[i] + T''[j] = 0$ alors $0 \leq i < T.\mbox{\small longueur} \leq j$ (ou réciproquement).

Si on prend $A = 2(\sum \vert T[i]\vert + \sum \vert T'[i]\vert) + 1$ cela va fonctionner.

{% enddetails %}

On peut ensuite utiliser la même astuce que précédemment pour résoudre :

{% exercice %}
Montrer que 3-SUM' ≤ 3-SUM
{% endexercice %}
{% details "corrigé" %}

On procède (bien sur) comme précédemment en adaptant à trois tableaux. On choisit $A = 3(\sum \vert T[i]\vert + \sum \vert T'[i]\vert + \sum \vert T''[i]\vert) + 1$ et on crée un tableau $T'''$ tel que :

- $T'''[i] = T[i] + A$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T'''[T.\mbox{\small longueur} + j] = T'[j] + 3\cdot A$ pour $0 \leq j < T'.\mbox{\small longueur}$
- $T'''[T.\mbox{\small longueur} + T'.\mbox{\small longueur} + k] = T''[k] - 4\cdot A$ pour $0 \leq k < T''.\mbox{\small longueur}$

Ceci va garantir le fait que si on a 3 indices $i, j, k$ tels que $T'''[i] + T'''[j] + T'''[k] = 0$. on a bien (à ue permutation prêt) :

- $0 \leq i < T.\mbox{\small longueur}$
- $T.\mbox{\small longueur} \leq j < T.\mbox{\small longueur} + T'.\mbox{\small longueur}$
- $T.\mbox{\small longueur} + T'.\mbox{\small longueur} \leq k < T.\mbox{\small longueur} + T'.\mbox{\small longueur} + T''.\mbox{\small longueur}$

{% enddetails %}

### 3-SUM et géométrie algébrique

3-SUM est un problème fondamental en [géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique). Considérons par exemple le problème suivant :

{% note "**Problème**" %}

- **nom** : GEOBASE
- **Entrées** :
  Un ensemble de $n$ points du plan à coordonnées entières sur trois lignes horizontales avec $y = 0$, $y = 1$ et $y = 2$
- **question** : Existe-t-il une droite non horizontale passant par 3 points.
  {% endnote %}

On va montrer en plusieurs étapes qu'il est équivalent à 3-SUM' !

{% exercice %}
Montrez que deux vecteurs $\vec{u} = (x, y)$ et $\vec{v} = (x', y')$ sont colinéaires si $xy' - yx' = 0$.
{% endexercice %}
{% info %}
Vous pourrez utiliser le fait que deux vecteurs $\vec{u} = (x, y)$ et $\vec{v} = (x', y')$ sont colinéaires si $\vec{u} \cdot \vec{v}^{\perp} = 0$.
{% endinfo %}
{% details "corrigé" %}
Deux vecteurs $\vec{u} = (x, y)$ et $\vec{v} = (x', y')$ sont colinéaires si $\vec{u} \cdot \vec{v}^{\perp} = 0$. Comme $\vec{v}^{\perp} = (-y', x')$, $\vec{u}$ et $\vec{v}$ sont colinéaires si $xy' - yx' = 0$.

{% enddetails %}

Poursuivons dans cette optique :

{% exercice %}
Montrez que les 3 points $A = (x, 0)$, $B = (y, 1)$ et $C = (z, 2)$ sont alignés si et seulement si : $2y = x + z$

{% endexercice %}
{% details "corrigé" %}
En utilisant l'exercice précédent, $A$, $B$ et $C$ sont alignés si $\vec{AB} = (y-x, 1)$ et $\vec{BC} = (z-y, 1)$ sont colinéaires donc si : $y-x -(z-y) = 0$
{% enddetails %}

Vous devez avoir assez de billes pour montrer les 2 réductions linéaires :

{% exercice %}
Montrer que 3-SUM' ≤ GEOBASE pour une réduction linéaire
{% endexercice %}
{% details "corrigé" %}

Il suffit alors de construire les points :

- $(T[i], 0)$
- $(T''[i]/2, 1)$
- $(T'[i], 2)$

si trois points sont colinéaires alors il existe i, j et k tels que $T[i] + T'[j] = T''[k]$
{% enddetails %}

{% exercice %}
Montrer que GEOBASE ≤ 3-SUM' pour une réduction linéaire
{% endexercice %}
{% details "corrigé" %}

On fait le contraire. On ajoute chaque point de :

- $(x, 0)$ dans $T = [x | \forall (x, 0)]$
- $(x, 1)$ dans $T'' = [2x | \forall (x, 1)]$
- $(x, 2)$ dans $T' = [x | \forall (x, 2)]$

{% enddetails %}

Et enfin l'équivalence :

{% exercice %}
Montrer que 3-SUM = GEOBASE pour l'ordre des réductions linéaires.
{% endexercice %}
{% details "corrigé" %}
Clair puisque 3-SUM = 3-SUM' = GEOBASE
{% enddetails %}

> TBD <https://en.wikipedia.org/wiki/3SUM#3SUM-hardness> Peut-on-ton le résoudre mieux que n^2 ?
Si ce genre de problème de géométrie solvable algébriquement, n'hésitez pas à jeter un coup d'œil aux liens suivants :

{% lien %}

- <https://people.csail.mit.edu/virgi/6.s078/papers/gajovermars.pdf>
- <https://www.cs.mcgill.ca/~jking/papers/3sumhard.pdf>

{% endlien %}
