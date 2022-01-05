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

Dans [la partie précédente]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}), on a donné une façon d'écrire des pseudo-codes. Mais est-ce la seule façon de faire ? Et, au final, que peut-on réellement faire avec un algorithme ?

## algorithmes et fonctions

On va montrer qu'un algorithme peut être vu comme une fonction particulière.

### règles d'un algorithme {#regles-generales}

Un algorithme, [on l'a vu]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %}#algorithme), est un ensemble de règles propre à un **calcul**. La [définition de calcul](https://dictionnaire.lerobert.com/definition/calcul) du Petit Robert est cependant très générale et ne pose pas vraiment la question du choix des règles, de comment réaliser effectivement ce calcul. On s'accorde (voir [la page wikipedia sur la calculabilité](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church#Formulation_de_la_th%C3%A8se)) à garder **4 règles générales** :

1. un algorithme possède un ensemble fini de règles, décrites avec un nombre fini de symboles
2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes
3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
4. exécuter une règle ne doit pas nécessiter d'intelligence (à part celle pour comprendre la règle)

Tout ça est un peu plus précis. On constate que c'est le terme **fini** qui revient constamment : pour qu'un humain comprenne, et surtout puisse agir, il faut pas qu'il y ait un nombre infini de choses à regarder (chaque chose à faire prend un temps de réflexion non nulle, une instruction contenant un nombre infini n'est humainement pas réalisable). En même, si l'on admet que l'on est immortel et que l'on peut réaliser un nombre infini d'opérations, elles sont réalisées les unes à la suite des autres et chaque opération ne peut manipuler qu'un nombre fini d'éléments : on ne ainsi atteindre que des choses [dénombrables](https://fr.wikipedia.org/wiki/Ensemble_d%C3%A9nombrable) c'est à dire représentables par des entiers.

>Cette remarque, évidente, a une conséquence fondamentale : **un algorithme ne peut pas manipuler de nombres réels**. On ne peut considérer un réel que comme une abstraction (un symbole particulier) ou une approximation (on ne considère qu'un nombre fini de décimale).
{: .note}

Prenons $\pi$ par exemple. On peut le considérer de deux manières : comme le symbole $\pi$ et de là faire de opérations sur lui (comme $2 \cdot \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaitre sa valeur ou comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations. On ne pourra cependant **jamais** avoir la valeur exacte de $\pi$ avec un algorithme (et ce même s'il avait une mémoire infinie).

Ce n'est pas bien grave en général puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) : considérer les réels en [notation scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique) en se fixant un précision ne gène pas les calculs physiques.

> Faites tout de même attention car parfois, c'est problématique. Pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon), certes, mais aussi lorsque l'on prend l'inverse de choses très petites qui du coup deviennent très grandes. Ce sont des problèmes dit de [stabilité numérique](https://fr.wikipedia.org/wiki/Stabilit%C3%A9_num%C3%A9rique).

Fini ne veut pas dire petit nombres. Un algorithme peut utiliser des nombres entiers aussi grand qu'il le veut, du moment qu'ils ne soient pas infini
{: .attention}

>Les règles que l'on a défini [précédemment]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) pour écrire un pseudo-code respectent alors les règles ci-dessus si on enlève les réels comme objets basique. On peut même se restreindre [sans perte de généralité](https://en.wikipedia.org/wiki/Structured_program_theorem) (même si ce sera plus compliqué d'écrire le code) aux règles suivantes (il n'y a même pas besoin de récursivité) :
>
> * de lire et d'affecter des entiers à des variables
> * d'avoir un test d'égalité entre deux variables
> * d'exécuter une instruction puis un autre, séquentiellement
> * exécuter une instruction si un test d'égalité est vraie
> * exécuter un bloc d'instructions tant qu'un test d'égalité est vraie
{: .note}

Tous les pseudo-code utilisant les 5 règles ci-dessus auront la même expressivité (on pourra faire exactement les même choses) que ceux utilisant [les règles]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) utilisées couramment.

On pense même (c'est ce qu'on appelle la [thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church)) que quelque soit les règles qu'on va se donner, du moment qu'elles respectent les 4 règles générales, alors on ne pourra pas calculer plus de choses.

### fonctions

Un algorithme, représenté par son pseudo code, a des entrées et une sorite. D'après ce qui précède, ces entrées et cette sortie peuvent être :

* des entiers finis
* des approximations finies de réels
* des chaines de caractères

> Un algorithme à $p$ entrées, dont $q$ entrées entières, $r$ entrées approximation des réels et $s$ chaines de caractères est une fonction de :
>
> $$f: \mathbb{N}^{q} \times R^r \times C^t \rightarrow N \cup A \cup C$$
>
> où $\mathbb{N}$ est l'ensemble des entiers, $R$ l'ensemble des approximations de réels et $C$ l'ensemble des chaines de caractères.
{: .note}

On a pas trop dit grand chose pour l'instant. On a fait que reécrire ce qu'on savait déjà sos la forme de fonctions. On va montrer qu'on peut faire bien mieux.

## modèle

On montre ici que l'on peut aller bien plus loin que la partie précédente et montrer qu'un algorithme est une fonction de $\mathbb{N}$ (les entiers) dans $\mathbb{N}$ 

Cela nous permettra ensuite de montrer qu'un algorithme ne peut pas **tout** calculer : il existe des fonctions de $\mathbb{N}$ dans $\mathbb{N}$ qu'aucun ordinateur ne pourra calculer.

> Trouver des fonctions non calculables par un ordinateur n'est pas une tâche simple cependant. Il faut connaitre les machines de Turing pour en exhiber.

### fonctions à plusieurs paramètres entiers {#fonction-plusieurs-entier}

Les paramètres d'un algorithme peuvent tous être représentés par des entiers :

* des entiers finis : c'est clair.
* des approximations finies de réels : on peut utiliser la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754). Par exemple 3.1415 en codage IEEE 754 sur 32 bits correspond à l'entier binaire : `01000000010010010000111001010110` (j'ai utilisé [un convertisseur](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
* des chaines de caractères : que l'on peut représenter comme un entier en utilisant le le codage [utf-8](https://fr.wikipedia.org/wiki/UTF-8). Par exemple la chaine de caractère "Yop !" correspond au nombre binaire `111100101101111011100000010000000100001` en utilisant  (là aussi, j'ai utilisé [un convertisseur](http://hapax.qc.ca/conversion.fr.html)).

On peut donc reformuler notre assertion précédente en unifiant les paramètres (on les recodent tous sous la forme d'entiers) :

> Un algorithme est une fonction de $p$ paramètres entiers et qui rend un entier.
>
> $$f: \mathbb{N}^p \rightarrow \mathbb{N}$$
>
{: .note}

C'est bien mieux mais on sépare encore les algorithmes par leur nombre de paramètres. Allons plus loin.

### fonctions à un paramètre entiers {#fonction-un-entier}

Démontrons que tout élément de $\mathbb{N}^p$ peut être représenté par un entier. Pour ce faire on montrera que $\mathbb{N}^p$ est en bijection avec $\mathbb{N}$ quelque soit $p$.

La figure ci-dessous montre comment faire pour $\mathbb{N}^2$. On ordonne les diagonales (la diagonale $D_i$ contient les éléments dont la somme des coordonnées est égale à $i$) les une par rapport aux autres et dans chaque diagonale on prend l'ordre lexicographque (ordre du dictionnaire en considérant chaque coordonnée comme une lettre).

![compteur]({{ "/assets/cours/algorithmie/theorie_n2dansN.png" | relative_url }}){:style="margin: auto;display: block; width: 200px"}

Dans le cas général, notons $D_k$ (la diagonale numéro $k$) l'ensemble des éléments $(n_1, \dots, n_p)$ de $\mathbb{N}^p$ dont la somme $\sum_i n_i$ vaut $k$. Il y a un nombre fini d'éléments dans $D_k$ puisque chaque coordonnées est plus petite que $k$ (il y a au plus $k^p$ éléments dans $D_k$), ce qui nous permet d'ordonner tous les éléments de $\mathbb{N}^p$ : $e < f$ si :

* $e \in D_k$ et $f \in D_{k'}$ avec $k' < k$
* ou si $e, f \in D_k$ et que $e$ est avant $f$ dans l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique#G%C3%A9n%C3%A9ralisation_aux_produits_cart%C3%A9siens_finis) de $D_k$.

Cet ordre nous permet de définir [une injection](https://fr.wikipedia.org/wiki/Injection_(math%C3%A9matiques)) de $\mathbb{N}^p$ dans $\mathbb{N}$ par l'application :

$$ h(e) = \vert \{ g \mid g < e \}\vert$$

Cela fonctionne car :

* si $f < e$ alors $f$ est dans une diagonale plus petite ou égale à $e$, il y a donc un nombre fini d'éléments plus petit que $e$
* si $f < e$ alors $\\{ g \mid g < f \\} \cup \\{f \\} \subseteq \\{ g \mid g < e \\}$ et donc $h(f) < h(e)$
* si $e$ et $f$ sont deux éléments différents de $\mathbb{N}^p$ alors soit $e < f$ soit $f < e$

On conclut en remarquant que la fonction $h'(n) = (n, 0, \dots , 0)$ est une injection de $\mathbb{N}$ dans $\mathbb{N}^p$. Il existe donc une injection de $\mathbb{N}$ dans $\mathbb{N}^p$ (la fonction $h'$) et une injection de $\mathbb{N}^p$ dans $\mathbb{N}$ (la fonction $h$) : il existe une bijection de $\mathbb{N}^p$ dans $\mathbb{N}$.

Toute fonction de $\mathbb{N}^p$ dans $\mathbb{N}$ peut alors s'écrire comme une fonction de $\mathbb{N}$ dans $\mathbb{N}$ ce qui nous permet de dire que :

> Un algorithme est une fonction de :
>
> $$f: \mathbb{N} \rightarrow \mathbb{N}$$
>
{: .note}

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

En remarquant que tout entier peut s'écrire sous sa [notation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire), il existe une bijection entre $\mathbb{N}$ et l'ensemble des mots que l'on peut former avec $0$ et $1$. En notant cet ensemble $\\{0, 1\\}^\star$, on en conclut que :

> Un algorithme est une fonction de :
>
> $$f: \{0, 1\}^\star \rightarrow \{0, 1\}$$
>
{: .note}

## que calcule-t-on ?

On a démontré qu'un algorithme était une fonction de $\mathbb{N}$ dans $\mathbb{N}$ (ou, ce qui est identique, de $\\{0, 1\\}^\star$ dans $\\{0, 1\\}$). Mais c'est une fonction particulière puisque ce qu'elle procède selon un plan détaillé (des instructions) qu'elle exécute petit à petit (séquentiellement).

On ne donnera pas ici d'exemple concret de fonction non calculables on montre juste que contrairement à une idée répandue :

> Un algorithme ne peut pas **tout** calculer. En revanche, quelque soit le formalisme utilisé pour le calcul (le pseudo-code ou code) ils peuvent tous calculer **la même chose**.
{: .note}

### on ne calcule pas tout

On va montrer qu'il existe des fonctions qui ne sont pas des algorithmes car il existe strictement plus de fonctions que d'algorithmes.

#### nombre d'algorithmes {#nombre-algorithmes}

Comme un algorithme peut-être décrit par son pseudo-code, qui est une chaine de caractères (qu'on peut limiter aux mots Français si on a envie), in y a au plus autant d'algorithmes que de chaines de caractères. Ca en fait un sacré paquet mais comme chaque chaine de caractère est un entier (on l'a vu [juste avant](#fonction-plusieurs-entier)) :

> Il ne peut y avoir plus d'algorithme que de nombres entiers.
{: .note}

#### nombre de fonctions

Soit $f: \mathbb{N} \rightarrow \mathbb{N}$. En associant pour chaque entier $n$ le couple $(n, f(n))$ on associe à chaque fonction de $\mathbb{N}$ dans $\mathbb{N}$ l'ensemble :

$$I(f) = \{ (n, f(n)) \vert n \in \mathbb{N} \}$$

Connaitre $f$ ou $I(f)$ est équivalent et comme $I(f) \subseteq \mathbb{N} \times \mathbb{N}$ on en conclut :

> Il y a autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de parties de $\mathbb{N} \times \mathbb{N}$
{: .note}

Or pour tout ensemble $E$ il y a strictement plus d'éléments dans l'ensemble de ses parties (qu'on note $2^E$) que dans $E$ (c'est le [théorème de Cantor](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cantor)). On en conclut qu'il y a strictement plus de fonctions que d'éléments dans $\mathbb{N} \times \mathbb{N}$. Or comme $\mathbb{N} \times \mathbb{N}$ et $\mathbb{N}$ sont en bijection (mais si, on l'a vu [précédemment](#fonction-un-entier)) :

> Il y a strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de nombres entiers.
{: .note}

La preuve du Théorème de Cantor repose sur le fait que pour toute fonction $f: E \rightarrow 2^E$, l'ensemble $D = \\{x \in E \vert x \notin f(x)\\}$ n'a pas d'antécédent pour $f$. En effet, s'il en avait un, disons $y$, on aurait $f(y) = D$ et alors :

* $y \notin D$ car s'il y était alors $y \notin f(y)$ ce qui est incohérent avec le fait que $f(y) = D$
* $y \in D$ car s'il n'y était pas alors $y \in f(y)$ ce qui est incohérent avec le fait que $f(y) = D$

Bref, $y$ n'existe pas. On en conclut qu'il existe des éléments de $2^E$ qui ne sont pas des images de $f$ : ce n'est pas une [surjection](https://fr.wikipedia.org/wiki/Surjection). Comme $f$ a été prise au hasard, ça signifie que pour toute fonction de $E$ dans $2^E$ il existera des éléments de $2^E$ qui ne seront pas atteints : il y a strictement plus d'élément dans $2^E$ que dans $E$.

### mais lorsqu'on calcule, on calcule la même chose

Les règles qu'on s'est donné pour écrire du pseudo-code vont être pratiques pour décrire un algorithme pour un humain. Le fait qu'une fois posées, les règles ne nécessitent pas d'intelligence pour être exécutées, les rendent même accessible à des étudiants !
Cependant les termes qu'on peut utiliser ne sont pas définis clairement, il y a de multiples façons d'interpréter les [4 règles générales](#regles-generales) d'un calcul et donc de multiples façon d'écrire du pseudo-code.

On peut déjà penser aux multiples langages de programmation, allant de [l'assembleur](https://fr.wikipedia.org/wiki/Assembleur) compréhensible par les processeurs de nos ordinateurs au [python](https://fr.wikipedia.org/wiki/Python_(langage)) que tout le monde connait, en passant par le [haskell](https://fr.wikipedia.org/wiki/Haskell) ou encore le [C](https://fr.wikipedia.org/wiki/C_(langage)). On trouve même des langages désignées pour être les plus simples possibles (appelés [turing tarpit](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique)) et permettant de calculer tout ce qu'on peut faire en python par exemple, comme le [brainfuck](https://fr.wikipedia.org/wiki/Brainfuck) qui est le plus célèbres d'entres eux.

> *fun fact*, on peut utiliser aussi certains jeu comme langage de programmation comme [factorio](https://www.factorio.com/) (l'algorithme de tri [quicksort](https://www.youtube.com/watch?v=ts5EKp9w4TU)), ou encore [minecraft](https://www.minecraft.net/) ([une caculatrie](https://www.youtube.com/watch?v=uGug-4xkw6M)).

Et bien on peut démontrer que tous ces langages **calculent exactement la même chose** (mais de façon différente) !

> l'assembleur, le python ou encore le C sont des langages qui permettent de calculer exactement ce qu'on peut calculer avec une [machine de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing). De plus, on ne connait pas de langages qui permettent de calculer plus de choses.
{: .note}

Tous ces exemples, plus bien d'autres essais, tendent à [accréditer la thèse de Church-Turing](https://plato.stanford.edu/entries/church-turing/#ReasForAcceThes) selon laquelle :

> On est convaincu que tout ce qu'un humain, une machine, ou encore un système physique peut calculer (c'est à dire en suivant les 4 règles générales) est exactement égal à ce qu'une machine de Turing peut calculer.
{: .note}

Pour répondre à notre question initiale, *que peut-on calculer ?*, on peut maintenant répondre : ce qu'une machine de Turing peut calculer (et ce n'est pas tout, mais c'est quand même pas mal de choses).

## algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique. 

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déduction qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible à démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machine de turing qui ne s'arrêtent jamais et que savoir si une machine de turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3))
7. Turing, en 1936, démontre que (5) est équivalent à écrire un algorithme

## Conclusion

On a montré ici 3 choses fondamentales :

* un algorithme ne peut pas tout faire
* un algorithme est une démonstration
* quelque soit le langage utilisé on pourra résoudre les même problèmes

Ceci signifie que l'on doit toujours utiliser le formalisme (ou langage) qui est le plus simple pour résoudre le problème qu'on s'est fixé :

* d'algorithmie : on utilisera les mots du pseudo-code les plus adaptés, dans le respect des 4 règles fondamentales (chaque instruction doit être simple ou explicitée)
* de code : on utilisera le langage qui est plus adapté à notre problème car ils ont tous leurs spécificités. Il est donc impératif d'apprendre plus d'un langage et surtout d'apprendre à en changer quand on change de problème à résoudre.
* théorique : on utilisera [la machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}), modèle théorique simple qui permet d'appréhender tout ce qui est calculable.

Enfin, faites attention aux réels ! Ils n'existent pas (en informatique). Vous ne manipulez que des approximations : il faut faire attention à la stabilité numérique de vos algorithme et ne **jamais** tester l'égalité entre deux réels mais **toujours** les comparer à epsilon prêt.
