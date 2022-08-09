---
layout: layout/post.njk 
title: Utiliser le terminal

tags: ['tutoriel', 'système', 'terminal']
---

{% chemin %}
[Tutoriels]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Terminal](../terminal)
* [naviguer dans un système de fichiers](../fichiers-navigation)

{% endprerequis %}

<!-- début résumé -->

Comment utiliser un terminal.

<!-- fin résumé -->

## Prompt

Lorsque l'on ouvre un terminal, on se retrouve devant un [prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande). Ce prompt sera différent selon le terminal utilisé, mais il aura toujours la même fonction : on tape une ***ligne de commande*** et on appuie sur entrée pour l'exécuter. Cette ligne sera toujours :

* soit un fichier exécutable
* soit une instructions compréhensible par le terminal, comme `ls` par exemple.

{% note %}
Une ligne de commande est **toujours** soit un fichier exécutable soit une instruction.
{% endnote %}

Les instructions sous différentes entre unix/mac (qu'on appelle ***shell***) et windows (appelé ***powershell***), mais il existe presque toujours un equivalent entre les instruction unix/mac et powershell ([liste des instructions powershell](https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/), [liste des instructions shell (bash)](https://manpages.ubuntu.com/manpages/bionic/man7/bash-builtins.7.html))

## Dossier courant

De plus un terminal est **toujours** positionné dans un dossier précis de votre arborescence de fichiers. C'est le **dossier courant**. L'exécution d'une ligne de commande se fera **toujours** par rapport à cet endroit.

{% note %}
Pour connaître l'endroit où est positionné le terminal, on peut utiliser la commande shell `pwd`.
{% endnote %}

Lorsque l'on ouvre un terminal, son dossier courant est souvent le dossier principal de l'utilisateur.

On peut également directement ouvrir un terminal dans un dossier spécifique :

{% details "sous linux" %}

Avec l'explorateur de fichier : *clique droit sur un dossier > ouvrir avec une autre application > terminal*
{% enddetails %}

{% details "sous mac" %}

Dans le finder : *clique droit sur un dossier> services > Nouveau terminal au dossier*

{% enddetails %}

{% details "sous windows" %}

Dans un explorateur de fichier cliquez sur le dossier, puis dans le menu fichier choisir ouvrir un terminal.

{% enddetails %}

## Exécuter un fichier

Le premier élément de la ligne de commande est un fichier qui doit être exécuté. Par exemple :

```shell
python mon_script.py
```

Comme le mot *python* n'est pas une instruction c'est **forcément** un fichier exécutable. Le système d'exploitation cherche alors un fichier s'appelant `python`{.fichier} (ou `python.exe`{.fichier} si on est sous windows) dans un ensemble de dossiers qu'on appelle le **path**.

### Path

{% note %}
> Le **path** permet de trouver l'endroit où est le fichier à exécuter.
{% endnote %}

Connaître le path :

{% details "sous linux/mac" %}

Dans un terminal, tapez :

```shell
echo $PATH
```

Cela affichera les différents dossier dans le path.

{% enddetails %}

{% details "sous windows" %}

```shell
$env:Path
```

Vous pouvez aussi voir les différentes variables d'environnement (et les modifier). Voir par exemple [ce tuto](https://java.com/fr/download/help/path_fr.html).

{% enddetails %}

Si le fichier `python`{.fichier} (ou `python.exe`{.fichier} si on est sous windows) n'est pas trouvé, le terminal rend une erreur.

S'il est trouvé, il est exécuté.

{% info %}
Souvent `.` (le répertoire courant) n'est pas dans le path. Il faut donc taper  `./truc` si on veut exécuter  le fichier s'appelant truc dans le dossier courant.
{% endinfo %}

### Paramètres

Tout Ce qui suit l'instruction ou le fichier exécutable dans une ligne de commande sont les ***paramètres***.

```shell
python mon_script.py
```

Dans la ligne de commande précédente on a :

* un fichier à exécuter : `python`{.fichier}
* ses paramètres : `mon_script.py` (que `mon_script.py`{.fichier} soit également un fichier n'a aucune importance ici)

{% info %}
Les paramètres peuvent être très simple (comme ci-dessous) comme très compliqué. Par exemple : `pandoc --mathjax --standalone --metadata pagetitle="titre page" --metadata charset="UTF-8"  page.md -o page.html` (tiré du [tutorial pandoc](../pandoc#pandoc-html))
{% endinfo %}

Pour savoir quelles sont les paramètres possible, il faut regarder la documentation du fichier exécutable. Dans notre exemple [documentation de la commande python](https://docs.python.org/3/using/cmdline.html) nous indique que le paramètre `mon_script.py` correspond à un chemin relatif au dossier courant vers un fichier python à interpréter.

{% note %}
Pour que notre commande `python mon_script.py` soit exécutée sans erreur il faut donc :

1. qu'un fichier exécutable nommé `python`{.fichier} (ou  `python.exe`{.fichier} sous windows) soit présent dans un des dossiers du path
2. qu'il existe un fichier nommé `mon_script.py` dans le dossier courant du terminal
{% endnote %}

### Quelle commande ?

La commande exécutée d'une ligne de commande est un fichier présent dans le path. S'il existe plusieurs possibilités, c'est la 1ère rencontrée qui est utilisée. Il existe une commande shell pour déterminer le chemin absolu de la commande utilisée :

* [`which`](https://linux.die.net/man/1/which) sous unix/mac.
* [`get-command`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.2) sous powershell

Ainsi `which python` sous unix/mac et `get-command python` sous powershell vont donner le chemin absolu vers le python utilisé.

### Modification permanente du path

On a parfois besoin de modifier de façon permanente le path. Les méthodes utilisées pour cela sont différentes sous unix/mac et windows.

{% attention %}
Ce ne sont pas des modifications courantes, on peut très bien essayer de s'en passer si la modification de fichiers de configuration fait un peu peur.
{% endattention %}

* [sous windows](https://codingbee.net/powershell/powershell-make-a-permanent-change-to-the-path-environment-variable). Voir aussi la [documentation sur les variables d'environnements](https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2)
* [sous unix/mac](https://opensource.com/article/17/6/set-path-linux)

## Opérations sur le dossier courant

### Où ?

La commande shell `pwd` donne le dossier courant du terminal.

### changer le dossier courant

Pour changer de dossier courant, on utiliser la commande shell `cd` suivi d'un chemin absolu ou relatif vers un autre dossier.

Par exemple, sur mon mac, je crée un nouveau terminal. Par défaut, son dossier courant est la maison. La commande `pwd` me rend en effet : `/Users/fbrucker`.

Si je veux aller dans le dossier contenant ma plus belle photo d'Ada Lovelace, je peux taper :

* un chemin absolu : `cd /Users/fbrucker/Desktop`
* un chemin relatif : `cd Desktop`, ou encore `cd ./Desktop`

{% attention %}
Notez que je ne peux pas aller dans un fichier.

Si j'avais tapé `/Users/fbrucker/Desktop/ada_lovelace.png` j'aurais eu une erreur. Sur mon mac, ça dit : `cd: not a directory: /Users/fbrucker/Desktop/ada_lovelace.png`
{% endattention %}

Sous unix, le caractère `~` est équivalent au chemin absolu vers la maison. En tapant `cd ~` je me retrouve alors directement à la maison. De là, `cd ~/Desktop` m'envoie dans le dossier `/Users/fbrucker/Desktop` quelque soit l'endroit où je me trouve.

### Fichier et dossiers du dossier courant

La commande `ls` donne les dossiers et les fichiers du dossier courant.

La commande `ls` est en fait plus générale car on peut l'utiliser avec un paramètre qui est un chemin absolu ou relatif où lister les fichiers/dossiers. Par exemple, sur mon mac, si je tape :

```shell
ls /
```

J'obtiens tous les dossier de la racine :

```shell
Applications Users        cores        home         sbin         var
Library      Volumes      dev          opt          tmp
System       bin          etc          private      usr
```

La commande `ls` a beaucoup de paramètres possible. Dans le monde du terminal, une commande va faire une unique chose mais de plein de façon disponible. C'est souvent ce qui fait peur, mais au final on utilisera jamais toutes les possibilités. Par exemple la [documentation de la commande ls](http://manpagesfr.free.fr/man/man1/ls.1.html) nous permet :

* afficher toutes les informations :
  * unix/mac : `ls -l`
  * powershell : `ls`. L'instruction `ls` sous powershell est équivalente à [`Get-ChildItem`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
* voir les fichiers cachés :
  * unix/mac : `ls -a`
  * powershell : `ls -Force`
* voir tous les fichiers et récursivement :
  * `ls -R`. Si je veux voir tous les fichiers depuis la racine, je peux taper : `s -R /` (attention ça va prendre du temps...)
  * `ls -Depth 3`. Sous powershell, il faut donner le nombre de récursion que 'on peut faire. Ici 3.
* ...

{% info %}

N'hésitez pas à aller voir la documentation :

* [ls du powershell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem) alias vers la commande `Get-ChildItem`
* [ls unix](http://manpagesfr.free.fr/man/man1/ls.1.html)

{% endinfo %}

## Création et suppression de fichiers/dossiers

### Créer un dossier

Commande :

```shell
mkdir <chemin absolu ou relatif vers le dossier à créer>
```

Par exemple : `mkdir truc/chose`  crée le dossier chose dans le dossier truc lui même placé dans le dossier courant (si le dossier *"./truc"* n'existe pas, il y a une erreur)

{% info %}
Documentation :

* [mkdir du powershell](https://ss64.com/ps/new-item.html) qui est un alias vers la commande `new-item`
* [mkdir unix](https://linux.die.net/man/1/mkdir)

{% endinfo %}

### Supprimer un fichier/dossier

```shell
rm <chemin absolu ou relatif vers le fichier à supprimer>
rm -r <chemin absolu ou relatif vers le dossier à supprimer>
```

{% info %}
Documentation :

* [rm du powershell](https://ss64.com/ps/remove-item.html) alors vers la commande `remove-item`
* [rm unix](https://linuxtect.com/linux-rm-command-tutorial/) La commande `rm` a beaucoup, beaucoup de paramètres possibles

{% endinfo %}
