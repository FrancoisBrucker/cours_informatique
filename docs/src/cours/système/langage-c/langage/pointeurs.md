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

Le schéma en mémoire est le suivant :

```
adresse  :     &i         &p
mémoire  :   | 42 | ... | &i | ....
variable :     i          p
type     :    int        void*
```

L'utilité d'un pointeur générique est cependant faible : il ne permet que de contenir l'adresse d'autres variables. Sans la connaissance du type de la variable, il est impossible de la modifier

## Pointeur typé

En `C` tout est orienté autour du type des données. Un pointeur est une indirection vers une donnée. Pour rendre ceci explicite sépare le type pointé de l'indirection. Par exemple un pointeur sur un entier sera défini  avec la forme suivante (préférablement à `int* p = NULL;`{.language-}, qui fonctionne aussi) :

```c
int *p = NULL;
```

En reprenant la symbolique du `C` :

```c
type variable = valeur;
```

La déclaration du pointeur s'écrit :

```c
int (*p) = NULL;
```

Et on a bien que :

- `*p` est une variable de type entier
- `p` est un pointeur
- comme c'est la variable `p` que l'on initialise la valeur `NULL` s'applique bien à `p`.

L'opérateur `*` désigne une indirection : `p` est une indirection vers une donnée du type désigné. La donnée présente à l'indice `p` de la mémoire est un entier.

Une fois que vous aurez l'habitude, le code ci-après deviendra limpide :

```c
int i = 42;
int *p = &i;

printf("L'entier i vaut : %i\n", *p);
```

Le schéma en mémoire est le même qu'avec le pointeur générique  :

```
adresse  :     &i         &p
mémoire  :   | 42 | ... | &i | ....
variable :     i          p
type     :    int        int*
```

Sauf que maintenant la valeur pointée est typée, on peut donc l'affecter :

```c
int i = 42;
int *p = &i;

*p = 12;

printf("L'entier i vaut : %i\n", i);
```

L'indirection `*p` se lit : va à l'adresse présente dans la variable `p`, c'est à dire i. On a la formule suivante :

```c
*p = *(&i) = i
```

Attention, ne confondez pas :

- `int *p = &i;` qui définit la valeur du pointeur `p`
- `p` qui est une variable contenant une adresse
- `*p` qui est la donnée à l'adresse de `p`
- `&p` qui est l'adresse où est stockée la variable `p`

Si vous avez du mal écrivez plutôt :

```c
int i = 42;
int (*p);
p = &i;

(*p) = 12;
```

{% attention "**danger !**" %}
Ne définissez jamais un pointeur uniquement par : `int *p;` sans le spécifier immédiatement après.

En effet, `p` vaut quelque chose, mais on ne sais pas quoi (ce qu'il y avait en mémoire à ce moment là).

Il peut donc se passer plein de chose lorsque l'on cherchera à afficher ou à affecter `*p` :

- de la moins grave : le programme plante
- à la plus grave : le programme modifie une valeur dans le programme, mais on ne sait pas laquelle. Ce qui produira un bug plus tard, mais on ne sait pas bien quand ni quoi.
{% endattention %}

On peut avoir autant d'indirection que l'on veut. Par exemple :

```c
int (***p) = NULL;
```

Signifie que p est une indirection d'indirection d'indirection vers un donnée de type entier.

Le plus souvent on aura que 2 indirection. Comme par exemple :

```
int (**p);
```

La variable `p` est un pointeur sur un pointeur d'entier. Cela se comprend si on décompose l'instruction :

1. `(**p)` l'élément dans la parenthèse est un entier
2. `*(*p)` l'élément dans la parenthèse est une indirection vers un entier
3. `**(p)` l'élément dans la parenthèse est une indirection vers une indirection vers un entier

Ce qui donne le schéma en mémoire suivant :

```
adresse  :       &i          a            &p
mémoire  :   |   42  | ... | &i | .... |   a   |
variable :     i=**p         *p            p
type     :      int         int*         int**
```

Cette double indirection est très fréquente, en particulier pour les caractères, comme nous le verrons.

## Pointeurs et fonctions

Outre l'allocation dynamique de mémoire (comme on le verra plus tard),
l'intérêts des pointeurs est qu'il permet d'accéder à une variable de multiples façons.

Une utilisation courante des pointeurs consiste à passer l'adresse d'une variable (un pointeur sur elle) à une fonction pour pouvoir la modifier.

Par exemple le code suivant ne modifie bien sur pas la variable `i`.language-} :

 ```c#
#include <stdio.h>

void modification(int x) {

  x = 12;

}

int main() {

int i = 0;

modification(i)

printf("Entier : %i\n", i);
}

```

La variable `x`{.language}, crée à l'exécution de la fonction sur la pile, contient la donnée de `i`, ps `i`. Pour modifier `i`, il faut la passer directement à la fonction via un pointeur :

```c#
#include <stdio.h>

void modification_p(int *x) {

  *x = 12;

}

int main() {

int i = 0;

modification_p(&i)

printf("Entier : %i\n", i);
}

```

Cette technique est très puissante et est utilisée massivement e `C`.

### scanf

La fonction [`scanf`{.language-}](http://ressources.unit.eu/cours/Cfacile/co/ch4_p5_6.html) demande à l'entrée standard (les champs sont séparés par des espaces par défaut) de renseigner une variable. On l'utilise de cette manière :

```c#
#include <stdio.h>

int main() {

int i = 0;

scanf("Tapez un entier signé : %i", &i);
printf("Entier (signé) : %i\n", i);
}

```

On voit l'utilité des pointeurs car sans eux il serait impossible de modifier une variable d'un type donnée. La fonction ne pouvant avoir qu'un type donné de sortie, le seul possible serait `void*` et elle devrait devrait allouer elle-même de la mémoire pour y stocker le retour demandé.

### Retour multiples de fonctions

Une fonction en `C` rend toujours 1 unique résultat. Il est donc impossible de faire comme en python l'astuce suivante :

```python
def double_si_positif(x):
  if x > 0:
    return true, 2 * x
  else :
    return false, x

réussi, x = double_si_positif(x)
```

Si l'on faire ce genre de chose, il faut :

- choisir quel sera le return
- modifier les autres choses via des pointeurs

En reprenant l'exemple précédent, le paramètre de retour est clair, c'est le booléen. Il faut alors modifier `x` via un pointeur :

```c
#include <stdio.h>

int double_si_positif(int *x) {
  if (*x >0) {
    *x = 2 * (*x);

    return 1;
  } 
  
  return 0;
}

int main() {

int i = 0;

scanf("Tapez un entier signé : %i", &i);
int reussite = double_si_positif(&i)

printf("Entier (signé) : %i\n", i);
}

```

{% exercice %}

Créer une fonction qui échange deux variables passées en paramètre.

{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>

void swap(int *x, int *y) {
  int t = *x;

  *x = *y;
  *y = t;

}

int main() {

int i = 12;
int j = 34;

printf("avant swap : i=%i, j=%i\n", i, j);
swap(&i, &j);

printf("après swap : i=%i, j=%i\n", i, j);
}

```

{% enddetails %}

### Retour de pointeurs

Les pointeurs rendus par une fonction doivent uniquement concerner des pointeurs qui seront toujours vrais après l'exécution de la fonction. Le code suivant est par exemple faux :

```c
#include <stdio.h>

int *retour_faux() {
  int t = 12;

  return &t;
}

int main() {

int *i = retour_faux();

printf("Entier : i=%i\n", i);

}

```

La variable `t` n'est plus valable en sorte de fonction : son adresse n'est plus utilisée !

{% attention "**danger !**" %}
Ne pas rendre une pointeur sur une une variable crée dans une fonction.
{% endattention %}

## Pointeurs de fonctions

Il est tout à fait possible d'avoir un pointeur sur une fonction et d'utiliser le pointeur pour l'appeler.

{% lien %}
[Pointeur sur une fonction](https://www.youtube.com/watch?v=axngwDJ79GY)
{% endlien %}

```c
int fahrenheit(int x) {
  return (x * 9/5) + 32;
} 
```

La signature de cette fonction est :

```c
double fahrenheit(int);
```

Son type est `double function(int)`. On peut alors créer un pointeur sur une fonction ayant sa signature en écrivant :

```c
double (*p)(int)
```

Puisque `(*p)` sera de type `int function(int)`.

{% attention "**danger !**" %}

Les parenthèses sont importantes car : `double *p(int)`{.language-} correspond à la signature d'une fonction nommée p qui rend un pointeur sur un double en sortie.

Dans le doute mettez **toujours** des parenthèses lorsque vous voulez une indirection.
{% endattention %}

Le code suivant est alors tout à fait fonctionnel :

```c#
#include <stdio.h>

double fahrenheit(int x) {
  return (x * 9.0/5) + 32;
}

int main() {

double (*p)(int) = &fahrenheit;

printf("%f \n", p(1));

}

```

{% info %}
Dans le code précédent, on aurait aussi pu écrire en ligne 9 :

```c
double (*p)(int) = fahrenheit;

```

On a `fahrenheit = &fahrenheit`.

{% endinfo %}

Cette technique permet d'utiliser des fonctions en paramètre d'autres fonctions. Par exemple :

```c
#include <stdio.h>

double fahrenheit(int celcius) {
  return (celcius * 9.0/5) + 32;
}

double kelvin(int celcius) {
  return celcius + 273.15;
}

double conversion(int celcius, double (*f)(int)) {
    return f(celcius);

}

int main() {

printf("%f \n", conversion(37,  fahrenheit));
printf("%f \n", conversion(37, kelvin));

}

```

{% lien %}
[Comprendre tout les types de fonctions](https://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations#funct_ptrs)
{% endlien %}
