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

Fichier `hello.c`{.fivhier} :

```c
#include <stdlib.h> 
#include <stdio.h>

int main(void) { 

    printf("Hello World!");

    return EXIT_SUCCESS; 
}
```

### Compilation & exécution

#### Compilation

On utilise le compilateur [clang](https://clang.llvm.org/), fait pour compiler de nombreux langages, dont le C.

```
clang hello.c
```

#### Exécution

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

## Compilation

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
