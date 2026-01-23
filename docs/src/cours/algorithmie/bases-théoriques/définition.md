---
layout: layout/post.njk
title: Définitionsd'un algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On doit le mot algorithme à [Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) (1815-1852) qui est le(a) premier(e) informaticien(ne) de l'histoire. Elle a donné ce nom en hommage à un savant persan du 9ème siècle (né vers 780 et mort en 850 à Bagdad) nommé [Al-Khwârizmî](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) qui a publié le premier manuel d'algèbre connu à ce jour.


On va montrer quelques propriétés générales d'un programme et d'un algorithme.

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
    3. lire la définition et l'
    4. pour chaque mot non compris dans la définition :
       4.1. comprendre_une_définition_du_petit_Robert(mot)
```

C'est un algorithme tout à fait valable. Ce n'est pas du python, mais c'est :

- compréhensible
- chaque instruction (lire une définition, comprendre un mot, ...) peut être caractérisée par un petit texte en français
- notre algorithme s'arrête bien à un moment (au pire une fois que l'on a passé en revue tous les mots du dictionnaire)

Règles de construction de l'algorithme utilisées :

- **des** paramètres en entrée mais **au plus une** sortie (qui peut être une structure composée comme une liste par exemple).
- le **retour** d'un algorithme est la dernière instruction qu'il fait, en rendant la sortie (ici, il ne rend rien)
- une description de ce qu'il fait
- l'exécution d'un algorithme est signifié par son nom suivie de parenthèses contenant ses paramètres
- afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme : l'algorithme continue de fonctionner après l'affichage

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme#Quelques_d%C3%A9finitions_connexes) :

- **finitude** : Un algorithme doit toujours se terminer après un nombre fini d’étapes.
- **définition précise** : Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas.
- **entrées** : […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié.
- **sortie** : […] des quantités ayant une relation spécifiée avec les entrées.
- **rendement** : […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon.

On peut en déduire la définition suivante : Un **_algorithme_** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions. Ou, de façon équivalente :

<div id="définition-règles-générales"></div>
{% note2 "**Définition**" %}

Un **_algorithme_** est défini par les 4 propriétés suivantes :

1. un algorithme est constitué d'un **suite finie d'instructions**, chacune décrite avec **un nombre fini de symboles**
2. un humain doit pouvoir suivre chaque étape avec **un papier et un crayon**
3. exécuter une instruction **ne doit pas nécessiter d'intelligence** (à part celle pour comprendre l'instruction)
4. l'algorithme produit un résultat et s'arrête après **un nombre fini d'étapes** (une étape étant l'application d'une instruction) successives.

{% endnote2 %}
{% note2 "**Définition**" %}
On appellera **_programme_** un texte qui ne respecte que les 3 premières propriétés : un algorithme est un programme qui s'arrête.

{% endnote2 %}

Une recette de cuisine est donc un algorithme, un trajet google maps, etc.

{% lien %}
N'hésitez pas à regarder cette vidéo, [petite biographie de Donald Knuth](https://www.youtube.com/watch?v=d2a4MpY7I2w), grand informaticien.
{% endlien %}

Prenons l'énoncé suivant qui décrit une procédure permettant de chercher un élément particulier dans une suite finie de nombres :

```text
Demander à l'utilisateur :
  - de donner un entier que l'on appellera x
  - de donner une suite d'entiers que l'on appellera t

Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
Si on trouve un tel élément, afficher "J'ai trouvé ton entier dans la liste ! Je suis trop trop fort !" à l'écran.
```

Pour transformer cette description en programme/algorithme, il faut procéder à plusieurs modifications :

1. Un programme a un nom pour qu'on puisse le retrouver une fois décrit
2. L'utilisateur n'existe pas : un programme doit exister en tant que tel. Les entrées (demander des choses à l'utilisateur) et les sorties (afficher des résultats) sont abstraites :
   - on parle de paramètres d'entrée du programme
   - on parle de sortie du programme (le programme rend quelque chose, comme une fonction)

En appliquant ces règles, la description précédente devient :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "J'ai trouvé ton entier dans la liste ! Je suis trop trop fort !".
```

Il nous manque cependant encore une chose : si le programme s'arrête il doit rendre quelque chose, ce qui n'est pas le cas ici si on ne trouve pas `x`{.language-} dans `t`{.language-}. Modifions le :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "J'ai trouvé ton entier dans la liste ! Je suis trop trop fort !".
    Sinon rendre "L'entier n'est pas dans la liste".
```

Notre programme s'arrête tout le temps : c'est un algorithme.

On peut le rendre un peut plus professionnel en ne rendant pas une chaîne de caractère mais un booléen (`Vrai` s'il est dans la liste et `Faux` sinon) :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Sortie :
    un booléen
Programme :
    Parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre `Vrai`.
    Sinon rendre `Faux`.
```

{% attention "**À retenir**" %}
Un **programme** possède :

- un nom
- des paramètres d'entrée (il peut y en avoir 0). Chaque paramètre à un nom qui pourra être utilisé dans la description du programme et un type qui décrit sa nature.
- une sortie. Si le programme s'arrête il doit rendre quelque chose. La sortie doit toujours être du même type.
- une description qui explicite ce qu'il fait.

Si le programme s'arrête quelque soient ses entrées, c'est un **algorithme**.
{% endattention %}
{% info %}
Afficher un résultat à l'écran est différent de rendre un résultat : le premier s'adresse à un utilisateur et est _perdu_, le second peut être à nouveau utilisé par au autre programme.
{% endinfo %}

La définition très générale d'un algorithme se décline usuellement sous deux formes concrètes :

1. le pseudo-code : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'instructions générales précisément définies. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser la syntaxe d'un langage de programmation pour le décrire (le python, par exemple, est très utilisé pour décrire des algorithmes). Le but ici est de montrer que l'on peut résoudre un problème donné avec un algorithme.
2. le code : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.

Par exemple l'algorithme recherche s'écrirait en pseudo-code de cette façon :

<span id="algorithme-recherche"></span>

```pseudocode
algorithme recherche(T: [entier],
                     x: entier
                    ) → booléen:

    pour chaque (e := entier) de T:
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

## Objets manipulables par un programme

Le terme **fini** de la définition d'un programme/algorithme est crucial : pour qu'un humain comprenne, et surtout puisse agir, il faut que :

- chaque algorithme soit décri par un texte **fini**
- chaque instruction doit s'exécuter en un temps **fini** 
- chaque donnée manipulée doit être de taille **finie**

Donc la description du programme ainsi que les données doivent être décrite avec un _"langage"_ formé  avec des [mots d'un alphabet fini](<https://fr.wikipedia.org/wiki/Mot_(math%C3%A9matiques)>).

{% note2 "**Définition**" %}

On appelle :

- **_alphabet_** est un ensemble fini $\mathcal{A}$
- une **_lettre_** est un élément d'un alphabet
- un **_mot_** d'un alphabet $\mathcal{A}$ est une suite finie d'élément de $\mathcal{A}$
- la **_longueur_** d'un mot est lee nombre d'élément de la suite le constituant
- le **_mot vide_**, de longueur 0, est noté $\epsilon$
- l'ensemble de tous les mots d'un alphabet $\mathcal{A}$ est noté $\mathcal{A}^\star$
- un **_language_** est un sous-ensemble de $\mathcal{A}^\star$ (un ensemble, possiblement infini, de mots de $\mathcal{A}^\star$)

{% endnote2 %}

Par exemple le programme suivant qui énumère tous les entiers :

```text
Nom : énumère
Programme :
    x = 0
    répéter le bloc de deux instructions suivant :
        écrire x en base 10 sur une feuille de papier
        x = x + 1
```

Même si le programme ne s'arrête pas, chaque étape est bien finie : 

- `x` est toujours un entier que l'on peut décrire comme des mots de l'alphabet $\\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\}$
- écrire un nombre sur une feuille de papier est toujours possible et prendra un temps proportionnel aux nombre de ses chiffres à écrire.
- ajouter 1 à `x` est possible en posant l'addition et cela prendra un temps proportionnel à son nombre de chiffres et l'[on peut décrire le principe de l'addition en français](https://fr.wikipedia.org/wiki/Addition#Proc%C3%A9d%C3%A9_de_calcul), donc avec un nombre fini de symboles (les lettres, les chiffres et quelques symboles de ponctuation)


La conséquence fondamentale de ceci est que :

{% note "**Proposition**" %}
Un programme ne peut manipuler que des données de la forme d'une suite fini d'un ensemble fini.
{% endnote %}
{% details "preuve", "open" %}

Comme une donnée doit être lue en temps finie, elle doit être composée d'une liste finie d'éléments. Si le nombre d'éléments possibles était infini, il faudrait une description infinie de chaque instruction qui l'utiliserait.

{% enddetails %}

Une conséquence directe de la proposition précédente est qu'un programme ne peut pas manipuler de nombres réels.

{% attention "**À retenir**" %}
**Un réel ne l'est pas : c'est une limite**. 

Un réel est une abstraction que l'on peut considérer soit comme une approximation (ne considérer qu'un nombre fini de ses décimales) soit comme un symbole mais jamais en tant que nombre.
{% endattention %}



Prenons $\pi$ par exemple. Il existe des algorithmes qui [calculent les décimales de pi](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80#Calcul_de_la_n-i%C3%A8me_d%C3%A9cimale_de_%CF%80), mais on ne pourra jamais écrire que le nombre $\pi$ est le résultat d'un algorithme, puisque l'algorithme doit s'arrêter : on aura qu'un nombre fini de décimales, pas le nombre $\pi$. On ne pourra le considérer que de deux manières :

- soit comme un symbole et l'utiliser pour faire des opérations sur lui (comme $2 + \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaître sa valeur
- soit comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations.

Ce n'est pas bien grave en général puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) : considérer les réels en [notation scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique) en se fixant une précision ne gène pas les calculs physiques.

{% info %}
Faites tout de même attention car parfois, c'est problématique. Pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon), certes, mais aussi lorsque l'on prend l'inverse de choses très petites qui du coup deviennent très grandes. Ce sont des problèmes dit de [stabilité numérique](https://fr.wikipedia.org/wiki/Stabilit%C3%A9_num%C3%A9rique).
{% endinfo %}

Or :

<span id="paramètres-binaires"></span>

{% note2 "**Définition**" %}
Pour un ensemble $\mathcal{A}$, on note $(\mathcal{A})^\star$ l'ensemble de toutes les suites finies d'éléments de $\mathcal{A}$.
{% endnote2 %}
{% note "**Proposition**" %}

Il existe [une injection](https://fr.wikipedia.org/wiki/Injection_(math%C3%A9matiques)) entre $\mathcal{A}^\star$ et $\\{0, 1\\}^\star$ pour tout ensemble fini $\mathcal{A}$.

{% endnote %}
{% details "preuve", "open" %}

On va le montrer avec les chaînes de caractères pour se fixer les idées mais la généralisation à tout ensemble fini $\mathcal{A}$ est triviale.

On considère l'ensemble $\mathcal{U}$ des caractères des différentes langues écrites actuelles ou passée. Cet ensemble est fini et existe ! C'est l'ensemble [des caractères UNICODE](https://fr.wikipedia.org/wiki/Unicode) que l'on va noter. Il est constitué de 159801 caractères (appelées glyphes) dont chacun est associé un numéro. Par exemple le caractère 'A' est associé au numéro 65 et '𑒣' au numéro 70820.

Une chaîne de caractère $(c_i)_{0\leq i < n}$ est alors une suite de $6n$ chiffres. Par exemple : "Coucou toi !" correspond au nombre :

<div>
$$
\underbracket{000067}_{\text{C}}\underbracket{000111}_{\text{o}}\underbracket{000117}_{\text{u}}\underbracket{000099}_{\text{c}}\underbracket{000111}_{\text{o}}\underbracket{000117}_{\text{u}}\underbracket{000032}_{\text{ }}\underbracket{000116}_{\text{t}}\underbracket{000111}_{\text{o}}\underbracket{000105}_{\text{i}}\underbracket{000032}_{\text{ }}\underbracket{000033}_{\text{!}}
$$
</div>

Pour éviter tout soucis avec des données commençant par le caractère Unicode de nombre 0 (un même nombre peut avoir autant de chiffre 0 qu'il veut au début), on fait commencer toute données par le chiffre 1. La chaîne de caractères  "Coucou toi !" correspond ainsi au nombre :

<div>
$$
1000067000111000117000099000111000117000032000116000111000105000032000033
$$
</div>

Qui en notation binaire devient la suite finie :

<div>
$$
\begin{array}{l}
100100001110011010001011111100110010100110001101001001110110\\
101110011110110011000001101011011000000011010110111111101110\\
110101111000001001010010110011110000101011001101011000010110\\
011100101110101111101010100111000001111101111101100000100001
\end{array}
$$
</div>

On associe bien de façon unique à toute chaîne de caractères $(c_i)_{0\leq i < n}$ un élément de l'ensemble $\\{0, 1\\}^\star$. 
{% enddetails %}

La proposition précédente montre que l'on peut représenter toute suite finie d'éléments d'un ensemble fini par une suite finie de `0` et de `1` de façon unique. On en déduit le résultat que tout le monde connaît :

{% note2 "**Définition**" %}
Un caractère (`0` ou `1`) [est appelé **_bit_**](https://fr.wikipedia.org/wiki/Bit).
{% endnote2 %}

{% note "**Proposition**" %}
Tout ce que peut manipuler un programme est une suite finie de bits.
{% endnote %}

Cependant n'utiliser que des tableaux de bits (dont le type est `[bit]`) pour nos programmes les rendrait illisible. On défini donc d'autres types qui représentent nos données. Un tableau de bits pourra alors être interprété comme :

- un entier relatif :
  - positif en utilisant leur notation binaire et en les faisant commencer par un `0`, par exemple 3 sera encodé par `011` (le `0` tout à gauche signifiant que l'entier est positif)
  - négatif en utilisant [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) de la représentation binaire de son opposé. Ainsi -3 sera encodé par `101` (un entier négatif ainsi représenté commencera toujours par un `1`)
- une approximation finie d'un réel en utilisant la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754). Par exemple 3.1415 en codage IEEE 754 sur 32 bits correspond à l'entier binaire : `01000000010010010000111001010110` (j'ai utilisé [un convertisseur](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
- une chaîne de caractères en utilisant le code utf-8. Par exemple "Yop !" correspond au nombre hexadécimal 0x596F702021 (là aussi, j'ai utilisé [un convertisseur](http://hapax.qc.ca/conversion.fr.html)) qui en binaire vaut : `0000010110010110111101110000001000000010`

{% exercice %}
Montrez qu'il existe une injection entre $\mathcal{A}^\star$ et $\\{ 1\\}^\star$.

Pourquoi s'embêter avec un deuxième symbole (le `0`) alors ?
{% endexercice %}
{% details "corrigé" %}
Toute suite binaire est un nombre $n$ écrit en base 2. On peut donc représenter cette suite par $n$ `1` successifs.

On a cependant besoin d'un second caractère pour terminer la séquence lorsqu'on l'écrit ! Sinon, comment savoir lorsque le mot est fini ? On ne peut donc pas écrire toutes les suites juste avec un seul caractère puisqu'il en faut au moins un deuxième qui détermine la fin de la chaîne.

Dans la première définition [des machines de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing) les données de la machines sont décrites sur un ruban supposé infini dont les cases ne peuvent prendre que deux valeurs `1` et ` ` (blanc).

{% enddetails %}


Au final :

{% attention "**À retenir**" %}
On peut sans perte de généralité supposer que les seuls objets manipulables par un programme sont des suites finies de `0` et de `1`.

Alternativement, on peut aussi sans perte de généralité que les seuls objets manipulables par un programme sont des entiers positifs puisqu'une suite finie de `0` et de `1` est la représentation d'un entier en base 2.
{% endattention %}


## Nombres de paramètres d'entrée d'un programme

On vient de voir que tous les objets manipulables par des programmes peuvent être assimilé à des suites finies de `0` et de `1`, bref à des entiers représenté en base 2. On peut aller plus loin en représentant les tableaux de suites finies de `0` et de `1` par une unique suite finie de `0` et de `1`.
 
<div id="proposition-cartésien"></div>

{% note "**Proposition**" %}

Il existe une injection de $\\{0, 1\\}^\star \times \\{0, 1\\}^\star$ dans $\\{0, 1\\}^\star$.
{% endnote %}
{% details "preuve", "open" %}

On représente
On peut utiliser l'encodage suivant :

- le caractère `0` est encodé par la suite `10`
- le caractère `1` est encodé par la suite `11`
- le caractère de séparation est encodé par la suite `00`

Ainsi l'élément de `(00110, 110)` de $\\{0, 1\\}^\star \times \\{0, 1\\}^\star$ sera encodé par la suite `101011111000111110`. 

Il est clair que cet encodage est unique puisque :

- il sera de longueur paire
- commence par un 1
- chaque élément est codé par 2 bit

Ce qui assure que l'on peu retrouver le couple initial à partir de la suite finale.

{% enddetails %}

Cette proposition est vraiment importante Car elle montre que l'on peut toujours représenter un algorithme à $p > 1$ paramètres dans $\\{0, 1\\}^\star$ en un algorithme avec $p-1$ paramètres dans $\\{0, 1\\}^\star$ en fusionnant les deux premiers paramètres en utilisant l'injection définie dans la proposition et en les retrouvant en utilisant la procédure inverse au d´´but de l'algorithme !

Ceci montre que tout programme peut être écrit avec un unique paramètre dans $\\{0, 1\\}^\star$, quite à retrouver les paramètres initiaux en utilisant . Comme les suites finies de `0` et de `1` sont des entiers écrit en base 2, on obtient le résultat fondamental :

{% attention "**À retenir**" %}

Tout programme peut être écrit comme ayant :

- au plus une entrée dans $\\{0, 1\\}^\star$ 
- une sortie dans $\\{0, 1\\}^\star$ s'il s'arrête


**De manière équivalente**, tout programme peut être écrit comme ayant :

- au plus une entrée dans $\mathbb{N}$ 
- une sortie dans $\mathbb{N}$ s'il s'arrête

{% endattention %}

Arrêtez vous un instant sur les conséquences de ce que l'on vient de démontrer : on vient de montrer qu'il y a moins d'élément dans $\mathbb{Q}$ (l'ensemble des fractions entière qui est égal à la division de deux entiers et donc en bijection avec $\mathbb{N} \times \mathbb{N}$ lui même en bijection avec à $\\{0, 1\\}^\star \times \\{0, 1\\}^\star$)  que dans $\mathbb{N}$ (qui est en bijection avec à $\\{0, 1\\}^\star$). Étonnant, non ?

Terminons avec un petit exercice pour voir si vous avez compris :

{% exercice %}
Donnez un encodage permettant d'écrire comme une suite de `0` et de `1`  les listes imbriquées de tableaux de 0 et de 1, comme `[0, [1, [1]], 0]`.
{% endexercice %}
{% info %}
Encodez chaque caractère nécessaire (`0`, `1`, `,`, `[` et `]`) par son propre code sur 3 bits. 
{% endinfo %}
{% details "corrigé" %}

On peut utiliser le codage :

- le caractère `0` est encodé par la suite `100`
- le caractère `1` est encodé par la suite `101`
- le caractère de séparation `,` est encodé par la suite `000`
- le caractère `[` est encodé par la suite `110`
- le caractère `]` est encodé par la suite `111`

Par exemple `[0, [1, [1]], 0]` sera encodé par : `110100000110101000110101111111000100111`

{% enddetails %}

## Nombre de programmes

La définition générale d'un programme stipule qu'il doit être constitué d'un nombre **fini** d'instructions, chaque instruction décrite par un nombre **fini** de symboles. De plus, c'est implicite, mais un programme doit être compris par un humain.

On se place ici dans le cadre précédent où un programme prend en paramètre un entier et rend un entier.

### Une infinité de programmes différents

De la définition d'un algorithme on peut donc déjà conclure que :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes différents.
{% endnote %}
{% details "preuve", "open" %}
Le texte ci-dessous est un algorithme de deux instructions :

```text
Ne fait rien
rend 1
```

En notant alors $R_k$ ($k >0$) l'algorithme de $k$ instructions `Ne fait rien`{.language-} à la suite suivi de l'instruction `rend 1` (l'algorithme précédent est $R_1$).

Les algorithmes $R_k$ sont tous différents puisque leurs suites d'instructions sont différentes : il existe donc une infinité d'algorithmes différents.
{% enddetails %}

De la preuve de la proposition précédente montre qu'il existe une infinité d’algorithmes différents mais faisant la même chose : tous les algorithmes $R_k$ pour $k$ entier font la même chose, rien puis rendent 1.

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

D'après ce qui précède, un algorithme est un texte. On peut alors considérer que les symboles formant la description de chaque instruction sont des caractères pris dans l'alphabet [Unicode](https://fr.wikipedia.org/wiki/Unicode). De là :

{% note "**Proposition**" %}

Un **_programme_** est une suite finie $c_1 \dots c_n$ où :

- $c_i \in \mathcal{U}$ pour tout $1 \leq i \leq n$
- avec $\mathcal{U}$ l'ensemble des caractères [Unicode](https://fr.wikipedia.org/wiki/Unicode), $\vert \mathcal{U} \vert \leq 150000$.

{% endnote %}
{% details "preuve", "open" %}
Un programme est composée d'une suite finie d'instruction. Comme chaque instruction peut être nommée par un texte et que chaque instruction est décrite un texte en Français, tout algorithme est une suite de caractères Unicode.
{% enddetails %}

Bref, les programmes correspondent à un sous-ensemble de l'ensemble des chaînes de caractères écrites en Unicode. On peut alors utiliser [la proposition sur les suites binaires](./#paramètres-binaires){.interne} pour avoir la proposition suivante :

<div id="proposition-encodage-algorithme"></div>
{% note "**Proposition**" %}
On peut associer à tout programme un entier unique. C'est à dire qu'il existe une injection $N$ de l'ensemble $\mathcal{P}$ de tous les programmes vers l'ensemble des entiers.
{% endnote %}
{% details "preuve", "open" %}
Comme tout programme est une suite finie $c_1 \dots c_n$ de caractère Unicode, on utilise la technique de [la proposition sur les suites binaires](./#paramètres-binaires){.interne} puis lui associer un nombre unique.

{% enddetails %}


On déduit immédiatement la proposition suivante :

<span id="proposition-nb-dénombrable-algorithmes"></span>
{% note "**Proposition**" %}
Il y a exactement autant de programmes différents que de nombres entiers.
{% endnote %}
{% details "preuve", "open" %}

Soit $f: \mathcal{P} \rightarrow \mathbb{N}$ une injection permettant d'associer un entier à un programme donné.

On peut alors ordonner les programmes selon l'ordre induit par $N$. On note :

- $A_1$ est le programme de plus petit nombre associé
- pour $k > 1$, $A_k$ est l'algorithme est dont le nombre associé est le plus petit qui est plus grand que le nombre associé à $A_{k-1}$

On a alors :

- $A_k$ existe pour entier $k$ (puisqu'il y a une infinité de programmes différents, donc de descriptions différentes)
- pour tout programme $P$, il existe $k$ telle que $P=A_k$

Ce qui implique que la fonction qui associe à tout algorithme sa position dans la suite $(A_k)_{k \geq 1}$ est une bijection entre l'ensemble des programmes et l'ensemble des entiers strictement positifs.

{% enddetails %}

La preuve ci-dessus est classique et est basée sur le fait que deux ensembles sont de même cardiaux que s'il existe une bijection entre les deux. Cette définition est évidente lorsque les ensembles sont fini et elle s'étend lorsque les ensemble sont infinis :

{% note2 "**Définition**" %}
Un ensemble est dénombrable s'il est en bijection avec $\mathbb{N}$.
{% endnote2 %}

Il faut faire un peut attention avec les infinis, par exemple les deux fonctions suivantes sont des injections :

- $f(n) = 2n$ pour entier positif $n$,
- $g(n) = 2n-1$ pour entier positif $n$.

Ceci montre que :

- les entiers sont en bijection avec $f(\mathbb{N})$ c'est à dire les entiers pairs
- les entiers sont en bijection avec $g(\mathbb{N})$ c'est à dire les entiers impair

Bref : il y a autant d'entier que d'entier pair que d'entiers impair !

{% attention "**À retenir**" %}
Ceci montre que lorsqu'il y a un nombre infini d'entiers (_ie._ d'élément d'un ensemble dénombrable), il y en a autant que d'entiers. 
{% endattention %}

À vous, pour voir si vous avez compris :

{% exercice %}
Montrez que l'ensemble des mots d'un alphabet fini est dénombrable.
{% endexercice %}

{% details "corrigé" %}

L'alphabet est fini on peut donc ordonner ses lettres, puis ordonner ses mots dans l'ordre du dictionnaire :

le mot vide, puis tous les mots de longueur 1, puis tous ceux de longueur 2, etc.

{% enddetails %}

La remarque précédente est un cas particulier d'[un théorème plus général que l'on doit à Cantor et Bernstein](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cantor-Bernstein) :

{% note "**Proposition**" %}
S'il y a une injection d'un ensemble $E$ dans une partie $F$ de celui-ci, alors $E$ et $F$ sont en bijection.

{% endnote %}
{% details "preuve", "open" %}

On suppose que $f$ est une injection de $E$ dans $F \subsetneq E$ et on note :

<div>
$$
G_i \coloneqq \begin{cases}
        G_0 = E \backslash F & \text{si } i = 0\\
        G_{i} = f(G_{i-1}) & \text{sinon }
    \end{cases}
$$
</div>

On note alors 

<div>
$$
G \coloneqq \cup_{i \in \mathbb{N}} G_i \subseteq F
$$
</div> 

Et $g$ la fonction de $E$ dans $F$ telle que :

<div>
$$
g(x) \coloneqq \begin{cases}
        f(x) & \text{si } x \in G\\
        x & \text{sinon}
    \end{cases}
$$
</div>

Nous allons montrer que $g$ est une bijection de $E$ dans $F$, ce qui conclura la preuve :

- $g$ est une injection car :
  - si $x \in G$, alors $g(x) = f(x) \in G$ et $g$ est une injection de $G$ dans $G$
  - si $x \notin G$, $g(x)$ est l'identité $E\backslash G$ dans $E\backslash G$
- $g$ est une surjection car si $x \in F$, alors il existe un entier $i$ tel que $x \in G_i$. Soit $i^\star$ le plus petit $i^\star$ tel que $x \in G_{i^\star}$. On a $i^\star > 0$ puisque $F \cap G_0 = \varnothing$ et donc il existe $y \in G_{i^\star -1}$ tel que $f(y) = x$

{% enddetails %}
{% note "**Corollaire (Théorème de Cantor-Bernstein)**" %}
S'il y a une injection d'un ensemble $A$ dans un ensemble $B$  et une injection de $B$ dans $A$, alors $A$ et $B$ sont en bijection.
{% endnote %}
{% details "preuve", "open" %}

Soit :

- $f$ une injection de $A$ vers $B$
- $g$ une injection de $B$ vers $A$

Donc $f \circ g$ est une injection de $B$ dans $f(A) \subseteq B$ : la proposition précédente montre qu'il existe une bijection $h$ de $B$ dans $f(A)$.

Comme $f$ est une bijection de $f$ dans son image $f(A)$, $h^{-1} \circ f$ est une bijection de $A$ vers $B$ ce qui conclut la preuve.

{% enddetails %}
{% info %}
[Référence](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cantor-Bernstein#Premi%C3%A8re_d%C3%A9monstration)
{% endinfo %}

Jouer avec l'infini est à la fois rigolo et donne le vertige. De nombreux résultats sont contre-intuitif comme le résultat précédent qui montre qu'il peut y avoir autant d'élément dans un ensemble et une partie de celui-ci. 

On peut grâce au résultat précédent démontrer :

{% note "**Proposition**" %}

Les ensembles $\mathbb{N}$ et $\mathbb{Q}$ sont en bijection.
{% endnote %}
{% details "preuve", "open" %}


On utilise [la proposition du produit cartésien](./#proposition-cartésien) qui montre qu'il existe une injection de $\mathbb{N}$ dans $\mathbb{Q}$ et comme les entiers sont dans $\mathbb{Q}$ (c'est $n / 1$) il existe une injection de $\mathbb{Q}$ dans $\mathbb{N}$

{% enddetails %}

D'un point de vue informatique, on conclut de cette partie que tout ce qu'on manipule en informatique sont des suites finies de `0` et de `1`, que ce soit les données ou les programmes eux-même :

{% attention "**À retenir**" %}

On peut définir sans perte de généralité un algorithme comme étant une suite finie de `0` et de `1` qui prend en paramètre d'entrée une suite de finie de `0` et de `1` et rend en sortie une suite finie de `0` et de `1`.

Connaître les données ou les instructions "réels" d'un algorithme se fait via des procédures qui transforment les suites de finies de `0` et de `1` :

- en instructions
- en données

{% endattention %}


Pour finir, un petit résultat très utile que vous pouvez démontrer :

{% exercice %}
On peut définir sans perte de généralité un algorithme comme étant une suite finie de `0` et de `1` qui prend en paramètre d'entrée une suite de finie de `0` et de `1` et rend en sortie `1` ou `0`.

{% endexercice %}
{% details "corrigé" %}

Soit $A$ un algorithme qui à partir d'une entrée $E$ donne une sortie $S$.
Le couple $(E, S)$ est formellement un élément de $\mathbb{Q}$ (on associe la suite finie de `0` et de `1` à un nombre écrit en base 2). En utilisant une bijection $f$ entre $\mathbb{Q}$ et $\mathbb{N}$ on peut lui associer un nombre $F(E, S)$ donc une suite finie de `0` et de `1`.

De là on peut associer à notre algorithme l'unique algorithme :

```
A'(E):
    E', S' = f^{-1}(E)
    S'' = A(E')

    Si S' == S'':
        rendre 1
    sinon:
        rendre 0
```


{% enddetails %}
{% exercice %}
Déduire de l'exercice précédent qu'un algorithme peut être vu comme un langage de $\\{0, 1\\}$.
{% endexercice %}
{% details "corrigé" %}
On considère les algorithmes comme vu dans l'exercice précédent, c'est à dire une suite finie de `0` et de `1` qui prend en paramètre d'entrée une suite de finie de `0` et de `1` et rend en sortie `1` ou `0`.

Et on associe à un algorithme $A$ le langage formé de toutes les entrées pour lesquelles il rend `1`.
{% enddetails %}

## Algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (cela a plus sa place dans un cours de logique ou de calculabilité) mais, en gros, les mathématiques sont une partie de l'informatique (certains diraient même, et réciproquement. Des mathématiciens certainement...).

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3))


{% attention "**À retenir**" %}

Algorithmes et démonstrations mathématiques sont deux notions équivalentes.

{% endattention %}
