---
layout: layout/post.njk
title: Définition d'un algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On doit le mot algorithme à [Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) (1815-1852) qui est le(a) premier(e) informaticien(ne) de l'histoire. Elle a donné ce nom en hommage à un savant persan du 9ème siècle (né vers 780 et mort en 850 à Bagdad) nommé [Al-Khwârizmî](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) qui a publié le premier manuel d'algèbre connu à ce jour.

## <span id="algorithme"></span> Algorithme ?

{% note "Définition du '*Petit Robert*'  d'un **algorithme** :" %}
Un **_algorithme_** est un ensemble des règles opératoires propres à un _calcul_.
{% endnote %}

Qu'est-ce que ça veut dire ?

- **algorithme** : ensemble des règles opératoires propres à un **calcul**
- **calcul** : enchaînement des instructions nécessaires à l'accomplissement d'une **tâche**
- **tâche** : ...

Tel monsieur Jourdain, on a utilisé un algorithme pour comprendre ce qu'est un algorithme ! Formalisons le :

```text
Nom : comprendre_une_définition_du_petit_Robert
Entrées :
    m : un mot à définir
Programme :
    1. étant donné la définition de m dans le dictionnaire du 'Petit Robert'
    2. afficher la définition à l'écran
    3. pour chaque mot non compris dans la définition :
       3.1. comprendre_une_définition_du_petit_Robert(mot)
```

C'est un algorithme tout à fait valable. Ce n'est pas du python, mais c'est :

- compréhensible
- chaque instruction (lire une définition, afficher à l'écran, ...) peut être caractérisée par un petit texte en français
- notre algorithme s'arrête bien à un moment (au pire une fois que l'on a passé en revu tous les mots du dictionnaire)

Règles de construction de l'algorithme utilisé :

- **des** paramètres en entrée mais **au plus une** sortie (qui peut être une structure composée comme une liste par exemple).
- le **retour** d'un algorithme est la dernière instruction qu'il fait, en rendant la sortie (ici, il ne rend rien)
- une description de ce qu'il fait
- L'exécution d'un algorithme est signifié par son nom suivie de parenthèses contenant ses paramètres
- afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme.

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

- **finitude** : Un algorithme doit toujours se terminer après un nombre fini d’étapes.
- **définition précise** : Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas.
- **entrées** : […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié.
- **sortie** : […] des quantités ayant une relation spécifiée avec les entrées.
- **rendement** : […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon.

On peut en déduire la définition suivante : Un **_algorithme_** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions. Ou, de façon équivalente :

<div id="règles-générales"></div>
{% note "**Définition**" %}

Un **_algorithme_** est défini par les 4 propriétés suivantes :

1. un algorithme est constitué d'un **suite fini d'instructions**, chacune décrite avec **un nombre fini de symboles**
2. un humain doit pouvoir suivre chaque étape avec **un papier et un crayon**
3. exécuter une instruction **ne doit pas nécessiter d'intelligence** (à part celle pour comprendre l'instruction)
4. l'algorithme produit un résultat et s'arrête après **un nombre fini d'étapes** (une étape étant l'application d'une instruction) successives.

{% endnote %}
{% note %}
On appellera **_programme_** un texte qui ne respecte que les 3 premières propriétés : un algorithme est un programme qui s'arrête.

{% endnote %}

Une recette de cuisine est donc un algorithme, un trajet google maps, etc.

## <span id="algorithmes-trois-voies"></span> Programmes et Algorithmes

Prenons l'énoncé suivant qui décrit une procédure permettant de chercher un élément particulier dans une suite finie de nombres :

```text
Demander à l'utilisateur :
  - de donner un entier que l'on appellera x
  - de donner une suite d'entiers que l'on appellera t

Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
Si on trouve un tel élément, afficher "Vrai" à l'écran.
```

Pour transformer cette description en algorithme, il faut procéder à plusieurs modifications :

1. Un programme a un nom pour qu'on puisse le retrouver une fois décrit
2. L'utilisateur n'existe pas : un programme doit exister en tant que tel. Les entrées (demander des choses à l'utilisateur) et les sorties (afficher des résultats) sont abstraites :
   - on parle de paramètres d'entrées du programme
   - on parle de sortie du programme (le programme rend quelque chose, comme une fonction)

En appliquant ces règles, la description précédente devient :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai".
```

Il nous manque cependant encore une chose : si le programme s'arrête il doit rendre quelque chose, ce qui n'est pas le cas ici si on ne trouve pas `x`{.language-} dans `t`{.language-}. Modifions le :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai".
    Sinon rendre "Faux".
```

Notre programme s'arrêtant tout le temps : c'est un algorithme.

{% note "**À retenir**" %}
Un programme **programme** possède :

- un nom
- des paramètres d'entrées (il peut y en avoir 0). Chaque paramètre à un nom qui pourra être utilisé dans la description du programme et un type qui décrit sa nature.
- une sortie. Si le programme s'arrête il doit rendre quelque chose.
- une description qui explicite ce qu'il fait.

Si le programme s'arrête quelque soient ses entrées, c'est un **algorithme**.
{% endnote %}
{% attention %}
Afficher un résultat à l'écran est différent de rendre un résultat : le premier s'adresse à un utilisateur et est _perdu_, le second peut être à nouveau utilisé par au autre programme.
{% endattention %}

La définition très générale d'un algorithme se décline usuellement sous deux formes concrètes :

1. le pseudo-code : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'instructions générales précisément définies. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser la syntaxe d'un langage de programmation pour le décrire (le python, par exemple, est très utilisé pour décrire des algorithmes). Le but ici est de montrer que l'on peut résoudre un problème donné avec un algorithme.
2. le code : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.

Par exemple l'algorithme recherche s'écrirait en pseudo-code de cette façon :

<span id="algorithme-recherche"></span>

```pseudocode
algorithme recherche(T: [entier],
                     x: entier
                    ) → booléen:

    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Et en code python (qui est très similaire au pseudo-code) :

```python/
def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False
```

Ces deux formes ont des buts différents, mais on ne peut exceller dans l'une sans connaître l'autre. Tout _théoricien_ doit avoir de bonnes connaissances pratiques sur ce que peut calculer un ordinateur et — tôt ou tard — il devra programmer ses algorithmes. Réciproquement, tout _développeur_ doit avoir des connaissances fortes en algorithmie pour pouvoir écrire du code performant.

Mais avant de n'utiliser plus que du pseudo-code, regardons ce que cela veut dire d'écrire un algorithme de façon générale et sans autres contraintes que celle de la définition.

## Nombre de programmes

La définition générale d'un programme stipule qu'il doit être constitué d'un nombre **fini** d'instructions, chaque instruction décrite par un nombre **fini** de symboles. De plus, c'est implicite, mais un programme doit être compris par un humain.

### Une infinité de programmes différents

On va se concentrer sur les algorithmes puisque tout algorithme est un programme. De la définition d'un algorithme on peut donc déjà conclure que :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes différents.
{% endnote %}
{% details "preuve", "open" %}
Si on considère l'instruction `Ne fait rien`{.language-}, le texte ci-dessous est un algorithme d'une instruction :

```text
Ne fait rien
```

En notant alors $R_k$ ($k >0$) l'algorithme de $k$ instructions `Ne fait rien`{.language-} à la suite (l'algorithme précédent est $R_1$).

Les algorithmes $R_k$ sont tous différents puisque leurs suites d'instructions sont différentes : il existe donc une infinité d'algorithmes différents.
{% enddetails %}

De la preuve de la proposition précédente montre qu'il existe une infinité d’algorithmes différents mais faisant la même chose : tous les algorithmes $R_k$ pour $k$ entier font la même chose, rien.

{% info %}
On y reviendra, mais savoir ce que fait un algorithme n'est pas un problème simple du tout dans le cas général.
{% endinfo %}

Mais, on peut aussi démontrer :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes faisant des choses deux à deux différentes.
{% endnote %}
{% details "preuve", "open" %}
On peut par exemple considérer la familles $A_k$ d'algorithmes ($k > 0$) définis tels que $A_k$ soit constitué d'une seule instruction :

```text
Rend l'entier k
```

Les $A_k$ sont bien des algorithmes puisque chaque entier $k$ se décrit avec un nombre fini de chiffres. De plus, les $A_k$ rendent tous des entiers différents.

{% enddetails %}

Il y a donc **beaucoup** d'algorithmes possibles... mais en réalité pas tant que ça.

### Mais seulement une infinité dénombrable

D'après ce qui précède, un algorithme est un texte. On peut alors considérer que les symboles formant la description de chaque instruction sont des caractères pris dans un alphabet. Pour ne pas être chiche, on peut prendre l'alphabet [Unicode](https://fr.wikipedia.org/wiki/Unicode) qui permet d'écrire, entre autres, en Français et contient un peut moins de 150000 caractères différents.

De là :

{% note "**Proposition**" %}

Un **_programme_** est une suite finie $c_1 \dots c_n$ où :

- $c_i \in \mathcal{U}$ pour tout $1 \leq i \leq n$
- avec $\mathcal{U}$ l'ensemble des caractères [Unicode](https://fr.wikipedia.org/wiki/Unicode), $\vert \mathcal{U} \vert \leq 150000$.

On note $\mathcal{A}$ cet ensemble.

{% endnote %}
{% details "preuve", "open" %}
Un algorithme est composée d'une suite finie d'instruction. Comme chaque instruction peut être nommée par un texte et que chaque instruction est décrite un texte en Français, tout algorithme est une suite de caractères Unicode.
{% enddetails %}

Bref, les programmes correspondent à un sous-ensemble de l'ensemble des chaînes de caractères écrites en Unicode. On peut alors utiliser l'ordre entre caractères Unicode (chaque caractère est identifié par un entier) pour ordonner les algorithmes selon l'ordre du dictionnaire :

<div id="encodage-algorithme"></div>
{% note "**Proposition**" %}
On peut associer à toute chaîne de caractère un entier strictement positif unique.
{% endnote %}
{% details "preuve", "open" %}
Il suffit d'associer le numéro de chaque caractère Unicode écrit avec 6 chiffres. Une chaîne de caractère $(c_i)_{0\leq i < n}$ est alors une suite de $6n$ chiffres. Par exemple : l'instruction "Ne fait rien" correspond au nombre :

<div>
$$
\underbracket{000078}_{\text{N}}\underbracket{000101}_{\text{e}}\underbracket{000032}_{\text{ }}\underbracket{000102}_{\text{f}}\underbracket{000097}_{\text{a}}\underbracket{000105}_{\text{i}}\underbracket{000116}_{\text{t}}\underbracket{000032}_{\text{ }}\underbracket{000114}_{\text{r}}\underbracket{000105}_{\text{i}}\underbracket{000101}_{\text{e}}\underbracket{000110}_{\text{n}}
$$
</div>

Pour éviter tout soucis avec des algorithmes commençant par le caractère Unicode de nombre 0 (un même nombre peut avoir autant de chiffre 0 qu'il veut au début), on fait commencer tout algorithme par le chiffre 1. L'algorithme d'une seule instruction "Ne fait rien" correspond ainsi au nombre :

$$
1000078000101000032000102000097000105000116000032000114000105000101000110
$$

On associe bien à toute chaîne de caractères $(c_i)_{0\leq i < n}$ un nombre de $6n +1$ chiffres unique.
{% enddetails %}

On déduit immédiatement la proposition suivante :

<span id="nb-dénombrable-algorithmes"></span>
{% note "**Proposition**" %}
Il y a exactement autant d'algorithmes différents que de nombres entiers.
{% endnote %}
{% details "preuve", "open" %}
Comme à chaque algorithme est associé un entier strictement positif unique, on peut les ranger par nombre croissant et considérer la suite d'algorithmes $(A_k)_{k \geq 1}$ telle que :

- $A_1$ est l'algorithme de plus petit nombre associé
- pour $k > 1$, $A_k$ est l'algorithme est dont le nombre associé est le plus petit qui est plus grand que le nombre associé à $A_{k-1}$

On a alors :

- $A_k$ existe pour entier $k$ (puisqu'il y a une infinité d'algorithmes différents, donc de descriptions différentes)
- pour tout algorithme $A$, il existe $k$ telle que $A=A_k$

Ce qui implique que la fonction qui associe à tout algorithme sa position dans la suite $(A_k)_{k \geq 1}$ est une bijection entre l'ensemble des algorithmes et l'ensemble des entiers strictement positifs.

{% enddetails %}

La preuve ci-dessus est classique. Lorsqu'il y a un nombre infini de choses dénombrable, il y en a autant que d'entiers. C'est pourquoi il y a autant d'entiers pair que d'entiers impair que de multiples de 42.

### Nombres réels sans algorithme

Savoir qu'il n'y a pas plus d'algorithmes que de nombres entiers est une très information très importante car elle montre qu'un algorithme ne peut pas tout faire. En effet :

<span id="diagonale-cantor"></span>
{% note "**Théorème**" %}
Il existe strictement plus de nombres réels dans l'intervalle $[0, 1]$ que de nombres entiers strictement positifs.
{% endnote %}
{% details "preuve", "open" %}
On doit cette preuve magnifique au mathématicien allemand [Georg Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor). Elle est basée sur l'argument s'appelant [diagonale de Cantor](https://fr.wikipedia.org/wiki/Argument_de_la_diagonale_de_Cantor#La_non-d%C3%A9nombrabilit%C3%A9_des_r%C3%A9els).

On commence en remarquant que l'on peut associer à tout entier $i$ formé des chiffres $c_1\dots c_k$ le réel de représentation décimale $0.c_1\dots c_k$, ce qui démontre qu'il y a au moins autant de réels dans $[0, 1]$ que de nombres entiers.

On suppose ensuite qu'il existe une injection $f: [0, 1] \rightarrow \mathbb{N}$ entre les réels de l'intervalle $[0, 1]$ et les entiers. On peut alors classer tous les réels selon leurs valeurs selon $f$ :

- on appelle $r_1$ le 1er réel, c'est à dire celui tel que $f(r_1) \leq f(x)$, quelque soit $x \in [0, 1]$
- on appelle $r_2$ le second réel $r_2$ , c'est à dire celui tel que $f(r_2) \leq f(x)$ pour tout $x \in [0, 1] \backslash \\{ r_1 \\}$
- ...
- on appelle $r_i$ le $i$ème réel : $f(r_i) \leq f(x)$ pour tout $x \in [0, 1] \backslash \\{ r_1, \dots, r_{i-1} \\}$
- ...

Chaque réel pouvant s'écrire sous sa représentation décimale (par exemple $0.1034842$), on construit le nombre réel $r$ de $[0, 1]$ tel que sont $i$ème chiffre après la virgule soit :

- $1$ si le $i$ème chiffre après la virgule de $r_i$ est différent de $1$
- $2$ si le $i$ème chiffre après la virgule de $r_i$ est $1$

Le nombre $r$ est bien dans $[0, 1]$ mais il ne peut pas être $r_i$ quelque soit $i$ ! Il y a une contradiction (comme notre nombre ne finit ni par 9 ni par 0 il a [un unique développement décimal](https://fr.wikipedia.org/wiki/D%C3%A9veloppement_d%C3%A9cimal#Cas_des_nombres_r%C3%A9els), il apparaît forcément dans notre liste). Notre hypothèse était donc fausse, il ne peut exister d'injection entre les réels de l'intervalle $[0, 1]$ et les entiers.

Il y a donc strictement plus de réels dans $[0, 1]$ que d'entiers.

{% enddetails %}

Le fait qu'il y ait des infinis plus ou moins gros est un résultat que l'on doit à Cantor et qui est très profond. On note communément $\aleph_0$ le nombre d'entiers qui est strictement plus petit que le nombre de réels, noté $\aleph_1$. Une question reste encore en suspend, mais on a pour l'instant toujours pas la réponse, c'est : y a-t-il un infini entre $\aleph_0$ et $\aleph_1$ ? On ne sais pas, mais on pense que non. C'est l'[hypothèse du continu](https://fr.wikipedia.org/wiki/Hypoth%C3%A8se_du_continu).

{% info %}
Pour une introduction en douceur sur ces sujets, consulter [cette émission d'Arte](https://www.arte.tv/fr/videos/097454-005-A/voyages-au-pays-des-maths/), très bien faite.
{% endinfo %}

On déduit du théorème précédent que :

{% note %}

Il existe des réels pour lesquels il n'existe aucun algorithme $A(i)$ qui calcule la $i$ème décimale de $i$ quelque soit $i$

{% endnote %}

Trouver de tels nombres est compliqué, car pour y penser il faut le décrire et donc en proposer un algorithme... Mais... ils existent (nous en verrons un plus tard).

## Objets manipulables par un algorithme

Le terme **fini** de la définition d'un algorithme est crucial : pour qu'un humain comprenne, et surtout puisse agir, il ne faut pas qu'il y ait un nombre infini de choses à regarder (chaque chose à faire prend un temps de réflexion non nul, une instruction contenant un nombre infini n'est humainement pas réalisable).

On en déduit la définition (très générale) d'une instruction d'un algorithme :

{% note %}
Une **instruction** d'un algorithme est une règle définie par un nombre **fini** de symboles.
{% endnote %}

Fini ne veut pas dire petit nombre. Un algorithme peut utiliser des nombres entiers relatifs aussi grand ou petit qu'il
le veut, du moment qu'ils ne soient pas infinis.

Puisque l'on a le droit de ne manipuler que des choses finies, un algorithme ne peut manipuler que des [mots d'un alphabet fini](<https://fr.wikipedia.org/wiki/Mot_(math%C3%A9matiques)>). La conséquence fondamentale de ceci est que :

{% note "**un algorithme ne peut pas manipuler de nombres réels**" %}

On ne peut considérer un réel que comme une abstraction (un symbole particulier) ou une approximation (ne considérer qu'un nombre fini de ses décimales).
{% endnote %}

Prenons $\pi$ par exemple. Il existe des algorithmes qui [calculent les décimales de pi](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80#Calcul_de_la_n-i%C3%A8me_d%C3%A9cimale_de_%CF%80), mais on ne pourra jamais écrire que le nombre $\pi$ est le résultat d'un algorithme, puisque l'algorithme doit s'arrêter : on aura qu'un nombre fini de décimales, pas le nombre $\pi$.

On ne pourra considérer $\pi$ que de deux manières :

- soit comme un symbole et l'utiliser pour faire des opérations sur lui (comme $2 + \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaître sa valeur
- soit comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations.

Ce n'est pas bien grave en général puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) : considérer les réels en [notation scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique) en se fixant une précision ne gène pas les calculs physiques.

{% info %}
Faites tout de même attention car parfois, c'est problématique. Pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon), certes, mais aussi lorsque l'on prend l'inverse de choses très petites qui du coup deviennent très grandes. Ce sont des problèmes dit de [stabilité numérique](https://fr.wikipedia.org/wiki/Stabilit%C3%A9_num%C3%A9rique).
{% endinfo %}

Donc :

{% note %}

Les objets manipulables par un programme sont uniquement les suites finies composés des objets de type :

- les entiers relatifs
- les approximations finies de réels
- les chaînes de caractères

{% endnote %}

Ces objets sont tous représentables par des suites finies de `0` et de `1` :

- des entiers relatifs :
  - positifs en utilisant leur notation binaire et en les faisant commencer par un `0`, par exemple 3 sera encodé par `011` (le `0` tout à gauche signifiant que l'entier est positif)
  - négatifs en utilisant [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) de la représentation binaire de son opposé. Ainsi -3 sera encodé par `101` (un entier négatif ainsi représenté commencera toujours par un `1`)
- des approximations finies de réels : on peut utiliser la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754). Par exemple 3.1415 en codage IEEE 754 sur 32 bits correspond à l'entier binaire : `01000000010010010000111001010110` (j'ai utilisé [un convertisseur](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
- des chaînes de caractères : que l'on peut représenter comme un entier. Par exemple la chaîne de caractères "Yop !" correspond en utf-8 au nombre hexadécimal 0x596F702021 (là aussi, j'ai utilisé [un convertisseur](http://hapax.qc.ca/conversion.fr.html)) qui en binaire vaut : `0000010110010110111101110000001000000010`

On peu aller plus loin en représentant les tableaux de suites finies de "0" et de "1" par une unique suite finie de "0" et de "1". Pour cela on peut utiliser l'encodage suivant :

- le caractère `0` est encodé par la suite `100`
- le caractère `1` est encodé par la suite `101`
- le caractère de séparation est encodé par la suite `000`
- le caractère de début de liste est encodé par la suite `010`
- le caractère de fin de liste est encodé par la suite `001`

Ainsi le tableau `[00110, 110]` sera encodé par la suite `010100100101101100000101101100001`. Notez que cet encodage permet d'encoder tout aussi aisément les listes imbriquées de suites finies de 0 et de 1, comme `[0, [1, [1]], 0]`, chaque caractère nécessaire (`0`, `1`, `,`, `[` et `]`) ayant son propre code sur 3 bits.

En conclusion, comme on peut associer une suite finie de de `0` et de `1` à tout algorithme et à tout ce qu'il peut manipuler :

<span id="paramètres-binaires"></span>
{% note "**Proposition**" %}
Tout ce que peut manipuler un programme est une suite finie de caractères `0` et `1`.
{% endnote %}
{% note "**Définition**" %}
Un caractère (`0` ou `1`) [est appelé **_bit_**](https://fr.wikipedia.org/wiki/Bit).
{% endnote %}

Un bit est l'information minimale que l'on peut véhiculer puisqu'il ne peut avoir que 2 valeurs différentes. Cette unité minimale d'information est très puissante puisque les suites finies de bits permettent non seulement de stocker tous les objets que peut manipuler un algorithme mais aussi les algorithmes eux-même via le codage binaires des chaines Unicode par exemple. On en conclut que :

{% note "**À retenir**" %}
Un algorithme et tout ce qu'il peut manipuler est une suite finie de `0` et de `1`.
{% endnote %}

## Algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique (certains diraient même, et réciproquement. Des mathématiciens certainement...).

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3))
