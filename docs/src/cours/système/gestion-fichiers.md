---
layout: layout/post.njk

title: Gestion des fichiers

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

La gestion des fichiers avec Linux est très simple et est une abstraction utilisée pour la majoueure partie des communications faites.

## Système

File descriptor

- concept 
- voir les fichiers ouvert (fopen), qui a ouvert quoi
- communication : lecture, écriture dans buffer puis flush

- fichier caractère, ligne, etc.
- close (EOF) ferme le file descriptor.

<https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html#stdbuf-invocation>

fuser

## En shell

`>` et `<`

## En C

- open -> int
- fopen -> FILE * (type opaque ?)

lecture dans buffer
écriture dans buffer et flush.

<https://en.wikipedia.org/wiki/File_descriptor>

1. gestion des :
    1. fichiers
    2. entrées sorties read et write <https://stackoverflow.com/questions/15883568/reading-from-stdin>

## entrées sorties

Des fichiers comme les autres.
