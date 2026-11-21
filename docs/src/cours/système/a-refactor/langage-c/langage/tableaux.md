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
int tableau[] = {1, 3};
```

Un tableau a une taille qui vaut le nombre de byte nécessaire à son stockage. Le tableau précédent à donc une taille de `2 * sizeof(int)`, qui est égal à *B sur ma machine (un `int`{.language-} y est stocké sur 4B).

Tout comme un pointeur, un tableau peut être vu comme une indirection :

```c
type (variable[N]);
```

`variable`{.language-} est une suite de N données de type type contiguës.

On ne peut uniquement accéder qu'à un élément du tableau à la fois, il est donc impossible :

- de comparer deux tableaux
- d'assigner un tableau à un autre

## Accès aux éléments

On utilise les tableaux comme en python, entre crochet.

```c

int tableau[3] = { 0 };

tableau[1] = 42;

printf("la première valeur du tableau est %i\n", tableau[0]);
printf("la seconde valeur du tableau est %i\n", tableau[1]);
printf("la troisième valeur du tableau est %i\n", tableau[2]);
```

{% exercice %}
Connaître le nombre d'élément d'un tableau non vide sans connaître son type ?
{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>


int main(void) {

    int t[2] = {1, 3};
    
    printf("Taille de t : %zu\n", sizeof(t) / sizeof(t[0]));

    return 0;
}


```

{% enddetails %}

## Tableaux et pointeurs

Pointeurs et tableaux ne sont pas identiques, mais ils partagent des propriétés. Par exemple, si :

```c
int tableau[20] = {0};
```

Alors `tableau` est l'adresse du premier élément du tableau, c'est 0 dire qu'en `C` on a les 3 égalités suivantes :

```c
tableau = &(tableau[0]) = &tableau
```

{% exercice %}
Créez un programme qui vérifie les 3 égalités ci-dessus.
{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>

int main() {

int *t[10] = {0};

printf("%p \n", (void*)t);
printf("%p \n", (void*)&(t[0]));
printf("%p \n", (void*)&t);

}

```

{% enddetails %}

Ce qui fait que l'on peut écrire :

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

### Tableaux et arithmétique de pointeurs

L'addition de pointeurs fonctionne ainsi : Si `p` est un pointeur et `K` un entier alors `p + K`{.language-} est :

- un pointeur sur le même type que `p`
- sa valeur vaut la valeur de `p` incrémenté de `K * sizeof(*p)`{.language-}

{% attention "**danger !**" %}
Le pas d'incrémentation dépend du type de l'objet pointé.
{% endattention  %}

Ce fonctionnement est fait pour faire fonctionner de concert les pointeurs et les tableaux. Considérez par exemple le code suivant, souvent utilisé :

```c
#include <stdio.h>

int main() {

  int t[] = {1, 2, 3, 4, 5, 6};
  const size_t N = 6;

  int *p = t;

  for (size_t i=0 ; i < N ; i++) {
    printf("t[%zu] = %i\n", i, *p);
    p++;
  }

  return 0;
}

```

Enfin, on peut utiliser la même technique directement pour un tableau. Le code suivant un pointeur au 5ème élément d'un tableau :
 :

```c
#include <stdio.h>

int main() {

  int tableau[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  int *p = tableau + 4;

  printf("Un entier : %i\n", *p);

  return 0;
}

```

On ne peux cependant pas incrémenter un tableau : il est impossible d'écrire `tableau += 1`{.language-} ou encore `tableau++`{.language-}

## Tableaux de tableaux

On peut combiner les tableaux. Par exemple `int M[3][2]`{.language-} qui est un tableau de 3 tableaux de 2 entiers. On peut les initialiser explicitement :

```c
int M[3][2] = { {1, 2}, {3, 4}, {5, 6} };
```

Ou implicitement :

```c
int M[3][2] = {0};
```

Attention à l'ordre de lecture, les crochets se lisent de droite à gauche

1. le second et dernier crochet donne le nombre d'élément du type de base (ici `int`{.language-}) : le type actuel est "tableau de 2 `int`{.language-}"
2. le premier crochet (l'avant-dernier) donne le nombre d'élément du type courant ("tableau de 2 `int`{.language-}"), et donc notre type devient : "tableau de 3 (tableau de 2 `int`{.language-})"

{% exercice %}

Comment initialiseriez vous explicitement un tableau de type : `int M[4][3][2]` ?

{% endexercice %}
{% details "solution" %}

On lit de droite à gauche :

1. tableau de 2 int
2. tableau de 3 (tableau de 2 int)
3. tableau de 4 (tableau de 3 (tableau de 2 int))

On peut donc l'initialiser explicitement comme ça :

```c
#include <stdio.h>

int main() {

    int M[4][3][2] = { { {1, 2}, {3, 4}, {5, 6} }, 
                       { {7, 8}, {9, 10}, {11, 12} },
                       { {13, 14}, {15, 16}, {17, 18} },
                       { {19, 20}, {21, 22}, {23, 24} } };

    for (size_t i=0 ; i < 4 ; i++) {
        for (size_t j=0 ; j < 3 ; j++) {
            for (size_t k=0 ; k < 2 ; k++) {
                printf("M[%zu][%zu][%zu] = %i\n", i, j, k, M[i][j][k]);    
            }
            
        }

    }

    return 0;
}

```

{% enddetails %}

De la même façon que l'on a pu écrire :

```c

int t[4] = {0};
int *p = t;

```

On peut écrire :

```c

int M[3][2] = {0};
int (*p)[2] = M;

```

Puisque :

- `M` est un tableau de "tableau de 2 int"
- en écrivant `int (*p)[2]` :
  - p est une indirection vers le type
  - le type est un tableau de 2 int
  
{% attention "**danger !**" %}
Les parenthèses sont indispensables. En effet, de part les règles de priorité on a :

```c
*p[2] = *(p[2])
```

Ce qui n'est pas ce que l'on veut.

{% endattention %}

On peut ensuite procéder comme précédemment. Voyons si vous avez compris :

{% exercice %}
On suppose que l'on a les deux déclarations de variables suivantes :

```c
int M[3][2] = { {1, 2}, {3, 4}, {5, 6}};
int (*p)[2] = M;
```

Que vaut :

- `(*p)[1]`{.language-} ?
- `*(p[1]) = *p[1]`{.language-} ?
- `(*(p+1))[1]`{.language-} ?
- `(M+2)[0][0]`{.language-} ?
{% endexercice %}
{% details "solution" %}

```c
#include <stdio.h>


int main(void) {
    
    int M[3][2] = { {1, 2}, {3, 4}, {5, 6} };
    int (*p)[2] = M;
    
    printf("%i\n", (*p)[1]);
    printf("%i\n", *(p[1]));
    printf("%i\n", (*(p+1))[1]);
    printf("%i\n", (M+2)[0][0]);

    return 0;
}

```

- `(*p)[1]`{.language-} : `p`{.language-} est un pointeur sur un tableau à 2 élément et il pointe sur le premier élément de `M`{.language-}. Donc `(*p)[1] = M[0][1]`{.language-}
- `*(p[1]) = *p[1]`{.language-} : `p[1] = p + 1`{.language-}. Comme `p`{.language-} est un pointeur sur un tableau à 2 élément et qu'il pointe sur le premier élément de `M`{.language-}, on a que `*(p+1) = M[1][0]`{.language-}.
- `(*(p+1))[1]`{.language-}. Le même raisonnement que précédemment donne `(*(p+1))[1] = M[1][1]`{.language-}
- `(M+2)[0][0] = M[2][0]`{.language-}

{% enddetails %}

## Tableaux de pointeurs de fonctions

Finissons avec une technique qui peut parfois se révéler utile et qui clora cette partie : le tableau de pointeurs de fonctions.

Commençons par définir les deux fonctions dont ont construira le tableau :

```c
int add(int i, int j) {
    return i + j;
}


int mul(int i, int j) {
    return i * j;
}
```

Le type des deux fonctions est le même :

```c
int (function)(int, int)
```

Un pointeur `p` sur un de ces fonction s'écrit alors :

```c
int (*p)(int, int)
```

Et enfin, un tableau de 2 pointeurs s'écrira :

```c
int (*(t[2]))(int, int)
```

Ce qui est équivalent à :

```c
int (*t[2])(int, int)
```

On peut maintenant utiliser ce tableau :

```c
#include <stdio.h>

int add(int i, int j) {
    return i + j;
}

int mul(int i, int j) {
    return i * j;
}

int main() {

  int (*t[2])(int, int) = {add, mul};

  for (size_t i=0; i < 2 ; i++) {
      printf("i=%zu , f(1, 2) = %i\n", i, t[i](1, 2));
  }

}

```

{% aller %}
Ce genre de typage peut vite devenir très complexe. Heureusement, il n'y a que très peu de chance que vous tombiez sur un tel
[exemple bien complexe](https://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations#right_left_rule).
{% endaller %}
