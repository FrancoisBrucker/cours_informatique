---
layout: layout/post.njk

title: Appels systèmes fichiers

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[fichiers et appels systèmes](https://www.youtube.com/watch?v=ayMPFUGE_b4&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=20)
{% endlien %}

La création et gestion des fichiers est du ressort du noyau. Il faut donc faire un appel système à chaque manipulation.

La gestion effective des fichiers lorsque l'on code en **C** se fait souvent via d'autres fonctions (que nous verrons plus tard), plus pratiques à utiliser.

Les cinq principaux appels systèmes pour gérer un fichier sont :

- [open](https://man7.org/linux/man-pages/man2/open.2.html) : ouvre un fichier et rend un file descriptor
- [close](https://man7.org/linux/man-pages/man2/close.2.html) : ferme un fichier via son file descriptor
- [read](https://man7.org/linux/man-pages/man2/read.2.html) : lit du fichier
- [write](https://man7.org/linux/man-pages/man2/write.2.html) : écrit dans un fichier
- [lseek](https://man7.org/linux/man-pages/man2/lseek.2.html) : se positionne dans un fichier, si disponible

Il en existe d'autres, comme [dup](https://man7.org/linux/man-pages/man2/dup.2.html) dont le but est de dupliquer des file descriptors.

{% info %}
La section 2 de la commande `man` renseigne sur les appels systèmes. Faites l'essai pour les 5 fonctions ci-dessus
{% endinfo %}

> TBD : un buffer ?

## Gestion des fichiers

{% lien %}
[file descriptor en C](https://www.youtube.com/watch?v=tKvm_qOeRpU)
{% endlien %}

> TBD ici. faire les programmes et expliquer. Puis strace/ltrace après chacun.

Plusieurs programmes :

### Ouverture et/ou création

```c#
#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

extern int errno;

int main()
{
    int fd = open("mon-fichier.txt",
                  O_WRONLY|O_CREAT|O_TRUNC,
                  S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH | S_IWOTH);

    //printf("fd = %d\n", fd);

    if (fd == -1) {
        perror("Erreur");
    }

    close(fd);
    return 0;
}

```

une fois compilé, on peut exécuter le code. Il crée un fichier nommé `mon-fichier.txt` dans le dossier courant. En lisant la page `man 2 open` (la section 2 est pour les appels systèmes)


Écrire :

1. crée ou ouvre un fichier en écriture avec `open(path, O_WRONLY|O_CREAT|O_TRUNC, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH);`{.language-}
2. écrire dedans
3. le referme

Le lire :

4. le ré-ouvre en lecture et l'affiche : attention aux '\0'
5. le referme

Les erreurs :

6. change les droits et voit le programme planter
7. remet bien les droits


## Appels systèmes

{% lien %}

- [strace et ltrace](https://www.youtube.com/watch?v=2AmP7Pse4U0)
- [appels systèmes fichiers avec strace](https://www.youtube.com/watch?v=-gP58pozNuM)
- [playlist `strace`](https://www.youtube.com/watch?v=j_w-vQ3UriM&list=PLn6POgpklwWq1YUQsMHzddjoiwJzPiqcf)

{% endlien %}

{% faire %}
Faire un `strace` d'un fichier pour voir les appels systèmes
{% endfaire %}

## Autre

- [dup et dup2](https://www.delftstack.com/fr/howto/c/dup2-in-c/)

> TBD lseek et monter ce que ça donne sur un fichier ?
> adapter  [fseek](https://www.youtube.com/watch?v=EA2MVIgu7Q4)

## Buffers

{% attention %}

[N'oubliez pas le buffer](https://www.learntosolveit.com/cprogramming/chapter8/sec_8.2_getchar.html)
{% endattention %}
