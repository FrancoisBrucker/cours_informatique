---
layout: layout/post.njk 
title: "Projet : alignement de séquences"

eleventyNavigation:
  key: "Projet : alignement de séquences"
  parent: Code

prerequis:
    - "../../algorithme/étude-alignement-séquences/"
    - "../programmation-objet/héritage/"
---

<!-- début résumé -->

Le but de ce projet est de coder les différents algorithmes d'alignements de séquences vus dans la partie [étude](../../algorithme/étude-alignement-séquences).

On considérera pour ce projet que le caractère *"-"* ne fait **pas** parti de l'alphabet $\mathcal{A}$ utilisé.

## Alignement

On rappelle qu'un alignement est un couple de deux séquences $(a^\star, b^\star)$ tels que :

* $a^\star$ et $b^\star$ soient de même longueur $L$
* chaque caractère de $a^\star$ et $b^\star$ soit dans $\mathcal{A} \cup \{ - \}$
* $(a^\star_i, b^\star_i) \neq (-,-)$ pour tout $0 \leq i < L$

1. Représentez *graphiquement* l'alignement (les 2 chaines l'une sous l'autre avec les `|`, comme dans l'[étude](../../algorithme/étude-alignement-séquences#distance-entre-chaines-))
2. pour un alignement $(a^\star, b^\star)$ donné, rendez les listes de chaînes de caractères permettant de passer de $a$ à $b$, comme fait dans l'[étude](../../algorithme/étude-alignement-séquences#évolution-dune-séquence-en-lautre)

Pour cela :

{% faire %}
Vous créerez une classe `Alignement` telle que :

* le constructeur prend les deux chaines $a^\star$ et $b^\star$
* cette classe doit contenir les méthodes suivantes :
  * `a()` qui rend $a$
  * `b()` qui rend $b$
  * `affiche()` qui affiche l'alignement
  * `evolution()` qui rend la liste de chaines permettant de passer de $a$ à $b$
{% endfaire %}

## Distance élémentaire

Pour deux séquences $a$ et $b$ il faut maintenant pouvoir calculer la distance d'édition avec la distance élémentaire :

1. calculer la matrice d'édition
2. rendre la distance d'édition
3. rendre un alignement

Pour cela :

{% faire %}
Vous créerez une classe `DistanceElem` telle que :

* le constructeur prend les deux chaines $a$ et $b$
* cette classe doit contenir les méthodes suivantes :
  * `matrice()` qui rend la matrice d'édition en utilisant la distance élémentaire
  * `dist()` qui rend la distance d'édition associée à la matrice
  * `alignement()` qui rend un alignement associé à la matrice.
{% endfaire %}

Vous vérifierez bien que les 3 alignements suivants sont corrects :

* "ACTGATT" et "GCTAATCG"
* "ACTGATT" et "-"
* "-" et "GCTAATCG"

## Cas général

On suppose que le coût est défini par une fonction dont la signature est `coût(x, y=None)` :

* si on renseigne `x` et `y` la fonction rend le coût de substitution entre `x` et `y`
* si on ne donne qu'un paramètre, la fonction rend le coût d'insertion/suppression de `x`

{% faire %}
Définissez la fonction de coût pour l'exemple du cas général de l'étude
{% endfaire %}

On peut maintenant créer l'alignement général :

{% faire %}
En héritant de la classe `DistanceElem`, créez la classe `Distance` qui réalise un alignement.

* le constructeur prend les deux chaines $a$ et $b$ et la fonction de coût
* cette classe doit contenir les même méthodes que la classe `DistanceElem`.

Arrangez vous pour conserver le plus de code possible entre les deux classes.
{% endfaire %}

## POur aller plus loin : étude biologique

{% info %}
Cette partie nécessite de connaître les dictionnaires python.
{% endinfo %}

Le fichier texte [pro-opsines.edi](./pro-opsines.edi) contient le code (sous la formes d'acides aminées) 3 protéines d'[opsines](https://fr.wikipedia.org/wiki/Opsine) qui permettent aux humains de voir en couleurs. Ces 3 protéines dérivent d'un ancêtre commun.

{% faire %}

1. Récupérez sous la forme de 3 chaines de caractères les 3 protéines (les lignes commençant par un ";" sont considérées comme des commentaire pour ce type de fichier)
2. faites l'alignement élémentaire des 3 protéines 2 à 2

{% endfaire %}

La distance élémentaire n'est pas très utilisée en pratique. Pour l'étude de séquences protéiques, on utilise souvent la matrice de similarité [BLOSUM62](https://en.wikipedia.org/wiki/BLOSUM) :

```python
PROTEINS = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X"]

BLOSUM_MATRIX = [
  [4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0],
  [-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1],
  [-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1],
  [-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1],
  [0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
  [-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1],
  [-1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
  [0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1],
  [-2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1],
  [-1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1],
  [-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1],
  [-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1],
  [-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1],
  [-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1],
  [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2],
  [1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0],
  [0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0],
  [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2],
  [-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1],
  [0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1],
  [-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1],
  [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
  [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1]
]
```

{% attention %}

* pour la transformer en matrice de coût, il faut prendre l'opposé de sa valeur !
* l'identité n'est plus de coût nul.

{% endattention %}

{% faire %}
Faites un alignement 2 à 2 de ces 3 protéines en utilisant la matrice de coût associée.
{% endfaire %}
