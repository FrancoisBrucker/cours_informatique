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
Le but de cette partie est de montrer que l'on peut "_compiler_" toute fonction de signature `f(e:[bit]) → [bit]`{.language-}  pseudo-code épuré en une fonction SAT

## Pseudo-code épuré

On a vu qu'écrire un pseudo-code pouvait se résumer sans perte de généralité au fait de n'utiliser que des types `bit`{.language-} et `[bit]`{.language-} et l'opération logique `NAND`{.language-}. On peut même aller plus loin est supposer sans perte de généralité que les seules structures de contrôle autorisées sont :

- `si x: ...bloc...`{.language-} où `x` est une variable binaire. Le bloc n'est exécuté que si `x = 1`{.language-},
- `tant que x: ...bloc...`{.language-} où `x` est une variable binaire. Le bloc n'est exécuté que tant que `x = 1`{.language-}.

Une ligne de ce pseudo-code épuré ne peut donc être qu'un des choix suivant :

1. création et affectation d'une variable :
  1. `x`{.language-} où $x$ est une variable de type `bit`{.language-} : création d'une variable de type `bit`{.language-} et initialisation à 0
  2. `x[:K]`{.language-} création d'une variable de type `[bit]`{.language-} à $K$ éléments
  3. `x[:u(k)]`{.language-} création d'une variable de type `[bit]`{.language-} à $u(k)$ éléments
2. affectation d'une variable de type `bit`{.language-} : 
  1. `x ← 0`{.language-} où $x$ est une variable de type `bit`{.language-}
  2. `x ← 1`{.language-} où $x$ est une variable de type `bit`{.language-}
  3. `x ← y`{.language-} où $x$ et $y$ sont des variables de type `bit`{.language-}
  4. `x ← y[K]`{.language-} où $x$ est une variable de type `bit`{.language-}, $y$ une variable de type `[bit]`{.language-} et $K$ un entier
  5. `x ← y[u(i)]`{.language-} où $x$ est une variable de type `bit`{.language-}, $y$ et $i$ deux variables de type `[bit]`{.language-}
3. affectation d'une case d'un tableau de type `[bit]`{.language-} avec indice constant : `x[K] ← y`{.language-} où $K$ est un entier, $x$ est une variable de type `[bit]`{.language-} et $y$ est une variable de type `bit`{.language-}
4. affectation d'une case d'un tableau de type `[bit]`{.language-} avec indice déterminé par une variable : `x[u(i)] ← y`{.language-} où $x$ et $i$ sont des variable de type `[bit]`{.language-} et $y$ est une variable de type `bit`{.language-}
5. instruction de contrôle :
  1. `si x:`{.language-} où $x$ est une variable de type `bit`{.language-}
  2. `tant que x:`{.language-} où $x$ est une variable de type `bit`{.language-}
6. opération `x ← NAND(y, z)`{.language-} où $x$, $y$ et $z$ sont des variables de type `bit`{.language-}

Toutes les instructions vont nécessiter $\mathcal{O}(1)$ opérations élémentaires à part les instructions où il faut utiliser la fonction $u()$ qui ajoute $\mathcal{O}(n)$ opérations élémentaires où $n$ est la longueur du tableau en entrée.

> TBD : peut dériver le reste, comme `x[u(i)] ← 0`{.language-}, `x[u(i)] ← y[u(j)]`{.language-} ou encore `si x[u(i)]:`{.language-} avec ces primitives.

## Formule logique et SAT

Un pseudo-code épuré est assimilable à une liste d'instructions


1. formule logique : avec et ou non. On a vu que ça fait tout. On peut "programmer" le tout en remplaçant des choses plus évoluée. Et max d'un tableau.
2. transformation en CNF avec Tseitin Linéaire rappel de ce que l'on a vu

s.

> TBD attention complexité spatiale et temporelle.
>- création et affectation d'une variable :
  - `x ← 0`{.language-} où $x$ est une variable de type `bit`{.language-} : création d'une variable de type `bit`{.language-} et initialisation à 0
  - `x[:K] ← 0`{.language-} création d'une variable de type `[bit]`{.language-} à $K$ éléments et initialisation de chacun de ses éléments à 0
  - `x[:u(k)] ← 0`{.language-} création d'une variable de type `[bit]`{.language-} à $u(k)$ éléments et initialisation de chacun de ses éléments à 0

> TBD faire la fonction associe un déplacement pour contraindre toute case allouée à être utilisée avec un dictionnaire de taille la complexité, change rien si poly on  est en complexité au carré.
> TBD mais cases non initialisé implique résultat pas déterministe (aussi dans la vraie vie...) donc on alloue = bonne pratique et on force ici: `t[:n] ← 0` pour allouer. NB ne change rien. en vrai mais plus propre. même en code.

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


5. résoudre sortie = résoudre entrée ! 
6. ce n'est pas encore Cook et Levin car pas polynomial.

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
