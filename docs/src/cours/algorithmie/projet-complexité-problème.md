---
layout: layout/post.njk
title: "Projets : complexités de problèmes algorithmiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous montrerons ici quelques problème ainsi que des algorithmes permettant d'atteindre leur complexité.

## Col de tableaux

> - **Utilité** : à connaître car un classique des concours (on le donne sans indications...)
> - **Difficulté** : facile

Le but de cet exercice est d'étudier les **_cols_** d'un tableau.

{% note2 "**Définition**" %}
Un **_col_** d'un tableau d'entiers $T$ de taille $n > 1$ est un indice $0 \leq i < n$ tel que :

- soit $i = 0$ et $T[i] \leq T[1]$
- soit $i = n-1$ et $T[i] \leq T[n-2]$
- soit $0 < i < n-1$ et $T[i] \leq \min(T[i-1], T[i+1])$

{% endnote2 %}

### Existence

{% exercice %}
Montrer que tout tableau d'entiers $T$ de taille $n > 1$ contient au moins 1 col.
{% endexercice %}
{% details "corrigé" %}

On donne trois preuves possibles.

#### En reprenant la définition

Si la première condition ($i=0$) est vérifiée, le tableau contient un col. On la suppose donc non vérifiée : $T[0] > T[1]$. De même, si la seconde condition ($i=n-1$) est vérifiée, le tableau contient également un col. Supposons la donc également non vérifiée : $T[n-2] < T[n-1]$.

Les deux conditions précédentes montrent qu'il existe $n-1 > i^\star > 0$ le plus petit indice tel que $T[i^\star] \leq T[i^\star +1]$. On a alors : $T[i^\star -1] > T[i^\star ] \leq T[i^\star +1]$ et $i^\star$ est un col.

#### On utilise une astuce

Un tableau d'entier possède forcément un élément minimum. Il existe donc $i^\star$ tel que $T[i^\star] \leq T[i]$ pour tout $0 \leq i < n$. De là :

- soit $i^\star = 0$ et $T[i^\star] \leq T[1]$
- soit $i^\star = n-1$ et $T[i^\star] \leq T[n-2]$
- soit $0 < i^\star < n-1$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$

Simple et efficace, non ?

#### Par récurrence

On montre par récurrence sur la taille $n$ du tableau qu'il existe toujours un col.

1. Initialisation. Si $n=2$ soit $T[0] \leq T[1]$ soit $T[0] \geq T[1]$ (ce qui est équivalent pour $n=2$ à $T[n-1] \leq T[n-2]$). Ces deux cas correspondent aux deux premières possibilités pour un col
2. on suppose la propriété vrai pour $n \geq 2$. Et on se donne un tableau $T$ de taille $n+1$.
3. l'hypothèse de récurrence stipule que le tableau $T'$ constitué des $n$ premières cases de $T$ ($T'= T[:-1]$) possède un col, disons à l'indice $i^\star$. 3 cas sont possibles :
   1. $i^\star = 0$ et $T'[0] \leq T'[1]$ ce qui implique $T[0] \leq T[1]$ : $i^\star$ est aussi un col pour $T$
   2. $0 < i^\star < n-1$ et $T'[i^\star] \leq \min(T'[i-1], T'[i+1])$ ce qui implique $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
   3. $i^\star = n-1$ et $T'[n-1] \leq T'[n-2]$ ce qui implique $T[n-1] \leq T[n-2]$. On conclut en remarquant que :
      1. soit $T[n] \geq T[n-1]$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
      2. soit $T[n] < T[n-1]$ et $n$ est un col pour $T$.



{% enddetails %}

### Découverte

{% exercice %}
Donnez un algorithme nommé `trouve(T)`{.language-} permettant de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre en $\mathcal{O}(n)$ opérations.

Vous expliciterez :

- que la complexité de votre algorithme est bien celle demandée,
- qu'il trouve bien un col.

{% endexercice %}
{% details "corrigé" %}

La preuve de la 1ère question montrant qu'il existe forcément un col, l'algorithme suivant qui mime directement la définition (lignes 2-3 : 1ère condition, lignes 5-6 : 2ème condition et lignes 8-10 la troisième condition) trouvera forcément un col :

```pseudocode
algorithme trouve(T: [entier]) → entier:  # T.longueur > 1
    si T[0] <= T[1]:
        rend 0

    si T[-1] <= T[-2]:
        rendre T.longueur - 1

    pour chaque (i := entier) de [1 .. T.longueur - 1[:
        si T[i] <= min(T[i-1], T[i + 1]):
            rendre i

```

Sa complexité dans le cas le pire a lieu pour les tableaux dont le premier et seul col se trouve à l'avant dernier indice (comme pour la liste $[5, 4, 3, 2, 1, 2]$ par exemple), forçant l'algorithme à :

- faire échouer le 1er test de la ligne 2 en $\mathcal{O}(1)$ opérations
- faire échouer le 2er test de la ligne 5 en $\mathcal{O}(1)$ opérations
- faire les $\mathcal{O}(n)$ itérations de la boucle for en :
  - faisant échouer tous les tests sauf le dernier $\mathcal{O}(1)$ opérations
  - réussissant le dernier test et en faisant un retour de fonction en $\mathcal{O}(1)$ opérations

La complexité totale maximale est alors :

$$
C(n) = \mathcal{O}(1) + \mathcal{O}(1) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) = \mathcal{O}(n)
$$

On peut aussi utiliser la preuve précédente et _simplifier_ la boucle `pour chaque`{.language-} en gardant la même complexité :

```pseudocode
algorithme trouve(T: [entier]) → entier:  # T.longueur > 1
    si T[0] <= T[1]:
        rend 0

    si T[-1] <= T[-2]:
        rendre T.longueur - 1

    pour chaque (i := entier) de [1 .. T.longueur - 1[:
        si T[i] <= T[i + 1]:
            rendre i

```

{% enddetails %}

### Rapidité

{% exercice %}
Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.


```pseudocode
algorithme trouve_vite(T: [entier]) → entier:    # T.longueur > 1
    si T[0] <= T[1]:
        rendre 0

    si T[-1] <= T[-2]:
        rendre T.longueur - 1

    début ← 0
    fin ← T.longueur - 1

    tant que Vrai:
        milieu ← (fin + début) // 2
        si T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            rendre milieu

        si T[milieu] > T[milieu - 1]:
            fin ← milieu
        sinon:
            début ← milieu
```

{% details "code python" %}

```python/
def trouve_vite(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    début = 0
    fin = len(T) - 1

    while True:
        milieu = (fin + début) // 2
        if T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            return milieu

        if T[milieu] > T[milieu - 1]:
            fin = milieu
        else:
            début = milieu

```

{% enddetails %}
{% endexercice %}
{% details "corrigé" %}

La preuve d'existence du 1 montre que pour tout $i + 1 < j$, si $T[i] > T[i+1]$ et $T[j] > T[j-1]$, alors il existe un indice $i < k < j$ tel que $k$ soit un col de la matrice.

L'invariant de boucle de la boucle `tant que`{.language-} est alors :

> **Invariant de boucle :** A la fin de chaque itération de la boucle `tant que`{.language-}, soit :
>
> - `T[milieu]`{.language-} est un col
> - `T[milieu]`{.language-} n'est pas un col et :
> - `début + 1 < fin`{.language-}
> - `T[début] > T[début+1]`{.language-} et `T[fin] > T[fin-1]`{.language-}

A la fin de la première itération, on a soit :

- `T[milieu] <= min(T[milieu - 1], T[milieu + 1])`{.language-} et `milieu`{.language-} est un col
- `fin' = milieu`{.language-} et `début' = début`{.language-} si `T[milieu] > T[milieu -1]`{.language-}. Comme initialement `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu - 1 > début`{.language-} puisque `T[0] > T[1]`{.language-} et l'invariant est vérifié.
- `fin' = fin`{.language-} et `début' = milieu`{.language-} si `T[milieu] <= T[milieu -1]`{.language-} et `T[milieu] > T[milieu + 1]`{.language-}. Comme `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu + 1 < fin`{.language-} puisque `T[-1] > T[-2]`{.language-} et l'invariant est vérifié.

La même démonstration fonctionne à l'identique à la fin de l'itération $i+1$ si l'invariant est vrai à la fin de l'itération $i$.

Comme `fin - début >= 0` et diminue strictement à chaque itération de la boucle `tant que`{.language-}, il arrivera **forcément** un moment où `milieu`{.language-} sera un col.

{% enddetails %}
{% exercice %}
Donnez la complexité de l'algorithme `trouve_vite(T)`{.language-}.
{% endexercice %}
{% details "corrigé" %}
La procédure de la boucle `tant que`{.language-} est identique à la recherche dichotomique puisque l'on se place toujours au milieu de l'espace de recherche. Le cours nous indiquant que la complexité de la recherche dichotomique est $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$, on en conclut que l'algorithme `trouve_vite(T)`{.language-} est également en $\mathcal{O}(\ln(n))$ opérations.

{% enddetails %}


### Complexité du problème

{% exercice %}
Après avoir formalisé le problème de la recherche d'un col dans un tableau, vous démontrerez que sa complexité est égale à la complexité de l'algorithme `trouve_vite(T)`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Il existe des tableaux ayant tous un unique col en position $i$ pour tout $0 \leq i < n$ (prenez les tableaux $[0, -1, \dots, -i, -i+1, -i +2, \dots, -i + (n - i - 1)]$). Tout algorithme trouvant les col des tableaux doit donc pouvoir distinguer parmi $n$ cas : il est au moins de complexité $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$.

Comme l'algorithme `trouve_vite(T)`{.language-} est de complexité $\mathcal{O}(\ln(n))$, c'est borne min est atteinte.

{% enddetails %}

## Tours de Hanoï

> - **Utilité** : classique parmi les classique. La preuve que la complexité est minimale est à connaître
> - **Difficulté** : moyen

[Les _tours de Hanoï_](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF) sont un célèbre casse tête inventé par Édouard Lucas.

Il consiste à déplacer $n$ disques de diamètres différents d'une tour de _"départ"_ à une tour d' _"arrivée"_ en passant par une tour _"intermédiaire"_, tout en respectant les règles suivantes :

- on ne peut déplacer qu'un disque à la fois
- on ne peut placer un disque sur un disque plus petit que lui.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

{% lien %}
[Une interface pour jouer aux tours de Hanoï](http://championmath.free.fr/tourhanoi.htm).

Déplacez les disques par glisser/déposer.
{% endlien %}

Essayons de résoudre ce problème de façon optimale.

### Algorithme récursif

{% exercice %}
Donnez un algorithme récursif permettant de résoudre le problème. 
{% endexercice %}
{% info %}
On pourra supposer que : 

- les disques sont des entiers de diamètres allant de 1 à $n$
- les 3 tours, nommées $A$, $B$ et $C$, seront des tableaux de longueur $n$ contenant :
  - en 1er élément le nombre de disques de la tour
  - les diamètres de ses disques dans l'ordre à partir de l'élément d'indice 1

On pourra supposer qu'on a un algorithme `Hanoï(nombre, départ, arrivée, intermédiaire)`{.language-} permettant de déplacer les $n$ disques supérieurs d'une tour de départ à une tour d'arrivée avec la dernière tour comme tour de transit.

{% endinfo %}
{% details "corrigé" %}

On suppose que l'on a les trois emplacements de tours A, B et C ; et que l'on veuille déplacer les disques de la tour A vers la tour C.

1. pour pouvoir déplacer le plus grand disque de la tour A, il faut avoir déplacé tous les disques au-dessus de lui. Comme c'est le plus grand disque, il est de plus seul sur son emplacement
2. une fois le plus grand disque seul sur sa tour, il faut le déplacer en C (ce disque peut être en B ou en A)
3. une fois le plus grand disque à sa place, il convient de déplacer la tour formée des autres disques sur l'emplacement C.

On a donc l'algorithme suivant :

```pseudocode
fonction déplace(départ: [entier], arrivée: [entier]):
    (disque := entier) ← départ[départ[0]]
    départ[0] ← départ[0] - 1 
    arrivée[0] ← arrivée[0] + 1 
    arrivée[arrivée[0]] ← disque

algorithme Hanoï(nombre: entier, départ: [entier], arrivée: [entier], intermédiaire: [entier]):
    si nombre > 0:
        Hanoï(nombre - 1, départ, intermédiaire, arrivée)  # déplace n-1 à intermédiaire
        déplace(départ, arrivée)                           # place le premier disque
        Hanoï(nombre - 1, intermédiaire, arrivée, départ)  # déplace n-1 de intermédiaire à arrivée

```

Comme les tableau sont mutables, les objets sont déplacés dans le tableau on a besoin de ne rien rendre.

{% enddetails %}
{% exercice %}
Quel est le nombre de récursion de votre algorithme ? En déduire sa complexité.
{% endexercice %}
{% details "corrigé" %}

Si $N(n)$ est le nombre de récursions. déplacements pour résoudre le problème de la tour de Hanoï, il faut donc au moins :

1. déplacer une tour de $n-1$ éléments : $1 + N(n-1)$ récursions
2. re-déplacer une tour de $n-1$ éléments : $1 + N(n-1)$ récursions

On a donc un nombre de récursion de : 

<div>
$$
N(n) = 
\begin{cases}
2 + 2 \cdot N(n-1) & \text{si } n > 0\\
0 & \text{sinon}
\end{cases}
$$
</div>


On obtient facilement l'expression, pour $n\geq 1$ :

<div>
$$
N(n) = 2^n
$$
</div>


Comme, hors récursion, l'algorithme effectue $\Theta(1)$ opérations, la complexité $C(n)$ de l'algorithme vaut $C(n) = \Theta(1) \cdot N(n) + \Theta(1)$ (le dernier $\mathcal{O}(1)$ vient du fait que pour $n =0$ il n'y a pas de récursion mais tout de même $\Theta(1)$ opérations).

On a donc au final une complexité valant :

<div>
$$
C(n) = \Theta(2^n)
$$
</div>

{% enddetails %}
{% exercice %}
Donnez un code python permettant d'implémenter cet algorithme ainsi qu'un exemple d'exécution.
{% endexercice %}
{% details "corrigé" %}

On a utilisé des listes qui permettent d'ajouter ou de supprimer des éléments. Cela ne change pas la complexité (on le justifiera plus tard, lorsque l'on étudiera [les structures de listes](../structure-liste/){.interne})

```python
A = list(range(5, 0, -1))
B = []
C = []

def déplace(départ, arrivée):
    disque = départ.pop()
    arrivée.append(disque)

def Hanoi(n, départ, arrivée, intermédiaire):
    if n == 0:
        return
    Hanoi(n-1, départ, intermédiaire, arrivée)
    déplace(départ, arrivée)
    print(A, B, C)
    Hanoi(n-1, intermédiaire, arrivée, départ)

print(A, B, C)
Hanoi(len(A), A, C, B)
```

{% enddetails  %}


### Complexité du problème

{% exercice %}
Donnez le nombre de déplacement effectué par notre algorithme.
Peut-on faire mieux ?
{% endexercice %}
{% details "corrigé" %}

Si $D(n)$ est le nombre de déplacements pour résoudre le problème de la tour de Hanoï, il faut donc au moins :

1. déplacer une tour de $n-1$ éléments pour pouvoir déplacer le dernier disque  : nombre de déplacement $D(n-1)$
2. déplacer le dernier disque 
3. re-déplacer une tour de $n-1$ éléments sur le dernier disque : nombre de déplacement  $D(n-1)$

On a donc l'inégalité : $D(n) \leq 1 + 2 \cdot D(n-1)$ pour tout algorithme de déplacement. Comme on a l'égalité pour notre algorithme, il est optimal.

Le nombre minimal de déplacement est :

<div>
$$
D(n) = 
\begin{cases}
1 + D(n-1) + D(n-1) = 1 + 2\cdot C(n-1) & \text{si } n > 0\\
0 & \text{sinon}
\end{cases}
$$
</div>

On obtient facilement l'expression, pour $n\geq 1$ :

<div>
$$
D(n) = \sum_{i=0}^{n-1}2^i + 2^n\cdot D(0) = \sum_{i=0}^{n-1}2^i = 2^n-1
$$
</div>

Le lecteur averti se sera rendu compte que c'est exactement notre complexité.

{% enddetails  %}

## Algorithmes arithmétique


> - **Utilité** : pour la culture générale et si vous voulez faire de l'informatique plus tard
> - **Difficulté** : difficile


> TBD intro avec le nombre de bit d'un entier
> dire lorsque nombre infini forcément pas O(1). Exemple binaire

### Somme

### Multiplication

#### Naive

#### Karatsuba

> TBD [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba)

#### Peut-on mieux faire ?

> TBD borne min
>  Puis parler de Strassen et de l'optimal <https://fr.wikipedia.org/wiki/Algorithme_de_multiplication_d%27entiers> et <https://math.univ-lyon1.fr/~roblot/resources/ens_partie_2.pdf>
> conjecture
> nb tres tres grand pour que ca marche
> en pratique on fixe la taille

### Conclusion

> TBD c'est pour ça que parfois on sépare somme et multiplication dans le calcul de la complexité (cf. polynôme dans les calculs de complexité).


