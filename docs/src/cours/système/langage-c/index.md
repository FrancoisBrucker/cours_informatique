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

```c
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

### Exécution

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

## Compilation

Avant de pouvoir exécuter un fichier `.c`, il faut procéder à plusieurs étapes pour le transformer en exécutable (le fichier `a.out`{.fichier})

{% aller %}
[La compilation](compilation){.interne}
{% endaller %}

## Éléments de langage

{% aller %}
[Langage C](langage){.interne}
{% endaller %}

## Gestion des sources

{% aller %}
[Gestion du code source](gestion-code-source){.interne}
{% endaller %}

## Gestion des erreurs

{% aller %}
[Gestion des erreurs](gestion-erreurs){.interne}
{% endaller %}

## Bibliothèques

{% aller %}
[Ajout de bibliothèques](ajout-bibliothèques){.interne}
{% endaller %}

## Exercices

Il existe de nombreux sites compilant des exercices (plus ou moins corrigés) en `C`, par exemple :

- <https://www.lamsade.dauphine.fr/~manouvri/C/PolyExoC_MM.pdf>
- <https://perso.univ-perp.fr/langlois/images/pdf/ens/touslestd.pdf>

Nous en ajoutons quelques-un ci-après.

{% aller %}
[Exercices](./exercices){.interne}
{% endaller %}

{% aller %}
[Projet : Algorithme X](./projet-algorithme-x){.interne}
{% endaller %}

{% aller %}
[Examen](./examen){.interne}
{% endaller %}

## C art

- [une histoire d'amour à sens unix](https://www.cise.ufl.edu/~manuel/obfuscate/westley.hint)
- [poème et ASCII art en C](https://www.welcometothejungle.com/fr/articles/btc-poem-code-avalanche-stars)
- [encore un poème en C](https://code-poetry.com/water)

## TBD

- [python et C](https://www.youtube.com/watch?v=l8dRF_AnFE0)
- Créer une lib en [static](https://dev.to/iamkhalil42/all-you-need-to-know-about-c-static-libraries-1o0b) avec ar
- [diff entre clone, fork, vfork](https://www.baeldung.com/linux/fork-vfork-exec-clone)
- fork/clone : avec strace : <https://www.youtube.com/watch?v=uRYyj8tcDTE&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=17>
- complet : [C et segments mémoires utilisées](https://gist.github.com/CMCDragonkai/10ab53654b2aa6ce55c11cfc5b2432a4)
- [timer](https://0xax.gitbooks.io/linux-insides/content/Timers/linux-timers-6.html)

## Bibliographie

- <https://learncodethehardway.org/c/>
- [effective C](https://www.amazon.fr/Effective-Introduction-Professional-Robert-Seacord/dp/1718501048/)
- [modern C](https://gustedt.gitlabpages.inria.fr/modern-c/)
- [cours OpenClassroom](https://openclassrooms.com/fr/courses/19980-apprenez-a-programmer-en-c)
- [C programming a modern approach](https://github.com/Embed-Threads/Learn-C/blob/main/books/c-programming-a-modern-approach-2nbsped-0393979504-9780393979503_compress.pdf)
- [playlist sur la mémoire](https://www.youtube.com/playlist?list=PL9IEJIKnBJjGAINguks7wyq7TAnHOZGRl)
