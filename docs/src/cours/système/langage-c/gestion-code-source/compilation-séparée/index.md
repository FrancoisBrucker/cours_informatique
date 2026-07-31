---
layout: layout/post.njk

title: Compilation séparée

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Reprenons [le code vu précédemment](../#code){.interne} et séparons le code du fichier `degres.c`{.fichiers} en unités fonctionnelles :

1. un fichier `main.c`{.fichier} qui regroupera uniquement le programme principal
2. un fichier `celcius.c`{.fichier} qui regroupera uniquement les fonctions de conversions

Ce que l'on sait de la compilation nous permet de comprendre commet organiser ces deux fichiers :

1. le fichier `main.c`{.fichier} peut utiliser des fonctions non déclarées si :
   1. il connaît leurs signatures
   2. elles sont inclues à l'édition de lien
2. le fichier `celcius.c`{.fichier} peut être inclut uniquement à l'édition de lien et peut être compilé de façon séparée

## Fichiers

Fichier `main.c`{.fichier} :

```c
#include <stdio.h>

double fahrenheit(int celcius);
int kelvin(int celcius);

int main() {

printf("%f \n", fahrenheit(37));
printf("%i \n", kelvin(37));

}

```

Fichier `celcius.c`{.fichier} :

```c
double fahrenheit(int celcius) {
  return (celcius * 9.0/5) + 32;
}

int kelvin(int celcius) {
  return celcius + 273;
}

```

On peut ensuite procéder à notre compilation en plusieurs étapes :

1. compilation des objets :
   - `clang -c main.c`
   - `clang -c celcius.c`
2. édition de lien : `clang main.o celcius.o`

Si l'on ne modifie qu'un seul fichier, disons le fichier `main.c`{.fichier} il n'est pas nécessaire de recompiler `celcius.c`{.fichier}

Il nous reste cependant une dépendance entre les deux fichiers : la déclaration des fonctions de `celcius.c`{.fichier} dans `main.c`{.fichier}.

## Fichiers d'entêtes

Pour ne pas avoir à déclarer explicitement les fonctions de `celcius.c`{.fichier} dans `main.c`{.fichier}, on va utiliser un fichier annexe qui va les contenir :

Fichier `celcius.h`{.fichier} à inclure au projet dans le même dossier que `main.c`{.fichier} et `celcius.c`{.fichier} :

```c
double fahrenheit(int celcius);
int kelvin(int celcius);
```

Le fichier `main.c`{.fichier} devient alors :

```c
#include <stdio.h>
#include "celcius.h"

int main() {

printf("%f \n", fahrenheit(37));
printf("%i \n", kelvin(37));

}

```

Notez que comme le fichier `celcius.h`{.fichier} est spécifique au projet (il est dans le même dossier que le reste du programme), on utilise des `"` pour l'inclure. Le préprocesseur `C` allant chercher ces fichiers en priorité dans le projet.

## Prévenir l'inclusion multiple

A chaque fois qu'un fichier aura besoin d'utiliser des fonction de `celcius.c`{.fichier}, il lui faudra inclure son fichier de headers `celcius.h`{.fichier}. S'il est inclus plusieurs fois, le préprocesseur le recopiera plusieurs fois.

Par exemple le fichier `test.c`{.fichier} :

```c
#include "celcius.h"
#include "celcius.h"

int main() {

return 0;
}
```

Donnera après la phase du préprocesseur (`clang -E test.c`) le fichier :

```
# 1 "celcius.c"
# 1 "<built-in>" 1
# 1 "<built-in>" 3
# 418 "<built-in>" 3
# 1 "<command line>" 1
# 1 "<built-in>" 2
# 1 "celcius.c" 2
# 1 "./celcius.h" 1
double fahrenheit(int celcius);
int kelvin(int celcius);
# 2 "celcius.c" 2
# 1 "./celcius.h" 1
double fahrenheit(int celcius);
int kelvin(int celcius);
# 3 "celcius.c" 2

int main() {

return 0;
}

```

Qui inclut bien deux fois dans le même fichier le fichier `celcius.h`{.fichier}.

POur éviter ceci on ajoute [une astuce](https://gcc.gnu.org/onlinedocs/cpp/Once-Only-Headers.html) qui utilise le préprocesseur. Le fichier `celcius.h`{.fichier} sera écrit :

```c
#ifndef FILE_CELCIUS
#define FILE_CELCIUS

double fahrenheit(int celcius);
int kelvin(int celcius);

#endif
```

A la première lecture, la constante `FILE_CELCIUS` n'existe pas et on écrit tout le fichier, à la deuxième la constante est définie et donc le préprocesseur saute la partie définition.

La preuve en regardant le résultat de la phase du préprocesseur du fichier `test.c`{.fichier} avec ce nouveau fichier d'entête :

```
# 1 "celcius.c"
# 1 "<built-in>" 1
# 1 "<built-in>" 3
# 418 "<built-in>" 3
# 1 "<command line>" 1
# 1 "<built-in>" 2
# 1 "celcius.c" 2
# 1 "./celcius.h" 1



double fahrenheit(int celcius);
int kelvin(int celcius);
# 2 "celcius.c" 2


int main() {

return 0;
}

```

## Résumé

Séparez votre programme en autant de d'unités sémantiques. Chaque unité est composée :

1. d'un fichier d'entête (`.h`) contenant les signatures des différentes fonctions mises à disposition du programme
2. d'un fichier `.c` contenant le corps de ces fonctions

Lorsque l'on veut utiliser une fonction définie dans une unité sémantique, on inclut son `.h` en utilisant les `"` (à la différence des inclusions système qui sont inclues entre `<>`).

Enfin, la fonction `main` qui constitue le programme principal est ans son fichier à part, nommé `main.c`{.fichier}.

La compilation se fait en deux temps :

1. compilation en objet `.o` en utilisant l'option `-c`
2. édition de liens de différents fichiers objets

Dans le cadre de notre exemple, on a 3 fichiers :

`celcius.h`{.fichier} :

```c

double fahrenheit(int celcius);
int kelvin(int celcius);
#ifndef FILE_CELCIUS
#define FILE_CELCIUS

double fahrenheit(int celcius);
int kelvin(int celcius);

#endif

```

`celcius.c`{.fichier} :

```c
double fahrenheit(int celcius) {
  return (celcius * 9.0/5) + 32;
}

int kelvin(int celcius) {
  return celcius + 273;
}

```

`main.c`{.fichier} :

```c
#include <stdio.h>
#include "celcius.h"

int main() {

printf("%3.2f \n", fahrenheit(37));
printf("%i \n", kelvin(37));

}

```

Phases de compilation :

1. compilation en objet : `clang -c main.c celcius.c` qui produit les fichiers `main.o`{.fichier} et `celcius.c`{.fichier}
2. édition de lien : `clang main.o celcius.o` qui produit le fichiers `a.out`{.fichier}
