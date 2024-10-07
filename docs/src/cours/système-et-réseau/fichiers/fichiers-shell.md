---
layout: layout/post.njk

title: Fichiers avec Bash

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

On a déjà l'habitude d'utiliser les 3 file descriptor stdin, stdout et stderr.

Leurs numéros sont utilisés lorsqu'on écrit des choses comme cela :

```shell
$ cd /root/ 2>/dev/null
```

On redirige le file descriptor 2 (stderr) vers le fichier `/dev/null`{.fichier}.

## Créer ses file descriptors

{% lien %}
[file descriptor en Bash](https://www.youtube.com/watch?v=FuiLk7uH9Jw)
{% endlien %}

Bash permet d'ouvrir/créer des fichiers et de leurs associer des file descriptor très facilement.

On peut en créer d'autres avec `exec` (attention tout doit être collé), qui seront soit :

- associé à des fichiers déjà ouvert
- associé à un nouveau fichier

Par exemple le code suivant qui crée un nouveau file descriptor qui est associé au *fichier* de la sortie standard:

```shell
$ exec 42>&1
$ echo coucou >&42
coucou
ls -la /proc/$$/fd/42
lrwx------ 1 fbrucker fbrucker 64 oct.  13 09:20 /proc/704757/fd/42 -> /dev/pts/0

```

Ou créer un file descriptor associer à un nouveau fichier  :

```shell
$ exec 42>texte
$ echo coucou >&42
$ cat texte 
coucou
$ ls -la /proc/$$/fd/42
l-wx------ 1 fbrucker fbrucker 64 oct.  13 09:20 /proc/704757/fd/42 -> /home/fbrucker/texte

```

Supprimer un file descriptor se fait ensuite avec `exec 42>&-` :

```shell
$ exec 42>&-
$ ls -la /proc/$$/fd/42
ls: impossible d'accéder à '/proc/704757/fd/42': Aucun fichier ou dossier de ce type
```

## Buffers

{% attention %}

[N'oubliez pas le buffer](https://eklitzke.org/stdout-buffering)
{% endattention %}
