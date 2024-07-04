---
layout: layout/post.njk

title: Pseudo-assembleur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons présenter une version _"minimale"_ de pseudo-code que nous appellerons pseudo-assembleur. Cet assembleur idéal et théorique nous permettra de faire le lien entre pseudo-code et le langage machine qui est effectivement exécuté.

## Objet et variables

{% note "**Définition**" %}
Les objets que peut manipuler le pseudo-assembleur sont les caractères `0` et `1` et les suites finies de ces caractères.
{% endnote %}

Par exemple l'objet de nom `o` :

```python
o = 1011001
```

Dans un pseudo-code, l'endroit où sont stockés les objets n'est pas défini, dans le pseudo-assembleur, on les stocke explicitement dans un tableau nommé **_mémoire_** :

{% note "**Définition**" %}
La **_mémoire_** est un tableau $M$ de taille $N$ où chaque case peut contenir soit le caractère `0`, soit le caractère `1`.
{% endnote %}

Chaque objet $o = o_0\dots o_{p-1}$, une suite finie de `0` et de `1`, est stocké dans des cases contiguës de la mémoire.

L'objet `o` de tout à l'heure sera alors rangé :

```python
    01234567
o = 11010100

M[i + 0] = 1
M[i + 1] = 1
M[i + 2] = 0
M[i + 3] = 1
M[i + 4] = 0
M[i + 5] = 1
M[i + 6] = 0
M[i + 7] = 0
```

Attention à la lecture, **_le bit de poids fort_** de l'objet, celui le plus à gauche, est d'indice le plus petit.

{% attention %}
Les bits de l'objet sont numérotés dans l'ordre opposé de leur lecture. On appelle cette **convention** [**_big endian_** (ou gros boutisme en français)](https://fr.wikipedia.org/wiki/Boutisme).

Comme toute convention, certains prennent la convention opposée, dite **_little endian_** (ou petit boutisme en français).
{% endattention %}

Ce stockage permet de définir les références :

{% note "**Définition**" %}
Une _**référence**_ d'un objet est l'adresse du premier indice en mémoire le contenant.
{% endnote %}

Une variable est alors une référence nommée :

{% note "**Définition**" %}
Une _**variable**_ est un nom auquel est associé une référence à un objet.
{% endnote %}

La mémoire étant finie, la référence à un objet est toujours codée sur $S = \log_2(N)$ bits.

{% note "**Définition**" %}
La taille $N$ de la mémoire sera toujours une puissance de $2$. On notera $S = \log_2(N)$$, la taille (entière et en bit) du codage binaire d'une adresse.
{% endnote %}

Ceci permet de définir rigoureusement un tableau :

{% note "**Définition**" %}
Un _**tableau**_ de taille $n$ est suite finie et contiguë de $n \cdot S$ cases mémoire. Chaque $S$ bits successifs en mémoire contient la référence d'un objet.
{% endnote %}

> TBD : exemple avec mémoire, objet et tableau. Et variables nommées qui les références. Pour l'instant, les variables ne sont pas en mémoire (on le fera avec la pile et le modèle de von Neumann).

### Objets entiers

L'objet entier n'existe pas à proprement parler, mais on suppose qu'une suite finie de $S = \log_2(N)$ bits, qui correspond à une adresse, peut aussi être vue comme un entier. Pour cela, on on possède les deux fonctions suivantes :

- $u: \\{0, 1\\}^{S}\rightarrow \mathbb{N}$ qui rend l'entier associé à la suite considérée comme sa représentation binaire
- $s: \\{0, 1\\}^{S}\rightarrow \mathbb{Z}$ qui rend l'entier associé à la suite considérée comme sa représentation binaire en [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) sur $S$ bits.
- $b: \mathbb{Z} \rightarrow  \\{0, 1\\}^{S}$ qui rend la représentation binaire en [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) sur $S$ bits associé à l'entier.

Pour l'objet `o = 1011001` précédent, on a :

- `u(o) = 212`
- `s(o) = -44`

Si `o` code un entier, c'est qu'une adresse mémoire est codée sur 8bits et donc que sa taille vaut $N = 2^8 = 256$.

### Équivalence avec le pseudo-code

On l'a vu, [un programme ne peut manipuler que des suites finies de `0` et de `1`](../../bases-théoriques/définition/#paramètres-binaires){.interne}. Le pseudo-code et le pseudo-assembleur manipulent les mêmes objets.

De plus, la finitude de la mémoire n'est pas un problème pour les algorithmes puisqu'ils finissent. On pourra donc toujours trouver une taille de mémoire permettant de l'exécuter. De là, si un programme en pseudo-assembleur atteint la limite de la mémoire, on peut toujours stopper son exécution et la recommencer avec une mémoire deux fois plus grande. L'algorithme en pseudo-assembleur finira toujours par s'arrêter. On a donc :

{% note "**Proposition**" %}
Pseudo-assembleur et pseudo-code sont équivalent pour la gestion des objets.
{% endnote %}

## Fonctions et appel de fonctions

En pseudo-code, on appelle les fonctions via des paramètres :

```python
ma_fonction(p1, ..., pn)
```

En pseudo-assembleur, une fonction est appelée avec un unique paramètre $p$ qui correspond à une adresse mémoire d'un tableau $t$ à $n$ adresses telle que :

1. $M[p]$ soit l'adresse du début d'un objet tableau $t$ de taille $n$
2. $t[i]$ corresponde à l'adresse du paramètre $p_i$
3. si $k = \log_2(N)$ vaut le nombre de bits pour stocker une adresse, alors aucun objet n'est pour l'instant stocké à une adresse supérieure à $k \cdot n$ : le tableau $t$ est le dernier objet stocké en mémoire par l'algorithme.

Les deux premières conditions permettent de ne pas faire de différence entre paramètre de fonctions et objet de l'algorithme et la troisième permet d'appeler facilement des fonction de manière récursive !

Par exemple la fonction de Fibonacci que l'on pourrait écrire en pseudo-code :

```python
def fibo(a, b, n):
  si n ≤ 1:
    return a
  sinon:
    return fibo(a + b, a, n - 1)

affiche à l'écran fibo(1, 1, 3)
```

Deviendrait en pseudo-assembleur :

```python
def fibo(p):
  a = u(M[p:p+S])
  b = u(M[p + S:p + 2 * S])
  n = u(M[p + 2 * S:p + 3 * S])

  si n ≤ 1:
    stocke a dans les cases M[p + 3 * S:p + 4 * S]
    return p + 3 * S
  sinon:
    stocke l'entier a + b dans les cases M[p + 3 * S:p + 4 * S]
    stocke l'entier a dans les cases M[p + 4 * S:p + 5 * S]
    stocke l'entier n-1 dans les cases M[p + 5 * S:p + 6 * S]

    return fibo(p + 3 * S)

  affiche à l'écran u(M[fibo(1, 1, 3)])
```

La fonction `fibo` retourne l'adresse d'un entier en mémoire et est correcte puisque l'on sait qu'aucun objet n'est stocké après le tableau de paramètre : l'appel récursif ne peut pas faire planter l'algorithme.

> TBD dérouler l'exemple (avec la mémoire représentée à chaque exécution de ligne)

L'utilisation de ce tableau de paramètre en mémoire permet d'avoir :

{% note "**Proposition**" %}
Pseudo-assembleur et pseudo-code sont équivalent pour la gestion des fonctions.
{% endnote %}

## Structures de contrôles

On associe à chaque ligne du programme en pseudo-assembleur un **_label_**, qui correspond à son numéro de ligne. Cet ajout va permettre de gérer les structures de contrôles et les tests sans blocs : uniquement avec des sauts.

### Saut

On ajoute au pseudo-assembleur une instruction de saut :

```python
GOTO label
```

L'instruction `GOTO` ("go to" : "aller à") _saute_ à l'instruction de label `label`. Par exemple le programme suivant qui est une version itérative (et infinie) de la suite de Fibonacci :

```python#
a = M[0:S] = b(1)
b = M[S:2S] = b(1)
n = M[2S:3S] = b(1)

affiche à l'écran n, a

n = n + 1
a, b = a + b, a

GOTO 8
```

> TBD : dérouler l'exemple (avec la mémoire représentée à chaque exécution de ligne)
> dire qu'on a assimiler variable et case mémoire.

{% attention %}
L'utilisation de saut était très répandu dans les débuts de la programmation (des langages comme [le C en possède une instruction de saut](https://koor.fr/C/Statements/goto.wp#google_vignette)), mais son usage a été banni pour être remplacé par des blocs car il rendait le code très difficile à lire.

{% endattention %}
{% aller %}
[Célèbre article de Dijkstra contre l'utilisation des sauts en programmation](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf).
{% endaller %}

Notez que les sauts peuvent être utilisés pour des appels de fonctions ! Il suffit de permettre le saut à partir d'une variable. Le code suivant utilise la variable `I` pour stocker l'endroit où sauter après l'exécution de la fonction :

```python
GOTO 6

affiche à l'écran n, a
GOTO I

a = M[0:S] = b(1)
b = M[S:2S] = b(1)
n = M[2S:3S] = b(1)

I = 12
GOTO 3

n = n + 1
a, b = a + b, a

I = 18
GOTO 3

GOTO 5
```

{% note "**Proposition**" %}
L'appel de fonction en pseudo-assembleur se fait avec des instruction de saut et une variable contenant la ligne de retour.
{% endnote %}
{% attention %}
Dans ce cas là, le nombre de ligne de code est borné par l'adressage possible en mémoire. Ce n'est pas gênant en pratique, un adressage sur 64bit permet d'écrire $2^{64}$ lignes de code...
{% endattention %}

### Test

Les tests en pseudo-code sont de deux types :

- arithmétiques, comme $a < b$
- logique, comme $(A OU B) ET C$

Ils n'existent pas à proprement parler en pseudo-assembleur, mais ils peuvent être simulé grâce aux **_drapeaux_**.

{% note "**Définition**" %}
Un **_drapeau_** (**_flag_**)  est une variable binaire affectée automatiquement après une opération.
{% endnote %}

En particulier, on considère que le pseudo-assembleur possède les deux drapeaux suivant, qui permettent de faire tous les tests du pseudo-code :

{% note "**Définition**" %}
Le pseudo-assembleur possède les deux drapeaux :

- `NÉGATIF` qui vaut `1` si la dernière opération arithmétique a donné un résultat négatif, et `0` sinon.
- `ZÉRO` qui vaut `1` si la dernière opération arithmétique ou logique a donné un résultat de zéro, et `0` sinon.
{% endnote %}

Ainsi :

- $a \leq b$ pourra être effectué en regardant la valeur du drapeau `NÉGATIF` après l'opération $b-a$.
- $(A OU B) ET C$ pourra être effectué en regardant la valeur du drapeau `ZÉRO` (s'il vaut `0`, c'est vrai)

On a donc :

{% note "**Proposition**" %}
On peut créer les mêmes tests en pseudo-assembleur et en pseudo-code.
{% endnote %}

### Saut conditionnel

Enfin, pour permettre de construire les structures de contrôle du pseudo-code, on ajoute les **_sauts conditionnels_** :

{% note "**Définition**" %}
Un saut conditionnel est de la forme :

```python
IFGOTO drapeau label
```

La prochaine instruction exécutée sera celle de la ligne `label` si le drapeau de nom `drapeau` vaut `1`.

De même :

```python
IFNOTGOTO drapeau label
```

La prochaine instruction exécutée sera celle de la ligne `label` si le drapeau de nom `drapeau` vaut `0`.

{% endnote %}

Le code ci-après utilise le saut conditionnel pour afficher les 11 premières valeurs de la suite de Fibonacci.

```python#
a = M[0:S] = b(1)
b = M[S:2S] = b(1)
n = M[2S:3S] = b(1)

affiche à l'écran n, a

n = n + 1
a, b = a + b, a

n-10
IFNOTGOTO NÉGATIF 5

affiche à l'écran "FIN", n, a
```

Comme on le voit, il est facile de remplacer les structures de contrôles et les répétitions du pseudo-code par une utilisation combinée des labels et des sauts conditionnels :

{% note "**Proposition**" %}
On peut créer les mêmes structure de contrôles et les boucles en pseudo-assembleur et en pseudo-code.
{% endnote %}

## Opérations

Les opérations autorisées en pseudo-code sont de deux ordres : logique et arithmétiques. Les autres opérations (concaténation de chaines de caractères, manipulation d'approximation de réels, ...) se déduisent de ces deux catégories. Les opérations logiques et arithmétiques fonctionnent toutes de la même manière :

- elles prennent au plus 2 paramètres
- elles rendent au plus 1 objet

Par exemple l'addition (2 paramètres et une sortie) ou la négation (1 paramètre et une sortie). Notez que les opérations qui rendent plus que une sortie (comme la division euclidienne par exemple) peuvent être décomposées en plusieurs opérations rendant chacune une unique sortie (division entière et modulo pour la division euclidienne).

{% note "**Définition**" %}

Le schéma général d'une **_opération_** en pseudo-assembleur est :

```python
OP #1 #2 #3 
```

Où :

- `OP` est le [code mnémonique](https://fr.wikipedia.org/wiki/Code_mn%C3%A9monique) associée (le nom) à l'opération
- `#1`, `#2` et `#3` représentent les paramètres de l'opération et peuvent représenter soit des entrées soit une sortie selon l'opération.

{% endnote %}

Les paramètres d'entrées et la sortie sont stockés dans des [registres](https://fr.wikipedia.org/wiki/Registre_de_processeur) qui sont des variables spéciales.

### Registres

{% note "**Définition**" %}

Un **_registre_** est une mémoire de taille $S$ (donc suffisante pour stocker une adresse). Il en existe deux types :

- les registres génériques qui peuvent indépendamment être utilisé comme entrée et sortie d'une opération. Ils sont désignés par un numéro `$1`, `$2`, etc.
- les registres spécifiques qui véhiculent des informations précisent et sont souvent en lecture seule (les drapeaux sont des registres spécifiques par exemple).

{% endnote %}

Les registres permettent de faire fonctionner le pseudo-assembleur et forment les liens entre opérations et mémoire. Les opérations permettant de déplacer les valeurs des registres à la mémoire et inversement sont :

- `LOAD $X $Y` qui place la valeur en mémoire `M[u($Y):u($Y)+S]`  (`u($Y)` est la valeur du registre de numéro `Y` prise comme une adresse) dans le registre de numéro `X`
- `STORE $X $Y` qui place la valeur du registre `X` dans les cases mémoires `M[u($Y):u($Y)+S]`
- `SET $X Y` qui place la constante `Y` (une suite de 0 et de 1 de taille $S$) dans le registre de numéro `X`

> TBD exemple avec image de la mémoire et de 2 registres.

### Types d'opérations

Les opérations d'un pseudo-assembleur, comme pour un pseudo-code sont essentiellement arithmétique

#### Logiques

Les opérations logiques sont des fonctions de $\\{0, 1\\}^p \rightarrow \\{0, 1\\}$, avec $p$ valant 0 ou 1. On les représentent via leurs [tables de vérité](https://fr.wikipedia.org/wiki/Table_de_v%C3%A9rit%C3%A9).

Si $p$ vaut, il n'y a qu'une seule opération différente de l'identité :

{% note "**Définition**" %}
La fonction $\text{NOT}(x) = \bar{x}$ est définie selon la table de vérité suivante :

x | NOT
--|----
0 | 1
1 | 0

Elle _inverse_ son paramètre.
{% endnote %}

Si $p$ vaut 2, on a coutume d'utiliser les deux fonctions suivantes :

{% note "**Définition**" %}
La fonction $\text{AND}(x, y) = x \land y$ est définie selon la table de vérité suivante :

x | y | AND
--|----
0 | 0 | 0
1 | 0 | 0
0 | 1 | 0
1 | 1 | 1

Elle est vraie si $x$ et $y$ sont vrais.
{% endnote %}

{% note "**Définition**" %}
La fonction $\text{OR}(x, y) = x \lor y$ est définie selon la table de vérité suivante :

x | y | AND
--|---|----
0 | 0 | 0
1 | 0 | 1
0 | 1 | 1
1 | 1 | 1

Elle est vraie si $x$ ou $y$ est vrai.
{% endnote %}

Ces trois fonctions sont fondamentales :

{% note "**Proposition**" %}
Toute fonction de $\\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ peut s'écrire comme combinaison des fonctions $\text{NOT}(x)$, $\text{AND}(x, y)$, et $\text{OR}(x, y)$.

{% endnote %}
{% details "preuve", "open" %}

Il y a 16 possibilités de fonctions :

x | y | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16  
--|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----
0 | 0 | 0  | 1  | 0  | 0  | 0  | 1  | 1  | 1  | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  
1 | 0 | 0  | 0  | 1  | 0  | 0  | 1  | 0  | 0  | 1  | 1  | 0  | 1  | 1  | 0  | 1  | 1  
0 | 1 | 0  | 0  | 0  | 1  | 0  | 0  | 1  | 0  | 1  | 1  | 1  | 0  | 1  | 1  | 0  | 1  
1 | 1 | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 1  | 1  | 1  | 1  | 1  | 0  | 1  | 1  | 0  

On a :

- la fonction $f_i = \overline{f_{i+8}}$ pour $1\leq i \leq 8$
- $f_1$ est la fonction constante valant 0
- $f_{2+8}(x, y)$ est la fonction $x \lor y$
- $f_{3}(x, y) = f_{4}(y, x)$ et $f_{3+8}$ est la fonction $\bar{x} \lor y$
- $f_{5}(x, y)$ est la fonction $x \land y$
- $f_{6}(x, y)$ est la fonction $\bar{y}$
- $f_{7 + 8}(x, y)$ est la fonction $x$
- $f_{8 + 8}(x, y)$ est la fonction $(x \land \bar{y}) \lor (\bar{x} \land y)$
{% enddetails %}

Le résultat précédent se généralise pour tout $p$. Pour cela, commençons par définir un concept fondamental en logique la _**conjonction de clauses**_ :

{% note "**Définition**" %}
Soient $x_1, \dots, x_n$, $n$ variables binaires. On définit :

- un **_littéral_** $l$ comme étant soit une variable $l = x_i$, soit sa négation $l = \overline{x_i}$
- une **_clause_** comme étant une disjonction de littéraux $c = l_1 \lor \dots \lor l_k$ (avec $l_1, \dots l_k$ littéraux)
- une **_conjonction de clauses_** comme étant $c = c_1 \land \dots \land c_m$ (avec $c_1, \dots c_m$ des clauses)
{% endnote %}

Toute fonction $f: \\{0, 1\\}^n \rightarrow \\{0, 1\\}$ peut alors s'écrire comme une conjonction de clauses :

{% note "**Proposition**" %}
Toute fonction de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$ peut s'écrire comme une conjonction de clauses.
{% endnote %}
{% details "preuve", "open" %}

Soit $f(x_1, \dots, x_n)$ une fonction de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$.

À tout élément $x=(x_1, \dots, x_n)$ de $\\{0, 1\\}^n$ on peut associer la fonction $l^x(y_1, \dots, y_n) = l^x_1 \land \dots \land l^x_i \land \dots \land l^x_n$ où $l^x_i = y_i$ si $x_i = 1$ et $l^x_i = \overline{y_i}$ sinon. La fonction $f$ est alors égale à :

$$
f(x) = \lor \\{l^y(x) | f(y) = 1\\}
$$

Comme $(a \land b)\lor c = (a \lor c)\land (b \lor c)$, $f$ peut se récrire en conjonction de clauses ce qui conclut la preuve.

{% enddetails %}

On voit qu'il suffit que le pseudo-assembleur définisse les fonctions $\text{NOT}(x)$, $\text{OR}(x, y)$ et $\text{AND}(x, y)$ pour des variables $x$ et $y$ binaires pour pouvoir générer toutes les fonctions de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$, quelque soit l'entier $n$. On peut aller encore plus loin grâce à la proposition suivante :

{% note "**Proposition**" %}
Les fonctions $\text{NOT}(x)$, $\text{OR}(x, y)$ et $\text{AND}(x, y)$ pour des variables $x$ et $y$ binaires peuvent s'écrire comme compositions de fonctions $\text{NAND}(x, y) = \text{NOT}(\text{AND}(x, y))$
{% endnote %}
{% details "preuve", "open" %}

> TBD

{% enddetails %}
{% note %}
> TBD cela marche aussi avec XOR.
{% endnote %}

Son pendant en
L'opération `NOT $1 $2`, ou 
, dont la table de vérité est :

Si 
> bit à bit
> peut se généraliser sur tout un registre
> peut se généraliser à aussi long qu'on veut : on peut découper

> TBD faire une partie arithmétique booléenne ?

On peut tout faire avec une combinaison de not, and et or : c'est une clause.


#### Arithmétiques

> addition dans 0,1 est une fonction sur 0, 1, donc logique. Elle est de plus découpable avec une retenue (registre)
> 
> avec complément à deux parce que soustraction = addition

> a priori opération aussi grande qu'on veut mais on peut découper. Exemple sur logique et 1 seul bit. Ou addition et retenue.
deux catégories

On verra que l'on peut même se restreindre à une seule opération pour construire toutes les autres, mais commençons par formaliser comment le pseudo-assembleur utilise les opérations.

> TBD parler des additions/soustraction etc par bout de taille fixe. plus drapeau retenue pour permettre de faire sur taille pas fixe si besoin.
> On peut tout faire avec add et on peut faire add avec XOR.
> Opérations logiques avec NANDm donc juste NAND pour tout faire.

Le pseudo-code doit permettre de faire les opérations arithmétiques courantes sur les objets :

- plus, moins, fois et divisé pour les entiers relatifs et les approximations des réels
- plus, moins, fois et divisé pour les approximations de réels
- concaténation des chaines de caractères

L'intérêt d'utiliser des suites binaires est que toutes les opérations arithmétiques peuvent se réaliser avec les deux opérations logiques suivantes :

- `copie(x)`
- `SHIFT(x, y)` rend un objet contenant la concaténation de y0...0 ajout de s(x) 0 à droite de y si s(x) > 0 et de -s(x) 0 à gauche si s(x) < 0
- `NAND(x, y)` : opérateur logique NON ET.

En effet, il est possible d'[obtenir toutes les opérations logiques avec NAND](https://en.wikipedia.org/wiki/NAND_logic) et l'opération SHIFT permet d'ajouter des bits à gauche ou à droite d'un objet (si on veut ajouter des 1 on peut fait NOT(SHIFT(x, NOT(y))))

Ou 1 ou 2 paramètre et une sortie.

### Équivalences

{% note "**Proposition**" %}
> TBD que NAND sur 1 bit
{% endnote %}

## I/O

> TBD pas core (il suffit de regarder la mémoire), mais utile

- afficher à l'écran
- fichier et clavier ?

## MMIX

Nous n'avons montré que le principe d'un pseudo-assembleur, juste assez pour nous convaincre que les notions de pseudo-code et pseudo-assembleurs sont équivalentes.

Donald Knuth a formellement décrit un pseudo-assembleur complet, nommée [MMIX](https://fr.wikipedia.org/wiki/MMIX). Je ne saurais trop vous conseiller d'aller jeter un coup d'œil au site qui explique son fonctionnement, comme toujours avec Knuth, de façon claire et précise :

{% lien %}
<https://mmix.cs.hm.edu/>
{% endlien %}
