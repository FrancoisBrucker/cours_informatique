---
layout: layout/post.njk

title: Les variables et leurs types

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un tableau est une suite contiguë en mémoire d'éléments de même type.

Contrairement à python, un tableau n'est **pas** redimensionnable.

## Déclaration

On peut les déclarer de deux façons.

Soit avec leurs taille :

```c#
int tableau[2] = {1, 2};
int tableau[20] = {0};
```

- la ligne 1 déclare un tableau de 2 entiers, dont le premier élément vaut 1 et le second 2
- la ligne 2 déclare un tableau de 20 entiers, dont tous les éléments valent 0

Les tableaux sont entièrement stockés dans la pile (leurs tailles est connue).

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

Un tableau est une structure de donnée. C'est un type dérivé d'un type courant. On ne peut pas :

- comparer deux tableaux
- assigner un tableau à un autre

On ne peut uniquement accéder à un élément du tableau à la fois.

## Accès aux éléments

On utilise les tableaux comme en python, entre crochet.

```c

int tableau[3] = { 0 };

tableau[1] = 42;

printf("la première valeur du tableau est %i\n", tableau[0]);
printf("la seconde valeur du tableau est %i\n", tableau[1]);
printf("la troisième valeur du tableau est %i\n", tableau[2]);
```

## Tableaux et pointeurs

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

### Pointeurs et tableaux

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

On peut alors associer un pointeur au 5ème élément d'un tableau :

```c
int tableau[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int *p = tableau + 4;

printf("Un entier : %i\n", *p);
```

{% exercice %}
Qu'affiche à l'écran l'exemple précédent ?
{% endexercice %}

## Tableaux de tableaux

On peut combiner les tableaux. Par exemple `int M[3][2]`{.language-} qui est un tableau de 2 tableau de 3 entiers. On peut les initialiser explicitement :

```c
int M[3][2] = { {1, 2}, {3, 4}, {5, 6} };
```

Ou implicitement :

```c
int M[3][2] = {0};
```

Attention à l'ordre de lecture :

1. le premier crochet donne le le nombre d'élément du tableau
2. le second crochet donne le nombre d'élément de chaque élément du tableau

{% exercice %}

Avec l'initialisation explicite, que vaut `M[1][1]`{.language-} ?
{% endexercice %}
{% details "solution" %}

Cela vaut 3.

```c
#include <stdio.h>

int main() {

int M[3][2] = { {1, 2}, {3, 4}, {5, 6} };

printf("Taille d'un réel : %i\n", M[1][1]);

}
```

{% enddetails %}

Si l'on veut associer un pointeur à notre tableau en deux dimensions, le type du pointeur serait un pointeur sur un tableau à deux dimensions, c'est à dire :

```c
int (*p)[2]
```

Notez que le parenthésage est obligatoire de part la précédence entre les opérateurs `[]` et `*` (écrire `int (*p)[2]` correspond à `int *(p[2])` qui n'est pas une déclaration correcte).

{% exercice %}

Avec l'initialisation explicite et `p` déclaré comme précédemment,

que vaut :

- `(*p)[1]`{.language-} ?
- `*p[1]`{.language-} ?
- `(*(p+1))[1]`{.language-} ?

{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>

int main() {

int M[3][2] = { {1, 2}, {3, 4}, {5, 6} };
int (*p)[2] = M;

printf("Taille d'un réel : %i\n", (*p)[1]); // 2
printf("Taille d'un réel : %i\n", *(p[1])); // 3

printf("Taille d'un réel : %i\n", (*(p+1))[1]); // 4
}
```

- `(*p)[1]`{.language-} : `*p` est un tableau à deux élément et est le premier élément de `M`, donc `(*p)[1] = M[0][1] = 2`
- `*p[1]`{.language-} : correspond à `*(p[1])`{.language-} donc correspond à `M[1][0]`
- `(*(p+1))[1]`{.language-} : correspond à un incrément de 1 de `p` qui pointe sur un tableau à deux éléments, donc correspond à `M[1][1] = 3`
{% enddetails %}
