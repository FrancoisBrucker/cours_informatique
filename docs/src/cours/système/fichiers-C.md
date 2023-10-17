---
layout: layout/post.njk

title: Fichiers en C

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

S'il est tout à fait possible d'utiliser les appels systèmes fichiers en C pour gérer ses fichiers, la libc propose toute une batterie de fonctions qui permettent de les gérer plus facilement. Ces fonctions reprennent essentiellement les appels systèmes et ajoutent un `f` devant.

{% lien %}
[fopen vs open](https://www.youtube.com/watch?v=BQJBe4IbsvQ)
{% endlien %}

## Structure FILE

{% lien %}

[Utiliser FILE pour gérer ses fichiers](https://www.youtube.com/watch?v=bOF-SpEAYgk&list=PLhQjrBD2T381k8ul4WQ8SQ165XqY149WW&index=20)

{% endlien %}

## stdin/out

> test avec un PID dun autre process et envoie du texte dans le stdin d'au autre process
> faire avec 1 fichier C et une commande, puis avec 2 fichiers C.

[stdin/out](https://stackoverflow.com/questions/15883568/reading-from-stdin)

## TBD

- [Créer des fifo](https://www.geeksforgeeks.org/named-pipe-fifo-example-c-program/)

- fopen -> FILE * (type opaque ?)

```c
#include <stdio.h>
    ...
    while ((c = getchar()) != EOF)
      putchar(c);

    OR

    FILE *fp;
    int c;
    ...
    while ((c = getc(fp)) != EOF)
      putc(c, stdout);
```

- [popen : fifo](https://www.youtube.com/watch?v=8AXEHrQTf3I)

- [strace fopen](https://www.youtube.com/watch?v=-gP58pozNuM)

- structure opaque, qui contient le File descriptor, les options d'ouverture, le buffer, etc.
- pour de vrais fichiers
- bufferisé pour la rapidité : attention au flush.

- tout pour fichier avec f devant :
  - fopen, fclose, fread, fwrite, fgetc, fputc,  (si plus loin que la fin quel caractère est ajouté ?)
- et deux fonctions formatées : fprintf et fscanf
