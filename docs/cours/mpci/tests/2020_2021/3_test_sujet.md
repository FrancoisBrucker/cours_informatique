---
layout: page
title:  "sujet Test 3 : preuve"
category: cours
tags: informatique cours 
---

## 1. suppression de valeur

Donnez la complexité et prouvez  que l'algorithme suivant rend  une liste `L2`, restriction de L aux valeurs différentes de val.

* **Données** : `val` une valeur et `L` une liste de n valeurs
* **Début** :
  * création d’une liste `L2` vide
  * pour chaque élément `x` de L:
    * si `x `≠ `val`: ajoute `x` à la fin de `L2`
* **Rendre** : `L2`

## 2. suppression de doublon

Donnez la complexité et prouvez que l'algorithme suivant retourne une liste `L2` ne contenant qu’une seule occurrence de chaque valeur de `L`, en conservant le même ordre.

* **Données** : `L` une liste de n valeurs
* **Début** :
  * création d’une liste `L2` vide
  * tant que  `L` est non vide:
    * `x` = `L`[0]
    * ajoute `x` à `L2`
    * `L` = algorithme-question-1(L, x)
* **Rendre** : `L2`
