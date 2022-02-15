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

Les informaticiens adorent les [algorithmes de tris](https://fr.wikipedia.org/wiki/). Pas parce qu'ils aiment l'ordre — loin de là — mais parce qu'il existe des millions de façons différentes de trier. Commençons par définir le problème :

>
> * nom : tri
> * données : un tableau d'entiers
> * réponse : un tableau contenant les valeurs du tableau en entrée triées selon l'ordre croissant
>
{: .note}

## problème de reconnaissance

Commençons par travailler sur un problème connexe au problème du tri, celui de la reconnaissance :

>
> * nom : est trié ?
> * données : un tableau $T$ d'entiers
> * question : $T$ est-il trié de façon croissante ?
> * réponse : OUI ou NON.
>
{: .note}

### algorithme {#algo-est-trie}

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

La finitude de l'algorithme est claire puisqu'il n'y a qu'une boucle for avec autant d'itérations que la taille du tableau passé en entrée.

Le preuve en démontrant l'invariant de boucle : à la fin d'un itération, les $i + 1$ premiers éléments du tableau sont triés.

1. à la fin de la première itération, si l'on est pas sorti de la boucle c'est que $\mbox{tableau}[i] \geq \mbox{tableau}[i-1]$ pour $i=1$ : les 2 premiers éléments du tableau sont bien triés.
2. Si l'invariant est vrai à la fin de l'itération $i-1$, à la fin de l'itération $i$ on à $\mbox{tableau}[i] \geq \mbox{tableau}[i-1]$ et comme les $i + 1$ premiers éléments du tableau sont triés : les $i + 1$ premiers éléments du tableau sont triés.

Au final :

* L'invariant prouve que : si on arrive à la ligne 6 de l'algorithme c'est que les $n$ premiers éléments du tableau sont triés.
* si on utilise le retour de la ligne 5 c'est qu'il existe $i$ avec $\mbox{tableau}[i] < \mbox{tableau}[i-1]$, donc $\mbox{tableau}$ ne peut être trié.

> L'algorithme `est_trie` est une solution au problème *"est trié ?"*
{: .note}

#### complexité de l'algorithme

Ligne à ligne :

1. définition de la fonction $\mathcal{O}(1)$
2. 
3. une boucle for de $k$ itérations
4. un tests de deux valeurs dans un tableau : $\mathcal{O}(1)$
5. un retour de fonction $\mathcal{O}(1)$
6. un retour de fonction $\mathcal{O}(1)$

Que l'on sorte par le retour de la ligne 5 ou 6, le complexité est : $\mathcal{O}(k)$. Dans le cas le pire, on parcourt tout le tableau, donc :

> La complexité de l'algorithme `est_trie` est $\mathcal{O}(n)$ avec $n$ la taille du tableau en entrée.
{: .note}

### complexité du problème

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [complexité du problème de la *"recherche"*]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %}#complexite-recherche), un algorithme résolvant ce problème doit considérer toutes les cases du tableau et donc une borne min du problème *"est trié ?"* est $\mathcal{O}(n)$ où $n$ est la taille du talbeau en entrée. Comme la complexité de `est_trie`  est égalemnt de $\mathcal{O}(n)$.On en conclut :

> La complexité du problème *"est trié ?"* est de $\mathcal{O}(n)$ où $n$ est la taille du tableau en entrée
{: .note}

## bornes du problème

### borne maximum {#borne-max}

Etant donné un tableau $T$ de taille $n$, on peut utiliser l'algorithme `permutations(T)` de l'[étude sur les mélanges]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %}#algo-toutes-permutations) qui rend toutes les permutations d'un tableau donné en $\mathcal{O}((n+2)!)$ opérations.

Par exemple, l'algorithme `permutations([1, 3, 2])` rendra :

```python
[[1, 3, 2], [1, 2, 3], [3, 1, 2], [3, 2, 1], [2, 1, 3], [2, 3, 1]]
```

C'est une complexité énorme, mais cela nous permet de résoudre notre problème puisque l'algorithme `est_trie` permet de savoir si un tableau est trié en $\mathcal{O}(n)$ opérations : on peut résoudre le problème *"trie"* en énumérant toutes les permutations du tableau passé en paramètre et en vérifiant pour chacune d'entre elle s'il est trié ou non.

Un proposition d'algorithme peut alors être :

```text
def trie_long(T):
    possibles = permutations(T)
    pour chaque element de possible:
        si est_trie(element):
            rendre True
```

La complexité de `trie_long` est égale à la complexité de `permutations`  ($\mathcal{O}(n+2)!$) plus la complexité de  `est_trie` ($\mathcal{O}(n)$) multiplié par le nombre de permutations ($n!$) : ce qui donne une complexité finale de $\mathcal{O}(n+2)!$.

> Une borne maximum du problème *"tri"* existe, et est de complexité $\mathcal{O}((n+2)!)$ où $n$ est la taille du tableau passé en entrée.
{: .note}

Comme [n! est trop gros]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#n_factoriel), ce n'est vraiment pas un algorithme à utiliser si on peut faire mieux... Mais il nous permet d'énoncer la propriété :

> Pour tout problème algorithmique, s'il existe :
>
> * un algorithme énumérant tous les cas possibles
> * un algorithme permettant de vérifier si un cas donné est une solution
>
> Alors la combinaison des deux algorithmes est une solution au problème initial.
{: .note}

Souvent les algorithmes produits par la remarque précédente ne sont pas optimaux car on explore bien trop de cas.

### borne minimum

Si les éléments du tableau à trier sont tous différents, les permutations de celui-ci sont toutes différentes et une seule est la solution au problème "tri".

Par exemple, pour un tableau à trois éléments :

1. $[1, 2, 3]$
2. $[1, 3, 2]$
3. $[2, 1, 3]$
4. $[2, 3, 1]$
5. $[3, 1, 2]$
6. $[3, 2, 1]$

Quelque soit la forme de l'entrée (de 1 à 6), l'algorithme de tri doit rendre la forme 1 : un algorithme de tri doit pouvoir distinguer parmi toutes les permutations du tableau. Comme il y a $n!$  permutations différentes pour un tableau de taille $n$ dont les éléments sont deux à deux différents, tout algorithme de tri doit pouvoir distinguer parmi $n!$ choix, en utilisant la propriété de nombre de cas à distinguer vue [dans la complexité du problème de la *"recherche ordonnée"*]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %}#complexite-recherche-ordonnee), on en déduit que :

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

Notre algorithme pour trier un tableau est un monstre de complexité. Il en existe de très simples et de complexité bien plus faible. Nous en montrons 2, classiques.

### tri par sélection {#tri-selection}

L'algorithme procède alors ainsi : à chaque itération de l'algorithme, on place à l'indice $i$ du tableau son $i$-ème plus petit élément.

> Ecrivez un algorithme qui met en œuvre ce principe
{: .a-faire}
{% details  une solution %}
<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def selection(tableau):
    for i in range(len(tableau) - 1):
        min_index = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[min_index]:
                min_index = j
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]

{% endhighlight %}

L'algorithme `selection` **modifie** le tableau passé en paramètre. On appelle ces algorithmes [in place](https://en.wikipedia.org/wiki/In-place_algorithm) car ils ne rendent rien, mais modifient les données en entrées.

{% enddetails %}

#### fonctionnement {#fonctionnement-selection}

On vérifie que l'algorithme fonctionne pour :

* un petit tableau trié : `[1, 2, 3]`
* un petit tableau non trié où le plus petit est en dernière place : `[3, 2, 1]`

#### preuve {#preuve-selection}

Le principe de fonctionnement est clair. Il reste à prouver que c'est bien ce que l'algorithme `selection` fait.

1. la boucle `for` de la ligne 4 trouve l'indice du plus petit élément du tableau `tableau[i:]`.
2. la ligne 7 échange le minimum du tableau `tableau[i:]` avec `tableau[i]`
3. comme la boucle `for` de la ligne 2 incrémente $i$, on a l'invariant de boucle : *"à la fin de chaque étape $i$ de l'algorithme les $i$ plus petites valeurs du tableau sont triées aux $i$ premiers indices du tableau"*

#### complexités {#complexites-selection}

On suppose que la taille du tableau est $n$.

Ligne à ligne :

1. début de fonction : $\mathcal{O}(1)$
2. une boucle de $n-1$ itérations
3. une affectation $\mathcal{O}(1)$
4. une boucle de $n-i-1$ itérations ($i$ est la variable définie ligne 2)
5. un test et deux valeurs d'un tableau : $\mathcal{O}(1)$
6. une affectation : $\mathcal{O}(1)$
7. deux affectation et quatre valeurs d'un tableau : $\mathcal{O}(1)$

Le nombre d'itérations de la boucle for de la ligne 4 n'est pas constant, mais il décroit puisque $i$ augmente à chaque itération de la boucle `for`de la ligne 2. On peut alors utiliser la [règle de croissance]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#regle-croissance) pour utiliser le maximum, $n-1$, pour le calcul de la complexité.

Ce qui donne une complexité de :

$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \\
&& (n-1) \cdot (\\
&& \mathcal{O}(1) + \\
&& (n-1) \cdot ( \\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1)) \\
& = & \mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1))\\
& = & \mathcal{O}(n^2) \\
\end{array}
$$

Le nombre d'itérations est constant quelque soit le tableau, on a donc :

> La complexité de l'algorithme `selection` est ($n$ est la taille du tableau passé en entrée) :
>
>* la **complexité min** vaut $\mathcal{O}(n^2)$
>* la **complexité (max)** vaut $\mathcal{O}(n^2)$
>
{: .note}

Puisque la complexité min et max sont égales, on en déduit que la **complexité en moyenne** vaut également $\mathcal{O}(n^2)$.

### tri par insertion {#tri-insertion}

Le tri par insertion est une extension de l'[algorithme `est_trie`](#algorithme-algo-est-trie). Plutôt que de rendre `False` il répare. L'algorithme `est_trie` répond `False` au plus petit `i` tel que `tableau[i] < tableau[i-1]`. On est alors dans le cas où :

* `tableau[:i]` est trié
* `tableau[i] < tableau[i-1]`

Pour que l'on puisse continuer, il faut s'arranger pour que `tableau[:i+1]` soit trié. Pour cela, on peut utiliser le fait que `tableau[:i+1]` est trié si et seulement si :

* `tableau[1] >= tableau[0]`
* `tableau[2] >= tableau[1]`
* ...
* `tableau[i] >= tableau[i-1]`

Dans notre cas, toutes les conditions sont vérifiées sauf la dernière. Si l'on échange `tableau[i]` et `tableau[i-1]` toutes les conditions seront vérifiées sauf peut-être l'avant-dernière. Si elle n'est pas vérifiée on peut échanger `tableau[i-1]` et `tableau[i-1]` et alors toutes les conditions seront vérifiées sauf peut-être l'avant-avant-dernière, que l'on peut à nouveau échanger, et ainsi de suite jusqu'à ce que toutes les conditions soient vérifiées.

Cette analyse (ce n'est pas encore une preuve formelle) nous permet de dégager le principe suivant :

On vérifie itérativement que `tableau[i] >= tableau[i-1]` et si ce n'est pas le cas on fait *remonter* `tableau[i]` par échanges successifs à la première place où il sera plus grand que le précédent.

> Ecrivez un algorithme qui met en œuvre ce principe
{: .a-faire}
{% details  une solution %}
<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def insertion(tableau):
    for i in range(1, len(tableau)):
        courant = tableau[i]
        j = i
        while (j > 0) and (courant < tableau[j - 1]):
            tableau[j] = tableau[j - 1]
            j -= 1
        tableau[j] = courant

{% endhighlight %}

L'algorithme `insertion`, comme l'algorithme `selection`, **modifie** le tableau passé en paramètre.

Pour garantir que `tableau[j - 1]` soit toujours valide (il faut que $j-1 \geq 0$), on place en tête de la condition `(courant < tableau[j - 1])` de la ligne 5 la [sentinelle](https://en.wikipedia.org/wiki/Sentinel_value) `(j > 0)`. Les deux conditions étant liées par un `and`, python (et tout autre langage de programmation) n'évaluera la seconde condition **que si la première est vérifiée** (un `and` ne peut être vrai que si les deux conditions sont vraies. Si la première condition est fausse, il est impossible que le `and` soit vrai il est donc inutile de vérifier la seconde condition). Cette technique est très utile, ça vaut le coup de la connaître.

{% enddetails %}

#### fonctionnement {#fonctionnement-insertion}

Tout comme pour l'algorithme de tri par sélection, on vérifie que l'algorithme fonctionne pour :

* un petit tableau trié : `[1, 2, 3]`
* un petit tableau non trié où le plus petit est en dernière place : `[3, 2, 1]`

#### preuve {#preuve-insertion}

Le principe de programmation du tri par insertion est correct puisque `est_trie` est prouvé. Mais il faut vérifier qu'il est bien mis en œuvre dans l'algorithme. On utilise ici celui donné en solution.

Tout d'abord, comme la condition de la boucle `while` de la ligne 5 contient `(j > 0)` et que `j` décroit strictement à chaque itération (ligne 7), notre algorithme va bien s'arrêter.

A chaque itération $i$ de la boucle `for` (ligne 2), l'algorithme fonctionne ainsi :

* ligne 3 : on a : `tableau[:i+1] = tableau[:i] + [courant]`
* à la sortie de la boucle `while`, juste avant la ligne 8. En notant `tableau` le tableau avant la boucle `while` et `tableau'` le tableau en fin de `while`, on a :
  * `tableau'[:i+1] = tableau[:j] + [tableau[j]] + tableau[j:i]`
  * `tableau[:j]` trié et `courant >= tableau[j-1]`
  * `tableau[j:i]` trié `courant < tableau[j]`
* après la ligne 8, juste avant de faire une nouvelle itération de la boucle `for`. En notant `tableau` le tableau avant le début de l'itération et `tableau` le tableau en fin d'itération', on a : `tableau'[:i+1] = tableau[:j] + [tableau[i]] + tableau[j:i]`

Notre invariant de boucle est donc : *"à la fin de l'itération i, les i premiers éléments du tableau sont triés"*

#### complexités {#complexites-insertion}

Ligne à ligne :

1. appel de fonction : $\mathcal{O}(1)$
2. $n-1$ itérations, avec $n$ la taille du tableau
3. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$
4. affectation d'une variable : $\mathcal{O}(1)$
5. $k$ itérations et deux tests en $\mathcal{O}(1)$ pour chaque itération
6. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$
7. une soustraction et une affectation : $\mathcal{O}(1)$
8. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$

Comme $k$ n'est pas constant pour chaque itération de la boucle `for` il faut regarder les valeurs extrêmes que peut prendre $k$ :

* si le tableau est déjà trié : on ne rentre jamais dans la boucle `while` : $k = 0$ pour chaque itération.
* si le tableau est trié à l'envers : pour la $i$-ème itération de la boucle `for`, on aura $k=i$. C'est de plus le maximum théorique possible ($j=i$ initialement et j décroit de 1 à chaque itération de la boucle `while`).

On a donc 2 cas extrêmes pour le calcul :

1. $k = 0$ à chaque itération
2. $k$ croit de $1$ à $n-1$ à chaque itération : la [règle de croissance]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#regle-croissance) nous indique qu'on peut considérer que $k=n-1$ pour le calcul de la complexité

Ce qui donne une complexité de :

$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \\
&& (n-1) \cdot (\\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& k \cdot (\mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1)) \\
& = & \mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + k \cdot (\mathcal{O}(1))\\
& = & \mathcal{O}(n \cdot (k + 1)) \\
\end{array}
$$

> La complexité de l'algorithme `insertion` est ($n$ est la taille du tableau passé en entrée) :
>
>* la **complexité min** est atteinte pour $k=0$, c'est à dire lorsque le tableau est déjà trié, et vaut $\mathcal{O}(n)$
>* la **complexité (max)** est atteinte pour $k=n-1$, c'est à dire lorsque le tableau est trié par ordre décroissant, et vaut $\mathcal{O}(n^2)$
>
{: .note}

La complexité min est différente de la complexité maximale. On va donc calculer la complexité en moyenne pour connaitre la complexité pour des données *standard*.
Pour savoir ce que veut dire *standard*, il faut déterminer le modèle de données : prenons le équiprobable.

Cela signifie que pour chaque itération $i$ :

* `tableau[i]` sera bien placé pour une proportion de $\frac{1}{i + 1}$ tableaux
* `tableau[i]` devra être positionné en $i-1$ pour une proportion de $\frac{1}{i + 1}$ tableaux,
* ...
* `tableau[i]` devra être positionné en $i-j$ pour une proportion de $\frac{1}{i + 1}$ tableaux,
* ...
* `tableau[i]` devra être positionné en $0$ pour une proportion de $\frac{1}{i + 1}$ tableaux.

La complexité en moyenne sera donc égale à :

$$
\begin{array}{lcl}
C_m &=& \mbox{complexité hors boucle for} + \sum_{i=1}^{n-1}(\mbox{complexité hors boucle while} + i \cdot (\mbox{complexité boucle while}))\\
&=& \mathcal{O}(1) + \sum_{i=1}^{n-1} (\mathcal{O}(1) + i \cdot \mathcal{O}(1))\\
&=& \mathcal{O}(1) \cdot \sum_{i=1}^{n-1} i \\
&=& \mathcal{O}(1) \cdot \frac{n(n-1)}{2} \\
&=& \mathcal{O}(n^2)\\
\end{array}
$$

> La **complexité en moyenne** de l'algorithme `insertion` est $\mathcal{O}(n^2)$ où $n$ est la taille du tableau passé en entrée.
{: .note}

Le cas le meilleur arrive très rarement par rapport au cas le pire (parmi les $n!$ ordres possibles, il y en a très peu qui sont presque triés).

Si l'on change le modèle de données et que l'on considère des tableaux *presque triées*, la complexité en moyenne va être de l'ordre de la complexité minimale, à savoir : $\mathcal{O}(n)$

> On utilise le tri par insertion lorsque nos données seront presque toujours déjà triées ou très peu en désordre.
{: .note}

Ce calcul de complexité nous permet d'utiliser la règle suivante, qui va se révéler très utile :

> Soit $A$ un ensemble de $n$ nombres aléatoires, et $x$ un nombre également aléatoire.
> Pour tout $ y \in A$, il y a 50% de chances que $x \leq y$. Il y a donc en moyenne $\frac{n}{2}$ éléments de $A$ qui sont plus grand que $x$.
{: .note}

## tri fusion

Le [tri fusion](https://fr.wikipedia.org/wiki/Tri_fusion) est un tri de complexité $\mathcal{O}(n\ln(n))$ opérations où $n$ est la taille de la liste en entrée. Il fonctionne ainsi :

Si l'on possède une fonction `colle(T1, T2)`, avec `T1` et `T2` des tableaux triés, qui rend le tri de la concaténation de `T1` et `T2`, alors la fonction récursive suivante (avec $\mid T \mid$ la longueur du tableau $T$) est un algorithme de tri !

$$
\mbox{fusion}(T) = \left\{
    \begin{array}{lr}
        \mbox{colle}(\mbox{fusion}(T[\mid T\mid //\ 2:]), \mbox{fusion}(T[:\mid T\mid //\ 2]) & \mbox{si } \mid T \mid \geq 2\\
        T & \mbox{sinon.}
    \end{array}
\right.
$$

L'algorithme fonctionne en effet ainsi :

1. on coupe la liste à trier en 2
2. on trie chacune des sous-listes à part (en s'utilisant soit-même pour trier)
3. on recolle les deux listes triées en une unique liste triée

> L'algorithme de tri `fusion` utilise la méthode de création d'algorithme nommée [diviser pour régner](https://fr.wikipedia.org/wiki/Diviser_pour_r%C3%A9gner_(informatique)) qui est une méthode se révélant souvent efficace lorsqu'il est facile de reconstruire une solution globale à un problème à partir de solutions partielles.
{: .note}

### algorithme colle

> Pour comprendre pourquoi c'est une bonne idée, écrivez un algorithme qui implémente la fonction `colle(T1, T2)`. Il faut que sa complexité soit égale à $\mathcal{O}(n_1 + n_2)$ avec $n_1$ et $n_2$ les tailles des tableaux `T1` et `T2` respectivement.
>
{: .a-faire}
{% details   une solution %}

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def colle(tab1, tab2):
    i1 = i2 = 0
    tab_colle = []
    while i1 < len(tab1) or i2 < len(tab2):
        if i2 == len(tab2):
            tab_colle.append(tab1[i1])
            i1 += 1
        elif i1 == len(tab1):
            tab_colle.append(tab2[i2])
            i2 += 1
        elif tab1[i1] < tab2[i2]:
            tab_colle.append(tab1[i1])
            i1 += 1
        else:
            tab_colle.append(tab2[i2])
            i2 += 1
    return tab_colle

{% endhighlight %}

{% enddetails %}

#### fonctionnement {#fonctionnement-colle}

On vérifie pour deux petits tableaux **triés**, par exemple : `[1, 4, 7]` et `[0, 2, 3, 98]`.

#### preuve {#preuve-colle}

L'algorithme se finit bien puisqu'à chaque itération de la boucle while soit `i1` soit `i2` augmente. Au bout de `len(T1) + len(T2)` itération on aura `i1` = `len(T1)` et `i2` = `len(T1)`, donc la condition `i1 < len(tab1) or i2 < len(tab2)` ne sera plus vérifiée.

L'invariant de boucle que l'on peut facilement prouver est : *"`tab_colle` est trié et contient les `i1` premiers éléments `T1` et les `i2` premiers éléments `T2`"*.

#### complexités {#complexites-colle}

Allons un peu plus vite :

* on a une boucle `while` de `len(T1) + len(T2)` itérations
* chaque ligne de l'algorithme est en $\mathcal{O}(1)$

> La complexité max et min de `colle` est $\mathcal{O}(n_1 + n_2)$ avec $n_1$ et $n_2$ les tailles des tableaux `T1` et `T2` respectivement.
{: .note}

### algorithme fusion

Une proposition d'algorithme de la fonction récurente est ci-après :

```python

def fusion(tableau):
    if len(tableau) < 2:
        return tableau
    else:
        milieu = len(tableau) // 2
    return colle(fusion(tableau[:milieu]), fusion(tableau[milieu:]))

```

#### fonctionnement {#fonctionnement-fusion}

On vérifie pour deux petits tableaux, par exemple :

* `[4]`
* `[1, 2, 0, 4, 3, 98, 7]`

#### preuve {#preuve-fusion}

Comme  `milieu < len(tableau)` si `len(tableau) > 1`, l'algorithme va bien converger. De plus, comme l'algorithme `colle` est démontré, `fusion` est bien un algorithme de tri.

#### complexités {#complexites-fusion}

La complexité de l'algorithme `fusion` est (avec $n$ la taille du tableau passé en entrée) :

$$C(n) = 2 \cdot C(\frac{n}{2}) + D(n)$$

Où :

* $C(n)$ est la complexité de l'algorithme fusion pour une liste à $n$ éléments (algorithme `fusion`)
* $D(n)$ est la complexité de fusionner deux listes triées en une unique liste triées (algorithme `colle`).

Comme l'algorithme `colle` est en $\mathcal{O}(n)$, l'équation de récurrence de la complexité est :

$$C(n) = 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)$$

Pour connaître la valeur de la complexité on utilise le [master theorem](https://fr.wikipedia.org/wiki/Master_theorem) qui est **LE** théorème des complexités pour les algorithmes récursifs. Sa preuve dépasse (de loin) le cadre de ce cours, mais [son énoncé sous la notation de Landau](https://fr.wikipedia.org/wiki/Master_theorem#%C3%89nonc%C3%A9_avec_la_notation_de_Landau), nous permet de déterminer aisément la complexité de nombreux algorithmes récursifs dont le nôtre :

> **Master Theorem**
>  
> $$T(n) = a \cdot T(\frac{n}{b}) + \mathcal{O}(n^d)$$
>
> * si $d < \log_b(a)$ alors $T(n)  = \mathcal{O}(n^{\log_b(a)})$
> * si $d = \log_b(a)$ alors $T(n)  = \mathcal{O}(n^d \cdot \ln(n))$
> * si $d > \log_b(a)$ alors $T(n)  = \mathcal{O}(n^d)$
>
{: .note}

Dans notre cas on a $a = 2$, $b = 2$  et $d = 1$ donc $d = \log_2(a)$ :

> La complexité de l'algorithme `fusion` est $\mathcal{O}(n\ln(n))$ où $n$ est la taille de la liste en entrée
{: .note}

Tout comme le tri par sélection, le tri fusion a la particularité d'avoir toujours le même nombre d'opérations quelque soit la liste en entrée.

{% details calcul de la complexité sans utiliser le master theorem %}

$$
\begin{array}{lcl}
C(n) &=& 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2 \cdot (2 \cdot (C(\frac{n}{4}) + \mathcal{O}(\frac{n}{2})) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(n)\\
&=& ...\\
&=& 2^k \cdot C(\frac{n}{2^k}) + k \cdot \mathcal{O}(n)\\
&=& ...\\
&=& 2^{\log_2(n)} \cdot C(1) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& n \cdot C(1) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& \mathcal{O}(n) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& \mathcal{O}(n\log_2(n))\\
&=& \mathcal{O}(n\ln(n))
\end{array}
$$

{% enddetails %}

## tri de python

```python

T = [1, 3, 2, 6, 4, 5]
T.sort()

print(T)

```

Le tri de python est **in place**. L'algorithme utilisé est [timsort](https://en.wikipedia.org/wiki/Timsort), mix entre le tri fusion et le tri par insertion. C'est un tri très efficace puisque :

> Pour un tableau de taille $n$ :
>
> * La complexité de l'algorithme timsort est $\mathcal{O}(n\ln(n))$
> * La complexité min de l'algorithme timsort est $\mathcal{O}(n)$
> * La complexité en moyenne de l'algorithme timsort est $\mathcal{O}(n\ln(n))$
>
{: .note}

## tri rapide {#tri-rapide}

Le tri rapide est un algorithme qui a été très utilisé par le passé. On le montre encore maintenant car c'est un exemple de *diviser pour régner* et, surtout, le calcul des complexités est très intéressant.

Son principe est le suivant, si on souhaite trier le tableau $T$ :

1. on choisit un élément du tableau, souvent $T[0]$
2. on sépare $T[1:]$ en deux sous tableaux
   * $T_1$ qui contient tous les éléments plus petit ou égal à $T[0]$
   * $T_2$ qui contient tous les éléments plus grand strictement à $T[0]$
3. on trie $T_1$ en $T'_1$ et $T_2$ en $T'_2$
4. on constitue le tableau initial trié : $T'_1 + [T[0]] + T'_2$

> Ecrivez cet algorithme en python
{: .a-faire}
{% details   une solution %}

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def rapide(tableau):
    if len(tableau) <= 1:
        return tableau

    pivot = tableau[0]

    tab_gauche = [tableau[i] for i in range(1, len(tableau)) if tableau[i] <= pivot]
    tab_droite = [tableau[i] for i in range(1, len(tableau)) if tableau[i] > pivot]

    return rapide(tab_gauche) + [pivot] + rapide(tab_droite)

{% endhighlight %}

On a utilisé les [list comprehension](https://python.doctor/page-comprehension-list-listes-python-cours-debutants) de python. C'est un moyen clair et efficace de générer des listes. Utilisez-les, ça rend le code plus clair et facile à écrire.

{% enddetails %}

### fonctionnement {#fonctionnement-rapide}

Tout comme pour le tri fusion, on peut tester pour deux petits tableaux, par exemple :

* `[4]`
* `[1, 2, 0, 4, 3, 98, 7]`

### preuve {#preuve-rapide}

* `tab_gauche` contient tous les éléments du tableau d'indice `> 0` et plus petit ou égal à `pivot` qui est égal à `tab[0]`
* `tab_droite` contient tous les éléments du tableau d'indice `> 0` et plus plus grand strictement à `pivot`

Si rapide fonctionne pour des tableaux de longueurs strictement plus petit que $n$, il fonctionne également pour des tableaux de longueur $n$ : le tableau rendu est le tableau des valeurs plus petite que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurrence) + `[pivot]` + le tableau des valeurs plus grande que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurrence)

Or il fonctionne pour des tableaux de longueur 0 ou 1, donc par récurrence, c'est ok.

### complexités {#complexites-rapide}

En notant $n$ la taille de la liste on a comme équation de récurrence pour la complexité $C(n)$ :

$${
C(n) = \underbrace{\mathcal{O}(n)}_{\mbox{création des tableaux}}{} + \underbrace{C(n_1) + C(n_2)}_{\mbox{récursions}}{}
}$$

Où $n_1$ est la taille du tableau de gauche et $n_2$ celle de droite ($n_1 + n_2 = n-1$). Pour trouver $n_1$ et $n_2$, il faut  résoudre l'équation :

$${
C(n) = \mathcal{O}(n) + \max_{0 \leq i < n}(C(i) + C(n-i-1))
}$$

On va montrer que :

> Pour trier un tableau de longueur $n$, les complexités de `rapide` sont :
>
> * la complexité (maximale) est $\mathcal{O}(n^2)$,
> * la complexité en moyenne est $\mathcal{O}(n\ln (n))$,
> * la complexité minimale est $\mathcal{O}(n\ln (n))$,
>
{: .note}

#### complexité (maximale) du tri rapide

**Intuitivement**, ce cas va arriver si un des deux tableaux est toujours vide. Par exemple lorsque le tableau est déjà trié. Dans ce cas là, l'autre tableau est de taille $n-1$, ce qui donne une complexité de :

$$C_{\mbox{trié}}(n) = \mathcal{O}(n) + C(0) +  C_{\mbox{trié}}(n-1)$$

Donc :

$$
\begin{array}{lcl}
C_{\mbox{trié}}(n) &=& \mathcal{O}(n) + C(0) + C_{\mbox{trié}}(n-1)\\
&=& \mathcal{O}(n) + \mathcal{O}(1) + C_{\mbox{trié}}(n-1)\\
&=& \mathcal{O}(n) + C_{\mbox{trié}}(n-1)\\
&=& \mathcal{O}(n) + \mathcal{O}(n-1) + C_{\mbox{trié}}(n-2)\\
&=& ...\\
&=& \sum_{i=2}^{n}\mathcal{O}(i) + C_{\mbox{trié}}(1)\\
&=& \sum_{i=2}^{n}\mathcal{O}(i) + \mathcal{O}(1)\\
&=& \mathcal{O}(\sum_{i=1}^{n}i)\\
&=& \mathcal{O}(n^2)\\
\end{array}
$$

Finalement, si le tableau de taille $n$ en entrée est trié l'algorithme du tri rapide va effectuer $\mathcal{O}(n^2)$ opérations. En notant $C(n)$ la complexité de l'algorithme du tri rapide, on alors :

$$
\begin{array}{lcl}
C_{\mbox{trié}}(n) &\leq& C(n)\\
\mathcal{O}(n^2) &\leq& C(n)\\
\end{array}
$$

{% details **Pour finir la preuve de façon formelle** il reste à démontrer que $C(n) \leq \mathcal{O}(n^2)$. %}
Faisons le par récurrence. Notre hypothèse de récurrence est : il existe $k$ tel que $C(n) \leq k \cdot n^2$
Cette hypothèse est trivialement vraie pour $n=1$ et supposons la vraie pour $n-1$. Examinons le cas $n$ :

$$
\begin{array}{lcll}
C(n) & = & \mathcal{O}(n) + \max_{0 \leq i < n}(C(i) + C(n-i-1))&\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot i^2 + k\cdot(n-i-1)^2)&\mbox{par hypothèse de récurrence}\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot(i + n-i-1)^2)&\mbox{car } a^2+b^2 \leq (a+b)^2\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot(n-1)^2)&\\
& \leq & \mathcal{O}(n) + k\cdot(n-1)^2&\\
& \leq & \mathcal{O}(n) + k\cdot n^2 -k(2n-1)&\\
\end{array}
$$

Comme une fonction $f$ en $\mathcal{O}(n)$ est telle que pour tout $N \geq N_0$ on a $f(N) \leq k'\cdot N$, On peut prendre $k'' = \max(\max_{1\leq N \leq N_0}f(N), k, k')$ et alors :

$$C(n) \leq  k''\cdot n^2$$

Notre hypothèse est démontrée. Au final on a l'encadrement :

$$\mathcal{O}(n^2) \leq C(n) \leq \mathcal{O}(n^2)$$

{% enddetails %}

> La complexité du tri rapide pour un tableau de taille $n$ est $\mathcal{O}(n^2)$
{: .note}

#### complexité minimale du tri rapide

**intuitivement**, si l'on découpe notre tableau de façon non équilibrée, une branche de la récursion va faire plus d'opérations que $C(n/2)$. La complexité minimale est ainsi atteinte lorsque l'on coupe notre tableau exactement en 2.

Dans ce cas là, on a l'équation de récurrence : $C(n) = \mathcal{O}(n) + 2 \cdot C(\frac{n}{2})$ qui est la même que celle du tri fusion. La complexité minimale du tri `rapide` est inférieure à $\mathcal{O}(n\ln(n))$.

Pour finir la preuve, remarquons que $C(k) \geq k$ : la courbe de $C(n)$ est plus grande qu'une droite. On en conclut que $C(\frac{(k-1)n}{k})$ est au dessus de la droite liant $C(\frac{n}{k})$ et $C(\frac{n}{2})$, pour $k >2$ :

![droite]({{ "/assets/cours/algorithmie/etude-tris-1.png" | relative_url }}){:style="margin: auto;display: block;"}

De là, $C(\frac{n}{2})$ est en-dessous de la droite liant $C(\frac{n}{k})$ à $C(\frac{(k-1)n}{k})$ :

![courbe C(n)]({{ "/assets/cours/algorithmie/etude-tris-2.png" | relative_url }}){:style="margin: auto;display: block;"}

On a donc $C(\frac{n}{2}) \leq \frac{1}{2}(C(\frac{n}{k}) + C(\frac{(k-1)n}{k}))$ (le rond vide est au-desus du rond plein) pour tout $k > 2$. Il est donc **toujours** plus avantageux de découper le tableau en 2 parties égales.

> La complexité **minimale** du tri rapide pour un tableau de taille $n$ est $\mathcal{O}(n\ln(n))$
{: .note}

#### complexité en moyenne du tri rapide

**Intuitivement**, on utilise l'argument utilisé pour calculer la complexité en moyenne du [tri par insertion](#complexites-insertion). Si les données sont aléatoires la moitié de `tableau[1:]` est plus grande que `tableau[0]`. De là, en moyenne, on va toujours couper le tableau en 2 parties (plus ou moins) égales.

Si l'on coupe toujours au milieu on a alors la même équation que pour la complexité minimale : $C(n) = \mathcal{O}(n) + 2 \cdot C(\frac{n}{2})$, ce qui donne une complexité de $\mathcal{O}(n\ln(n))$.

**De façon formelle**, il faut résoudre l'équation :

$${
C_{\mbox{moy}}(n) = \mathcal{O}(n) + \sum_{0 \leq i < n}p_i(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

où $p_i$ est la probabilité que le pivot soit le $i+1$ plus petit élément du tableau.

{% details **résolution** de l'équation qui montre que $C_{\mbox{moy}}(n) = \mathcal{O}(n\ln(n))$ %}
Pour éviter de nous trimballer des $\mathcal{O}(n)$ partout, on va considérer que l'on y effectue $K\cdot n$ opérations où $K$ est une constante. On peut alors écrire :

$${
C_{\mbox{moy}}(n) = K\cdot n + \sum_{0 \leq i < n}p_i(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

De plus on va considérer que nos données sont équiprobables, c'est à dire que le pivot a la même probabilité d'être le $i$ ou le $j$ ème plus petit élément du tableau : $p_i = \frac{1}{n}$. On a alors à résoudre :

$${
C_{\mbox{moy}}(n) = K\cdot n + \frac{1}{n}\sum_{0 \leq i < n}(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

Comme :

* $\sum_{0 \leq i < n}C_{\mbox{moy}}(i) = \sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)$
* $\sum_{0 \leq i < n}C_{\mbox{moy}}(n-i-1) = \sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)$

On a :

$${
C_{\mbox{moy}}(n) = K\cdot n + \frac{2}{n}\sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)
}$$

Il va maintenant y avoir 2 astuces coup sur coup. La première astuce est de considérer l'équation $n\cdot C_{\mbox{moy}}(n) - (n-1)\cdot C_{\mbox{moy}}(n-1)$ qui va nous permettre d'éliminer la somme :

$$
\begin{array}{lcl}
n\cdot C_{\mbox{moy}}(n) - (n-1)\cdot C_{\mbox{moy}}(n-1) & = & K\cdot n^2 +2\sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)\\
&&- K\cdot (n-1)^2 - 2\sum_{1 \leq i \leq n-1}C_{\mbox{moy}}(i-1)\\
&=& K(n^2 - (n-1)^2) + 2\cdot C_{\mbox{moy}}(n-1)\\
&=& K(2n - 1) + 2\cdot C_{\mbox{moy}}(n-1)\\
\end{array}
$$

On en déduit :

$$
n\cdot C_{\mbox{moy}}(n) = K(2n - 1) + (n+1)\cdot C_{\mbox{moy}}(n-1)
$$

Et maintenant la seconde astuce : on divise l'équation ci-dessus par $n(n+1)$ pour obtenir un terme générique identique des deux côtés de l'équation :

$$
\frac{C_{\mbox{moy}}(n)}{n+1}=\frac{C_{\mbox{moy}}(n-1)}{n} + K\cdot\frac{2n - 1}{n(n+1)}
$$

On peut alors poser $A(n) = \frac{C_{\mbox{moy}}(n)}{n+1}$ et on doit maintenant résoudre :

$$
A(n) = A(n-1) + K\cdot\frac{2n - 1}{n(n+1)}
$$

Ce qui donne :

$$
\begin{array}{lcl}
A(n) &=& A(n-1) + K\cdot\frac{2n - 1}{n(n+1)}\\
&=& A(n-2) + K\cdot\frac{2(n-1) - 1}{(n-1)(n)} +  K\cdot\frac{2n - 1}{n(n+1)}\\
&=& \dots \\
&=&K \sum_{i=1}^{n}\frac{2i-1}{i(i+1)} + A(0)\\
&=&K \sum_{i=1}^{n}\frac{2}{(i+1)} - K \sum_{i=1}^{n}\frac{1}{i(i+1)} + A(0)\\
\end{array}
$$

On peut facilement montrer (par récurrence) que $\sum_{i=1}^{n}\frac{1}{i(i+1)} = \frac{n}{n+1} \leq 1$ et donc que :

$$
\begin{array}{lcl}
A(n) &=& 2K\sum_{i=1}^{n}\frac{1}{(i+1)} + \mathcal{O}(1)\\
&=& 2K\sum_{i=1}^{n}\frac{1}{i} - 2K + \mathcal{O}(1)\\
&=& 2K\sum_{i=1}^{n}\frac{1}{i} + \mathcal{O}(1)\\
&=& \mathcal{O}(\sum_{i=1}^{n}\frac{1}{i})\\
\end{array}
$$

La suite $A(n)$ se comporte comme un $\mathcal{O}(H(n)$ où $H(n) = \sum_{i=1}^{n}\frac{1}{i}$.

Cette fonction est connue, elle s'appelle la [série harmonique](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique),
et est [équivalente](https://fr.wikipedia.org/wiki/%C3%89quivalent) à $\ln(n)$ lorsque $n$ tend vers $+\infty$.  On a alors que $\mathcal{O}(H(n)) = \mathcal{O}(\ln(n))$, et de là :

$$
A(n) = \mathcal{O}(\ln(n))
$$

En revenant aux $C_{\mbox{moy}}(n) = n\cdot A(n)$ :

$$
C_{\mbox{moy}}(n) = \mathcal{O}(n\ln(n))
$$

ouf.
{% enddetails %}

> La complexité **en moyenne** du tri rapide pour un tableau de taille $n$ est $\mathcal{O}(n\ln(n))$
{: .note}

### conclusion

Le tri rapide a :

* une complexité moyenne qui vaut sa complexité minimale et qui est $\mathcal{O}(n \ln(n))$, donc la meilleur possible
* il très rapide pour les tableaux en désordre et très lent pour les tableaux déjà triés.

C'est donc *rigolo* :

> Commencer par mélanger un tableau pour le trier avec `rapide` ensuite est plus rapide en moyenne que de le trier directement.
{: .note}
