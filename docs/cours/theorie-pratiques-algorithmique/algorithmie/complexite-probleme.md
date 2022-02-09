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
> * **nom** : le nom du problème
> * **données** : les paramètres dont aura besoin l'algorithme
> * **question** : ce que l'on cherche à résoudre
> * **réponse** : la sortie de l'algorithme
>
{: .note}

Par exemple :

* **nom** : recherche
* **données** : une valeur et un tableau d'entiers
* **question** : valeur est-elle présente dans le tableau ?
* **réponse** : OUI ou NON

Ou, si l'on cherche l'indice de valeur dans ce tableau :

* **nom** : recherche indice
* **données** : une valeur et un tableau d'entiers contenant valeur
* **réponse** : l'indice du tableau contenant valeur

La question peut-être omise si la réponse est spécifique.

### complexités

On pourra définir pour un problème donné :

> * une **borne minimale** de complexité du problème : tout algorithme qui le résout sera de complexité supérieure ou égale (mais on ne sait pas si un tel algorithme existe)
> * une **borne maximale** de complexité du problème : le meilleur algorithme sera de complexité plus faible ou égale (mais on ne sait pas si un tel algorithme existe)
>* la **complexité du problème** : la complexité maximale du meilleur algorithme permettant de résoudre le problème (cette complexité existe toujours puisqu'il existe un algorithme permettant de résoudre le problème et qu'il existe un [nombre dénombrable d'algorithmes]({% link cours/theorie-pratiques-algorithmique/theorie/fonctions.md %}#nombre-algos))
>
{: .note}

## exemple : recherche d'un élément dans un tableau

On va chercher à résoudre le problème d'existence dans le tableau :

* **nom** : recherche
* **données** : une valeur et un tableau d'entiers
* **question** : valeur est-elle présente dans le tableau ?
* **réponse** : OUI ou NON

Ce qu'on peut déjà dire de notre problème :

* une **borne minimale** : $\mathcal{O}(1)$ puisque la taille la sortie est un booléen
* une **borne maximale** : $\mathcal{O}(n)$ où $n$ est la taille du tableau puisque l'algorithme ci-dessous (qu'on [a déjà vu]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#exemple-recherche) résout le problème

```python
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

### complexité du problème "recherche" {#complexite-recherche}

Notre borne minimale de $\mathcal{O}(1)$ semble irréaliste. Supposons de façon plus générale qu'il existe un algorithme qui résout le problème en prenant strictement moins que $n$ opérations où $n$ est la taille du tableau, pour $n > N_0$.

Ceci signifie que pour $n$ assez grand, l'algorithme résout le problème en strictement moins que $n$ opérations : il n'a pas besoin de regarder toutes les cases du tableau pour répondre.

Soit alors un tableau $T$ de taille $n > N_0$ qui ne contient pas `valeur`. Notre algorithme va répondre NON à la question "est-ce que valeur est dans $T$" ? en strictement moins de $n$ opérations. Il existe donc une case du tableau, disons $T[i^\star]$, que l'algorithme n'a jamais regardé lors de son exécution : il ne sait pas ce que contient cette case.

On crée alors un tableau $T'$ de $n$ cases tel que :

* $T'[i] = T[i]$ si $i \neq i^\star$
* $T'[i^\star] = \mbox{valeur}$

Comme $T$ et $T'$ sont identiques sauf pour la case d'indice $i^\star$,
si l'algorithme ne regarde pas la case $T[i^\star]$ lors de son exécution pour $T$, il ne regardera pas non plus la case $T'[i^\star]$ lors de son exécution pour $T'$. Il ne pourra donc répondre que la même chose pour $T$ et $T'$, ce qui est impossible puisque la réponse est NON pour $T$ et OUI pour $T'$.

Notre hypothèse était fausse : un algorithme qui résout le problème de la recherche doit accéder au moins une fois à toutes les cases du tableau, il doit au moins être de complexité $\mathcal{O}(n)$.

Attention, ça ne veut pas dire qu'il n'existe pas des instances où l'algorithme va plus vite (si valeur est le 1er élément du tableau par exemple), mais que pour toute taille $n$ du tableau, il existe des tableaux pour lesquels on est obligé de vérifier toutes les cases (si valeur n'est pas dans tableau).

Au final on a :

* une borne minimale de la complexité de la recherche de $\mathcal{O}(n)$
* un algorithme qui résout le problème en $\mathcal{O}(n)$

Donc :

> La complexité du problème de la recherche est en $\mathcal{O}(n)$ où $n$ est la taille du tableau.
{: .note}

On peut en déduire une règle générale de la complexité d'un problème :

> Si les données n'ont pas de structure particulière, très souvent, la complexité d'un problème est au moins égal à la taille de ses données.
{: .note}

Si ce n'est pas vrai, c'est que très souvent notre problème est mal posé et qu'on peut se passer de certaines entrées.

### cas particulier des tableaux ordonnés

Un cas particulier courant de recherche est le problème :

* nom : recherche ordonnée
* données : une valeur et un tableau d'entiers triés par ordre croissant
* question : valeur est-elle présente dans le tableau ?
* réponse : OUI ou NON

Le problème "recherche ordonnée" est un sous problème de "recherche", on a donc une borne maximale de $\mathcal{O}(n)$ (où $n$ est la taille du tableau) pour le résoudre puisqu'il suffit d'utiliser l'algorithme `est_dans_tableau`. Cependant, on utilise souvent un autre algorithme : la recherche dichotomique.

#### algorithme de la recherche dichotomique

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
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

{% endhighlight %}

> Lorsque l'on code la recherche dichotomique, il faut faire **très** attention à ce que l'on prend comme milieu et comme condition d'arrêt. Sans quoi votre algorithme risque de tourner indéfiniment.
>
> On a utilisé ici le fait que  `(fin + debut) // 2` va donner la valeur entière de `(fin + debut) / 2`.
{: .attention}

[Etude]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %}#étude) de l'algorithme :

* **fonctionnement**. On vérifie que pour :
  * un tableau `[1, 3, 7]` l'algorithme trouve bien `7` et ne trouve pas `8`
  * un tableau `[1, 3, 3, 7]` l'algorithme trouve bien `7` et ne trouve pas `9`
* **preuve** :
  * **finitude**. La quantité entière `fin - debut` **décroit strictement** à chaque itération, elle sera donc strictement négative après un nombre fini d'opération.
  * **preuve**.
    1. on montre trivialement l'invariant de boucle suivant: si valeur est dans `tableau_trie`, alors sa position est plus grande que `debut` et plus petite que `fin`
    2. si l'on sort de la boucle l'invariant est toujours vérifié mais comme `debut` > `fin`, valeur ne peut être dans `tableau_trie`

Les remarques ci-dessus prouvent que l'algorithme `recherche_dichotomique` résout bien le problème "recherche ordonnée".

Etudions sa complexité. Ligne à ligne :

1. initiation de la fonction $\mathcal{O}(1)$
2. affection : $\mathcal{O}(1)$
3. affection : $\mathcal{O}(1)$
4. 
5. boucle de $k$ itérations
6. affection : $\mathcal{O}(1)$
7. 
8. test d'une valeur dans un tableau : $\mathcal{O}(1)$
9. retour de fonction : $\mathcal{O}(1)$
10. test d'une valeur dans un tableau : $\mathcal{O}(1)$
11. addition plus une affectation : $\mathcal{O}(1)$
12. 
13. soustraction plus une affectation : $\mathcal{O}(1)$
14. retour de fonction : $\mathcal{O}(1)$

Ce qui donne comme complexité :

$$
\begin{array}{lcl}
C(n) & = & 3 \cdot \mathcal{O}(1) + \\
& & k \cdot (6 \cdot \mathcal{O}(1)) + \\
& & \mathcal{O}(1) \\
& = & \mathcal{O}(k)
\end{array}
$$

Comme à chaque itération, `fin - debut` est divisé par 2 : il y a donc au plus $\log_2(n)$ itérations (avec $n$ la taille du tableau) :

> l'algorithme `recherche_dichotomique` résout le problème "recherche ordonnée" en $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau)
{: .note}

#### complexité du problème "recherche ordonnée" {#complexite-recherche-ordonnee}

L'algorithme de la recherche dichotomique résout le problème de la "recherche ordonnée" de façon bien plus efficace que l'algorithme `est_dans_tableau` : il n'a pas besoin de connaitre toutes les cases du tableau pour répondre à la question car le tableau est trié. Une borne maximum de la complexité du problème "recherche ordonnée" est alors $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau).

Nous allons montrer que l'on ne peut pas faire mieux en montrant que $\mathcal{O}(\ln(n))$ est une borne minimum de notre problème.

> Remarquez bien que la preuve que l'on a donné pour la complexité de "recherche" ne fonctionne pas dans le cas de "recherche ordonnée". On ne peut pas fabriquer comme précédemment de tableau $T'$ car les tableaux doivent être ordonnés.

Commençons par remarquer que `valeur` peut se trouver à chaque position du tableau. Tout algorithme qui résout "recherche ordonnée" doit ainsi réussir à distinguer parmi $n + 1$ cas :

* soit `valeur` n'est pas dans tableau
* soit `valeur` est à l'indice 0 du tableau
* soit `valeur` est à l'indice 1 du tableau
* ...
* soit `valeur` est à l'indice $n-1$ du tableau

En algorithmie, distinguer parmi plusieurs cas se fait par des tests (on utilise les opérations `si alors sinon`). De là :

* s'il y a 0 test, un algorithme ne peut pas distinguer de cas.
* s'il y a 1 test, un algorithme peut distinguer au plus  2 cas :
  * 1 cas si le test est vrai
  * 1 cas si le test est faux
* s'il y a 2 tests, un algorithme peut distinguer au plus $2 \cdot 2 = 4$ cas :
  * 1 cas si les deux tests sont vrai
  * 1 cas si le premier test est vrai et le second test faux
  * 1 cas si le premier test est faux et le second test vrai
  * 1 cas si les deux tests sont faux
* s'il y a 3 tests, un algorithme peut distinguer au plus $2 \cdot 2 \cdot 2 = 2^3 = 8$ cas :
  * 1 cas si les trois tests sont vrai
  * 1 cas si les deux premiers tests sont vrai et le troisième test faux
  * ...
  * 1 cas si les trois tests sont faux
* ...
* s'il y a $k$ tests, un algorithme peut distinguer au plus $2^k$ cas

On a alors la proprité suivante :

> Si un algorithme doit distinguer parmi $n$ cas, il devra posséder au moins $\log_2(n)$ tests. Sa complexité sera ainsi supérieure à $\mathcal{O}(\ln(n))$
{: .note}

Comme il y a $n+1$ cas au moins à traiter, notre algorithme sera de complexité supérieure à à $\mathcal{O}(\ln(n + 1)) = \mathcal{O}(\ln(n))$ opérations.

Au final, le problème de la "recherche ordonnée" pour un tableau à $n$ éléments :

* une borne minimale de complexité égal à $\mathcal{O}(\ln(n))$
* la complexité de l'algorithme `recherche_dichotomique` est en $\mathcal{O}(\ln(n))$

> La complexité du problème de la "recherche ordonnée" est en $\mathcal{O}(n)$ où $n$ est la taille du tableau.
{: .note}
