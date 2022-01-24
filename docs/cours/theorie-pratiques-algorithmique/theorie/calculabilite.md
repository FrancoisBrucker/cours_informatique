---
layout: page
title:  "Algorithme : machine de Turing calculs ?"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [calculabilité]({% link cours/theorie-pratiques-algorithmique/theorie/calculabilite.md %})
>
> prérequis :
>
> * [machine de turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
{: .chemin}

La machine de Turing est un modèle permettant de rendre compte d'un algorithme. Soit $M$ une machine de turing et considérons son exécution pour l'entrée $\mu$. La machine va alors soit :

* ne pas s'arrêter (elle n'arrivera jamais à l'état final)
* s'arrêter et sortir un résultat.

Connaitre l'algorithme de la machine correspond ainsi à **deux** problèmes :

1. connaitre les mots d'entrée qui vont faire stopper la machine : c'est la *décidabilité*
2. connaitre la sortie de la machine pour un mot d'entrée qui la fait s'arrêter : c'est la *calculabilité*

Aucun de ces deux problèmes n'est simple.

> Dans la suite, une machine de Turing sera **toujours** une machine sur un alphabet $\\{\sharp, 0, 1\\}$, avec $\\{0, 1\\}$ comme alphabet d'entrée.
> Ceci, [On l'a vu]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}#alphabet-01), se fait sans perte de généralité et va grandement nous simplifier les notations.
{: .attention}

## décidabilité

La décidabilité dans le cadre des machines de Turing couvre deux sous-problèmes :

* savoir si, pour un ensemble de mots $L$, il existe une machine de Turing $M$ telle que $\mathcal{L}(M) = L$ (la machine s'arrête exactement sur les mots de $L$)
* savoir si, pour une machine de Turing $M$ donnée et une entrée $E$, $E \in \mathcal{L}(M)$ (est-ce que la machine va s'arrêter avec l'entrée $E$)

Nous utiliserons une machine spéciale, appelée *décideur* pour nous aider à formaliser ces deux problèmes :

Commençons par définir un *décideur* :

> Un **décideur** est une machine de Turing qui accepte tous les mots et dont la sortie est soit $1$ (on dit alors que la sortie est *Vraie*) soit $0$ (la sortie est *fausse*).
{: .note}

### langage décidable

Savoir si un ensemble de mots $L$ est le langage d'une machine se formalise ainsi :

> Un ensemble de mots $L$ est **reconnaissable** s'il existe une machine de Turing $M$ d'alphabet d'entrée $\Sigma$ tel que $L = \mathcal{L}(M)$
{: .note}

{% details  Par exemple, l'ensemble des palindromes $L$ est reconnaissable. %}
On utilise le fait qu'on mot $m$ est un palindrome si :

* le mot vide est un palindrome
* le mot d'un caractère est un palindrome
* le premier et le dernier caractère doivent être identique
* le mot privé de son premier et dernier caractères doit être un palindrome

On ne décrit pas précisément les différents états, mais on va décrire sont fonctionnement assez précisément pour que ce soit faisable :

1. lit le 1er caractère :
   * si c'est $0$ on place la machine dans l'état $a$
   * si c'est $1$ on place la machine dans l'état $b$
   * si c'est $\sharp$ : on écrit $\sharp 1 \sharp$ sur le ruban, on place le curseur sur le $1$ et l'état de la machine sur l'état d'acceptation : **on a un palindrome** (c'est le mot vide)
2. on remplace le caractère par $\sharp$ on se déplace à droite jusqu'à arriver sur un $\sharp$, on déplace d'un cran à gauche et on lit le caractère :
   * s'il est vide : on écrit $\sharp 1 \sharp$ sur le ruban, on place le curseur sur le $1$ et l'état de la machine sur l'état d'acceptation : **on a un palindrome** (c'est le mot d'un caractère)
   * si c'est $0$ et qu'on est dans l'état $b$ : on écrit $\sharp 0 \sharp$ sur le ruban, on place le curseur sur le $0$ et l'état de la machine sur l'état d'acceptation : **on a pas un palindrome** (le mot ne commence et ne fini pas avec la même lettre)
   * si c'est $1$ et qu'on est dans l'état $a$ : on écrit $\sharp 0 \sharp$ sur le ruban, on place le curseur sur le $0$ et l'état de la machine sur l'état d'acceptation : **on a pas un palindrome** (le mot ne commence et ne fini pas avec la même lettre)
3. on remplace le caractère par $\sharp$ on se déplace à gauche jusqu'à arriver sur un $\sharp$, on déplace d'un cran à droite et on se place dans l'état initial : **on revient à l'étape 1 en ayant supprimer le premier et dernier caractère de l'entrée**

{% enddetails %}

La machine précédente fait même plus que juste reconnaitre un palindrome, si le mot n'est pas un palindrome elle rend faux : notre machine est un décideur pour l'ensemble des palindromes. Reconnaitre si un mot est un palindrome est *décidable* :

> Un ensemble de mots $L$ est **décidable** s'il existe un décideur qui rend $1$ si l'entrée est dans $L$ et $0$ sinon.
{: .note}

La notion de *décidabilité* est centrale en informatique théorique puisqu'elle permet de rendre compte des problèmes que peut résoudre un ordinateur :

> Savoir s'il existe un algorithme permettant de répondre *Vrai* si un élément $A$ à la propriété $P$ et *faux* sinon, est équivalent à savoir si l'ensemble des éléments $A$ ayant la propriété $P$ est décidable.
{: .note}

Prenons par exemple le problème suivant : Soit $P(X)$ un [polynôme](https://fr.wikipedia.org/wiki/Polyn%C3%B4me) à coefficients dans $\mathbb{Z}$. Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% details ce problème est reconnaissable %}

On peut facilement créer un algorithme qui, à partir d'un polynôme $P(x)$ à coefficients dans $\mathbb{Z}$ et d'un entier $a$ calcule $P(a)$ (on peut donc aussi fabriquer une machine de Turing qui le fait).

Il suffit ensuite d'essayer tous les entiers un à un. Si le polynôme en entrée admet une racine entière, on va bien tomber dessus à un moment donné.

{% enddetails %}

{% details il est même décidable %}

On peut borner les racines d'un polynôme. Voir par exemple [le corollaire de ce lien](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me_r%C3%A9el_ou_complexe#Une_premi%C3%A8re_estimation). On aura donc pour chaque polynôme qu'un nombre fini de possibilités à examiner avant de donner la réponse.

{% enddetails %}

Notez que *décidable* est bien plus fort que *reconnaissable*. En effet, si un langage est juste reconnaissable on ne saura pas si l'exécution de la machine avec une entrée donnée met juste longtemps à répondre oui ou si le mot n'est pas accepté par elle.

Il existe bien sûr des langages qui sont reconnaissables et non décidables, par exemple une généralisation de notre problème précédent :

> Le problème consistant à savoir si un [polynôme à plusieurs variables](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es) à coefficients dans $\mathbb{Z}$ admet une racine dans $\mathbb{N}$ est indécidable.
{: .note}

**Félicitations !** Vous venez de rencontrer votre premier problème que ne pourra pas résoudre un ordinateur.

> Ce cas est historiquement important car il correspond au [dixième problème de Hilbert](https://fr.wikipedia.org/wiki/Dixi%C3%A8me_probl%C3%A8me_de_Hilbert). Il a été prouvé indécidable par Matiiassevitch en 1970 en montrant qu'on ne pouvait pas borner les racine d'un polynôme à plusieurs variables.

### arrêt d'un algorithme

Savoir si un algorithme (ou une machine de Turing puisque c'est équivalent) va s'arrêter sur une entrée ou pas est un problème compliqué. Prenez par exemple l'[algorithme suivant](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```python

def syracuse(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

```

L'algorithme est très simple : à partir d'un entier $n$, il le divise par 2 s'il est pair ou le multiplie par 3 et ajoute 1 s'il est impair et recommence tant que ce nombre est strictement plus grand que 1.

Personne ne sait (à l'heure où je tape ces caractères) si cet algorithme s'arrête pour tout $n$.
> Testez chez vous pour plusieurs nombres, c'est assez bluffant. 
> Vous pouvez aussi afficher la suite de nombre ou la représenter graphiquement pour voir l'évolution de votre nombre d'entrée jusqu'à 1.
{: .a-faire}

De façon plus générale :

> [Le problème](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt) de savoir si une machine de Turing $M$ va s'arrêter sur l'entrée $E$ est un problème indécidable.
{: .note}
{% details preuve %}

On doit la preuve à Turing lui-même.

Commençons par remarquer que comme une machine de Turing peut s'[encoder sous la forme d'une suite de 0 et de 1]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}#mtu), on peut bien encoder la paire consituée de la machine de Turing et d'un mot (l'entrée) sous la forme d'un unique mot qui sera l'entrée du décideur s'il existe.

On va maintenant supposer qu'un tel décideur existe et notons le `halt(<M>, E)` avec `<M>` le mot encodant la machine `M`. Cet encodeur rend `1` si l'exécution de `M` avec `E` va s'arrêter et `0` sinon.

On peut alors créer une autre machine dont le pseudo-code est :

```text
def diag(x):
    if halt(x, x) == 1:
        boucle infinie
    else:
        return 1
```

Tout comme [la preuve du théorème de Cantor]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#nombre-fonction) cette nouvelle machine va tout casser :

1. `diag(x)` ne va s'arrêter que si `halt(x, x)` est faux
2. `halt(<diag>, x)` va répondre 1 que si `diag(x)` s'arrête
3. `halt(<diag>, <diag>)` va répondre 1 si `diag(<diag>)` s'arrête or `diag(<diag>)` ne peut s'arrêter que si `halt(<diag>, <diag>)` ne s'arrête pas
4. contradiction

{% enddetails %}

Il faut bien comprendre l'énoncé ci-dessus. Il n'existe pas de décideur qui prend comme entrée une machine de Turing et un mot et qui rend *Vrai* si la machine va s'arrêter : la machine **et** le mot d'entrée sont les paramètres du décideur.

Cela ne contredit pas le fait qu'on puisse créer un décideur spécifique à une machine qui réponde *vrai* ou *faux* selon le paramètre d'entrée de celle-ci. C'est l'algorithme qui décide pour toutes les machines qui est impossible.

> lorsque l'on parle de décidabilité ou de problème il faut toujours bien faire attention à ce qui est un paramètre d'entrée et ce qui est donné.

Le théorème d'indécidabilité de l'arrêt de machine de Turing est fondamental théoriquement. Il est à la base de nombreux contre-exemples et :

* il exhibe le fait qu'il existe des choses que l'on ne peut pas calculer avec un ordinateur
* en creux, il montre qu'on peut tout de même faire beaucoup de choses avec un ordinateur puisqu'il faut chercher des exemples bien tordus pour que ça ne marche pas

## calculabilité

On a vu qu'il existe des problèmes qu'on ne peut pas résoudre avec un algorithme

>ex de ackerman. Impossible de connaitre la valeur sans exécuter l'algo.
{: .tbd}

<https://en.wikipedia.org/wiki/Computable_function>

### fonctions calculables

comme reconnaissable puisque (E, F(E)) est reconnaissable si la fonction est calculable

> castor affairées non


### nombres calculables

> pi oui

<https://en.wikipedia.org/wiki/Computable_number>

* que peut-on calculer ?
* de pseudo code à calcul de f(N) -> N

pour l'instant tous les pseudo-code qu'on a écrit s'arrêtent tout le temps. Mais celui là ? syracuse. On ne sais pas.

## arrêt de la machine

des actions successives qui menent au résultat : ce n'est pas immédiat ! Et on ne sais pas si ça s'arrête.

passer d'un pseudo code à la machine. entier/réels/chaine de caractères. Permet de voir théoriquement ce qu'on peut faire.

## logique, démonstrations mathématiques et calculabilité

<https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice>
<https://en.wikipedia.org/wiki/List_of_undecidable_problems>

démonstation = pseudo-code

## Ackermann

Souvent, savoir si un algorithme va finir est trivial. Mais qu'en est-il de la [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), très importante en informatique théorique ?

En gros, c'est une fonction qui ne peut être décrite que par un algorithme. Il n'existe pas de fonction qui la calcule. Elle se définit de la manière suivante, pour tous entiers m et n positifs :

* A(m, n) = n + 1 si m = 0 
* A(m - 1, 1) si n = 0
* A(m - 1, A(m, n - 1)) sinon.

Cette fonction s'arrête bien un jour.



Pour chaque appel récursif de la fonction d'ackerman, soit m, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$.
 

Pour calculer Ack(2, 3) par exemple, on a les récurrences suivantes :

* Ack(2, 3) = Ack(1, Ack(2, 2))
* Ack(2, 2) = Ack(1, Ack(2, 1))
* Ack(2, 1) = Ack(1, Ack(2, 0))
* Ack(2, 0) = Ack(1, 1)
* Ack(1, 1) = Ack(0, Ack(1, 0))
* Ack(1, 0) = Ack(0, 1) = 2
* puis on remonte d'un cran et les récursions recommencent...


Au final on trouve Ack(2, 3) = 9. La fonction croît très très vite. Par exemple Ack(5, 0) = Ack (4, 1) = 65533 et Ack(4, 2) = $2^{65536} - 3$.

Complexité : nombre d'opération au moins supérieure à son résultat puisque que l'on ne fait qu'ajouter 1 à n comme calcul et les valeurs de n sont modifiées de +1 ou -1.


## refs

<https://plato.stanford.edu/entries/church-turing/>
<http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf>
<https://www.cs.odu.edu/~zeil/cs390/latest/Public/turing-complete/index.html>