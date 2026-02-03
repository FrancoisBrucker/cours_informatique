---
layout: layout/post.njk
title: "La pile"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[La pile](https://fr.wikipedia.org/wiki/Pile_(informatique))
{% endlien %}

La pile est une structure de donnée extrêmement utilisée. Elle permet de traiter en priorité la donnée **la plus récemment stockée**. On appelle également cette structure **_LIFO_** pour _last in, first out_ : on rend toujours la donnée la plus récemment stockée. La structure d'une pile de type `Type`{.language-} sera alors :

```pseudocode
structure Pile<T>:
    attributs:
        taille: entier
        
        #  autres attributs
    méthodes:
        fonction empile(donnée: T) → ∅  # push
        fonction depile() → T           # pop
        fonction nombre() → entier      # number

        fonction vide() → booléen       # empty
        fonction pleine() → booléen     # full
```

La taille de la pile doit être déterminée à la création. L'implémentation d'une pile nécessitera d'autres attributs comme on va le voir.

{% attention2 "**À retenir**" %}
La pile se comporte comme une pile d'assiettes, on prend ou on pose toujours celle du dessus de la pile.

Une donnée est traité une fois toutes les données plus récentes traitées. Elle permet de traiter les objets dans l'ordre inverse de leur introduction dans la structure.
{% endattention2 %}

## <span id="structure"></span>Implémentation

Une pile générique pourra être implémentée de cette façon :

<span id="structure-pile"></span>

```pseudocode
structure Pile<Type>:
    attributs:
        taille: entier
        
        T: [Type] ← nouveau [Type] de longueur taille
        suivant: entier ← 0
    méthodes:
        fonction empile(donnée: Type) → ∅:
            T[suivant] ← donnée
            suivant ← suivant + 1
        fonction depile() → Type:
            suivant ← suivant - 1
            rendre T[suivant]
        fonction nombre() → entier:
            rendre suivant

        fonction vide() → booléen:
            si nombre() == 0:
                rendre Faux
            rendre Vrai
        fonction pleine() → booléen:
            si (nombre() == taille):
                rendre Vrai
            rendre Faux
```

{% info %}
Une méthode peut utiliser une autre méthode : les méthodes `pleine`{.language-} et `vide`{.language-} utilisent `nombre`{.language-}.
{% endinfo %}

On voit facilement que :

{% note "**Proposition**" %}
Les complexités de toutes les méthodes de la structure `Pile`{.language-} sont en $\mathcal{O}(1)$.

Utiliser une pile peut se voire comme une opération élémentaire.
{% endnote %}

Prenons un exemple avec une pile d'entiers pour comprendre comment cette implémentation fonctionne.

Départ :

```text
       s  
Pile : 0123
```

Ajout d'un élément 1 :

```text
        s 
File : 0123
       1  
```

Ajout d'un élément 2 :

```text
         s
File : 0123
       12
```

On dépile un élément (2) :

```text
        s  
File : 0123
       1
```

Notez qu'une pile s'implémente très facilement en python avec une liste  (c'est même fait pour) :

{% exercice %}
Implémentez une structure de pile en python.
{% endexercice %}
{% details "solution" %}
On utilise une liste et les méthodes :

- `append`{.language-} pour ajouter un élément à la fin de la liste
- `pop`{.language-} pour supprimer et rendre le dernier élément de la liste

La fonction `len`{.language-} nous permet de connaître le nombre d'élément dans la structure, ce qui permet de calculer toutes les autres méthodes.

Dans un interpréteur python :

```python
>>> P = list()
>>> P.append(2)
>>> P.append(5)
>>> len(P)
2
>>> x = P.pop()
>>> print(x)
5
>>> x = P.pop()
>>> len(P)
0
>>> print(x)
2
>>>
```

Notez que comme une liste python n'a pas de borne, cette implémentation de la pile n'a pas de taille.
{% enddetails %}

## Exemples

Nous allons voir 2 exemples classiques de l'utilisation d'une pile pour écrire un algorithme. Il y a de très nombreux algorithmes qui utilisent une pile, pensez-y lorsque vous devez gérer des flux de données.

### Exemple historique : évaluation d'une expression

On utilise pour cela un ré-ordonnancement qui place l'opérateur après ses deux paramètres (et ce récursivement si nécessaire). Par exemple à la place d'écrire :

- `1 + 2` on écrit `[1, 2, +]`
- `1 - (2 + 4)` on écrit `[1, 2, 4, +, -]`

On évalue ensuite l'expression avec une pile `P`

```pseudocode
algorithme évaluation(T):
    P ← Pile {taille: T.longueur}
    pour chaque x de T:
        si x est un opérateur:
            b ← P.depile()
            a ← P.depile()
            y ← a `x` b  # effectue l'opération décrite par `x`
            P.empile(y)
        sinon:
            P.empile(x)

    rendre P.depile()
```

Faisons l'expérience avec l'expression `1 + 2 - (3+4) * (5 + 6)` qui devient le tableau `[1, 2, +, 3, 4, +, 5, 6, +, *, -]`. Les différentes opérations sur la pile par itération de la boucle `pour chaque`{.language-} sont :

1. **empile** 1
2. **empile** 2
3. **dépile** 2 ; **dépile** 1 ; **empile** 1 + 2 = 3
4. **empile** 3
5. **empile** 4
6. **dépile** 4 ; **dépile** 3 ; **empile** 3 + 4 = 7
7. **empile** 5
8. **empile** 6
9. **dépile** 6 ; **dépile** 5 ; **empile** 5 + 6 = 11
10. **dépile** 11 ; **dépile** 7 ; **empile** 11 * 7 = 77
11. **dépile** 77 ; **dépile** 3 ; **empile** 3 - 77 = -74

Le résultat final est le seul élément restant dans la pile, - 74, que l'on dépile à la fin

Plus besoin de parenthèses !

{% info %}
Cette notation est appelée [_notation polonaise inverse_](https://fr.wikipedia.org/wiki/Notation_polonaise_inverse) et est due à Hamblin. C'est le premier à utiliser directement la notion de pile, inventée par Turing.

C'est ensuite Dijkstra qui se rendra compte que la pile permet non seulement de stocker des variables mais également de gérer les appels de fonctions (on appelle cela _la pile d'appels_) et qui permet d'exécuter des fonctions (récursives ou non). On généralise à cette époque la notion de pile et de tas pour gérer les variables, les objets et les appels de fonctions de façon sous-jacente dans tout language de programmation.
{% endinfo %}
{% lien %}

L'histoire de la Pile et de ses multiples usages vaut le détour :

- [Histoire de la pile en texte](https://www.sigcis.org/files/A%20brief%20history.pdf)
- [Histoire de La pile en vidéo](https://www.youtube.com/watch?v=2vBVvQTTdXg)

{% endlien %}

### Exemple fondamental : décurryfication d'un algorithme récursif

{% lien %}
[Passer de récursif à itératif avec une pile](https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#conversion-using-stacks)
{% endlien %}

La pile est la structure permettant de transformer tout algorithme récursif en un algorithme itératif : il suffit de stocker dans la pile les variables avant de procéder à un appel !

#### Factoriel

Par exemple le calcul naif de la factorielle de façon récursive :

```pseudocode
algorithme fact_rec(n):
    si n < 1:
        rendre 1
    sinon:
        rendre n * fact_rec(n-1)
```

Pour mettre en place une pile de récursion, il faut bien décorréler les appels récursifs, le retour de la fonction et les autres opérations. Ce qui donne :

```pseudocode
algorithme fact_rec(n):
    # pos = 1 : début de la fonction
    si n < 1:
        r ← 1
    sinon:
        r' ← fact_rec(n-1)
        # pos = 2 : après la récursion
        r ← n * r'  # retour de la fonction
    rendre r
```

On peut maintenant mettre en place une pile qui va stocker :

- les paramètres d'appel : ici uniquement `n`{.language-}
- les variables locales : ici `r'`{.language-}
- l'endroit dans le code où doit continuer le code (avant et après les récursions).

Le retour de la fonction récursive, `r`{.language-}, ne sera jamais empilé.

On obtient le code :

```pseudocode
algorithme fact(n):
    P ← Pile<(entier, entier, entier)> {taille: n} # variables locales : n, r', pos
    P.empile((n, ∅, 1))
    tant que P.vide() est Faux:
        n, r', pos ← P.depile()

        si pos == 1:  # début de la fonction
            si n < 1:      
                r ← 1
            sinon:
                P.empile((n, r', 2))  # on continue l'appel courant
                P.empile((n-1, r', 1)) # une fois l'appel récursif fini
        sinon si pos == 2: # après la récursion
            r' ← r  # le résultat de la récursion précédente
            r ← n * r'  # le résultat actuel
    rendre r
```

{% details "code python" %}

```python
def fact(n):
    P = []
    P.append((n, None, 1))
    while len(P):
        n, r1, pos = = P.pop()

        if pos == 1:
            if n < 1:
                r = 1
            else:
                P.append((n, r1, 2))
                P.append((n-1, r1, 1))
        elif pos == 2:
            r1 = r
            r = n * r1
    return r
```

{% enddetails %}

Remarquez comment la variable pos permet de rediriger les différents appels récursifs. À chaque nouvel appel récursif on empile deux choses :

1. l'ancien appel qui devra continuer à sa nouvelle position une fois l'appel récursif terminée : `P.append((n, r1, 2))`{.language-}
2. l'appel récursif en lui même qui doit recommencer tout au début du code, en position 1 : `P.append((n-1, r1, 1))`{.language-}

Enfin, on remarque que la variable locale  `r'`{.language-} n'est jamais utilisé dans la récursion. On n'est donc pas obligé de l'empiler :

```pseudocode
algorithme fact(n):
    P ← Pile<(entier, entier)> {taille: n}
    P.empile((n, 1))
    tant que P.vide() est Faux:
        n, pos ← P.depile()

        si pos == 1:
            si n < 1:      
                r ← 1
            sinon:
                P.empile((n, 2))
                P.empile((n-1, 1)) 
        sinon si pos == 2:
            r ← n * r
    rendre r
```

{% details "code python" %}

```python
def fact(n):
    P = []
    P.append((n, 1))
    while len(P):
        n, pos = P.pop()

        if pos == 1:
            if n < 1:
                r = 1
            else:
                P.append((n, 2))
                P.append((n-1, 1))
        elif pos == 2:
            r = n * r
    return r
```

{% enddetails %}

#### Fibonacci

Fonctionne aussi avec plusieurs récursions :

```pseudocode
algorithme fibo_rec(n):
    si n < 3:
        rendre 1
    sinon:
        rendre fibo_rec(n-1) + fibo_rec(n-2)
```

```pseudocode
algorithme fibo_rec(n):
    # pos = 1
    si n < 3:
        r ← 1
    sinon:
        r' ← fibo_rec(n-1)
        # pos = 2
        r'' ← fibo_rec(n-2)
        # pos = 3
        r ← r' + r''
    rendre r
```

Ce qui donne :

```pseudocode
algorithme fibo(n):
    P ← Pile<(entier, entier, entier, entier)> {taille: 2^n}
    P.empile((n, ∅, ∅, 1))
    tant que P.vide() est fausse:
        n, r', r'', pos ← P.depile()

        si pos == 1:
            si n < 3:
                r ← 1
            sinon:
                P.empile((n, r', r'', 2))
                P.empile((n-1, r', r'', 1))
        sinon si pos == 2:
            r' ← r
            P.empile((n, r', r'', 3))
            P.empile((n-2, r', r'', 1))
        sinon si pos == 3:
            r'' ← r
            r ← r' + r''
    rendre r
```

{% details "code python" %}

```python
def fibo(n):
    P = []
    P.append((n, None, None, 1))
    while len(P):
        n, r1, r2, pos = P.pop()

        if pos == 1:
            if n < 3:
                r = 1
            else:
                P.append((n, r1, r2, 2))
                P.append((n-1, r1, r2, 1))
        elif pos == 2:
            r1 = r
            P.append((n, r1, r2, 3))
            P.append((n-2, r1, r2, 1))
        elif pos == 3:
            r2 = r
            r = r1 + r2
    return r
```

{% enddetails %}

Cette approche ne diminue pas la complexité, elle ne fait que la réécrire itérativement : il faut une taille de pile exponentielle (on a mis $2^n$). La complexité de l'algorithme itératif précédent est donc tout autant catastrophique que l'algorithme récursif initial.

{% exercice %}
Simplifiez le code précédent.
{% endexercice %}
{% details "corrigé" %}

 On a pas besoin de `r''`{.language-} :

```pseudocode
algorithme fibo(n):
    P ← Pile<(entier, entier, entier)> {taille: 2^n }  # n, r', pos
    P.empile((n, ∅, ∅, 1))
    tant que P.vide() est fausse:
        n, r', pos ← P.depile()

        si pos == 1:
            si n < 3:
                r ← 1
            sinon:
                P.empile((n, r', 2))
                P.empile((n-1, r', 1))
        sinon si pos == 2:
            r' ← r
            P.empile((n, r', 3))
            P.empile((n-2, r',  1))
        sinon si pos == 3:
            r ← r' + r
    rendre r
```

{% details "code python" %}

```python
def fibo(n):
    P = []
    P.append((n, 0, 1))
    while len(P):
        n, r1, pos = P.pop()

        if pos == 1:
            if n < 3:
                r = 1
            else:
                P.append((n, r1, 2))
                P.append((n-1, r1, 1))
        elif pos == 2:
            P.append((n, r, 3))
            P.append((n-2, r, 1))
        elif pos == 3:
            r = r1 + r
    return r
```

{% enddetails %}
{% enddetails %}
