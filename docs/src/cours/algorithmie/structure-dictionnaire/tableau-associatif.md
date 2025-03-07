---
layout: layout/post.njk
title: "Tableaux associatifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer dans cette  partie une structure de donnée très utilisée en développement : le tableau associatif, aussi appelé dictionnaire.

Cette structure utilise de façon sous-jacente une [fonctions de hachage](../fonctions-hash){.interne}.

## Principe

Supposons que l'on ait une fonction de hachage $f$ qui a tout objet associe un nombre entre 0 et $m-1$. On peut de plus supposer que le hash est calculé en $\mathcal{O}$ de la taille de l'objet à hacher. Par exemple en $\mathcal{O}(len(s))$ pour une chaîne de caractères $s$ par exemple.

### hash injective

Si la fonction $f$ est injective, c'est à dire que tous nos objets ont une valeur de hash unique, on peut accéder aux élément d'un tableau $T$ de taille $m$ soit :

- par un indice $0 \leq i < m$ : $T[i]$
- par un objet $o$ puisque $0 \leq \mbox{hash}(o) < m$  : $T[\mbox{hash}(o)]$

L'objet $o$ est une **_clé_** permettant d'accéder à la **_valeur_** $T[\mbox{hash}(o)]$

La structure de dictionnaire est alors, en supposant que l'on possède un type générique objet :

```pseudocode
structure Dictionnaire:
    attributs:
        T: [Objet]
        f: (Objet → [0, m[)  # fonction de hachage injective
    création() → Dictionnaire:
        T ← un tableau de taille m
    méthodes:
        méthode donne_valeur(clé: Objet) → entier:
            rendre T[f(clé)]
        méthode associe_valeur(clé: Objet, valeur: entier) → vide:
            T[f(clé)] ← valeur
```

On accède aux éléments stockés via un objet et plus un indice, ce qui est vraiment pratique !

### hash quelconque

Si la fonction de hash n'est pas injective (ce qui est généralement le cas), plusieurs objets peuvent avoir le même hash. Il faut pouvoir les distinguer. La façon classique de faire ceci est de créer une indirection via une liste contenant des couples (clé, valeur) possibles :

```pseudocode
structure Dictionnaire:
    attributs:
        T: [Liste de (Objet, Objet)]
        f: (Objet → [0, m[)   # fonction de hachage non injective
    création() → Dictionnaire:
        T ← un tableau de taille m
        pour chaque i de [0, m[:
            T[i] ← nouvelle liste vide  # liste de couples (clé, valeur)
    méthodes:
        méthode donne_valeur(clé: objet) → entier:
            l ← T[f(clé)]  # liste de couples

            pour chaque couple (o, v) de l:
                si o == clé:
                    rendre v
        méthode associe_valeur(clé: objet, valeur: entier) → vide:
            l ← T[f(clé)]  # liste de couples

            pour chaque i de [0, l.longueur[:
                o, v ← l[i]
                si o == clé:  # clé est déjà associée à une valeur
                    l[i] ← (clé, valeur)  # on met à jour
                    rendre vide

            l.append((clé, valeur))  # clé n'est pas encore stockée
```

Chaque élément du tableau T de la structure est une liste qui stockera les différentes clés ayant même hash.

C'est cette structure qui est implémentée puisque qu'aucune fonction de hash n'est injective.

## Complexité de la recherche d'une clé

Analysons la complexité dans les deux cas précédents

### Fonction de hachage injective

La complexité de la recherche d'une valeur à partir d'une clé est égale à la complexité du calcule de la fonction de hash de la clé $f(\mbox{clé})$.

Comme les clés sont associés à des objets non modifiables, leur hash peut être connu à la création des objets donc le calcul de $f(\mbox{clé})$ se fait en $\mathcal{O}(1)$.

### Fonction de hachage quelconque

Outre le calcul de $f(\mbox{clé})$, il faut ensuite :

1. parcourir la liste des couples (objet, valeur) stocké pour une valeur de hash donnée
2. comparer chaque objet à notre clé avec l'opérateur `==`{.language-}  pour voir s'il sont égaux.

On considère que l'opérateur `==`{.language-} a une complexité de l'ordre de la taille de la structure à comparer ($\mathcal{O}(1)$ pour des types de base, mais de l'ordre de la taille si on compare deux tableaux d'entiers par exemple). Si la taille maximale des objets est connue, on a coutume de considérer que la complexité de l'opérateur `==`{.language-} vaut $\mathcal{O}(1)$ pour tout objet $c$.

On en conclut que la recherche et l'affectation dans un dictionnaire est en _grand O_ du nombre maximum de clé stockés avec la même valeur de hash.

## Taille de la structure

Comme la liste principale où stocker les éléments est de taille $m$, il est impossible d'utiliser la fonction de hachage directement. En effet, si l'on utilise [sha-2](https://fr.wikipedia.org/wiki/SHA-2) comme fonction de hachage il faudrait une taille de liste de $2^{160}$ ce qui est impossible...

C'est pourquoi, en réalité on n'utilise une fonction supplémentaire appelée **fonction d'adressage** qui est une deuxième fonction de hash dont on peut maîtriser la taille :

{% note "**Définition**" %}
Une **_fonction d'adressage_** $f_m$ est une fonction : de $\mathbb{N}$ dans $[0\mathrel{ {...} } m[$.
{% endnote %}

Une structure de dictionnaire est alors :

```pseudocode
structure Dictionnaire:
    attributs:
        T: [Liste de (Objet, Objet)]
        f: (Objet → [0, m'[)   # fonction de hachage non injective
        f_m: ([0, m'[ → [0, m[) # fonction d'adressage
    création() → Dictionnaire:
        T ← un tableau de taille m
        pour chaque i de [0, m[:
            T[i] ← nouvelle liste vide
    méthodes:
        méthode donne_valeur(clé: objet) → entier:
            l ← T[f_m(f(clé))]  # liste de couples

            pour chaque couple (o, v) de l:
                si o == clé:
                    rendre v
        méthode associe_valeur(clé: objet, valeur: entier) → vide:
            l ← T[f_m(f(clé))]  # liste de couples

            pour chaque i de [0, l.longueur[:
                o, v ← l[i]
                si o == clé:  # clé est déjà associée à une valeur
                    l[i] ← (clé, valeur)  # on met à jour
                    rendre vide

            l.append((clé, valeur))  # clé n'est pas encore stockée
```

La fonction d'adressage permet de choisir $m$ pas trop grand. De plus, on peut considérer que son calcul est toujours en $\mathcal{O}(1)$ car elle sera toujours utilisée avec un nombre de taille fixe qui est le hash d'un objet.

## Complexités des méthodes

En supposant que la fonction d'adressage est une fonction de hash utile,
On va estimer la complexité des opérations suivantes :

- création de la structure
- suppression de la structure (liste de liste)
- ajout d'un élément à la structure
- recherche d'un élément à la structure
- suppression d'un élément à la structure

On le rappelle, une structure de dictionnaire est constitué d'une liste de $m$ éléments, chaque élément étant lui-même une liste. L'accès aux données dépend du nombre d'éléments stockés $n$ et de la taille de la liste principale $m$. Si on cherche si la clé `c` est dans un dictionnaire, il faut regarder chaque élément de la liste stockée à l'indice $T[f_m(f(c))]$.

### Création de la structure

La création de la structure est en $\mathcal{O}(m)$ puisqu'il faut créer une liste de $m$ éléments chaque élément étant une liste vide.

Initialement, $m$ est une constante, on a donc :

{% note %}
La création d'une structure de dictionnaire prend $\mathcal{O}(1)$ opérations.
{% endnote %}

### Suppression de la structure

La suppression de la structure en $\mathcal{O}(m)$ (il faut supprimer toutes les listes stockées).

{% note %}
La suppression d'une structure de dictionnaire prend $\mathcal{O}(m)$ opérations, où $m$ est la taille de la liste principale.
{% endnote %}

### Ajout/recherche et suppression d'un élément

Les complexités sont identiques car cela revient à chercher si la clé $c$ est déjà stockée ou non dans la structure.

Cette complexité peut aller de :

- cas le meilleur : $\mathcal{O}(1)$. Ceci arrive lorsque la liste $T[f_m(f(c))]$ est vide
- cas le pire : $\mathcal{O}(n)$ (en considérant que la complexité de l'opérateur `==`{.language-} vaut $\mathcal{O}(1)$). Ceci arrive lorsque tous les éléments de la liste ont même hash, le nombre d'élément de $T[f_m(f(c))]$ sera $n$
- cas moyen : $\mathcal{O}(\frac{n}{m})$. Si les clés sont uniformément distribuées, il y aura de l'ordre de $\frac{n}{m}$ éléments dans la liste $L[f_m(f(c))]$.

Une astuce permet de diminuer la complexité moyenne. Il suffit de s'assurer que $\frac{n}{m}$ soit une constante.

On peut alors utiliser un processus semblable à celui des listes où lorsque l'on a stocké $n = m$ éléments :

1. on double la fonction d'adressage
2. on recalcule le hash de tous les $n$ éléments qu'on replace dans la structure

On s'assure par là que $\frac{n}{m} \leq 2$. Comme de plus ce recalcule est effectué rarement on à :

{% note "**Proposition**" %}
La complexité en moyenne d'ajout, de recherche et suppression d'un élément dans un dictionnaire est $\mathcal{O}(1)$
{% endnote %}
{% details "preuve" %}

Le raisonnement est identique à la preuve des [$N$ ajouts successifs pour une liste](../../structure-liste/#preuve-liste-ajout){.interne}

{% enddetails %}

La structure de dictionnaire est donc une structure très efficace ! N'hésitez pas à l'utiliser car son temps moyen d'exécution est très rapide.

{% note "**À retenir**" %}
La complexité minimale et en moyenne de l'ajout, de la recherche et de la suppression d'un élément dans un dictionnaire est $\mathcal{O}(1)$.

La complexité maximale de ces méthodes est en $\mathcal{O}(n)$.
{% endnote %}

## Exercice fondamental

Exercice fondamental pour comprendre l'intérêt des dictionnaires.

- données :
  - une liste de $n$ prix différents deux à deux : $p_i$ ($0 \leq i < n$)
  - un crédit : $C$
- Question : donner deux indices $i$ et $j$ tels que $p_i + p_j = C$. On suppose qu'il existe toujours une solution.

On va essayer de répondre à cet exercice de trois façons différentes, toutes avec des complexités différentes. Une fois n'est pas coutume on écrira les algorithmes en python, car les dictionnaires sont bien plus souvent utilisés en programmation qu'en algorithmie. Si vous n'avez pas de notion pratique sur les dictionnaires en python, n'hésitez pas à aller jeter un coup d'œil à :

{% lien %}
[Dictionnaires python](/cours/coder-et-développer/bases-programmation/conteneurs/#ensembles-dictionnaires){.interne}
{% endlien %}

### Deux boucles for imbriquées

Comme il faut trouver deux indices différents dans la liste $p$ (à $n$ éléments), deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Code python :

```python
def recherche(p):
    for i in range(n):
        for  in range(i + 1, n):
            if p[i] + p[j] == C:
                return (i, j)
```

Deux boucles imbriquées et le reste en $\mathcal{O}(1)$ : la complexité totale est en $\mathcal{O}(n^2)$.

{% enddetails %}

### Une boucle et un tri

On trie la liste (ce qui donne la complexité de la solution) puis il suffit de remarquer que :

- si $P[i] + P[j] > C$ alors $P[i'] + P[j'] > C$ pour tous $i' \leq i$ et $j' \geq j$
- si $P[i] + P[j] < C$ alors $P[i'] + P[j'] < C$ pour tous $i' \geq i$ et $j' \leq j$

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Code python :

```python
def recherche(p):

    p2 = sorted(p)

    i = 0
    j = n-1
    while p2[i] + p2[j] != C:
        if p2[i] + p2[j] < C:
            i += 1
        else:
            j -= 1

        if i > j:
            return None
    
    i2 = None
    j2 = None
    for k in range(len(p)):
        if p[k] == p2[i]:
            i2 = k
        elif p[k] == p2[j]:
            j2 = k

    return (i2, j2)
```

Notez que cette solution est aussi en $\mathcal{O}(n\cdot log(n))$ en moyenne car le tri utilisé par python est de complexité $\mathcal{O}(n\cdot log(n))$ en moyenne.

{% enddetails %}

### Avec un dictionnaire

Solution en $\mathcal{O}(n)$ en moyenne et complexité maximale $\mathcal{O}(n^2)$

L'idée est de mettre les prix en clé et les indices en valeur.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Code python v1 :

```python
def recherche(p):
    d = dict()

    for i in range(n):
        d[p[i]] = i

    for u in range(n):
        p2 = C - p[u] 
        if p2 in d:
            v = d[p2]
            return min(u, v), max(u, v)
```

Sans tout remplir, qui évite un `max`{.language-} et est plus idiomatique :

```python
def recherche(p):
    d = dict()

    for j in range(n):
        if C - p[j] in d:
            return (d[C-p[j]], j)
        d[p[j]] = j
    return None
```

{% enddetails %}

### Expérimentation

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant au moins une solution.
{% endexercice %}
{% details "solution" %}

> TBD On tire des pi au hasard dans [1, pmax] sans remise (avec choice) puis on choisi i et j avec C = pi + pj

{% enddetails %}

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant exactement une solution.
{% endexercice %}
{% details "solution" %}

> TBD On tire des di dans [-m, m] tel que si di est tiré, on ne peut plus tirer -di (on met tout ca dans des ensembles) pi = C/2 + di pour i ≤ n-2. Les deux derniers sont choisis  pour que la somme fasse C.

{% enddetails %}

{% faire %}
Implémentez en python les 3 algorithmes précédent pour montrer voir la rapidité croissantes avec laquelle ces problèmes sont traités
{% endfaire %}
