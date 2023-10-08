---
layout: layout/post.njk

title: Compilation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Reprenons le code du fichier `hello.c`{.fichier} :

```c
#include <stdlib.h> 
#include <stdio.h>

int main(void) { 

    printf("Hello World!\n");

    return EXIT_SUCCESS; 
}
```

Compiler un programme C se fait en plusieurs étapes, dont les 4 principales sont :

1. [préprocesseur](https://fr.wikipedia.org/wiki/Pr%C3%A9processeur_C)
2. compilateur en ASM
3. compilateur ASM vers objet
4. édition de lien

## Étapes

### Préprocesseur

```
clang -E hello.c -o hello.i
```

{% info %}
Par défaut la sortie de l'option `-E` est la sortie standard. On précise donc le fichier de sortie par l'option `-o`.
{% endinfo %}

Notez que l'on directement compiler la sortie du préprocesseur, c'est toujours un code c valable

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

Le but de l'édition de lien est d'assembler les *bouts de codes* en un tout cohérent. Un *bout de code* étant :

- les objets compilées (les `.o`{.fichier})
- les bibliothèques statiques (les `.a` sous Linux) qui seront incluses dans le code final
- les bibliothèques partagées (les `.so` sous Linux, `.dylib` sous Macos et `.DLL` sous windows) : dont seule une référence sera incluse dans le code final.

```
clang hello.o
```

Le compilateur `clang` v ajouter les bibliothèques standard par défaut. On le voit en regardant les bibliothèques dynamiques utilisées par l'exécutable produit (grâce à la commande [`ldd`](https://man7.org/linux/man-pages/man1/ldd.1.html), `otool -L` sous macos):

```
ldd a.out
```

La [libc](https://www.gnu.org/software/libc/manual/html_node/index.html) est en particulier incluse. Cette bibliothèque est incluse dans quasi tout exécutable issu de `C`. C'est en particulier elle qui contient le code de la fonction [`printf`](https://www.gnu.org/software/libc/manual/html_node/Formatted-Output-Basics.html).

On peut tenter une édition de lien sans l'inclusion de bibliothèques par défaut :

```
clang hello.c -nostdlib
```

Qui va produire l'erreur :

```
Undefined symbols for architecture x86_64:
  "_printf", referenced from:
      _main in hello-ab8cef.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

```

On peut alors inclure la bibliothèque à la main avec l'option `-l` :

```
clang hello.c -nostdlib -lc
```

L'édition de lien fait deux choses :

- elle associe le code d'une fonction à son utilisation via sa [signature](https://developer.mozilla.org/fr/docs/Glossary/Signature/Function). C'est pourquoi il faut déclarer la fonction même si on a pas son code
- elle donne le point d'entrée du programme, la fonction `main`

## Règles de survie

Un célèbre dicton dit qu' *"en C, les soucis commencent lorsque le code compile"*.

Le C ne fait en effet aucune vérification par défaut ni n'installe de protection : il fait une confiance aveugle au développeur.

Ceci permet de faire du code qui s'exécute très rapidement, mais qui se conçoit lentement car il faut être assuré qu'il fonctionne parfaitement.

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

## Détails

- [préprocesseur](préprocesseur){.interne}
- [Édition de liens](édition-liens){.interne}
