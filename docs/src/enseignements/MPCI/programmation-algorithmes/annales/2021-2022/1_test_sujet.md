---
layout: layout/post.njk

title:  "sujet Test 1 : code"
authors:
    - François Brucker
---

Toute fonction écrite doit être testée.

Faites les questions dans l'ordre. Ce n'est pas grave si vous ne faites pas toutes les questions, mais si vous donnez une fonction sans ses tests ou qui ne fonctionne pas elle ne sera pas notée.

Enfin, faites aussi en sorte que votre code ait 0 défaut de style (le linter ne doit pas râler).

## 1. écrivez une fonction *valeur* telle que

* **paramètres d'entrée** :
  1. une liste de $n+1$ réels $[a_0, \dots, a_n]$ $n \geq 0$
  2. un réel $x$

* **sortie** :
  * $\sum_{i=0}^na_i x^i$

Vous pourrez utiliser le fait que `x ** i`{.language-} en python soit égal à $x^i$

## 2. programme principal

Votre programme doit demander à l'utilisateur un entier $x$ et il rend la valeur $\sum_{i=0}^{4} x^i$.

* vous utiliserez la fonction créée en 1
* vous supposerez que l'utilisateur ne se trompe pas (pas besoin de gérer ses erreurs potentielles)
* vous utiliserez la fonction `input()`{.language-} qui rend une chaîne de caractères tapée par l'utilisateur
* `int(x)`{.language-} est l'entier représenté par la chaîne de caractères `x`{.language-}

## 3. écrivez une fonction *somme* telle que

* **paramètres d'entrée** :
  1. une liste de réels $[a_0, \dots, a_n]$
  2. une liste de réels $[b_0, \dots, b_m]$

* **sortie** :
  * $[a_0 + b_0, \dots, a_n+b_n]$ si $n = m$
  * $[a_0 + b_0, \dots, a_n+b_n, b_{n+1}, \dots, b_m]$ si $n < m$
  * $[a_0 + b_0, \dots, a_m+b_m, a_{m+1}, \dots, a_n]$ si $m < n$

Vous pourrez utiliser la méthode `append`{.language-} des listes qui ajoute un élément en fin de liste (si `l= [1, 2]`{.language-}, l'instruction `l.append(3)`{.language-} **modifie** `l`{.language-}, pour qu'elle soit égale à `l= [1, 2, 3]`{.language-})

## 4. écrivez une fonction *produit* telle que

* **paramètres d'entrée** :
  1. une liste de réels $[a_0, \dots, a_n]$
  2. une liste de réels $[b_0, \dots, b_m]$
* **sortie**  (on suppose):
  * une liste $[c_0, \dots, c_{m+n}]$ telle que $c_k = \sum_{i+j=k}a_ib_j$ pour tout $0\leq k \leq m+n$