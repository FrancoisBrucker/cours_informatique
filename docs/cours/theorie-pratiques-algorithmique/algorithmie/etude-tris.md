---
layout: page
title:  "étude / algorithmes de tris"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude : trier un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %})
>
> prérequis :
>
>* [complexité moyenne]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-moyenne.md %})
>* [complexité d'un problème]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %})
>
{: .chemin}

Les informaticiens adorent les [algorithmes de tris]. Pas parce qu'ils aime l'ordre — loin de là — mais parce qu'il existe des zillions de façons de trier. Commençons par définir le problème :

>
> * nom : tri d'un tableau
> * des données : un tableau d'entiers
> * la réponse : un tableau contenant les valeurs du tableau en entrée triées selon l'ordre croissant
>
{: .note}

Nous allons voir trois catégories de tris


## tris simple

### tri par sélection

En entrée, un tableau `tab` remplit de nombre et de taille $n$ :

```python
def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

```

#### preuve que sélection trie

Il y a 2 boucles imbriquées. La raison d'être de la boucle faisant varier j est de faire en sorte que `min_index` soit l'indice de de la plus petite valeur du tableau pour les indices plus grand que $i$.

Ensuite on échange cette valeur avec celle initialement à l'indice $i$.

Notre invariant de boucle peut donc être : _"à la fin de chaque étape $i$ de l'algorithme les $i$ plus petites valeurs du tableaux sont triées aux $i$ premiers indices du tableau"_

#### complexités du tri par sélection

deux boucles imbriquées :

* la boucle extérieure est en $\mathcal{O}(n)$
* la boucle intérieure est d'itérations variables mais décroissantes de $n$ à 1 itérations : on utilise la règle qui dit que globalement, sa complexité est donc en nombre d'itérations max : $\mathcal{O}(n)$.

L'échange étant en $\mathcal{O}(1)$ la complexité totales est en $\mathcal{O}(n) * \mathcal{O}(n) = \mathcal{O}(^2)$.

Le nombre d'itérations n'est pas dépendant du tableau.

### tri par insertion

en entrée, un tableau `tab` remplit de nombre et de taille $n$.

```python
def insertion(tab):
    for i in range(1, len(tab)):
        actu = tab[i]
        j = i
        while j > 0 and tab[j - 1] > actu:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = actu
```

#### preuve qu'insertion trie

A chaque itération $i$ l'algorithme remonte la valeur initialement en position $i$ à la première position pour laquelle il est plus grand que le précédent. Remarquez bien que nous n'avons jamais changé les différentes valeurs du tableau.

Notre invariant de boucle peut donc être : _"à la fin de l'itération i, les i premiers éléments du tableau sont triés"_

#### complexités du tri par insertions

La complexité va changer selon la nature du tableau :

* si le tableau est déjà trié : je ne rentre jamais dans la boucle du *tant que* : la complexité est en $\mathcal{O}(n)$
* si le tableau est trié à l'envers : on effectue à chaque itération $i$, $i$ étapes dans la boucle du *tant que* : la complexité est en $\mathcal{O}(n^2)$

Ceci est problématique. La complexité (le cas le pire) arrive-t-elle souvent ou pas pour des données "normales" ?

Pour le savoir, on calcule la complexité en moyenne de notre algorithme. La complexité en moyenne dépend d'un modèle de donnée.

Par exemple, pour un modèle de données où nos données sont toujours tries ou juste quelques inversions : la complexité en moyenne va être $\mathcal{O}(n)$.

Souvent, pour la complexité en moyenne on considère des données aléatoires. C'est à dire que tout peut se passer de façon équiprobable : dans notre cas, au doigt mouillé, ça veut dire que notre boucle tant que va tout le temps remonter de la moitié de ce qui est possible (donc $i /2$ opérations) : pour un élément donné (aléatoire) il y a autant de nombre plus petit que lui que de nombre plus grand.

En moyenne, la boucle *tant que* effectue donc un nombre d'itérations égal à $i /2$ : ça croit de 1 à $n/2$ : elle est donc de complexité $\mathcal{O}(n)$. Au final, la complexité moyenne de l'algorithme est donc en $\mathcal{O}(n^2)$

Pour notre algorithme cela veut dire que le cas le meilleur arrive très rarement par rapport au cas le pire (parmi les $n!$ ordres possible, il y en a très peut qui sont presque triés).

> **Remarque** : Vous allez le prouver expérimentalement pendant la session de code.

### différence de traitement des données ?

Chaque tri a une façon bien à lui de trier les objets. C'est pour ça qu'un informaticien aime les tris : il a plein de façon différente de faire.

On va le *voir*.

On dessine le tableau à chaque modification de celui-ci. On voit la différence de traitement des algorithmes de tris.

Exemple pour le tri par insertion/sélection. On a tout mis dans un unique fichier *"main.py"* :

```python
import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    plt.cla()  # on efface le dessin 
    plt.plot(tab, 'ro')
    plt.pause(0.1) # on pause le dessin
    


def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        draw_tab(tab)


def insertion(tab):
    for i in range(1, len(tab)):
        actu = tab[i]
        j = i
        while j > 0 and tab[j - 1] > actu:
            tab[j] = tab[j - 1]
            draw_tab(tab)
            j -= 1
        tab[j] = actu
        draw_tab(tab)


tab = list(range(30))
random.shuffle(tab)

print(tab)
plt.plot(tab, 'ro')
# selection(tab)
insertion(tab)
plt.show()

print(tab)
```

## tri rapide {#tri-rapide}

Le tri rapide est une méthode de tri d'une liste à $n$ éléments dont :

* la complexité (maximale) est $\mathcal{O}(n^2)$,
* la complexité en moyenne est $\mathcal{O}(n\ln_2 (n))$,
* la complexité minimale est $\mathcal{O}(n\ln_2 (n))$,

```python
def rapide(tab):
    if len(tab) <= 1:
        return tab

    pivot = tab[0]

    tab_gauche = [tab[i] for i in range(1, len(tab)) if tab[i] <= pivot]
    tab_droite = [tab[i] for i in range(1, len(tab)) if tab[i] > pivot]

    return rapide(tab_gauche) + [pivot] + rapide(tab_droite)
```

On utilise les [list comprehension](https://python.doctor/page-comprehension-list-listes-python-cours-debutants) de python. C'est un moyen clair et efficace de générer des listes.

### preuve du tri rapide

* `tab_gauche` contient tous les élements du tableau d'indice `> 0` et plus petit ou égal à `pivot` qui est égal à `tab[0]`
* `tab_droite` contient tous les élements du tableau d'indice `> 0` et plus plus grand strictement à `pivot`
 
Si rapide fonctionne pour des tableaux de longeurs strictement plus petit que $n$, il fonctionne également pour des tableaux de longueur $n$ : le tableau rendu est le tableau des valeurs plus petite que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurence) + `[pivot]` + le tableau des valeurs plus grande que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurence)

On il fonctionne pour des tableau de longueur 0 ou 1, donc par récurrence, c'est ok.

### complexités du tri rapide

Nous n'allons pas faire ici de calcul rigoureux. Si ça vous intéresse, reportez vous là : <http://perso.eleves.ens-rennes.fr/~mruffini/Files/Other/rapide.pdf>

En notant $n$ la taille de la liste on a comme équation de récurrence pour la complexité $C(n)$ :

$$C(n) = \mathcal{O}(n) + C(n_1) + C(n_2)$$

Où $n_1$ est la taille du tableau de gauche et $n_2$ celle de droite ($n_1 + n_2 = n$)

On voit que la complexité du tri rapide tient dans le nombre de récursions qui est fait.

#### complexité (maximale) du tri rapide

Un tableau de n-1 case et l'autre tout petit. Ca arrive pour des tableaux déjà triés. La complexité est alors de :

$$C(n) = \mathcal{O}(n) + C(n-1)$$

Donc $C(n) = \mathcal{O}(n) + \dots + \mathcal{O}(n)$ où l'on additionne $n$ fois $\mathcal{O}(n)$ : la complexité est de $C(n) = \mathcal{O}(n^2)$.

**Attention** : on additionne $n$ fois $\mathcal{O}(n)$. Comme $n$ n'est pas une constante, il **FAUT** le rentrer dans le $\mathcal{O}$.

#### complexité en moyenne du tri rapide

On coupe toujours le tableau en 2 parties égales. Si les nombres sont répartiés aléatoirement, il n'y a en effet aucune raison que notre pivot sot le plus petit ou le plus grand. Intuitivement, la plus grande probabilité est qu'il soit environ plus grand que la moitié des valeurs restantes et plus petit que l'autre moitié.

Si l'on coupe toujours au milieu on a alors : 

$$C(n) = \mathcal{O}(n) + 2 * C(\frac{n}{2})$$

Ce qui donne :

$$C(n) = \mathcal{O}(n) + 2 * (\mathcal{O}(\frac{n}{2}) + 2 * C(\frac{n}{4})) = 2 * \mathcal{O}(n) + 4 * C(\frac{n}{4})$$

>**Attention** : Comme on est entrain de tout calculer, il ne faut pas simplifier les $2 * \mathcal{O}(n)$. Si vous avez du mal, remplacez tous les $\mathcal{O}(n)$ par une constante $K$ et poursuivez le calcul jusqu'au baut, c'est à dire jusqu'à éliminer les $C(n)$.

Une rapide récurrence nous donne alors : 

$$C(n) = i * \mathcal{O}(n) + 2^{i} * C(\frac{n}{2^{i}})$$

Au maximum $i = \ln_2(n)$ (après, $\frac{n}{2^{i}} < 1$) et dans ce cas là :

$$C(n) = \ln_2(n) * \mathcal{O}(n) + 2^{\ln_2(n)} * C(\frac{n}{2^{\ln_2(n)}})$$

$$C(n) = \ln_2(n) * \mathcal{O}(n) + n * C(1)$$

On en conclut que la complexité vaut : $$C(n) = \mathcal{O}(\ln_2(n) * n)$$

#### complexité minimale du tri rapide

Si l'on découpe notre tableau de façon  non équilibrée, une branche de la récursion va faire plus d'opérations que $C(n/2)$. La complexité minimale est ainsi atteinte lorsque l'on coupe notre tableau exactement en 2.

#### conclusion

Le tri rapide est donc rigolo :

* il a une complexité moyenne qui vaut sa complexité minimale et qui est $\mathcal{O}(n * \ln(n))$, donc la meilleur possible
* il est très rapide pour les tableaux en désordre et très lent pour les tableaux déjà triés.

En pratique, on commence donc par mélanger le tableau pour le trier ensuite, c'est plus rapide que le trier tout court.

## complexité du tri ?

Mais au final, parmi tous les algorithmes de tris, c'est les quels qui vont le plus vite ? Et est-ce le minimum possible ?

nombre de cas différents que peut traiter un algorithme : Dépend du nombre de tests que fait l'algorithme pour pouvoir les différentier :

* 0 test -> 1 cas (l'algorithme répond toujours la même chose)
* 1 test -> 2 cas
* 2 tests -> $4 = 2^2$ cas
* p tests -> $2^p$ cas

Si on veut distinguer $k$ cas il faut ainsi au moins $\ln_2(k)$ tests. Donc un algorithme qui doit traiter $k$ cas différents aura au moins une complexité de $\mathcal{O}(\ln_2(k))$ opérations (les tests).

Dans le cas du tri, une liste de $n$ éléments aura $n!$ permutations possibles.

Par exemple pour les 3 premiers entiers on a $[1, 2, 3]$, $[1, 3, 2]$, $[2, 1, 3]$, $[2, 3, 1]$, $[3, 1, 2]$ et $[3, 2, 1]$ : c'est bien 3! possibilités.

>**Remarque** : Si on prend la liste des 1 premiers entiers. Le plus petit entier peut être à $n$ positions différentes. Une fois sa position déterminée, le deuxième plus petit élément n'a plus que $n-1$ positions possibles : Il y a donc $n * (n-1)$ possiblités pour placer les 2 plus petits éléments. Par récurrence on démontre alors que le nombre de possibilités pour ranger les $n$ premiers entiers est $n * (n-1) * \dots * 2 * 1 = n!$.

Un algorithme de tri d'une liste à $n$ éléments quelqu'il soit aura besoin de pouvoir distinguer parmi toutes les permutations possibles de cette liste, donc parmi $n!$ possibilités.
On en déduit que sa complexité sera au moins de $C = \mathcal{O}(\ln_2(n!))$ opérations.

On peut montrer que cette complexité est équivalente à une complexité de
$\mathcal{O}(n\ln_2(n))$ opérations (voir les parties suivantes pour le détail).

Tout algorithme de tri dune liste à $n$ élément a donc au moins une complexité de $\mathcal{O}(n\ln_2(n))$.

On n'en connaît pas encore, en effet le tri par insertion, sélection et tri rapide sont tous trois de complexité égale à $\mathcal{O}(n^2)$ (même si le tri rapide est de complexité moyenne $\mathcal{O}(n\ln_2(n))$, il existe des cas où sa complexité est de $\mathcal{O}(n^2)$). Mais il en existe, comme le [tri fusion par exemple](https://fr.wikipedia.org/wiki/Tri_fusion) par exemple.

La borne de $\mathcal{O}(n \ln_2(n))$ est donc atteinte ! 

En appelant *complexité d'un problème*, la complexité (maximale) du meilleur algorithme pour le résoudre, on a que :

La complexité du tri est  de $\mathcal{O}(n\ln_2(n))$ opérations.

> **Remarque** : le tri est le cas heureux d'un problème dont on connaît la complexité (c'est à dire que l'on a un algorithme de cmplexité (maximale) minimale). Ce n'est pas le cas pour tous les problèmes. Genre la [multiplication de matrices](https://fr.wikipedia.org/wiki/Produit_matriciel), ou une borne min est de $\mathcal{O}(n^2)$ (avec $n$ le nombre de lignes de la matrice), mais on ne sait pas s'il existe des algorithme pour le faire. Le mieux que l'on sait faire pour l'instant c'est en $\mathcal{O}(n^{2.376})$.

### calcul rapide de l'équivalence

Comment arrive-t-on à prouver que $\mathcal{O}(\ln_2(n!))$ et $\mathcal{O}(n\ln_2(n))$ sont équivalents ?

En jouant avec les $\mathcal{O}$ :

$$C = \mathcal{O}(\ln_2(n!)) = \mathcal{O}(\ln_2(n * (n-1) * \dots... * 1))$$

en utilisant le fait que $\ln_2(ab) = \ln_2(a) + \ln_2(b)$ on a :

$$ C = \mathcal{O}(\ln_2(n)  + \ln_2(n-1) + \dots + \ln_2(1))$$

comme $\ln_2$ est une fonction croissante on a :

$$ C < \mathcal{O}(\ln_2(n)  + \ln_2(n) + \dots + \ln_2(n)) = \mathcal{O}(n\ln_2(n))$$

Ceci montre que toute fonction en $\mathcal{O}(n\ln_2(n))$ est en $\mathcal{O}(\ln_2(n!))$. L'implication réciproque est plus compliquée à montrer, comme on le verra dans la partie suivante.

### calcul détaillé de l'équivalence des O

Nombre de cas différents pour trier tri une liste de $n$ éléments ? Toutes les permutations possibles donc $n!$ façons de ranger $n$ éléments. 

comme $n! = n * (n-1) * (n-2) * \dots * 2 * 1$, on arrive à obtenir l'encadrement suivant :

* comme $n$ est plus grand que tous les éléments du produit on à $n! \leq n^n$
* comme $n! \geq n * (n-1) * ... * (n/2 + 1) * (n/2)$ et que  $n/2$ est plus petit que les éléments du produit, on a $n! > (n/2)^{(n/2)}$

donc :

* $(n/2)^{(n/2)} \leq n! \leq n^n$
* en passant au log : $\ln_2 ((n/2)^{(n/2)}) \leq \ln_2(n!) \leq \ln_2 (n^n)$
* donc $n/2 * \ln_2 (n/2) \leq \ln_2(n!) \leq n \ln_2(n)$

Comme $\ln_2 (n/2) = \ln_2 (n) + \ln_2(1/2) = \ln_2 (n) - \ln_2(2) = \ln_2 (n) - 1$, on a que :

$$\frac{1}{2} n\ln_2(n) - \frac{n}{2} \leq \ln_2(n!) \leq n\ln_2(n)$$

Ce qui donne :

$$\frac{1}{2} - \frac{1}{\ln_2(n)} \leq \frac{\ln_2(n!)}{n\ln_2(n)} \leq 1$$

Et puisque pour tout $n > 2^4$  on a que $\ln_2(n) > 4$, donc que $\frac{1}{2} - \frac{1}{\ln_2(n)} \leq \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$.

De là,  pour $n > 2^4$ :

$$\frac{1}{4} \leq \frac{\ln_2(n!)}{n\ln_2(n)} \leq 1$$

On peut maintenant montrer l'équivalence de $\mathcal{O}(\ln_2(n!))$ et de  $\mathcal{O}(n\ln_2(n))$ :

* si $g(n)$ est en $\mathcal{O}(\ln_2(n!))$ il existe $n_0$ et $C$ tel que : $g(n) < C * \ln_2(n!)$ pour n > $n_0$. Pour $n_1 = \max(n_0, 2^4)$ on a donc $g(n) < C * \ln_2(n!) < C * n\ln_2(n)$ : $g(n)$ est en $\mathcal{O}(n\ln_2(n))$.
* si $g(n)$ est en $\mathcal{O}(n\ln_2(n))$ il existe $n_0$ et $C$ tel que : $g(n) < C * n\ln_2(n)$ pour n > $n_0$. Pour $n_1 = \max(n_0, 2^4)$ on a donc $g(n) < C * \ln_2(n!) < C * 4 * \ln_2(n!)$ : $g(n)$ est en $\mathcal{O}(\ln_2(n!))$.

## tri fusion

Le [tri fusion](https://fr.wikipedia.org/wiki/Tri_fusion) est un tri de complexité $\mathcal{O}(n\ln_2(n))$ opérations où $n$ est la taille de la liste en entrée.

Une proposition de code est ci-après :

```python
def fusion(tab):
    if len(tab) < 2:
        return tab
    else:
        milieu = len(tab) // 2
    return fusion_colle(fusion(tab[:milieu]), fusion(tab[milieu:]))


def fusion_colle(tab1, tab2):
    i1 = i2 = 0
    tab_colle = []
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_colle.append(tab1[i1])
            i1 += 1
        else:
            tab_colle.append(tab2[i2])
            i2 += 1
    if i1 == len(tab1):
        tab_colle.extend(tab2[i2:])
    else:
        tab_colle.extend(tab1[i1:])
    return tab_colle
```

L'algorithme fonctionne ainsi :

1. on coupe la liste à trier en 2
2. on trie chacune des sous-listes à part
3. on recolle les deux listes triées en une unique liste triée (c'est `fusion_colle`)

Comme on peut utiliser n'importe quel algorithme pour trier les 2 sous-listes, autant s'utiliser soit-même ! L'algorithme fusion utilise donc l'algorithme fusion pour trier les sous-listes de l'algorithme fusion.

La complexité de l'algorithme est alors :

$$C(n) = 2 * C(n/2) + D(n)$$

Où :
* $C(n)$ est la complexité de l'algorithme fusion pour une liste à $n$ éléments (algorithme `fusion`)
* $D(n)$ est la complexité de fusionner deux listes triées en une unique liste triées (algorithme `fusion_colle`). 

Comme l'algorithme `fusion_colle` est en $\mathcal{O}(n)$, l'équation de récurrence de la complexité est :

$$C(n) = 2 * C(n/2) + \mathcal{O}(n)$$

Pour connaître la valeur de la complexité on utilise le [master theorem](https://fr.wikipedia.org/wiki/Master_theorem) qui est **LE** théorème des complexités pour les algorithmes récursifs. Sa preuve dépasse (de loin) le cadre de ce cours, mais son énoncé sous la  [notation de Landau](https://fr.wikipedia.org/wiki/Master_theorem#%C3%89nonc%C3%A9_avec_la_notation_de_Landau), nous permet de déterminer aisément la complexité de nombreux algorithmes récursifs, dont le notre : $\mathcal{O}(n\ln_2(n))$, puisque $1 = \ln_2(2)$.

> **Remarque** : tout comme le tri par sélection, le tri fusion a la particularité d'avoir toujours le même nombre d'opérations quelque soit la liste en entrée. 

### fusion colle ?

Comprenez comment la fonction `fusion_colle` fonctionne. Une fois que vous avez compris, faites des tests pour cette fonction que vous ajouterez à vos tests.

### fusion ?

La logique de l'algorithme `fusion` est appelée *diviser pour régner* : on résous des sous-problèmes puis on crée une solution globale à partir des solutions partielles. Cette stratégie fonctionne lorsque la création d'une solution globale à partir de solutions partielle est aisée. 

Pour notre algorithme fusion :

* quels sont les solutions partielles ?
* comment sont calculées les solutions partielles ?
* comment est construite la solution globale à partir des solutions partielles ?
* la construction de la solution globale est-elle facile ? Quelle est sa complexité ?

### expérimentation

Vérifier expérimentalement que la complexité est bien $\mathcal{O}(n\ln_2(n))$. Ici c'est bien la complexité maximale que l'on observe puisque le nombre d'opérations est constant (en grand O) quel que soit la liste à trier.

Regardez le aussi trier, c'est très différent des autres tris.

## mélanger des listes ?

On s'est appuyé sur la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle) pour mélanger des listes.

Mais sommes-nous bien sur que le mélange est bien équiprobable ? Sinon nos mesures de complexité en moyenne seraient tous faux...

Rassurez vous c'est le cas. Elle utilise la méthode de mélange de [Fisher-Yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), qui est un algorithme linéaire permettant d'obtenir toutes les permutations possibles de façon équiprobable.

Ce qui est marrant c'est que cet algorithme est *"l'inverse"* d'un tri par sélection. 

Implémentez cet algorithme et vérifiez que pour la liste des 4 premiers entiers vous obtenez bien (sur un grand nombre d'essais) à peut prêt le même nombre des 24 permutations possibles.

Si vous voulez en savoir un peu plus sur cet algorithme et de comment générer un nombre aléatoire en python : <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>