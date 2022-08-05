---
layout: page
title:  "sujet Test 6 : algorithmes gloutons"
category: cours
tags: code python
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [exercices]({% link cours/algorithme-code-theorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-theorie/exercices/2021-2022/index.md %}) / [sujet Test 6 : algorithmes gloutons]({% link cours/algorithme-code-theorie/exercices/2021-2022/6_test_sujet.md %})
{: .chemin}

Un automobiliste veut parcourir une route allant de la ville $A$ à la ville $B$. Cette route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. On suppose que les villes $A$ et $B$ possèdent une station service (stations numéros $0$ et $n-1$ respectivement).

La distance de la ville $A$ à la station numéro $i$ est rangée dans une liste `d` (la station $i$ est à `d[i]` kilomètres de $A$). On suppose enfin que chaque litre d'essence permet de parcourir 1km et que la voiture possède un réservoir de $r$ litres, initialement vide (on **doit** acheter de l'essence à la station de la ville $A$).

On cherche à rendre une liste `a` telle que $a[i]$ contient le nombre de litres d'essence acheté à la station $i$. On veut de plus que la quantité $Q$ soit minimum :

$$
Q = \sum_{0 \leq i < n} a[i]
$$

## 1 

### 1.1

S'il existe une solution, que vaut $Q$ ?

### 1.2

Donner une condition nécessaire et suffisante pour que le problème admette une solution.

## 2

### 2.1

Montrer qu'il existe une solution de coût minimal qui minimise aussi le nombre d'arrêts (on suppose que l'automobiliste ne s'arrête pas à la station $i$ si $a[i] = 0$).

### 2.2

Montrer à partir d'un exemple qu'il peut exister des solutions à coût minimal ayant plus d'arrêt que le nombre minimal.

## 3

Écrivez (et prouvez) un algorithme (glouton) qui résout le problème en un nombre minimum d'arrêt.



