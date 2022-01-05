---
layout: page
title:  "étude / algorithmes de tris"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude : algorithmes de tris]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %})
>
> prérequis :
>
>* [complexité moyenne]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-moyenne.md %})
>* [complexité d'un problème]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %})
>
{: .chemin}

désordre

> dépend d'un nombre aléatoire. On fera ça plus tard, pour l'onstnat on suppose qu'on sait le faire.
{: .tbd}

## mélanger des listes ?

On s'est appuyé sur la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle) pour mélanger des listes.

Mais sommes-nous bien sur que le mélange est bien équiprobable ? Sinon nos mesures de complexité en moyenne seraient tous faux...

Rassurez vous c'est le cas. Elle utilise la méthode de mélange de [Fisher-Yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), qui est un algorithme linéaire permettant d'obtenir toutes les permutations possibles de façon équiprobable.

Ce qui est marrant c'est que cet algorithme est *"l'inverse"* d'un tri par sélection. 

Implémentez cet algorithme et vérifiez que pour la liste des 4 premiers entiers vous obtenez bien (sur un grand nombre d'essais) à peut prêt le même nombre des 24 permutations possibles.

Si vous voulez en savoir un peu plus sur cet algorithme et de comment générer un nombre aléatoire en python : <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>