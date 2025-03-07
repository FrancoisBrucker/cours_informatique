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

La pile est une structure de donnée extrêmement utilisée. Elle permet de traiter en priorité la donnée **la plus récemment stockée**. On appelle également cette structure **_LIFO_** pour _last in, first out_ : on rend toujours la donnée la plus récemment stockée. La structure d'une pile d'entiers sera alors :

```pseudocode
structure Pile:
    création(taille: entier) → Pile
    méthodes:
        méthode empiler(donnée: entier) → vide
        méthode dépiler() → entier
        méthode vide() → booléen
        méthode pleine() → booléen
        méthode nombre() → entier
```

La taille de la pile est déterminée à la création et, en plus des méthodes de stockage (`empiler`{.language-}) ert de rendu (`dépiler`{.language-}), possède deux méthodes permettant de savoir si la file est vide ou pleine et une méthode donnant le nombre de données stockées.

{% note "**Utilité de la pile**" %}
La pile se comporte comme une pile d'assiette, on prend ou on pose toujours celle du dessus de la pile.

Une donnée est traité une fois toutes les données plus récentes traitées. Elle permet de traiter les objets dans l'ordre inverse de leur introduction dans la structure.
{% endnote %}

### exemple : évaluation d'une expression

On utilise pour cela [la notation polonaise inverse](https://fr.wikipedia.org/wiki/Notation_polonaise_inverse) qui place l'opérateur après ses deux paramètres (et ce récursivement si nécessaire).

Par exemple à la place d'écrire :

- `1 + 2` on écrit `[1, 2, +]`
- `1 - (2 + 4)` on écrit `[1, 2, 4, +, -]`

On évalue ensuite l'expression avec une pile `P`

```pseudocode
algorithme évaluation(T):
    P ← une nouvelle pile de taille T.longueur
    pour chaque x du tableau:
        si x est un opérateur:
            b ← P.dépile()
            a ← P.dépile()
            y ← a `x` b
            P.empile(y)
        sinon:

    rendre P.dépile()
```

Faisons l'expérience avec l'expression `1 + 2 - (3+4) * (5 + 6)` qui devient le tableau `[1, 2, +, 3, 4, +, 5, 6, +, *, -]`. Les différentes opération sur la pile sont :

1. empile 1
2. empile 2
3. dépile 2
4. dépile 1
5. empile 1 + 2 = 3
6. empile 3
7. empile 4
8. dépile 4
9. dépile 3
10. empile 3 + 4 = 7
11. empile 5
12. empile 6
13. dépile 6
14. dépile 5
15. empile 5 + 6 = 11
16. dépile 11
17. dépile 7
18. empile 11 * 7 = 77
19. dépile 77
20. dépile 3
21. empile 3 - 77 = -74
22. dépile -74 qui est le résultat final.

Plus besoin de parenthèses !

On doit cette technique à Hamblin qui utilise la notion de pile, inventée par Turing.

C'est ensuite Dijkstra qui se rendra compte que la pile permet non seulement de stocker des variables mais également de gérer les appels de fonctions (on appelle cela _la pile d'appels_) et qui permet d'exécuter des fonctions (récursives ou non). On généralise à cette époque la notion de pile et de tas pour gérer les variables, les objets et les appels de fonctions de façon sous-jacente dans tout language de programmation.

{% lien %}

- [Histoire de la pile en texte](https://www.sigcis.org/files/A%20brief%20history.pdf)
- [Histoire de La pile en vidéo](https://www.youtube.com/watch?v=2vBVvQTTdXg)

{% endlien %}

### Implémentation

```pseudocode
structure Pile:
    attributs:
        T: [entier]
        longueur: entier
        suivant: entier
    création(taille: entier) → Pile:
        T ← un nouveau tableau d'entiers de longueur taille
        longueur ← taille
        suivant ← 0
    méthodes:
        méthode empiler(donnée: entier) → vide:
            T[suivant] ← donnée
            suivant ← suivant + 1
        méthode dépiler() → entier:
            suivant ← suivant - 1
            rendre T[suivant]
        méthode vide() → booléen:
            si nombre() == 0:
                rendre Faux
            rendre Vrai
        méthode pleine() → booléen:
            si (nombre() == longueur):
                rendre Vrai
            rendre Faux
        méthode nombre() → entier:
            rendre suivant
```

{% info %}
Une méthode peut utiliser une autre méthode : les méthodes `pleine`{.language-} et `vide`{.language-} utilisent `nombre`{.language-}.
{% endinfo %}

On voit facilement que :

{% note "**À retenir**" %}
Les complexités de toutes les méthodes de la structure `Pile`{.language-} sont en $\mathcal{O}(1)$.

Utiliser une pile peut se voire comme une opération élémentaire.
{% endnote %}

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

## Exemple fondamental : décurryfication d'un algorithme récursif

{% lien %}
[Passer de récursif à itératif avec une pile](https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#conversion-using-stacks)
{% endlien %}

La pile est la structure permettant de transformer tout algorithme récursif en un algorithme itératif : il suffit de stocker dans la pile les variables avant de procéder à un appel !

Par exemple le calcul naif de la factorielle de façon récursive :

```pseudocode
algorithme fact_rec(n):
    si n < 1:
        rendre 1
    sinon:
        rendre n * fact_rec(n-1)
```

> TBD factoriel avec pile

Fonctionne aussi avec plusieurs récursions :

```pseudocode
algorithme fibo_rec(n):
    si n < 3:
        rendre 1
    sinon:
        rendre fibo_rec(n-1) + fibo_rec(n-2)
```

> TBD Fibonacci avec pile

Cette approche ne diminue cependant pas la complexité, elle ne fait que la réécrire itérativement.

> TBD Dijkstra appel de fonction est identique.
