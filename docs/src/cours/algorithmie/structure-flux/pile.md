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

> TBD classique avec notation polonaise inverse <https://thibautdeguillaume.fr/documents/nsi_terminale/polonaise_inverse.pdf> : on met l'opérateur à droite des deux autres. Plus besoin de parenthèses !

> `1 + 2 - (3+4) * (5 + 6)` devient `1 2 + 3 4 + 5 6 + * -`
> avec algo si opération dépile op dépile

C'est l'invention de la pile : Hamblin's stack pour stocker les variables.
> puis Disjkstra a vu que ça permettait de gérer l'appel (possiblement récursif) de fonctions : : heap et stack. Donner exemple de l'appel de fonction et de la recursion.


{% lien %}
[Histoire de La pile](https://www.youtube.com/watch?v=2vBVvQTTdXg)
{% endlien %}

### Implémentation

```pseudocode
structure Pile:
    attributs:
        T: [entier]
        suivant: entier
    création(taille: entier) → Pile:
        T ← un nouveau tableau d'entiers de taille taille
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
            si (nombre() == T.longueur):
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
