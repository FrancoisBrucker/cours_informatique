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

Nous allons voir comment la gestion des fichiers est effectuée via des appels systèmes. La gestion effective des fichiers en **C** se fait souvent via d'autres fonctions (que nous verrons plus tard), plus pratiques à utiliser.

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

## Création d'un fichier

1. crée un fichier texte : param = flags
2. l'ouvre
3. le lit : attention aux '\0'
4. le referme
5. change les droits et voit le programme planter
6. remet bien les droits
7. strace du chose.

open(path, O_WRONLY|O_CREAT|O_TRUNC, mode);

On crée un fichier

> TBD faire un strace <https://www.youtube.com/watch?v=-gP58pozNuM>

## Autre

- [dup et dup2](https://www.delftstack.com/fr/howto/c/dup2-in-c/)

## Buffers

{% attention %}

[N'oubliez pas le buffer](https://www.learntosolveit.com/cprogramming/chapter8/sec_8.2_getchar.html)
{% endattention %}
