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

C'est l'invention de la pile : Hamblin's stack pour les expressions et les variables.
> puis Disjkstra a vu que ça permettait de gérer l'appel (possiblement récursif) de fonctions.

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
            si suivant > 0:
                rendre Faux
            rendre Vrai
        méthode pleine() → booléen:
            si (T.longueur - suivant) > 0:
                rendre Vrai
            rendre Faux
        méthode nombre() → entier:
            rendre suivant
```

> TBD : complexités

## Exemple fondamental : décurryfication d'un algorithme récursif

> rendre itératif des algorithmes récursifs

> TBD : exo pile/file simple (jouer avec la structure) et usage dans des algos. Montrer aussi que la pile peut être utilisée pour stocker des variables : faire fibo et enfin dire que c'est comme ça en mémoire : heap et stack. Donner exemple de l'appel de fonction et de la recursion.

> TBD grace à une todo list (aka une pile)
<https://www.youtube.com/watch?v=HXNhEYqFo0o>

> TBD :
>
> cours ici  <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration>
> On a vu recursion terminale et parfois ça marche pas ex. fibonnacci.
> on reprend et on regarde comment on ferait en stockant les infos à fire.

> - <https://www.lirmm.fr/~dony/notesCours/c4.s.pdf>
> - <https://www.enseignement.polytechnique.fr/informatique/INF321/Amphis12/amphi5.pdf>
> - <https://web4.ensiie.fr/~dubois/recursivite.pdf> fact est récursive primitive.L'écrire de façon itérative.

avec un tant que utiliser <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration>
>
