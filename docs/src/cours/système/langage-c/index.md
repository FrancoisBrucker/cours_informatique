---
layout: layout/post.njk

title: C pour le système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## plan

Faire une série de codes + compilation pour illustrer les thèmes.

1. compilation + type
2. boucles
3. while
4. if/then/else
5. ...

## Histoire

Le  [C a été créé pour créer Unix](https://www.youtube.com/watch?v=de2Hsvxaf8M). Son but est de créer des systèmes d'exploitation. Il :

- est très proche de la machine
- fait confiance au développeur et n'effectue aucune vérification

Le but est de ne pas avoir d'[overhead](https://en.wikipedia.org/wiki/Overhead_(computing)) dans l'exécution du code. C'est donc un formidable langage pour comprendre le fonctionnement d'un ordinateur.

Il existe plusieurs compilateurs permettant de produire du code machine à partir d'un programme en C. On peut en citer deux : [gcc](https://gcc.gnu.org/) et [llvm](https://llvm.org/). Nous utiliserons ce dernier dans ce cours.

C n'a cessé d'évoluer au cours du temps. La norme actuelle date de 2023 (dite `c23`), c'est elle que nous utiliserons et qui remplace la dernière spécification datant de 2017 (la `c17`).

## Installation llvm

Il existe plusieurs compilateurs de `C`. Nous allons utiliser [llvm](https://apt.llvm.org/) pour ce cours.

{% aller %}
[Installation du compilateur](installation){.interne}
{% endaller %}

## Premier programme

Fichier `hello.c`{.fichier} :

```c#
#include <stdlib.h> 
#include <stdio.h>

int main() { 
    printf(u8"Hello World!\n");

    return EXIT_SUCCESS; 
}
```

### Détails du code

ligne à ligne

En comparant par rapport à un code python :

- les imports sont notées `#include`
- les fonctions sont définies avec les types :
  - de leur sortie, ici `int`, un entier signé
  - le type de la chaîne de caractère doit être spécifié, ici de l'UTF-8
  - de leurs paramètres, ici comme en python `()` signifie qu'il n'y en a pas
- les blocs ne sont gérées par des `{}` et non par l'indentation.
- la fin d'une commande doit être signalée par un `;`

{% info %}
Venant du python, il peut sembler grisant de pouvoir écrire plusieurs instructions sur une ligne, par exemple :

```
int main(void){printf("Hello World!\n");return EXIT_SUCCESS;}
```

Est tout à fait valable.

Mais ne le faite pas. Du code non clairement indenté vous sautera tôt ou tard à la figure.
{% endinfo %}
{% info %}
Vous verrez aussi parfois écrire `main(void)` qui utilise le mot clé `void` qui signifie le vide à la place de `main()`. Ce n'est plus nécessaire depuis la révision 2023 du C.
{% endinfo %}
{% info %}
Si vous ne spécifiez pas le type de la chaîne de caractère son type est indéfini, il dépend de la locale du système. Il n'est défini que pour les caractère ASCII sur 7bits.
{% endinfo %}

### Compilation

> ici mettre toutes les options

On utilise le compilateur [clang](https://clang.llvm.org/), fait pour compiler de nombreux langages, dont le C.

```
clang hello.c
```

La compilation a crée un fichier exécutable `a.out`{.fichier} dans le dossier courant :

```
./a.out
```

On peut toujours préciser le fichier de sortie vec l'option `-o`. Par exemple :

```
clang hello.c -o hello
```

Produire l'exécutable `hello`{.fichier}

{% info %}
En ajoutant l'option `-v`, verbose, clang détaille ses opérations. N'hésitez pas à le faire à chaque commande pour voir ce qu'il fait effectivement.
{% endinfo %}

{% lien %}
[La compilation](compilation){.interne}
{% endlien %}

## Règles de survie

Un célèbre dicton dit qu' *"en C, les soucis commencent lorsque le code compile"*.

Le C ne fait en effet aucune vérification par défaut ni n'installe de protection : il fait une confiance aveugle au développeur.

Ceci permet de faire du code qui s'exécute très rapidement, mais qui se conçoit lentement car il faut être assuré qu'il fonctionne parfaitement.

Il y a donc quelques règles à respecter pour se simplifier la tâche de développement :

- être explicite
  - pas de magic number
  - typage explicite
- on ne fait pas le malin :
  - avec le préprocesseur
  - avec les subtilités syntaxiques du langage
- utilisez toujours les options `-Wall -Werror -pedantic -std=c23` (ou `-std=c2x` si votre compilateur n'est pas le plus récent)

{% info %}
Pour référence :

<https://linuxfr.org/news/nouveautes-du-langage-c-dans-sa-prochaine-version-c23>

Pour l'instant cela doit vous sembler incompréhensible, c'est normal.
{% endinfo %}

De plus, le compilateur C est très efficace pur trouver des optimisations à votre code. Pour ne pas le prendre en traître, restez simple dans votre code.

## Éléments de langage

1. types de base
   1. char
   2. int
   3. double (et float)
   4. type dérivés short, unsigned, long
   5. spécificateur volatile
   6. exemples avec printf/scanf
   7. sizeof
   8. cast explicites et implicites
2. Types dérivées :
   1. tableaux
   2. strings
   3. pointeurs
3. stockage :
   1. tout dans la stack
   2. protée
4. structures de contrôle
5. fonctions
6. struct et enum
7. typedef et size_t, struct

8. fichiers et entrées/sorties
9.  malloc
10. plusieurs fichiers, bibliothèques et make
11. tests

Ajouter des exos à faire

- commentaires
- type -> type dérivé (tableau et pointeur)
- en python **tout** est une indirection.
- structure
- fonctions (signature et type fonction)
- cast et void
- ce qui est important en C c'est le type. Accessible directement ou via une indirection (l'`*`)
- type et durée de vie d'une variable

- typedef à utiliser :
  - size_t
  - char8

1. types
   1. chaîne
   2. int

<https://en.wikipedia.org/wiki/C_data_types#Member_data_types>

- projet :
  - makefile : 2 fichiers et .h associés
  - test
  - ajout lib en [static](https://dev.to/iamkhalil42/all-you-need-to-know-about-c-static-libraries-1o0b)
exemple avec tout, et étapes de compil :

- où sont les .h <> vs ""

- variables
- struct
- une seule déclaration de variable par ligne (a cause des pointeurs)
- *a et &a sont des indirections
- fonction :
  - déclaration
  - définition
- typedef
- scope p18 et storage duration. tout dans la stack
- char dépend du `LOCALE` : pratiquement tout le temps utf-8. Si on veut être sur on utilise les types spécifiques. C'est aussi la plus petite unité de stockage. Donc 8bit. On s'en fiche si c'est signed ou non du moment qu'on l'utilise exclusivement pour les chaines de caractères. Si on veut être explicite, on utilise `char8_t` à la place partout en c23.
- <https://www.reddit.com/r/cpp_questions/comments/jetu17/what_is_difference_between_size_t_unsigned_int/>

## TBD

- udefined behaviour simple : <https://www.youtube.com/watch?v=VONnWLo7abU>
- gros exemple : <https://www.youtube.com/watch?v=va_UZwTVR5g>
- utiliser une fonction de hash puis dictionnaire circulaire de knuth
- fonctionnement de malloc avec les blocs libres
- pointeur et cast différents type pour voir la différence. TOu est toujours dépendant du type, uie de l'interprétation
- le C se focalise sur l'utilisation, donc la valeur et son type. C'est pourquoi on écrit `int *p` (la valeur est accédée via un pointeur); et pas `int* p` (un pointeur sur un entier)
- [f() vs f(void)](https://www.youtube.com/watch?v=VsRs0H4hXEE)
- [pointeur sur fonction](https://www.youtube.com/watch?v=axngwDJ79GY)
- [diff entre clone, fork, vfork](https://www.baeldung.com/linux/fork-vfork-exec-clone)
- fork/clone : avec strace : <https://www.youtube.com/watch?v=uRYyj8tcDTE&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=17>
- complet : [C et segments mémoires utilisées](https://gist.github.com/CMCDragonkai/10ab53654b2aa6ce55c11cfc5b2432a4)
- [préprocesseur](http://jhnet.co.uk/articles/cpp_magic)
- [timer](https://0xax.gitbooks.io/linux-insides/content/Timers/linux-timers-6.html)
- [une histoire d'amour à sens unix](https://www.cise.ufl.edu/~manuel/obfuscate/westley.hint)
- [ascii art](https://www.welcometothejungle.com/fr/articles/btc-poem-code-avalanche-stars)
- [encore des poèmes](https://code-poetry.com/water)
- memory leak detection : <https://github.com/google/sanitizers/wiki/AddressSanitizer> (<https://clang.llvm.org/docs/AddressSanitizer.html>) pour remplacer <https://valgrind.org/> qui ne marche pas sous ARM.

- [algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [listes chaînées intrusives](https://www.data-structures-in-practice.com/intrusive-linked-lists/)

## Bibliographie

- <https://learncodethehardway.org/c/>
- [effective C](https://www.amazon.fr/Effective-Introduction-Professional-Robert-Seacord/dp/1718501048/)
- [modern C](https://gustedt.gitlabpages.inria.fr/modern-c/)
