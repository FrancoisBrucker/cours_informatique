---
layout: layout/post.njk

title: Préprocesseur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://en.wikipedia.org/wiki/C_preprocessor>
<https://gcc.gnu.org/onlinedocs/cpp/Preprocessor-Output.html>
<http://jhnet.co.uk/articles/cpp_magic>


> TBD détailler les include, comment on fait etc.

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

Le but du préprocesseur est de préparer le code à être compilé. Le préprocesseur lit le fichier à préprocesser et cherche des :

- [directives](https://www.rocq.inria.fr/secret/Anne.Canteaut/COURS_C/chapitre5.html) à exécuter
- [macros](https://gcc.gnu.org/onlinedocs/cpp/Macro-Arguments.html#Macro-Arguments-1) à remplacer

Lorsque le préprocesseur
Attention, c'est juste du texte qui est remplacé. Il n'y a pas de logique interne.

```
clang -E hello.c -o hello.i
```

## Directives

Les directives sont des commandes commençant pas un `#`. Elles sont de trois types :

- `#include` : pour inclure un fichier
  - le nom de fichier peut être entre `<>` : pour les fichiers dépendant sdu système
  - le nom de fichier peut être entre `""` : pour les fichiers locaux à votre projet
- `#define` : pour créer
  - des macros
  - des constantes. Elles sont habituellement en majuscule pour les reconnaître
- les test `#ifdef`...`#endif` et `#ifndef`...`#endif`

Le fichier produit après préprocession est le fichier contenant les inclusions de fichiers et les macros et constantes remplacées.

### Remplacement des macros et constantes

Les macros et constantes définies par les directives sont remplacées par leur code.

Il faut faire très attention aux effets de bords avec les macros.

> TBD exemple

Bref, n'en faites pas vous même.

