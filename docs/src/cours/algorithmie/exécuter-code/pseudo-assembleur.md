---
layout: layout/post.njk

title: Pseudo-assembleur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD ici dire qu'on peut augmenter la taille.
> 
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
>
> TBD : le fait que ce soit fini ne change rien :
>
> - à l'exécution : si on dépasse on double la mémoire et on recommence
> - à la complexité : le temps mis/nb d'instruction effectué est T(sum i/2^i) = 2T. Voir universal search

### Objets entiers

L'objet entier n'existe pas à proprement parler, mais on suppose qu'une suite finie de $S = \log_2(N)$ bits, qui correspond à une adresse, peut aussi être vue comme un entier. Pour cela, on on possède les deux fonctions suivantes :

- $u: \\{0, 1\\}^{S}\rightarrow \mathbb{N}$ qui rend l'entier associé à la suite considérée comme sa représentation binaire
- $s: \\{0, 1\\}^{S}\rightarrow \mathbb{Z}$ qui rend l'entier associé à la suite considérée comme sa représentation binaire en [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) sur $S$ bits.
- $b: \mathbb{Z} \rightarrow  \\{0, 1\\}^{S}$ qui rend la représentation binaire en [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) sur $S$ bits associé à l'entier.

Pour l'objet `o = 1011001` précédent, on a :

- `u(o) = 212`
- `s(o) = -44`

Si `o` code un entier, c'est qu'une adresse mémoire est codée sur 8bits ($S = 8$) et donc que sa taille vaut $N = 2^8 = 256$. Pour affecter des entiers dans la mémoire on écrira alors :

```
M[X:X+S] = b(212)
```

Qui sera équivalent à `M[X:X+S] = 1011001` si $S=8$ et à `M[X:X+S] = 000000001011001` si $S=16$.

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

En pseudo-assembleur, une fonction est appelée avec un unique paramètre $p$ qui correspond à une adresse mémoire d'un tableau à $n$ adresses telle que :

1. $M[p+(i-1)S:p+iS]$ corresponde à l'adresse du paramètre $p_i$
2. Pour tout $k \geq p+nS$, Aucune case mémoire $M[k]$, n'est utilisée pour l'instant par le programme.

La  première condition permet de ne pas faire de différence entre paramètre de fonctions et objet de l'algorithme et la seconde permet d'appeler facilement des fonction de manière récursive !

Par exemple la fonction factorielle que l'on pourrait écrire en pseudo-code :

```python
def factorielle(n):
  si n ≤ 1:
    return 1
  sinon:
    return n * factorielle(n-1)

affiche à l'écran factorielle(3)
```

Deviendrait en pseudo-assembleur :

```python/
def factorielle(p):
  si u(M[p:p+S]) ≤ 1:
    return 1
  sinon:
    M[p + S:p +2*S] = b(u(M[p:p+S]) - 1)
    return u(M[p:p+S]) * factorielle(p + S)

M[0:S] = b(4)
affiche à l'écran factorielle(0)
```

Lors de l'exécution du code précédent, la fonction factorielle va être appelée quatre fois. Voyons ça pour $S=4$ et donc une taille mémoire de 32bits.

premier appel depuis la ligne 9 du programme `factorielle(0)` :

```
0         1         2         3
012345678901234567890123456789012
010000000000000000000000000000000
p
```

Comme u(M[0:0+4]) vaut 4, on rappelle factorielle en ligne 6, `factorielle(4)` :

```
0         1         2         3
012345678901234567890123456789012
010000110000000000000000000000000
    p
```

Comme u(M[4:4+4]) vaut 3, on rappelle factorielle en ligne 6, `factorielle(8)` :

```
0         1         2         3
012345678901234567890123456789012
010000110010000000000000000000000
        p
```

Comme u(M[8:8+4]) vaut 2, on rappelle factorielle en ligne 6, `factorielle(12)` :

```
0         1         2         3
012345678901234567890123456789012
010000110010000100000000000000000
            p
```

Comme u(M[12:12+4]) vaut 1 : `factorielle(12)` rend `1`. On se trouve donc dans la fonction `factorielle(8)` qui peut maintenant également s'arrêter en rendant `u(M[8:8+4]) * factorielle(12)` qui vaut : $2 \cdot 1 = 2$.

De là `factorielle(4)` s'arrête en rendant `u(M[4:4+4]) * factorielle(8)` qui vaut : $3 \cdot 2 = 6$ ce qui permet à `factorielle(0)` de rendre `u(M[0:0+4]) * factorielle(4)` qui vaut $4 \cdot 6 = 24$.

L'utilisation de ce tableau de paramètres en mémoire permet d'avoir :

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

L'instruction `GOTO` ("go to" : "aller à") _saute_ à l'instruction de label `label`. Par exemple le programme suivant qui est une version itérative (et infinie) de la factorielle :

```python/
M[0:S] = b(1)
M[S:2S] = b(1)

affiche à l'écran u(M[0:S])

M[S:2S] = b(u(M[S:2S]) + 1)
M[0:S] = b(u(M[0:S]) * u(M[S:2S]))

GOTO 3
```

Contrairement à la version récursive précédente, la taille de la mémoire utilisée de change pas.

Notez que les sauts peuvent être utilisés pour des appels de fonctions ! Il suffit de permettre le saut à partir d'une variable. Le code suivant utilise une variable pour stocker l'endroit où sauter après l'exécution de la fonction :

```python
GOTO 6

affiche à l'écran u(M[0:S])
GOTO u(M[2S:3S])

M[0:S] = b(1)
M[S:2S] = b(1)
M[2S:3S] = b(10)
GOTO 3

M[S:2S] = b(u(M[S:2S]) + 1)
M[0:S] = b(u(M[0:S]) * u(M[S:2S]))

M[2S:3S] = 17
GOTO 3

GOTO 11
```

{% note "**Proposition**" %}
L'appel de fonction en pseudo-assembleur se fait avec des instructions de saut et une variable contenant la ligne de retour.
{% endnote %}
{% attention %}
Dans ce cas là, le nombre de ligne de code est borné par l'adressage possible en mémoire. Ce n'est pas gênant en pratique, un adressage sur 64bit permet d'écrire $2^{64}$ lignes de code...
{% endattention %}

On le voit, l'utilisation de saut peut vite être difficile à lire, on recommande de l'utiliser de façon parcimonieuse.

{% lien %}
[Célèbre article de Dijkstra contre l'utilisation des sauts en programmation](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf).
{% endlien %}

### Test

Les tests en pseudo-code sont de deux types :

- arithmétiques, comme $a < b$
- logique, comme $(A OU B) ET C$

Ils n'existent pas à proprement parler en pseudo-assembleur, mais ils peuvent être simulé grâce aux **_drapeaux_**.

{% note "**Définition**" %}
Un **_drapeau_** (**_flag_**)  est une variable binaire affectée automatiquement après une opération.
{% endnote %}

Par exemple :

- $a \leq b$ pourra être effectué en regardant la valeur du drapeau `NÉGATIF` après l'opération $b-a$.
- $(A OU B) ET C$ pourra être effectué en regardant la valeur du drapeau `ZÉRO` (s'il vaut `0`, c'est vrai)

Comme les nombres négatifs seront codés en [Complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux), le bit d poids ford d'un entier vaudra 0 s-il est positif et 1 s'il est négatif. Le drapeau `NÉGATIF`  peut donc être simulé par le drapeau `ZÉRO` en effectuant l'opération `x ET 01...1` qui vaudra 0 (le drapeau `ZÉRO` vaudra alors 1) que le si le nombre `u(x)` est positif.

On peut donc faire tout nos test en utilisant uniquement le drapeau `ZÉRO` :

{% note "**Définition**" %}
Le pseudo-assembleur possède un drapeau `ZÉRO` qui vaut `1` si la dernière opération arithmétique ou logique a donné un résultat de zéro, et `0` sinon.
{% endnote %}

Ce drapeau nous permet de faire tous les tests possibles en pseudo-code et donc :

{% note "**Proposition**" %}
On peut créer les mêmes tests en pseudo-assembleur et en pseudo-code.
{% endnote %}

### Saut conditionnel

Enfin, pour permettre de construire les structures de contrôle du pseudo-code, on ajoute les **_sauts conditionnels_** :

{% note "**Définition**" %}
Un saut conditionnel est de la forme :

```python
GOTOIF drapeau label
```

La prochaine instruction exécutée sera celle de la ligne `label` si le drapeau de nom `drapeau` vaut `1`.

De même :

```python
GOTOIFNOT drapeau label
```

La prochaine instruction exécutée sera celle de la ligne `label` si le drapeau de nom `drapeau` vaut `0`.

{% endnote %}

Le code ci-après utilise le saut conditionnel pour afficher factorielle de 4 :

```python/
M[0:S] = b(1)
M[S:2S] = b(4)

M[0:S] = b(u(M[0:S]) * (u(M[S:2S])))

M[S:2S] = b(u(M[S:2S]) - 1)
GOTOIF ZÉRO 3

affiche à l'écran u(M[0:S])
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
- `SET $X Y` qui place la constante `Y` (un entier relatif) dans le registre de numéro `X`

Encore et toujours factorielle, mais avec des registres

```python
SET $1 1
SET $2 4

$1 = b(u($1) * (u($2)))
$2 = b(u($2) - 1)
GOTOIF ZÉRO 3

affiche à l'écran u($1)

```

### Types d'opérations

Les opérations d'un pseudo-assembleur, comme pour un pseudo-code sont essentiellement arithmétique

#### Logiques


On en conclut donc qu'il suffit que le pseudo-assembleur ne doit posséder que la fonction $\text{NAND}(x, y)$ pour 1bit pour pouvoir effectuer toutes les opérations logiques. D'où la proposition suivante :

{% note "**Proposition**" %}
Le pseudo-assembleur peut effectuer toutes les opérations logiques du pseudo-code s'il possède l'opération :

```python
NAND $1 $2 $3
```

Qui effectue l'opération $\text{NAND}$ pour les 2 objets de longueur 1 des registres `$1` et `$2` et affecte le résultat dans le registre `$3`.
{% endnote %}

#### Arithmétiques

Pour générer toutes les opérations arithmétiques sur les entiers relatifs, il suffit de posséder les opérations d'addition et de soustraction. En utilisant le complément à deux pour noter les entiers négatifs, addition et soustractions sont équivalents :

{% lien %}
[Complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
{% endlien %}

On peut de plus additionner bit à bit deux nombres en utilisant la retenue. Par exemple, ci-dessous le code de la fonction additionnant deux bits `M[0]` et `M[1]` pour rendre la valeur `M[3]` et la retenue, `M[2]`, s'il y en a une:

```python
M[2] = 0

M[3] = XOR(XOR(M[2], M[0]), M[1])
M[2] = OR(AND(M[2], M[0]), OR(AND(M[2], M[1]), AND(M[0], M[1])))
```

En reprenant la sortie de l'algorithme précédent et en l'itérant autant de fois que nécessaire (les paramètres d'entrées seront les deux bit à additionner et la retenue précédente), on peut peut additionner des entiers de toute taille :

{% note "**Proposition**" %}
Le pseudo-assembleur peut effectuer toutes les opérations arithmétiques du pseudo-code s'il possède l'opération :

```python
ADD $1 $2 $3
```

et le drapeau `RETENUE` telle que `ADD` additionne les valeurs des registres `$1` et `$2` en tenant compte du drapeau `RETENUE` et affecte le résultat dans le registre `$3` en mettant à jour la valeur du drapeau `RETENUE`.
{% endnote %}

Come l'addition bit à bit permet de créer l'addition sur un registre complet et que celle ci se fait uniquement avec des opérations logiques, on a de plus :

{% note "**Proposition**" %}
Le pseudo-assembleur peut effectuer toutes les opérations arithmétiques du pseudo-code s'il possède l'opération :

```python
NAND $1 $2 $3
```

Qui effectue l'opération $\text{NAND}$ pour les 2 objets de longueur 1 des registres `$1` et `$2` et affecte le résultat dans le registre `$3`.
{% endnote %}

#### Autres opérations

Les autres opérations possibles par un pseudo-code (gestion des réels, concaténation de chaines, etc) sont facilement codable avec les opérations logique et arithmétiques sur les entiers.

La factorielle finale serait alors quelque chose du genre, en supposant que l'on ait les opérations de somme et de multiplications :

```python
SET $1 1
SET $2 4

MUL $1 $2 $1
ADD $2 -1 $2

GOTOIF ZÉRO 3

affiche à l'écran u($1)
```

### Conclusion

La seule opération que doit pouvoir faire un pseudo-assembleur pour pouvoir faire tout ce que peut faire un pseudo-code est l'opération `NAND`. Tout le reste peut être construit grâce à du code.

{% attention "**À retenir**" %}
Les structure de contrôles, les variables en mémoire et l'unique opération `NAND` permettent de simuler toutes les structures de données possibles ainsi que leurs opérations.
{% endattention %}

## I/O

[Les entrées/sorties](https://fr.wikipedia.org/wiki/Entr%C3%A9e-sortie) ne sont pas indispensables au bon fonctionnement d'un pseudo-assembleur (il suffit d'écrire ou de lire directement en mémoire) on peut supposer qu'il existe des fonctions permettant de lire des données ou d'afficher des résultat à l'écran mais qu'elles ne sont pas directement gérées par le pseudo-assembleur.

## Pseudo-assembleur minimal

On vient de voir qu'il ne faut vraiment pas grand chose pour simuler tout ce que faire du pseudo-code :

1. Mémoire de taille fixe $N = 2^S$ cases
2. 3 registres de taille $S$, deux pour les entrées et une pour la sortie
3. 3 opérations permettant :
   - de déplacer des données de la mémoire vers le registre `$1` ou `$2`
   - de déplacer des données d'un des 3 registres vers la mémoire
   - d'écrire des constantes dans le registre `$1` ou `$2`
4. 1 drapeau `ZÉRO` (pour les saut conditionnels)
5. une opération `NAND $1 $2 $3` (qui permet de créer en code toutes les autres opérations)
6. un saut conditionnel avec le drapeau `ZÉRO` à une ligne donnée du code

Tout le reste peut–être géré via du code, lui aussi est très simple puisqu'il est uniquement constitué de transfert de mémoire, d'opérations `NAND` et de sauts conditionnels.

{% attention "**À retenir**" %}
Le pseudo-code ne peut pas faire plus que du pseudo-assembleur, c'est juste plus agréable à écrire.
{% endattention %}
