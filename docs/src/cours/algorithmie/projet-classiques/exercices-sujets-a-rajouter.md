---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD a ajouter plus tard.

## Min et max d'un tableau d'entiers

On compte précisément les comparaisons (comme on l'a fait en comptant les multiplications avec le problème de l'exponentiation)

- juste min
- juste max
- faire les deux ensemble

### corrigé : Min et max d'un tableau d'entiers

> TBD

Si on fait les deux à la suite on a 2n comparaisons.

On commence par trier les éléments $T[i]$ et $T[i+1]$ pour tout $i$ ($n/2$ comparaisons)

Puis on cherche le min sur les $T[[2i]$ ($n/2$ comparaisons) et le max sur les $T[[2i +1]$ ($n/2$ comparaisons)

## Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>

- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

### Corrigé Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>

- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

## Chaînes de caractères

### Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est une {\em sous-séquence} de $S_1$ si il existe une fonction strictement croissante

$$
f : \{0,\ldots, len(S_2)-1\} \longrightarrow \{0,\ldots, len(S_1)-1\}
$$

Telle que $S_1[f(j)] = S_2[ j]$ pour tout $j$ de $\{0,\ldots, len(S_2)-1\}$.

Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.

### Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $0$ à $len(S_2) - 1$.

- Proposez, prouver et donner la complexité d'un algorithme qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(len(S_1))$ pour résoudre ce problème.

## Algorithme mystère

L'algorithme suivant, à partir d'une liste d'entiers positifs, rend une autre liste. On suppose pour cet exercice que la création des deux listes tempo et sortie est en $\mathcal{O}(1)$ opérations.

```python
def mystère(tab):
    k = max(tab)
    tempo = [0] * (k + 1)
    sortie = [0] * len(tab)

    for i in range(len(tab)):
        tempo[tab[i]] += 1
    for i in range(1, k + 1):
        tempo[i] += tempo[i - 1]

    for i in range(n):
        sortie[i] = tempo[tab[i]] - 1
        tempo[tab[i]] -= 1

    return sortie

```

- Donnez la complexité de cet algorithme.
- Dites ce qu'il fait et prouvez le (_indication_: après chacune des deux premières boucles, que contient tempo ?).
- Commentaires ?

## Permutation circulaire

Étant donné un liste $L$ de longueur $n$ et un entier $k$, le problème est de transformer $L$ par permutation circulaire en décalant (circulairement) tous les éléments de $L$ de $k$ places. Par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $L' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

- Donnez un algorithme $\text{Permut}(L, k)$ qui, avec une liste $L$ et un entier $k$ en entrées, construit une nouvelle liste $L'$, permutation circulaire de $L$.
- Si on veut transformer $L$ en $\text{Permut}(L,k)$, montrez que la place mémoire utilisée (en plus de celle des données du problème ($L$)) par votre algorithme est $O(n)$.

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $O(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

- Donnez un algorithme en $O(n)$ et utilisant $O(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.
- Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}), alors \text{Permut}(L, k) = (A^RB^R)^R$.
- Déduisez-en un algorithme de complexité $O(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $O(1)$ espace mémoire supplémentaire.

## Algorithmes arithmétique

- addition de listes de chiffres
- multiplications de listes de chiffres

(- [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba))

## Matrices

- structure
- addition
- produit par un scalaire
- produit naïf

(- [produit de Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen))

## Méthodes de tri

### Tri par monotonies

Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. Par exemple :
si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

Donnez un algorithme qui, étant donné un tableau $T$ construit une liste (de listes) $L$, chaque élément de $L$ étant une monotonie de $T$ (et vice versa). À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.

Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$ (ceci est aussi une question de cours).

Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.

En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.

Cet algorithme est en fait une variante d'un algorithme vu en cours. Lequel ?

## Odds and ends

> TBD ajouter : k-médiane (voir et 20/21 mpci.)

> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.
> TBD exos : <https://www.inf.usi.ch/carzaniga/edu/algo19s/exercises.pdf>

> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n^2)$
> 3-SUM $T[i] + T[j] + T[k] = 0$ en $\mathcal{O}(n^3)$ (en modifiant 2-sum avec $T[i] + T[j] = K$) puis en $\mathcal{O}(n^2)$ (avec tri). Faire tout est tout aussi rapide que faire 1.

> TBD lièvre et lapin.
