---
layout: page
title:  utiliser un terminal
tags: système terminal CLI
categories: CLI terminal
authors: 
    - François Brucker
---

> **prérequis :**
>
>* [le terminal]({% post_url /tutos/systeme/2021-08-24-terminal %})
>* [naviguer dans un système de fichiers]({% post_url /tutos/systeme/2021-08-24-fichiers-navigation %})
{: .chemin}

Comment utiliser un terminal pour taper des commandes.

<!--more-->

## prompt

Lorsque l'on ouvre un terminal, on se retrouve devant un [prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande). Ce prompt sera différent selon le terminal utilisé, mais il aura toujours la même fonction : on tape une **ligne de commande** et on appuie sur entrée pour l'exécuter. Cette ligne sera toujours :

* soit un fichier exécutable
* soit une commande shell (comme `ls` par exemple) : [liste des commandes powershell](https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/), [liste des commandes shell (bash)](https://manpages.ubuntu.com/manpages/bionic/man7/bash-builtins.7.html)

> Une ligne de commande est **toujours** soit un fichier exécutable soit une commande shell.
{: .note}

## dossier courant

De plus un terminal est **toujours** positionné dans un dossier précis de votre arborescence de fichiers. C'est le **dossier courant**. L'exécution d'une ligne de commande se fera **toujours** par rapport à cet endroit.

>Pour connaitre l'endroit où est positionné le terminal, on peut utiliser la commande shell `pwd`.
{: .note}

Lorsque l'on ouvre un terminal, son dossier courant est souvent le dossier principal de l'utilisateur. On peut également directement ouvrir un terminal dans un dossier spécifique :

{% details sous linux %}

Avec l'explorateur de fichier : *clique droit sur un dossier > ouvrir avec une autre application > terminal*
{% enddetails %}

{% details sous mac %}

Dans le finder : *clique droit sur un dossier> services > Nouveau terminal au dossier*

{% enddetails %}

{% details sous windows %}

Dans un explorateur de fichier cliquez sur le dossier, puis dans le menu fichier choisir ouvrir un terminal.

{% enddetails %}

## exécuter un fichiers

Le premier élément de la ligne de commande est un fichier qui doit être exécuté. Par exemple :

```shell
python mon_script.py
```

Comme `python` n'est pas une commande c'est **forcément** un fichier exécutable. Le système d'exploitation cherche alors un fichier s'appelant `python` (ou `python.exe` si on est sous windows) dans un ensemble de dossiers qu'on appelle le **path**.

### path

> Le **path** permet de trouver l'endroit où est le fichier à exécuter.
{: .note}

Connaître le path :

{% details sous linux/mac %}

Dans un terminal, tapez :

```shell
echo $PATH
```

Cela affichera les différents dossier dans le path.

{% enddetails %}

{% details sous windows %}

```shell
$env:Path
```

Vous pouvez aussi voir les différentes variables d'environnement (et les modifier). Voir par exemple [ce tuto](https://java.com/fr/download/help/path_fr.html).

{% enddetails %}

Si le fichier *"python"* (ou *"python.exe"* si on est sous windows) n'est pas trouvé, le terminal rend une erreur.

S'il est trouvé, il est exécuté.

> Souvent `.` (le répertoire courant) n'est pas dans le path. Il faut donc taper  `./truc` si on veut exécuter  le fichier s'appelant truc dans le dossier courant.

La partie suivant le fichier exécutable correspondent aux paramètre du programme. Pour savoir quelles sont les possibilités on regarde la documentation du fichier. Dans notre exemple c'est `mon_script.py` et la [documentation de la commande python](https://docs.python.org/3/using/cmdline.html) nous indique que cela correspond à un chemin relatif au dossier courant vers un fichier python à interpréter.

Pour que notre commande soit exécutée sans erreur il faut donc :

1. qu'un fichier exécutable nommé *"python"* (ou  *"python.exe"* sous windows) soit présent dansun des dossiers du path
2. qu'il existe un fichier nommé *"mon_script.py"* dans le dossier courant du terminal

### quelle commande ?

La commande exécutée d'une ligne de commande est un fichier présent dans le path. S'il existe plusieurs possibilités, c'est la 1ère rencontrée qui est utilisée. Il existe une commande shell pour déterminer le chemin absolu de la commande utilisée :

* [which](https://linux.die.net/man/1/which) sous unix/mac.
* [get-command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.2) sous powershell

Ainsi `which python` sous unix/mac et `get-command python` sous powershell vont donner le chemin absolu vers le python utilisé.

### modification permanante du path

On a parfois besoin de modifier de façon permanente le path. Les méthodes utilisées pour cela sont différentes sous unix/mac et windows.

> Ce ne sont pas des modifications courantes, on peut très bien essayer de s'en passer si la modification de fichiers de configuration fait un peu peur.

* [sous windows](https://codingbee.net/powershell/powershell-make-a-permanent-change-to-the-path-environment-variable). Voir aussi la [documentation sur les variables d'environnements](https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2)
* [sous unix/mac](https://opensource.com/article/17/6/set-path-linux)

## opérations sur le dossier courant

### où ?

La commande shell `pwd` donne le dossier courant du terminal.

### changer le dossier courant

Pour changer de dossier courant, on utiliser la commande shell `cd` suivi d'un chemin absolu ou relatif vers un autre dossier.

Par exemple, sur mon mac, je crée un nouveau terminal. Par défaut, son dossier courant est la maison. La commande `pwd` me rend en effet : `/Users/fbrucker`.

Si je veux aller dans le dossier contenant ma plus belle photo d'Ada Lovelace, je peux taper :

* un chemin absolu : `cd /Users/fbrucker/Desktop`
* un chemin relatif : `cd Desktop`, ou encore `cd ./Desktop`

> Notez que je ne peux pas aller dans un fichier.
> Si j'avais tapé `/Users/fbrucker/Desktop/ada_lovelace.png` j'aurais eu une erreur. Sur mon mac, ça dit : `cd: not a directory: /Users/fbrucker/Desktop/ada_lovelace.png`
{: .attention}

Sous unix, le caractère `~` est équivalent au chemin absolu vers la maison. En tapant `cd ~` je me retrouve alors directement à la maison. De là, `cd ~/Desktop` m'envoie dans le dossier `/Users/fbrucker/Desktop` quelque soit l'endroit où je me trouve.

> ~ est-il aussi vrai avec powershell ?
{: .tbd}

### fichier et dossiers du dossier courant

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

La commande `ls` a beaucoup de paramètres possible. Dans le monde du terminal, une commande va faire une unique chose mais de plein de façon disponible. C'est souvent ce qui fait peur, mais au final on utilisera jamais toutes les possibiliés. Par exemple la [documentation de la commande ls](http://manpagesfr.free.fr/man/man1/ls.1.html) nous permet :

* voir les fichiers cachés : `ls -a`
* voir tous les fichiers et récursivement : `ls -R`. Si je veux voir tous les fichiers depuis la racine, je peux taper : `s -R /` (attention ça va prendre du temps...)
* afficher toutes les informations : `ls -l`
* ...

On peut aussi combiner ces paramètres. Par exemple, si je veux voir tous les fichiers et dossiers (caché ou non) du dossier courant de façon longue, je peux taper : `ls -la` (je combine les options `l` et `a`)

> sous powershell ?
{: .tbd}

> Pour les commandes unix, retenez quelques formes utiles de la commande (pour `ls`, je ne retiens que `ls -la`) et pour le reste ayez la reflex de regarder la documentation
{: .note}

* [ls du powershell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.2) alias vers la commande `Get-ChildItem`
* [ls unix](http://manpagesfr.free.fr/man/man1/ls.1.html)

## création et suppression de fichiers/dossiers

### créer un dossier

Commande :

```shell
mkdir <chemin absolu ou relatif vers le dossier à créer>
```

Par exemple : `mkdir truc/chose`  crée le dossier chose dans le dossier truc lui même placé dans le dossier courant (si le dossier *"./truc"* n'existe pas, il y a une erreur)

Documentation :

* [mkdir du powershell](https://ss64.com/ps/new-item.html) qui est un alias vers la commande `new-item`
* [mkdir unix](https://linux.die.net/man/1/mkdir)

### supprimer un fichier/dossier

```shell
rm <chemin absolu ou relatif vers le fichier à supprimer>
rm -r <chemin absolu ou relatif vers le dossier à supprimer>
```

* [rm du powershell](https://ss64.com/ps/remove-item.html) alirs vers la commande `remove-item`
* [rm unix](https://linuxtect.com/linux-rm-command-tutorial/) La commande `rm` a beaucoup, beaucoup de paramètres possibles
