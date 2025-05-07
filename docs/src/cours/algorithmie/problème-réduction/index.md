---
layout: layout/post.njk 
title:  "Réduction de problèmes"

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
\Uparrow &  & \Downarrow\\
S_1 & \leftarrow & S_2
\end{array}
$$
</div>

La formalisation de cette opération s'appelle [une réduction](https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)) et peut prendre plusieurs formes, que nous expliciterons. Outre ses applications pratiques évidentes pour le design d'algorithme et la résolution de problèmes, la réduction est est un outil fondamental permettant de comparer et de classer les problèmes algorithmiques.

{% info %}
Nous ne parlerons pas ici de la [Réduction de Turing](https://en.wikipedia.org/wiki/Turing_reduction), trop générale et demandant des connaissances comme [les machines à oracles](https://fr.wikipedia.org/wiki/Oracle_(machine_de_Turing)) dont nous ne parlerons pas dans ce cours d'algorithmie.
{% endinfo %}

## Définitions

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction_** de $P_2$ en $P_1$ est un couple d'algorithmes $A_1$ et $A_2$ tels que :

- Si $E_1$ est une entrée du problème $P_1$ alors $A_1(E_1)$ est une entrée de du problème $P_2$
- Si $S_2$ est une solution au problème $P_2$ avec $A_1(E_1)$ comme entrée alors $A_2(S_2)$ est une solution au problème $P_1$ d'entrée $E_1$.

Les réductions forment un ordre sur les problèmes algorithmiques : s'il existe une réduction de $P_2$ en $P_1$ on notera $P_1 \leq P_2$.
{% endnote %}

Cette définition, très générale, permet de montrer qu'un problème est plus général qu'un autre : $A \leq B$ signifie que $A$ est un cas particulier de $B$, que résoudre $B$ permet de résoudre $A$. De là, la complexité du problème $B$ ne peut être plus petite que celle du problème $A$. Par exemple :

{% exercice %}
Montrez que le problème de recherche du minimum dans un tableau d'entiers  est plus simple que le problème de recherche du maximum dans un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

Pour cela, On crée le tableau $T'$ tel que $T'[x] = \max(T)-T[x]$ et on cherche $\max(T')$. Le min est alors : $\min(T) = \max(T) - \max(T')$.

{% enddetails %}

Si l'on veut utiliser la réduction pour résoudre notre problème réduit, on cherche le couple d'algorithmes avec la complexité la plus faible, si possible linéaire (comme dans l'exercice précédent) et au mieux polynomiale :

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction polynomiale_** de $P_2$ en $P_1$ est une réduction ou les deux algorithmes $A_1$ et $A_2$ sont de complexité polynomiale.
{% endnote %}
{% attention %}
Les réductions polynomiales sont les seules utilisées en algorithmie, c'est pourquoi on considérera souvent que **_réduction_** et **_réduction polynomiale_** comme équivalent, une réduction **devant être** polynomiale.
{% endattention %}

Une réduction polynomiale nous permettra d'utiliser effectivement l'algorithme résolvant $P_2$ pour résoudre $P_1$.

Enfin :

{% note "**Définition**" %}
On dira que deux problèmes $P_1$ et $P_2$ sont **_équivalents_** s'il existe deux **réductions polynomiales** $P_1 \leq P_2$ et $P_2 \leq P_1$.
{% endnote %}

Par exemple :

{% exercice %}
Montrez que le problèmes de recherche du minimum dans un tableau d'entiers relatifs est  le problème de recherche du maximum dans un tableau d'entiers relatifs sont équivalent et que la réduction est linéaire.
{% endexercice %}
{% details "corrigé" %}
Pour des entiers relatifs, il suffit de faire $T'[x] = -T[x]$.
{% enddetails %}

## Exemples et exercices

### Tris

Trier un tableau d'entier va souvent rendre les problèmes bien plus facile. ce qui fait que c'est souvent utile de faire une réduction au tri.

{% exercice %}
Montrez que le problème de recherche du maximum dans un tableau d'entiers  est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

On trie puis on prend le max.

{% enddetails %}

{% exercice %}
Montrez que le problème de la recherche de doublon dans un tableau d'entiers est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

On trie puis on parcourt le tableau jusqu'à trouver deux éléments successifs égaux.

{% enddetails %}

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

Nous allons voir ici une chaîne de réductions, qui nous serons utiles plus tard.

#### 2-SUM ≤ ÉGAL

Commençons par [le problème 2-SUM](../projet-algorithmes-classiques/#2-sum){.interne} que nous avons déjà vu :

{% note "**Problème**" %}

- **nom** : 2-SUM
- **Entrée** :
  - T : un tableau de $n$ entiers relatifs
- **question** : existe-t-il 2 indices $i$ et $j$ (pouvant être égaux) tels que $T[i] + T[j] = 0$

{% endnote %}

Regardons un problème qui lui ressemble :

{% note "**Problème**" %}

- **nom** : ÉGAL
- **Entrées** :
  - $T$, $T'$ : deux tableaux d'entiers relatifs
- **question** : existe-t-il 2 indices tels que $T[i] = T'[j]$

{% endnote %}

Montrez que :

{% exercice %}
Montrer que 2-SUM ≤ ÉGAL
{% endexercice %}
{% details "corrigé" %}

On prend $T'$ le tableau tel que $T'[k] = -T[k]$ pour tout indice $k$

{% enddetails %}

#### 3-SUM ≤ 3-SUM'

Reprenons [le problème 3-SUM](../projet-algorithmes-classiques/#3-sum){.interne} que nous avons déjà vu :

{% note "**Problème**" %}

- **nom** : 3-SUM
- **Entrées** :
  - T : un tableau de $n$ entiers relatifs
- **question** : existe-t-il 3 indices (pouvant être égaux) tels que $T[i] + T[j] + T[k] = 0$

{% endnote %}

Continuons sur notre lancée en considérant le problème suivant :

{% note "**Problème**" %}

- **Nom** : 3-SUM'
- **Entrées** :
  - $T$, $T'$ et $T''$ : trois tableaux d'entiers relatifs
- **Question** : existe-t-il 3 indices tels que $T[i] + T'[j] = T''[k]$

{% endnote %}

Qui, selon toute logique doit être plus général que 3-SUM. Montrez le :
Prouvez le :

{% exercice %}
Montrer que 3-SUM ≤ 3-SUM'
{% endexercice %}
{% details "corrigé" %}

On prend $T = T'$ et $T''[x] = -T[x]$

{% enddetails %}

#### Problèmes équivalents ?

Montrons que les versions alternatives des problèmes 2-SUM (ÉGAL) et 3-SUM (3-SUM') sont équivalents aux problèmes d'origine. Ces réduction vont nécessiter un peu de travail.

{% exercice %}
Montrer que ÉGAL ≤ 2-SUM
{% endexercice %}
{% details "corrigé" %}

Il faut commencer par mettre 2 tableaux dans un seul en définissant un tableau $T''$ dont les premiers éléments sont liés a $T$ et les derniers à $T$. On ne peut prendre directement :

- $T''[i] = T[i]$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T''[T.\mbox{\small longueur} + j] = T'[j]$ pour $0 \leq j < T'.\mbox{\small longueur}$

Car l'égalité pourrait arriver pour deux indices du même tableau initial. On prend donc :

- $T''[i] = T[i] + A$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T''[T.\mbox{\small longueur} + j] = T'[j] - A$ pour $0 \leq j < T'.\mbox{\small longueur}$

Avec $A$ assez grand pour que $2A > T[i] + [j]$ et $2A > T'[i] + T'[j]$ pur tous $i$ et $j$ ce qui impliquera que si %$T''[i] + T''[j] = 0$ alors $0 \leq i < T.\mbox{\small longueur} \leq j$ (ou réciproquement).

Si on prend $A = 2(\sum \vert T[i]\vert + \sum \vert T'[i]\vert) + 1$ cela va fonctionner.

{% enddetails %}
{% exercice %}
Montrer que 3-SUM' ≤ 3-SUM
{% endexercice %}
{% details "corrigé" %}

On procède (bien sur) comme précédemment en adaptant à trois tableaux. On choisit $A = 3(\sum \vert T[i]\vert + \sum \vert T'[i]\vert + \sum \vert T''[i]\vert) + 1$ et on crée un tableau $T'''$ tel que :

- $T'''[i] = T[i] + A$ pour $0 \leq i < T.\mbox{\small longueur}$
- $T'''[T.\mbox{\small longueur} + j] = T'[j] + 3\cdot A$ pour $0 \leq j < T'.\mbox{\small longueur}$
- $T'''[T.\mbox{\small longueur} + T'.\mbox{\small longueur} + k] = T''[k] - 4\cdot A$ pour $0 \leq k < T''.\mbox{\small longueur}$

Ceci va garantir le fait que si on a 3 indices $i, j, k$ tels que T'''[i] + T'''[j] + T'''[k] = 0$. on a bien (à ue permutation prêt) :

- $0 \leq i < T.\mbox{\small longueur}$
- $T.\mbox{\small longueur} \leq j < T.\mbox{\small longueur} + T'.\mbox{\small longueur}$
- $T.\mbox{\small longueur} + T'.\mbox{\small longueur} \leq k < T.\mbox{\small longueur} + T'.\mbox{\small longueur} + T''.\mbox{\small longueur}$

{% enddetails %}

#### ÉGAL ≤ 3-SUM

Terminons cette partie en montrant que 3-SUM est plus général que ÉGAL, cette réduction est un peu plus dure que les précédentes :

{% exercice %}
Montrer que ÉGAL ≤ 3-SUM
{% endexercice %}
{% details "corrigé" %}

Soit $T$ et $T'$ une instance du problème ÉGAL telle que $T.\mbox{\small longueur} = n$ et $T'.\mbox{\small longueur} = n'$.

L'idée est toujours la même : créer un grand tableau $T''$ de taille $n + n' + 1$
De telle sorte que s'il existe $i$, $j$ et $k$ avec $T''[i] + T''[j] + T''[k] = 0$ alors :

- $0 \leq i < n$ et est lié au tableau $T$
- $n \leq j < n + n'$ et est lié au tableau $T'$
- $k = n + n'$

On va pour cela éloigner fortement les valeurs des tableaux $T$ et $T'$ dans $T''$. Par exemple :

- $T''[i] = T[i] + K$ pour tout $0 \leq i < n$
- $T''[i + n] = -T'[i] + K'$ pour tout $0 \leq i < n'$
- $T''[n+n'] = -K-K'$

En prenant $K = \max_i(\\,\vert\\, T[i] \\,\vert\\,) + 1$ et $K'= K + 2 \cdot (\max_i(\\,\vert\\, T[i] \\,\vert\\,) + \max_i(\\,\vert\\, T'[i] \\,\vert\\,)) + 1$ on a bien que $T''[i] + T''[j] + T''[k] = 0$ si :

1. $k = n+n'$ sinon on ne peut avoir de somme égale à 0
2. avec $k = n+n'$  on ne peut avoir $0 \leq i, j < n$ sinon $T''[i] + T''[j] \leq 2(K + \max_i(\\,\vert\\, T[i] \\,\vert\\,) < K + K' = T''[k]$
3. avec $k = n+n'$ on ne peut avoir $n \leq i, j < n + n'$ sinon $T''[i] + T''[j] \geq 2(K' - \max_i(\\,\vert\\, T'[i] \\,\vert\\,)) > K + K' = T''[k]$

{% enddetails %}
