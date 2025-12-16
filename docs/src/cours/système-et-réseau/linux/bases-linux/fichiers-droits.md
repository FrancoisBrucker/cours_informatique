---
layout: layout/post.njk

title: Droits et fichiers

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



> TBD permission  fichiers : <https://www.youtube.com/watch?v=q7kqrGC_sXE>
> TBD user/groups et numéros : voir le fichier /etc/passwd

{% lien %}
<https://www.cekome.com/blog/permissions-utilisateurs-linux/>
{% endlien %}

Dans le système Linux, (pratiquement) tout ce que l'on manipule est un fichier :

- les dossiers sont des fichiers
- les commandes dans le dossier `/usr/bin`{.fichier}
- les données de configuration dans les dossier `/etc`{.fichier}
- les données dans `/var/` ou dans notre dossier maison
- l'accès aux ressources comme le disque dur `/dev/sda` ou encore aux services `/proc/cpuinfo`

{% info %}
Que toutes les interactions avec le système soient effectuées sous la forme d'un fichier dérive du projet [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs) dont le modo était :*everything is a file*.
{% endinfo %}

## Types de fichiers

- fichier normal
- fichier caché
- dossier
- pseudo-fichier
- lien symbolique
- lien physique

## Propriété

La sécurité des accès est donc basée sur les droits d'accès aux fichiers. Chaque fichier possède :

- un propriétaire : un utilisateur du système
- un groupe : un ensemble d'utilisateurs

{% note %}
Les utilisateurs du système sont listés dans le fichier `/etc/passwd` (seuls les utilisateurs *réels* ont un dossier personnel dans `/home`) et les groupes dans le fichier `/etc/group`.
{% endnote %}
{% info %}

- [lister les utilisateurs](https://linuxize.com/post/how-to-list-users-in-linux/)
- [lister les groupes](https://linuxize.com/post/how-to-list-groups-in-linux/)

Attention, ce n'est pas pareil sous macos. Voir `man DirectoryService`
{% endinfo %}

Si l'on est l'actuel propriétaire du fichier on peut en modifier :

- son propriétaire `chown`
- son groupe `chgrp`

Chaque utilisateur et groupe est identifié par un numéro. Son UID. Seul `root` a un UID de 0, qui est spécial : aucune vérification de sécurité n'est faite pour lui.

## Droits

{% lien %}
<https://www.cekome.com/blog/permissions-utilisateurs-linux/>
{% endlien %}

L'accès à un fichier peut être de 3 sortes :

- lecture : pour lire son contenu
- écriture : pour modifier son contenu
- exécution : en faire une commande pour un fichier et accéder à son contenu pour les dossiers

Ces droits peuvent être différents pour :

- le propriétaire
- le groupe
- les autres

> TBD droit par défaut [umask](https://en.wikipedia.org/wiki/Umask)

### Voir les droits

```
ls -l
```

### Modifier les droits

```
chmod
```

- changer droits et group gou+
- chiffres

### Droits spéciaux

- [sticky bit](https://en.wikipedia.org/wiki/Sticky_bit) de `/tmp`
