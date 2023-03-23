---
layout: layout/post.njk 
title:  "Décidabilité"
category: cours
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-théorie/index.md %}) / [théorie]({% link cours/algorithme-code-théorie/théorie/index.md %}) / [décidabilité]({% link cours/algorithme-code-théorie/théorie/decidabilite.md %})
>
> prérequis :
>
> * [Algorithmes, fonctions et pseudo-code]({% link cours/algorithme-code-théorie/théorie/algorithmes-fonctions-pseudo-code.md %})
{.chemin}

On a vu dans la partie [fonctions]({% link cours/algorithme-code-théorie/théorie/fonctions.md %}) qu'un algorithme ne pouvait pas tout calculer, qu'il y a avait même bien plus de choses qu'on ne pouvait pas faire avec un algorithme que de chose qu'on pouvait faire avec.

Nous allons étudier le problème sous l'angle de *décidabilité*, c'est à dire de savoir si un problème donné admet un algorithme pour le résoudre.

> on peut aussi regarder le problème sous l'angle de la [calculabilité]({% link cours/algorithme-code-théorie/théorie/calculabilite.md %}), c'est à dire de savoir si telle fonction ou tel nombre peut être calculé par un algorithme.

Ce qui faut retenir de cette partie :

* un décideur est un algorithme spécifique à un problème de décision donné. Il répond oui si l'entrée admet une réponse au problème et non sinon
* savoir si un algorithme va s'arrêter est un problème indécidable
* connaitre les algorithmes qui résolvent tel ou tel problème est indécidable

## problèmes de décision

Commençons par définir un *problème de décision* :

> Un **problème de décision**, est une question qui ne peut avoir que deux réponses *vrai* ou *fausse* selon l'entrée donnée.
{.note}

Par exemple le problème suivant est un problème de décision :

* **nom** : premier
* **entrée** : un nombre $n$
* **question** : $n$ est-il un nombre premier ?

Un problème de décision est **décidable**,  si on peut lui associer un algorithme (on dit un *décideur*) qui répond comme lui :

> Un **décideur** est un algorithme qui pour toute entrée, répond *Vrai* ou *faux*
{.note}

Le problème de décision *premier* admet un décideur (il suffit de tester tous les entiers plus petit que $n$ pour voir si le reste de la division entière vaut 0), mais ce n'est pas de tous les les problèmes.

Par exemple le problème suivant [n'admet pas de décideur](#arret), il est **indécidable** :

* **nom** : arrêt
* **entrées** : un algorithme $A$, et une entrée $E$
* **question** : L'algorithme $A$ s'arrête-t-il avec $E$ comme entrée ?

La décidabilité est donc le fait de savoir si on peut reconnaitre l'ensemble $L$ des entrées qui satisfont une propriété donnée :

> Un ensemble de mots $L$ est décidable s'il existe un **décideur** qui répond *vrai* si l'entrée est dans $L$ et *faux* sinon.
{.note}

Il existe un cas plus faible que la décidabilité, c'est la *reconnaissabilité* :

> Un ensemble de mots $L$ est **reconnaissable** s'il existe un algorithme $M$ telle que $L = \mathcal{L}(M)$ (l'algorithme ne va s'arrêter que pour les entrées de $L$)
{.note}

Notez que tout problème décidable est reconnaissable (à la place de répondre *Faux* on boucle indéfiniment), mais ce n'est pas le cas de tous les problèmes ([ce problème](#poli-z) par exemple).

## exemples

Nous allons montrer ici trois exemples de problèmes décidable ou non qui sont fondamentaux.

### racines de polynômes à coefficients dans $\mathbb{Z}$ {#poli-z}

Soit le problème de décision suivant :

* **nom** : racine polynôme
* **entrées** : $P(X)$ un [polynôme](https://fr.wikipedia.org/wiki/Polyn%C3%B4me) à coefficients dans $\mathbb{Z}$
* **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% details ce problème est reconnaissable %}

On peut facilement créer un algorithme qui, à partir d'un polynôme $P(x)$ à coefficients dans $\mathbb{Z}$ et d'un entier $a$ calcule $P(a)$.

Il suffit ensuite d'essayer tous les entiers un à un. Si le polynôme en entrée admet une racine entière, on va bien tomber dessus à un moment donné.

{% enddetails %}

{% details il est même décidable %}

Soit $P(X) = \sum_{i=0}^na_iX^i$ (avec $a_n \neq 0$) un polynôme. On va montrer que pour tout $\mid X \mid > \max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$, on a $\mid P(X)\mid > 0$.

Toutes les racine du polynôme seront donc plus petites que $\frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid}$ et on pourra stopper l'algorithme d'énumération au bout d'un nombre fini d'itérations.

On a en effet la suite d'implications :

$$
\begin{array}{lcll}
    \mid X \mid & > & \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid}&\mbox{et } \mid X \mid > 1\\
    \mid a_n X^n \mid & > & \sum_{i=0}^{n-1}(\mid a_i X^{n-1} \mid)&\\
    \mid a_n X^n \mid & > & \mid a_{n-1}X^{n-1}\mid + \mid X \mid \cdot \sum_{i=0}^{n-2}(\mid a_i X^{n-2} \mid)&\\
    \mid a_n X^n \mid & > & \mid a_{n-1}X^{n-1}\mid + \sum_{i=0}^{n-2}(\mid a_i X^{n-2} \mid)& \mbox{car } \mid X \mid > 1\\
    \mid a_n X^n \mid & > & \dots&\\
    \mid a_n X^n \mid & > & \sum_{i=0}^{n-1}\mid a_i X^{i} \mid&\\
    \mid a_n X^n \mid & > & \mid \sum_{i=0}^{n-1} a_i X^{i} \mid&\\
\end{array}
$$

qui prouvent que $\mid P(X) \mid = \mid a_nX^n + \sum_{i=0}^{n-1} a_i X^{i}\mid$ sera toujours non nul et du signe de $a_n$ pour tout $\mid X \mid > \max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$
{% enddetails %}

En revanche le problème suivant qui en est une généralisation n'est pas décidable, bien qu'il reste reconnaissable :

* **nom** : racine polynôme plusieurs variables
* **entrées** : $P(X)$ un [polynôme à plusieurs variables](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es) à coefficients dans $\mathbb{Z}$
* **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

> *"racine polynôme plusieurs variables"* est un problème **reconnaissable** mais **indécidable**.
{.note}
{% details élément de la preuve %}
Cela a été [démontré en 1970 par Matiiassevitch](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Matiiassevitch) en prouvant que l'on ne pouvait pas borner les racines d'un polynôme à plusieurs variables.

Il n'existe donc pas d'algorithme qui s'arrête au bout d'un temps fini si un polynôme à plusieurs variables n'a pas de racine dans $\mathbb{N}$.

{% enddetails %}

**Félicitations !** Vous venez de rencontrer votre premier problème que ne pourra pas résoudre un ordinateur.

> Ce cas est historiquement important car il correspond au [dixième problème de Hilbert](https://fr.wikipedia.org/wiki/Dixi%C3%A8me_probl%C3%A8me_de_Hilbert).

### arrêt d'un algorithme {#arret}

Savoir si un algorithme va s'arrêter, ou pas, sur une entrée est un problème compliqué. Prenez par exemple l'[algorithme suivant](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```python

def syracuse(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

```

L'algorithme est très simple : à partir d'un entier $n$, il le divise par 2 s'il est pair ou le multiplie par 3 et ajoute 1 s'il est impair et recommence tant que ce nombre est strictement plus grand que 1.

> Testez chez vous pour plusieurs nombres, c'est assez bluffant.
>
> Affichez également la suite de nombre ou la représenter graphiquement pour voir l'évolution de votre nombre d'entrée jusqu'à 1.
{.faire}

Personne ne sait (à l'heure où je tape ces caractères) si cet algorithme s'arrête pour tout $n$.

De façon plus générale le problème de décision :
>
> * **nom** : [Arrêt](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)
> * **entrées** :
>   * un algorithme $A$
>   * une entrée $E$
> * **question** : $A$ s'arrête-t-il avec $E$ comme entrée ?
>
> est **indécidable**.
{.note}
{% details preuve %}

On doit la preuve à Turing lui-même, qui l'a démontrée dans le cadre de ses machines. Et comme une machine de Turing est équivalente à un algorithme, on peut reprendre directement sa preuve.

Commençons par remarquer qu'un algorithme, tout comme une machine de Turing, peut s'[encoder sous la forme d'une suite de 0 et de 1]({% link cours/algorithme-code-théorie/théorie/machine-turing.md %}#mtu), on peut donc bien passer un algorithme comme paramètre d'entrée d'un algorithme.

On va maintenant supposer qu'un tel décideur existe et notons le `halt(<A>, E)` avec `<A>` le mot encodant l'algorithme `A`. Cet encodeur rend *Vrai* si l'exécution de `A` avec `E` va s'arrêter et *Faux* sinon.

On peut alors créer un  autre algorithme dont le pseudo-code est :

```text
def diag(x):
    if halt(x, x) == 1:
        boucle infinie
    else:
        return Vrai
```

Tout comme [la preuve du théorème de Cantor]({% link cours/algorithme-code-théorie/théorie/fonctions.md %}#nb-ss-ensemble-N) cette nouvelle machine va tout casser :

1. `diag(x)` ne va s'arrêter que si `halt(x, x)` est faux
2. `halt(<diag>, x)` va répondre 1 que si `diag(x)` s'arrête
3. `halt(<diag>, <diag>)` va répondre 1 si `diag(<diag>)` s'arrête or `diag(<diag>)` ne peut s'arrêter que si `halt(<diag>, <diag>)` ne s'arrête pas
4. contradiction

{% enddetails %}

> Le problème de l'arrêt est souvent donné pour une machine de Turing : on cherche à savoir si une machine de Turing donnée s'arrête ou pas.

On peut montrer que le cas particulier suivant est lui aussi indécidable :

> Le problème :
>
> * **nom** : Arrêt vide
> * **entrée** : un algorithme $A$
> * **question** : $A$ s'arrête-t-il avec une entrée vide ?
>
> est **indécidable**.
{.note}
{% details preuve %}
Si $E$ est une entrée et $A$ un algorithme, il existe un algorithme $A_E$ qui commence par affecter l'entrée $E$ à une variable, puis exécute l'algorithme $A(E)$. On a donc que $A$ s'arête avec $E$ comme entrée si et seulement si $A_E$ s'arrête avec une entrée vide.

De là, un algorithme qui pourrait décider si $A_E$ s'arrête ou non avec une entrée vide déciderait également si $A$ s'arrête avec l'entrée $E$, ce qui est impossible puisque le problème de l'arrêt est indécidable.

{% enddetails %}

> Il faut bien comprendre l'énoncé ci-dessus.
{.attention}

Il n'existe pas de décideur qui prend comme entrée **et** un algorithme **et** une entrée et qui rend *Vrai* si l'algorithme va s'arrêter : l'algorithme et le mot d'entrée sont les **entrées** du décideur.

Cela ne contredit pas le fait qu'on puisse créer un décideur spécifique à un algorithme qui réponde *vrai* ou *faux* selon l'entrée de celui-ci. C'est l'algorithme général, indépendant de l'algorithme à tester, qui n'existe pas.

> Lorsque l'on parle de décidabilité ou de problème **il faut toujours bien faire attention à ce qui est un paramètre d'entrée et ce qui est donné**.
{.note}

Le théorème d'indécidabilité de l'arrêt d'un algorithme est fondamental théoriquement. Il est à la base de nombreux contre-exemples et :

* il exhibe le fait qu'il existe des choses que l'on ne peut pas calculer avec un ordinateur
* en creux, il montre qu'on peut tout de même faire beaucoup de choses avec des algorithmes puisqu'il faut chercher des exemples bien tordus pour que ça ne marche pas

## théorème de Rice {#theoreme-rice}

Le [Théorème de Rice](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice) est un exemple d'indécidabilité est fondamental car il montre que l'on ne peut pas *a priori* savoir ce que va faire un algorithme.

> Soit $\mathcal{A}$ un ensemble non vide d'algorithmes.
>
> Le problème :
>
> * **nom** : propriétés-$\mathcal{A}$
> * **entrée** : un algorithme $A$
> * **question** : Est-ce qu'il existe $A'$ dans $\mathcal{A}$ tel que $A(E) = A'(E)$ pour toute entrée $E$ ?
>
> est **indécidable**.
{.note}
{% details preuve %}
Soit $A0 \in \mathcal{A}$ et $M$ un algorithme. On peut alors construire l'algorithme suivant :

```text
def A-M(x):
    M()
    A0(x)
    return Vrai
```

L'algorithme `A-M` est dans $\mathcal{A}$ si et seulement si l'algorithme $M$ s'arrête pour une entrée vide.

On en conclut que si *propriétés-$\mathcal{A}$* était décidable, alors le problème *"Arrêt vide"* le serait également, ce qui est impossible.

{% enddetails %}

Ce théorème a de profondes implications. Il montre en effet que l'on ne peut pas a priori savoir ce que va faire un algorithme et, réciproquement que quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront.

Par exemple : il est indécidable de savoir si un algorithme calcule $n!$

> en revanche il est parfois possible de démonter si un algorithme donné calcule $n!$ ou pas.
{.attention}

Ceci rend impossible des méthodes automatisées de preuve d'algorithmes. Il est donc nécessaire :

* de prouver individuellement tout algorithme que l'on conçoit
* de tester personnellement toute fonction que l'on code

Il est **impossible** d'automatiser le processus.
