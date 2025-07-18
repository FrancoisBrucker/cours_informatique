---
layout: layout/post.njk
title: Diviser pour régner

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Principe

{% lien %}
<https://fr.wikipedia.org/wiki/Diviser_pour_r%C3%A9gner_(informatique)>
{% endlien %}

Le principe du design diviser pour régner consiste à découper le problème initial en sous-problèmes que l'on peut résoudre puis, si nécessaire, les recombiner en une solution du problème initial.

L'élégance de ce principe réside dans le fait que l'on peut utiliser l'algorithme que l'on est en train de construire pour résoudre les sous-problèmes ! Toute la difficulté réside dans le fait de trouver un découpage du problème initial facile à traiter.

### Sous-problème

Si l'on peut trouver _facilement_ une restriction du problème dans laquelle va se trouver la solution globale, on peut utiliser le design suivant :

```pseudocode
algorithme diviser(données):
    À partir de données créer, k donnees_partielles_i (1 ≤ i ≤ k)
    Parmi ces k donnees_partielles_i, en choisir une que l'on nomme donnee_partielle

    rendre diviser(donnee_partielle)
```

On restreint nos données en supprimant les données superflues : c'est le principe d'un algorithme récursif où l'on restreint à chaque itération l'ensemble de nos données.

On a utilisé ce principe dans [la dichotomie](../../../projet-algorithmes-classiques/#dichotomie){.interne} par exemple.

{% attention "**À retenir**" %}
On utilise le design **diviser** que lorsqu'il est _facile_ (et rapide) algorithmiquement de trouver un sous-ensemble des données initiales donnant la même solution.

{% endattention %}

### Diviser puis combiner

Mais souvent, il ne suffit pas de diviser pour trouver notre solution, il faut pouvoir recombiner des solutions partielles en une solution globale. On ajoute alors une étape de combinaison pour obtenir le principe général du design diviser pour régner :

```pseudocode
algorithme diviser_puis_combiner(données):
    À partir de données, créer k donnees_partielles_i (1 ≤ i ≤ k)
    pour chaque i  de [1 .. k]:
        solution_i ← diviser_puis_combiner(donnees_partielles_i)

    solution ← combiner(solution_1, ..., solution_k)

    rendre solution
```

On a déjà vu ce design lorsque l'on a étudié [le tri fusion](../../problème-tris/algorithme-fusion/){.interne} ou [le tri rapide](../../problème-tris/algorithme-rapide/){.interne}.

{% attention "**À retenir**" %}
On utilise le design **diviser pour régner** que lorsqu'il est _facile_ (et rapide) algorithmiquement de combiner des solutions partielles en une solution globale.

Toute la difficulté réside dans le fait de trouver un découpage du problème initial facile à combiner.
{% endattention %}

On l'a utilisé pour le tri car :

- il est facile de combiner deux tableaux trié si le max de l'un est inférieur au min de l'autre (tri rapide)
- il est plus généralement facile de construire un tableau trié à partir de 2 sous-tableaux triés (tri fusion)

{% info %}
Si la seconde condition est plus générale, la première peut se faire in-place ce qui est avantageux si le tableau à trier est gigantesque.
{% endinfo %}

## Complexité

Pour connaître la complexité d'un algorithme sous la forme diviser pour régner il faut connaître :

- le coût du découpage en sous-problème
- le nombre d'appels récursifs
- le coût de la combinaison des solutions partielles en une solution globale

La forme de l'équation de récursion est toujours la même et sa valeur est donnée par le **[Master theorem](https://fr.wikipedia.org/wiki/Master_theorem)**. Il existe plusieurs formes de ce théorème, nous donnons ici sa forme en $\mathcal{O}$ qui est la plus simple à démontrer :

<span id="master-theorem"></span>
{% note "**Forme O du Master Theorem**" %}

Une complexité de la forme :

<div>
$$
C(n) \leq a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)
$$
</div>

est en :

- $C(n)  = \mathcal{O}(n^d \cdot \ln(n))$ si $a=b^d$ (équivalent à $d = \log_b(a)$)
- $C(n)  = \mathcal{O}(n^{\log_b(a)})$ si $a>b^d$
- $C(n)  = \mathcal{O}(n^d)$ si si $a<b^d$

{% endnote %}
{% details "preuve", "open" %}

Comme $C(n) \leq a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)$, il existe $N_0$ tel que pour tout $n \geq N_0$, on a :

<div>
$$
C(n) \leq a \cdot C(\frac{n}{b}) + K\cdot n^d
$$
</div>

On en conclut que si $C'(n) = a \cdot C'(\frac{n}{b}) + K\cdot n^d$ alors $C(n) \leq C'(n)$ pour tout $n$ et donc si $C'(n)$ est en $\mathcal{O}(g(n))$, alors $C(n)$ le sera aussi.

<div>
$$
\begin{array}{lcl}
C'(n) &=&a \cdot C'(\frac{n}{b}) + K\cdot n^d \\
&=& a\cdot (a \cdot C'(\frac{n}{b^2}) + K\cdot (\frac{n}{b})^d) + K\cdot n^d\\
&=& a^2 \cdot C'(\frac{n}{b^2}) + K\cdot n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^2 \cdot (a \cdot C'(\frac{n}{b^3}) + K\cdot (\frac{n}{b^2})^d) + K\cdot n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^3 \cdot C'(\frac{n}{b^3}) + K\cdot n^d \cdot (1 + \frac{a}{b^d} + (\frac{a}{b^d})^2)\\
&=& \dots \\
&=& a^{\log_b(n)}C'(1) + K\cdot n^d \cdot (\sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i)\\
\end{array}
$$
</div>

Comme $a^{\log_b(n)} = \exp(\ln(a) \cdot \frac{\ln(n)}{\ln(b)} ) = \exp(\ln(n) \cdot \frac{\ln(a)}{\ln(b)} ) = n^{\log_b(a)}$ on en conclut, en posant $C'(1) = K'$, que :

<div>
$$
C'(n) = K' \cdot n^{\log_b(a)} + K\cdot n^d \cdot \sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i
$$
</div>

Il y a alors plusieurs cas. Commençons par étudier le cas où $\frac{a}{b^d} = 1$ (équivalent à $d = \log_b(a)$). Dans ce cas, on a :

<div>
$$
C'(n) = K' \cdot n^d + K\cdot n^d \cdot \sum_{i=0}^{\log_b(n)}1 = K\cdot n^d(\log_b(n) + \frac{K'}{K}) = \mathcal{O}(n^d \cdot \ln(n))
$$
</div>

Si $\frac{a}{b^d} \neq 1$, on peut utiliser le fait que $\sum_{i=0}^kx^k = \frac{x^{k+1} -1}{x-1}$ (cette formule  se démontre aisément par récurrence  sur $k$ et est super utile dans plein de calculs de complexité, il est bon de la connaître) pour obtenir :

<div>
$$
\begin{array}{lcl}
C'(n) &=& K\cdot (\frac{K'}{K} \cdot n^{\log_b(a)} + n^d \cdot \frac{(\frac{a}{b^d})^{\log_b(n) +1} -1}{\frac{a}{b^d}-1})\\
\frac{1}{K}\cdot C'(n) &=& \frac{K'}{K} \cdot n^{\log_b(a)} + n^d \cdot \frac{(\frac{a}{b^d})^{\log_b(n) +1} -1}{\frac{a}{b^d}-1}\\
& = & \frac{K'}{K} \cdot n^{\log_b(a)} + n^d \cdot \frac{\frac{a}{b^d}\cdot\frac{n^{\log_b(a)}}{n^d} -1}{\frac{a}{b^d}-1}\\
& =& \frac{K'}{K} \cdot n^{\log_b(a)} + \frac{\frac{a}{b^d}\cdot n^{\log_b(a)} - n^d}{\frac{a}{b^d}-1} \\
& = & (\frac{K'}{K} + \frac{\frac{a}{b^d}}{\frac{a}{b^d} - 1}) \cdot n^{\log_b(a)} - \frac{1}{\frac{a}{b^d} - 1} \cdot n^d
\end{array}
$$
</div>

On en déduit facilement que :

- $\frac{a}{b^d} < 1$ (équivalent à $\log_b(a) < d$) implique $C'(n) = \mathcal{O}(n^d)$
- $\frac{a}{b^d} > 1$ (équivalent à $\log_b(a) > d$) implique $C'(n) = \mathcal{O}(n^{\log_b(a)})$

{% enddetails %}
{% info %}
Le master theorem est la raison pour laquelle vous verrez parfois des complexités avec des exposants non entiers
{% endinfo %}
Dans le cas du tri fusion, on a $a = 2$, $b = 2$  et $d = 1$ donc $a=b^d$ :

## Exemples

### Somme

Soit $T$ un tableau de $n$ entiers relatifs.

{% exercice %}
Donnez un algorithme en $\mathcal{O}(n)$ de signature `max_somme(T: [entier relatif], i: entier) → entier relatif`{.language-} qui calcule :

<div>
$$
\max_{j\geq i}\sum_{i\leq k \leq j}T[k]
$$
</div>

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire un algorithme en $\mathcal{O}(n)$ de signature `max_somme2(T: [entier relatif], i: entier) → entier relatif`{.language-} qui calcule :

<div>
$$
\max_{j \leq i\leq j'}\sum_{j\leq k \leq j'}T[k]
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Les deux exercices précédents doivent vous permettre de trouver un algorithme permettant de trouver :

<div>
$$
\max_{0\leq j \leq j'}\sum_{j\leq k \leq j'}T[k]
$$
</div>

{% exercice %}
Utiliser la méthode diviser pour régner pour créer un algorithme de complexité $\mathcal{O}(n\ln(n))$ permettant de calculer la somme précédente pour un tableau de $n$ entiers relatifs.

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

### Multiplication de matrices

[L'algorithme de Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen) pour multiplier deux matrices  est le plus classique des exemples de diviser pour régner.

On suppose pour cet exercice que l'on cherche à multiplier deux matrices carrées (de dimension $n$) $A$ et $B$, avec $n$ une puissance de 2.

{% info %}
La méthode de Strassen fonctionne de la même manière pour la multiplication de matrices non carrées ou dont le nombre de lignes n'est pas une puissance de 2, il faut juste faire attention lorsque l'on divise par 2.
{% endinfo %}

#### Algorithme naif

{% exercice %}
Donner un algorithme naïf de signature `multiplication(A: [[entier]], B:[[entier]]) → [[entier]]`{.language-} et de complexité $\mathcal{O}(n^3)$ permettant de multiplier deux matrices carrées de $n$ lignes.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

#### Méthode de Strassen

La méthode de Strassen va diviser la multiplication en sous-matrices **puis** utiliser une astuce de calcul.

Commençons par juste decomposer notre problème en sous-problèmes en écrivant la multiplication des matrices $A$ et $B$ par :

<div>
$$
A \cdot B =
\begin{pmatrix}
A_{1,1} & A_{1,2} \\
A_{2,1} & A_{2,2}
\end{pmatrix} \cdot
\begin{pmatrix}
B_{1,1} & B_{1,2} \\
B_{2,1} & B_{2,2}
\end{pmatrix} = \begin{pmatrix}
A_{1,1} \cdot B_{1,1} + A_{1,2} \cdot B_{2,1} & A_{1,1} \cdot B_{1,2} + A_{1,2} \cdot B_{2,2} \\
A_{2,1} \cdot B_{1,1} + A_{2,2} \cdot B_{2,1} & A_{2,1} \cdot B_{1,2} + A_{2,2} \cdot B_{2,2}
\end{pmatrix} =
\begin{pmatrix}
C_{1,1} & C_{1,2} \\
C_{2,1} & C_{2,2}
\end{pmatrix}
$$
</div>

Avec $A_{i, j}$ et $B_{i, j}$ des matrices carrées de taille $n/2$.

{% exercice %}
Exprimez ce calcul par sous-matrices dans un algorithme de type diviser pour régner
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En donner l'équation de récurrence de sa complexité.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire sa complexité. Conclusion ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Pour gagner en complexité il faut faire mieux ! L'astuce est la suivante :

On pose les 7 matrices suivantes :

- $M_1 = (A_{1,1} +A_{2,2}) \cdot (B_{1,1} +B_{2,2})$
- $M_2 = (A_{2,1} +A_{2,2}) \cdot B_{1,1}$
- $M_3 = A_{1,1} \cdot (B_{1,2} - B_{2,2})$
- $M_4 = A_{2,2} \cdot (B_{2,1} - B_{1,1})$
- $M_5 = (A_{1,1} +A_{1,2}) \cdot B_{2,2}$
- $M_6 = (A_{2,1} - A_{1,1}) \cdot (B_{1,1} +B_{1,2})$
- $M_7 = (A_{1,2} - A_{2,2}) \cdot (B_{2,1} +B_{2,2})$

C'est une astuce de taille assez conséquente pour donner lui nom de son inventeur... En effet :

{% exercice %}Montrez que :

- $C_{1, 1} = M_1 + M_4 - M_5 + M_7$
- $C_{1, 2} = M_3 + M_5$
- $C_{2, 1} = M_2 + M_4$
- $C_{2, 2} = M_1 - M_2 - M_3 + M_6$
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

{% exercice %}
Ce nouveau calcul change l'algorithme et l'équation de récursion. Que devient-elle ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire la complexité de ce nouvel algorithme. Conclusion ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Vous voyez que gagner 1 multiplication de matrice fait gagner beaucoup en complexité... Et on peut faire mieux, l'exposant diminue régulièrement au fil du temps et des nouveaux algorithmes. On en est actuellement (en 2025 et à ma meilleure connaissance) à des algorithmes de complexité $\mathcal{O}(n^{2.37286})$.

{% lien %}

- [Les méthodes de multiplications de matrices](https://www.youtube.com/watch?v=DruwS2_cVys) par Josh Alman un des deux co-auteurs de l'algorithme le plus rapide actuel avec un algorithme de complexité $\mathcal{O}(n^{2.37286})$
- [Multiplication de matrices algorithme actuel](https://www.youtube.com/watch?v=HdysaWNs1g8)  par Virginia Vassilevska-Williams, l'autre co-auteur du record actuel

{% endlien %}

#### Inversion de matrice

On suppose que l'on possède un algorithme de multiplication de matrices carrée à $n$ lignes optimal, de complexité $\mathcal{O}(n^\Omega)$ avec $2 \leq \Omega$.

Dans son article séminal, Strassen montre que l'on peut utiliser cet algorithme pour inverser une matrice en utilisant [la formule de l'inversion par bloc](https://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion). Il en conclut que la complexité de l'inversion d'une matrice est identique à la complexité de la multiplication :

{% exercice %}
En utilisant [la formule de l'inversion par bloc](https://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion) et le master theorem, montrez que la complexité de l'inversion de matrice est de la même complexité que le problème de la multiplication de matrice.

{% endexercice %}
{% details "corrigé" %}

Il faut juste calculer 2 inverses $A^{-1}$ et $(D - CA^{-1}B)^{-1}$ puis multiplier un nombre constant de fois des matrices. En utilisant l'algorithme diviser pour régner on arrive à un algorithme de complexité :

<div>
$$
C(n) = \mathcal{O}(n^\Omega) + 2T(n/2)
$$
</div>

Comme $\Omega \geq 2$ le master theorem permet de conclure que $C(n) = \mathcal{O}(n^\Omega)$.
{% enddetails %}

#### Déterminant de matrice

On suppose que l'on possède un algorithme de multiplication de matrices carrées à $n$ lignes optimal, de complexité $\mathcal{O}(n^\Omega)$ avec $2 \leq \Omega$.

Dans son article séminal Strassen montre que l'on peut utiliser cet algorithme pour calculer le déterminant d'un matrice en utilisant [les formules de calcul d'un déterminant par bloc](https://en.wikipedia.org/wiki/Determinant#Block_matrices). Il en conclut que la complexité de l'inversion d'une matrice est identique à la complexité de la multiplication :

{% exercice %}
En utilisant [les formules de calcul d'un déterminant par bloc](https://en.wikipedia.org/wiki/Determinant#Block_matrices) et le master theorem, montrez que la complexité de l'inversion de matrice est de la même complexité que le problème de la multiplication de matrice.

{% endexercice %}
{% details "corrigé" %}

Si $A$ et $D$ sont non inversibles, alors le déterminant de la matrice est nul. Comme le calcul de l'inverse d'une matrice est en $\mathcal{O}(n^\Omega)$, on peut tester en $\mathcal{O}(n^\Omega)$ laquelle des deux matrice est inversible.

En supposant que c'est $A$ la complexité du calcul de $A^{-1}$ et $(D - CA^{-1}B)$ est de $\mathcal{O}(n^\Omega)$. Puis il suffit de calculer 2 déterminant sur des matrices deux fois plus petites. En utilisant l'algorithme diviser pour régner on arrive à un algorithme de complexité :

<div>
$$
C(n) = \mathcal{O}(n^\Omega) + 2T(n/2)
$$
</div>

Comme $\Omega \geq 2$ le master theorem permet de conclure que $C(n) = \mathcal{O}(n^\Omega)$.
{% enddetails %}

### Pavage incomplet du plan

> TBD exo 3 de <https://info-llg.fr/option-mpsi/pdf/08.diviser_pour_regner.pdf>

### Nombre d'inversions

> TBD exo 4 de <https://info-llg.fr/option-mpsi/pdf/08.diviser_pour_regner.pdf>
