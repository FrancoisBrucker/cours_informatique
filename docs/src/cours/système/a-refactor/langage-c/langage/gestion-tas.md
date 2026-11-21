---
layout: layout/post.njk

title: Gestion du tas

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

[gestion de la mémoire](https://www.youtube.com/watch?v=P0NWSHbNooA&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=26)

{% endlien %}

La pile c'est chouette mais son utilisation est impossible pour des données dont on ne connaît pas la taille à la compilation, de taille changeante ou encore trop grandes (la taille de la pile est limitée).

Il faut pouvoir utiliser le tas et gérer soit même ses données. Le `C` propose une gestion du tas dans la libc, sous la forme de 2 fonctions définies dans `stdlib.h`{.fichier} :

- `void *malloc(size_t size)`{.language-} : alloue `size` bytes contiguës en mémoire et rend un pointeur anonyme sur l'adresse du premier byte
- `void free(void *ptr)`{.language-} qui libère la mémoire commençant en `ptr`{.language-} (obtenu par un précédant `malloc`)

## Allocation de la mémoire

L'usage veut que l'on alloue uniquement la mémoire nécessaire pour stocker une donnée d'un type donné. On accède ensuite à cette donnée via un pointeur.

### Malloc

Par exemple allouer un tableau de 10000 entiers :

```c
#include <stdlib.h>

int main() {

  int *p = NULL;

  p = (int *)malloc(10000 * sizeof(int));

  return 0
}

```

Remarquez que :

- `malloc`{.language-} rend un pointeur générique, il faut donc faire un cast explicite vers le pointeur de retour
- la taille doit être déterminée par un `sizeof` pour que le code soit portable.

### Free

L'allocation de la mémoire n'est pas sensible aux blocs. La mémoire allouée l'est pour la durée du programme. Il faut donc désallouer la mémoire lorsque l'on en a plus besoin :

```c
#include <stdlib.h>

int main() {

  int *p = NULL;

  p = (int *)malloc(10000 * sizeof(int));

  // utilisation de p

  free(p);
  p = NULL;

  return 0
}

```

{% attention "**danger !**" %}
Une fois la mémoire libérée prenez l'habitude de toujours repositionner le pointeur à `NULL`{.language-}. Ceci évitera des bugs futurs où utilisera `p` en oubliant que la mémoire avait été désallouée.
{% endattention %}

### Gestion des erreurs

L'allocation peut échouer (s'il n'y a plus de place par exemple), il faut donc toujours vérifier que tout s'est bien passé avant de continuer :

```c
#include <stdlib.h>
#include <stdio.h>

int main() {

  int *p = NULL;

  p = (int *)malloc(10000 * sizeof(int));
  if (p == NULL) {
    perror("malloc failed!");
    exit(EXIT_FAILURE); // sortie du programme
  }

  // utilisation de p

  free(p);
  p = NULL;

  return EXIT_SUCCESS
}

```

### Fuite de mémoire

Toute mémoire allouée l'est pour la durée du programme, le code suivant a une [fuite de mémoire](https://fr.wikipedia.org/wiki/Fuite_de_m%C3%A9moire), il est impossible de désallouer la mémoire après l'exécution de la fonction `alloue()`{.language-}

```c
#include <stdlib.h>
#include <stdio.h>

void alloue() {
  int *p = (int *)malloc(10000 * sizeof(int));

  // utilisation de p 

  //oups... oublie de désallouer p.
}

int main() {

  alloue();

  // impossible de retrouver la mémoire allouée

  return EXIT_SUCCESS
}

```

{% attention "**danger !**" %}
La gestion de la mémoire est un travail ingrat et souvent compliqué. Mais il est nécessaire car un programme `C` doit pouvoir tourner indéfiniment sans gaspiller de la mémoire.
{% endattention %}

> TBD : memory leak detection : <https://github.com/google/sanitizers/wiki/AddressSanitizer> (<https://clang.llvm.org/docs/AddressSanitizer.html>) pour remplacer <https://valgrind.org/> qui ne marche pas sous ARM.

## Autres fonctions d'allocations

{% lien %}
[gestion mémoire en C](https://fr.wikipedia.org/wiki/Malloc)
{% endlien %}

- `void *calloc(size_t nmemb, size_t size)`{.language-} : alloue `size * nmemb`{.language-} bytes contiguës en mémoire (`nmemb`{.language-} éléments de taille `size`{.language-}) et initialise la mémoire avec des `0`
- `void *realloc(void *ptr, size_t size)`{.language-} : réalloue la place mémoire commençant au pointeur `ptr`{.language-} (obtenu par un `malloc`{.language-} ou `realloc`{.language-}) pour en changer sa taille en `size`{.language-}

## Principe d'allocation

{% lien %}
<https://www.youtube.com/watch?v=UTii4dyhR5c&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=27>
{% endlien %}

> TBD en dessous de malloc, il y a brk. <https://www.youtube.com/watch?v=XV5sRaSVtXQ>
>
> TBD on a vue dans la partie noyau que le tas n'est pas tout
> TBD On peut se passer de malloc si on veut mais il faut gérer les allocation/dé-allocation de la mémoire (reprendre la vidéo du dessus et le faire) avec [brk](https://man7.org/linux/man-pages/man2/brk.2.html) pour augmenter le tas. Mais il faut gérer à la main les allocation/dé allocations. 
> 
> TBD : en faire un exemple come dans la 2ne vidéo avec le brk qui bouge td avancé (après que les étudiants aient utilisé malloc) ?
