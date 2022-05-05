---
layout: page
title:  "projet / alignement de séquences"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [projet : alignement de séquences]({% link cours/algorithme-code-theorie/code/projet-alignement-sequences.md %})
>
> prérequis :
>
> * [étude : alignement de séquences]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %})
> * [héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/heritage.md %})
> * [projet : fichiers]({% link cours/algorithme-code-theorie/code/projet-fichiers.md %})
>
{: .chemin}

Le but de ce projet est de coder les différents algorithmes d'alignements de séquences vus dans la partie [étude]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %}).

On considérera pour ce projet que le caractère *"-"* ne fait **pas** parti de l'alphabet $\mathcal{A}$ utilisé.

## alignement

On rappelle qu'un alignement est un couple de deux séquences $(a^\star, b^\star)$ tels que :

* $a^\star$ et $b^\star$ soient de même longueur $L$
* chaque caractère de $a^\star$ et $b^\star$ soient soit dans $\mathcal{A} \cup \{ - \}$
* $(a^\star_i, b^\star_i) \neq (-,-)$ pour tout $0 \leq i < L$

1. Représentez *graphiquement* l'alignement (les 2 chaines l'une sous l'autre avec les `|`, comme dans l'[étude]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %}#distance-entre-chaines-))
2. pour un alignement $(a^\star, b^\star)$ donné, rendez les liste de chaînes de caraxtères permettant de passer de $a$ à $b$, comme fait dans l'[étude]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %}#évolution-dune-séquence-en-lautre)

Pour cela :

> Vous créerez une classe `Alignement` telle que :
>
> * le constructeur prend les deux chaines $a^\star$ et $b^\star$
> * cette classe doit contenir les méthodes suivantes :
>   * `a()` qui rend $a$
>   * `b()` qui rend $b$
>   * `affiche()` qui affiche l'alignement
>   * `évolution()` qui rend la liste de chaines permettant de passer de $a$ à $b$
>
{: .a-faire}

## distance élémentaire

Pour deux séquences $a$ et $b$ il faut maintenant pouvoir calculer la distance d'édition avec la distance élémentaire :

1. calculer la matrice d'édition
2. rendre la distance d'édition
3. rendre un alignement

Pour cela :

> Vous créerez une classe `DistanceElem` telle que :
>
> * le constructeur prend les deux chaines $a$ et $b$
> * cette classe doit contenir les méthodes suivantes :
>   * `matrice()` qui rend la matrice d'édition en utilisant la distance élémentaire
>   * `dist()` qui rend la distance d'édition associée à la matrice
>   * `alignement()` qui rend un alignement associé à la matrice.
>
{: .a-faire}

Vous vérifierez bien que les 3 alignements suivants sont corrects :

* "ACTGATT" et "GCTAATCG"
* "ACTGATT" et "-"
* "-" et "GCTAATCG"

## cas général

On suppose que le coût est défini par une fonction dont la signature est `cout(x, y=None)` :

* si on renseigne `x` et `y` la fonction rend le cout de substitution entre `x` et `y`
* si on ne donne qu'un paramètre, la fonction rend le cout d'insertion/suppression de `x`

> Définissez la fonction de cout pour l'exemple du cas général de l'étude
{: .a-faire}

On peut maintenant créer l'alignement général :

> En héritant de la classe `DistanceElem`, créez la classe `Distance` qui réalise un alignement.
>
> * le constructeur prend les deux chaines $a$ et $b$ et la fonction de coût
> * cette classe doit contenir les même méthodes que la classe `DistanceElem`.
>
> Arrangez vous pour conserver le plus de code possible entre les deux classes.
{: .a-faire}

## étude biologique

Le fichier texte [pro-opsines.edi](./pro-opsines.edi) contient le code (sous la formes d'acides aminées) 3 protéines d'[opsines](https://fr.wikipedia.org/wiki/Opsine) qui permettent aux humain de voir en couleur. Ces 3 protéines dérivent d'un ancêtre commun.

> 1. En utilisant les techniques de lecture de fichier, récupérez sous la forme de 3 chaines de caractères les 3 protéines
> 2. faites l'alignement élémentaire des 3 protéines 2 à 2
{: .a-faire}

La distance élémentaire n'est pas très utilisée en pratique. POur l'étude de séquences protéiques, on utilise souvent la matrice de similarité [BLOSUM62](https://en.wikipedia.org/wiki/BLOSUM).

**Attention** :

* pour la transformer en matrice de coût, il faut prendre l'opposé de sa valeur !
* l'identité n'est plus de coût nul.

> Faites un alignement 2 à 2 de ces 3 protéines en utilisant la matrice de coût associé. Le fichier de la matrice de similarité (dont il faut prendre l'opposé) peut être téléchargé [là](https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt)).
{: .a-faire}
