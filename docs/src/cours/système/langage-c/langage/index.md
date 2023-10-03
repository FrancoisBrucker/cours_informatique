---
layout: layout/post.njk

title: Langage C

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : ajouter des "on ne fait pas le malin" pour les choses un peu tricky.

## Commentaires

Deux types de commentaires :

Sur plusieurs lignes :

```
/* commentaire sur 

plusieurs

lignes

*/
```

Tout ce qui est entre `/*` et `*/` est ignoré

Sur une ligne :

```
// commentaire sur une ligne
```

Tout ce qui est après `//` sur la même ligne est ignoré.

## Types de base

{% lien %}
[Types de données](types-base){.interne}
{% endlien %}

Une seule déclaration de variable par ligne (a cause des pointeurs)

## Fonctions

```c
type_de_retour nom(paramètres) {
  instructions de la fonction 

  return valeur_de_type_de_retour;
}
```

Le type de retour est obligatoire. Si la fonction ne retourne rien son type de retour doit être `void`.

La signature de la fonction est ce qui est nécessaire pour la caractériser :

- son type de retour
- son nom
- ses paramètres et leurs types

Par exemple :

```c
int fahrenheit(int x) {
  return (x * 9/5) + 32;
} 
```

Sa signature est :

```c
int fahrenheit(int);
```

Si on définit une fonction à l'intérieur d'une autre fonction, son scope est réduit à la fonction dans laquelle elle est décrite. Pour vos programmes, il faut doc mettre les fonctions en-dehors de la fonction main :

```c
#include <stdio.h>

int fahrenheit(int x) {
  return (x * 9/5) + 32;
} 

int main() {
  printf("%d\n", fahrenheit(0))
}

```

{% exercice %}

Transformez la fonction pour que sa signature soit `double fahrenheit(int);`{.language-} (vérifiez que la fonction rendent bien que 0C soit égal à 33.8F)

{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}

## Pointeurs

{% lien %}
[Pointeurs](pointeurs){.interne}
{% endlien %}

{% exercice %}

input et cast
    - demander avec [`scanf`{.language-}](http://ressources.unit.eu/cours/Cfacile/co/ch4_p5_6.html) à l'utilisateur un entier correspondant à un degré Celsius
    - le convertir en degré Fahrenheit et l'afficher à l'écran
{% endexercice %}

## Tableaux

{% lien %}
[Tableaux](tableaux){.interne}
{% endlien %}

## Chaînes de caractères

{% lien %}
[Chaînes de caractères](chaines-caractères){.interne}
{% endlien %}

## Qualificateur

qualificateur : const, volatile, restrict

attention ce qui est const c'est le type pas le type pointé...
Et on peut avec des pointeur tout modifier avec des cast.

## Structures de contrôle

En `C` le type booléen n'existe pas (il existe un typedef pour cela). Une condition est un entier qui est considéré comme :

- vrai s'il est strictement positif
- faux s'il est nul

Pour les conditions utiliser les [opérateurs logiques](https://www.tutorialspoint.com/cprogramming/c_logical_operators.htm).

{% attention "**ne faites pas les malins**" %}
Ne confondez pas `&&` et `&` ainsi que `||` et `|`.
{% endattention %}

### if/then/else

```c
if (condition) {
  // bloc if
} else {
  // bloc else
}
```

Le else est facultatif.

{% attention "**ne faites pas les malins**" %}
Mettez toujours des `{}` à vos conditions, même s'il existe une exception.
{% endattention %}

La structure `elif` n'existe pas en `C`. On chaîne les tests :

```c
if (condition) {
  // bloc if
} 
else if (condition2) {
  // bloc else if
} else {
  // bloc else
}
```

> TBD exemple

### while

Deux flavors de while :

```c
while (condition) {
  // bloc while
}
```

et :

```c
do {
  // bloc do while
} while (condition)
```

> TBD exemple

### opérateur ternaire

```c
condition ? expr2 : expr2;
```

Qui est équivalent à :

```c
if (condition) {
  expr1
} else (
  expr2
)
```

sur une ligne

> TBD exemple

### boucle for

```c
for (expr1 ; condition ; expr2) {
  // bloc for
}
```

Qui est équivalent à la structure while :

```c
expr1;
while (condition) {
  
  // bloc for

  expr2;
}
```

```c
for (size_t i = 0 ; i < 10 ; i++) {
  printf("%zu ", i);
}
printf("\n");
```

pour faire une boucle for sur des opérations. <https://www.geeksforgeeks.org/function-pointer-in-c/>

## Les structures

Une structure est un type dérivé permettant de regrouper des données de type hétérogène. Par exemple, on définie une structure `personne`{.language-} :

```c
struct personne {
  char *prénom;
  int age;
};
```

Pour créer une variable de cette structure, comme ce n'est ni un type reconnu ni un typedef il faut :

```c
struct personne x = {"Chun-Li", 55};
```

On peut ensuite accéder à chaque élément avec une notation pointée :

```c
#include <stdio.h>

int main() {

struct personne {
    char *prenom;
    int age;
};

struct personne x = { "Chun-Li", 55};

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

Il est bien sur possible de modifier les variables après la création :

```c
#include <stdio.h>

int main() {

struct personne {
    char *prenom;
    int age;
};

struct personne x = { "", 0};

x.prenom = "Ken";
x.age = 58;

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

Pour ne pas avoir à retaper `struct` avant chaque création, on a l'habitude de passer par un `typedef` : `typedef struct personne personne;`{.anguage-},
pour ensuite directement créer une personne par : `personne x = {"", 0};`.

On peut aussi tout faire en une fois et la déclaration du struct et le typedef :

```c
#include <stdio.h>

int main() {

typedef struct personne {
        char *prenom;
        int age;
} personne;

personne x = { "Chun-Li", 55};

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

On peut utiliser un struct dans un tableau, comme tout autre type, ou via un pointeur :

```c
personne ken = {"Ken", 56};
personne *p = &ken;
```

{% note %}
Utiliser un pointeur pour accéder à une structure étant tellement utilisée qu'il existe un raccourci : on peut écrire `p->x` à la place de `(*p).x`, ce qui est plus clair.
{% endnote %}

## enum

Le `C` permet aussi d'utiliser des [enum](https://www.w3schools.com/c/c_enums.php) pour gérer des modalités discrètes.

## Règles

Attention aux [Undefined Behavior (UB)](https://en.wikipedia.org/wiki/Undefined_behavior) résultant d'erreur de code qui font que :

- ces erreurs ne sont pas détectées à la compilation
- elles produisent des résultats différents selon les fois, les gens ou les compilateurs.

Voir par exemple [ce court tuto](https://www.youtube.com/watch?v=VONnWLo7abU) ou [celui-ci](https://www.youtube.com/watch?v=va_UZwTVR5g) (un peu plus long)

Cela rend le déboguage très difficile. Il faut donc toujours essayer d'être le plus explicite possible et surtout rester simple.

 1. cast explicites et implicites
 2. qualificateur : const, volatile, restrict
 3. règles :
    1. on initialise toutes les variables, pointeur à null
    2. char, int, double, size_t
    3. une seule variable déclarée par ligne (sinon effet de bord avec les pointeurs)
