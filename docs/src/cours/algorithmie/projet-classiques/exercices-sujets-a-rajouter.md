---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD regardez tous les exos d'avant et le remettre s'ils sont chouettes, genre ceux des piles/file, fibo, etc. Et ajouter les questions suivantes si nécessaire.

## 2-sum et 3-sum

> TBD ajouter exos pour dictionnaires.
> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n)$ en moyenne avec dico. Ne change rien pour 3-SUM, il faut le faire n fois.
>
> TBD pas toujours la meilleur solution le dico : faire lièvre et lapin (qu'on aura vu dans algo classiques) pour deux tableaux avec égalité mieux que dictionnaire.

## Decurryfications

> TBD McCarty, Ackerman, etc.

#### Ackermann, le retour

Essayons de voir comment écrire l'algorithme d'Ackermann sans toutes ces récurrences, comme on l'a fait avec la fonction 91.

Pour calculer $\text{Ack}(m, n)$ :

1. soit $m=0$ alors $A = n+1$
2. soit $m>0$ et $n=0$ et alors $A = \text{Ack}(m-1, 1)$
3. soit $m>0$ et $n>0$ et alors :
     1. $A = \text{Ack}(m, n-1)$
     2. $A = \text{Ack}(m-1, A)$

On voit que ce n'est pas une formulation récursive terminale à cause du troisième cas. En 3.2 :

- on utilise la valeur de $A$ calculée en 3.1
- on utilise la valeur que valait $m$ avant 3.1

Il faut donc se rappeler de $m$ pour le calcul de 3.2 tout en utilisant la valeur de $A$ calculée précédemment. Pour ce genre de récursion, on peut utiliser une [TODO list](https://fr.wikipedia.org/wiki/To-do_list) qui nous permet de nous rappeler toutes les tâches à effectuer et des variables à sauvegarder :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs et $A$ à 0
3. on ajoute à la liste le triplet (1, m, n)
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste)
      1. si le premier élément de l'item vaut 1 alors on affecte :
         1. $m$ au second élément du triplet
         2. $n$ au troisième élément du triplet
      2. si le premier élément vaut 2 alors on affecte :
         1. $m$ au second élément du triplet
         2. $A$ à $n$
   2. On fait le calcul :
      1. si $m=0$ alors $A=n+1$
      2. si $m>0$ et $n=0$ alors on ajoute $(1, m-1, 1)$ à la TODO list
      3. si $m>0$ et $n>0$ alors :
          - on ajoute $(2, m-1)$ à la TODO list
          - on ajoute $(1, m, n-1)$ à la TODO list
5. rendre $A$

> TBD faire $A(2, 3)$

On peut même se passer de $A$ complètement :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs
3. on ajoute à la liste l'entier $m$
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste) et en l'affectant à $m$
   2. On a un choix selon les valeurs de $m$ et $n$ :
      - si $m=0$ alors $n=n+1$
      - si $m>0$ et $n=0$ alors (récursion terminale):
          - $n = 1$
          - ajoute l'entier $m-1$ à la TODO  List
      - $m>0$ et $n>0$ alors :
          - ajoute l'entier $m-1$ à la TODO  List
          - ajoute l'entier $m$ à la TODO  List
          - $n=n-1$
5. rendre $A$

{% info %}
Implémentation en python en utilisant une liste comme TODO-list :

```python
def Ack(m, n):
    s = [m]
    while (s):
        m = s.pop()
        if m == 0:
            n += 1
        elif n == 0:
            s.append(m - 1)
            n = 1
        else:
            s.append(m - 1)
            s.append(m)
            n -= 1
        return n
```

{% endinfo %}

> pas récursivité terminale = il faut faire des trucs en plus de la récursion. Il faut se rappeler de que l'on veut faire. Avec une TODO list (faire exemple avec ack petit) = pile en informatique
> faire un item de la todo list = dépile.
>

> 
> truc à faire = empile
> <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#conversion-using-stacks>
> 1. curryfication puis decurryfication
> A(m, n) = A(0, n')
> A'(s, n) = A'(s[:-1], A(s[-1], n))
> A'([m], n) = A(m, n) par récurrence sur m+n = k
>
> TBD faire la preuve que c'est ok (voir <https://stackoverflow.com/a/54356919>)

{% info %}
Notez que tout algorithme récursif peut s'écrire de façon itérative avec une TODO-list (une pile).
{% endinfo %}

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

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est une _sous-séquence_ de $S_1$ si il existe une fonction strictement croissante

$$
f : \{0,\ldots, len(S_2)-1\} \longrightarrow \{0,\ldots, len(S_1)-1\}
$$

Telle que $S_1[f(j)] = S_2[ j]$ pour tout $j$ de $\{0,\ldots, len(S_2)-1\}$.

Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.

### Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $0$ à $len(S_2) - 1$.

- Proposez, prouver et donner la complexité d'un algorithme qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(len(S_1))$ pour résoudre ce problème.

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

## Odds and ends

> TBD ajouter : k-médiane (voir et 20/21 mpci.)

> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.
> TBD exos : <https://www.inf.usi.ch/carzaniga/edu/algo19s/exercises.pdf>

> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n^2)$
> 3-SUM $T[i] + T[j] + T[k] = 0$ en $\mathcal{O}(n^3)$ (en modifiant 2-sum avec $T[i] + T[j] = K$) puis en $\mathcal{O}(n^2)$ (avec tri). Faire tout est tout aussi rapide que faire 1.

> TBD lièvre et lapin.
