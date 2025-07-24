---
layout: layout/post.njk 
title:  "SAT et pseudo-code"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD plan
> TBD donner exemple fil rouge


5. résoudre sortie = résoudre entrée ! 
6. ce n'est pas encore Cook et Levin car pas polynomial.

## Formule logique et SAT

1. formule logique : avec et ou non. On a vu que ça fait tout. On peut "programmer" le tout en remplaçant des choses plus évoluée. Et max d'un tableau.
2. transformation en CNF avec Tseitin Linéaire rappel de ce que l'on a vu

s.

## Pseudo-code et transcription vers une formule logique

3. pseudo-code = pseudo-code binaire = instructions minimales
4. pseudo-code = formule logique = SAT (taille des tableaux = complexité)

> TBD attention à la taille des tableaux. Elle doit être connue à la "compilation" donc doit uniquement dépendre de la taille des entrées
à chaque étape toute les variables.

{% note "**Proposition**" %}
Un pseudo-code utilisant uniquement :

- des variables binaires ou des tableaux binaires
- l'opération logique `NAND`{.language-}
- des affectations de bit (variable binaire ou une case de tableaux)
- des boucles `tant que x: <bloc>`{.language-} avec $x$ une variable binaire :  le bloc n'est exécuté que si $x = 1$.
- des instructions conditionnelles de la forme `si x: <bloc>`{.language-} avec $x$ une variable binaire :  le bloc n'est exécuté que si $x = 1$.
 
A la même expressivité que [le pseudo-code classique](../pseudo-code/){.interne}.
{% endnote %}

> TBD tout algo est un sat.
> TBD on a vue que les opérations peuvent être mise sous forme logique. C'est aussi vrai pour les structures de contrôle.
> TBD on vu que toute fonction est un sat et que tout circuit logique est un sat. Le problème SAT va être fondamental.
> TBD dire que toute fonction booléenne vectorielle s'écrit comme une conjonction de clause. et que comme on passe d'un problème à l'autre, on peut le faire puisque nos entrées sont données.

> TBD dire taille des variables dépendant de la taille des entrées. Au pire = complexité. Ne change pas si dans P.

> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.


## Inversibilité de SAT

> Inversibilité du problème SAT

> TBD fct booléenne de l'addition ou du produit. Comme c'est une fonction booléenne cela permet d'avoir une réponse mais aussi d'avoir les entrées.
>
> TBD on y reviendra mais en crypto c'est crucial de ne pas pouvoir  faire... Par exemple pour les produit de 2 nombres premiers. On revient au fait que factor doit être de complexité importante.
> 
> polylog circuit et sat : <https://www.youtube.com/watch?v=6OPsH8PK7xM>
>
>

> exemple réduction :
>
