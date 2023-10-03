---
layout: layout/post.njk

title: C pour le système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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
    printf("Hello World!\n");

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

On utilise le compilateur [clang](https://clang.llvm.org/), fait pour compiler de nombreux langages, dont le C.

```
clang hello.c
```

La compilation a crée un fichier exécutable `a.out`{.fichier} dans le dossier courant :

```
./a.out
```

Notez que si vous voulez exécuter le résultat de la compilation uniquement si la compilation a réussie, vous pouvez utiliser la commande :

```
clang hello.c && ./a.out
```

On peut toujours préciser le fichier de sortie avec l'option `-o`. Par exemple :

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

{% note %}

Utilisez toujours les options de compilation très strictes :

```
clang hello.c -Wall -Wextra -Werror -pedantic -std=c23
```

(ou `-std=c2x` si votre compilateur n'est pas le plus récent)
{% endnote %}
{% exercice %}
A quoi correspondent les [options llvm](https://clang.llvm.org/docs/UsersManual.html) ajoutées ?
{% endexercice %}
{% details "solution" %}

- `-Wall -Wextra` : tous les warnings
- `-Werror` : les warnings sont considérés comme des erreurs, cela stope le process de compilation
- `-std=c23` : se conforme au standard de code `c23` du C
- `-pedantic` : vérifie que le standard `c23` et uniquement lui est bien respecté.
{% enddetails %}

{% info %}
Pour référence :

<https://linuxfr.org/news/nouveautes-du-langage-c-dans-sa-prochaine-version-c23>

Pour l'instant cela doit vous sembler incompréhensible, c'est normal.
{% endinfo %}

De plus, le compilateur C est très efficace pur trouver des optimisations à votre code. Pour ne pas le prendre en traître, restez simple dans votre code.

## Éléments de langage

{% lien %}
[Langage C](./langage/){.interne}
{% endlien %}

1. malloc (pointeur + malloc = python).
1. gestion des fichiers et entrées/sorties
2. plusieurs fichiers de sources, bibliothèques et make
3. tests


- projet :
  - makefile : 2 fichiers et .h associés
  - test
  - ajout lib en [static](https://dev.to/iamkhalil42/all-you-need-to-know-about-c-static-libraries-1o0b)
exemple avec tout, et étapes de compil :

- où sont les .h <> vs ""

- *a et &a sont des indirections
- fonction :
  - déclaration
  - définition
- typedef
- scope p18 et storage duration. tout dans la stack
- char dépend du `LOCALE` : pratiquement tout le temps utf-8. Si on veut être sur on utilise les types spécifiques. C'est aussi la plus petite unité de stockage. Donc 8bit. On s'en fiche si c'est signed ou non du moment qu'on l'utilise exclusivement pour les chaines de caractères. Si on veut être explicite, on utilise `char8_t` à la place partout en c23.
- <https://www.reddit.com/r/cpp_questions/comments/jetu17/what_is_difference_between_size_t_unsigned_int/>

## Compilation séparée

### Utilisation de fonctions de la libc

La `libc` est inclue par défaut dans la compilation. Elle définit tout un tas de fonctions utiles réparties en autant de fichier de de déclarations.

On connaissez déjà `printf` dont la déclaration est dans le fichier `stdio.h` (dans les bibliothèques systèmes). Mais il en existe de nombreuses autres très utiles dans la majorité des programmes `C`.

{% exercice %}
En utilisant la fonction `ceil` de la bibliothèque [math de la libc](https://www.geeksforgeeks.org/c-library-math-h-functions/) de fichier de déclaration `math.h` (dans les bibliothèques systèmes), faites en sorte que votre fonction farhenheit rende le plus petit entier plus grand que la valeur exacte de conversion.
{% endexercice %}

### makefile

Il est courant de déplacer ses fonctions dans des fichiers séparés pour ne pas avoir à les recompiler à chaque fois.

Pour que ça fonctionne, il faut qu'il n'y ait qu'un seul fichier contenant une fonction main. Les autres fichiers seront considérés comme des ensembles de fonctions utiles.

{% exercice %}

{% endexercice %}

1. avec la signature
2. puis un point.h
3. puis on combine le tout avec un makefile

## TBD

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
- [cours OpenClassroom](https://openclassrooms.com/fr/courses/19980-apprenez-a-programmer-en-c)
- [C programming a modern approach](https://github.com/Embed-Threads/Learn-C/blob/main/books/c-programming-a-modern-approach-2nbsped-0393979504-9780393979503_compress.pdf)
