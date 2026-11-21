---
layout: layout/post.njk

title: Appels systèmes fichiers

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD commencer par un [strace fopen](https://www.youtube.com/watch?v=-gP58pozNuM) et voir que c'est open qui est utilisé.

{% lien %}
[fopen vs open](https://www.youtube.com/watch?v=BQJBe4IbsvQ)
{% endlien %}

> TBD faire un fopen et voir avec un strace que c'est bien open qui est utilisé.


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

une fois compilé, on peut exécuter le code. Il crée un fichier nommé `mon-fichier.txt` dans le dossier courant. En lisant la page `man 2 open` (la section 2 est pour les appels systèmes) on voit que l'on :

- crée ou ouvre un fichier en écriture
- on lui donne des droits.

{% faire %}

1. modifiez le contenu de `mon-fichier.txt`{.fichier} dans un éditeur puis re-exécutez le code. Le fichier devrait à nouveau être vide
2. changez le code pour que les autres n'aient pas le droit de lire le fichier créé

{% endfaire %}

En utilisant `ltrace` pour voir les appels aux bibliothèques :

```shell
$ ltrace ./a.out
__libc_start_main(0xaaaacf2e0854, 1, 0xffffc805d068, 0 <unfinished ...>
open("mon-fichier.txt", 577, 0646)               = 3
printf("fd = %d\n", 3fd = 3
)                           = 7
close(3)                                         = 0
__cxa_finalize(0xaaaacf2f1048, 0xaaaacf2e0800, 0x10dd0, 1) = 1
+++ exited (status 0) +++

```

On voit qu'il y en à 3 : `open`, `printf` et `close`. Ils correspondent à des appels à la libc. Pour utiliser des fichiers, le  process doit demander au noyau de le faire via des appels systèmes. On peut les voir avec la commande `strace`.

{% lien %}

[strace ouverture de fichiers](https://www.youtube.com/watch?v=mBfurelWwPQ)

{% endlien %}

{% lien %}

- [strace et ltrace](https://www.youtube.com/watch?v=2AmP7Pse4U0)
- [appels systèmes fichiers avec strace](https://www.youtube.com/watch?v=-gP58pozNuM)
- [playlist `strace`](https://www.youtube.com/watch?v=j_w-vQ3UriM&list=PLn6POgpklwWq1YUQsMHzddjoiwJzPiqcf)

{% endlien %}


```shell
$ strace ./a.out
execve("./a.out", ["./a.out"], 0xfffffb9635d0 /* 46 vars */) = 0
brk(NULL)                               = 0xaaab1d30f000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff94947000
faccessat(AT_FDCWD, "/etc/ld.so.preload", R_OK) = -1 ENOENT (Aucun fichier ou dossier de ce type)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=72775, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 72775, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffff94900000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\340u\2\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=1641496, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 1810024, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff94746000
mmap(0xffff94750000, 1744488, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0) = 0xffff94750000
munmap(0xffff94746000, 40960)           = 0
munmap(0xffff948fa000, 24168)           = 0
mprotect(0xffff948d9000, 61440, PROT_NONE) = 0
mmap(0xffff948e8000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x188000) = 0xffff948e8000
mmap(0xffff948ee000, 48744, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffff948ee000
close(3)                                = 0
set_tid_address(0xffff94947f30)         = 1858948
set_robust_list(0xffff94947f40, 24)     = 0
rseq(0xffff94948600, 0x20, 0, 0xd428bc00) = 0
mprotect(0xffff948e8000, 16384, PROT_READ) = 0
mprotect(0xaaaae5610000, 4096, PROT_READ) = 0
mprotect(0xffff9494c000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0xffff94900000, 72775)           = 0
openat(AT_FDCWD, "mon-fichier.txt", O_WRONLY|O_CREAT|O_TRUNC, 0646) = 3
close(3)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++

```

Tout le début des appels systèmes est là pour mettre en mémoire le programme, charger la bibliothèque partagée `libc` et faire les différents liens pour permettre son exécution.

Les 3 derniers appels sont en revanche issus de notre code :

1. le dernier `exit_group(0)`{.language-} est le code de sortie (ligne 23 du code)
2. l'avant dernier `close(3)`{.language-} correspond à la fermeture de notre fichier (ligne 23 du code)
3. l'avant avant dernier `openat(AT_FDCWD, "mon-fichier.txt", O_WRONLY|O_CREAT|O_TRUNC, 0646) = 3
`{.language-} correspond à l'ouverture du fichier (ligne 12 du code)

On voit que le compilateur a utilisé :

- l'appel système `openat`
- il a donné un numéro octal (il commence par 0) pour les permissions.

Et que le file descriptor de notre fichier ouvert est 3.

{% exercice %}
Dé-commentez la ligne 16 du code et trouvez l'appel système correspondant.
{% endexercice %}
{%details "solution" %}
C'est un write dans stdout (de file descriptor 1).
{% enddetails %}

## Autre

- [dup et dup2](https://www.delftstack.com/fr/howto/c/dup2-in-c/)
- [Créer des fifo](https://www.geeksforgeeks.org/named-pipe-fifo-example-c-program/)
- [popen : fifo](https://www.youtube.com/watch?v=8AXEHrQTf3I)

> TBD lseek et monter ce que ça donne sur un fichier ?
> adapter  [fseek](https://www.youtube.com/watch?v=EA2MVIgu7Q4)

## Buffers

{% attention %}
[N'oubliez pas le buffer](https://www.learntosolveit.com/cprogramming/chapter8/sec_8.2_getchar.html)
{% endattention %}
