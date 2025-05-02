---
layout: layout/post.njk
title: "Tableaux associatifs ou dictionnaire"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer dans cette  partie une structure de donnée très utilisée en développement : le tableau associatif, aussi appelé dictionnaire.

Cette structure utilise de façon sous-jacente une [fonctions de hachage](../fonctions-hash){.interne}.

## Fonction de hachage utilisée

Dans tout ce qui suit on considérera uniquement des données représentés par un tableau binaire. Ceci permettra de considérer que l'on peut appliquer ses fonctions à n'importe quel type de donnée via leur représentation binaire.

Nos fonctions de hachage seront donc de type :

<div>
$$
f: \{0, 1\}^\star \rightarrow [0\mathrel{ {.}\,{.} } m[
$$
</div>

Puisqu'utilisés dans un algorithme :

- on doit pouvoir les calculer : on peut leur associer un algorithme `f(d: [bit]) → entier`{.language-},
- ce calcul doit être rapide : de complexité linéaire $\mathcal{O}(d.\mbox{\small longueur})$.

Enfin, pour que tout se passe bien en moyenne on supposera les supposera [utiles](../fonctions-hash/#définition-hachage-utile){.interne}.

## Principe

Le squelette de la structure de Dictionnaire est la suivante :

```pseudocode
structure Dictionnaire:
    attributs:
        taille: entier 

        T: [entier] ← tableau de longueur taille
    méthodes:
        fonction f(clé: [bit]) → entier

        # valeur ← self[clé] = valeur ← self.get(clé)
        fonction get(clé: [bit]) → entier:
            rendre T[f(clé)]

        # self[clé] ← valeur = self.set(clé, valeur)
        fonction set(clé: [bit], valeur) → ∅:
            T[f(clé)] ← valeur

```

On utilise [le même abus que pour les listes](../../structure-liste/#structure-getter-setter){.interne} : pour un dictionnaire `d`{.language-} on écrira toujours `d[clé]`{.language-} à la place de `d.T[d.f(clé)]`{.language-}.

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

{% attention "**À retenir**" %}
La complexité minimale et en moyenne de l'ajout, de la recherche et de la suppression d'un élément dans un dictionnaire est $\mathcal{O}(1)$.

La complexité maximale de ces méthodes est en $\mathcal{O}(n)$.
{% endattention %}
