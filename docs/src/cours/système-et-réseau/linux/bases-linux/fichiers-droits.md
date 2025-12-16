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


{% lien %}
[breaking down how Linux file permissions work!](https://www.youtube.com/watch?v=q7kqrGC_sXE)
{% endlien %}

> TBD user/groups et numéros : voir le fichier /etc/passwd

{% lien %}
<https://www.cekome.com/blog/permissions-utilisateurs-linux/>
{% endlien %}

Dans le système Linux, (pratiquement) tout ce que l'on manipule est un fichier. Cela comporte bien sur :

- des fichiers classiques, une suite de 0 et de 1 stockées sur le disque dur, (comme les commandes dans le dossier `/usr/bin`{.fichier}, les données de configuration dans le dossier `/etc`{.fichier} ou encore les fichiers de données de notre dossier maison)
- les dossiers qui permettent de stocker d'autres dossiers ou des fichiers.
- les liens symboliques

Mais également d'autre types de fichiers, parfois appelé pseudo-fichiers permettant :

- d'interagir avec le système
- l'accès aux ressources comme le disque dur `/dev/sda` ou encore aux services `/proc/cpuinfo`
- les transmissions de données

Le terme fichier regroupe ainsi tout objet à laquelle on peut accéder pour lire et/ou écrire des information de façon séquentielle.

{% info %}
Que toutes les interactions avec le système soient effectuées sous la forme d'un fichier dérive du projet [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs) dont le modo était :*everything is a file*.
{% endinfo %}

L'accès à ces fichiers par un utilisateur est réglementé par des droits.

## Propriété

Chaque fichier possède deux propriétaires :

- un utilisateur du système
- un groupe du système

{% note %}
Les utilisateurs du système sont listés dans le fichier `/etc/passwd` (seuls les utilisateurs *réels* ont un dossier personnel dans `/home`) et les groupes dans le fichier `/etc/group`.
{% endnote %}
{% info %}

- [lister les utilisateurs](https://linuxize.com/post/how-to-list-users-in-linux/)
- [lister les groupes](https://linuxize.com/post/how-to-list-groups-in-linux/)

Attention, ce n'est pas pareil sous macos. Voir `man DirectoryService`
{% endinfo %}

Chaque utilisateur et groupe est identifié par un numéro. Son UID. Seul `root` a un UID de 0, qui est spécial : aucune vérification de sécurité n'est faite pour lui.

### Voir la propriété

On utilise l'option `-l` de [la commande `ls`](https://man7.org/linux/man-pages/man1/ls.1.html). Par exemple :

```shell
$ ls -l
total 72
drwxr-xr-x  2 fbrucker prof  6 16 déc.  10:12 bin
drwxr-xr-x  6 fbrucker prof  6 26 avril  2016 cours
drwx------  3 fbrucker prof  4  4 sept.  2017 Downloads
drwx--x--x 16 fbrucker prof 24  9 oct.   2024 html
drwxr-xr-x 11 fbrucker prof 12 14 déc.   2023 private
drwxr-xr-x  2 fbrucker prof  2 16 févr.  2011 Public
drwxr-xr-x  5 fbrucker prof  9  1 déc.  13:06 temp
```

Chaque ligne correspond à un fichier et les informations  correspondant aux propriétés sont :

- le troisième champ qui correspond au propriétaire,
- le quatrième champ qui correspond au groupe.

{% info %}
Sous Linux, il existe souvent un groupe du même nom que l'utilisateur qui est le groupe par défaut d'un fichier.
{% endinfo %}

### Modifier la propriété

Si l'on est l'actuel propriétaire du fichier on peut en modifier :

- son propriétaire avec [la commande `chown`](https://man7.org/linux/man-pages/man1/chown.1p.html)
- son groupe avec [la commande `chgrp`](https://man7.org/linux/man-pages/man1/chgrp.1.html)

## Droits

{% lien %}
<https://www.cekome.com/blog/permissions-utilisateurs-linux/>
{% endlien %}

L'accès à un fichier peut être de 3 sortes :

- lecture : pour lire son contenu
- écriture : pour modifier son contenu
- exécution : en faire une commande pour un fichier et accéder à son contenu pour les dossiers

Ces droits peuvent être différents pour :

- le propriétaire du fichier
- le groupe du fichier
- les autres

### Voir les droits

On utilise l'option `-l` de [la commande `ls`](https://man7.org/linux/man-pages/man1/ls.1.html). Par exemple :

<!-- TBD 

refaire avec un Ubuntu à la maison.

 -->

```shell
$ ls -l
total 72
drwxr-xr-x  2 fbrucker prof  6 16 déc.  10:12 bin
drwxr-xr-x  6 fbrucker prof  6 26 avril  2016 cours
drwx------  3 fbrucker prof  4  4 sept.  2017 Downloads
drwx--x--x 16 fbrucker prof 24  9 oct.   2024 html
drwxr-xr-x 11 fbrucker prof 12 14 déc.   2023 private
drwxr-xr-x  2 fbrucker prof  2 16 févr.  2011 Public
drwxr-xr-x  5 fbrucker prof  9  1 déc.  13:06 temp
```

Chaque ligne correspond à un fichier et les informations et le premier champ correspond aux droits. Il est composé de 10 caractères réparties en 4 parties :

- le premier caractère correspond au type de fichier
- les 2 à 4 ème caractères correspondent aux droits du propriétaire du fichier
- les 5 à 7 ème caractères correspondent aux droits des utilisateur faisant parti du groupe du fichier
- les 8 au 10 ème caractères correspondent aux droits des utilisateurs ne faisant pas parti des catégories précédentes

Les 3 caractères correspondant aux droits se comportent de la même manière :

- `r..` l'utilisateur concerné peut lire le contenu du fichier et `-..` il ne peut pas
- `.w.` l'utilisateur concerné peut écrire dans le fichier et `.-.` il ne peut pas
- `..x` l'utilisateur concerné peut exécuter le fichier et `..-` il ne peut pas

Si le fichier est de type dossier :

- lire un dossier signifie connaître les fichiers qu'il contient
- écrire dans un dossier signifie connaître ajouter/supprimer un fichier à son contenu
- exécuter un dosser signifie pouvoir aller dans le dossier

> TBD exemples

### Modifier les droits

```shell
chmod
```

- changer droits et group gou+
- chiffres

### Droits par défaut

> TBD droit par défaut [umask](https://en.wikipedia.org/wiki/Umask)

## Types de fichiers

<!-- TBD 

donner un exemple et voir son type avec ls -l
 -->

- fichier normal
- fichier caché : montrer le -a du ls
- dossier
- pseudo-fichier
- lien symbolique
- lien physique

## Droits spéciaux

- [sticky bit](https://en.wikipedia.org/wiki/Sticky_bit) de `/tmp`
- setuid
- setgid
