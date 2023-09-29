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

créé pour créer Unix.

Plusieurs gcc, llvm.

## Installation llvm

Il existe plusieurs compilateurs de `C`. Nous allons utiliser [llvm](https://apt.llvm.org/) pour ce cours.

{% aller %}
[Installation du compilateur](installation){.interne}
{% endaller %}

## Premier programme

Fichier `hello.c`{.fichier} :

```c
#include <stdlib.h> 
#include <stdio.h>

int main(void) { 

    printf("Hello World!\n");

    return EXIT_SUCCESS; 
}
```

## Compilation

On utilise le compilateur [clang](https://clang.llvm.org/), fait pour compiler de nombreux langages, dont le C.

```
clang hello.c
```

La compilation a crée un fichier exécutable `a.out`{.fichier} dans le dossier courant :

```
./a.out
```

Le C est un langage compilé. C'est à dire qu'il va produire un fichier exécutable par la machine, dépendant du système d'exploitation.

1. hello world
2. étapes de compilation :
   1. ou est quoi
3. .h = :
   1. signatures
   2. préprocesseur
4. types
   1. chaîne
   2. int

## Étapes de compilations

1. [préprocesseur](https://fr.wikipedia.org/wiki/Pr%C3%A9processeur_C)
2. compilateur en ASM
3. compilateur ASM vers objet
4. édition de lien

### Préprocesseur

```
clang -E hello.c -o hello.i
```

{% info %}
Par défaut la sortie de l'option `-E` est la sortie standard. On précise donc le fichier de sortie par l'option `-o`.
{% endinfo %}

Notez que l'on directement compiler la sortie du préprocesseur, c'est toujours un code c valable

{% lien %}
[préprocesseur](préprocesseur){.interne}
{% endlien %}

Le but ce cette partie est :

1. d'inclure les fichiers `.h` des directives `#define` au code du programme que l'on compile, ici les deux fichiers `stdlib.h`{.fichier} et `stdio.h`{.fichier}. Ces fichiers sont présent dans les dossiers systèmes
2. de remplacer les constantes par leurs valeurs

Cette étape permet d'avoir un code où toutes les références sont explicites pour permettre une compilation du code.

{% exercice %}
Dans le code précédent quelle est l'intérêt d'inclure `stdlib.h`{.fichier} et `stdio.h`{.fichier} ?
{% endexercice %}
{% details "solution" %}
On supprime une oigne et on recompile pour voir.

En supprimant la ligne `#include <stdlib.h>` on obtient l'erreur de compilation :

```
hello.c:7:12: error: use of undeclared identifier 'EXIT_SUCCESS'
    return EXIT_SUCCESS; 
           ^
1 error generated.
```

Et en supprimant la ligne `#include <stdio.h>` on obtient l'erreur de compilation :

```
hello.c:5:5: error: call to undeclared library function 'printf' with type 'int (const char *, ...)'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
    printf("Hello World!\n");
    ^
hello.c:5:5: note: include the header <stdio.h> or explicitly provide a declaration for 'printf'
1 error generated.
```

Ne supprimez pas les 2 lignes en même temps, lors d'un processus de compilation, seule la 1ère erreur est significative. La seconde peut découler de la première...

{% enddetails %}


> TBD ajout de chemins de .h avec `-I`

### Compilation en assembleur

```
clang -S hello.c
```

{% info %}
Par défaut la sortie de l'option `-S` est un fichier d'extension `.a`. On précise donc pas le fichier de sortie par l'option `-o`, la commande va produire un fichier `hello.s`{.fichier}
{% endinfo %}

Par défaut c'est la syntaxe GNU qui est utilisée. Pour utiliser la syntaxe [nasm](https://www.nasm.us/), il faut rajouter des options :

```
clang -S hello.c -masm=intel   
```

### Compilation en Objets

```
clang -c hello.c 
```

{% info %}
Par défaut la sortie de l'option `-c` est un fichier d'extension `.o`. On précise donc pas le fichier de sortie par l'option `-o`, la commande va produire un fichier `hello.o`{.fichier}
{% endinfo %}

Cette phase transforme le code en fichier objet, au format ELF sous Linux. Ce fichier n'est pas exécutable car il ne possède pas le code de toutes les fonctions en particulier la fonction `printf`.

En effet, la directive include ne fait que donner la signature des fonctions que l'on a le droit d'utiliser. En l'état, notre code est identique à :

```c
#include <stdlib.h> 

int printf(const char* format, ...);

int main(void) { 

    printf("Hello World!\n");

    return EXIT_SUCCESS; 
}
```

Sa compilation fonctionnera de la même manière : le fichier objet contient :

- le code du fichier compilé
- une liste de signatures de fonctions utilisées mais non définies

C'est la partie suivante qui en fera un tout cohérent.

### Edition de liens

> TBD ajout de chemins de bibliothèque avec `-L`
> -nostdlib et il ne trouve plus printf : -lc
> static avec -static

> libc automatic, pas math.
> TBD ldd
L'édition de lien 
L'édition de lien va regrouper un ensemble de fichiers objets et de bibliothèques pour créer un exécutable.

Liens entre les différentes fonctions. Chaque appel de fonction doit être associée à un code. Via les signatures de fonctions.

> TBD exemple en regardant le .h qui définit les signatures utilisables.

## Règles de survie

- explicite
- on ne fait pas le malin


exemple avec tout, et étapes de compil :

- étapes
- où sont les .h <> vs ""
- édition de lien, où sont les libs
- statiques vs dynamiques
- variables
- struct

## TBD

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
