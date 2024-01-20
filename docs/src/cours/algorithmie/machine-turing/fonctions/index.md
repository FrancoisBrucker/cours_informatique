---
layout: layout/post.njk 
title: "Fonctions et machines de Turing"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Le problème de l'arrêt de la machine de Turing et donc de tout pseudo-code est insoluble. De plus, dans la définition d'un [algorithme](../../définition/#algorithme){.interne} on suppose stipule qu'il doit, à partir d'une entrée, rendre un calcul en un temps fini.

On a donc l'habitude de ne considérer que les pseudo-codes qui se terminent quelque soit l'entrée. Ces pseudo-codes prennent une entrée qui est une suite de `0` et de `1` et rendent une suite de `0` et de `1` : ce sont des fonctions.

{% note %}
Une machine de Turing qui s'arrête quelque soit l'entrée est une fonction :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies d'éléments de $\\{0, 1\\}$.
{% endnote %}

Pour garantir que toutes les entrées et sorites sont possibles, on peut utiliser une [machine de Turing `01#`](../définitions-alternatives/#MT-01#){.interne} qui rend plus simple la gestion des entrées/sortie sans perte de généralité.

{% info %}
Lorsque nous parlons de Machine de Turing, c'est equivalent à tout pseudo-code et donc (sous l'hypothèse de la thèse de Church-Turing) tout programme.
{% endinfo %}

## Décideur

{% note "**Définition**" %}
Un ***décideur*** $D$ est une machine de Turing qui s'arrête quelque soit l'entrée et rend soit :

* `0` on dit que la sortie est *fausse*
* `1` on dit que la sortie est *vraie*

On dit qu'un L'ensemble des entrées $\mathcal{L}(D) = \\{ E \mid D(E) == 1 \\}$ est appelé ***language*** de $D$.
{% endnote %}

Un décideur est une machine qui dit oui ou non et permet de *reconnaître* certains mots (un mot est une suite finie de caractères d'un alphabet) de $\\{0, 1\\}^\star$ :

{% note "**Définition**" %}
Un ensemble de mots $L \subseteq \\{0, 1\\}^\star$ est ***décidable*** s'il existe un **décideur** qui répond *vrai* si l'entrée est dans $L$ et *faux* sinon.
{% endnote %}

Nous verrons que la définition précédente va être fondamentale lorsque l'on voudra définir ce qu'est un *problème*.

### Équivalence entre décideur et Machines de Turing

Un décideur semble être un cas particulier de machine mais, comme presque toujours avec les machine de Turing, il n'est est rien.

{% note "**Théorème**" %}
On peut simuler une machine de Turing qui s'arrête tout le temps par un décideur.

Les notions de décideur et de machine de Turing sont donc équivalentes.
{% endnote %}
{% details "preuve" %}
Soit $M$ une machine de Turing et on considère pour toute entrée $E$, le couple $(E, M(E))$. Ce couple peut être écrit sous la forme d'un mot de l'alphabet $\\{0, 1\\}$ en utilisant la même technique que l'on a utilisé pour convertir l'[entrée d'une machine à de 2 rubans en une entrée pour une machine à 1 ruban](../définitions-alternatives/#rubans-equivalence-entrée){.interne}. Soit alors le décideur $D$ de pseudo code :

```
def D(E):
    Si E peut être décodée en (A, B) 
        alors:
            exécuter M(A) et stocker sa sortie dans S
            Si S == B alors: rendre 1
                      sinon: rendre 0
        sinon:
            rendre 0
```

Le langage reconnu par $D$ est exactement composé des couples $(E, M(E))$.

L'exécution de la machine de Turing $M(E)$ est alors équivalente à exécuter $D$ avec tous les mots $E'$ de taille croissantes jusqu'à arriver à un mot $(E, E')$ reconnu par $D$.
{% enddetails %}

### Machine de Turing et fonctions

La partie précédente a montré que :

{% note %}
Une machine de Turing qui s'arrête quelque soit l'entrée est une fonction :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies d'éléments de $\\{0, 1\\}$.
{% endnote %}

En remarquant que tout entier peut s'écrire sous sa [notation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire), qui peut être vue comme une suite finie de 0 et de 1 il existe une bijection entre $\mathbb{N}$ et l'ensemble des suite finies de  $0$ et de $1$. On en conclut que  :

{% note %}
Une machine de Turing qui s'arrête quelque soit l'entrée est une fonction :

$$f: \mathbb{N} \rightarrow \\{0, 1 \\}$$

{% endnote %}

Enfin, comme une machine de Turing est équivalente aux mots qu'elle reconnaît :

{% note %}
Une machine de Turing $f: \mathbb{N} \mapsto \\{0, 1 \\}$ qui s'arrête quelque soit l'entrée est équivalente à son ***langage***. C'est le sous-ensemble de $2^\mathbb{N}$ valant :

$$\\{n \mid f(n) = 1\\}$$

{% endnote %}

## Que calcule-t-on ?

Un algorithme et une machine de Turing sont des fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$, mais quelles sont les fonctions qui sont des algorithmes ?

Nous allons répondre indirectement à cette question en montrant que toutes les fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ ne peuvent être écrite par des algorithmes.

On l'a vu il n'existe qu'un [nombre dénombrable d'algorithme](../../algorithme/définition#nb-dénombrable-algorithmes){.interne}, nous allons montrer qu'il y a strictement plus de fonction de $\mathbb{N}$ dans $\\{0, 1 \\}$ que de nombres entiers.

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
Ceci montre qu'il y a des infinis plus grand que d'autre et qu'il y en a autant qu'on veut. Le nombre d'entiers (noté $\aleph_0$) est strictement plus petit que le nombre de ses sous-ensembles (noté $\aleph_1$), lui même strictement plus petit que le nombre de sous-ensemble de l'ensemble des sous-ensembles de d'entiers (noté $\aleph_2$) qui est plus petit le nombre de sous-ensemble de l'ensemble de l'ensemble des sous-ensemble de l'ensemble des sous-ensembles de d'entiers. Et ainsi de suite...

{% endinfo %}

En utilisant le théorème de Cantor et le fait qu'il y ait autant de fonction de $\mathbb{N}$ dans $\\{0, 1 \\}$ que de sous-ensembles de $\mathbb{N}$ on en déduit donc :

{% note %}
Il y a strictement plus de fonctions $\mathbb{N}$ dans $\\{0, 1 \\}$ que d'entiers.
{% endnote %}

Et donc :

{% note %}
Il existe des fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$ qui ne sont pas des algorithmes. Ces fonctions sont dites ***non calculables***.
{% endnote %}

Tout comme trouver un nombre réel non calculable est compliqué, il en est de même avec les fonctions non calculables.

## <span id="r-et-n"></span> Nombre de fonctions

Je ne saurais vous laisser dans l'ignorance du nombre de fonctions de $\mathbb{N}$ dans $\\{0, 1 \\}$, c'est à dire du nombre de sous-ensembles de $\mathbb{N}$ :

{% note "**Théorème**" %}
il y a autant de de sous-ensembles de $\mathbb{N}$ que de nombres réels de $[0, 1[$.
{% endnote %}
{% details "preuve" %}
On va commencer par montrer qu'il y en a moins puis qu'il y en a plus pour en conclure qu'il y en a donc autant.

Prenons un sous-ensemble $A$ de $\mathbb{N}$. On peut ranger ses éléments par ordre croissant et concaténer leurs représentations décimales en une chaîne de caractères (possiblement infini) contenant uniquement des chiffres. On concatène cette chaîne à "0." pour obtenir la représentation décimale d'un réel.

Exemple : Si $A = \\{0, 1, 4, 42\\}$ on lui associe le réel $R(A) = 0.01442$

Il est clair que cette opération est une injection, c'est à dire que sir $A \neq A'$, on a bien $R(A) \neq R(A')$ et donc que : Il y a plus d'éléments dans $[0, 1[$ que de sous-ensembles de $\mathbb{N}$

Prenons maintenant un réel $r$ dans l'intervalle $[0, 1[$. Son écriture décimale s'écrit : $0.a_1a_2\dots a_i\dots$ de longueur infinie, avec possiblement des 0 à la fin. On peut lui associer le sous ensemble infini : $S(r) = \\{a_i + 10 \cdot i \mid i > 0 \\}$.
Il est clair que cette opération est une injection, c'est à dire que sir $r \neq r'$, on a bien $S(r) \neq S(r')$ et donc que :

Il y a plus de sous-ensembles de $\mathbb{N}$ que d'éléments dans $[0, 1[$
{% enddetails %}

## Calculabilité et décidabilité

Décidabilité et calculabilité sont les deux faces d'une même pièce :

{% note "**proposition**" %}
Si une fonction $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est **calculable** alors $\\{ (a, f(a) \mid a \in \mathcal{F}\\}$ est **reconnaissable**.
{% endnote %}
{% details "preuve" %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, l'algorithme $M$ prenant en entrée deux mots $a$ et $b$ et qui rend *Vrai* si $f(a) = b$ et ne s'arrête pas sinon est bien tel que $\mathcal{L}(M) = \\{ (a, f(a) \mid a \in \mathcal{F}\\}$.

{% enddetails %}

Et si $f$ est défini sur tout mot (ce qui est très souvent le cas) on a même :

{% note "**proposition**" %}
Une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$ est **calculable** si et seulement si $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$ est **décidable**.
{% endnote %}
{% details "preuve" %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, l’algorithme $M$ prenant en entrée deux mots $a$ et $b$ et qui rend *vrai* si $f(a) = b$ et *faux* sinon est bien un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$

Réciproquement, soit $M$ un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$, l'algorithme $M'$ qui prend itérativement tous les mots $b$ et qui rend $b$ lorsque $M(a, b)$ rend *vrai* est bien fini pour tout $a$ et calcule bien $f(a)$.

{% enddetails %}

## Algorithme et fonctions

> TBD : à transformer en DM ?

Un ***algorithme*** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.

On pense très fortement que machine de Turing et algorithmes sont deux notions équivalentes (c'est la [thèse de Church-Turing](../pseudo-code/#thèse-Church-Turing)) mais on en a pas la preuve.

Nous allons montrer dans cette partie que ce que l'on a fait précédemment peut se faire directement avec des algorithmes, on a pas besoin de machine de Turing.

Ce qu'il faudra retenir de cette partie :

* un algorithme peut-être vue une fonction prenant **un** mot composé de 0 et de 1 en entrée et qui rend un mot composé de 0 et de 1 en sortie
* que l'on ne peut pas manipuler de réels directement que des approximations
* que toutes les fonctions prenant **un** mot composé de 0 et de 1 en entrée et qui donne un mot composé de 0 et de 1 en sortie ne peuvent pas être calculées par un algorithme (et savoir pourquoi)

{% info %}
Dans la suite de cette partie on utilisera les [bijections](https://fr.wikipedia.org/wiki/Bijection) entre ensembles. Si deux ensembles sont en bijections on peut passer de l'un à autre (et réciproquement) sans soucis, les deux ensembles sont équivalents.

On peut utiliser l'un ou l'autre de façon équivalente.
{% endinfo %}

Comme [tout ce que manipuler un algorithme c'est des entiers](../../définition/#paramètres-entier){.interne} on a :

{% note %}
Un algorithme à $p$ entrées est une fonction :

$$f: \mathbb{N}^p \rightarrow  \mathbb{N}$$

{% endnote %}

### <span id="fonction-un-entier"></span> Fonctions à un paramètre entier

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

### Forme ultime d'un algorithme

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
