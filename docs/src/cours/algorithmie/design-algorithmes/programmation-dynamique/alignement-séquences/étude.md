---
layout: layout/post.njk
title: "Étude"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir dans cette étude comment définir/calculer une distance entre 2 chaînes de caractères. Nous utiliserons la [distance d'édition](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein), très utilisée.

## Distance entre chaines ?

Soient $a$ et $b$ deux chaines de caractères définies sur un alphabet $\mathcal{A}$. Commençons par supposer qu'elles sont de même longueur (disons $n$). On peut compter les différences entre $a$ et $b$ :

<div>
$$
H(a, b) = \vert \{i \mid a[i] \neq b[i], 0 \leq i < n \} \vert
$$
</div>

{% info %}
La distance entre _"MISO"_ et _"SILO"_ est de 2 différences.
{% endinfo %}

{% note %}

Cette distance est très utilisée dans de nombreux domaines.
Son nom commun est [Distance de Hamming ou distance L1](https://fr.wikipedia.org/wiki/Distance_de_Hamming).

{% endnote %}
{% exercice %}
Montrez que la distance de Hamming est une _vraie_ distance :

- elle est symétrique et positive
- elle vaut 0 si $a=b$
- elle respecte l'inégalité triangulaire

{% endexercice %}
{% details "corrigé" %}
Les deux premières propriétés sont évidentes. La seule chose à démontrer est l'inégalité triangulaire.

Soient $a$, $b$ et $c$ trois chaînes de caractères de même longueur. Si $a[i] \neq c[i]$ alors soit $a[i] \neq b[i]$, soit $b[i] \neq c[i]$. Donc :

<div>
$$
\{i \mid a[i] \neq c[i], 0 \leq i < n \} \subseteq \{i \mid a[i] \neq b[i], 0 \leq i < n \} \cup \{i \mid b[i] \neq c[i], 0 \leq i < n \}
$$
</div>

Ce qui implique :

<div>
$$
\vert \{i \mid a[i] \neq c[i], 0 \leq i < n \} \vert \leq \vert \{i \mid a[i] \neq b[i], 0 \leq i < n \} \cup \{i \mid b[i] \neq c[i], 0 \leq i < n \} \vert
$$
</div>

Et donc :

<div>
$$
\vert \{i \mid a[i] \neq c[i], 0 \leq i < n \} \vert \leq \vert \{i \mid a[i] \neq b[i], 0 \leq i < n \} \vert + \vert \{i \mid b[i] \neq c[i], 0 \leq i < n \} \vert
$$
</div>

Ce qui est égal à :

$$
H(a, c) \leq H(a, b) + H(b, c)
$$

{% enddetails %}
Cette définition de distance est cependant un peu frustre puisque qu'elle ne permet de comparer que deux mots ayant le même nombre de caractères. Il faut donc généraliser pour permettre de comparer deux chaînes de longueur différentes.

Pour cela, on va ajouter un caractère noté `-` qui correspond à un caractère _vide_ et dont le but est d'allonger artificiellement une chaîne. Par exemple : `MEROU` et `ME-R-OU` correspondent aux même chaînes, mais l'une est de longueur 6 et la seconde de longueur 8.

On peut donc maintenant comparer `MEROU` et `MARLOU` via un _allongement_ de `MEROU`. Par exemple comparer `MERO-U` et `MARLOU`, ce qui donne une distance de 3. Le dessin ci-dessous représente cette distance. On a mis des `|` entre les lettres identiques :

```text
MERO-U
| |  |
MARLOU
```

La distance est donc égale :

- au nombre de lettres différentes
- à la longueur des mots moins le nombre de lettres identiques

Ceci pose cependant deux (gros) problèmes :

1. selon l'allongement choisi, la distance n'est pas la même :

   ```text
   MER-OU
   | | ||
   MARLOU
   ```

2. on peut utiliser l'allongement pour changer la distance de 2 chaînes de mêmes longueurs :

   ```text
   MEROUS       MER-OUS
   | |      ≠   | | ||
   MARLOU       MARLOU-
   ```

Il faut donc tout refaire... Une solution pour unifier les deux approches est de formaliser la notion d'**alignement** entre séquences, puis d'utiliser cet outil pour définir la distance d'édition entre deux séquences.

## Alignement

{% note %}
Un alignement entre la chaîne $a =a_0\dots a_{n-1}$ et $b = b_0\dots b_{m-1}$ est un couple $(a^\star, b^\star)$ tel que :

- $a^\star =a^\star_0\dots a^\star_{L-1}$
- $b^\star =b^\star_0\dots b^\star_{L-1}$
- chaque caractère de $a^\star$ et $b^\star$ est soit `-` soit un caractère de la chaîne initiale
- $(a^\star_i, b^\star_i) \neq (-, -)$ pour tout $0 \leq i < L$
- $a^\star$ (respectivement $b^\star$) privé des caractères `-` est égal à $a$ (_resp._ $b$)

{% endnote %}

On remarque que : $\max(n, m) \leq L < n + m$.

### Distance

Étant donné un alignement $(a^\star, b^\star)$, on peut alors définir sa distance de Hamming :

<div>
$$
H(a^\star, b^\star) = \sum_{i=0}^{L-1} \delta(a^\star_i, b^\star_i)
$$
</div>

Avec la **distance élémentaire** $\delta$ :

<div>
$$
\delta(a^\star_i, b^\star_i) = \begin{cases} 0 & \text{si } a^\star_i = b^\star_i\\ 1 & \text{sinon}\end{cases}
$$
</div>

### Evolution d'une séquence en l'autre

Un alignement permet de simuler le passage d'une séquence à l'autre. Par exemple en considérant l'alignement suivant :

```text
MER-OUS
| | ||
MARLOU-
```

En allant de gauche à droite on passe de `MEROUS` à `MARLOU` :

0. MEROUS (mot initial)
1. **M**EROUS (identité)
2. **MA**ROUS (**substitution** de E en A)
3. **MAR**OUS (identité)
4. **MARL**OUS (**insertion** de L)
5. **MARLO**US (identité)
6. **MARLOU**S (identité)
7. **MARLOU** (**suppression** de S)

### Nombre d'alignements

#### Formule

Il peut y avoir beaucoup (beaucoup) d'alignements possibles entre 2 séquences.

{% exercice %}
Trouver au moins 3 alignements différents entre les séquences `ACTGC` et `ACGTC`
{% endexercice %}
{% details "solution" %}

```text
ACTG-C
|  |
A-CGTC
```

```text
ACTGC
||  |
ACGTC
```

```text
ACTG-C
|| | |
AC-GTC
```

et bien d'autres encore sont possibles.

{% enddetails %}

On peut remarquer que ce nombre ne dépend que de la longueur des chaines $a$ et $b$, pas de leur contenu. On note alors $f(n, m)$ le nombre possible d'alignements entre une chaîne de longueur $n$ et une chaîne de longueur $m$.

Comme un alignement ne peut finir sur $(-, -)$, on ne peut qu'avoir 3 possibilités :

- $(a_{n-1}, b_{m-1})$
- $(a_{n-1}, -)$
- $(-, b_{m-1})$

Aligner $a$ et $b$ revient alors soit à aligner :

- $a_0\dots a_{n-2}$ et $b_0\dots b_{m-2}$ et ajouter $(a_{n-1}, b_{m-1})$ à la fin de cet alignement
- aligner $a_0\dots a_{n-2}$ et $b$ et ajouter $(a_{n-1}, -)$ à la fin de cet alignement
- aligner $a$ et $b_0\dots b_{m-2}$ et ajouter $(-, b_{m-1})$ à la fin de cet alignement

Ce qui donne l'équation de récurrence générale suivante :

<div>
$$
f(n, m) = f(n − 1, m − 1) + f(n − 1, m) + f(n, m − 1)
$$
</div>

Avec les conditions aux limites :

- $f(1, 1) = 3$
- $f(n, 0) = 1$ pour tous $n \geq 1$
- $f(0, m) = 1$ pour tout $m \geq 1$

{% info %}
Notez que $f(0, 0)$ ne peut exister puisque l'alignement $(-, -)$ n'existe pas.
{% endinfo %}

Ce nombre est gigantesque. On peut en effet prouver, si $n=m$ :

<div>
$$
f(n, n) \sim \frac{(1 + \sqrt{2})^{2n + 1}}{\sqrt{n}}
$$
</div>

Ce qui donne :

- $f(10, 10) \sim 34537380$
- $f(100, 100) \sim 8.67 \cdot 10^{75}$
- $f(200, 200) \sim 2.2 \cdot 10^{152}$

{% info %}
Il n'y a qu'environ $10^{80}$ particules dans l'univers.
{% endinfo %}

#### Calcul

Comme il est impossible d'énumérer tous les alignements car il y en a trop, il faut ruser pour calculer le nombre $f(n, m)$ pour $1 \leq n, m$.

On remarque que pour calculer $f(n, m)$ on a besoin que de $f(n-1, m-1)$, $f(n-1, m)$ et $f(n, m-1)$. Si l'on a stocké ces 3 valeurs, le calcul de $f(n, m)$ devient aisé.

On peut représenter ces dépendances de façon matricielle :

|     | 0   | 1   | ... | j-1           | j           | ... | m        |
| --- | --- | --- | --- | ------------- | ----------- | --- | -------- |
| 0   | $1$ | $1$ |     | $1$           | $1$         |     | $1$      |
| 1   | $1$ | $3$ |     |               |             |     |          |
| ... |     |     |     |               |             |     |          |
| i-1 | $1$ |     |     | $f(i-1, j-1)$ | $f(i-1, j)$ |     |          |
| i   | $1$ |     |     | $f(i, j-1)$   | $f(i, j)$   |     |          |
| ... |     |     |     |               |             |     |          |
| n   | $1$ |     |     |               |             |     | $f(n,m)$ |

En notant $F$ cette matrice on a alors :

$$
F[i][j] = F[i-1][j] + F[i][j-1] + F[i-1][j-1]
$$

Remplir la matrice $F$ nous donne le nombre d'alignements, ce qui se fait aisément en remarquant que l'on peut construire $F$ ligne à ligne :

```python
F = []
for i in range(n+1):  # matrice de 1
    ligne = [1] * (m + 1)
    F.append(ligne)

for i in range(1, n + 1):  # ligne après ligne àn partir de la seconde
    for j in range(1, m + 1):
        F[i][j] = F[i - 1][j] + F[i][j - 1] + F[i - 1][j - 1]
```

On a utilisé l'astuce de placer $F[0][0] = 1$ pour que $F[1][1]$ puisse être calculé sans cas particulier.

{% details "M pour n=m=10" %}

```python
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
 [1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221],
 [1, 7, 25, 63, 129, 231, 377, 575, 833, 1159, 1561],
 [1, 9, 41, 129, 321, 681, 1289, 2241, 3649, 5641, 8361],
 [1, 11, 61, 231, 681, 1683, 3653, 7183, 13073, 22363, 36365],
 [1, 13, 85, 377, 1289, 3653, 8989, 19825, 40081, 75517, 134245],
 [1, 15, 113, 575, 2241, 7183, 19825, 48639, 108545, 224143, 433905],
 [1, 17, 145, 833, 3649, 13073, 40081, 108545, 265729, 598417, 1256465],
 [1, 19, 181, 1159, 5641, 22363, 75517, 224143, 598417, 1462563, 3317445],
 [1, 21, 221, 1561, 8361, 36365, 134245, 433905, 1256465, 3317445, 8097453]]
```

On voit que l'approximation précédente n'est pas encore trop valide lorsque $n$ est petit. Elle le devient de plus en plus à mesure que $n$ augmente.

{% enddetails %}

La complexité de l'algorithme de calcul précédent :

- nécessite $\mathcal{O}(nm)$ opérations
- nécessite le stockage d'une matrice de taille $m \cdot n$ en mémoire, il est donc de complexité spatiale $\mathcal{O}(nm)$

{% exercice %}
Proposez un algorithme nécessitant uniquement une complexité spatiale de $\mathcal{O}(m)$ pour calculer $f(n, m)$.
{% endexercice %}
{% details "corrigé" %}
On remarque que l'algorithme n'a uniquement besoin que de la ligne précédente à chaque itération. On peut alors le modifier :

```python
ligne_précédente = [-1] + [1] * m
ligne_actuelle = [1]

for i in range(1, n + 1):
    print(ligne_précédente)
    for j in range(1, m + 1):
        f_ij =  ligne_précédente[j] + ligne_actuelle[j - 1] + ligne_précédente[j - 1]
        ligne_actuelle.append(f_ij)
    ligne_précédente = ligne_actuelle
    ligne_actuelle = [1]

f_nm = ligne_précédente[-1]
```

{% enddetails %}

## Distance d'édition

L'alignement entre 2 séquences nous permet de définir, à partir d'une distance pour alignement, une distance pour séquences :

<div>
$$
D(a, b) = \min \{ H(a^\star, b^\star) \mid \text{pour tous les alignements } (a^\star, b^\star) \text{ entre } a \text{ et } b\}
$$
</div>

Comme il est impossible de trouver tous les alignements possibles, il faut ruser pour calculer cette distance sans faire exploser la complexité.

### Calcul pour la distance élémentaire

Reprenons le calcul de la distance pour un alignement donné :

<div>
$$
H(a^\star, b^\star) = \sum_{i=0}^{L-1} \delta(a^\star_i, b^\star_i) = \sum_{i=0}^{L-2} \delta(a^\star_i, b^\star_i) + \delta(a^\star_{L-1}, b^\star_{L-1})
$$
</div>

Ce qui, pour la distance élémentaire, donne :

<div>
$$
H(a^\star, b^\star) = \sum_{i=0}^{L-2} \delta(a^\star_i, b^\star_i) +
\begin{cases}
0 & \text{si } a^\star_{L-1} = b^\star_{L-1}\\
1 & \text{sinon}
\end{cases}
$$
</div>

De la même façon que l'on a fait pour établir l'équation de récurrence pour déterminer le nombre d'alignements, on a que $(a^\star_{L-1}, b^\star_{L-1})$ peut être égal à :

- $(a_{n-1}, b_{m-1})$ et donc $((a^\star_0\dots a^\star_{L-2}), (b^\star_0\dots b^\star_{L-2}))$ est un alignement des séquences $a[:-1] = a_0\dots a_{n-2}$ et $b[:-1] = b_0\dots b_{m-2}$
- $(a_{n-1}, -)$ et donc $((a^\star_0\dots a^\star_{L-2}), (b^\star_0\dots b^\star_{L-1}))$ est un alignement des séquences $a[:-1] = a_0\dots a_{n-2}$ et $b$
- $(-, b_{m-1})$ et donc $((a^\star_0\dots a^\star_{L-1}), (b^\star_0\dots b^\star_{L-2}))$ est un alignement des séquences $a$ et $b[:-1] = b_0\dots b_{m-2}$

De là, si l'alignement $(a^\star, b^\star)$ est celui réalisant la distance ($D(a, b) = H(a^\star, b^\star)$), le cas réalisant le minimum est forcément également une distance.

Par exemple, si $H(a^\star_0\dots a^\star_{L-2}, b^\star_0\dots b^\star_{L-2}) + \delta(a_{n-1}, b_{m-1})$ est plus petit que $H(a^\star_0\dots a^\star_{L-2}, b^\star_0\dots b^\star_{L-1}) + \delta(a_{n-1}, -)$ et que $H(a^\star_0\dots a^\star_{L-1}, b^\star_0\dots b^\star_{L-2}) + \delta(-, b_{m-1})$, alors non seulement :

$$
H(a^\star, b^\star) = H(a^\star_0\dots a^\star_{L-2}, b^\star_0\dots b^\star_{L-2}) + \delta(a_{n-1}, b_{m-1})
$$

Mais on en déduit également que :

$$
D(a[:-1], b[:-1]) = H(a^\star_0\dots a^\star_{L-2}, b^\star_0\dots b^\star_{L-2})
$$

Car si $D(a[:-1], b[:-1])$ était strictement plus petite, on aurait pu passer par l'alignement utilisé pour avoir un alignement entre $a$ et $b$ plus petit que $H$, ce qui est impossible.

Les deux autres cas, se traitent de la même manière : un alignement optimal est composé de sous-alignements eux aussi optimaux !

{% note %}
C'est le principe de la [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique) : un chemin optimal est constitué de sous-chemins eux-mêmes optimaux.
{% endnote %}

Donc si l'on connaît :

- $D(a[:-1], b[:-1])$
- $D(a[:-1], b)$
- $D(a, b[:-1])$

on a :

<div>
$$
D(a, b) = \min  \begin{cases}
      D(a[:-1], b[:-1]) + \delta(a_{n-1}, b_{m-1}) & \\
     D(a[:-1], b) + 1 & \\
      D(a, b[:-1]) + 1 &\\
    \end{cases}
$$
</div>

Ceci se généralise pour tout $i$ et $j$ :

<div>
$$
D(a[:i+1], b[:j+1]) = \min \begin{cases}
      D(a[:i], b[:j]) + \delta(a[i], b[j]) & \\
      D(a[:i], b[:j + 1]) + 1 & \\
      D(a[:i + 1], b[:j]) + 1 & \\
    \end{cases}
$$
</div>

Et nous permet – tout comme on l'a fait pour le calcul du nombre d'alignements – de créer une représentation matricielle de l'alignement et de la distance d'édition, appelée **matrice d'édition** :

|          | $-$   | $a[0]$ | ... | $a[i-1]$           | $a[i]$               | $a[n-1]$ |
| -------- | ----- | ------ | --- | ------------------ | -------------------- | -------- |
| $-$      | 0     | $1$    |     | $i$                | $i+1$                | $n$      |
| $b[0]$   | $1$   |        |     |                    |                      |          |
| ...      |       |        |     |                    |                      |          |
| $b[j-1]$ | $j$   |        |     | $D(a[:i],b[:j])$   | $D(a[:i+1],b[:j])$   |          |
| $b[j]$   | $j+1$ |        |     | $D(a[:i],b[:j+1])$ | $D(a[:i+1],b[:j+1])$ |          |
| ...      |       |        |     |                    |                      |          |
| $b[m-1]$ | $m$   |        |     |                    |                      | $D(a,b)$ |

Et nous donne un algorithme très facile pour la calculer, puisqu'il suffit de remplir la première ligne et la première colonne, puis de progresser ligne à ligne avec la formule:

<div>
$$
M[i + 1][j + 1] = \min \begin{cases}
M[i][j] + 0  & \text{si } a[j] = b[i]\\
M[i][j] + 1  & \text{si } a[j] \neq b[i]\\
M[i + 1][j] + 1 &\\
M[i][j + 1] + 1&\\
\end{cases}
$$
</div>

La distance entre $a$ et $b$ qui correspond à un alignement de distance minimale est alors à la dernière ligne et dernière colonne de la matrice (en $M[-1][-1]$).

### Exemple pour la distance élémentaire

Distance de `ACTGATT` (horizontal) à `GCTAATCG` (vertical).

{% exercice %}
Créez la matrice d'édition _vierge_ à utiliser
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   |     |     |     |     |     |     |     |
| G   |     |     |     |     |     |     |     |
| C   |     |     |     |     |     |     |     |
| T   |     |     |     |     |     |     |     |
| A   |     |     |     |     |     |     |     |
| A   |     |     |     |     |     |     |     |
| T   |     |     |     |     |     |     |     |
| C   |     |     |     |     |     |     |     |
| G   |     |     |     |     |     |     |     |

{% enddetails  %}

{% exercice %}
Remplissez la première ligne et la première colonne
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| G   | 1   |     |     |     |     |     |     |
| C   | 2   |     |     |     |     |     |     |
| T   | 3   |     |     |     |     |     |     |
| A   | 4   |     |     |     |     |     |     |
| A   | 5   |     |     |     |     |     |     |
| T   | 6   |     |     |     |     |     |     |
| C   | 7   |     |     |     |     |     |     |
| G   | 8   |     |     |     |     |     |     |

{% enddetails  %}

{% exercice %}
Remplissez le reste de la matrice ligne à ligne
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| G   | 1   | 1   | 2   | 3   | 3   | 4   | 5   | 6   |
| C   | 2   | 2   | 1   | 2   | 3   | 4   | 5   | 6   |
| T   | 3   | 3   | 2   | 1   | 2   | 3   | 4   | 5   |
| A   | 4   | 3   | 3   | 2   | 2   | 2   | 3   | 4   |
| A   | 5   | 4   | 4   | 3   | 3   | 2   | 3   | 4   |
| T   | 6   | 5   | 5   | 4   | 4   | 3   | 2   | 3   |
| C   | 7   | 6   | 5   | 5   | 5   | 4   | 3   | 3   |
| G   | 8   | 7   | 6   | 6   | 5   | 5   | 4   | 4   |

{% enddetails  %}

{% exercice %}
Donnez la distance obtenue
{% endexercice %}
{% details "solution" %}

C'est $M[-1][-1]$ et cela vaut 4

{% enddetails  %}

### Alignement et distance d'édition

Avec la matrice d'édition, il est facile de retrouver un alignement qui a réalisé la distance minimale en _remontant_ dans la matrice.

1. on pose $i=-1$ et $j=-1$
2. on pose $A = []$, c'est le tableau qui va contenir notre alignement
3. on considère $M[i][j]$ qui est la valeur courante de la matrice
4. on cherche le minimum parmi les 4 possibilités :
   1. $M[i-1][j-1]$ si $a[j] = b[i]$
   2. $M[i-1][j-1] + 1$ si $a[j] \neq b[i]$
   3. $M[i-1][j] + 1$
   4. $M[i][j-1] + 1$
5. le minimum de l'étape 4 nous donne une partie de l'alignement à ajouter :
   1. on ajoute $(a[j], b[i])$ au début de $A$ et on pose $i=i-1$ et $j=j-1$
   2. on ajoute $(a[j], b[i])$ au début de $A$ et on pose $i=i-1$ et $j=j-1$
   3. on ajoute $(-, b[i])$ au début de $A$ et on pose $i=i-1$
   4. on ajoute $(a[j], -)$ au début de $A$ et on pose $j=j-1$
6. si $i> -m$ ou $j>-n$ on retourne en 3.

L'algorithme précédent est une idée de l'algorithme. Il faudra ajouter les conditions au bord de la matrice (lorsque $i=-m$ et $j > -n$ par exemple) pour ne pas déborder.

{% exercice %}
En reprenant l'exemple précédent, donner un alignement donnant le coût minimum
{% endexercice %}
{% details "solution" %}

Le chemin dans la matrice est donné en gras :

|     | -     | A     | C     | T     | G     | A     | T     | T     |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| -   | **0** | 1     | 2     | 3     | 4     | 5     | 6     | 7     |
| G   | 1     | **1** | 2     | 3     | 3     | 4     | 5     | 6     |
| C   | 2     | 2     | **1** | 2     | 3     | 4     | 5     | 6     |
| T   | 3     | 3     | 2     | **1** | 2     | 3     | 4     | 5     |
| A   | 4     | 4     | 3     | 2     | **2** | 2     | 3     | 4     |
| A   | 5     | 4     | 4     | 3     | 3     | **2** | 3     | 4     |
| T   | 6     | 5     | 4     | 4     | 4     | 3     | **2** | 3     |
| C   | 7     | 6     | 5     | 5     | 5     | 4     | **3** | 3     |
| G   | 8     | 7     | 6     | 6     | 5     | 5     | 4     | **4** |

On obtient alors l'alignement :

```text
ACTGAT-T
 || ||
GCTAATCG
```

Notez qu'il y a un autre alignement possible :

|     | -     | A     | C     | T     | G     | A     | T     | T     |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| -   | **0** | 1     | 2     | 3     | 4     | 5     | 6     | 7     |
| G   | 1     | **1** | 2     | 3     | 3     | 4     | 5     | 6     |
| C   | 2     | 2     | **1** | 2     | 3     | 4     | 5     | 6     |
| T   | 3     | 3     | 2     | **1** | 2     | 3     | 4     | 5     |
| A   | 4     | 4     | 3     | 2     | **2** | 2     | 3     | 4     |
| A   | 5     | 4     | 4     | 3     | 3     | **2** | 3     | 4     |
| T   | 6     | 5     | 4     | 4     | 4     | 3     | **2** | 3     |
| C   | 7     | 6     | 5     | 5     | 5     | 4     | 3     | **3** |
| G   | 8     | 7     | 6     | 6     | 5     | 5     | 4     | **4** |

Qui donne l'alignement :

```text
ACTGATT-
 || ||
GCTAATCG
```

{% enddetails  %}

## cas général

Pour l'instant notre distance élémentaire est définie telle que :

Avec la **distance élémentaire** $\delta$ :

<div>
$$
\delta(a^\star_i, b^\star_i) = \begin{cases} 0 & \text{si } a^\star_i = b^\star_i\\ 1 & \text{sinon}\end{cases}
$$
</div>

Comme $a^\star_i$ et $b^\star_j$ sont soit des caractères de l'alphabet soit le caractère vide $-$, on peut définir $\delta$ tel que :

- $\delta(u, u) = 0$ pour tout caractère $u$
- $\delta(u, v) = 1$ si $u$ et $v$ sont deux caractères différents
- $\delta(u, -) = \delta(-, u) = 1$

Il peut parfois être intéressant d'affiner un peu cette distance. Par exemple, si l'on cherche à trouver les erreurs de frappe, on pourra tenter de supposer que deux mots sont proches si les lettres qui les composent sont proches sur le clavier.

{% info %}
_"ORNE"_ sera plus proche de _"ORBE"_ que de _"URNE"_ si l'on compte l'éloignement des touches sur le clavier.
{%endinfo %}

On pourra alors utiliser la distance :

- $\delta'(u, u) = 0$ pour tout caractère $u$
- $\delta'(u, v)$ vaut la distance entre les touches $u$ et $v$ sur le clavier
- $\delta'(u, -) = \delta'(-, u) = K$, une constante.

De façon général, on définit alors un coût entre caractères défini tel que

- $d(x, -)$ est appelé **coût de suppression**,
- $d(-, x)$ est appelé **coût d'insertion** et est égal à $d(x, -)$
- $d(x, y)$ est nommé **coût de substitution**

### définition du cas général

Tout ce qu'on a fait précédemment est toujours applicable !

Sachant un coût $d$, on peut définir la distance $S_d$ pour un alignement $(a^\star, b^\star)$:

<div>
$$
S_d(a^\star, b^\star) = \sum_{i=0}^{L-1} d(a^\star_i, b^\star_i)
$$
</div>

Ce qui nous permet de définir la distance entre deux séquences pour un coût $d$ :

<div>
$$
D_d(a, b) = \min \{ S_d(a^\star, b^\star) \mid \text{pour tous les alignements } (a^\star, b^\star) \text{ entre } a \text{ et } b\}
$$
</div>

On en déduit une méthode itérative pour trouver cette distance grâce à l'équation :

<div>
$$
D_d(a[:i+1], b[:j+1]) = \min \begin{cases}
      D_d(a[:i], b[:j]) + d(a[i], b[j]) & \\
      D_d(a[:i], b[:j + 1]) + d(a[i], -) & \\
      D_d(a[:i + 1], b[:j]) + d(-, b[j]) & \\
    \end{cases}
$$
</div>

Et le terme général de la matrice d'édition :

```python
M[i + 1][j + 1] = min(M[i][j] + d(a[j], b[i]),
                      M[i + 1][j] + d(-, b[i]),
                      M[i][j + 1] + d(a[j], -))
```

### exemple du cas général

Considérons le coût :

|     | A   | C   | G   | T   |
| --- | --- | --- | --- | --- |
| A   | 0   |     |     |
| C   | 2   | 0   |     |
| G   | 2   | 2   | 0   |
| T   | 2   | 2   | 2   | 0   |
| -   | 1   | 1   | 1   | 1   |

Aller de `ACTGATT` (horizontal) à `GCTAATCG` (vertical).

{% exercice %}
Créez la matrice d'édition _vierge_ à utiliser
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   |     |     |     |     |     |     |     |
| G   |     |     |     |     |     |     |     |
| C   |     |     |     |     |     |     |     |
| T   |     |     |     |     |     |     |     |
| A   |     |     |     |     |     |     |     |
| A   |     |     |     |     |     |     |     |
| T   |     |     |     |     |     |     |     |
| C   |     |     |     |     |     |     |     |
| G   |     |     |     |     |     |     |     |

{% enddetails  %}

{% exercice %}
Remplissez la première ligne et la première colonne
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| G   | 1   |     |     |     |     |     |     |
| C   | 2   |     |     |     |     |     |     |
| T   | 3   |     |     |     |     |     |     |
| A   | 4   |     |     |     |     |     |     |
| A   | 5   |     |     |     |     |     |     |
| T   | 6   |     |     |     |     |     |     |
| C   | 7   |     |     |     |     |     |     |
| G   | 8   |     |     |     |     |     |     |

{% enddetails  %}

{% exercice %}
Remplissez le reste de la matrice ligne à ligne
{% endexercice %}
{% details "solution" %}

|     | -   | A   | C   | T   | G   | A   | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| G   | 1   | 2   | 3   | 4   | 3   | 4   | 5   | 6   |
| C   | 2   | 3   | 2   | 3   | 4   | 5   | 6   | 7   |
| T   | 3   | 4   | 3   | 2   | 3   | 4   | 5   | 6   |
| A   | 4   | 3   | 4   | 3   | 4   | 3   | 4   | 5   |
| A   | 5   | 4   | 5   | 4   | 5   | 4   | 5   | 6   |
| T   | 6   | 5   | 6   | 5   | 6   | 5   | 4   | 5   |
| C   | 7   | 6   | 5   | 6   | 7   | 6   | 5   | 6   |
| G   | 8   | 7   | 6   | 7   | 6   | 7   | 6   | 7   |

{% enddetails  %}

{% exercice %}
Quel est la distance entre les deux séquences ?
{% endexercice %}
{% details "solution" %}

7

{% enddetails  %}
