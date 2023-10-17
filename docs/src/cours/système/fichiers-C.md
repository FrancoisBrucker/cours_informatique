---
layout: layout/post.njk

title: Fichiers en C

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [fopen vs open](https://www.youtube.com/watch?v=BQJBe4IbsvQ)
- [structure FILE](https://www.youtube.com/watch?v=bOF-SpEAYgk&list=PLhQjrBD2T381k8ul4WQ8SQ165XqY149WW&index=20)
- [fseek](https://www.youtube.com/watch?v=EA2MVIgu7Q4)

{% endlien %}

## stdin/out

> test avec un PID dun autre process et envoie du texte dans le stdin d'au autre process
> faire avec 1 fichier C et une commande, puis avec 2 fichiers C.

[stdin/out](https://stackoverflow.com/questions/15883568/reading-from-stdin)

## TBD

- [créer des fifo](https://www.geeksforgeeks.org/named-pipe-fifo-example-c-program/)

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

[strace fopen](https://www.youtube.com/watch?v=-gP58pozNuM)

- structure opaque, qui contient le File descriptor, les options d'ouverture, le buffer, etc.
- pour de vrais fichiers
- bufferisé pour la rapidité : attention au flush.

- tout pour fichier avec f devant :
  - fopen, fclose, fread, fwrite, fgetc, fputc,  (si plus loin que la fin quel caractère est ajouté ?)
- et deux fonctions formattées : fprintf et fscanf
