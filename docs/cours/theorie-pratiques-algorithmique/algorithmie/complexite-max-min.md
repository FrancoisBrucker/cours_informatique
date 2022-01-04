---
layout: page
title:  "Complexité max/min"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [complexité max/min]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %})
>
> prérequis :
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

Où l'on se donne des outils pour mesurer (théoriquement et en pratique) les performances d'un algorithmes

## mesures en $\mathcal{O}$

Mesurer les performances d'un algorithme se fera presque exclusivement en utilisant des $\mathcal{O}$ (*grand O*)

>Une fonction $f(N)$ est en $\mathcal{O}(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot f'(N)$ pour tout $N > N_0$.
{: .note}

Cela permet :

* d'avoir un majorant de notre mesure lorsque $N$ devient grand
* de ne pas s'occuper des constantes puisque (on va le démontrer) une fonction en $\mathcal{O}(\mbox{constante})$ est également en $\mathcal{O}(1)$
* de ne pas s'occuper de la proportionnalité car (on va le démontrer) une fonction en $\mathcal{O}(\mbox{constante} \cdot f(N))$ est également en $\mathcal{O}(f(N))$

> Connaitre le comportement en $\mathcal{O}$ d'une mesure dépendant de $N$ nous donne un majorant de son comportement lorsque $N$ devient grand. Si le majorant n'est pas trop éloigné de la mesure originale, cela nous donne une **idée générale** de la valeur de la mesure lorsque $N$ devient grand.
{: .note}

Ceci est plutôt intéressant en algorithmie car l'on ne connait pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer :

* le nombre d'opérations élémentaires effectuée par l'algorithme avant de s'arrêter
* le temps mis par l'algorithme pour s'exécuter
* la taille de la mémoire utilisée pour par l'algorithme

Par rapport à la taille $N$ de l'entrée de l'algorithme.

### arithmétique des $\mathcal{O}$

Par abus de langage, on notera :

* $\mathcal{O}(f(N))$ plutôt que soit $f'(N)$ une fonction en $\mathcal{O}(f(N))$
* $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Rightarrow \mathcal{O}(g(N))$ plutôt que "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(g(N))$ plutôt que "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$ et réciproquement"

> On a les règles suivantes :
>
> 1. $\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une contante strictement positive
> 2. $\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$
> 3. $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$
> 4. $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$
>
> Et en combinant les $\mathcal{O}$ pour $f$ et $g$ deux fonction positives :
>
> * $\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$
> * $\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$
>
{: .note}

> Démontrez ces propriétés.
{: .a-faire}

{% details  Démonstration de $\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une contante strictement positive %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot A$. En posant $c'_0 = c_0 \cdot A$, on a $f(N) < c'_0 \cdot 1$ pour tout $N > N_0$ donc $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) < c'_0 \cdot A$ pour tout $N > N_0$ donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

{% details  Démonstration de $\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$ %}

Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$.
Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p < c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$  et $p \leq q$ : $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

{% details  Démonstration de $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$ %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$. Si $f'(N) = \mathcal{O}(f(N) + g(N) + h(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) + g(N) + h(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 c_0 g(N) + c'_0 g(N) + c'_0 h(N)$ pour $N > \max \\{ N_0, N'_0 \\}$ ce qui implique $f'(N) < \max \\{ c'_0, c_0 \\}^2 (g(N) + h(N))$ pour $N > \max \\{ N_0, N'_0 \\}$ : $f'(N) = \mathcal{O}(g(N) + h(N))$

{% enddetails %}

{% details  Démonstration de $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$ %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$. Si $f'(N) = \mathcal{O}(f(N)\cdot g(N) \cdot h(N) + h'(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) \cdot g(N) \cdot h(N) + h'(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 (c_0 g(N) \cdot g(N) \cdot h(N) + h'(N)$ pour $N > \max \\{ N_0, N'_0 \\}$ ce qui implique $f'(N) < \max \\{ c'_0, c_0 \\}^2 (g(N)^2 \cdot  h(N) + h'(N))$ pour $N > \max \\{ N_0, N'_0 \\}$ : $f'(N) = \mathcal{O}((g(N))^2 \cdot h(N) + h'(N))$

{% enddetails %}

{% details  Démonstration de $\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$ %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) + g'(N) < \max \\{c_0, c'_0\\} (f(N) + g(N))$ pour $N > \max \\{ N_0, N'_0\\}$ : $f'(N) + g'(N) = \mathcal{O}(f(N) + g(N))$.

{% enddetails %}

{% details  Démonstration de $\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$ %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) \cdot g'(N) < \max \\{c_0, c'_0, 1 \\}^2 (f(N) \cdot g(N))$ pour $N > \max \\{ N_0, N'_0\\}$ car $f$ et $g$ sont positives : $f'(N) \cdot g'(N) = \mathcal{O}(f(N) \cdot g(N))$.

{% enddetails %}

### conséquences algorithmique

La règle (1) montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basique]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#instruction-basique) est constitué une opération, ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur par exemple. L'addition avec un x68 est faites [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86) par exemple, et donc l'addition nécessite 2 opération du processeur). Mais on pourra toujours montrer qu'il y en a un nombre constant (ou borné par un nombre constant) :

> La complexité d'une opération basique nécessite $\mathcal{O}(1)$ opérations.
{: .note}

De là :

> un nombre constant d'opérations basiques nécessite $\mathcal{O}(1)$ opérations.
{: .note}

Les règles précédentes permettent plus généralement de montrer :

> $\mathcal{O}(A \cdot f(N)) \Leftrightarrow A \cdot \mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(f(N))$, avec $A$ une contante strictement positive et $f(N)$ une fonction strictement positive pour $N > N_0$
{: .note}

Ceci est pratique, car cela permet de ne pas compter toutes les opérations basiques précisément. Ainsi, en reprenant l'exemple de la partie [complexité des pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#complexité) :

```text
x = 30
if ((x > 12) AND (y < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction, donc $\mathcal{O}(1)$ opérations.
2. un test avec 2 comparaisons et un `AND` : 3 instructions, donc $\mathcal{O}(3) = \mathcal{O}(1)$ opérations.
3. on affecte le résultat d'une opération élémentaire : 2 instructions, donc $\mathcal{O}(2) = \mathcal{O}(1)$ opérations.

Un nombre total d'instructions de $3 \mathcal{O}(1) = \mathcal{O}(1)$ opérations.

En revanche, faites attention, cela ne marque que pour les constantes !

> Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$. On ne peut pas simplifier les variables.
{: .attention}

Enfin, comme en algorithmie on manipulera souvent des polynômes, on peut montrer facilement avec les règles précédentes que :

> $$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n)$$
{: .note}

## complexité d'un algorithme

On l'a vu dans la partie [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#complexité), la complexité est le nombre d'opérations basiques effectuées par un algorithme. Le nombre d'opérations basiques effectué par un pseudo-code va être dépendant des entrées de celui-ci, même si les entrées ont la même taille (on verra des exemples de ça).

On distinguera trois types de complexités :

* nombre d'opérations basiques effectuées
* temps d'exécution d'un programme
* taille mémoire consommée pendant l'exécution

Les complexités vont toutes dépendre des entrées, plus précisément d'un paramètre rendant compte de leur **taille**, c'est à dire du nombre de cases mémoires nécessaires pour les stocker.

> Lorsque l'on donne des complexité c'est toujours en fonction d'un ou plusieurs paramètres qu'il **faut** expliciter
{: .attention}

### nombre d'opérations basiques

> La **complexité** (aussi parfois appelée **complexité maximale**) d'un algorithme est le **nombre maximum d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{: .note}

La **taille** d'une entrée est proportionnelle au nombre de cases mémoires que celle-ci nécessite.

> Lorsque vous entendrez parler de *complexité* d'un algorithme, ce sera par défaut **toujours** la complexité maximale.

Il arrive que certains algorithmes aient un comportement très différent selon les entrées. Parler seulement de la complexité (nombre maximum d'opérations) ne permet pas alors de le caractériser complètement. On parlera alors aussi de :

> La **complexité minimale** d'un algorithme est le **nombre minium d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{: .note}

Lorsque l'on calcule une complexité (maximale ou minimale) sous la forme d'un $\mathcal{O}(f(N))$, on tentera bien sur de trouver la fonction $f(N)$ la plus petite possible.

### temps d'exécution

Un moyen efficace de mesurer la complexité d'un algorithme écrit sous la forme d'un code exécutable est de mesurer le temps mis pour son exécution pour un jeu d'entrée donné.

> la **complexité en temps** d'un algorithme est le temps mis pour l'exécuter en utilisant un jeu de donné **pour lequel la complexité (max) est atteinte** et d'une taille totale donnée.
{: .note}

Le temps pris sera bien sur différent si l'on prend une machine plus puissante ou si l'on change le code de l'algorithme mais **l'évolution de la complexité en temps par rapport à la taille des données est toujours proportionnelle à la complexité**. Pour le voir, il suffit de mesurer la durée d'exécution de chaque instruction basique et de la borner par le max.

> Si vous ne prenez pas un jeu de donné pour lequel la complexité de l'algorithme est atteinte, vous ne mesurez **pas** la complexité temporelle de l'algorithme...
{: .attention}

### taille mémoire

> la **complexité en espace** d'un algorithme est le nombre maximum de cases mémoires utilisées pour l'exécuter en utilisant un jeu de donné de taille donnée.
{: .note}

Comme la complexité, on la mesurera avec des $\mathcal{O}$.

Notez que la complexité en espace n'est pas forcément atteinte pour un jeu de donné donnant la complexité de l'algorithme, mais **la complexité en espace sera toujours plus faible que la complexité** (visiter une case mémoire nécessitant une opération élémentaire).

### complexité de méthodes ou de structures

Lorsque l'on code un algorithme, on a coutume (et c'est très bien) d'utiliser des fonctions, des méthodes ou des structures que l'on a pas écrite. Il faut en revanche bien connaître leurs complexités pour ne pas commettre d'erreur de calcul.

> Lorsque l'on calcul une complexité toutes les méthodes et fonctions doivent être examinées
{: .note}

#### complexité de structure

En informatique, les **objets que l'on manipule ont des types**. On connait déjà des [objets basiques]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#objets-basique) que sont de types booléens, entiers, réels ou encore chaines de caractères pour les quels toutes les opérations que l'on peut effectuer avec eux sont en $\mathcal{O}(1)$. Ce n'est plus le cas lorsque l'on utilise des type plus complexes, composé de types basiques comme les conteneurs comme les tableaux, ou encore les listes de python. Pour pouvoir calculer la complexité d'un algorithme les utilisant, il faut connaitre les complexités de ses opérations. Souvent, les opérations suivantes suffisent :

> Pour chaque type de donnée, il faut connaitre la complexité de :
>
> * la création d'un objet de ce type
> * la suppression d'un objet de ce type
> * chaque méthode liée au type
>
{: .note}

Prenons le type [tableau](https://fr.wikipedia.org/wiki/Tableau_(structure_de_donn%C3%A9es)) comme exemple. Un tableau est un conteneur pouvant contenir $n$ objets (on appelle $n$ la taille d'un tableau). On peut accéder et affecter un objet au tableau grâce à un indice allant de $0$ à $n-1$ : si `t` est un tableau `t[i]` correspond à l'objet d'indice $i$ du tableau. Avec un tableau on peut :

* créer un tableau de taille $n$ en $\mathcal{O}(1)$ opérations
* supprimer un tableau est possible en $\mathcal{O}(1)$ opérations
* récupérer et affecter l'objet d'indice $i$ du tableau (objet `t[i]`) se fait en $\mathcal{O}(1)$ opérations
* pour augmenter la taille d'un tableau, il faut recréer un tableau vide avec la nouvelle taille puis recopier tous les éléments de l'ancien tableau au nouveau. Cela se fait donc en $\mathcal{O}(n)$ opérations où $n$ est la taille de l'ancien tableau.
* pour réduire la taille d'un tableau, il faut recréer un tableau vide avec la nouvelle taille puis recopier les éléments que l'on veut garder de l'ancien tableau au nouveau. Cela se fait en $\mathcal{O}(n)$ opérations où $n$ est la taille du nouveau tableau.

> De façon pratique, un tableau est un ensemble des $n$ cases mémoires continues. Ce qui fait qu'on peut donc facilement les réserver et les libérer en une fois et que à la case mémoire d'indice $i$ vaut `&t + i` où `&t` est le numéro de la case mémoire d'indice $0$ du tableau.

Le langage python ne connait pas les tableaux. Il utiliser le type **liste** à la place. Une liste peut être vue comme l'évolution du type tableau. On donne ici juste les complexités de cette structure pour que vous puissiez les utiliser dans vos programmes, nous ne les démontrerons pas :

* créer et supprimer une liste de taille $n$ en $\mathcal{O}(1)$ opérations
* récupérer et affecter l'objet d'indice $i$ d'une liste (objet `t[i]`) se fait en $\mathcal{O}(1)$ opérations
* pour augmenter la taille d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
* supprimer le dernier élément d'une liste se fait en $\mathcal{O}(1)$ opérations

Une liste peut être vue comme un tableau dont on peut augmenter ou diminuer la taille par la fin en $\mathcal{O}(1)$ opérations.

> Ne confondez pas liste et [liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e) ce n'est pas du tout la même structure !
{: .attention}

#### fonction et méthodes données

Il faut connaître les différentes complexités des méthodes et fonctions utilisées. Ne vous laissez pas méprendre. Ce n'est pas parce qu'elle font 1 seule ligne que leur complexité est en $\mathcal{O}(1)$. Par exemple la complexité de la méthode `max` de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Est de complexité $\mathcal{O}(n)$  où $n$ est la taille da liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

### exemple

Prenons par exemple l'algorithme écrit en python suivant :

```python
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

L'intérieur de la boucle est constitué du code :

```python
if x == valeur:
    return True
```

Qui est de complexité $\mathcal{O}(1)$. Ce code est exécuté autant de fois que l'on va rentrer dans la boucle for. La complexité de notre algorithme est alors égale à $k * \mathcal{O}(1)$ où $k$ est le nombre de fois où l'on rentre dans la boucle.

On cherche le cas le pire. Elle est atteinte lorsque la boucle for parcours tout le tableau, c'est à dire pour deux cas :

* l'élément recherché n'est pas dans le tableau
* l'élément recherché est le dernier élément du tableau

On en conclut que la complexité de notre algorithme est $n * \mathcal{O}(1)$ où $n$ est la taille du tableau qui est un paramètre d'entrée (c'est donc une variable qu'on ne peut faire disparaître) la complexité de notre algorithme est : $\mathcal{O}(n)$.

La complexité minimale est quant-à-elle atteinte lorsque l'on ne parcours pas notre boucle, c'est à dire lorsque la valeur recherchée est la 1ère valeure du tableau. Dans ce cas là, la complexité est de $\mathcal{O}(1)$ opérations.

Au final :

* la complexité maximale de l'algorithme `est_dans_tableau` est $\mathcal{O}(n)$
* la complexité minimale de l'algorithme `est_dans_tableau` est $\mathcal{O}(1)$

## types de complexité en algorithmie

En algorithmie, la plupart des complexités que l'on étudiera seront de cinq types (plus leurs combinaisons) :

> On appelle :
>
> * **complexité constante** une complexité en $\mathcal{O}(1)$
> * **complexité logarithmique** une complexité en $\mathcal{O}(\ln(n))$ où $n$ est le paramètre de taille de l'algorithme
> * **complexité linéaire** une complexité en $\mathcal{O}(n)$ où $n$ est le paramètre de taille de l'algorithme
> * **complexité polynomiale** une complexité en $\mathcal{O}(n^k)$ où $n$ est le paramètre de taille de l'algorithme et $k$ une constante
> * **complexité exponentielle** une complexité en $\mathcal{O}(k^n)$ où $n$ est le paramètre de taille de l'algorithme et $k$ une constante
>
{: .note}

Les type de complexité ci-dessus sont rangés par taille, de la moins longue à la plus longue. Remarquez qu'un algorithme de complexité linaire nécessite de lire toutes les données au plus un nombre constant de fois pour s'exécuter. Un algorithme de complexité logarithmique n'a même pas besoin de lire une fois toutes les données pour s'exécuter ! Ceci n'est souvent possible que si les données en entrées ont une structure très particulière. Par exemple pour le problème de la recherche du plus grand élément d'une liste :

* trouver le plus grand élément dans une liste non triée nécessite $\mathcal{O}(n)$ où $n$ est la taille de la liste,
* trouver le plus grand élément dans une liste triée nécessite $\mathcal{O}(1)$ où $n$ est la taille de la liste,

Ou le problème de la recherche d'un élément particulier de la liste :

* trouver un élément dans une liste non triée nécessite $\mathcal{O}(n)$ où $n$ est la taille de la liste,
* trouver un élément dans une liste triée nécessite $\mathcal{O}(\ln (n))$ où $n$ est la taille de la liste en utilisant la [recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique)

> Notez bien que la complexité logarithmique est la même quelque soit la base utilisée. En effet $\log_k(n) = \frac{\ln (n)}{\ln (k)}$ et donc $\mathcal{O}(\log_k(n)) = \mathcal{O}(\ln(n))$ pour toute base constante $k$.

Il est crucial de chercher la meilleure complexité pour un algorithme car ses performance seront drastiquement différentes selon le type de complexité qu'il possède, comme le montre les deux tableaux ci-dessous, repris du livre [Computer and intractabilityt](https://en.wikipedia.org/wiki/Computers_and_Intractability). Ce qu'il faut retenir :

> * il y a une **énorme différence** entre complexité linéaire et complexité polynomiale
> * il y a une **énorme différence** entre complexité polynomiale et complexité exponentielle (qu'il ne faut donc jamais avoir si possible)
{: .note}

### temps pour résoudre un problème de taille $n$

Exemple d'évolution du temps de calcul par rapport à la complexité. En supposant, que l'on ait un ordinateur qui résout des problèmes de complexité $n$ en 0.01 ms pour des données de taille 10, on peut remplir le tableau ci-après.

En colonnes le nombre $n$ de données, en lignes les complexités des algorithmes.

| complexité  |     10     |   20     |    30   |      40     |     50                   |       60                   |
|-------------|------------|----------|---------|-------------|--------------------------|----------------------------|
|   $\ln(n)$  |  2 $\mu s$ | 3 $\mu s$|3 $\mu s$|  4 $\mu s$  | 4 $\mu s$                | 4 $\mu s$                  |
|    $n$      |    0.01 ms | 0.02 ms  | 0.03 ms |  0.04 ms    | 0.05 ms                  | 0.06 ms                    |
|    $n^2$    |    0.1 ms  | 0.4 ms   | 0.9 ms  |  1.6 ms     | 2.5 ms                   | 3.6 ms                     |
|    $n^3$    |    1 ms    | 8 ms     | 27 ms   |  64 ms      | 125 ms                   | 216 ms                     |
|    $n^5$    |    1s      | 3.2 s    | 24.3 s  |  1.7 min    | 5.2 min                  | 13 min                     |
|    $2^n$    |    1 ms    | 1s       | 17.9 min|  12.7 jours | 35.7 ans                 | 36600 ans                  |
|    $3^n$    |    59 ms   | 58 min   | 6.5 ans |  385500 ans | $2.27\cdot 10^8$ siècles | $1.3\cdot 10^{13}$ siècles |

L'évolution est dramatique plus la complexité augmente. Pour une complexité logarithmique, le temps *semble* constant et pour une complexité polynomiale, la croissance reste maitrisée même s'il vaut mieux avoir une petite complexité pour traiter plus de données. Pour une complexité exponentielle ($2^n$ et $3^n$) en revanche, la durée est tout simplement rédhibitoire.

> Pour générer le tableau, on voit que le temps  $t$ pour exécuter 1 opération est de .001ms (on regarde la ligne de complexité linéaire : pour $n=10$ on prend 0.01 opérations, donc 1 opération nécessite $0.01/10ms$). Le temps pris pour exécuter $f(n)$ opérations avec une entrée de taille de $n$ est alors : $t \cdot f(n)$

### nombre de problèmes résolus par heure

En colonne la rapidité de la machine, en ligne la taille maximale d'un problème que l'on peut résoudre en 1heure.

| complexité | machine actuelle | 100x plus rapide | 1000x plus rapide |
|------------|------------------|------------------|-------------------|
|  $\ln(n)$  |        $N0$      |$e^{100} \cdot N0$|$e^{1000} \cdot N0$|
|    $n$     |        $N1$      |  $100 \cdot N1$  |  $1000 \cdot N1$  |
|    $n^2$   |        $N2$      |  $10 \cdot N2$   |  $31.6 \cdot N2$  |
|    $n^3$   |        $N3$      |  $4.64 \cdot N3$ |  $10 \cdot N3$    |
|    $n^5$   |        $N4$      |  $2.5 \cdot N4$  |   $3.98 \cdot N4$ |
|    $2^n$   |        $N5$      |    $N5 + 6.64$   |   $N5 + 9.97$     |
|    $3^n$   |        $N6$      |    $N6 + 4.19$   |   $N6 + 6.29$     |

La encore, l'évolution est dramatique plus la complexité augmente. Pour des complexités logarithmiques et polynomiales le nombre de problème augmente d'un facteur multiplicatif lorsque la vitesse augmente, mais ce n'est pas le cas pour des complexités exponentielles. Pour ces problèmes, augmenter la vitesse de la machine ne change pas fondamentalement le nombre de problèmes que l'on peut résoudre.

> Pour générer le tableau, on suppose que l'on peut résoudre $K$ opérations en 1 heure. On cherche alors $n$ tel que $f(n)$ soit égal à $K$ et donc $n = f^{-1}(K)$. En remarquant que $K$ est égal à la taille maximale d'un problème de complexité linéaire résoluble en 1heure, on la taille maximale $n$ d'un problème de complexité $f(n)$ résoluble en 1 heure pour une machine allant $k$ fois pus vite qu'une machine actuelle vaut $f^{-1}(k \cdot N1)$.

### le cas particulier de $n!$

Souvent les étudiants veulent que leurs algorithmes soient en $\mathcal{O}(n!)$. Ce n'est **presque jamais exact** ! En effet, la [formule de sirling](https://fr.wikipedia.org/wiki/Formule_de_Stirling) donne l'équivalent suivant pour $n!$ :

$$
n! \sim \sqrt{2\pi n}(\frac{n}{e})^n
$$

On a donc que $n!$ est de l'ordre de $\mathcal{O}(n^{n+1/2})$, qui est vachement plus grand que $\mathcal{O}(2^{n})$ qui est déjà gigantesque.

>Si vous pensez que votre algorithme tout bête est en $\mathcal{O}(n!)$. Réfléchissez-y à deux fois. C'est presque sûrement une erreur...
{: .note}

## règles de calcul de complexité

On va donner ici quelques règles de calcul de complexité pour que vous puissiez estimer rapidement la complexité d'un algorithme simple.

### une boucle simple

Lorsque l'on a une boucle où le nombre de fois où l'on va rentrer dedans est évident.

Par exemple :

```text

tant que condition:
    bloc d'instructions

```

> La complexité est : $\mathcal{O}$(nombre de fois ou la condition est remplie) * ($\mathcal{O}$(complexité du bloc d'instruction) + $\mathcal{O}$(complexité de la vérification de la condition))
{: .note}

Souvent, $\mathcal{O}$(complexité de la vérification de la condition) sera égal à $\mathcal{O}(1)$ et pourra ne pas en tenir compte dans le calcul. C'est le cas, entre autre pour une boucle tant que :

```text

pour chaque element de structure:
    bloc d'instructions

```

> La complexité est : $\mathcal{O}$(nombre d'éléments de la structure) * $\mathcal{O}$(complexité du bloc d'instruction)
{: .note}

Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$, on pourra ne pas en tenir compte dans le calcul et la complexité est alors égale à la taille de la structure.

En conclusion :

> Si le bloc d'instruction est une suite d'instructions de complexité $\mathcal{O}(1)$ et que la vérification de la fin de la boucle est $\mathcal{O}(1)$, la complexité de la boucle est égal au nombre de fois où l'on effectue la boucle
{: .note}

### boucles imbriquées indépendantes

Plusieurs boucles imbriquées dont dont le nombre de fois où l'on va rentrer dedans est indépendant des autres boucles. Par exemple :

```text
boucle 1 éxecutée n1 fois:
    boucle 2 éxecutée n2 fois:
        ...
            boucle i éxecutée ni fois:
                bloc d'instructions
```

On peut utiliser la règle précédente de façon récursive, la partie $\mathcal{O}$(complexité du bloc d'instruction) contenant elle même une ou plusieurs boucles. 

> Si la condition à remplir pour rentrer dans la boucle est en $\mathcal{O}(1)$, la complexité des boucles imbriquées est le produit du nombre de fois où l'on rentre dans chaque boucle pris indépendamment multiplié par la complexité du bloc d'instructions.
{: .note}

Exemple :

```python
total=0
de i=1 à n-1 faire:
    de j=1 à n faire :
        total=total+1
Rendre total
```

La boucle en $i$ est exécuté $n-1$ fois ($i$ va de 1 à $n-1$), donc $\mathcal{O}(n)$ fois. La boucle en $j$ va également être exécutée $\mathcal{O}(n)$ fois indépendamment de la boucle en $i$. Enfin la complexité du bloc d'instruction est $\mathcal{O}(1)$, la complexité totale des deux boucles imbriquées vaut :

$${
\underbrace{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbrace{\mathcal{O}(n)}_{\mbox{boucle en j}} \cdot \underbrace{\mathcal{O}(1)}_{\mbox{bloc d'instructions}}
} = \mathcal{O}(n^2)$$

> Ne comptez pas trop précisément le nombre de fois où l'on rentre dans une boucle $n-3$ exécution de la boucle pouvant être avantageusement remplacé par $\mathcal{O}(n)$

### boucles dépendantes mais monotones

Il arrive souvent que les boucles imbriquées d'un algorithme soient dépendantes les unes des autres. Dans le cas général on ne peut pas factoriser le calcul de la complexité et il faut alors dérouler tout l'algorithme en additionnant les complexités de chaque ligne comme s'il n'y avait pas de boucles.

Il existe cependant un cas pratique (et qui arrive assez souvent) où l'on peut factoriser :

> Si une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (respectivement décroissante), on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois de l'ordre du maximum de fois.
{: .note}

On va vérifier cela avec un exemple :

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight text linenos %}

total=0
de i=1 à n-1 faire :
    de j=i+1 à n faire :
        total=total+1
Rendre total

{% endhighlight %}

Le nombre de fois où la boucle en $j$ est exécutée est un nombre variable de fois qui dépend de la valeur de $i$. Comme $i$ va croitre, le nombre de fois où cette boucle va s'exécuter va décroitre. Si l'on applique la règle  on peut dire qu'elle va s'exécuter de l'ordre de $\mathcal{O}(n)$ fois comme dans l'exemple de la partie précédente. La complexité de l'algorithme est donc de $\mathcal{O}(n^2)$.

Refaisons le calcul en décomposant toutes les instructions, comme on le ferait dans le cas général, pour voir que notre règle est valide (et donnera aussi une idée de la preuve de cette règle) :

* ligne 1 : $\mathcal{O}(1)$
* itération pour $i=1$:
  * une affectation $i=1$ : $\mathcal{O}(1)$
  * boucle pour $j=1$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $n-1$ fois
* itération pour $i=2$:
  * une affectation $i=2$ : $\mathcal{O}(1)$
  * boucle pour $j=2$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $n-2$ fois
* ...
* itération pour $i=n-1$:
  * une affectation $i=n-1$ : $\mathcal{O}(1)$
  * boucle pour $j=n-1$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $1$ fois
* ligne 5 : $\mathcal{O}(1)$

Notre complexité totale est donc :

$$
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    (\mathcal{O}(1) + (n-2) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    \dots\\
 + (\mathcal{O}(1) + (1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) \\
 + \mathcal{O}(1)
\end{aligned}
$$

comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a :

$$
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot \mathcal{O}(1)) + \\
    (\mathcal{O}(1) + (n-2) \cdot \mathcal{O}(1)) + \\
    \dots\\
 + (\mathcal{O}(1) + 1 \cdot \mathcal{O}(1)) \\
 + \mathcal{O}(1)
\end{aligned}
$$

Ce qui donne :

$$
\begin{aligned}
    \mathcal{O}(1) + \\
    n \cdot \mathcal{O}(1) + \\
    (n-1) \cdot \mathcal{O}(1) + \\
    \dots\\
 + \mathcal{O}(1)
\end{aligned}
$$

et donc notre complexité vaut :
$$\mathcal{O}(1) + \sum_{1\leq i \leq n} i \cdot \mathcal{O}(1)$$

Comme la somme des n premiers entiers vaut $\frac{(n+1)(n)}{2}$ notre complexité devient :

$$\mathcal{O}(1) + \frac{(n+1)(n)}{2} \mathcal{O}(1)$$

Ce qui est de l'ordre de : $\mathcal{O}(\frac{(n+1)(n)}{2})$. Or :

$$\mathcal{O}(\frac{(n+1)(n)}{2}) = \mathcal{O}(\frac{n^n + n}{2}) = \mathcal{O}(n^2 +n) = \mathcal{O}(n^2)$$

On retrouve bien le résultat attendu.

### complexité d'algorithmes récursifs

Un algorithme récursif est un algorithme qui s'appelle lui-même jusqu'à ce qu'on arrive à une condition d'arrêt qui stope la récursion. On en calcul la complexité en posant une équation qu'il faut résoudre :

> Pour calculer la complexité d'un algorithme récursif en fonction de la taille $n$ de l'entrée, on pose que $C(n)$ est la complexité et l'on utilise cette fonction pour estimer la complexité des appels récursifs. Une fois les complexités des éléments d'arrêts estimés, trouver $C(n)$ revient à résoudre une équation de récurrence.
{: .note}

Pour ilustrer ce calcul, prenons l'exemple suivant :

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight text linenos %}

fonction maximum(t, n):
    si n == 1
        rendre t[0]
    sinon:
        x = maximum(t, n-1)
        si x > t[n-1]:
            rendre x
        sinon:
            rendre t[n-1]

{% endhighlight %}

On exécute cette fonction avec comme paramètres initiaux un tableau nommé `t` de taille `n`. On vérifie qu'avec ces paramètres initaux :

1. l'algorithme converge bien
2. il rend bien le maximum de `t`

La taille des données est de l'ordre de la taille du tableau, c'est à dire le paramètre $n$. On pose alors que la complexité de notre algorithme pour un tableau de taille $n$ est : $C(n)$. De là :

* la complexité de la ligne 2 est en $\mathcal{O}(1)$ : c'est une comparaison
* la complexité de la ligne 3 est en $\mathcal{O}(1)$ : on cheche un élément particulier d'un tableau
* la complexité de la ligne 5 est en $C(n-1) + \mathcal{O}(1)$ : on exécute notre algorithme avec un tableau de taille $n-1$ — sa complexité est donc par définition de $C(n-1)$ — puis on affecte le résultat à une variable
* la complexité de la ligne 6 est en $\mathcal{O}(1)$ : c'est une comparaison d'une varaible et d'un élément particulier d'un tableau
* la complexité de la ligne 7 est en $\mathcal{O}(1)$
* la complexité de la ligne 9 est en $\mathcal{O}(1)$ : on rend un élément particulier d'un tableau

La complexité est définie par l'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$. Notre condition d'arrêt est obtenue pour `n` valant 1 et dans ce cas on a $C(1) = \mathcal{O}(1)$

Trouver $C(n)$ revient à résoudre :

$$
\left\{
    \begin{array}{lcl}
        C(n) & = & \mathcal{O}(1) + C(n-1)\\
        C(0) & = & \mathcal{O}(1)
    \end{array}
\right.
$$

On a alors :

$$
\begin{array}{lcl}
    C(n) & = & \mathcal{O}(1) + C(n-1)\\
    & = & \mathcal{O}(1) + \mathcal{O}(1) + C(n-2) = 2 \cdot \mathcal{O}(1) + C(n-2)\\
    & = & 3 \cdot \mathcal{O}(1) + C(n-3) \\
    & = & \dots \\
    & = & i \cdot \mathcal{O}(1) + C(n-i) \\
    & = & \dots \\
    & = & (n-1) \cdot \mathcal{O}(1) + C(1) = (n-1) \cdot \mathcal{O}(1) + \mathcal{O}(1) \\
    & = & n \cdot \mathcal{O}(1) = \mathcal{O}(n) \\
\end{array}
$$

Au fnal, on trouve que la complexité $C(n)$ de notre algorithme est en $\mathcal{O}(n)$ où $n$ est la taille du tableau placé initialement en paramètre.