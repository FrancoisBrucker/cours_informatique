---
layout: layout/post.njk

title: Architecture de Von Neumann

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'[Architecture de Von Neumann](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann) est une façon d'unifier code et donnée. Il est basé sur deux notions supplémentaire au pseudo-assembleur :

- Unification du code et des données
- Utilisation de la pile pour gérer la portée des variables et les appels de fonctions

On se place donc dans le cas où l'on souhaite exécuter du code écrit en [pseudo-assembleur](../pseudo-assembleur) sur une machine de $N=2^S$ cases mémoires. On supposera ici que $S$ vaut 64, ou plus.

## Unifier mémoire et code

Chaque ligne de code du pseudo-assembleur est constituée de la même manière :

```python
OP #1 #2 #3 
```

Où `OP` est le nom de l'instruction et `#1`, `#2` et `#3` des registres ou des constantes.

Comme on a un nombre fini d'opérations et de registres, on peut associer :

- un nombre, on dit [OPCODE](https://fr.wikipedia.org/wiki/Code_op%C3%A9ration), à chaque opération
- un nombre à chaque registre.

L'instruction précédente peut alors être associé à un quadruplet d'entiers $(o, r_1, r_2, r_3)$.

Si l'on à $S=64$, on peut avoir jusqu'à $2^{16} = 65536$ opérations et registres ! Habituellement, on stocke chaque instruction sur 32bits, ce qui permet d'avoir 256 registres (3 suffisent) et 256 opérations (une seule opération, NAND, est nécessaire) :

{% note "**Proposition**" %}
Il existe une injection permettant d'associer une suite de `0` et de `1` de taille $S$ à toute instruction de pseudo-assembleur.
{% endnote %}

Par exemple si l'on associe 42 à l'opération `NAND`, l'instruction `NAND $2 $1 $3` sera codée par le quadruplet : $(42, 2, 1, 3)$ ce qui sur 32bit donne le code (on a séparé les 32bits par paquet de 8 pour plus de clarté):

```
00101010 00000010 00000001 00000011
```

Cette injection entre code et suite de `0` et de `1` permet de placer le code en mémoire :

{% note "**Proposition**" %}
Dans une architecture de Von Neumann, le code est placé en mémoire sous la forme d'une suite de `0` et de `1`. So exécution est contrôlée par un registre spécial, $I$ appelé pointeur d'instruction dont la valeur est l'adresse de la **prochaine** instruction à exécuter.

Exécuter une instruction se fait alors de la façon suivante :

1. lire l'instruction à exécuter dont le code commence en $M[u(I)]$
2. incrémenter la valeur de $I$ de la taille de l'instruction lue
3. exécuter l'instruction lue
{% endnote %}

L'utilisation d'un pointeur d'instruction et le fait qu'il pointe sur l'instruction suivante permet de gérer simplement les sauts : il suffit de modifier sa valeur.

## Variable et pile

L'architecture de Von Neumann utilise le concept de [pile](https://fr.wikipedia.org/wiki/Pile_(informatique)) :

{% note "**_Définition_**" %}
Une **_pile_** est une structure de donnée qui comprend deux fonctions :

- empile(d) : ajoute l'élément d à la pile et rend son indice de stockage
- dépile() : supprime un élément de la pile et le rend
- accès(0) : accède au i+1 ème élément de la pile en lecture ou en écriture

Le **premier** élément de la pile est le **dernier** empilé.

{% endnote %}

Prenons l'exemple suivant :

```python
empile(1)
empile(2)
print(accès(0))  # rendra 2
print(accès(1))  # rendra 1
dépile()
print(accès(0))  # rendra 1
```

La pile est une structure fondamentale en algorithmie (on y reviendra) et permet de résoudre efficacement tout un tas de problèmes lié au stockage de données. Le modèle de Von Neumann l'utilise pour gérer efficacement les variables et les appels de fonctions.

{% lien %}
La pile est un concept ancien et déjà présent chez Turing pour l'appel de fonctions. Je ne saurais trop vous conseiller de regarder cette [vidéo qui détaille l'invention et les diverses utilisations de la pile](https://www.youtube.com/watch?v=2vBVvQTTdXg).
{% endlien %}

### Implémentation et fonctionnement

La pile est composée de cases contiguës en mémoire : classiquement les derniers.

Pour gérer la pile le modèle de Von Neumann possède :

- trois instructions :
  - `PUSH $X` qui empile la valeur du registre `X` dans la pile
  - `PUSH X` qui empile la constante `X`
  - `POP $X` : dépile la pile dans le registre `X`
- deux registres :
  - `SP` (**_stack pointer_**) qui contient l'adresse de fin de pile, c'est à dire le début de l'adresse du dernier élément dans la pile
  - `FP` (**_frame pointer_**)  qui contient l'adresse du début de la pile

{% attention %}

- On ne peut placer que des valeurs de taille $S$ dans la pile
- Lorsque l'on empile des éléments à la pile, la valeur `u(SP)` **décroît**.

{% endattention %}

La pile est ainsi constituée du segment de mémoire $M[u(SP):u(FP)]$, que l'on appelle un **_frame_** et à chaque fois qu'une valeur est ajoutée dans la pile, le registre `SP` est décrémenté de $S$. Ainsi :

- le dernier élément ajouté à la pile sera dans le segment $M[u(SP):u(SP) + S]$
- l'avant-dernier élément ajouté à la pile sera dans le segment $M[u(SP) + S:u(SP) + 2S]$
- ...

Notez que l'on peut retrouver un élément de la pile si on sait combien d'éléments ont été ajouté **après lui**. Si $k$ éléments ont été ajoutés après l'élément recherché, il se trouve à cet endroit de la pile : $M[u(SP) + k\cdot S:u(SP) + (k+1)\cdot S]$

On peut également retrouver un élément de la pile si on sait combien d'éléments ont été ajouté **avant lui**. Si $k$ éléments ont été ajoutés avant l'élément recherché, il se trouve à cet endroit de la pile : $M[u(FP) - (k+1)\cdot S:u(FP) - k\cdot S]$

C'est exactement ce qu'il faut pour gérer des variables !

### Usage

{% note "**_Définition_**" %}
Dans une architecture de de Von Neumann la pile contient les adresses des données stockées en mémoire : ce sont les variables du programme
{% endnote %}

#### Stocker des variables

Lorsqu'une variable est créée en mémoire son adresse est empilée et le code y accède via la pile.

On peut y accéder via le registre `SP`. Par exemple avec cette boucle for qui calcule factorielle 4 :

```python
M[0:S] = b(4)
PUSH 0

affiche à l'écran u(M[SP:SP+S])

M[S:2S] = b(1)
PUSH S

M[u(SP):u(SP)+S] = b(u(M[u(SP):u(SP)+S]) * u(M[u(SP)+S:u(SP)+2S]))
affiche à l'écran u(M[u(SP):u(SP)+S])

M[u(SP)+S:u(SP)+2S] = b(u(M[u(SP)+S:u(SP)+2S]) - 1)
GOTOIFNOT ZÉRO 9
```

Le programme va créer 2 variables en faisant pour chacune 2 opérations :

1. création de l'objet en mémoire
2. assignation de l'objet à une _variable_ en l'empilant

Puis on utilise les objets via les variables, c'est à dire la pile.

{% exercice %}
Qu'affiche à l'écran le code précédent ?
{% endexercice %}
{% details "corrigé" %}
Il va afficher 4, 4, 12, 24, 24

{% enddetails %}

Mais on a coutume d'accéder aux variables par rapport à `FP` car cela permet d'accéder à l'objet sans changer d'adresse. Le code précédent devient alors :

```python
M[0:S] = b(4)
PUSH 0

affiche à l'écran u(M[u(FP)-S:u(FP)])

M[S:2S] = b(1)
PUSH S

M[u(FP)-2S:u(FP)-S] = b(u(M[u(FP)-2S:u(FP)-S]) * u(M[u(FP)-S:u(FP)]))
affiche à l'écran u(M[u(FP)-2S:u(FP)-S])

M[u(FP)-S:u(FP)] = b(u(M[u(FP)-S:u(FP)]) - 1)
GOTOIFNOT ZÉRO 9
```

Dans une frame, les données (en mémoire) sont toujours associé aux même variables (valeurs selon `FP`).

#### Supprimer des variables

Lorsque l'on a plus besoin d'un objet, on le dépile et on peut réutiliser la mémoire qu'il utilisait. Pour que cela fonctionne il faut créer et supprimer les variables dans l'ordre, on ne peux pas supprimer une variable sans supprimer également toutes celles qui ont étés crées après elle.

L'usage veut que l'on supprime tout le frame. Pour ne pas avoir à garder toutes les variables, on va créer des frame temporaires pour stocker les variables locales, en particulier lors de l'appels des fonctions.

#### Appels de fonctions

{% lien %}
Ce n'est pas Von Neumann mais Dijkstra qui a a proposé cette façon de faire (utiliser la pile pour appeler des fonctions et stocker les variables locales), toujours utilisée dans nos ordinateurs actuels.

Le, célèbre article où il présente cette idée est là :
[Recursive programming](https://ics.uci.edu/~jajones/INF102-S18/readings/07_dijkstra.pdf)
{% endlien %}

Pour pouvoir exécuter des fonctions il faut pouvoir faire deux choses :

1. gestion des variables locales à la fonction ainsi que ses paramètres
2. permettre de gérer l'appel et le retour après la fonction exécutée

Le pseudo-assembleur gère les deux cas précédent en :

1. passant les paramètres dans un tableau
2. s'assurant que les variables locales seront crées après toutes les autres variables.

Si le deuxième point est géré de la même manière par le modèle de Von Neumann (_ie._ c'est au développeur de faire attention), l'adresse de retour, les paramètres et les variables locales sont gérées par la pile, en associant à chaque fonction sa **_frame de pile**_.

Nous allons montrer ici une façon générale de procéder mais il n'existe en pratique plein d'implémentation différente de ce principe général (voir par exemple [les conventions d'appels pour les processeurs x64 Linux](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame) où certains paramètres sont passés par des registres pour aller plus vite).

1. paramètres de la fonction : empile les paramètres
2. saut vers la fonction :
   1. empile `IP`
   2. affecte `IP` à l'adresse de la fonction
3. fonction :
   1. préparation de la fonction :
      1. empile `FP` : sauvegarde de la _frame_ appelante
      2. `FP = SP` : nouvelle _frame_ pour les variables locales
   2. corps de la fonction : normale avec création de variables locales et
   3. fin de fonction :
      1. place le résultat de la fonction dans le registre `$1`
      2. dépile toutes les variables locales
      3. dépile dans `FP` : on retrouve la _frame_ précédente
   4. saut retour : dépile dans `IP`
4. nettoyage on dépile les paramètres de la fonction

La partie 3.1.2 permet de gérer facilement les variables locales à la fonction. On remet tout en place en 3.3.3 où le replace le pointeur `FP` à sa valeur d'avant l'appel de la fonction.

Voici un exemple avec le code de la factorielle itérative :

```python
#### Main

M[0:S] = b(4)   # paramètre de la fonction
PUSH 0          
PUSH IP+2       # adresse de retour
IP = 13          # saut vers la fonction
                
POP              # retour de la fonction. On dépile le paramètre
affiche à l'écran $1

#### factorielle

PUSH FP           # nouveau frame
FP = SP

M[S:2S] = b(1)   # une variable locale
PUSH S

M[u(FP)-S:u(FP)] = b(u(M[u(FP)+2S:u(FP)+3S]) * u(M[u(FP)-S:u(FP)]))

M[u(FP)+2S:u(FP)+3S]) = b(u(M[u(FP)+2S:u(FP)+3S])) - 1)
GOTOIFNOT ZÉRO 19

POP $1          # retour de fonction
POP FP          # ancien frame

POP IP          # retour de la fonction
```

Si on avait utilisé le code de la factorielle récursive, il aurait fallut faire attention à où l'on stockait la variable locale. Pour cela, on peut réserver un registre qui indique la valeur maximum où sont stockés les données et on l'incrémente ou décrémente dès que l'on crée ou supprime des données.

{% exercice %}
En supposant que le registre $p$ contienne l'adresse maximum en mémoire, modifiez le code de la factorielle.
{% endexercice %}
{% details "corrigé" %}

```python#
#### factorielle recursive

PUSH FP           
FP = SP

M[u(p):u(p)+S] = b(1)   # une variable locale crée après p
PUSH S
p = u(p) + S            # incrémente p

M[u(FP)-S:u(FP)] = b(u(M[u(FP)+2S:u(FP)+3S]) * u(M[u(FP)-S:u(FP)]))

M[u(FP)+2S:u(FP)+3S]) = b(u(M[u(FP)+2S:u(FP)+3S])) - 1)
GOTOIFNOT ZÉRO 19

POP $1          # retour de fonction
p = u(p) - S    
POP FP          

POP IP          

```

{% enddetails %}

## Structure du programme en mémoire

La mémoire doit permettre de stocker à la fois le code, les variables via la pile et les données. Ces dernières se
Avoir de la place pour

- code
- la pile
- le reste :
  - données constantes
  - données allouées dynamiquement : le tas

Mémoire de bas en haut :

```
pile                   # hautes valeurs de M
...
...
tas
constantes
code                  # basses valeurs de M
```

La pile augmente en _descendant_, le tas augmente en _montant_ les valeurs de la mémoire. On supposera que la mémoire est assez grande pour pqs qu'ils se rencontrent.

Enfin, les constantes ou les données statiques sont souvent placé juste au-dessus du code.

## Processeur

Dans l'architecture de Von Neumann, le processeur est séparé en deux :

- l'**_unité arithmétique_** qui s'occupe d'exécuter les opérations (au pire juste NAND et gestion transferts mémoire <-> registres)
- l'**_unité contrôle_** qui gère le code, c'est à dire la transcription des opcode en instructions.
