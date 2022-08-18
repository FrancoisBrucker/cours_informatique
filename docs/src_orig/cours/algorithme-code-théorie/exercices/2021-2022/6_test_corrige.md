---
layout: page
title:  "corrigé Test 6 : algorithmes gloutons"
category: cours
tags: code python
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-théorie/index.md %}) / [exercices]({% link cours/algorithme-code-théorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-théorie/exercices/2021-2022/index.md %}) / [corrigé Test 6 : algorithmes gloutons]({% link cours/algorithme-code-théorie/exercices/2021-2022/6_test_corrige.md %})
{.chemin}

## 1 

### 1.1


S'il existe une solution, c'est que l'on peut arriver en $B$. Donc $Q \geq d[n-1]$ et vaut le nombre de litres d'essence achetée.

Comme chaque litre permet de faire 1km, c'est exactement le nombre maximum de kilomètre que la voiture peut faire.

### 1.2

Il faut et il suffit que la distance entre 2 stations services soient plus petite que la taille du réservoir.

## 2

### 2.1

Si l'on possède une solution avec un nombre d'arrêt minimum mais qui n'est pas minimum, c'est que la dernière station où l'on a acheté de l'essence — disons celle de numéro $i^\star$ — est telle que : $a[i^\star] > Q - d[n-1]$ (sinon on aurait pu s'arrêter encore moins). 

En supprimant $Q - d[n-1]$ à $a[i^\star]$ on obtient une solution minimale à nombre d'arrêt minimum.

### 2.2

Si l'on place une station tous les kilomètres et que l'on achète qu'un litre à chaque fois, on aura bien $Q = d[n-1]$ mais on s'est arrêté bien trop de fois : si l'on avait acheté 2 litres d'essence à chaque station on serait arrêté 2 fois moins de fois.

## 3

```python
p = 0
while p < n-1:
    i = p
    while (i < n) and d[i] - d[p] < r:
        a[i] = 0
        i += 1
    i -= 1
    a[i] = d[i] - d[p]
    p = i 
```

L'algorithme précédent cherche la station la plus lointaine possible à partir de la station courante (celle de numéro $p$) puis met juste le nombre de litre nécessaire pour y arriver : on a $Q = d[n-1]$ à la fin de l'algorithme.

Notre algorithme est optimal pour $Q$ car s'il existait  une solution telle que $Q > d[n-1]$, on pourrait acheter 1 litre d'essence en moins à la dernière station service tout en arrivant à $B$ : cette solution n'est pas optimale pour $Q$.

Montrons que notre solution est également minimale en nombre d'arrêt. Notons notre solution $S$. Pour tout autre solution $S'$, on note $i_{S'}$ la première station différente de notre solution (on a $i_{S'} > 0$). Cette station est forcément avant celle choisie par $S$ car notre algorithme choisi toujours la station la plus éloignée de la station courante. On note $i_S$ cette station. On peut alors supprimer la station $i_{S'}$ et aller directement :

* à $i_S$ si elle est avant la prochaine station de $S'$
* à la prochaine station de $S'$ si elle est avant $i_S$


Comme on met de plus juste assez d'essence, la nouvelle solution issue de $S'$ sera de coût inférieure à $S'$ et aura un nombre de station visitée plus petit : notre solution a donc un nombre de station minimum.
