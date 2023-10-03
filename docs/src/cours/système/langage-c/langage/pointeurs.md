---
layout: layout/post.njk

title: Les variables et leurs types

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un pointeur est une variable contenant une adresse.

## Pointeur générique

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

## Pointeur typé

En `C` tout est orienté autour du type des données. Un pointeur est une indirection vers une donnée. Pour rendre ceci explicite sépare le type pointé de l'indirection. Par exemple un pointeur sur un entier sera défini préférablement :

```c
int *p = NULL;
```

à `int* p = NULL;`{.language-} (qui fonctionne aussi).

`p` est un pointeur dont la valeur est l'adresse d'un `int`. Comme le précédent pointeur, pour l'instant `p` ne pointe sur rien.

L'opérateur `*` désigne une indirection :

1. ce qui est un entier, c'est `*p`
2. donc `p` est l'adresse, le pointeur

Mettez des parenthèses et séparer les deux instructions pour clarifier si vous préférez :

```c
int (*p);
p = NULL;
```

Une fois que vous aurez l'habitude, le code ci-après deviendra limpide :

```c
int i = 42;
int *p = &i;

printf("L'entier i vaut : %i\n", *p);
```

Avec un pointeur typé, on peut modifier la valeur de ce sur quoi on pointe :

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
int (*p);
p = &i;

(*p) = 12;
```

{% attention "**ne faites pas les malins**" %}
Ne définissez jamais un pointeur uniquement par : `int *p;` sans le spécifier. En effet, `p` vaut quelque chose, mais on ne sais pas quoi (ce qu'il y avait en mémoire à ce moment là).

Il peut donc se passer plein de chose lorsque l'on cherchera à afficher ou à affecter `*p` :

- de la moins grave : le programme plante
- à la plus grave : le programme modifie une valeur dans le programme, mais on ne sait pas laquelle. Ce qui produira un bug plus tard, mais on ne sait pas bien quand ni quoi.
{% endattention %}

L'indirection peut se composer. Ainsi :

```
int **p;
```

Est un pointeur sur un pointeur d'entier. Cela se comprend si on décompose l'instruction :

- `(**p)` est un entier
- `(*p)` est un pointeur (sur un entier int)
- `p` est un pointeur sur (un pointeur (sur un entier int))

Cette double indirection est très fréquente.

## Pointeurs et fonctions

Il faut faire très attention à la durée de vie des pointeurs.

Lorsque des fonctions manipule des pointeurs, on passe en paramètre de la fonction un pointeur avec une adresse valide. C'est une technique qui permet à une fonction de modifier des variable et non des valeurs en passants leurs adresses.

{% exercice %}

Créer une fonction qui échange deux variables passées en paramètre

{% endexercice %}
{% details "solution" %}
on ne peut pas juste passer les variable car c'est des copies de valeurs.

Il faut passer 2 pointeurs en paramètre.
{% enddetails %}

{% attention "Aux durées de vies" %}
Ne pas rendre une pointeur sur une une variable crée dans une fonction.
{% endattention %}

## Pointeurs de fonctions

```c
int fahrenheit(int x) {
  return (x * 9/5) + 32;
} 
```

La signature de cette fonction est :

```c
int fahrenheit(int);
```

On peut alors créer un pointeur sur une fonction ayant sa signature en écrivant :

```c
int (*p)(int)
```

Le code suivant est alors tout à fait fonctionnel :

```c
#include <stdio.h>

int fahrenheit(int x) {
  return (x * 9/5) + 32;
}

int main() {

int (*p)(int) = fahrenheit;

printf("%i \n", p(0));

}
```

Cette technique permet d'utiliser des fonctions en paramètre d'autres fonctions.

{% exercice %}
Créez une fonction permettant, selon ses paramètres, soit d'additionner 2 nombres soit de les multiplier.
{% endexercice %}
{% details "solution" %}

{% enddetails %}
