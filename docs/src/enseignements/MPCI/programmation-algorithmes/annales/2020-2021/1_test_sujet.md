---
layout: layout/post.njk

title:  "sujet Test 1 : code"
authors:
    - François Brucker
---


Toute fonction écrite doit être testée.

Faites les questions dans l'ordre. Ce n'est pas grave si vous ne faites pas toutes les questions, mais si vous donnez une fonctions sans ses tests elle ne sera pas notée.

{% info %}
En utilisant le fait que le modulo s'écrit `%`{.language-} en python.
{% endinfo %}

## 1. écrivez une fonction `syracuse`{.language-} telle que

* **entrée** : un entier $x$
* **sortie** :
  * $x/2$ si $x$ est pair
  * $3x + 1$ si $x$ est impair

## 2. une fonction qui rend tous les éléments de la suite de Syracuse associée à un nombre

* **entrée** : un entier $x$
* **sortie** : les élément de la suite de Syracuse associée à $x$

La suite de Syracuse est définie telle que :

* $u_0 =x$
* $u_{n+1} = \mbox{syracuse}(u_n)$
* on s'arrête lorsque $u_n =1$

## 3. le programme principale demande à l'utilisateur de taper un nombre et rend la suite de syracuse de ce nombre

* vous supposerez que l'utilisateur ne se trompe pas (pas besoin de gérer ses erreurs potentielles)
* vous utiliserez la fonction `input()`{.language-} qui rend une chaîne de caractère tapée par l'utilisateur
* `int(x)`{.language-} est l'entier représenté par la chaîne de caractère `x`{.language-} est un entier sous la forme d'une chaîne de caractère
