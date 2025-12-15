---
layout: layout/post.njk

title: Hiérarchies des fichiers

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
<https://man.archlinux.org/man/file-hierarchy.7>
{% endlien %}

## Fichiers système

En utilisant la commande [tree](https://man.archlinux.org/man/tree.1.fr) (souvent installé par défaut), on visualise tous les dossiers d'une distribution Ubuntu présent à la racine (`/`{.fichier}) du système :

```shell
$ tree -d -L 1 /
/
├── bin -> usr/bin
├── boot
├── cdrom
├── dev
├── etc
├── home
├── lib -> usr/lib
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── snap
├── srv
├── sys
├── tmp
├── usr
└── var
```

Cette arborescence peut changer selon la distribution ou le type de Linux utilisé :

{% details "Sur une Debian de l'ecm" %}
```shell
fbrucker@roucas100:~$ tree -d -L 1 /
/
├── bin -> usr/bin
├── boot
├── dev
├── donnees
├── etc
├── home
├── lib -> usr/lib
├── lib32 -> usr/lib32
├── lib64 -> usr/lib64
├── libx32 -> usr/libx32
├── lost+found
├── media
├── mnt
├── net
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── srv
├── sys
├── tmp
├── users
├── usr
└── var

26 directories
```

{% enddetails %}
{% details "Sur un mac" %}

Les différents types de Linux, voir même différentes distributions vont avoir une architecture différentes. Cependant, les grands découpages restent identiques. Par exemple sur un mac :

```shell
❯ tree -d -L 1 /
/
├── Applications
├── bin
├── cores
├── dev
├── etc -> private/etc
├── home -> /System/Volumes/Data/home
├── Library
├── opt
├── private
├── sbin
├── System
├── tmp -> private/tmp
├── Users
├── usr
├── var -> private/var
└── Volumes

17 directories

```

{% enddetails %}

Mais vous retrouverez très souvent les même informations partout :

- `/`{.fichier} : racine de tout
- `/bin`{.fichier}  : programmes essentiels
- `/boot`{.fichier}  : contient les fichiers nécessaires pour démarrer la machine, en particulier le noyau
- `/dev`{.fichier} : les périphériques comme les sorties écrans, audio, ...
- `/etc`{.fichier}  : fichiers de configuration
- `/home`{.fichier} : répertoires utilisateurs
- `/lib`{.fichier}, `/lib32`{.fichier}, `/lib64`{.fichier} et `/libx32`{.fichier}: contiennent les bibliothèques partagées
- `/media`{.fichier}, `/mnt`{.fichier} ou `/mount`{.fichier}: supports amovibles
- `/opt`{.fichier} : programmes optionnels et dépendant de l'utilisation du machine
- `/proc`{.fichier} : processus du système
- `/root`{.fichier} : home de l'utilisateur root (administrateur)
- `/sbin`{.fichier} : programmes système
- `/tmp`{.fichier} : fichiers temporaires
- `/usr`{.fichier} : programmes utilisateur (_users_)
  - `/usr/bin`{.fichier} : programmes utiles aux utilisateurs
  - `/usr/sbin`{.fichier} : programmes utiles à root
- `/var`{.fichier} : fichiers variables (logs, cache…)

{% info %}
Les `->` signifient que ces dossiers sont [des liens symboliques](../../../bases-système/bases/fichiers-navigation/#liens){.interne} vers d'autres dossiers du système. On voit par exemple que sur un système Ubuntu (et tous les systèmes modernes) les executables et le bibliothèques partagées sont toutes placées dans le dossier `/usr`{.fichier}. Ne sont laissés à la racine que des liens permettant la compatibilité.
{% endinfo %}

Dans un système de type Unix, (pratiquement) tout est fichier :

- les dossiers sont des fichiers particuliers
- les commandes sont des fichiers exécutables
- les configurations sont des fichiers textes
- l’accès au matériel et au noyau se fait via des fichiers (ex `/proc`{.fichier}, `/dev`{.fichier}).

## Fichiers locaux

Ces fichiers vont contenir des choses différentes selon les utilisateurs et l'usage de la machine.

### Utilisateurs

La liste des utilisateurs est disponible dans le fichier `/etc/passwd`{.fichier}. Chaque ligne est consacrée à un utilisateur (On analysera ce fichier plus tard) et le premier champ (séparé par des `:`) contient son login. À chaque login d'utilisateur physique (ne nombreux utilisateurs ne sont que virtuels, comme l'utilisateur ` (les mots de passent n'y sont plus stocké. Ils sont maintenant dans le fichier `/etc/shadow`{.fichier})` par exemple dont le principal intérêt est de lancer le serveur ssh) possède un dossier où il peut ranger ses fichiers. C'est dans ce dossier, par défaut `/home/login`{fichier}, où seront par défaut placé tout nouveau terminal ouvert.
Il contiendra :

- ses fichiers
- ses fichiers de configuration à lui (souvent appelés [dotfiles](https://wiki.archlinux.org/title/Dotfiles))
- des programmes utiles à lui

### Opt

`/opt` remplace petit à petit `/usr/local` qui était le dossier par défaut où étaient placés tous les programmes optionnels et machine dépendant. Sous mac c'est par exemple dans ce dossier que s'installe <https://brew.sh/>

## Fichiers spéciaux

Plusieurs dossiers sont consacrés à ces pseudo-fichiers qui permettent d'interagir finement avec le système. Citons en deux `/proc`{.fichier} et `/dev`{.fichier}.

### `/proc`{.fichier}

Le dossier `/proc`{.fichier} va donner des informations sur tous les processus lancés par la machine ainsi que des informations sur le processeur. Par exemple [le fichier `/proc/uptime`{.fichier}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/s2-proc-uptime) contient par exemple le temps écoulé, en secondes, depuis son boot et le temps total de ses différents cœur passés à ne rien faire (s'il y a plus d'un cœur ce temps peut excéder le temps depuis le boot). Par exemple :

```shell
$ cat /proc/uptime
26179.16 522449.82
```

### `/dev`{.fichier}

Le dossier `/dev`{.fichier} va contenir des fichiers correspondant aux entrées/sorties. Comme :

- les sorties écran, audio
- les entrées disques, claviers

Il contient également des sorties plus spécifiques comme [le fichier `/dev/random/`{.file}](https://fr.wikipedia.org/wiki//dev/random) qui génère des nombres aléatoires. Par exemple la commande suivante (vous comprendrez la syntaxe plus tard), qui lit le contenu de `/dev/random/`{.file} et l'affiche à l'écran :

```shell
$ hexdump < /dev/random | head
0000000 fdab 87ca 5f18 d4ae 46db 697e 5ae9 3fd6
0000010 2845 2027 8d05 c60a 7a37 98c1 da04 5718
0000020 757b d8ec 1b69 d5f6 9875 2878 0608 778e
0000030 4af3 efcf 50aa 3d1f 859c 45f6 baa8 da77
0000040 42b8 4b75 533a 58f1 2c6d 4d9c b8f2 7526
0000050 1f58 84d8 9a3f db5b 39c4 280a e229 e38b
0000060 6803 bafe fa7e 69aa 2477 cd2d 4427 017c
0000070 df4c c55f f76d 1878 627a bf36 e2fe 3f6f
0000080 6e3f e684 3ead 7818 6272 2da7 daf2 ae65
0000090 ce95 f226 9b57 3994 6e39 8997 1b4e fec4
```
