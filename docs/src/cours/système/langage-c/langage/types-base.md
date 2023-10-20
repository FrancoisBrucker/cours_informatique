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

{% attention "**danger !**" %}
`C` vous permet de créer plusieurs variable en une fois `int i, j;` mais ne le faites pas.

- une seule déclaration de variable par ligne.
- initialisez cette variable

{% endattention  %}

Prenez l'habitude de **toujours** initialiser vos variables à la création.

Le C permet de commencer par déclarer une variable par l'instruction  `type nom;` avant de l'utiliser plus tard, mais c'est presque toujours une mauvaise idée.
{% endnote %}

{% note %}
Chaque type a une taille donnée (en bytes). La valeur de la variable est stockée :

- dans la pile si elle est définie dans une fonction
- dans la partie data si elle est n'est pas définie dans une fonction.

La durée de vie d'une variable est le bloc dans laquelle elle est définie ou le fichier si elle est définie en-dehors de tout bloc.

Une variable est ainsi l'indice de la pile ou de la partie data à laquelle sa valeur est stockée.

{% endnote %}

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

{% note %}
La fonction [printf](https://koor.fr/C/cstdio/fprintf.wp) permet d'afficher une chaîne de caractères formatée :

- le premier paramètre est ue chaîne de caractères. Elle contient des paramètres `%x` où `x` correspond au type de la variable à représenter.
- les autres paramètres correspondent aux variables qui remplaceront, dans l'ordre, les caractères `%x`

Il existe beaucoup de types possibles, ils sont tous représentés ici : [text spécifier](https://en.wikipedia.org/wiki/C_data_types#Main_types). On utilise fréquemment les formats :

- `%zu` : pour les résultats d'un sizeof
- `%i` : pour les entiers (signés)
- `%u` : pour les entiers non signés
- `%f` : pour les réels
- `%c` : pour un caractère
- `%s` : pour les chaines de caractères
- `%p` : pour les pointeurs génériques
{% endnote %}
{% exercice %}
Plutôt que d'afficher la taille en mémoire des différentes variables dans le code précédent, affichez leurs valeurs avec le bon type.
{% endexercice %}
{% details "solution" %}

```c#
#include <stdio.h>

int main() {

int i = 1;
double d = 3.14;
char c = 'A';

printf("Un entier : %i\n", i);
printf("Un réel : %f\n", d);
printf("Un caractère : %c\n", c);
}

```

{% enddetails %}

La fonction `printf`{.language-} et son fonctionnement est un bon moyen pour réaffirmer que la valeur d'une donnée dépend de son type (presque) indépendamment de sa valeur binaire effective. Prenez le code suivant comme exemple où l'on utilise la fonction `printf`{.language-} sur une même variable selon deux types différents :

```c#
#include <stdio.h>

int main() {

int i = -1;

printf("Entier (signé) : %i\n", i);
printf("Entier non signé : %u\n", i);
printf("flottant : %f\n", i);
}

```

- le premier affichage on utilise le format `%i` pour représenter un entier signé
- le premier affichage on utilise le format `%u` pour représenter un entier non signé (il ne peut que être positif)

Il est crucial de se rappeler qu'une donnée peut se voir de multiple façon selon le type par le prisme duquel on la regarde.

## Entiers

Le type `int` est l'entier par défaut en C. Il est signé, ce qui signifie qu'il peut être positif ou négatif. Sa taille n'est pas définie et peut donc être variable selon l'architecture. Il est habituellement codé sur 4B pour les machines de bureaux.

{% info %}
La norme `c23` impose que le signe soit effectué par [complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
{% endinfo %}

### Types d'entiers

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

L'intérêt d'utiliser des entiers non signés est double :

- on peut en aller plus loin
- les nombres cyclent du maximum à 0 (ce comportement est non définit pour les entiers signés)

{% exercice %}
En utilisant le fichier [`limits.h`](https://www.tutorialspoint.com/c_standard_library/limits_h.htm), vérifiez que lorsqu'on ajoute 1 à un entier non signé maximum, on obtient bien 0.

{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>
#include <limits.h>


int main() {

unsigned int i = UINT_MAX;

printf(" un entier non signé : %u\n", i);
i += 1;
printf(" un entier non signé : %u\n", i);
}
```

{% enddetails %}

{% info %}
On est pas obligé d'ajouter `int`, ainsi :

- `long long` est équivalent à `long long int`
- `unsigned` est équivalent à `unsigned int`

Il existe le `signed int` qui est équivalent à `int`
{% endinfo %}

{% note %}
Utilisez le type `int` par défaut lorsque vous avez besoin d'entiers.
{% endnote %}

### Représentation des entiers

> TBD : nombre décimal, binaire, hexadécimal (pour les adresses) ou octal (utilisé pour les droits.)

## Réels

Le type réel `double` est codé selon le format [double précision de la représentation ds nombre en virgule flottante](https://fr.wikipedia.org/wiki/IEEE_754#Format_double_pr%C3%A9cision_(64_bits)), sur 8B.

- le format en simple précision sur 4B, noté `float`, existe aussi mains n'est plus recommandé pour les calculs.
- le format `long double` existe également. Il est codé sur 16B.

{% note %}
Utilisez le type `double` par défaut lorsque vous avez besoin de réels.
{% endnote %}

## Char

Le type `char` est le plus petit adressage possible, sur 1B (sur toutes les implémentations actuelles). Il correspond aussi à la représentation d'un caractère ASCII sur 7b.

L'encodage par défaut actuel, [UTF-8](https://fr.wikipedia.org/wiki/UTF-8), encode également ses caractères sur des bytes, mais les caractères autres que les caractères ASCII sont codées sur plus d'un byte. Remplacez la ligne 7 de l'exemple par :

```
char c = 'é';
```

et le code ne compilera plus car `é` est codé sur 2 bytes et ne rentrera plus dans un unique char :

{% note %}
Le type `char` est l'unité fondamentale des chaines de caractères mais ne correspond pas toujours à un caractère.
{% endnote %}

Les caractères s'écrivent entre quote `'` et sont remplacé par leur code selon l'encodage par défaut (souvent utf8).

```c
printf(" un caractère : %c\n", 65);
printf(" un caractère : %i\n", 'A');
```

{% attention %}
Les double quote (`"`) servent aux chaînes de caractères et ne peuvent pas être utilisé pour représenter des caractères
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

Lorsque vous manipulez des nombres et vous voulez vous assurer que ce sont les opérations réelles qui sont utilisées, même si vous manipulez des entiers, écrivez-les sous la forme de réels. Par exemple :

```c
1.0 / 3
```

vous assurera d'utiliser la division réelle.

## Définition de nouveaux types

Le `C` ne possède qu'un nombre limité de types qui correspondant à une taille de stockages et pas à leurs utilisations. Il est alors courant de renommer ces types pour rendre leur usage explicite et faciliter la lecture du code.

Par exemple le type de retour de [`sizeof`](https://fr.wikipedia.org/wiki/Sizeof) est `size_t`. Ce type correspond chez moi à un entier long non signé (il est défini dans le fichier `stddef.h`).

Ce renommage utilise l'opérateur `typedef`{.language-} :

```c
typedef unsigned long int size_t;
```

L'opérateur `typedef` renomme un type (`unsigned long long`) en un autre (`size_t`)

Ce type est défini pour pouvoir contenir le nombre maximum d'élément d'un ensemble. Attention, cette quantité est dépendante de la structure. Elle vaut $2^{64}$ pour une architecture x64 mais peut–être plus petite pour un Raspberry PI par exemple.

C utilise cette techniques à ne nombreux endroits, et nous l'utiliserons aussi lorsque cela nous permettra de :

- raccourcir les notations (avec les structures par exemple)
- d'être pus clair

{% exercice %}
Créer un type `petit_entier` correspondant au plus petits entiers signé possible.
{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>

int main() {

typedef signed char petit_entier;

petit_entier i = 12;


printf(" un petit entier : %i\n", i);

}
```

{% enddetails %}

## Quel type utiliser quand

Si pas de contrainte de taille :

- entier : `int`
- si énumération ou comptage positif `size_t`
- réel : `double`

Les variables peuvent être [Qualifiées](https://en.wikipedia.org/wiki/Type_qualifier#C/C++). Cette qualification est utilisée par le compilateur pour optimiser le code produit, il n'a pas d'autre utilité en `C`.

Le qualifier se place au début de la déclaration, Par exemple :

```c
const double PI = 3.14
```

Il existe 4 types de qualifier :

- `const` : la variable est constante. Le compilateur va produire une erreur lorsque le code tentera de la modifier.
- `volatile` : la variable peut être modifiée en dehors du code (lorsque la variable correspond à des données partagées via le réseau par exemple), le compilateur ne doit pas *cacher* la variable par exemple
- `restrict` : assure le compilateur que cette donnée ne sera pas accessible par une autre variable. Cela évite le [*pointer aliasing*](https://en.wikipedia.org/wiki/Aliasing_(computing)#Aliased_pointers).

{% attention "**danger !**" %}
[Bizarreries de `const` en `C`](https://www.youtube.com/watch?v=8a3HyL1VN0Q)
{% endattention %}

## Opérations

- [opérations mathématiques](https://zestedesavoir.com/tutoriels/755/le-langage-c-1/1042_les-bases-du-langage-c/4535_les-operations-mathematiques/)
- [opérateur bit à bit](https://en.wikipedia.org/wiki/Bitwise_operations_in_C)

{% attention "**danger !**" %}
Méfiez vous de `++i` et `i++`.

1. ne combinez pas cet incrément à toute autre opération
2. si vous êtes obligé de le faire, utilisez **toujours** `++i`

{% endattention %}
{% exercice %}

Que fait le code ci-dessous :

```c
int i = 12;

printf(" un int : %i\n", i++);
printf(" un int : %i\n", i);
```

{% endexercice %}
