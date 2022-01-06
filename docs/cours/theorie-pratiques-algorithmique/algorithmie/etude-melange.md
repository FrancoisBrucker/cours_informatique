---
layout: page
title:  "étude / mélanger un tableau"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude :  mélanger un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %})
>
> prérequis :
>
>* [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
{: .chemin}

Nous allons étudier ici deux algorithmes permettant de mélanger un tableau. Commençons par identifier le problème. Nous allons utiliser le problème suivant, qui consiste à rendre une permutation des $n$ premiers entiers :

* nom : permutation
* entrée : un nombre $n$
* sortie : un tableau de taille $n$ contentant les entiers des 0 à $n-1$ dans un ordre aléatoire

> Ce problème est bien sur équivalent à mélanger un tableau, il suffit de 

>* utile pour les complexité en moyenne par exemple où il faut trouver des valeur aléatoires
>* dépend d'un nombre aléatoire. On fera ça plus tard, pour l'instant on suppose qu'on sait le faire.
{: .tbd}



## maths

suite de transpositions

## avec un tri

On trie des couples en python

## fisher-yates

## algorithme de python

## ref

* <https://possiblywrong.wordpress.com/2014/12/01/card-shuffling-algorithms-good-and-bad/>
* <https://blog.codinghorror.com/the-danger-of-naivete/>
* <https://draftsim.com/mtg-arena-shuffler/> ce que les maths disent de l'aléatoire vs ce que les humains disent de l'aléatoire


## mélanger des listes ?

On s'est appuyé sur la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle) pour mélanger des listes.

Mais sommes-nous bien sur que le mélange est bien équiprobable ? Sinon nos mesures de complexité en moyenne seraient tous faux...

Rassurez vous c'est le cas. Elle utilise la méthode de mélange de [Fisher-Yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), qui est un algorithme linéaire permettant d'obtenir toutes les permutations possibles de façon équiprobable.

Ce qui est marrant c'est que cet algorithme est *"l'inverse"* d'un tri par sélection. 

Implémentez cet algorithme et vérifiez que pour la liste des 4 premiers entiers vous obtenez bien (sur un grand nombre d'essais) à peut prêt le même nombre des 24 permutations possibles.

Si vous voulez en savoir un peu plus sur cet algorithme et de comment générer un nombre aléatoire en python : <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>