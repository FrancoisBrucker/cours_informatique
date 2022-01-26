---
layout: page
title:  "Algorithme : calcul"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [calcul]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %})
>
> prérequis :
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

Dans [la partie pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}), on a donné une façon d'écrire des algorithmes. Mais est-ce la seule façon de faire ? Et, au final, que peut-on réellement faire avec un algorithme ?

Ce qu'il faut retenir de cette partie :

* un algorithme peut-être vue une fonction prenant **un** mot composé de 0 et de 1 en entrée et qui donne un mot composé de 0 et de 1 en sortie
* que l'on ne peut pas manipuler de réels directement que des approximations
* que toutes les fonctions prenant **un** mot composé de 0 et de 1 en entrée et qui donne un mot composé de 0 et de 1 en sortie ne peuvent pas être calculées par un algorithme (et savoir pourquoi)
* qu'importe le jeu fini d'instructions utilisé pour le calcul (du moment que les instructions peuvent être décrite de façon finie) on ne pourra pas calculer plus de choses qu'en utilisant le jeu d'instructions défini dans la partie [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})

## algorithmes et pseudo-code

Un algorithme, [on l'a vu]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %}#algorithme), c'est :

> Un algorithme est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{: .note}

La définition est cependant très générale et ne pose pas vraiment la question du choix des instructions, ni de comment réaliser effectivement ce calcul. Tentons de le faire (voir [la page wikipedia sur la calculabilité](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church#Formulation_de_la_th%C3%A8se)) :

> Les **4 propriétés générales** qui définissent une instruction :
>
>1. un algorithme est constitué d'un ensemble fini d'instructions, décrites avec un nombre fini de symboles
>2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes (une étape étant l'application d'une instruction) successives.
>3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
>4. exécuter une instruction ne doit pas nécessiter d'intelligence (à part celle pour comprendre l'instruction)
>
{: .note}

Le terme **fini** est crucial : pour qu'un humain comprenne, et surtout puisse agir, il ne faut pas qu'il y ait un nombre infini de choses à regarder (chaque chose à faire prend un temps de réflexion non nul, une instruction contenant un nombre infini n'est humainement pas réalisable).

### instruction d'un algorithme

On en déduit la définition (très générale) d'une instruction d'un algorithme :

> Une **instruction** d'un algorithme est une règle définie par un nombre **fini** de symboles.
{: .note}

Fini ne veut pas dire petit nombre. Un algorithme peut utiliser des nombres entiers aussi grand qu'il
le veut, du moment qu'ils ne soient pas infini.

### objet manipulables

Puisque l'on a le droit de ne manipuler que des choses finies, un algorithme ne peut manipuler que des [mots d'un alphabet fini](https://fr.wikipedia.org/wiki/Mot_(math%C3%A9matiques)). La conséquence fondamentale de ceci est que :

> **un algorithme ne peut pas manipuler de nombres réels**. On ne peut considérer un réel que comme une abstraction (un symbole particulier) ou une approximation (on ne considère qu'un nombre fini de décimales).
{: .note}

Prenons $\pi$ par exemple. Il existe des algorithmes qui [calculent les décimales de pi](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80#Calcul_de_la_n-i%C3%A8me_d%C3%A9cimale_de_%CF%80), mais on ne pourra jamais écrire que pi est le résultat d'un algorithme, puisque l'algorithme doit s"arrêter : on aura qu'un nombre fini de décimales, donc on aura pas $\pi$.

On ne peut le considérer que de deux manières : comme le symbole $\pi$ et de là faire des opérations sur lui (comme $2 \cdot \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaître sa valeur ou comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations. On ne pourra cependant **jamais** avoir la valeur exacte de $\pi$ avec un algorithme (et ce même s'il avait une mémoire infinie).

Ce n'est pas bien grave en général puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) : considérer les réels en [notation scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique) en se fixant une précision ne gène pas les calculs physiques.

> Faites tout de même attention car parfois, c'est problématique. Pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon), certes, mais aussi lorsque l'on prend l'inverse de choses très petites qui du coup deviennent très grandes. Ce sont des problèmes dit de [stabilité numérique](https://fr.wikipedia.org/wiki/Stabilit%C3%A9_num%C3%A9rique).

En conclusion :

> Les objets manipulables par un algorithme sont uniquement :
>
> * les entiers finis
> * les approximations finies de réels
> * les chaînes de caractères
>
{: .note}

### instructions d'un pseudo-code {#regles-pseudo-code}

Un [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) est un algorithme particulier. Ses [instructions]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) respectent bien les 4 propriétés générales. On peut cependant montrer qu'elles peuvent être réduites à un ensemble bien plus petit :

> On peut ramener l'ensemble des [instructions d'un pseudo-code](https://en.wikipedia.org/wiki/Structured_program_theorem) (même si ce sera plus compliqué d'écrire le code) à trois types d'instructions et à trois façon de les exécuter.
>
> Une **instruction**  est soit :
>
> * une affectation d'un entier (voir même juste un bit) à une variable
> * une lecture d'une variable
> * un test d'égalité entre deux variables
>
> Un pseudo-code doit pouvoir :
>
> * exécuter une instruction puis une autre, **séquentiellement**
> * exécuter une instruction si un test d'égalité est vrai
> * exécuter un bloc d'instructions tant qu'un test d'égalité est vrai
{: .note}

Tous les pseudo-codes utilisant les 6 règles ci-dessus auront la même expressivité (on pourra faire exactement les mêmes choses) que ceux utilisant [les instruction d'un pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles), ce sera juste plus long et compliqué à écrire, c'est pourquoi leur intérêt est uniquement théorique.

### équivalence entre algorithme et pseudo-code ? {#equi-algo-pseudo-code}

On est intimement convaincu (c'est ce qu'on appelle la [thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church)) que les instructions d'un pseudo-code sont équivalentes aux instructions d'un algorithme, c'est çà dire que toutes les instructions que l'on pourrait inventer en un nombre fini de symboles peuvent s'écrire sous la forme des instructions d'un pseudo-code.

### nombre d'algorithmes

Comme un algorithme peut-être décrit par son pseudo-code, qui est une chaîne de caractères (qu'on peut limiter aux mots Français si on a envie) :

> Il ne peut y avoir plus d'algorithmes que de chaine de caractères écrites en Français.
{: .note}

Ça en fait un sacré paquet. Tentons d'être un peu plus précis. Comme chaque chaîne de caractères peut être associée à un entier en concaténant le code [unicode](https://fr.wikipedia.org/wiki/Unicode) associé à chaque caractère de la description de l'algorithme et des instructions utilisées (cela ne fait pas beaucoup de caractères différents si on écrit tout nos algorithmes en n'utilisant que les caracTères qui nous permettent d'écrire en Français) :

> Il ne peut y avoir plus d'algorithmes que de nombres entiers.
{: .note}

## fonctions

Un algorithme, représenté par son pseudo code, a des entrées et une sortie : c'est une fonction. D'après ce qui précède, on a donc :

> Un algorithme à $p$ entrées, dont $q$ entrées entières, $r$ entrées approximation des réels et $s$ chaînes de caractères est une fonction de :
>
> $$f: \mathbb{N}^{q} \times R^r \times C^s \rightarrow \mathbb{N} \cup R \cup C$$
>
> où $\mathbb{N}$ est l'ensemble des entiers, $R$ l'ensemble des approximations de réels et $C$ l'ensemble des chaînes de caractères.
{: .note}

On a pas trop dit grand chose pour l'instant. On a fait que re-écrire ce qu'on savait déjà sous la forme de fonctions. On va montrer qu'on peut faire bien mieux en montrant qu'un algorithme est une fonction de $\mathbb{N}$ (les entiers) dans $\mathbb{N}$.

Cela nous permettra de montrer qu'un algorithme ne peut pas **tout** calculer : il existe des fonctions de $\mathbb{N}$ dans $\mathbb{N}$ qu'aucun ordinateur ne pourra calculer (trouver des fonctions non calculables par un ordinateur n'est pas une tâche simple cependant. Il nous faudra un peut plus de connaissances pour en exhiber).

> Dans la suite de cette partie on utilisera les [bijections](https://fr.wikipedia.org/wiki/Bijection) entre ensembles. Si deux ensembles sont en bijections on peut passer de l'un à autre (et réciproquement) sans soucis, les deux ensembles sont équivalents : on peut utiliser l'un ou l'autre sans perte de généralité.
{: .attention}

### fonctions à plusieurs paramètres entiers {#fonction-plusieurs-entier}

Les paramètres d'un algorithme peuvent tous être représentés par des entiers :

* des entiers finis : c'est clair.
* des approximations finies de réels : on peut utiliser la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754). Par exemple 3.1415 en codage IEEE 754 sur 32 bits correspond à l'entier binaire : `01000000010010010000111001010110` (j'ai utilisé [un convertisseur](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
* des chaînes de caractères : que l'on peut représenter comme un entier. Par exemple la chaîne de caractères "Yop !" correspond au nombre binaire `111100101101111011100000010000000100001` en utilisant  (là aussi, j'ai utilisé [un convertisseur](http://hapax.qc.ca/conversion.fr.html)).

On peut donc reformuler notre assertion précédente en unifiant les paramètres (on les recode tous sous la forme d'entiers) :

> Un algorithme est une fonction de $p$ paramètres entiers et qui rend un entier.
>
> $$f: \mathbb{N}^p \rightarrow \mathbb{N}$$
>
{: .note}

C'est bien mieux mais on sépare encore les algorithmes par leur nombre de paramètres. Allons plus loin.

### fonctions à un paramètre entier {#fonction-un-entier}

Démontrons que tout élément de $\mathbb{N}^p$ peut être représenté par un entier. Pour ce faire on montrera que $\mathbb{N}^p$ est en bijection avec $\mathbb{N}$ quelque soit $p$.

La figure ci-dessous montre comment faire pour $\mathbb{N}^2$. On commence par placer tout élément $(x, y)$ de $\mathbb{N}^2$ dans le plan. puis on passe de l'un à l'autre en suivant les diagonales.

![compteur]({{ "/assets/cours/algorithmie/theorie_n2dansN.png" | relative_url }}){:style="margin: auto;
display: block; width: 200px"}

On chemine alors comme ça :

1. $(0, 0)$
2. $(1, 0)$
3. $(0, 1)$
4. $(2, 0)$
5. $(1, 1)$
6. $(0, 2)$
7. $(3, 0)$
8. ...

L'entier associé à $(x, y)$ est alors l'ordre dans ce cheminement : on peut associer un unique entier à tout couple d'entiers et réciproquement. On en conclue que :

> Il existe une bijection entre $\mathbb{N}^2$ et $\mathbb{N}$ : il y a autant de couples d'entiers que d'entiers.
{: .note}

De façon générale :

> Il existe une bijection entre $\mathbb{N}^p$ et $\mathbb{N}$ : il y a autant de $p$-uplets d'entiers que d'entiers.
{: .note}

{% details preuve %}

On note $D_i$ (une diagonale) l'ensemble des $p$-uplets $(n_1, \dots, n_p)$ tels que $\sum_{i=1}^p n_i = p$.

Comme chaque diagonale a un nombre fini d'élément, on peut les ordonner, en suivant l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique#G%C3%A9n%C3%A9ralisation_aux_produits_cart%C3%A9siens_finis) (le plus petit élément de $D_i$ est $(0, \dots, 0, i)$ et $(i, 0, \dots, 0)$ le plus grand par exemple).

De cet ordre dans une diagonale, on peut en déduire un ordre sur tous les $p$-uplets, en disant que $e < f$ si :

* $e \in D_k$ et $f \in D_{k'}$ avec $k' < k$
* ou si $e, f \in D_k$ et que $e$ est avant $f$ dans l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique#G%C3%A9n%C3%A9ralisation_aux_produits_cart%C3%A9siens_finis) de $D_k$.

La fonction $h$ suivante est alors une bijection de $\mathbb{N}^p$ dans $\mathbb{N}$ :

$$ h(e) = \vert \{ g \mid g < e \}\vert$$

En effet :

* la fonction est bien définie pour tout $p$-uplet : si $f < e$ alors $f$ est dans une diagonale plus petite ou égale à $e$, il y a donc un nombre fini d'éléments plus petit que $e$
* soit $f \neq e$ sont 2 $p$-uplets différents. On peut considérer sans perte de généralité que $f < e$ et donc $\\{ g \mid g < f \\} \cup \\{f \\} \subseteq \\{ g \mid g < e \\}$. On en déduit que $h(f) < h(e)$ et donc que pour tout entier $i$, il existe au plus 1 $p$-uplet $e$ tel que $h(e) = i$
* si on prend deux $p$-uplets successif pour otre ordre, disons $e < e'$ (et il n'existe pas $e''$ tel que $e < e'' < e'$) on a $h(e) + 1 = h(e')$ : pour tout entier $i$ il existe un $p$-uplet $e$ tel $h(e) = i$

{% enddetails %}

Toute fonction de $\mathbb{N}^p$ dans $\mathbb{N}$ peut alors s'écrire comme une fonction de $\mathbb{N}$ dans $\mathbb{N}$ ce qui nous permet de dire que :

> Un algorithme est une fonction de :
>
> $$f: \mathbb{N} \rightarrow \mathbb{N}$$
>
{: .note}

En remarquant que tout entier peut s'écrire sous sa [notation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire), il existe une bijection entre $\mathbb{N}$ et l'ensemble des mots que l'on peut former avec $0$ et $1$. En notant cet ensemble $\\{0, 1\\}^\star$, on en conclut que :

> Un algorithme est une fonction de :
>
> $$f: \{0, 1\}^\star \rightarrow \{0, 1\}^\star$$
>
{: .note}

C'est cette formulation que l'on utilisera le plus souvent.

### pour la bonne bouche {#fonction-un-binaire}

Vous allez rire, on peut encore aller plus loin. Pour l'instant, on sait qu'un algorithme est une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$. Elle associe donc un entier à un autre. Cette fonction est alors équivalente à la fonction $f'$ ci-dessous :

$$
f'(n, m) = \left\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

D'après ce qui précède, en utilisant une bijection entre $\mathbb{N} \times \mathbb{N}$ et $\mathbb{N}$, il existe alors une fonction $f'': \mathbb{N} \rightarrow \\{0, 1\\}$ équivalente à $f'$ et donc à $f$.

En utilisant les notations binaires on a alors :

> Un algorithme est une fonction de :
>
> $$f: \{0, 1\}^\star \rightarrow \{0, 1\}$$
>
{: .note}

## que calcule-t-on ?

On a démontré qu'un algorithme était une fonction de $\mathbb{N}$ dans $\mathbb{N}$ (ou, ce qui est identique, de $\\{0, 1\\}^\star$ dans $\\{0, 1\\}$). Mais c'est une fonction particulière puisque ce qu'elle procède selon un plan détaillé (des instructions) qu'elle exécute petit à petit (séquentiellement).

On ne donnera pas ici d'exemple concret de fonction non calculable on montre juste que contrairement à une idée répandue :

> Un algorithme **ne peut pas** tout calculer. En revanche, quelque soit le formalisme utilisé pour le calcul (le pseudo-code ou code) ils calculent tous **la même chose**.
{: .note}

### on ne calcule pas tout

On va montrer qu'il existe des fonctions qui ne sont pas des algorithmes car il existe strictement plus de fonctions que d'algorithmes.

Pour faire cela, on va procéder par étapes :

1. on montre qu'il y a exactement autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous ensembles de $\mathbb{N}$
2. on montre qu'il y a strictement plus de sous-ensembles de $\mathbb{N}$ que d'éléments dans $\mathb{N}$
3. on conclut

On finira cette partie en montrant, pour la bonne bouche, qu'il y a autant de sous-ensembles de $\mathbb{N}$ que ne nombres réels.

#### fonctions et sous ensembles de $\mathbb{N}$

On va montrer qu'il existe autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}$. Pour cela on commence par montrer qu'il y en a plus puis qu'il y en a moins pour en conclure finalement qu'il y en a donc autant.

Tout d'abord, il est clair que pour tout ensemble d'entiers $A$, on peut construire la fonction :

$$
f_A(x) = \left\{
    \begin{array}{ll}
        x + 1 & \mbox{si } x \in A \\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

On vérifie facilement que si $A \neq A'$ on a $f_A \neq f_{A'}$ (si $x \in A$ et $x \notin A'$ $f_A(x) = x + 1 > 0 = f_{A'}$) et donc que tout sous-ensemble d'entiers peut être associé à une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ différente. On peut donc dire que :

> Il y a plus de fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}$.
{: .note}

Réciproquement, on peut associer pour chaque fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ le sous ensemble de $\mathbb{N}^2$ :

$$I(f) = \{ (n, f(n)) \vert n \in \mathbb{N} \}$$

Si $f$ et $f'$ sont deux fonctions de $\mathbb{N} \rightarrow \mathbb{N}$ différentes on a clairement que $I(f) \neq I(f')$. Ceci nous permet de dire que :

> Il y a moins de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}^2$
{: .note}

Comme on a vu qu'il y avait une bijection entre $\mathbb{N}^2$  et $\mathbb{N}$, il y a autant de sous-ensembles de $\mathbb{N}^2$ que de sous ensemble de $\mathbb{N}$, ce qui nous permet d'écrire :

> Il y a moins de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}$
{: .note}

S'il y a à la fois plus et moins de fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}$, c'est que :

> Il y a autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de $\mathbb{N}$
{: .note}

#### nombre de sous-ensembles de $\mathbb{N}$

Si on prend un ensemble $E$ fini, il est clair qu'il y a strictement plus de sous-ensembles de $E$ que d'éléments dans $E$.

Par exemple, si on prend l'ensemble $\\{a, b, c\\}$. Les différents sous-ensembles qu'on peut faire sont :

* $\emptyset$
* $\\{1\\}$
* $\\{2\\}$
* $\\{3\\}$
* $\\{1, 2\\}$
* $\\{1, 3\\}$
* $\\{2, 3\\}$
* $\\{1, 2, 3\\}$

Il y a 8 sous-ensemble d'un ensemble à 3 éléments. De façon plus générale, on montre facilement que :

> Si $E$ est un ensemble fini et contient $n$ éléments, il y a $2^n$ sous-ensembles possibles à un ensemble à $n$ éléments.
{: .note}
{% details preuve %}

Si l'ensemble $E$ est fini on peut ordonner ses éléments. On a alors $E = \\{ e_1, \dots, e_n\\}$.

Un sous ensemble $F$ de $E$ est alors égal à un $n$-uplet : $T(F) = (u_1, \dots, u_n)$ avec $u_i = 1$ si $e_i \in F$ et $u_i = 0$ sinon.

Comme il est clair que $T$ est une bijection entre l'ensemble des sous-ensembles de $F$ et l'ensemble des $n$-uplets de $\\{0, 1\\}^n$, il y a autant de sous-ensembles de $F$ que d'éléments dans $\\{0, 1\\}^n$, c'est à dire $2^n$ (chaque coordonnée à deux possibilités et il y a $n$ coordonnées).

{% enddetails %}

Comme $2^n > n$ pour tout $n$, il y a strictement plus de sous-ensembles de $E$ que d'éléments de $E$ si $E$ est fini. Etrangement, ceci est toujours vrai si $E$ est infini :

> [**Théorème de Cantor**](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cantor) :
>
> Pour tout ensemble $E$ (même infini), il y a strictement plus de sous-ensembles de $E$ que d'éléments de $E$.
{: .note}

{% details  preuve du théorème de Cantor %}

La preuve du Théorème de Cantor repose sur le fait que pour toute fonction $f$ qui associe à un élément de $E$ un sous-ensemble de $E$, il existe des éléments qui n'ont pas d'antécédent.

L'ensemble $D = \\{x \in E \vert x \notin f(x)\\}$ est un de ceux là. En effet, s'il en avait un, disons $y$, on aurait $f(y) = D$ et alors :

* $y \notin D$ car s'il y était alors $y \notin f(y)$ ce qui est incohérent avec le fait que $f(y) = D$
* $y \in D$ car s'il n'y était pas alors $y \in f(y)$ ce qui est incohérent avec le fait que $f(y) = D$

Bref, $y$ n'existe pas.

On en conclut qu'il existe des sous-ensembles de $E$ qui ne sont pas des images de $f$ : ce n'est pas une [surjection](https://fr.wikipedia.org/wiki/Surjection). Comme $f$ a été prise au hasard, ça signifie que pour toute fonction il existera des sous-ensembles de $E$ qui ne seront pas atteints : il y a strictement plus de sous ensembles de $E$ que d'éléments de $E$.

{% enddetails %}

> Ce théorème est vachement profond !
>
> Il stipule qu'il existe plusieurs infinis, de plus en plus gros. L'infini de $\mathbb{N}$ étant plus petit que celui de l'ensemble de ses sous-ensembles.
>
> Regardez ce lien <https://www.arte.tv/fr/videos/097454-005-A/voyages-au-pays-des-maths/> par exemple qui illustre parfaitement cela.
{: .attention}

En utilisant le théorème de Cantor et le fait qu'il y ait autant de fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ que de sous-ensembles de$\mathbb{N}$ on en déduit donc :

> Il y a strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que d'entiers.
{: .note}

#### conclusion

On a vu qu'il ne pouvait pas y avoir plus d'algorithmes que d'entiers puisque chaque algorithme a une description finie. En utilisant ce qui précède on a alors :

> Il existe des fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ qui ne peuvent pas être calculées par des algorithmes.
{: .note}

#### pour la bonne bouche

Je ne saurais vous laisser dans l'ignorance du nombre de sous-sembles de $\mathbb{N}$. Nous allons démontrer ensemble qu'i y en a autant que de nombres réels entre 0 et 1 (exclus).

On va commencer par montrer qu'il y en a moins puis qu'il y en a plus pour en conclure finalement qu'il y en a donc autant.

Prenons un sous-ensemble $A$ de $\mathbb{N}$. On peut ranger ses éléments par ordre croissant et concaténer leurs représentations décimales en une chaine de caractères (possiblement infini) contenant uniquement des chiffres. On concatène cette chaine à "0.1" pour obtenir la représentation décimale d'un réel.

Exemple : Si $A = \\{0, 1, 4, 42\\}$ on lui associe le réel $R(A) = 0.101442$

Il est clair que cette opération est une injection, c'est à dire que sir $A \neq A'$, on a bien $R(A) \neq R(A')$ et donc que :

> Il y a plus d'éléments dans $]0, 1[$ que de sous-ensembles de $\mathbb{N}$
{: .note}

Prenons maintenant un réel $r$ dans l'intervalle $]0, 1[$. Son écriture décimale s'écrit : $0.a_1a_2\dots a_i\dots$ de longueur infinie, avec possiblement des 0 à la fin. On peut lui associer le sous ensemble infini : $S(r) = \\{a_i + 10 \cdot i \mid i > 0 \\}$.

Il est clair que cette opération est une injection, c'est à dire que sir $r \neq r'$, on a bien $S(r) \neq S(r')$ et donc que :

> Il y a plus de sous-ensembles de $\mathbb{N}$ que d'éléments dans $]0, 1[$
{: .note}

Il y a à la fois plus et moins d'éléments dans $]0, 1[$ que de sous ensembles de $\mathbb{N}$, donc :

> Il y a autant de sous-ensembles de $\mathbb{N}$ que d'éléments dans $]0, 1[$
{: .note}

En remarquant que la fonction $f(x) = \tan(\frac{x-1}{2}\cdot \pi)$ est une bijection de $]0, 1[$ dans $]-\infty, +\infty[$, on en conlut qui'l y a autant de réels dans $]0, 1[$ que dans $]-\infty, +\infty[$ et donc :

> Il y a autant de sous-ensembles de $\mathbb{N}$ que de réels
{: .note}

Le théorème de Cantor nous indique alors deux choses :

* que le nombre d'entiers que l'on note $\aleph_0$ est strictement plus petit que le nombre de réels, noté $\aleph_1$.
* Il y a des infinis plus grand que d'autre et qu'il y en a autant qu'on veut. Il suffit de prendre l'ensemble des sous-ensemble de de $\mathbb{R}$ (il y en a $\aleph_2$) pour avoir un infini plus grand que le nombre de réels. Et ainsi de suite... Pour obtenir $\aleph_0 < \aleph_1 < \dots \aleph_i < dots$

> Une question reste encore en suspend, mais on a pour l'instant toujours pas la réponse, c'est : y a-t-il un infini entre \aleph_0$ et \aleph_1$ ? On ne sais pas, mais on pense que non. C'est l'[hypothèse du continu](https://fr.wikipedia.org/wiki/Hypoth%C3%A8se_du_continu).

Concluant en rebouclant sur nos algorithmes :

> Un algorithme est une fonction $\mathbb{N} \rightarrow \mathbb{N}$.
> Parmi les $\aleph_1$ fonctions de $\mathbb{N} \rightarrow \mathbb{N}$ possibles, seules au plus $\aleph_0$ peuvent être construites par des algorithmes.
{: .note}

### mais lorsqu'on calcule, on calcule la même chose

Les instructions qu'on s'est données pour écrire du pseudo-code vont être pratiques pour décrire un algorithme pour un humain. Le fait qu'une fois posées, les règles ne nécessitent pas d'intelligence pour être exécutées, les rendent même accessible à des étudiants !
Cependant les termes qu'on peut utiliser ne sont pas définis clairement, il y a de multiples façons d'interpréter les [4 règles générales](#regles-generales), ou de manipuler les [6 règles d'un pseudo-code](#regles-pseudo-code).

On peut déjà penser aux multiples langages de programmation, allant de [l'assembleur](https://fr.wikipedia.org/wiki/Assembleur) compréhensible par les processeurs de nos ordinateurs au [python](https://fr.wikipedia.org/wiki/Python_(langage)) que tout le monde connait, en passant par le [haskell](https://fr.wikipedia.org/wiki/Haskell) ou encore le [C](https://fr.wikipedia.org/wiki/C_(langage)).

On trouve même des langages désignées pour être les plus simples possibles (appelés [turing tarpit](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique)) tout en étant aussi expressif que le python. Le plus célèbre d'entre eux est le [brainfuck](https://fr.wikipedia.org/wiki/Brainfuck).

> *fun fact*, on peut utiliser aussi certains jeu comme langage de programmation comme [factorio](https://www.factorio.com/) (l'algorithme de tri [quicksort](https://www.youtube.com/watch?v=ts5EKp9w4TU)), ou encore [minecraft](https://www.minecraft.net/) ([une calculatrice](https://www.youtube.com/watch?v=uGug-4xkw6M)).

Le représentant de toute ces variabilités est la [machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}). C'est un outil simple qui capture merveilleusement les [4 règles générales](#regles-generales) dans le sens où c'est **et** un outil puissant de démonstration **et** un un moyen de créer des algorithmes. C'est pourquoi la [question sur l'équivalence entre algorithme et pseudo-code](#equi-algo-pseudo-code) est souvent écrite de cette façon  :

> On est convaincu que tout ce qu'un humain, une machine, ou encore un système physique peut calculer (c'est à dire en suivant les 4 règles générales de l'algorithme) est exactement égal à ce qu'une machine de Turing peut calculer. C'est ce qu'on appelle [la thèse de Church-Turing](https://plato.stanford.edu/entries/church-Turing/#ReasForAcceThes)
{: .note}

Pour répondre à notre question initiale, *que peut-on calculer ?*, on peut maintenant répondre : ce qu'une machine de Turing peut calculer (et ce n'est pas tout, mais c'est quand même pas mal de choses).

## algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique.

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3))

## Conclusion

On a montré ici 3 choses fondamentales :

* un algorithme ne peut pas tout faire
* un algorithme est une démonstration
* quelque soit le langage utilisé on pourra résoudre les même problèmes

Ceci signifie que l'on doit toujours utiliser le formalisme (ou langage) qui est le plus simple pour résoudre le problème qu'on s'est fixé :

* d'algorithmie : on utilisera les mots du pseudo-code les plus adaptés, dans le respect des 4 règles fondamentales (chaque instruction doit être simple ou explicitée)
* de code : on utilisera le langage qui est plus adapté à notre problème car ils ont tous leurs spécificités. Il est donc impératif d'apprendre plus d'un langage et surtout d'apprendre à en changer quand on change de problème à résoudre.
* théorique : on utilisera [la machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}), modèle théorique simple qui permet d'appréhender tout ce qui est calculable.

Enfin, faites attention aux réels ! Ils n'existent pas (du moins en informatique). Vous ne manipulez que des approximations : il faut faire attention à la stabilité numérique de vos algorithmes et ne **jamais** tester l'égalité entre deux réels mais **toujours** les comparer à epsilon prêt.
