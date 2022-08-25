---
layout: layout/post.njk 
title: "Algorithmes et fonctions"

eleventyNavigation:
  key: "Algorithmes et fonctions"
  parent: "Théorie"
---

{% prerequis "**Prérequis** :" %}

* [pseudo-code](../../algorithme/pseudo-code)

{% endprerequis %}

> TBD : fix fonction non calculable.

<!-- début résumé -->

Nous allons dans cette partie, sans aucun présupposé sur les instructions à utiliser, montrer que l'on peut préciser ce qu'est un algorithme sous la forme de fonctions, juste en utilisant la finitude de sa description.

<!-- end résumé -->

Un algorithme, [on l'a vu](../../algorithme/définition#algorithme), c'est :

{% note %}
Un ***algorithme*** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{% endnote %}

Ce qu'il faudra retenir de cette partie :

* un algorithme peut-être vue une fonction prenant **un** mot composé de 0 et de 1 en entrée et qui donne un mot composé de 0 et de 1 en sortie
* que l'on ne peut pas manipuler de réels directement que des approximations
* que toutes les fonctions prenant **un** mot composé de 0 et de 1 en entrée et qui donne un mot composé de 0 et de 1 en sortie ne peuvent pas être calculées par un algorithme (et savoir pourquoi)

## Objets et instructions d'un algorithme

Le terme **fini** de la définition d'un algorithme est crucial : pour qu'un humain comprenne, et surtout puisse agir, il ne faut pas qu'il y ait un nombre infini de choses à regarder (chaque chose à faire prend un temps de réflexion non nul, une instruction contenant un nombre infini n'est humainement pas réalisable).

### Instructions d'un algorithme

On en déduit la définition (très générale) d'une instruction d'un algorithme :

{% note %}
Une **instruction** d'un algorithme est une règle définie par un nombre **fini** de symboles.
{% endnote %}

Fini ne veut pas dire petit nombre. Un algorithme peut utiliser des nombres entiers aussi grand qu'il
le veut, du moment qu'ils ne soient pas infini.

### Objet manipulables

Puisque l'on a le droit de ne manipuler que des choses finies, un algorithme ne peut manipuler que des [mots d'un alphabet fini](https://fr.wikipedia.org/wiki/Mot_(math%C3%A9matiques)). La conséquence fondamentale de ceci est que :

{% note "**un algorithme ne peut pas manipuler de nombres réels**" %}

On ne peut considérer un réel que comme une abstraction (un symbole particulier) ou une approximation (on ne considère qu'un nombre fini de décimales).
{% endnote %}

Prenons $\pi$ par exemple. Il existe des algorithmes qui [calculent les décimales de pi](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80#Calcul_de_la_n-i%C3%A8me_d%C3%A9cimale_de_%CF%80), mais on ne pourra jamais écrire que le nombre $\pi$ est le résultat d'un algorithme, puisque l'algorithme doit s'arrêter : on aura qu'un nombre fini de décimales, donc on aura pas $\pi$.

On ne pourra considérer $\pi$ que de deux manières :

* soit comme un symbole et l'utiliser pour faire des opérations sur lui (comme $2 \cdot \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaître sa valeur
* soit comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations.

Ce n'est pas bien grave en général puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) : considérer les réels en [notation scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique) en se fixant une précision ne gène pas les calculs physiques.

{% info %}
Faites tout de même attention car parfois, c'est problématique. Pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon), certes, mais aussi lorsque l'on prend l'inverse de choses très petites qui du coup deviennent très grandes. Ce sont des problèmes dit de [stabilité numérique](https://fr.wikipedia.org/wiki/Stabilit%C3%A9_num%C3%A9rique).
{% endinfo %}

En conclusion :

{% note "Les objets manipulables par un algorithme sont uniquement :" %}

* les entiers finis
* les approximations finies de réels
* les chaînes de caractères

{% endnote %}

## Algorithmes et fonctions

Un algorithme, représenté par sa description, a des entrées et une sortie : c'est une fonction. D'après ce qui précède, on a donc :

{% note %}
Un ***algorithme*** à $p$ entrées, dont $q$ entrées entières, $r$ entrées approximation des réels et $s$ chaînes de caractères est une fonction de :

$$f: \mathbb{N}^{q} \times R^r \times C^s \rightarrow \mathbb{N} \cup R \cup C$$

où $\mathbb{N}$ est l'ensemble des entiers, $R$ l'ensemble des approximations de réels et $C$ l'ensemble des chaînes de caractères.
{% endnote %}

On a pas trop dit grand chose pour l'instant. On a fait que re-écrire ce qu'on savait déjà sous la forme de fonctions. On va montrer qu'on peut faire bien mieux en montrant qu'un algorithme est une fonction de $\mathbb{N}$ (les entiers) dans $\mathbb{N}$.

Cela nous permettra de montrer qu'un algorithme ne peut pas **tout** calculer : il existe des fonctions de $\mathbb{N}$ dans $\mathbb{N}$ qu'aucun ordinateur ne pourra calculer (trouver des fonctions non calculables par un ordinateur n'est pas une tâche simple cependant. Il nous faudra un peut plus de connaissances pour en exhiber).

{% info %}
Dans la suite de cette partie on utilisera les [bijections](https://fr.wikipedia.org/wiki/Bijection) entre ensembles. Si deux ensembles sont en bijections on peut passer de l'un à autre (et réciproquement) sans soucis, les deux ensembles sont équivalents.

On peut utiliser l'un ou l'autre de façon équivalente.
{% endinfo %}

### Fonctions à plusieurs paramètres entiers { #fonction-plusieurs-entier }

Les paramètres d'un algorithme peuvent tous être représentés par des entiers :

* des entiers finis : c'est clair.
* des approximations finies de réels : on peut utiliser la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754). Par exemple 3.1415 en codage IEEE 754 sur 32 bits correspond à l'entier binaire : `01000000010010010000111001010110` (j'ai utilisé [un convertisseur](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
* des chaînes de caractères : que l'on peut représenter comme un entier. Par exemple la chaîne de caractères "Yop !" correspond en utf-8 au nombre hexadécimal 0x596F702021 (là aussi, j'ai utilisé [un convertisseur](http://hapax.qc.ca/conversion.fr.html)).

On peut donc reformuler notre assertion précédente en unifiant les paramètres (on les recode tous sous la forme d'entiers) :

{% note %}
Un ***algorithme*** est une fonction de $p$ paramètres entiers et qui rend un entier.

$$f: \mathbb{N}^p \rightarrow \mathbb{N}$$

{% endnote %}

C'est bien mieux mais on sépare encore les algorithmes par leur nombre de paramètres. Allons plus loin.

### Fonctions à un paramètre entier { #fonction-un-entier }

Démontrons que tout élément de $\mathbb{N}^p$ peut être représenté par un entier. Pour ce faire on exhibera une bijection entre $\mathbb{N}^p$ ($p>1$) et $\mathbb{N}$.

{% info %}
C'est un résultat que l'on doit au mathématicien [Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor)
{% endinfo %}

Commençons par démontrer que $\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection :

{% note "**Théorème**" %}
$\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection.
{% endnote %}
{% details "preuve" %}
Remarquons que tout élément de $\mathbb{N}^2$ est un point du plan :

![point de n2 dans le plan](n2_dans_plan.png)

On peut les parcourir en suivant les diagonales :

![point de n2 dans le plan](n2_dans_n.png)

On chemine alors comme ça :

1. $(0, 0)$
2. $(1, 0)$
3. $(0, 1)$
4. $(2, 0)$
5. $(1, 1)$
6. $(0, 2)$
7. $(3, 0)$
8. $(2, 1)$
9. $(1, 2)$
10. $(0, 3)$
11. $(4, 0)$
12. ...

Et on associe à un entier $(x, y)$ son ordre de cheminement $O((x, y))$ (par exemple $O((2, 1)) = 8$).

Ce cheminement est clairement une bijection.

On peut donc aussi associer un unique entier à tout couple d'entiers avec $O^{-1}$ ($O^{-1}(6) = (0, 2)$ par exemple).

{% enddetails %}

La bijection du théorème peut facilement se décrire par un pseudo-code.

{% exercice %}
Écrivez le pseudo-code de la fonction $O^{-1}$ qui associe un couple $(x, y)$ unique à un entier $i$ passé en paramètre.
{% endexercice %}
{% details "solution" %}

```text
Nom : O^{-1}
Entrée : un entier i
Sortie : un couple (x, y) d'entiers 
Programme :
    x = y = 0
    k = 0
    tant que k < i:
        si x == 0: 
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour (x, y)
```

{% enddetails %}

À partir du pseudo-code de $O^{-1}$, il est facile d’écrire le pseudo code de $O$.

{% exercice %}
Écrivez le pseudo-code de la fonction $O$ qui associe un entier $i$ unique à un couple $(x, y)$  passé en paramètre.
{% endexercice %}
{% details "solution" %}

```text
Nom : O
Entrée :  un couple (u, v) d'entiers
Sortie : un entier i
Programme :
    x = y = 0
    i = 0
    tant que (u, v) ≠ (x, y):
        i = i + 1
        si x == 0: 
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour i
```

{% enddetails %}

Le théorème admet comme corollaire immédiat que :

{% note "**corollaire**" %}
$\mathbb{N}^{p}$ et $\mathbb{N}^{p-1}$ sont en bijection, pour tout entier $p \geq 2$.
{% endnote %}
{% details "preuve" %}

Pour $p=2$ la fonction $O$ est une bijection.

Pour $p>2$, on construit la fonction $O_p: \mathbb{N}^{p} \rightarrow \mathbb{N}^{p-1}$ telle que :

$$
O_p(x_1, \dots, x_p) =(O(x_1, x_2), x_3 \dots, x_p)
$$

La fonction $O_p$ est clairement une bijection puisque $O$ en est une.

{% enddetails %}

Et donc par une récurrence immédiate :

{% note "**Théorème**" %}
$\mathbb{N}^p$ et $\mathbb{N}$ sont en bijection, pour tout $p \geq 1$
{% endnote %}

{% exercice %}
En utilisant la fonction $O$, donnez le pseudo-code de la fonction $OP$ qui associe un entier unique $i$ à un $p$-uplet $(x_1, \dots, x_p)$
{% endexercice %}
{% details "solution" %}

```text
Nom : OP
Entrée : x : un p-uplet
Sortie : i un entier
Programme :

    i = O(x[1], x[2])
    de k = 3 à p:
        i = O(i, x[k])

    Retour i
```

{% enddetails %}

{% exercice %}
En utilisant la fonction $O^{-1}$, donnez le pseudo-code de la fonction $OP^{-1}$ qui associe un $p$-uplet unique $(x_1, \dots, x_p)$ à un entier $i$
{% endexercice %}
{% details "solution" %}

```text
Nom : OP^{-1}
Entrée : un entier i
Sortie : un p-uplet x
Programme :

    de k=p à 2:
       i, x[k] = O^{-1}(i)
    x[1] = i
    
    Retour x
```

{% enddetails %}

La bijection entre $\mathbb{N}^p$ et $\mathbb{N}$ nous permet de dire que l'on peut indifféremment utiliser $\mathbb{N}^p$  ou $\mathbb{N}$ sans perte de généralité (on utilise la bijection pour passer de l'un à l'autre). De là, on peut dire que :

{% note %}
Un ***algorithme*** est une fonction de :

$$f: \mathbb{N} \rightarrow \mathbb{N}$$

{% endnote %}

### Forme ultime d'une algorithme

Vous allez rire, on peut encore simplifier.

Pour l'instant, on sait qu'un algorithme est une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$. Elle associe un entier à un autre. Cette fonction est alors équivalente à la fonction $f'$ ci-dessous :

$$
f'(n, m) = \left\\\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

On en conclut qu'un algorithme est une fonction de :

$$f: \mathbb{N}^2 \rightarrow \\{0, 1 \\}$$

Et comme $\mathbb{N}^2$ est en bijection avec $\mathbb{N}$ :

{% note %}
Un ***algorithme*** est une fonction de :

$$f: \mathbb{N} \rightarrow \\{0, 1 \\}$$

{% endnote %}

En remarquant que tout entier peut s'écrire sous sa [notation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire), qui peut être vue comme une suite finie de 0 et de 1 il existe une bijection entre $\mathbb{N}$ et l'ensemble des suite finies de  $0$ et de $1$. On en conclut que la forme ultime d'un algorithme est :

{% note %}
Un ***algorithme*** est une fonction de :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies d'éléments de $\\{0, 1\\}$.
{% endnote %}

## Que calcule-t-on ?

Un algorithme est une fonction de $\mathbb{N}$ dans $\\{0, 1 \\}$, mais quelles sont les fonctions qui sont des algorithmes ?

Nous allons répondre indirectement à cette question en montrant que toutes les fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ ne peuvent être écrite par des algorithmes.

On l'a vu il n'existe qu'un [nombre dénombrable d'algorithme](../../algorithme/définition#nb-dénombrable-algorithmes), nous allons montrer qu'il y a strictement plus de fonction de $\mathbb{N}$ dans $\\{0, 1 \\}$ que de nombres entiers.

Commençons par compter le nombre de fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ :

{% note "**Proposition**" %}
Il y a autant de fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ que de sous-ensembles de $\mathbb{N}$
{% endnote %}
{% details "preuve" %}
Une fonction $f: \mathbb{N} \rightarrow \\{0, 1 \\}$ est entièrement caractérisée par $f^{-1}(\\{1\\})$.

La fonction qui associe $f^{-1}(\\{1\\})$ à $f$ est ainsi une bijection.

{% enddetails %}

Puis montrons qu'il y a toujours strictement plus de sous-ensembles d'un ensemble que d'éléments de l'ensemble. Avant de passer au théorème, un petit exemple pour vous convaincre.

Si on prend un ensemble $E$ fini, il est clair qu'il y a strictement plus de sous-ensembles de $E$ que d'éléments dans $E$. Par exemple, si on prend l'ensemble $\\{1, 2, 3\\}$. Les différents sous-ensembles qu'on peut faire sont :

* $\emptyset$
* $\\{1\\}$
* $\\{2\\}$
* $\\{3\\}$
* $\\{1, 2\\}$
* $\\{1, 3\\}$
* $\\{2, 3\\}$
* $\\{1, 2, 3\\}$

Il y a 8 sous-ensemble d'un ensemble à 3 éléments. Ceci est encore vrai si les ensembles sont infinis... C'est le [**Théorème de Cantor**](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cantor) :

{% note "**Théorème**" %}
Pour tout ensemble $E$ (même infini), il y a strictement plus de sous-ensembles de $E$ que d'éléments de $E$
{% endnote %}
{% details  "preuve" %}

La preuve du Théorème de Cantor repose sur le fait que pour toute fonction $f$ qui associe à un élément de $E$ un sous-ensemble de $E$, il existe des éléments qui n'ont pas d'antécédent.

L'ensemble $D = \\{x \in E \vert x \notin f(x)\\}$ est un de ceux là. En effet, s'il en avait un, disons $y$, on aurait $f(y) = D$ et alors :

* $y \notin D$ car s'il y était alors $y \notin f(y)$ ce qui est incohérent avec le fait que $f(y) = D$
* $y \in D$ car s'il n'y était pas alors $y \in f(y)$ ce qui est incohérent avec le fait que $f(y) = D$

Bref, $y$ n'existe pas.

On en conclut qu'il existe des sous-ensembles de $E$ qui ne sont pas des images de $f$ : ce n'est pas une [surjection](https://fr.wikipedia.org/wiki/Surjection). Comme $f$ a été prise au hasard, ça signifie que pour toute fonction il existera des sous-ensembles de $E$ qui ne seront pas atteints : il y a strictement plus de sous ensembles de $E$ que d'éléments de $E$.

{% enddetails %}
{% info %}
Ceci montre qu'il y a des infinis plus grand que d'autre et qu'il y en a autant qu'on veut. Le nombre d'entiers (noté $\aleph_0$) est strictement plus petit que le nombre de ses sous-ensembles (noté $\aleph_1$), lui même strictement plus petit que le nombre de sous-ensemble de l'ensemble des sous-ensembles de d'entiers (noté $\aleph_2) qui est plus petit le nombre de sous-ensemble de l'ensemble de l'ensemble des sous-ensemble de l'ensemble des sous-ensembles de d'entiers. Et ainsi de suite...

{% endinfo %}

En utilisant le théorème de Cantor et le fait qu'il y ait autant de fonction de $\mathbb{N}$ dans $\\{0, 1 \\}$ que de sous-ensembles de $\mathbb{N}$ on en déduit donc :

{% note %}
Il y a strictement plus de fonctions $\mathbb{N}$ dans $\\{0, 1 \\}$ que d'entiers.
{% endnote %}

Et donc :

{% note %}
Il existe des fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ qui ne sont pas des algorithmes.
{% endnote %}

## Nombre de fonctions { #r-et-n }

Je ne saurais vous laisser dans l'ignorance du nombre de fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$, c'est à dire du nombre de sous-ensembles de $\mathbb{N}$ :

{% note "**Théorème**" %}
il y a autant de de sous-ensembles de $\mathbb{N}$ que de nombres réels entre 0 et 1 (exclus).
{% endnote %}
{% details "preuve" %}
On va commencer par montrer qu'il y en a moins puis qu'il y en a plus pour en conclure finalement qu'il y en a donc autant.

Prenons un sous-ensemble $A$ de $\mathbb{N}$. On peut ranger ses éléments par ordre croissant et concaténer leurs représentations décimales en une chaîne de caractères (possiblement infini) contenant uniquement des chiffres. On concatène cette chaîne à "0." pour obtenir la représentation décimale d'un réel.

Exemple : Si $A = \\{0, 1, 4, 42\\}$ on lui associe le réel $R(A) = 0.01442$

Il est clair que cette opération est une injection, c'est à dire que sir $A \neq A'$, on a bien $R(A) \neq R(A')$ et donc que : Il y a plus d'éléments dans $]0, 1[$ que de sous-ensembles de $\mathbb{N}$

Prenons maintenant un réel $r$ dans l'intervalle $]0, 1[$. Son écriture décimale s'écrit : $0.a_1a_2\dots a_i\dots$ de longueur infinie, avec possiblement des 0 à la fin. On peut lui associer le sous ensemble infini : $S(r) = \\{a_i + 10 \cdot i \mid i > 0 \\}$.
Il est clair que cette opération est une injection, c'est à dire que sir $r \neq r'$, on a bien $S(r) \neq S(r')$ et donc que :

Il y a plus de sous-ensembles de $\mathbb{N}$ que d'éléments dans $]0, 1[$

Il y a à la fois plus et moins d'éléments dans $]0, 1[$ que de sous ensembles de $\mathbb{N}$, donc :

Il y a autant de sous-ensembles de $\mathbb{N}$ que d'éléments dans $]0, 1[$

En remarquant que la fonction $f(x) = \tan(\frac{x-1}{2}\cdot \pi)$ est une bijection de $]0, 1[$ dans $]-\infty, +\infty[$, on en conclut qui'l y a autant de réels dans $]0, 1[$ que dans $]-\infty, +\infty[$ et donc :

Il y a autant de sous-ensembles de $\mathbb{N}$ que de réels
{% enddetails %}


