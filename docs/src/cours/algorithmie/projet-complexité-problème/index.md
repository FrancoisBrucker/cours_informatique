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

```pseudocode/
algorithme trouve(T: [entier]) → entier:  # T.longueur > 1
    si T[0] ≤ T[1]:
        rend 0

    si T[-1] ≤ T[-2]:
        rendre T.longueur - 1

    pour chaque (i := entier) de [1 .. T.longueur - 1[:
        si T[i] ≤ min(T[i-1], T[i + 1]):
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
    si T[0] ≤ T[1]:
        rend 0

    si T[-1] ≤ T[-2]:
        rendre T.longueur - 1

    pour chaque (i := entier) de [1 .. T.longueur - 1[:
        si T[i] ≤ T[i + 1]:
            rendre i

```

{% enddetails %}

### Rapidité

{% exercice %}
Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.


```pseudocode
algorithme trouve_vite(T: [entier]) → entier:    # T.longueur > 1
    si T[0] ≤ T[1]:
        rendre 0

    si T[-1] ≤ T[-2]:
        rendre T.longueur - 1

    (début := entier) ← 0
    (fin := entier) ← T.longueur - 1

    tant que Vrai:
        milieu ← (fin + début) // 2
        si T[milieu] ≤ min(T[milieu - 1], T[milieu + 1]):
            rendre milieu

        si T[milieu] > T[milieu - 1]:
            fin ← milieu
        sinon:
            début ← milieu
```

{% endexercice %}
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
Donnez le nombre de déplacements effectués par notre algorithme.
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

## <span id="point-fixe"></span>Algorithme de recherche de point fixe

> - **Utilité** : exercice classique des concours relevés donc donné sans trop d'explications
> - **Difficulté** : difficile

Nous allons étudier le problème algorithmique suivant :

{% note2 "**Définition**" %}

Une suite $(a_i)_{0\leq i}$ est dite _ultimement périodique_ si il existe $\lambda$ et $\mu$ tels que :

- les valeurs $a_0$ à $a_{\lambda + \mu - 1}$ sont distinctes
- $a_{ n + \lambda} = a_{ n }$ pour tout $n\geq \mu$

{% endnote2 %}

{% note2 "**Problème algorithmique**" %}

- Nom : Point fixe
- Entrée : une suite $(a_i)_{0\leq i}$ ultimement périodique
- Sortie : $\mu$

{% endnote2 %}

Cet problème est magnifique car :

- la complexité du problème est linéaire,
- l'algorithme optimal est tout simple mais sa démonstration ne l'est pas.

L'exercice est difficile mais sa beauté vaut le coût qu'on s'y arrache (un peu) les cheveux (si on en a).

### Analyse préliminaire

Une suite  ultimement périodique ressemble à un $\rho$ (rho) :

![rho](rho.png)

{% exercice %}

Donnez les $\lambda$ et $\mu$ pour la suite représentée par la figure précédente.

{% endexercice %}
{% details "corrigé" %}

- $\lambda = 7$
- $\mu = 3$
  
{% enddetails %}

{% exercice %}

Montrez que si $(a_i)_{i\geq 0}$ est ultimement périodique alors les entiers $\lambda$ et $\mu$ sont uniques.

{% endexercice %}
{% details "corrigé" %}

De part la définition la suite a $\lambda + \mu -1 $ valeurs distinctes de $a_0$ à $a_{ \mu + \lambda -1}$. La somme $\lambda + \mu$ est donc unique. De plus, tous les $m$ tels que $a_{ \mu + m} = a_{ \mu }$, sont multiples d'une valeur qui est l'unique $\lambda$ possible (pour garantir l'unicité des $\lambda + \mu -1 $ premières valeurs de la suite).

{% enddetails %}

{% exercice %}
Montrez que le problème de la recherche de point fixe de $(a_i)_{i\geq 0}$ est en $\Omega(\lambda + \mu)$.
{% endexercice %}
{% details "corrigé" %}

Il faut forcément parcourir les $\lambda + \mu -1$ premiers éléments de la suite pour garantir qu'ils sont tous différents et s'assurer que $a_{ \mu + \lambda} = a_{ \mu }$

{% enddetails %}

### Algorithme naïf

Résoudre le problème du point fixe va nécessiter un de travail. Commençons par étudier cet algorithme :

```pseudocode
algorithme point_fixe_naïf(a: (int) → int) → int
    (i := entier) ← 0
    (j := entier)

    tant que Vrai:
        i ← i + 1
        j ← 0
        tant que j < i:
            si a(i) == a(j):
                rendre j
            j ← j + 1
```

Remarquez que le paramètre de l'algorithme est une fonction. [Le type d'une fonction est sa signature](/cours/algorithmie/pseudo-code/algorithmes-fonctions/#type).


{% exercice %}
Montrer que l'algorithme `point_fixe_naïf`{.language-} résout le problème du point fixe.
{% endexercice %}
{% details "corrigé" %}

Si la suite est ultimement périodique, il existe $j < i$ tel que $a(i) == a(j)$. Ceci prouve :

- la finitude de notre algorithme
- son exactitude : puisque pour tout $i>0$ on teste tous les $j < i$

{% enddetails %}
{% exercice %}
Quelle est sa complexité ?
{% endexercice %}
{% details "corrigé" %}

L'algorithme va s'arrêter au plus petit $i$ tel qu'il existe $j < i$ tel que $a(i) == a(j)$ : $i = \lambda + \mu$ et $j = \mu$. Comme on à essayés tous couples plus petit la complexité est :


<div>
$$
\begin{array}{lcl}
C(\lambda, \mu) &=& \sum\limits_{i < \lambda + \mu} {(\sum\limits_{i > j}\mathcal{O}(1))} + \mu \cdot \mathcal{O}(1) \\
&=& \mathcal{O}((\lambda + \mu)^2) \cdot \mathcal{O}(1) + \mu \cdot \mathcal{O}(1) 
&=& \mathcal{O}((\lambda + \mu)^2)
\end{array}
$$
</div>


{% enddetails %}

### Algorithme optimal

{% exercice %}

Soit $(a_i)$ une suite ultimement périodique de paramètres $\lambda$ et $\mu$. Montrez qu'il existe $\mu \leq m \leq \lambda +\mu$ tel que $a_{m} = a_{2m}$.

{% endexercice %}
{% details "corrigé" %}

À chaque étape l'écart entre le lièvre et la tortue est augmenté de 1. Une fois la tortue et le lièvre sur le cycle il va forcément arriver un moment où le lièvre va prendre un tour à la tortue, et ceci va arriver avant que la tortue n'ait fait un tour de cycle complet.

Formalisons ça. Lorsque $m = \mu$, on a $a_{2\mu} = a_{\mu + k} =  a_{m + k}$ avec $0 \leq k \leq \lambda$ puisque l'on se trouve sur le cycle de longueur $\lambda$.

Si $k=0$ ou $k=\lambda$ on a bien trouvé notre $m$ et sinon, comme $a_{2(\mu + p)} = a_{2\mu + 2p} = a_{\mu + 2p + k} = a_{(\mu + p) + p + k}$ en prenant $0 < p = \lambda - k < \lambda$ on a bien $a_{2(\mu + p)} = a_{(\mu + p) + \lambda} = a_{(\mu + p)}$ ce qui conclut la preuve.

{% enddetails %}

L'exercice précédent est la pierre angulaire de l'algorithme optimal ! Cet algorithme s'appelle [l'algorithme du lièvre et de la tortue](https://fr.wikipedia.org/wiki/Algorithme_du_li%C3%A8vre_et_de_la_tortue) et est décrit ci-après :

```pseudocode
programme lièvre_tortue(a: (entier) → entier) → entier:

    (tortue := entier) ← 1
    (lièvre := entier) ← 2

    tant que a(tortue) ≠ a(lièvre):
        tortue ← tortue + 1
        lièvre ← lièvre + 2

```

{% exercice %}
Montrez que l'algorithme précédent rend un indice $m$ tel que :

- $\mu \leq m \leq \lambda +\mu$ 
- $a_{m} = a_{2m}$

{% endexercice %}
{% details "corrigé" %}

À la fin de chaque étape le lièvre vaut 2 fois la tortue et s'arrête au premier élément ou il y a égalité. O sait que c'est élément est entre $\mu$ et $\lambda + \mu$. 

{% enddetails %}

Et il le fait vite !

{% exercice %}
Montrez que la complexité de l'algorithme `lièvre_tortue`{.language-} est en $\mathcal{O}(\lambda + \mu)$
{% endexercice %}
{% details "corrigé" %}

Comme la valeur de la tortue est inférieure à $\lambda + \mu$, il n'y a eu au pire que $\lambda + \mu$ itérations d'une boucle en $\mathcal{O}(1)$.

{% enddetails %}

On peut maintenant s'atteler à trouver $\lambda$ et $\mu$. 

{% exercice %}
Soit $m$ avec $\mu \leq m \leq \lambda +\mu$ tel que $a_{m} = a_{2m}$. Montrez que $m$ est un multiple de $\lambda$.
{% endexercice %}
{% details "corrigé" %}

Puisque $m\geq \mu$ on est sur le cycle de longueur $\lambda$. Donc pour que $a_{m} = a_{2m}$ il faut que $2m = m + k\lambda$ ce qui montre que $m$ est un multiple de $\lambda$.

{% enddetails %}

{% exercice %}
Utilisez la question précédente et la nature de $m$ pour montrer que $\mu = b + k \cdot \lambda$ avec $b = \mu + \lambda - m$.

{% endexercice %}
{% details "corrigé" %}

La division entière de $\mu$ par $\lambda$ donne $\mu = b + k \cdot \lambda$ avec $b < lambda$. Comme de plus $\mu \leq m \leq \mu + \lambda$, on a $b + k \cdot \lambda \leq m \leq b + (k + 1) \cdot \lambda$.

Or $m$ est un multiple de $k$, on ne peut donc avoir que $m = (k+1) \cdot \lambda$. En injectant cette égalité dans $\mu$ on obtient : $\mu = b + k \cdot \lambda = b + (m - \lambda)$ ce qui conclut la preuve.

{% enddetails %}

<div id="point-fixe-mu"></div>

{% exercice %}
Déduire de ce qui précède un algorithme de signature `mu(a: (entier) → entier) → entier`{.language-} qui résout le problème du point fixe avec une complexité temporelle $\Theta(\lambda + \mu)$ et de complexité spatiale $\mathcal{O}(1)$.

{% endexercice %}
{% info %}
Où se rencontrent deux tortues démarrant en $a_m$ et en $a_0$ respectivement ?
{% endinfo %}
{% details "corrigé" %}

La question précédente a montré que $\mu + m = (\mu + \lambda) + \lambda = \mu + 2\cdot \lambda$.

En faisant partir deux tortue, l'une en 0 et l'autre en $m$, lorsque celle partant en $0$ arrivera en $\mu$ celle parti de $m$ sera en $\mu + m = \mu + 2\cdot \lambda$, donc au même point !

>TBD fin

{% enddetails %}

### Application

L'algorithme du lièvre et de la tortue est très utilisé pour trouver des points fixes de fonctions.

{% note2 "**Problème algorithmique**" %}

- Nom : Point fixe
- Entrées :
  - $f: \mathbb{N} \to [\\![ 1, n]\\!]$
- Sortie : Un couple d'entiers $x$ et $y$ tels que $f(x) = f(y)$

{% endnote2 %}

Commençons par lier nos fonctions à des suite ultimement périodiques :

{% exercice %}
Montrez que si $f: \mathbb{N} [\\![ 1, n]\\!]$ et $x$ un entier, alors la suite $(a_i)_{0\leq i}$ définie telle que :

- $a_0 = x$
- $a_i = f(a_{i-1})$ pour $i>0$

est ultimement périodique.

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

>TBD il faut adapter l'algorithme du lievre et de la tortue car le calcul  de a(m) sera trop long. Il faut gardr en memoire am-1.

{% exercice %}

Utilisez la question précédente pour résoudre le problème du point fixe de fonctions

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}

Modifiez l'algorithme du lièvre et de la tortue pour qu'il permette de résoudre le problème du point fixe d'une fonction.

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}


## <span id="arithmétique"></span>Algorithmes arithmétique


> - **Utilité** : pour la culture générale et si vous voulez faire de l'informatique plus tard
> - **Difficulté** : très difficile

On considérera toujours en algorithmie que lorsque l'on manipule des entiers les opérations de sommes et de multiplications sont en $\mathcal{O}(1)$ opérations. Si cette approximation fonctionne lorsque les nombres sont bornés (sur 64 bits usuellement), ce n'est bien sur pas possible si les nombres deviennent très grands où il faut considérer leur représentation interne.

{% note "**Définition**" %}

On note $u$ la bijection $u: \\{0, 1\\}^\star \rightarrow \mathbb{N}$ telle que :

<div>
$$
u([x_0, \dots, x_{n-1}]) = \sum_{i=0}^{n-1}x_i \cdot 2^i
$$
</div>

On note $u^{-1}(x)$ l'inverse de $u$ et $u^{-1}_n(x)$ le tableau y de $\\{0, 1\\}^n$ tel que $u(y) = x \bmod 2^n$
{% endnote %}

Ainsi :

- $u([0,1,0, 1]) = 10$ (de notation binaire $0\text{\tt b}1010$),
- $u^{-1}(10) = [0,1,0, 1]$
- $u_3^{-1}(10) = [0,1,0]$ (de notation binaire $0\text{\tt b}010$)
- $u_8^{-1}(10) = [0, 1, 0, 1, 0, 0, 0, 0]$ (de notation binaire $0\text{\tt b}00001010$)

Nous allons voir dans la suite les complexités des opération de somme et de multiplications pour des algorithmes prenants des tableaux de bits en entrées. Pour éviter les cas particuliers embêtant et qui n'apportent pas grand chose algorithmiquement :

### Bijection

Commençons par écrire la bijection permettant de passer d'un entier à un tableau de bits et réciproquement,

{% exercice %}
Écrivez un algorithme de signature `u(x: [bit]) → entier`{.language-} de complexité $\Omega(x.\text{longueur})$ qui rend l'entier positif associé au tableau de bits.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme u(x: [bit]) → entier:
    (v := entier) ← 0
    (puissance_2 := entier) ← 1
    pour chaque (i := entier) de [0 .. x.longueur - 1[:
        si (x[i] == 1):
            v ← v + puissance_2
        puissance_2 ← 2 * puissance_2

    rendre v
```

La finitude du programme est clair. L'invariant de boucle permettant de prouver l'algorithme est : "à la fin de l'itération $i$, $v = \sum_{0 \leq k  \leq i}x[i] \cdot 2^k$".

{% enddetails %}

{% exercice %}
Écrivez un algorithme de signature `u_moins_1(n: entier) → [bit]`{.language-} qui rend le tableau de bits associé à l'entier en paramètre. Sa complexité doit être en $\mathcal{O}(\ln(n))$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme u_moins_1(n: entier) → [bit]:
    (k := entier) ← 0
    (puissance_2 := entier) ← 1
    tant que puissance_2 ≤ n:
        puissance_2 ← 2 * puissance_2
        (k := entier) ← k + 1
    
    (T := [bit]) ← [bit]{longueur: k}
    (i := entier) ← 0
    tant que n > 0:
        si n est impair:
            T[i] ← 1
            n ← n -1
        sinon:
            T[i] ← 0
        n ← n // 2
        i ← i + 1

```

La finitude du programme est clair. puisque dans les deux boucle on augmente (respectivement diminue) strictement une variable qui stoppe la boucle si elle devient plus grande (respectivement plus petite) qu'un seuil.

POur prouver l'algorithme, on regarde les deux boucles de l'algorithme :

- La première (lignes 4-6) est là pour connaître la longueur du tableau de bit de la sortie en cherchant la première puissance de 2 strictement plus grande que $n$. Comme il y a $\log_2(n)$ itérations de cette boucle la complexité est en $\mathcal{O}(\ln(n))$.
- La seconde crée le tableau de bit et sit exactement la définition : si $n = \sum_{i=0}^{n-1}x_i \cdot 2^i$ alors $x_i = n \pmod 2^i$.

Les deux boucles ayant $\log_2(n)$ itération et le reste des instructions étant en $\mathcal{O}(1)$ on en déduit que la complexité de l'algorithme est en $\mathcal{O}(\ln(n))$

{% enddetails %}

### <span id="somme"></span>Addition

Vous allez implémenter l'algorithme de la somme posée ([on y a déjà réfléchit en base 10](../exercices-itératif-récursif/#somme){.interne}) pour des nombres codées sous leur forme binaire.

Sur deux entiers :

```
  100101
+ 001011
--------
  110001
```

Attention à la retenue qui potentiellement augmente la taille de la sortie :

```
   100101
+  011011
--------
  1000000
```

{% exercice %}
Écrivez un algorithme de signature `addition(x: [bit], y: [bit]) → [bit]`{.language-} utilisant l'addition posée. On supposera que :

- $x$ et $y$ sont tous deux de longueur $n$
- la sortie est de taille $n + 1$
{% endexercice %}
{% details "corrigé" %}


```pseudocode
algorithme addition(x: [bit],
                    y: [bit])  # on suppose x et y de même taille
                    → [bit]    # de la taille de x et y + 1

    (somme := [bit]) ← [bit]{longueur: x.longueur + 1}
    (retenue := bit) ← 0

    pour chaque (i := entier) de [0 .. x.longueur - 1[:
        si (x[i] == 1) et (y[i] == 1) et (retenue == 1):
            somme[i]  ← 1
            retenue ← 1
        sinon si ((x[i] == 1) et (retenue == 1)) ou ((y[i] == 1) et (retenue == 1)) ou ((x[i] == 1) et (y[i] == 1)):
            somme[i]  ← 0
            retenue  ← 1
        sinon si (x[i] == 1) ou (y[i] == 1) ou (retenue == 1):
            somme[i]  ← 1
            retenue  ← 0
        sinon:
            somme[i]  ← 0
            retenue  ← 0
    somme[x.longueur] ← retenue

    rendre somme
```

La preuve de correction vient du fait qu'à la fin de chaque itération, on tout se passe comme si on faisait la somme de 3 bit (`x[i]`{.language-}, `y[i]`{.language-}, et `retenue`{.language-})et que l'on mettait le bit unité dans `somme[i]`{.language-} et la dizaine (en base 2) dans `retenue`{.language-} :

```
          x[i]
          y[i]
+       retenue
-------------
retenue somme[i]
```

Les différents cas correspondes à tous les résultats possibles des additions.

{% enddetails %}
{% exercice %}
Quelle est la complexité de cet algorithme. Peut-on faire mieux ?
{% endexercice %}
{% details "corrigé" %}

Si $n$ est la taille des entrées, la complexité de l'algorithme est clairement en $\Theta(n)$. Comme l'addition nécessite au moins $\Omega(n)$ opérations pour lire les données, on est optimal.
{% enddetails %}

### Soustraction

On va se placer dans le cadre de la soustraction de deux nombres dont le résultat est positif.

{% exercice %}
Écrivez un algorithme de signature `soustraction(x: [bit], y: [bit]) → [bit]`{.language-} utilisant la soustraction posée. On supposera que :

- $x$ et $y$ sont tous deux de longueur $n$
- la sortie est de taille $n + 1$
- $u(x) \geq u(y)$
{% endexercice %}
{% details "corrigé" %}

Nos conventions veulent que `x.longueur`{.language-} et `y.longueur`{.language-} soient égales et comme on suppose que $u(x) \geq u(y)$ la sortie sera positive et de la même longueur que $x$.

```pseudocode
algorithme soustraction(x: [bit],
                        y: [bit])  # on suppose x et y de même taille et que u(x) ≥ u(y)
                        → [bit]    # de la taille de x et y

    (différence := [bit]) ← [bit]{longueur: x.longueur}
    (retenue := bit) ← 0

    pour chaque (i := entier) de [0 .. x.longueur - 1[:
        si (x[i] == 1) et (y[i] == 1) et (retenue == 1):
            différence[i]  ← 0
            retenue ← 1
        sinon si ((x[i] == 1) et (retenue == 1)) ou ((x[i] == 1) et (y[i] == 1)):
            différence[i]  ← 0
            retenue  ← 0
        sinon si ((y[i] == 1) et (retenue == 1)):
            différence[i]  ← 0
            retenue  ← 1
        sinon si (x[i] == 1):
            différence[i]  ← 0
            retenue  ← 0
        sinon si ((y[i] == 1) ou (retenue == 1)):
            différence[i]  ← 1
            retenue  ← 1
        sinon:
            différence[i]  ← 0
            retenue  ← 0
          
    rendre différence
```

La preuve de correction vient du fait qu'à la fin de chaque itération, on tout se passe comme si on faisait `x[i] - (y[i] + retenue)`{.language-} et que l'on mettait le bit unité dans `différence[i]`{.language-} et la dizaine (en base 2) dans `retenue`{.language-} :

```
            x[i]
- (         y[i]
   +      retenue)
----------------------
retenue différence[i]
```

Les différents cas correspondes à tous les résultats possibles des soustraction.

{% enddetails %}
{% exercice %}
Quelle est la complexité de cet algorithme. Peut-on faire mieux ?
{% endexercice %}
{% details "corrigé" %}

Si $n$ est la taille des entrées, la complexité de l'algorithme est clairement en $\Theta(n)$. Comme la soustraction nécessite au moins $\Omega(n)$ opérations pour lire les données, on est optimal.
{% enddetails %}

La méthode utilisée permet de gérer les entiers positifs et négatifs, mais [on verra plus tard](../fonctions-booléennes/#complément-à-deux){.interne} un moyen plus efficace de le faire en utilisant [le complément à 2](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)

### Améliorations

{% exercice %}
Que proposez-vous pour permettre :

1. des additions et de soustractions avec des tailles différentes
2. que la taille de la sortie soit la plus petite possible

Tout en gardant la même complexité.
{% endexercice %}
{% details "corrigé" %}

Pour le premier point, on peut garder le même algorithme en copiant les entrées dans deux tableaux originellement remplis de 0 tout deux de longueurs égale au max des longueurs des deux entrées :

```pseudocode
algorithme opération(x: [bit],
                     y: [bit])  # on suppose x et y de même taille
                     → [bit]    # de la taille de x et y + 1

    (x' := [bit]) ← [bit]{longueur: max(x.longueur, y.longueur)}
    x'[:] ← 0
    pour chaque (i := entier) de [0 .. x.longueur[:
        x'[i] ← x[i]
    (y' := [bit]) ← [bit]{longueur: max(x.longueur, y.longueur)}
    y'[:] ← 0
    pour chaque (i := entier) de [0 .. x.longueur[:
        y'[i] ← y[i]

    #  ... reste de l'algorithme
```

Les opérations ajoutées sont en $\mathcal{O}(max(x.\text{longueur}, y.\text{longueur}))$ ce qui ne change pas la complexité.

Pour le second point, on peut supprimer tous les derniers élément du tableaux égaux à 0 :

```pseudocode
algorithme opération(x: [bit],
                     y: [bit])  # on suppose x et y de même taille
                     → [bit]    # de la taille de x et y + 1

    #  ... début de l'algorithme

    (i := entier) ← résultat.longueur
    (on_reste := booléen) ← Vrai

    tant que on_reste:
        si (i == 0) ou (résultat[i-1] == 1):  # on s'arrête au premier 1 ou si résultat ne contient que des 0
            on_reste ← Faux
        sinon:
            i ← i - 1
    
    (résultat' := [bit]) ← [bit]{longueur: i}

    pour chaque i de [0 .. résultat'.longueur[:
        résultat'[i] ← résultat[i]
    
    rendre résultat'
```

Là encore, cet ajout ne change pas la complexité de l'algorithme.

{% enddetails %}


On considérera par la suite que nos algorithmes ont implémenté ces améliorations et que :

- $\text{addition}(x, y) = u^{-1}(u(x) + u(y))$ et on la notera $x + y$
- $\text{soustraction}(x, y) = u^{-1}(u(x) - u(y))$ si $u(x) \geq u(y)$ et on la notera $x - y$

### Multiplication

La multiplication de deux tableaux de bits 
{% exercice %}
Montrez que la complexité du problème de la multiplication de deux entiers sous leur forme binaires à $n$ bit est en $\Omega(n)$.
{% endexercice %}
{% details "corrigé" %}

Il faut au moins lire les données, ce qui nécessite au moins $\Omega(n)$ opérations.
{% enddetails %}

On ne connaît cependant pas d'algorithme de complexité $\mathcal{O}(n)$ et le meilleur algorithme connu est en $\mathcal{O}(n\ln(n))$, que l'on suppose être la complexité du problème. On a cependant longtemps pensé que la complexité du problème de la multiplication était égale à celle de la multiplication posée que l'on apprend en primaire jusqu'à ce que [Anatolii Alexevich Karatsuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba) prouve le contraire en 1962.

Le problème de la multiplication est intéressant à plus d'un titre :

- améliorer l'algorithme naïf est possible mais c'est dur
- on ne connaît pas la complexité du problème mais on a de fortes présomptions
- les algorithmes les plus efficaces ne sont pas utilisés en pratique car il ne sont efficaces que pour des nombres astronomiquement grand. En pratique dans les ordinateurs c'est une version optimisé de l'algorithme naïf qui est utilisé pour des nombre de tailles fixés (64b).

#### Puissances de 2

Commençons par étudier un cas particulier de la multiplication, celui où un des deux no,bre est une puissance de 2.

{% exercice %}
Montrez que multiplier un nombre par une puissance de 2 revient à ajouter des 0 à gauche de sa représentation binaire.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire un algorithme de signature `puissance(n: entier, x: [bit]) → [bit]`{.language-} permettant de rendre $u(2^n \cdot u^{-1}(x))$ avec une complexité optimale.

{% endexercice %}
{% details "corrigé" %}

> TBD complexité O(n)
> TBD algo

{% enddetails %}

On considérera par la suite que l'on a : $\text{puissance}(n, x) = u^{-1}(2^n \cdot u(y))$ et on la notera $2^n \cdot y$

#### Naive

On utilise la [multiplication posée](https://fr.wikipedia.org/wiki/Multiplication#Techniques_de_multiplication). Les nombres binaires simplifient grandement le calcul car il suffit de faire des additions.

```
       100101
     * 001011
    ---------
       100101  = 100101 * 1
      100101   = 100101 * 1
     000000    = 100101 * 0
    100101     = 100101 * 1
   000000      = 100101 * 0
+ 000000       = 100101 * 0
------------
  00110010111
```

On trouve que $0b100101 \cdot 0b1011 = 0b110010111$ ($37 \cot 11 = 407$).


{% exercice %}
Écrivez un algorithme de signature `multiplication(x: [bit], y: [bit]) → [bit]`{.language-} utilisant la multiplication posée.
{% endexercice %}
{% details "corrigé" %}

Nos conventions veulent que `x.longueur`{.language-} et `y.longueur`{.language-} soient égales, la longueur de la sortie sera donc égale à 2 fois la longueur de $x$.

On obtient l'algorithme suivant :

```pseudocode
algorithme multiplication(x: [bit], y: [bit]) → [bit]

    (résultat := [bit]) ← [bit]{longueur: 2 * x.longueur}
    résultat[:] ← 0

    retenue := entier
    temp := entier
    pour chaque k de [0 .. x.longueur[:
        retenue ← 0
        pour chaque i de [0 .. y.longueur[:
            si y[i] == 1:
                si (x[i] == 1) et (résultat[i + k] == 1) et (retenue == 1):
                    résultat[i + k]  ← 1
                    retenue ← 1
                sinon si ((x[i] == 1) et (retenue == 1)) ou ((résultat[i + k] == 1) et (retenue == 1)) ou ((x[i] == 1) et (résultat[i + k] == 1)):
                    somme[i]  ← 0
                    retenue  ← 1
                sinon si (x[i] == 1) ou (résultat[i + k] == 1) ou (retenue == 1):
                    résultat[i + k]  ← 1
                    retenue  ← 0
                sinon:
                    résultat[i + k]  ← 0
                    retenue  ← 0
            résultat[k + x.longueur] ← retenue
    rendre résultat
```

{% enddetails %}
{% exercice %}
Quelle est la complexité de cet algorithme.
{% endexercice %}
{% details "corrigé" %}
La complexité de l'algorithme est en $\Theta(n^2)$ avec $n$ la longueur des 2 entrées.
{% enddetails %}

#### Karatsuba

{% lien %}
[optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba)
{% endlien %}

On va décrire le procédé utilisé par Karatsuba en plusieurs temps. Pour des raisons de clarté, on va supposer que l'on a des algorithmes optimaux pour écrire :

- des additions de $[bit]$ sans soucis de taille : $[x_0, \dots, x_{p-1}] + [y_0, \dots, y_{q-1}] = [z_0, \dots z_{r-1}]$
- des soustractions de $[bit]$ sans soucis de taille (mais on considère toujours que le résultat doit être positif): $[x_0, \cdot x_{p-1}] - [y_0, \dots, y_{q-1}] = [z_0, \dots, z_{r-1}]$
- multiplier des $[bit]$ par $2^n$ : $2^n \cdot [x_0, \dots, x_{p-1}] = [0, \dots, 0, x_0, \dots, x_{p-1}]$

On cherche à effectuer de façon efficace la multiplication de $[bit]$ de même taille : $[x_0, \dots, x_{n-1}]  \cdot \cdot [y_0, \cdot y_{n-1}] = [z_0, \dots, z_{m-1}]$ (avec $m \leq 2n$)

Il a longtemps été pensé que l'on ne pouvait pas faire mieux que la multiplication naïve, la solution ne va donc pas consister à en optimiser le fonctionnement. L'idée est d'utiliser un principe [que l'on formalisera plus tard](../design-algorithmes/diviser-régner/){.interne} et qui s'appelle _"diviser pour régner"_. Notre but est d'utiliser la récursion pour effectuer des multiplication sur des tableaux de bits plus petit et espérer gagner en complexité.

Ceci est rendu possible car il est facile de reconstituer un tableau de bit à partir de bouts :

<div>
$$
[x_0, \dots, x_{2n-1}] = [x_0, \dots, x_{n-1}] + 2^n \cdot [x_n, \dots, x_{2n-1}]
$$
</div>

En utilisant nos algorithmes optimaux, l'équation précédente s'effectue en $\Omega(n)$. On peut alors développer le produit de deux tableaux de bits :

<div>
$$
\begin{array}{lcl}
[x_0, \dots, x_{n-1}] \cdot [y_0, \dots, y_{n-1}] &=& ([x_0, \dots, x_{n // 2}] + 2^{n // 2} \cdot [x_{n // 2}, \dots, x_{n-1}]) \cdot ([y_0, \dots, y_{n // 2}] + 2^{n // 2} \cdot [y_{n // 2}, \dots, y_{n-1}])\\
&=& 2^n \cdot [x_{n // 2}, \dots, x_{n-1}] \cdot [y_{n // 2}, \dots, y_{n-1}]  \\
&& + 2^{n // 2} \cdot ([x_0, \dots, x_{n // 2}] \cdot [y_{n // 2}, \dots, y_{n-1}] + [y_0, \dots, y_{n // 2}] \cdot [x_{n // 2}, \dots, x_{n-1}]) \\
&& + [x_0, \dots, x_{n // 2}] \cdot [y_0, \dots, y_{n // 2}]\\
\end{array}
$$
</div>

On remarque que pour multiplier deux nombres de longueur $n$ il suffit de multiplier des nombres de taille $n//2$ et d'utiliser des sommes et des multiplication par des puissances de 2 que l'on sait faire de façon optimale.

Pour transformer cette égalité en pseudocode il faut faire un peu attention à la taille de nos tableaux. Si leurs tailles ne sont pas paires les tableaux $[x_0, \dots, x_{n // 2 -1}]$ et $[x_{n // 2}, \dots, x_{n -1}]$ n'ont pas la même taille et cela brise la condition d'application de notre algorithme (les deux entrées doivent être de même taille).

{% exercice %}
Montrez que l'astuce suivante permet de séparer un tableau $x$ en 2 sous-tableaux de même taille quelque soit sa longueur $n$ :

```pseudocode
(x := entier) ← x.longueur

(x1 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
x1[-1] ← 0
x1[: n // 2] ← x[: n // 2]
(x2 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
x2[n // 2 :] ← x[n // 2 :]

```

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

On peut maintenant écrire le pseudo-code associé à notre équation :

{% exercice %}
Écrire l'algorithme permettant de multiplier récursivement deux `[bit]`{.language-} de même longueur en utilisant l'équation précédente. 

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme Karatsuba(x: [bit], y: [bit]) → [bit]:  # x et y de même longueur
    (n := entier) ← x.longueur

    # astuce pour garantir une même taille aux tableaux si la longueur est impaire
    (x1 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    x1[-1] ← 0
    x1[: n // 2] ← x[: n // 2]
    (x2 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    x2[n // 2 :] ← x[n // 2 :]

    (y1 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    y1[-1] ← 0
    y1[: n // 2] ← y[: n // 2]
    (y2 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    y2[n // 2 :] ← y[n // 2 :]

    (x2y2 := [bit]) ← Karatsuba(x2, y2)
    (x1y1 := [bit]) ← Karatsuba(x1, y1)

    (x1y2 := [bit]) ← Karatsuba(x1, y2)
    (x2y1 := [bit]) ← Karatsuba(x2, y1)

    résultat := [bit]

    résultat ← puissance(n, x2y2)
    résultat ← somme(résultat, puissance(n // 2, somme(x1y2, x2y1)))
    résultat ← somme(résultat, x1y1)
```

{% enddetails %}
{% exercice %}
Montrer que la complexité de l'algorithme précédent respecte l'équation de récurrence :

<div>
$$
C(n) = 4 \cdot C(n / 2) + \mathcal{O}(n)
$$
</div>

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
Montrez que la complexité $C(n)$ de l'algorithme avec $n$ la longueur des tableaux en entrée vaut :

<div>
$$
C(n) = (4^{K} + \sum_{0\leq i \leq K}4^i) \cdot \mathcal{O}(1)
$$
</div>

Avec $K = \log_2(n)$.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire que :
<div>
$$
C(n) = \mathcal{O}(4^{\log_2(n)})
$$
</div>

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire que sa complexité est en $C(n) = n^2$

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Flûte ! La complexité n'est pas meilleure que l'algorithme naïf. Tout n'est cependant pas perdu. Si on arrive à diminuer le nombre de récursions, donc le no,bre de multiplications, notre algorithme va être meilleur. Et c'est là que Karatsuba entre en scène, il a en effet remarqué que :

<div>
$$
\begin{array}{lcl}
[x_0, \dots, x_{n-1}] \cdot [y_0, \dots, y_{n-1}] &=& 2^n \cdot [x_{n // 2}, \dots, x_{n-1}] \cdot [y_{n // 2}, \dots, y_{n-1}]  \\
&& + 2^{n // 2} \cdot ([x_0, \dots, x_{n // 2}] + [x_{n // 2}, \dots, x_{n-1}]) \cdot ([y_0, \dots, y_{n // 2}] + [y_{n // 2}, \dots, y_{n-1}]) \\
&& - 2^{n // 2} \cdot ([x_{n // 2}, \dots, x_{n -1}] \cdot [y_{n //2}, \dots, y_{n -1}] + [x_0, \dots, x_{n // 2}] \cdot [y_{0}, \dots, y_{n // 2}]) \\
\end{array}
$$
</div>

On a plus besoin que de 3 multiplications ! Adaptons tout de suite notre algorithme :

{% exercice %}
Modifiez votre algorithme de Karatsuba pour qu'il intègre l'astuce précédente.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme Karatsuba(x: [bit], y: [bit]) → [bit]:  # x et y de même longueur
    (n := entier) ← x.longueur

    # astuce pour garantir une même taille aux tableaux si la longueur est impaire
    (x1 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    x1[-1] ← 0
    x1[: n // 2] ← x[: n // 2]
    (x2 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    x2[n // 2 :] ← x[n // 2 :]

    (y1 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    y1[-1] ← 0
    y1[: n // 2] ← y[: n // 2]
    (y2 := [bit]) ← [bit]{longueur: n // 2 + (n mod 1)}
    y2[n // 2 :] ← y[n // 2 :]

    (x2y2 := [bit]) ← Karatsuba(x2, y2)
    (x1y1 := [bit]) ← Karatsuba(x1, y1)

    (s1 := [bit]) ← somme(x1, x2)
    (s2 := [bit]) ← somme(y1, y2)
    (p := [bit]) ← Karatsuba(s1, s2)

    résultat := [bit]

    résultat ← puissance(n, x2y2)
    résultat ← somme(résultat, puissance(n // 2, x2y2))
    résultat ← soustraction(résultat, somme(x2y2, x1y1))
```

{% enddetails %}
{% exercice %}
Montrez que la complexité $C(n)$ de l'algorithme avec $n$ la longueur des tableaux en entrée suit l'équation de récursion :

<div>
$$
C(n) = 3 \cdot C(n / 2) + \mathcal{O}(n)
$$
</div>

{% endexercice %}
{% details "corrigé" %}

Il y a 3 appels à l'algorithme avec des tableaux de tailles divisées par deux et le reste des algorithmes appelés et des opérations est en $\mathcal{O}(n)$
{% enddetails %}
{% exercice %}
En déduire que :
<div>
$$
C(n) = \mathcal{O}(3^{\log_2(n)})
$$
</div>

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Cette formule n'est pas très jolie. Transformons la en quelque chose d'agréable pour conclure.

{% exercice %}
Montrez que $3^{\log_2(n)} = n^{log_2(3)}$

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% info %}
C'est cette astuce qui permet d'avoir des complexité avec des nombres réels en exposant.
{% endinfo %}
{% exercice %}
En déduire que la complexité de l'algorithme de Karatsuba est en $\mathcal{O}(n^{1.585})$. Conclusion par rapport à l'algorithme naïf ?

{% endexercice %}
{% details "corrigé" %}

Comme $\log_2(3) \simeq 1.58$, l'algorithme de Karatsuba est de complexité $\mathcal{O}(n^{1.59})$,  strictement plus petite que l'algorithme naïf de multiplication en $\mathcal{O}(n^{2})$.

{% enddetails %}

Vous le voyez, trouver mieux que l'algorithme naïf n'a pas été simple ! Mais c'est possible. La question brûlante est alors, peut-on faire encore mieux ?

#### Peut-on mieux faire ?

> TBD Strassen nlog(n) conjecture. et de l'optimal <https://fr.wikipedia.org/wiki/Algorithme_de_multiplication_d%27entiers> et <https://math.univ-lyon1.fr/~roblot/resources/ens_partie_2.pdf>

> TBD <https://www.youtube.com/watch?v=qKcwuRK9n6U> et <https://towardsdatascience.com/how-to-perform-fast-multiplications-in-science-using-the-fft-b751fafc2bac/>
>
> FFT : <https://informatique.ens-lyon.fr/concours-info/2014/multiplication.pdf>

### Conclusion

> conjecture
> nb tres tres grand pour que ca marche
> en pratique on fixe la taille

> TBD c'est pour ça que parfois on sépare somme et multiplication dans le calcul de la complexité (cf. polynôme dans les calculs de complexité).


