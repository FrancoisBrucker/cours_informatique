---
layout: layout/post.njk 
title: "Structure : dictionnaire"

eleventyNavigation:
  key: "Structure : dictionnaire"
  parent: Algorithme
---

{% prerequis "**Prérequis** :" %}

* [ensembles et dictionnaires]({{" /cours/base-code/ensembles-dictionnaires" | url}})
* [fonctions de hash](../../théorie/fonctions-hash)
* [complexité en moyenne](../complexité-moyenne)

{% endprerequis %}

<!-- début résumé -->

Mise en œuvre de la structure de dictionnaire qui est une structure fondamentale en code.

<!-- end résumé -->

Pour créer efficacement une structure de dictionnaire, on utilise des [fonctions de hachage](../../théorie/fonctions-hash.md %}).

Supposons que l'on ait une fonction de hachage $f$ qui a tout objet associe un nombre entre 0 et $m$.

On peut de plus supposer que le hash est calculé en $\mathcal{O}$ de la taille de l'objet à hacher. Par exemple en $\mathcal{O}(len(s))$ pour une chaîne de caractères `s` par exemple.

Si la fonction $f$ est injective, il suffit de stocker nos valeurs dans une liste $L$ à $m+1$ éléments à l'indice égal au hash de sa clé. Ainsi si je veux associer la valeur $v$ à la clé $c$, on effectuera l'opération : `L[f(c)] = v`.

Si la fonction n'est pas injective, chaque élément de la liste $L$ est une liste qui stockera les différentes clés ayant même hash. De là :

* pour associer $v$ à la clé $c$, on effectue les opérations suivantes :
  1. on cherche le hash `f(c)` qui sera un nombre entre $0$ et $m$.
  2. Soit $L'= L[f(c)]$. $L'$ est une liste composée de couple $(a, b)$. On a alors 2 cas :
     1. S'il existe $(c, b)$ dans $L'$ on remplace $b$ par v
     2. S'il n'existe pas de couple $(c, b)$ dans $L'$ on ajoute à la fin de la liste $L'$ le couple $(c, v)$
* pour retrouver la valeur $v$ associée la clé $c$, on effectue les opérations suivantes :
  1. on cherche le hash `f(c)` qui sera un nombre entre $0$ et $m$.
  2. Soit $L'= L[f(c)]$. $L'$ est une liste composée de couple $(a, b)$. On a alors 2 cas :
     1. S'il existe $(c, b)$ dans $L'$ on rend $b$
     2. S'il n'existe pas de couple $(c, b)$ $f(c)$ n'est pas une clé du dictionnaire et on rend une erreur.

Pour ces deux opérations, la complexité est alors la somme des complexités :

* du calcul du hash de l'objet `c` : `f(c)`
* du nombre d'éléments de `L[f(c)]`
* du temps pour vérifier l'égalité entre 2 objets.

Comme les clés sont associés à des objets non modifiables, leur hash peut être connu à la création des objets donc le calcul de `f(c)` se fait en $\mathcal{O}(1)$. La complexité vient donc de la comparaison de l'objet `c` à tous les premiers éléments de `L[f(c)]`, ce qui correspond à la complexité $K(c)$ de l'opérateur `==` de l'objet `c` multiplié par la longueur de `L[f(c)]`.

{% info %}
La complexité $K(c)$ dépend de l'objet `c`. Pour comparer deux réels, cela se fait en $\mathcal{O}(1)$, mais pour une liste par exemple cela va dépendre des éléments contenus dans la liste (comparer deux listes revient à comparer tous les éléments des deux listes 2 à 2).
{% endinfo %}

Si la taille maximale des objets est connues, on a coutume de considérer que $K(c) = \mathcal{O}(1)$ pour tout objet $c$.

## Taille de la structure

Comme la liste principale où stocker les éléments est de taille $m+1$, il est impossible d'utiliser la fonction de hachage directement. En effet, si l'on utilise sha-1 pour fonction de hachage il faudrait une taille de liste de $2^{160}$ ce qui est impossible...

C'est pourquoi, en réalité on n'utilise une fonction supplémentaire appelée **fonction d'adressage** qui est une deuxième fonction de hash dont on peut maîtriser la taille :

{% note %}
Une fonction d'adressage $f_m$ est une fonction : de $\mathbb{N}$ dans $[0\mathrel{ {.}\,{.} } m-1]$.
{% endnote %}

Une structure de dictionnaire est alors un couple :

* $L$ : la liste principale de taille $m$
* $f_m$ une fonction d'adressage.

Pour associer et rechercher une valeur on procède alors comme suit :

* pour associer $v$ à la clé $c$, on effectue les opérations suivantes :
  1. on cherche le hash `f(c)` de la clé $c$.
  2. on note $i_c = f_m(f(c))$ qui sera un nombre entre 0 et $m-1$
  3. Soit $L'= L[i_c]$. $L'$ est une liste composée de couple $(a, b)$. On a alors 2 cas :
     1. S'il existe $(c, b)$ dans $L'$ on remplace $b$ par v
     2. S'il n'existe pas de couple $(c, b)$ dans $L'$ on ajoute à la fin de la liste $L'$ le couple $(c, v)$
* pour retrouver la valeur $v$ associée la clé $c$, on effectue les opérations suivantes :
  1. on cherche le hash `f(c)` de la clé $c$.
  2. on note $i_c = f_m(f(c))$ qui sera un nombre entre 0 et $m-1$
  3. Soit $L'= L[f(c)]$. $L'$ est une liste composée de couple $(a, b)$. On a alors 2 cas :
     1. S'il existe $(c, b)$ dans $L'$ on rend $b$
     2. S'il n'existe pas de couple $(c, b)$ $f(c)$ 'est pas une clé du dictionnaire et on rend une erreur.

La fonction d'adressage permet de choisir $m$ pas trop grand. De plus, on peut considérer que son calcul est toujours en $\mathcal{O}(1)$ car elle sera toujours utilisée avec un nombre de taille fixe qui est le hash d'un objet.

## Complexités

On va estimer la complexité des opérations suivantes :

* création de la structure
* suppression de la structure (liste de liste)
* ajout d'un élément à la structure
* recherche d'un élément à la structure
* suppression d'un élément à la structure

On le rappelle, une structure de dictionnaire est constitué d'une liste de $m$ éléments, chaque élément étant lui-même une liste.  L'accès aux données dépend du nombre d'éléments stockés $n$ et de la taille de la liste principale $m$. Si on cherche si la clé `c` est dans un dictionnaire, il faut regarder chaque élément de la liste stockée à l'indice  $L[f_m(f(c))]$.

### Création de la structure

La création de la structure est en $\mathcal{O}(m)$ puisqu'il faut créer une liste de $m$ éléments chaque élément étant une liste vide.

Initialement, $m$ est une constante, on a donc :

{% note %}
La création d'une structure de dictionnaire prend $\mathcal{O}(1)$ opérations.
{% endnote %}

### Suppression de la structure

La suppression de la structure en $\mathcal{O}(m)$ (il faut supprimer toutes les listes stockées).

{% note %}
La création d'une structure de dictionnaire prend $\mathcal{O}(m)$ opérations, où $m$ est la taille de la liste principale.
{% endnote %}

### Ajout/recherche et suppression d'un élément

Les complexités sont identiques car cela revient à chercher si la clé $c$ est déjà stockée ou non dans la structure.

Cette complexité peut aller de :

* cas le meilleurs : $\mathcal{O}(1)$. Ceci arrive lorsque la liste $L[f_m(f(c))]$ est vide
* cas le pire : $\mathcal{O}(n \times K(c)) = \mathcal{O}(n)$ (en considérant que $K(c) = mathcal{O}(1)$). Ceci arrive lorsque tous les éléments de la liste ont même hash, le nombre d'élément de $L[f_m(f(c))]$ sera $n$
* cas moyen : $\mathcal{O}(\frac{n}{m})$. Si les clés sont uniformément distribuées, il y aura de l'ordre de $\frac{n}{m}$ éléments dans la liste $L[f_m(f(c))]$.

Une astuce permet de diminuer la complexité moyenne.

> TBD : modification de la taille de la structure comme une liste pour avoir une complexité de O(1) en moyenne.

## Modification de la taille

Le choix de `m` détermine la complexité en moyenne. La complexité en moyenne de l'ajout/recherche et suppression d'un élément étant de l'ordre de  $\mathcal{O}(\frac{n}{m})$, si l'on maintient ce ratio à une constante la complexité moyenne sera de $\mathcal{O}(1)$.

C'est pourquoi, lorsque le nombre d'objet stocké augmente et que le ratio augmente, on va de temps en temps recréer un nouveau dictionnaire en doublant la taille allouée pour faire diminuer ce ratio.

Cette technique, identique à celle utilisée dans les [listes](../structure-liste) permet de maintenant un ratio à *peut prêt constant* et donc :

{% note %}
Le temps moyen de recherche, d'ajout et de suppression d'un élément dans un dictionnaire est de  $\mathcal{O}(1)$ opération.
{% endnote %}

La structure de dictionnaire est donc une structure très efficace ! N'hésitez pas à l'utiliser car son temps moyen d'exécution est très rapide.

## Exercice

* données :  
  * une liste de $n$ prix : $p_i$ ($0 \leq i < n$)
  * un crédit : $C$
* Question : donner deux indices $i$ et $j$ tels que $p_i + p_j = C$ ou `None si cela n'existe pas.

On va essayer de répondre à cet exercice de trois façons différentes, toutes avec des complexités différentes.

### Deux boucles for imbriquées

Comme il faut trouver deux indices différents dans la liste $p$ (à $n$ éléments), deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

```python
def recherche(p):
    for i in range(n):
        for  in range(i + 1, n):
            if p[i] + p[j] == C:
                return (i, j)
    return None
```

Deux boucles imbriquées et le reste en $\mathcal{O}(1)$ : la complexité totale est en $\mathcal{O}(n^2)$.

{% enddetails %}

### Une boucle et un tri

Solution en $\mathcal{O}(n\cdot log(n))$

On trie la liste (ce qui donne la complexité de la solution) puis :

```python
def recherche(p):
    p.sort()

    i = 0
    j = n-1
    while p[i] + p[j] != C:
        if p[i] + p[j] < C:
            i += 1
        else:
            j -= 1
        
        if i > j:
            return None
    return (i, j)
```

Notez que cette solution est aussi en $\mathcal{O}(n\cdot log(n))$ en moyenne car le tri utilisé par python est de complexité $\mathcal{O}(n\cdot log(n))$ en moyenne.

### Avec un dictionnaire

solution en $\mathcal{O}(n)$ en moyenne et complexité maximale $\mathcal{O}(n\cdot log(n))$

```python
def recherche(p):
    d = dict()

    for i in range(n):
        if C - p[i] in d:
            return (d[C-p[i]], i)
        d[p[i]] = i
    return None
```
