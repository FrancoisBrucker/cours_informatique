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
>* [étude : mélanger un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %})
>
{: .chemin}

Les informaticiens adorent les [algorithmes de tris](https://fr.wikipedia.org/wiki/). Pas parce qu'ils aime l'ordre — loin de là — mais parce qu'il existe des millions de façons différentes de trier. Commençons par définir le problème :

>
> * nom : tri
> * données : un tableau d'entiers
> * réponse : un tableau contenant les valeurs du tableau en entrée triées selon l'ordre croissant
>
{: .note}

## problème de reconaissance

Commençons par travailler sur un problème connexe au problème du tri, celui de la reconnaissance :

>
> * nom : est trié ?
> * données : un tableau $T$ d'entiers
> * question : $T$ est-il trié de façon croissante ?
> * réponse : OUI ou NON.
>
{: .note}

### algorithme

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def est_trie(tableau):

    for i in range(1, len(tableau)):
        if tableau[i] < tableau[i-1]:
            return False
    return True

{% endhighlight %}

#### fonctionnement

L'algorithme rend bien :

* `True` pour `est_trie([42])`
* `False` pour `est_trie([4, 2])`
* `True` pour `est_trie([2, 4])`

#### preuve

La finitude de l'algorithme est clair puisqu'il n'y a qu'une boucle for avec autant d'itération que la taille du tableau passé en entrée.

Le preuve en démontrant l'invariant de boucle : à la fin d'un itération, les $i + 1$ premiers éléments du tableau sont triés.

1. à la fin de la première itération, si l'on est pas sorti de la boucle c'est que $tableau[i] \geq tableau[i-1]$ pour $i=1$ : les 2 premiers éléments du tableau sont bien triés.
2. Si l'invariant est vrai à la fin de l'itération $i-1$, à la fin de l'itération $i$ on à $tableau[i] \geq tableau[i-1]$ et comme les $i + 1$ premiers éléments du tableau sont triés : les $i + 1$ premiers éléments du tableau sont triés.

Au final :

* L'invariant prouve que : si on arrive à la ligne 6 de l'algorithme c'est que les $n$ premiers éléments du tableau sont triés.
* si on utilise le retour de la ligne 5 c'est qu'il existe $i$ avec `tableau[i] < tableau[i-1]`, donc tableau ne peut-être trié.

> L'algorithme `est_trie` est une solution au problème *"est trié ?"*
{: .note}

#### complexité de l'algoritme

Ligne à ligne :

1. définition de la finction $\mathcal{O}(1)$
2. 
3. une boucle for de $k$ itérations
4. un tests de deux valeur dans un tableau : $\mathcal{O}(1)$
5. un retour de fonction $\mathcal{O}(1)$
6. un retour de fonction $\mathcal{O}(1)$

Que l'on sorte par le retour de la ligne 5 oi 6, le complexité est : $\mathcal{O}(k)$. Dans le cas le pire, on parcours tout le tableau, donc :

> La complexité de l'algorithme `est_trie` est $\mathcal{O}(n)$ avec $n$ la taille du tableau en entrée.
{: .note}

### complexité du problème

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [complexité du problème de la *"recherche"*]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %}#complexite-recherche), un algorithme résolvant ce problème doit considérer toutes les cases du tableaux et donc une borne min du problème *"est trié ?"* est $\mathcal{O}(n)$ où $n$ est la taille du talbeau en entrée. Comme la complexité de `est_trie`  est égalemnt de $\mathcal{O}(n)$.On en conclut :

> La complexité du problème *"est trié ?"* est de $\mathcal{O}(n)$ où $n$ est la taille du talbeau en entrée
{: .note}

## bornes du problème

### borne maximum

La l'algorithme `permutations` de l'[étude sur les mélanges d'un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %}#algo-toutes-permutations) permet de calculer en $\mathcal{O}((n+2)!)$ toutes les permutations d'un tableau à $n$ éléments. Comme l'algorithme `est_trie` permet de savoir si un tableau est trié en $\mathcal{O}(n)$ opérations, on peut résoudre le problème *"trie"* en énumérant toutes les permutations du tableau passé en paramètre et en vérifiant pour chaque d'entre elle s'il est trié ou non.

La complexité de cet algorithme est alors le produit de la complexité de `permutations` et de `est_trie` : $\mathcal{O}(n \cdot (n+2)!)$. On en conclut :

> Une borne maximum du problème *"tri"* est $\mathcal{O}(n \cdot (n+2)!)$ où $n$ est la taille du tableau passé en entrée
{: .note}

Comme [n! est trop gros]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#n_factoriel), ce n'est vraiment pas un algorithme à utiliser si on peut faire mieux... Mais il nous permet d'énoncer la propriété :

> Pour tout problème algorithmique, s'il existe :
>
> * un algorithme énumérant tous les cas possibles
> * un algorithme permetant de vérifier si un cas donné est une solution
>
> Alors la combinaison des deux algorithmes, de complexité le produit des deux algorithmes la constituant, est une solution au problème initial.
{: .note}

Souvent les algorithme produit par la remarque précédente ne sont pas optimaux car on explore bien trop de cas.

### borne minimum

Si les éléments du tableau à trié sont tous différents, les permutations de celui-ci sont toutes différentes et une seule est la solution au problème "tri".

Par exemple, pour un tableau à trois éléments :

1. $[1, 2, 3]$
2. $[1, 3, 2]$
3. $[2, 1, 3]$
4. $[2, 3, 1]$
5. $[3, 1, 2]$
6. $[3, 2, 1]$

Quelque soit la forme de l'entrée (de 1 à 6), l'algorithme de tri doit rendre la forme 1 : un algorithme de tri doit pouvoir distinguer parmi toutes les permutations du tableau. Comme il y a $n!$  permutations différentes pour un tableau de taile $n$ dont éléments sont deux à deux différents, tout algorithme de tri doit pouvoir ditinguer parmi $n!$ choix, en utilisant la propriété de nobre de cas à distinguer choix vue [dans la complexité du problème de la *"recherche ordonnée"*]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %}#complexite-recherche-ordonnee), on en déduit que :

Tout algorithme de tri d'un tableau à $n$ élément doit distinguer parmi $n!$ cas, il est donc au minimum de complexité $\mathcal{O}(\ln(n!))$. On rend cette borne min un peu plus jolie en utilisant le fait que ;

>Toute fonction en $\mathcal{O}(\ln(n!))$ est également une fonction en $\mathcal{O}(n\ln(n))$ et réciproquement.
{: .note}
{% details démonstration %}

On a :

$$ (\frac{n}{2})^{\frac{n}{2}} \leq n \cdot (n-1) \cdot \ ...\ \cdot \frac{n}{2} \leq n! = n \cdot (n-1) \ ... \ \cdot 1 \leq n \cdot \ ...\  \cdot n = n ^n$$

Donc, en passant au $\ln$ :

$$
\ln((\frac{n}{2})^{\frac{n}{2}}) \leq \ln(n!) \leq \ln(n^n)
$$

Et donc, pour $n \geq 4$, on a l'encadrement suivant :

$$
\frac{n}{2}\ln(\frac{n}{2}) \leq \ln(n!) \leq n\ln(n)
$$

Poursuivons en triturant $\ln(\frac{n}{2})$ : 

$$
\begin{array}{lclr}
\ln(\frac{n}{2}) &= &\frac{1}{2}\ln(\frac{n}{2}) + \frac{1}{2}\ln(\frac{n}{2})&\\
\ln(\frac{n}{2}) &\geq& \frac{1}{2}\ln(\frac{4}{2}) + \frac{1}{2}\ln(\frac{n}{2}) & (\mbox{pour } n \geq 4)\\
\ln(\frac{n}{2}) &\geq& \frac{1}{2}(\ln(2) + \ln(\frac{n}{2})) & (\mbox{pour } n \geq 4)\\
\ln(\frac{n}{2}) &\geq& \frac{1}{2}(\ln(2\cdot \frac{n}{2})) & (\mbox{pour } n \geq 4)\\
\ln(\frac{n}{2}) &\geq& \frac{1}{2}(\ln(n)) & (\mbox{pour } n \geq 4)\\
\end{array}
$$

On combine cette inégalité à notre encadrement précédent pour trouver :

$$
\frac{n}{2}(\frac{1}{2}(\ln(n))) \leq \ln(n!) \leq n\ln(n)
$$

Ce qui se dérive directement, pour $n \geq 4$, en :

$$\frac{1}{4} \leq \frac{\ln(n!)}{n\ln(n)} \leq 1$$

Enfin, on peut montrer les équivalences de $\mathcal{O}$ : 

* si $g(n)$ est en $\mathcal{O}(\ln(n!))$ il existe $N_0$ et $C$ tel que : $g(n) < C \cdot \ln(n!)$ pour n > $N_0$. Pour $N_1 = \max(N_0, 4)$ on a donc $g(n) < C \cdot \ln(n!) < C \cdot n\ln(n)$ : $g(n)$ est en $\mathcal{O}(n\ln(n))$.
* si $g(n)$ est en $\mathcal{O}(n\ln(n))$ il existe $N_0$ et $C$ tel que : $g(n) < C \cdot n\ln(n)$ pour n > $N_0$. Pour $N_1 = \max(N_0, 4)$ on a donc $g(n) < C \cdot \ln_2(n!) < C \cdot 4 \cdot \ln(n!)$ : $g(n)$ est en $\mathcal{O}(\ln(n!))$.

{% enddetails %}

> Tout algorithme de tri d'une liste à $n$ éléments a au moins une complexité de $\mathcal{O}(n\ln(n))$ opérations.
{: .note}

Une borne min du problème du *"tri"* est donc $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau en entrée, mais on ne sait pas si un tel algorithme existe.

{% details spoil %}
oui, de tels algorithmes exitent.
{% enddetails %}

## tris *simples*

Notre algorithme pour trier un tableau est un monstre. Il en existe de très simples et de complexité bien plus faible. Nous en montrons 2, classiques.

### tri par insertion

### tri par selection


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

> anti melangeur. A la placede random on cherche
{: .tbd}

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

> Extension de la vérification. tri du jeu de carte. 
{: .tbd}


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

> Vous allez le prouver expérimentalement pendant la session de code.

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