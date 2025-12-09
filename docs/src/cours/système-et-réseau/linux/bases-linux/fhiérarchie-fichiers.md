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

À quoi servent ces dossiers :

- `/`{.fichier} : racine de tout
- `/bin`{.fichier}  : programmes essentiels
- `/sbin`{.fichier} : programmes système
- `/etc`{.fichier}  : fichiers de configuration
- `/home`{.fichier} : répertoires utilisateurs
- `/root`{.fichier} : home de l'utilisateur root (administrateur)
- `/usr`{.fichier} : programmes utilisateur
  - `/usr/bin`{.fichier} : programmes utiles aux utilisateurs
  - `/usr/sbin`{.fichier} : programmes utiles à root
- `/tmp`{.fichier} : fichiers temporaires
- `/var`{.fichier} : fichiers variables (logs, cache…)
- `/dev`{.fichier} : périphériques
- `/proc`{.fichier} : processus du système
- `/media`{.fichier}, `/mnt`{.fichier} : supports amovibles
- `/lib`{.fichier} : bibliothèques partagées

Dans un système de type Unix, (pratiquement) tout est fichier :

- les dossiers sont des fichiers particuliers
- les commandes sont des fichiers exécutables
- les configurations sont des fichiers textes
- l’accès au matériel et au noyau se fait via des fichiers (ex `/proc`{.fichier}, `/dev`{.fichier}).

## Fichiers utilisateurs

- maison :
  - ses fichiers
  - les fichiers de configuration de ses applications les dotfiles
  - des programmes utiles à lui
- root `/root` et `etc/shadow`
- `/opt` remplace petit à petit `/usr/local`. op test un fourre tout avec un dossier par app. usr/local est hiérarchisé /bin. lib, etc. C'est un système local

Sur un Linux :

## Fichiers spéciaux

{% lien %}
<https://mtodorovic.developpez.com/linux/programmation-avancee/?page=page_7>
{% endlien %}


> TBD `/proc`{.fichier}, `/dev`{.fichier}

[Le fichier `/proc/uptime`{.fichier}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/s2-proc-uptime) contient par exemple le temps écoulé, en secondes, depuis son boot et le temps total de ses différents cœur passés à ne rien faire (s'il y a plus d'un cœur ce temps peut excéder le temps depuis le boot) :

```shell
fbrucker@roucas100:/proc$ cat /proc/uptime
26179.16 522449.82
```
