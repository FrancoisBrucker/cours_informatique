---
layout: layout/post.njk

title: Les variables et leurs types

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il existe 3 grands types de variables basiques en C :

- les entiers
- les réels
- les caractères

Contrairement à python, chaque variable de C a un type qui ne peut changer. On déclare une variable de cette façon :

```c
type nom = valeur;
```

{% note %}

Prenez l'habitude de **toujours** initialiser vos variables à la création.

Le C permet de commencer par déclarer une variable par l'instruction  `type nom;` avant de l'utiliser plus tard, mais c'est presque toujours une mauvaise idée.
{% endnote %}

Chaque type ayant une taille donnée (en bytes), la valeur de la variable est stockée dans la pile le temps de sa durée de vie :

- la variable est l'indice de la pile dans laquelle sa valeur est stockée
- la durée de vie d'une variable est le bloc dans laquelle elle est définie ou le fichier si elle est définie en-dehors de tout bloc.

On peut connaître la taille d'une variable grâce à l'opérateur [`sizeof`](https://fr.wikipedia.org/wiki/Sizeof).

```c#
#include <stdio.h>

int main() {

int i = 1;
double d = 3.14;
char c = 'A';

printf("Taille d'un entier : %luB\n", sizeof(i));
printf("Taille d'un réel : %luB\n", sizeof(d));
printf("Taille d'un caractère : %luB\n", sizeof(c));
}
```

Le code ci-dessus donne le résultat suivant sur ma machine :

```
Taille d'un entier : 4B
Taille d'un réel : 8B
Taille d'un caractère : 1B
```

## Entiers

Le type `int` est l'entier par défaut en C. Il est signé, ce qui signifie qu'il peut être positif ou négatif. Sa taille n'est pas définie et peut donc être variable selon l'architecture. Il est habituellement codé sur 4B pour les machines de bureaux.

{% info %}
La norme `c23` impose que le signe soit effectué par [complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
{% endinfo %}

Ce type entier peut être spécifié pour moduler sa taille :

- `short int`
- `long int`
- `long long int`

{% exercice %}
Quelle est la taille de ces types sur votre machine ?
{% endexercice %}
{% details "solution" %}

- `short int` : 2B
- `long int`  : 8B
- `long long int` : 8B

La norme C impose uniquement le fait que ce soit plus grand, pas strictement plus grand
{% enddetails %}

Et on peut rendre le type non signé en ke faisant précéder de `unsigned`. Par exemple : `unsigned short int`

{% info %}
On est pas obligé d'ajouter `int`, ainsi :

- `long long` est équivalent à `long long int`
- `unsigned` est équivalent à `unsigned int`

Il existe le `signed int` qui est équivalent à `int`
{% endinfo %}

{% note %}
Utilisez le type `int` par défaut lorsque vous avez besoin d'entiers.
{% endnote %}

## Réels

Le type réel `double` est codé selon le format [double précision de la représentation ds nombre en virgule flottante](https://fr.wikipedia.org/wiki/IEEE_754#Format_double_pr%C3%A9cision_(64_bits)), sur 8B.

- le format en simple précision sur 4B, noté `float`, existe aussi mains n'est plus recommandé pour les calculs.
- le format `long double` existe également. Il est codé sur 16B.

{% note %}
Utilisez le type `double` par défaut lorsque vous avez besoin de réels.
{% endnote %}

## Char

Le type `char` est le plus petit adressage possible, sur 1B (sur toutes les implémentations actuelles). Il correspond aussi à la représentation d'un caractère ASCII sur 7b.

L'encodage par défaut actuel, UTF-8, encode également ses caractères sur des byte, mais les caractères autres que les caractères ASCII sont codées sur plus d'un byte. Remplacez la ligne 7 de l'exemple par :

```
char c = 'é';
```

et le code ne compilera plus car `é` est codé sur 2 bytes et ne rentrera plus dans un unique char. Le type `char` est donc l'unité fondamentale des chaines de caractères mais ne correspond pas toujours à un caractère.

{% attention %}
On le verra plus tard, mais les caractères s'écrivent entre quote `'`, les double quote (`"`) servent aux chaînes de caractères.
{% endattention %}

## Cast

Un type peut être converti en un autre. Ceci peut se faire de manière implicite :

```
int i = 42;
double k = i;
```

Ou de façon explicite en faisant précéder la variable par le type cible :

```
int i = 42;
double k = (double)i / 13; 
```

{% exercice %}
Que vaut $k$ sans et avec le cast explicite
{% endexercice %}
{% details "solution" %}
<https://zestedesavoir.com/tutoriels/755/le-langage-c-1/1042_les-bases-du-langage-c/4535_les-operations-mathematiques/#division-et-modulo>
{% enddetails %}

## Types dérivées

Les types dérivées sont des types crées à partir d'autres types. En `C` c'est le type de base qui est primordial, on commencera toujours par lui dans la déclaration, le type dérivé sera collé au nom de la variable.

### Les pointeurs

Un pointeur est une variable contenant une adresse.

#### Pointeur générique

En `C` cela se déclare ainsi :

```c
void* p = NULL;
```

La ligne ci-dessus définie une variable `p` contenant une adresse mémoire. On initialise cette adresse à `NULL`, qui correspond à `0x0`, c'est à dire l'adresse invalide.

On peut bien sur afficher sa valeur :

```
printf("%p", p)
```

Qui vaut 0 et sa taille :

```
printf("%uf", sizeof(p))
```

Qui vaut sur ma machine 8B=64b, ce qui semble raisonnable.

Ce type de pointeur n'est cependant pas très utile car l'adresse sur laquelle il pointe n'est pas utilisable. Le principal intérêt des pointeurs est de pouvoir être associer à l'adresse d'une vraie donnée.

Ceci se fait avec l'opérateur d'indirection `&`. Si par exemple on a :

```c
int i = 42;
```

On peut affecter la valeur de l'adresse où est stocké 42 par `&i` :

```c
int i = 42;
void* p = &i;

printf("%p", p)

```

L'utilité d'un pointeur générique est cependant faible : il ne permet que de contenir l'adresse d'autres variables. Sans la connaissance du type de la variable, il est impossible de la modifier

#### Pointeur typé

En `C` tout est orienté autour du type des données. Un pointeur est une indirection vers une donnée. Pour rendre ceci explicite sépare le type pointé de l'indirection. Par exemple un pointeur sur un entier sera défini préférablement :

```c
int *p = NULL;
```

à `int* p = NULL;`{.language-} (qui fonctionne aussi).

`p` est un pointeur dont la valeur est l'adresse d'un `int`. Comme le précédent pointeur, pour l'instant `p` ne pointe sur rien.

L'opérateur `*` désigne une indirection :

- `p` est l'adresse, le pointeur
- `*p` est la valeur de l'entier à l'adresse pointée (celle de `p`)

```c
int i = 42;
int *p = &i;

printf("L'entier i vaut : %i\n", *p);
```

On peut donc aussi modifier $i$ :

```c
int i = 42;
int *p = &i;

*p = 12;

printf("L'entier i vaut : %i\n", i);
```

Attention, ne confondez pas :

- `int *p = &i;` qui définit la valeur du pointeur `p`
- `*p = 12;` qui remplace la valeur de la donnée à l'adresse contenue dans `p`.

Si vous avez du mal écrivez plutôt :

```c
int i = 42;
int *p = NULL;
p = &i;

*p = 12;
```

{% attention %}
Ne définissez jamais un pointeur uniquement par : `int *p;` sans le spécifier, **MAIS** sa valeur est définie, il peut donc se passer plein de chose lorsque l'on cherchera à afficher ou à affecter `*p` :

- de la moins grave : le programme plante
- à la plus grave : le programme modifie une valeur dans le programme, mais on ne sait pas laquelle. Ce qui produira un bug plus tard, mais on ne sait pas bien quand ni quoi.
{% endattention %}

L'indirection peut se composer. Ainsi :

```
int **p;
```

Est un pointeur sur un pointeur d'entier. Cela se comprend si on décompose l'instruction :

- `int` est le type
- `*p` est un pointeur sur le type int
- `p` est un pointeur sur le type pointeur sur le type int

### Les Tableaux

#### Déclaration

On peut les déclarer de deux façons.

Soit avec leurs taille :

```c#
int tableau[2] = {1, 2};
int tableau[20] = {0};
```

- la ligne 1 déclare un tableau de 2 entiers, dont le premier élément vaut 1 et le second 2
- la ligne 2 déclare un tableau de 20 entiers, dont tous les éléments valent 0

{% attention %}

Ceci ne fonctionne pas :

```c#
int tableau[5] = {1, 2};
```

Ou on initialise chaque valeur individuellement soit toutes les valeurs en une fois.
{% endattention %}

On peut aussi initialiser un tableau en omettant sa taille si elle est définie par son affectation :

```c
int tableau[] = {1, 3, 5};
```

{% exercice %}
Quel est la taille de `tableau` s'il est issu de la définition :

```c
int tableau[20] = {0};
```

{% endexercice %}
{% details "solution" %}
> TBD avec un sizeof
{% enddetails %}

#### Utilisation

On utilise les tableaux comme en python, entre crochet.

```c

int tableau[3] = { 0 };

tableau[1] = 42;

printf("la première valeur du tableau est %i\n", tableau[0]);
printf("la seconde valeur du tableau est %i\n", tableau[1]);
printf("la troisième valeur du tableau est %i\n", tableau[2]);
```

#### Tableaux et pointeurs

Pointeurs et tableaux ne sont pas identiques, mais ils partagent des propriétés. Par exemple, si :

```c
int tableau[20] = {0};
```

Alors `tableau` est l'adresse du premier élément du tableau. Ce qui fait que l'on peut écrire :

```c
int tableau[20] = {0};
int *p = tableau;
```

Mais leurs tailles ne sont pas égales :

- `sizeof(tableau)`
- `sizeof(p)`

On peut cependant utiliser la notation [] avec les pointeurs. Si :

```c
int tableau[20] = {0};
int *p = tableau;
```

Alors `p[i]` correspond au $i$ème élément du tableau.

#### Pointeurs et tableaux

```c
int tableau[20] = {0};
int *p = tableau;
```

En additionnant un entier à un pointeur, on incrémente sa valeur de la taille de ce qu'il pointe. Par exemple :

```c
printf("Taille d'un entier : %i\n", sizeof(int));
printf("Taille d'un réel : %p\n", (void*)p);
printf("Taille d'un réel : %p\n", (void*)(p+1));
```

On peut alors associer un pointeur au 10ème élément d'un tableau :

```c
int tableau[20] = {0};
int *p = tableau + 9;
```

#### Tableaux de tableaux

On peut combiner les tableaux. Par exemple `int M[3][2]`{.language-} qui est un tableau de 2 tableau de 3 entiers. On peut les initialiser explicitement :

```c
int i[3][2] = { {1, 2}, {3, 4}, {5, 6} };
```

Ou implicitement :

```c
int i[3][2] = {0};
```

{% exercice %}

- Avec l'initialisation explicite, que vaut `M[1][1]`{.language-} ?
- Les éléments de M étant contiguës, comment accéder au même élément directement avec un pointeur sur un entier ?

{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>

int main() {

int i[3][2] = { {1, 2}, {3, 4}, {5, 6} };
int *p = (int*)i;
p = p + 3;
printf("Taille d'un réel : %i\n", i[1][1]);
printf("Taille d'un réel : %i\n", *p);

}
```

{% enddetails %}

#### Tableaux de pointeurs

### Les structures

tableaux et pointeurs

pointeur = python.

void *p;

attention au effets de bord : durée de vie et pointeurs.

## Caractères

"" vs ''

char et "string"
char[]

Deux formes recommandes :

```
char[10] = "";
char[] = "Hello !"
char* = "Hello !"
```

ok mais attention à : char[7] = "Hello !" qui est faux !

Le mal nommé. Un byte et utf8. Un caractère peut souvent encodée sur plusieurs bytes

## Définition de nouveaux types

3. struct et enum
4. typedef et size_t, struct

### enum

### typedef

char8_t, 16 et 32

## Quel type utiliser quand

- int
- double
- char*
- utiliser `size_t` pour compter.


## Entrées / sorties

[text spécifier](https://en.wikipedia.org/wiki/C_data_types#Main_types)

exemples avec printf/scanf

## Spécificateurs

- qualificateur : const, volatile, restrict


## Règles

 1. cast explicites et implicites
 2. règles :
    1. on initialise toutes les variables, pointeur à null
    2. char, int, double, size_t
    3. une seule variable déclarée par ligne (sinon effet de bord avec les pointeurs)
