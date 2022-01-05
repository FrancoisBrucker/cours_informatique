---
layout: page
title:  "Complexité d'un problème"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [complexité d'un problème]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %})
>
> prérequis :
>
>* [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
{: .chemin}

On l'a vu lors de l'[étude de l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %}), un même problème peut avoir plusieurs algorithmes solutions, certains étant meilleurs que d'autres. On peut alors se poser la question de la complexité d'un problème algorithmique. C'est à dire :

> La complexité (maximale) d'un problème algorithmique est la complexité (maximale) du meilleur algorithme qui le résout.
{: .note}

Ce n'est pas une question facile car :

* il faut pouvoir définir clairement quel est le problème que l'on cherche à résoudre
* il faut pouvoir raisonner sur les complexités sans avoir d'algorithme à sa disposition

Cependant, si l'on possède déjà un algorithme pour résoudre le problème, sa complexité est une borne maximale de la complexité du problème qu'il résout. Enfin, il est souvent facile de se donner une borne minimale de la complexité du problème (même si l'on ne sait pas s'il existe un algorithme pour le résoudre), c'est la taille de la sortie de l'algorithme.

Nous illustrerons ici cette problématique avec l'exemple de la recherche d'un élément dans un tableau qui permet d'illustrer plusieurs facettes de ce qu'est un problème algorithmique.

## problème algorithmique

On supposera toujours ici qu'il existe un algorithme pour résoudre notre problème (la question de connaitre les problèmes que peuvent résoudre un algorithme sera traité dans la [partie théorie](({% link cours/theorie-pratiques-algorithmique/theorie/index.md %})) de ce cours).

### définition

> Un **problème algorithmique** est composé de 4 parties :
>
> * nom : le nom du problème
> * des données : les paramètres dont aura besoin l'algorithme
> * la question : ce que l'on cherche à résoudre
> * la réponse : la sortie de l'algorithme
>
{: .note}

Par exemple :

* nom : recherche
* données : une valeur et un tableau d'entiers
* question : valeur est-elle présente dans le tableau ?
* réponse : OUI ou NON

Ou, si l'on cherche l'indice de valeur dans le dans ce tableau :

* nom : recherche indice
* données : une valeur et un tableau d'entiers contenant valeur
* réponse : l'indice du tableau contenant valeur

On voit que la question peut-être omise si la réponse est spécifique.

### complexités

On pourra définir pour un problème donné :

> * une **borne minimale** de complexité du problème : tout algorithme qui le résout sera de complexité supérieure ou égale (mais on ne sais pas si un tel algorithme existe)
> * une **borne maximale** de complexité du problème : le meilleur algorithme sera de complexité plus faible ou égale (mais on ne sais pas si un tel algorithme existe)
>* la **complexité du problème** : la complexité maximale du meilleur algorithme permettant de résoudre le problème (cette complexité existe toujours puisqu'il existe un algorithme permettant de résoudre le problème et qu'il existe un [nombre dénombrable d'algorithmes]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#nombre-algorithmes))
>
{: .note}

## exemple : recherche d'un élément dans un tableau

On va chercher à résoudre le problème d'existence dans le tableau :

* nom : recherche
* données : une valeur et un tableau d'entiers
* question : valeur est-elle présente dans le tableau ?
* réponse : OUI ou NON

Ce qu'on peut déjà dire de notre problème :

* une borne minimale : $\mathcal{O}(1)$ puisque la taille la sortie est un booléen
* une borne maximale : $\mathcal{O}(n)$ où $n$ est la taille du tableau puisque l'on a un [algorithme qui résout le problème]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#exemple-recherche) :

```python
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

### complexité du problème "recherche"

Notre borne minimale de $\mathcal{O}(1)$ semble irréaliste. Supposons de façon plus générale qu'il existe un algorithme qui résout le problème en prenant strictement moins que $n$ opérations où $n$ est la taille du tableau, pour $n > N_0$.

Ceci signifie que pour $n$ assez grand, l'algorithme résout le problème en strictement moins que $n$ opérations : il n'a pas besoin de regarder toutes les cases du tableau pour répondre.

Soit alors un tableau $T$ de taille $n > N_0$ qui ne contient pas valeur. Notre algorithme va répondre NON à la question "est-ce que valeur est dans $T$" ? en strictement moins de $n$ opérations : il existe donc une case du tableau, disons $T[i^*]$, que l'algorithme n'a jamais regardé lors de son exécution : il ne sait pas ce que contient cette case.

De là, en exécutant l'algorithme avec valeur et le tableau $T'$ tel que :

* $T'[i] = T[i]$ si $i \neq i^*$
* $T'[i^*] = \mbox{valeur}$

La réponse à la question "est-ce que valeur est dans $T'$ ?" ne pourra être que la même réponse que la question "est-ce que valeur est dans $T$ ?", ce qui est faux. Notre algorithme ne peut exister : Un algorithme qui résout le problème de la recherche doit au moins être de complexité $\mathcal{O}(n)$

Attention, ça ne veut pas dire qu'il n'existe pas des instances où l'algorithme va plus vite (si valeur est le 1er élément du tableau par exemple), mais que pour certains tableau, on est obligé de vérifier toutes les cases (si valeur n'est pas dans tableau).

Au final on a :

* une borne minimale de la complexité de la recherche de $\mathcal{O}(n)$
* un algorithme qui résout le problème en $\mathcal{O}(n)$

Donc :

> La complexité du problème de la recherche est en $\mathcal{O}(n)$ où $n$ est la taille du tableau.
{: .note}

### cas particulier des tableaux ordonnés

Un cas particulier courant de recherche est le problème :

* nom : recherche ordonnée
* données : une valeur et un tableau d'entiers triés par ordre croissant
* question : valeur est-elle présente dans le tableau ?
* réponse : OUI ou NON

Le problème "recherche ordonnée" est un sous problème de "recherche", on a donc une borne maximale de $\mathcal{O}(n)$ (où $n$ est la taille du tableau) pour le résoudre puisqu'il il suffit d'utiliser l'algorithme `est_dans_tableau`. Cependant, on utilise souvent un autre algorithme : la recherche dichotomique.

#### algorithme de la recherche dichotomique

```python
def recherche_dichotomique(valeur, tableau_trie):
    debut = 0
    fin = len(tableau_trie) - 1

    while fin - debut >= 0:
        milieu = (fin + debut) // 2
        
        if tableau_trie[milieu] == valeur:
            return True
        elif tableau_trie[milieu] < valeur:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False
```

On a utilisé ici le fait que  `(fin + debut) // 2` va donner la valeur entière de `(fin + debut) / 2`.

1. l'algorithme se termine bien car `fin - debut` décroit strictement à chaque itération
2. on a l'invariant de boucle : si valeur est dans `tableau_trie`, alors sa position plus grande que `debut` et plus petite que `fin`
3. si l'on sort de la boucle l'invariant est toujours vérifié, mais comme `debut` > `fin`, valeur ne peut être dans `tableau_trie`

Les trois remarques ci-dessus prouvent que l'algorithme `recherche_dichotomique` résout bien le problème "recherche ordonnée".

Enfin, à chaque itération, `fin - debut` est divisé par 2 : il y a donc au plus $\log_2(n)$ itérations (avec $n$ la taille du tableau). Comme le reste des lignes est soit une affectation soit un positionnement dans un tableau, la complexité totale de l'algorithme est $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau).

> l'algorithme `recherche_dichotomique` résout le problème "recherche ordonnée" en $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau)
{: .note}

#### complexité du problème "recherche ordonnée"

L'algorithme de la recherche dichotomique résout le problème de la "recherche ordonnée" de façon bien plus efficace que l'algorithme `est_dans_tableau` : il n'a pas besoin de connaitre toutes les cases du tableau pour répondre à la question car le tableau est trié. Une borne maximum de la complexité du problème "recherche ordonnée" est alors $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau).

Nous allons montrer que l'on ne peut pas faire mieux en montrant que $\mathcal{O}(\ln(n))$ est une borne minimum de notre problème.

> Remarquez bien que la preuve que l'on a donné pour la complexité de "recherche" ne fonctionne pas dans le cas de "recherche ordonnée". On ne peut pas fabriquer de tableau $T'$ ici puisque $T'$ doit rester ordonné.

Commençons par remarquer que `valeur` peut se trouver à chaque position du tableau. Tout algorithme qui résout "recherche ordonnée" doit ainsi réussir à distinguer parmi $n + 1$ cas : `valeur` n'est pas dans tableau, `valeur` est à la position 0 du tableau, `valeur` est à la position 1 du tableau, ..., `valeur` est à la position $n-1$ du tableau.

En algorithmique, distinguer parmi plusieurs cas se fait par des tests :

* s'il y a 0 test, un algorithme ne peut résoudre qu'un seul cas
* s'il y a 1 test, un algorithme peut résoudre au plus 2 cas :
  * 1 cas si le test est vrai
  * 1 cas si le test est faux
* s'il y a 2 tests, un algorithme peut résoudre au plus $2 \cdot 2 = 4$ cas :
  * 1 cas si les deux tests sont vrai
  * 1 cas si le premier test est vrai et le second test faux
  * 1 cas si le premier test est faux et le second test vrai
  * 1 cas si les deux tests sont faux
* s'il y a 3 tests, un algorithme peut résoudre au plus $2 \cdot 2 \cdot 2 = 2^3 = 8$ cas :
  * 1 cas si les trois tests sont vrai
  * 1 cas si les deux premiers tests sont vrai et le troisième test faux
  * ...
  * 1 cas si les trois tests sont faux
* ...
* s'il y a $k$ tests, un algorithme peut résoudre au plus $2^k$ cas

Comme il y a $n+1$ cas au moins à traiter, notre algorithme devra posséder au moins $\log_2(n)$  tests : sa complexité ne peut-être inférieure à $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$ opérations.

En conclusion le problème de la "recherche ordonnée" pour un tableau à $n$ éléments :

* une borne minimale de complexité égal à $\mathcal{O}(\ln(n))$
* la complexité de l'algorithme `recherche_dichotomique` est en $\mathcal{O}(\ln(n))$

> La complexité du problème de la "recherche ordonnée" est en $\mathcal{O}(n)$ où $n$ est la taille du tableau.
{: .note}
