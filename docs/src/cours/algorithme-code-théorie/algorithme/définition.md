---
layout: layout/post.njk 
title: Définition d'un algorithme

eleventyNavigation:
  key: "Définition d'un algorithme"
  parent: Algorithme
---

<!-- début résumé -->

Une définition de ce qu'est un algorithme.

<!-- end résumé -->

Pseudo-code, calcul et code sont les trois faces d'une même pièce nommée algorithme. Nous allons voir les implications de ces trois termes, mais commençons par définir un algorithme.

{% info %}
Une super introduction aux algorithmes : <https://www.arte.tv/fr/videos/094414-012-A/declics/>
{% endinfo %}

On doit le mot algorithme à [Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) (1815-1852) qui est le(a) premier(e) informaticien(ne) de l'histoire. Elle a donné ce nom en hommage à un savant persan du 9ème siècle (né vers 780 et mort en 850 à Bagdad) nommé [Al-Khwârizmî](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) qui a publié le premier manuel d'algèbre connu à ce jour.

## <span id="algorithme"></span> Algorithme ?

{% note "Définition du 'Petit Robert'  d'un **algorithme** :" %}
Ensemble des règles opératoires propres à un *calcul*
{% endnote %}

Qu'est-ce que ça veut dire ?

* **algorithme** : ensemble des règles opératoires propres à un **calcul**
* **calcul** : enchaînement des instructions nécessaires à l'accomplissement d'une **tâche**
* **tâche** : ...

Tel monsieur Jourdain, on a utilisé un algorithme pour comprendre ce qu'est un algorithme ! Formalisons le :

```text
Nom : comprendre_une_définition_du_petit_Robert
Entrées : 
    m : un mot à définir
Programme :
    1. étant donné la définition de m dans le dictionnaire du 'Petit Robert'
    2. afficher la définition à l'écran.
    3. pour chaque mot non compris dans la définition :
       1. comprendre_une_définition_du_petit_Robert(mot)
```

C'est un algorithme tout à fait valable. Ce n'est pas du python, mais c'est :

* compréhensible
* chaque instruction (lire une définition, afficher à l'écran, ...) peut être caractérisée par un petit texte en français
* notre algorithme s'arrête bien à un moment (au pire une fois que l'on a passé en revu tous les mots du dictionnaire)

Règles de construction de l'algorithme utilisé :

* **des** paramètres en entrée mais **au plus une** sortie (qui peut être une structure composée comme une liste par exemple).
* le **retour** d'un algorithme est la dernière instruction qu'il fait, en rendant la sortie (ici, il ne rend rien)
* une description de ce qu'il fait
* L'exécution d'un algorithme est signifié par son nom suivie de parenthèses contenant ses paramètres
* afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme.

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

* **finitude** : *« Un algorithme doit toujours se terminer après un nombre fini d’étapes. »*
* **définition précise** : *« Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas. »*
* **entrées** : *« […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié. »*
* **sortie** : *« […] des quantités ayant une relation spécifiée avec les entrées. »*
* **rendement** : *« […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon. »*

On peut en déduire la **définition** suivante :

{% note "**Définitions**" %}
Un ***algorithme*** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{% endnote %}

Ou, de façon équivalente :

{% note "Les **4 propriétés générales** qui définissent un algorithme :" %}

1. un algorithme est constitué d'un ensemble fini d'instructions, décrites avec un nombre fini de symboles
2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes (une étape étant l'application d'une instruction) successives.
3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
4. exécuter une instruction ne doit pas nécessiter d'intelligence (à part celle pour comprendre l'instruction)

{% endnote %}

Une recette de cuisine est donc un algorithme, un trajet google maps, etc.

## <span id="algorithmes-trois-voies"></span> Algorithmes !

La définition très générale d'un algorithme se décline usuellement sous trois formes concrètes :

1. [pseudo-code](../pseudo-code) : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'instructions générales précisément définies. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser un langage de programmation pour décrire notre code. Le but ici est de résoudre un problème donné avec un algorithme utilisant le moins d'instructions possibles.
2. [code](../../code/coder) : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.
3. [fonctions](../../théorie/fonctions) : un algorithme est vu comme une fonction qui calcule un nombre. Le but est ici de comprendre ce que peuvent faire les algorithmes, quels sont les problèmes qu'ils peuvent résoudre.

Ces trois formes ont des buts différents, mais on ne peut exceller dans l'une sans connaître les autres. Tout *théoricien* doit avoir de bonnes connaissances théoriques sur ce que peut calculer  un ordinateur et — tôt ou tard — il devra programmer ses algorithmes ; tout *développeur* doit avoir des connaissances fortes en algorithmie pour pouvoir écrire du code performant.

## Nombre d'algorithmes

La définition générale d'un algorithme stipule qu'il doit être constitué d'un nombre **fini** d'instructions, chaque instruction décrite par un nombre **fini**  de symbole. De plus, c'est implicite, mais un algorithme doit être compris par un humain.

L'idée force à retenir de cette partie est que :

{% note "**A retenir :**" %}
On ne peut pas tout calculer avec des algorithmes, même si on peut calculer beaucoup de choses.
{% endnote %}

### Une infinité d'algorithmes différents

On peut donc déjà conclure que :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes différents.
{% endnote %}
{% details "preuve" %}
Si on considère l'instruction *"Ne fait rien"*, le texte ci-dessous est un algorithme d'une instruction :

```text
Ne fait rien
```

En notant alors $R_k$ ($k >0$) l'algorithme de $k$ instructions *"Ne fait rien"* à la suite (l'algorithme précédent est $A_1$).

Les algorithmes $R_k$ sont tous différents puisque leurs suites d'instructions sont différentes : il existe donc une infinité d'algorithmes différents.
{% enddetails %}

De la preuve de la proposition précédente montre qu'il existe une infinité d’algorithmes différents mais faisant la même chose (tous les algorithmes $R_k$ pour $k$ entier font la même chose : rien)

{% info %}
On y reviendra, mais savoir ce que fait un algorithme n'est pas un problème simple du tout dans le cas général.
{% endinfo %}

Mais, on peut aussi démonter :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes faisant des choses deux à deux différentes.
{% endnote %}
{% details "preuve" %}
On peut par exemple considérer la familles $A_i$ d'algorithmes ($i > 0$) définis tels que $A_i$ soit constitué d'une seule instruction :

```text
Rend l'entier i
```

Les $A_i$ sont bien des algorithmes puisque chaque entier $i$ se décrit avec un nombre fini de chiffres. De plus, les $A_i$ rendent tous des entiers différents.

{% enddetails %}

Il y a donc **beaucoup** d'algorithmes possibles... mais en réalité pas tant que ça.

### Mais seulement une infinité dénombrable

D'après ce qui précède, un algorithme est un texte. On peut alors considérer que les symboles formant la description de chaque instruction sont des caractères pris dans un alphabet. Pour ne pas être chiche, on peut prendre l'alphabet [Unicode](https://fr.wikipedia.org/wiki/Unicode) qui permet d'écrire, entre autres, en Français et contient un peut moins de 150000 caractères différents.

De là :

{% note %}

Un algorithme est une suite finie $c_1 \dots c_n$ où :

* $c_i \in \mathcal{U}$ pour tout $1 \leq i \leq n$
* $\vert \mathcal{U} \vert \leq 150000$ avec $\mathcal{U}$ l'ensemble des caractères Unicode.

On note $\mathcal{A}$ cet ensemble.

{% endnote %}

Bref, les Algorithmes correspondent à un sous-ensemble de l'ensemble des chaînes de caractères écrites en Unicode

On peut alors utiliser l'ordre entre caractères Unicode (en triant les caractères par [numéro](http://ressources.univ-lemans.fr/AccesLibre/UM/Pedago/physique/02/divers/unicode.html) croissant) pour ordonner les algorithmes selon l'ordre du dictionnaire :

{% note "**Ordre entre Algorithmes**" %}

En définissant $\leq$ tel que, pour deux algorithmes $A =c_1\dots c_{n}$ et $A'={c'}_1\dots {c'}\_{n'}$ de $\mathcal{A}$ on ait $A < A'$ si une des deux conditions ci-dessous est vérifiée :

* $n < n'$
* $n = n'$ et il existe $1 \leq i \leq n$ tel que $c_j = c'_j$ pour tout $1 \leq j < i$ et $c_i < c'_i$

La relation $<$ est un [ordre total](https://fr.wikipedia.org/wiki/Ordre_total#D%C3%A9finition) sur l'ensemble des algorithmes.
{% endnote %}
{% details "preuve" %}

Les 4 propriétés de l'ordre total sont facilement vérifiées :

* transitivité : $A \leq B$ et $B \leq C$ implique $A \leq C$ :
  * si $\vert A \vert < \vert B \vert$ ou $\vert B \vert < \vert C \vert$ on a $\vert A \vert < \vert C \vert$
  * si $\vert A \vert = \vert B \vert$ et $\vert B \vert = \vert C \vert$, alors $\vert A \vert = \vert B \vert = \vert C \vert$ et en notant $i$ l'indice du premier caractère qui diffère entre $A$ et $B$ et $j$ l'indice du premier caractère qui diffère entre $B$ et $C$ on a :
    * si $i \leq j$ alors le $i$ème caractère de $A$ est strictement plus petit que le $i$ème caractère de $C$ et ils coïncident avant
    * si $i > j$ alors le $j$ème caractère de $A$ est strictement plus petit que le $j$ème caractère de $C$ et ils coïncident avant
* anti-symétrie : $A \leq B$ et $B \leq A$ implique $A = B$ :
  * si $\vert A \vert < \vert B \vert$ alors on ne peut avoir $B < A$
  * si $\vert A \vert = \vert B \vert$ et qu'il existe un caractère différent entre $A$ et $B$, le premier caractère qui diffère fera que soit $A < B$ soit $B < A$
* réflexivité : $A \leq A$ pour tout algorithme $A$ : clair
* total : $A \leq B$ ou $B \leq A$ pour tous algorithmes $A$ et $B$ : clair

{% enddetails %}

Comme $A \leq A'$ implique que le nombre de caractères de $A$ est plus petit ou égal à celui de $A'$, il n'existe qu'un nombre fini d'algorithmes plus petit que $A'$. De là, on peut montrer que :

{% note "**Proposition**" %}
Il existe $A_1$, le plus petit de tous les algorithmes (pour tout algorithme $A$, $A_1 \leq A$).
{% endnote %}
{% details "preuve" %}

Soit $A$ un algorithme. Comme tous les algorithmes plus petit que lui on autant ou moins de caractères, il n'y en a qu'un nombre fini. On note alors $A_1$ le plus petit algorithme de l'ensemble $\\{ B \mid B \leq A' \\}$. On peut utiliser l'algorithme ci-dessous pour le calculer :

```text
Nom : min
Entrée : un ensemble A
Programme :
    Soit x un élément de A
    pour chaque élément y de A:
        si x > y: 
            x = y
    Retour x
```

Cet algorithme calcule bien le minimum car :

1. à chaque nouvelle affectation de `x`{.language-} le nouveau `x`{.language-} sera strictement plus petit que le précédent. Le dernier `x`{.language-} (celui qui est rendu par l'algorithme) sera donc plus petit que tous les précédents
2. comme `A`{.language-} est fini, la variable `y`{.language-} de la boucle `pour chaque`{.language-} vaudra tous les élément de `A`{.language-}
3. tout `y`{.language-} sera soit plus grand qu'une des valeurs de `x`{.language-} prisent par l'algorithme, soit en vaudra un : `y`{.language-} est plus grand que le dernier `x`{.language-}

Soit Alors $A'$ un autre algorithme. Si on avait $A' < A_1$, alors $A' < A_1 \leq A$ et donc $A' \in \\{ B \mid B \leq A' \\}$ ceci est impossible puisque $A_1$ est le plus petit élément de cet ensemble. Notre hypothèse était donc fausse et $A_1 \leq A'$.

L'algorithme $A_1$ est bien plus petit que tout autre algorithme.

{% enddetails %}

a proposition précédente nous permet d'initier la suite $(A_i)_{i \geq 1}$ :

{% note "**Proposition**" %}
Soit $(A_i)_{i \geq 1}$ la suite définie définie telle que :

* $A_1$ est le plus petit algorithme
* pour $i > 1$, on note $A_{i}$ le plus petit algorithme strictement plus grand que $A_{i-1}$

On a :

* $A_i$ existe pour tout entier $i$,
* $A_i < A_j$ pour tout $i < j$
* pour tout algorithme $A$, il existe $i$ tel que $A = A_i$
{% endnote %}
{% details "preuve" %}

On a démontré que $A_1$ existe et il est clair par définition que si $A_i$ existe pour tout $i \leq k$ alors :

* $A_i < A_{i+1}$ pour tout $i < k$
* il n'existe pas d'algorithme $A$ tel que $A_i < A < A_{i+1}$
* il existe un algorithme $A > A_k$ (car il y aune infinité d'algorithmes différents et uniquement $k$ plus petits que $A_k$) et donc $A_{k+1}$ existe ($\\{ B \mid A_k < B \leq A \\}$ est fini et non vide, il admet un plus petit élément qui se trouve être $A_{k+1}$ (on le prouve de la même manière qu'on a prouvé l'existence de $A_1$))

Soit maintenant $A$ un algorithme et soit $k$ le plus grand entier tel que $A \geq A_k$ (cet entier existe puisque $A_1 \leq A$). Comme $A_k \in \\{ B \mid B \leq A \\}$, si $A > A_k$ alors :

1. l'ensemble $\\{ B \mid A_k < B \leq A \\}$ est non vide
2. il contient donc $A_{k+1}$
3. c'est impossible par hypothèse

On en conclut que $A=A_k$.

{% enddetails %}

On déduit immédiatement de la proposition suivante que la fonction $f$ qui associe a un entier $i$ son algorithme $A_i$ est une bijection et donc :

<span id="nb-dénombrable-algorithmes"></span>
{% note %}
Il y a exactement autant d'algorithmes différents que de nombres entier.
{% endnote %}

### Nombre réels sans algorithme

Savoir qu'il n'y a pas plus d'algorithmes que de nombres entiers est une très information très importante, car elle montre qu'un algorithme ne peut pas tout faire.

{% note "**Théorème**" %}
Il existe strictement plus de nombres réels dans l'intervalle $[0, 1]$ que de nombres entiers.
{% endnote %}
{% details "preuve" %}
On doit cette preuve au mathématicien allemand [Georg Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor). Cette preuve magnifique s'appelle [diagonale de Cantor](https://fr.wikipedia.org/wiki/Argument_de_la_diagonale_de_Cantor#La_non-d%C3%A9nombrabilit%C3%A9_des_r%C3%A9els).

On commence la preuve en remarquant que l'on peut associer à tout entier $i$ formé des chiffres $c_1\dots c_k$ le réel de représentation décimal $0.c_1\dots c_k$, ce qui démontre qu'il y a au moins autant de réels dans $[0, 1]$ que de nombres entiers.

On suppose qu'il existe une injection $f: [0, 1] \rightarrow \mathbb{N}$ entre les réels de l'intervalle $[0, 1]$ et les entiers. On peut alors classer tous les réels selon leurs valeurs selon $f$ :

* on appelle $r_1$ le 1er réel, c'est à dire celui tel que $f(r_1) \leq f(x)$, quelque soit $x \in [0, 1]$
* on appelle $r_2$ le second réel $r_2$ , c'est à dire celui tel que $f(r_2) \leq f(x)$ pour tout $x \in [0, 1] \backslash \\{ r_1 \\}$
* ...
* on appelle $r_i$ le $i$ème réel  : $f(r_i) \leq f(x)$ pour tout $x \in [0, 1] \backslash \\{ r_1, \dots, r_{i-1} \\}$
* ...

Chaque réel pouvant s'écrire sous sa représentation décimale (par exemple $0.1034842$), on construit le nombre réel $r$ de $[0, 1]$ tel que sont $i$ème chiffre après la virgule soit :

* $0$ si le $i$ chiffre après la virgule de $r_i$ est différent de $0$
* $1$ si le $i$ chiffre après la virgule de $r_i$ est $0$

Le nombre $r$ est bien dans $[0, 1]$ mais il ne peut pas être $r_i$ quelque soit $i$ ! Il y a une contradiction. Notre hypothèse était donc fausse, il ne peut exister d'injection entre les réels de l'intervalle $[0, 1]$ et les entiers.

Il y a donc strictement plus de réels dans $[0, 1]$ que d'entiers.

{% enddetails %}

{% info "Le fait qu'il y ait des infinis plus ou moins gros est un résultat que l'on doit à Cantor et qui est vachement profond !" %}
Pour une introduction en douceur, consulter [cette émission d'Arte](https://www.arte.tv/fr/videos/097454-005-A/voyages-au-pays-des-maths/), très bien faite.

On note communément $\aleph_0$ le nombre d'entiers qui est strictement plus petit que le nombre de réels, noté $\aleph_1$. Une question reste encore en suspend, mais on a pour l'instant toujours pas la réponse, c'est : y a-t-il un infini entre $\aleph_0$ et $\aleph_1$ ? On ne sais pas, mais on pense que non. C'est l'[hypothèse du continu](https://fr.wikipedia.org/wiki/Hypoth%C3%A8se_du_continu).

{% endinfo %}

On déduit du théorème précédent que :

{% note %}

Il existe des réels pour lesquels il n'existe aucun algorithme $A(i)$ qui calcule la $i$ème décimale de $i$ quelque soit $i$

{% endnote %}

Trouver de tels nombre est compliqué, car pour y penser il faut le décrire et donc en proposer un algorithme... mais... ils existent.

## Algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique (certains diraient même, et réciproquement. Des mathématiciens certainement...).

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3)
