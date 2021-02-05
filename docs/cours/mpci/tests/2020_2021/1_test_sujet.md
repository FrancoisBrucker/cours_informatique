---
layout: page
title:  "sujet Test 1 : code"
category: cours
tags: informatique cours 
---


Toute fonction écrite doit être testée.

Faites les questions dans l'ordre. Ce n'est pas grave si vous ne faites pas toutes les questions, mais si vous donnez une fonctions sans ses tests elle ne sera pas notée.

Questions :

En utilisant le fait que le modulo s'écrit `%` en python.

## 1. écrivez une fonction *syracuse* telle que

* **paramètre d'entrée** : un entier $x$

* **sortie** :

  * $x/2$ si $x$ est pair
  * $3x + 1$ si $x$ est impair

## 2. une fonction qui rend tous les éléments de la suite de syracuse associée à un nombre

* **entrée** : un entier $x$
* **sortie** : les élément de la suite de syracuse associée à $x$

La suite de syracuse est définie telle que :

* $u_0 =x$
* $u_{n+1} = {syracuse}(u_n)$
* on s'arrête lorsque $u_n =1$

## 3. le programme principale demande à l'utilisateur de taper un nombre et rend la suite de syracuse de ce nombre
