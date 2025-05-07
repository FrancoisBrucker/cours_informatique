---
layout: layout/post.njk
title: "Dictionnaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer dans cette  partie une structure de donnée très utilisée en développement : le dictionnaire (_hash map_) aussi appelé le tableau associatif.

Cette structure utilise de façon sous-jacente une [fonctions de hachage](../fonctions-hash){.interne}.

## Fonction de hachage utilisée

Dans tout ce qui suit on considérera uniquement des données représentés par un tableau binaire. Ceci permettra de considérer que l'on peut appliquer ses fonctions à n'importe quel type de donnée via leur représentation binaire.

Nos fonctions de hachage seront donc dans toutes leurs généralités de type :

<div>
$$
f: \{0, 1\}^\star \rightarrow [0\mathrel{ {.}\,{.} } m[
$$
</div>

Puisqu'utilisés dans un algorithme :

- on doit pouvoir les calculer : on peut leur associer un algorithme `f(d: [bit]) → entier`{.language-},
- ce calcul doit être rapide : de complexité linéaire $\mathcal{O}(d.\mbox{\small longueur})$

De plus, pour que tout se passe bien en moyenne on supposera les supposera [utiles](../fonctions-hash/#définition-hachage-utile){.interne}.

## Principe

Le squelette de la structure de dictionnaire est la suivante :

```pseudocode
structure Dictionaire<V>:
    attributs:
        T: [V] ← tableau de longueur m
    méthodes:
        fonction f(clé: [bit]) → entier  # fonction de hachage utile de C dans [0, m[

        fonction get(clé: [bit]) → V:  # valeur ← self[clé] = valeur ← self.get(clé)
            rendre T[f(clé)]
        fonction set(clé: [bit], valeur: V) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            T[f(clé)] ← valeur

```

{% info %}
On utilise [le même abus que pour les listes](../../structure-liste/#structure-getter-setter){.interne} : pour un dictionnaire `d`{.language-} on écrira toujours `d[clé]`{.language-} à la place de `d.get(clé)`{.language-} ou de `d.set(clé, valeur)`{.language-}.
{% endinfo %}

En deux mots, un dictionnaire est une structure permettant accéder à des _valeurs_ via des _clés_. Elle généralise la structure de tableau où les clés ne peuvent qu'être que des indices.

En supposant que tout objet peut être converti sous sa forme binaire, on peut écrire :

```pseudocode
rgb ← Dictionaire<entier>

rgb["rouge"] ← 230
rgb["vert"] ← 12
rgb["bleu"] ← 255

couleur ← 2^16 * rgb["rouge"] + 2^8 * rgb["vert"] + 2^16 * rgb["bleu"]
```

On ne peut cependant bien sur pas utiliser cette structure en tant que tel à cause des collisions. Par exemple si `Dictionaire.f("bleu")`{.language-} =  `Dictionaire.f("rouge")`{.language-} le code précédent ne fonctionnera pas.

$m$ est très grand devant le nombre d'objet que l'on veut stocker cette probabilité de collision est tellement faible qu'on peut la considérer comme nulle, mais :

- si on veut garder des tailles de structure raisonnables et donc réduire $m$ au maximum,
- si on ne peut se permettre une collision de probabilité aussi faible-soit elle

Il faut trouver un moyen de les gérer aux mieux (c'est à dire avec une complexité maîtrisée).

{% info %}
Notez que cette préoccupation n'est pas toujours utile. Le logiciel git, utilisé quotidiennement pas des millions de personnes ne fait pas de gestion de collision car les probabilités de collision sont trop faibles.
{% endinfo %}

Enfin, en toute rigueur le premier exemple devrait plutôt s'écrire :

```pseudocode
rgb ← Dictionaire<entier>

rgb[bin("rouge")] ← 230
rgb[bin("vert")] ← 12
rgb[bin("bleu")] ← 255

couleur ← 2^16 * rgb[bin("rouge")] + 2^8 * rgb[bin("vert")] + 2^16 * rgb[bin("bleu")]
```

En utilisant la fonction `bin`{.language-} qui rend la représentation binaire de l'objet. Pour éviter cette indirection, on peut spécifier un type spécifique aux clés et utiliser la structure suivante, avec deux type génériques :

<span id="structure-deux-types-génériques"></span>

```pseudocode
structure Dictionaire<C, V>:
    attributs:
        T: [V] ← tableau de longueur m
    méthodes:
        fonction f(clé: C) → entier  # fonction de hachage utile de C dans [0, m[

        fonction get(clé: C) → V:  # valeur ← self[clé] = valeur ← self.get(clé)
            rendre T[f(clé)]
        fonction set(clé: C, valeur: V) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            T[f(clé)] ← valeur

```

Ce qui permet d'écrire :

```pseudocode
rgb ← Dictionaire<chaîne, entier>

rgb["rouge"] ← 230
rgb["vert"] ← 12
rgb["bleu"] ← 255

couleur ← 2^16 * rgb["rouge"] + 2^8 * rgb["vert"] + 2^16 * rgb["bleu"]
```

Pour alléger un peu les notations on ne spécifiera que le type des valeurs dans la suite de cette partie et on supposera, par _abus de notation_ que les clés sont transformés en leur équivalent binaire.

En revanche, dans le reste du cours, on spécifiera très souvent les types de clés et de valeurs pour éviter toute utilisation caché de fonctions (ici la fonction `bin`{.language-}).

## Gestion des collisions

Pour gérer les collisions, on utilise [le théorème fondamental du développement logiciel](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering) :

<span id="théorème-fondamental-développement-logiciel"></span>

{% note "**Théorème fondamental du développement logiciel (TFDL)**" %}
Tout problème peut être résolu en ajoutant une couche d'indirection supplémentaire.

_"We can solve any problem by introducing an extra level of indirection."_
{% endnote  %}

Dans notre cas, l'indirection consiste à stocker les couples (clé, valeur) possibles dans $T[f(i)]$ :

```pseudocode
structure Dictionaire<Type>:
    attributs:
        T: [Liste<([bit], Type)>] ← tableau de longueur m où chaque élément est initialisé à une liste vide
    méthodes:
        fonction f(clé: [bit]) → entier  # fonction de hachage utile de {0, 1}^* dans [0, m[

        fonction get(clé: [bit]) → Type:  # valeur ← self[clé] = valeur ← self.get(clé)
            pour chaque couple (c, v) de T[f(clé)]:
                si c == clé:
                    rendre v

        fonction set(clé: [bit], valeur: Type) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            l ← T[f(clé)]
            pour chaque i de [0 à l.longueur[ :
                c, v ← l[i]
                si c == clé:
                    l[i] ← (clé, valeur)
                    rendre ∅

            T[f(clé)].append((clé, valeur))

        fonction in(clé: [bit]) → booléen:  # x est dans self = self.in(x)
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre Vrai
            rendre Faux
        fonction delete(clé: [bit]) → ∅:  # supprime x de self = self.delete(x)
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre ∅

```

Chaque élément du tableau T de la structure est une liste qui stockera les différentes clés ayant même hash.

Comme on peut ajouter des clés, on a ajouté deux méthodes `Dictionaire.in`{.language-} et `Dictionaire.delete`{.language-} permettant respectivement de savoir si une clé est présente dans le dictionnaire et pour supprimer une clé.

Reprenons l'exemple précédent :

```pseudocode
rgb ← Dictionaire

rgb["rouge"] ← 230
rgb["vert"] ← 12
rgb["bleu"] ← 255

```

En supposant que :

- m = 3
- `Dictionaire.f("vert")`{.language-} = 0
- `Dictionaire.f("bleu")`{.language-} =  `Dictionaire.f("rouge")`{.language-} = 2

Le dictionnaire `rgb`{.language-} vaudra :

```pseudocode
rgb = [[("vert", 12)],                    # indice 0
       [],                                # indice 1
       [("rouge", 230), ("bleu", 255)]]   # indice 2
```

## Complexité de la recherche d'une clé

La complexité de la méthode `Dictionaire.get`{.language-} vaut la somme de ces différentes opérations :

1. Calcul de $f(\mbox{clé})$
2. Parcourir la liste des couples $(c, v)$ de la liste $T[f(\mbox{clé})]$ et comparer chaque $c$ à notre clé avec l'opérateur `==`{.language-} pour voir s'il sont égaux.

Le calcul du hash de la clé et de l'opérateur `==`{.language-} sont linéaires en la taille des objets.

Si la taille maximale des objets est connue, on a coutume de considérer que la complexité de l'opérateur `==`{.language-} et du calcul de $f(\mbox{clé})$ se fait en $\mathcal{O}(1)$. Une autre astuce est de calculer le hash de chaque objet à sa création et de le stocker (le hash devient un attribut universel de tout objet) : le calcul de $f(\mbox{clé})$ devient alors effectivement $\mathcal{O}(1)$ puisque cela revient à lire un attribut (c'est comme ça que procède python par exemple).

On en conclut que :

{% note %}
La recherche et l'affectation dans un dictionnaire est en $\mathcal{O}$ du nombre maximum de clé stockés avec la même valeur de hash.
{% endnote %}

## Taille de la structure

Pour garantir une bonne répartition des valeur de hash, il faut que $m$ soit grand ($2^{64}$ bits par exemple pour [sipHash](https://en.wikipedia.org/wiki/SipHash), la fonction de hash utilisé par python), mais on ne peut pas stocker un tableau aussi gigantesque pour chaque dictionnaire.

Pour résoudre ce problème on va encore une fois utiliser [le TFDL](./#théorème-fondamental-développement-logiciel){.interne} et ajouter une indirection.

On utilise une fonction supplémentaire appelée **fonction d'adressage** qui est une deuxième fonction de hachage dont maîtrise la taille de l'entier en sortie. Sa signature est :

```pseudocode
f(x: entier, m': entier) → entier
```

Et correspond à une famille de fonctions de hachage **utiles** $f_{m'}$ telles que $f(x, m') = f_{m'}(x)$ avec :

<div>
$$
f_{m'}: [0\mathrel{ {.}\,{.} } m[ \rightarrow [0\mathrel{ {.}\,{.} } m'[
$$
</div>

En toute généralité on a :

{% note "**Définition**" %}
Une **_fonction d'adressage_** est une famille $f_m$ de fonctions : de $\mathbb{N}$ dans $[0\mathrel{ {...} } m[$ définis pour tout entier $m$.
{% endnote %}

### Taille fixe

La version finale de la structure de dictionnaire est alors :

```pseudocode
fonction f(clé: [bit]) → entier  # fonction de hachage utile de {0, 1}^* dans [0, m[

structure Dictionaire<Type>:
    attributs:
        taille: entier

        T: [Liste<([bit], Type)>] ← tableau de longueur taille où chaque élément est initialisé à une liste vide
    méthodes:
        fonction fa(clé: [bit], m: entier) → entier  # fonction d'adressage

        fonction get(clé: [bit]) → Type:  # valeur ← self[clé] = valeur ← self.get(clé)
            pour chaque couple (c, v) de T[fa(f(clé), T.longueur)]:
                si c == clé:
                    rendre v

        fonction set(clé: [bit], valeur: Type) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            l ← T[fa(f(clé), T.longueur)]
            pour chaque i de [0 à l.longueur[ :
                c, v ← l[i]
                si c == clé:
                    l[i] ← (clé, valeur)
                    rendre ∅

            T[fa(f(clé), T.longueur)].append((clé, valeur))

        fonction in(clé: [bit]) → booléen:  # x est dans self = self.in(x)
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre Vrai
            rendre Faux
        fonction delete(clé: [bit]) → ∅:  # supprime x de self = self.delete(x)  
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre ∅

```

La fonction d'adressage permet de choisir une taille de tableau qui correspond à nos besoins. De plus, on peut considérer que son calcul est toujours en $\mathcal{O}(1)$ car elle sera toujours utilisée avec un nombre de taille fixe qui est le hash d'un objet.

Cette version permet d'avoir une structure dont la taille est proportionnelle au nombre de valeurs stockées mais dont le nombre de collisions va augmenter plus on stocke de valeurs. On peut améliorer ça en utilisant la même technique que pour les listes.

### Taille dynamique

Enfin, pour minimiser les collisions, on peut redimensionner le tableau si le nombre d'éléments stockés est supérieur à sa longueur. C'est cette structure qui est appelée dictionnaire et correspond à la structure :

<span id="structure-dictionnaire"></span>

```pseudocode
fonction f(clé: [bit]) → entier  # fonction de hachage utile de {0, 1}^* dans [0, m[

structure Dictionaire<Type>:
    attributs:
        taille: entier ← 0

        T: [Liste<([bit], Type)>] ← tableau de longueur taille où chaque élément est initialisé à une liste vide
    méthodes:
        fonction fa(clé: [bit], m: entier) → entier  # fonction d'adressage

        fonction get(clé: [bit]) → Type:  # valeur ← self[clé] = valeur ← self.get(clé)
            pour chaque couple (c, v) de T[fa(f(clé), T.longueur)]:
                si c == clé:
                    rendre v

        fonction set(clé: [bit], valeur: Type) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            l ← T[fa(f(clé), T.longueur)]
            pour chaque i de [0 à l.longueur[ :
                c, v ← l[i]
                si c == clé:
                    l[i] ← (clé, valeur)
                    rendre ∅

            si taille == T.longueur:
                T2 ← T

                taille ← 0
                T ← un nouveau tableau de Liste<([bit], Type)> de longueur 2 * T2.longueur où chaque élément est initialisé à une liste vide
                pour chaque l de T2:
                    pour chaque (c, v) de l:
                        set(c, v)

                set(clé, valeur)
            sinon:
                taille ← taille + 1

                l ← T[fa(f(clé), T.longueur)]
                pour chaque i de [0 à l.longueur[ :
                    c, v ← l[i]
                    si c == clé:
                        l[i] ← (clé, valeur)
                        rendre ∅

                T[fa(f(clé), T.longueur)].append((clé, valeur))

        fonction in(clé: [bit]) → booléen:  # x est dans self = self.in(x)
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre Vrai
            rendre Faux
        fonction delete(clé: [bit]) → ∅:  # supprime x de self = self.delete(x)  
            l ← T[f(clé)]
            pour chaque e de l :
                c, v ← e
                si c == clé:
                    l.delete((c, v))
                    rendre ∅

```

Tout comme les listes, une fois que le nombre d'élément stocké dépasse la capacité ou double la capacité. Dans notre cas cela revient à changer de fonction d'adressage et de tout restocker.

## Complexités des méthodes

En supposant que la fonction d'adressage est une fonction de hash utile,
On va estimer la complexité des opérations suivantes :

- création de la structure
- suppression de la structure (liste de liste)
- ajout d'un élément à la structure
- recherche d'un élément à la structure
- suppression d'un élément à la structure

On utilisera ici la structure finale et dynamique du dictionnaire.

### Création de la structure

La taille initiale est nulle donc :

{% note %}
La création d'un dictionnaire prend $\mathcal{O}(1)$ opérations.
{% endnote %}

### Suppression de la structure

La suppression du dictionnaire implique la suppression de toutes les listes stockées :

{% note %}
La suppression d'une structure de dictionnaire prend $\mathcal{O}(T.\mbox{\small longueur})$ opérations.
{% endnote %}

### Ajout/recherche et suppression d'un élément

Les complexités sont identiques car cela revient à chercher si la clé $c$ est déjà stockée ou non dans la structure.

Cette complexité peut aller de :

- cas le meilleur : $\mathcal{O}(1)$. Ceci arrive lorsque la liste $T[f_m(f(c))]$ est vide
- cas le pire : $\mathcal{O}(\mbox{taille})$ (en considérant que la complexité de l'opérateur `==`{.language-} vaut $\mathcal{O}(1)$). Ceci arrive lorsque tous les éléments de la liste ont même hash, le nombre d'élément de $T[f_m(f(c))]$ vaudra $\mbox{taille}$, le nombre d'éléments stockés.
- cas moyen : $\mathcal{O}(\frac{\mbox{taille}}{T.\mbox{\small longueur}})$. Si les clés sont uniformément distribuées, il y aura de l'ordre de $\frac{\mbox{taille}}{T.\mbox{\small longueur}}$ éléments dans la liste $L[fa(f(c), m)]$.

Comme $\frac{\mbox{taille}}{T.\mbox{\small longueur}} \leq 1$ la complexité moyenne de recherche sera de $\mathcal{O}(1)$ et un raisonnement identique à la preuve des [$N$ ajouts successifs pour une liste](../../structure-liste/#preuve-liste-ajout){.interne} montre que la complexité amortie moyenne de l'ajout dun élément dans une liste vaut également $\mathcal{O}(1)$ (la complexité amortie valant $\mathcal{O}(\mbox{taille})$ puisqu'on pourrait toujours se retrouver dans le cas le pire). On a donc :

{% note "**Proposition**" %}
La complexité **en moyenne** d'ajout, de recherche et suppression d'un élément dans un dictionnaire est $\mathcal{O}(1)$
{% endnote %}

La structure de dictionnaire est donc une structure très efficace le cas le pire arrivant très rarement !

{% attention "**À retenir**" %}
La complexité minimale et en moyenne de l'ajout, de la recherche et de la suppression d'un élément dans un dictionnaire est $\mathcal{O}(1)$.

La complexité maximale de ces méthodes est en $\mathcal{O}(n)$ où n$ est le nombre d'éléments stockés dans la structure.
{% endattention %}

## Utilisation

Tableaux associatifs et dictionnaire sont deux synonymes. On utilisera cependant plus volontiers le terme de dictionnaire en code (popularisé par python qui en fait un usage intensif) que de tableau associatif plus daté.

Ils permettent d'utiliser directement les donnés du problèmes sans avoir besoin d'une indirection.

Par exemple :

```pseudocode
nombre_pommes ← Dictionnaire<chaîne>
nombre_pommes["fuji"] ← 12
nombre_pommes["gala"] ← 3
nombre_pommes["pink lady"] ← 42
```

Plutôt que de d'abord associer un indice aux données :

```pseudocode
pommes_indirection = ["fuji", "gala", "pink lady"]
nombre_pommes ← Tableau de chaîne de longueur 3
nombre_pommes[0] ← 12
nombre_pommes[1] ← 3
nombre_pommes[2] ← 42
```

{% attention "**À retenir**" %}
Si en algorithmie on préférera souvent manipuler les donnés sous la forme d'indices (via une indirection) pour obtenir une complexité de $\mathcal{O}(1)$, l'usage direct des données via un dictionnaire est très utilisé en code car le gain en simplicité vaut _a priori_ la légère perte de complexité ($\mathcal{O}(1)$ en moyenne seulement).

{% endattention %}

Initialiser un dictionnaire avec des données se fait en utilisant des accolades comme on le ferait pour spécifier les attributs d'une structure normale. Par exemple :

```pseudocode
nombre_pommes ← Dictionaire<entier> {"fuji": 12, "gala": 3, "pink lady": 42}
```
