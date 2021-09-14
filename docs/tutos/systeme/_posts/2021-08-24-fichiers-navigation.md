---
layout: page
title:  naviguer dans un système de fichiers
tags: système fichiers terminal
category: fichiers
authors: 
    - François Brucker
---

Qu'est-ce qu'un fichier ? Un dossier ? Comment naviguer dans un système de fichier avec le terminal ou l'explorateur de fichier.

<!--more-->

## système de fichier

Votre ordinateur est composé de fichiers et de dossiers (aussi appelé répertoire) :

* un **dossier** est un conteneur qui peut contenir soit d'autres dossier, soit des fichiers
* un **fichier** est ce que vous pouvez utiliser. C'est une image, du texte, ou encore un programme.

Il existe un dossier spécial, appelé *racine* qui est le départ : on peut atteindre tous les fichiers/dossiers de votre ordinateur à partir de celui-ci.

Cette organisation est appelée [arborescence de fichiers](https://fr.wikipedia.org/wiki/R%C3%A9pertoire_(informatique)).

### exploration de l'arborescence

Ouvre une fenêtre de l'explorateur de fichier et placez vous à la racine de votre système de fichier.

{% details sous linux %}

> TBD
{: .note}

{% enddetails %}

{% details sous mac %}
Ouvrez une nouvelle fenêtre du *Finder* et choisissez [le mode d'affichage des fichiers](https://support.apple.com/fr-fr/HT201732)) en colonne. Ensuite, choisissez dans le menu : *aller > ordinateur* et cliquez sur *"Macintosh HD"*, qui est la racine de votre système de fichier.
{% enddetails %}

{% details sous windows %}

on voit le chemin sur la barre du chemin (si c'est pas un dossier spécial)

> TBD
{: .note}

{% enddetails %}

Vous pourrez ensuite naviguer de dossiers en dossiers, jusqu'à arriver à un fichier d'où vous ne pourrez plus avancer.

Dans l'exemple ci-après, j'ai navigué sur mon mac jusqu'à ma photo d'[Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) :

![chemin vers le fichier ada_lovelace]({{ "/assets/tutos/fichiers-navigation/chemin-vers-ada.png" | relative_url }}){:style="margin: auto;display: block;"}

On voit bien le chemin parcouru de la racine (appelé *"Macintosh HD"* sur un mac et le fichier).

> Le nom des dossiers sur le disque dur et celui qui apparait dans l'explorateur de fichier peuvent être différent selon la langue du système d'exploitation.
> Ainsi, le nom *Bureau* dans l'explorateur correspondra au dossier `Desktop` sur le disque dur...
{: .attention}

### chemin

Le chemin vers un fichier depuis la racine s'écrit en séparant tous les dossiers parcourus par un `/`. Dans l'image de la navigation vers Ada Lovelace, son chemin est :

```shell
/Users/fbrucker/Desktop/ada_lovelace.png 
```

Tout fichier ou dossier de l'arborescence de fichier possède un chemin unique depuis la racine, c'est donc un moyen de l'identifier.

> Le chemin du dossier racine est `/`.

Un chemin qui commence par `/` est dit **chemin absolu**, puisqu'il part de la racine. On a aussi souvent coutume de parler de **chemin relatif** lorsqu'il part d'un dossier particulier. Dans l'exemple précédent, en partant du dossier `/Users/fbrucker`, le chemin relatif vers l'image d'Ada est : `Desktop/ada_lovelace.png`.

> Un chemin absolu commence toujours par `/`. Un chemin qui ne commence pas par `/` est **toujours** un chemin relatif.

### plusieurs racines

On considère parfois que chaque disque dur, chaque clé usb constitue sa propre racine. Il y a alors une *racine des racines*, qui contient le départ  vers les racines particulières des différents périphériques de stockages de l'ordinateur.
disques durs, clés, etc.

> C'est en réalité une vue de l'esprit. Il n'existe qu'une seule racine et chaque disque dur est [monté](https://fr.wikipedia.org/wiki/Point_de_montage).

Souvent sous windows ces racines sont explicites, c'est `c:` par exemple pour le disque dur principal.

### dossiers spéciaux

Pour qu'un ordinateur fonctionne, il a besoin d'avoir des dossiers spéciaux contenant le système d'exploitation, ainsi que des fichiers spéciaux contenant des programmes (ces fichiers sont dit exécutables).

Il existe aussi des dossiers pour chaque utilisateurs de l'ordinateur où il peut ranger ses fichiers et où le système stock les préférences de l'utilisateur.

### dossiers . et .. {#block-.-..}

Les dossiers `.` et `..` sont des dossiers spéciaux qui signifient :

* le dossiers courant pour `.`
* le dossiers précédent du dossiers `.` pour `..`.

De là les 4 chemins suivants sont identiques :

* `/Users/fbrucker/Desktop/ada_lovelace.png`
* `/Users/fbrucker/./Desktop/./ada_lovelace.png`
* `/Users/fbrucker/../fbrucker/Desktop/ada_lovelace.png`
* `/Users/fbrucker/../fbrucker/./Desktop/ada_lovelace.png`
  
> On fait souvent commencer un chemin relatif par `.` pour bien montrer sa différence par rapport à un chemin absolu qui commence par `/`.

#### maison

La *maison* est le dossier principal d'un utilisateur.

> Pour les utilisateurs de windows : il est recommandé que ce dossier ne comporte ni espace ni accent.

## fichiers

### extension de fichier

Un nom de fichier comporte souvent un texte, suivi d'un `.` puis de deux ou trois lettres qui forme une [*extension*](https://fr.wikipedia.org/wiki/Extension_de_nom_de_fichier).

Cette extension ne sert à rien pour l'ordinateur, c'est seulement une aide pour l'utilisateur et certaines applications. Cela permet à priori de catégoriser un fichier.

Ainsi, même si l'extension d'un fichier texte est *".txt"*, rien ne vous empêche de la changer en *".exe"* par exemple. Cela ne change en rien la nature du fichier. Cela cependant apporte de la confusion car certaines applications vont penser que c'est un fichier exécutable et cela va planter quand elles vont tenter de le faire.

> Dans un éditeur de texte, l'extension d'un fichier permet de charger une coloration syntaxique par défaut : *".py"* pour les fichiers python par exemple, *".md"* pour les fichier markdown.
>
> Ne soyez pas créatifs dans les extensions de fichiers, utilisez celle par défaut selon le type de fichier que vous utilisez.

### fichiers exécutables

Les fichiers exécutables sont le cœur d'un système d'exploitation : ce sont les programmes.

Leur format dépend du système d'exploitation, il est donc impossible d'utiliser un exécutable windows pour l'utiliser sous mac par exemple.

> Un fichier python n'est **pas** un fichier exécutable. C'est un fichier texte qui est est lu, on dit **interprété** par l'interpréteur python qui lui est un fichier exécutable.

## dossiers et fichiers cachés

Ce sont souvent des fichiers (ou des dossiers) de préférences, donc pas utile de les voir tout le temps. Dans le monde unix commencent par un `.` dans le monde windows commencent par un `_` et ils sont invisible lorsque l'on regarde ces fichiers avec un explorateur de fichier.

On peut cependant les afficher dans un explorateur de fichier en effectuant quelques manipulation :

{% details sous linux %}

> TBD
{: .note}

{% enddetails %}

{% details sous mac %}

[sous mac](https://www.ionos.fr/digitalguide/serveur/configuration/mac-afficher-les-fichiers-et-dossiers-caches/).

> Pour que la manipulation de touche décrite dans la page fonctionne, il faut également d'appuyer sur la touche `fn` en plus.

Si vous voulez aller dans un dossier particulier, vous pouvez utiliser : *menu Aller > Aller au dossier...*

{% enddetails %}

{% details sous windows %}

[afficher les dossiers cachés sous windows](https://support.microsoft.com/fr-fr/windows/voir-les-fichiers-et-les-dossiers-cach%C3%A9s-dans-windows-97fbc472-c603-9d90-91d0-1166d1d9f4b5)

{% enddetails %}

## terminal

Le [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %}) est l'outil permettant d'exécuter des programmes. Il permet de contrôler directement ce qui est exécuté, et est l'endroit où l'on lancera nos scripts python par exemple.

Une ligne du terminal sera toujours :

* soit un fichier exécutable
* soit une commande (comme `get-command` pour un powershell par exemple)

Etudions par exemple la commande :

```shell
python mon_script.py
```

Comme `python` n'est pas une commande c'est **forcément** un fichier exécutable.  Le système d'exploitation cherche alors un fichier s'appelant `python` (ou `python.exe` si on est sous windows) dans un ensemble de dossiers qu'on appelle le **path**.

Connaître le path :

{% details sous linux/mac %}

Dans un terminal, tapez :

```shell
echo $PATH
```

Cela affichera les différents dossier dans le path.

{% enddetails %}

{% details sous windows %}

[affichier et modifier le path](https://java.com/fr/download/help/path_fr.html)

{% enddetails %}

Si le fichier *"python"* (ou *"python.exe"* si on est sous windows) n'est pas trouvé, le terminal rend une erreur.

S'il est trouvé, il est exécuté.

> Souvent `.` (le répertoire courant) n'est pas dans le path. Il faut donc taper  `./truc` si on veut exécuter  le fichier s'appelant truc dans le dossier courant.

La partie suivant le fichier exécutable correspondent aux paramètre du programme. Pour savoir quelles sont les possibilités on regarde la [documentation](https://docs.python.org/3/using/cmdline.html) : un nom de fichier en paramètre signifie que l'on souhaite interpréter le fichier décrit par son chemin relatif.

Ici : cela signifie qu'il existe un fichier *"mon_script.py"* dans le répertoire courant du terminal.

### dossier courant d'un terminal

Lorsque l'on lance un terminal il est **toujours** dans un dossier du système. POur le connaitre, on peut taper la commande :

```shell
pwd
```

#### se déplacer avec cd

Pour changer de dossier, on utiliser la commande `cd` suivi d'un chemin absolu ou relatif.

Par exemple, sur mon mac, je crée un nouveau terminal. Par défaut, son dossier courant est la maison. La commande `pwd` me rend en effet : `/Users/fbrucker`.

Si je veux aller dans le dossier contenant ma photo d'Ada, je peux taper :

* un chemin absolu : `cd /Users/fbrucker/Desktop`
* un chemin relatif : `cd Desktop`, ou encore `cd ./Desktop` qui est équivalent.

> Notez que je ne peux pas aller dans un fichier.
> Si j'avais tapé `/Users/fbrucker/Desktop/ada_lovelace.png` j'aurais eu une erreur. Sur mon mac, ça dit : `cd: not a directory: /Users/fbrucker/Desktop/ada_lovelace.png`
{: .attention}

Sous unix, le caractère `~` est équivalent au chemin absolu vers la maison. En tapant `cd ~` je me retrouve alors directement à la maison. De là, `cd ~/Desktop` m'envoie dans le dossier `/Users/fbrucker/Desktop` quelque soit l'endroit où je me trouve.

> TBD : est-ce aussi vrai avec powershell ?
{: .note}

#### lister avec ls

La commande `ls` quand à elle donne les dossier et les fichier du dossier courant (on peut l'utiliser sans paramètre, ou avec un chemin absolu ou relatif).

Par exemple, sur mon mac, si je tape :

```shell
ls /
```

J'obtiens tous les dossier de la racine :

```shell
Applications Users        cores        home         sbin         var
Library      Volumes      dev          opt          tmp
System       bin          etc          private      usr
```

### ouvrir un terminal dans un dossier spécifique

{% details sous linux %}

> TBD
{: .note}

{% enddetails %}

{% details sous mac %}

Dans le finder cliquez droit sur le dossier, puis *services > Nouveau terminal au dossier*

{% enddetails %}

{% details sous windows %}

Dans un explorateur de fichier cliquez sur le dossier, puis dans le menu fichier

{% enddetails %}

### copier le chemin absolu

{% details sous linux %}

> TBD
{: .note}

{% enddetails %}

{% details sous mac %}

Dans le finder cliquez droit sur le dossier, puis copier. Coller ensuite dans le finder.

{% enddetails %}

{% details sous windows %}

Dans explorateur de fichier cliquez sur le dossier, puis *copier le chemin d'accès* dans le menu *accueil*

{% enddetails %}

## pour aller plus loin

> TBD :
>
> * liens
> * permissions
> * unix et tout est fichier
> * fichiers spéciaux (comme `/dev/audio` par exemple)
> * une application mac est un dossier.
> * comment écrire sur le disque dur, le [file system](https://en.wikipedia.org/wiki/Comparison_of_file_systems)
