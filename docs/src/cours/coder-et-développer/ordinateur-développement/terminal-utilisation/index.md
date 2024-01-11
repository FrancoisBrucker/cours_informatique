---
layout: layout/post.njk 

title: Utiliser le terminal
authors:
    - François Brucker

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Comment utiliser un terminal.

<!-- fin résumé -->

## Prompt

Lorsque l'on ouvre un terminal, on se retrouve devant [un prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande). Ce prompt sera différent selon le terminal utilisé, mais il aura toujours la même fonction : on tape une ***ligne de commande*** et on appuie sur entrée pour l'exécuter. Cette ligne sera toujours :

* soit un fichier exécutable
* soit une instructions compréhensible par le terminal, comme `ls`{.language-} par exemple.

{% note %}
Une ligne de commande est **toujours** soit un fichier exécutable soit une instruction.
{% endnote %}

Les instructions sous différentes entre les systèmes Unix (Linux et Mac) qu'on appelle ***shell*** et le système Windows appelé ***powershell***, mais il existe presque toujours un equivalent entre les instruction unix/mac et powershell :

* [liste des instructions powershell](https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/)
* [liste des instructions shell (bash)](https://manpages.ubuntu.com/manpages/bionic/man7/bash-builtins.7.html)

## Dossier courant

De plus un terminal est **toujours** positionné dans un dossier précis de votre arborescence de fichiers. C'est le **dossier courant**. L'exécution d'une ligne de commande se fera **toujours** par rapport à cet endroit.

{% note %}
Pour connaître l'endroit où est positionné le terminal, on peut utiliser la commande shell `pwd`{.language-}.
{% endnote %}

Lorsque l'on ouvre un terminal, son dossier courant est souvent le dossier principal de l'utilisateur. Mais on a aussi vu que l'on pouvait aussi directement ouvrir un terminal [dans un dossier spécifique](../terminal/#explorateur){.interne}.

## Exécuter une commande

Le premier élément de la ligne de commande est un fichier qui doit être exécuté. Par exemple :

```
python mon_script.py
```

Comme le mot *python* n'est pas une instruction c'est **forcément** un fichier exécutable. Le système d'exploitation cherche alors un fichier s'appelant `python`{.fichier} (ou `python.exe`{.fichier} si on est sous windows) dans un ensemble de dossiers qu'on appelle le [path](./#path).

Si le fichier `python`{.fichier} (ou `python.exe`{.fichier} si on est sous windows) n'est pas trouvé, le terminal rend une erreur.

S'il est trouvé, il est exécuté.

{% info %}
Souvent `.`{.fichier} (le répertoire courant) n'est pas dans le path. Il faut donc taper  `./truc`{.fichier} si on veut exécuter  le fichier s'appelant truc dans le dossier courant.
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
Les paramètres peuvent être très simple (comme ci-dessous) comme très compliqué. Par exemple : `pandoc --mathjax --standalone --metadata pagetitle="titre page" --metadata charset="UTF-8"  page.md -o page.html`{.language-} (tiré du [tutorial pandoc](/tutoriels/pandoc#pandoc-html){.interne})
{% endinfo %}

Pour savoir quelles sont les paramètres possible, il faut regarder la documentation du fichier exécutable. Dans notre exemple [documentation de la commande python](https://docs.python.org/3/using/cmdline.html) nous indique que le paramètre `mon_script.py`{.fichier} correspond à un chemin relatif au dossier courant vers un fichier python à interpréter.

{% note %}
Pour que notre commande `python mon_script.py`{.language-} soit exécutée sans erreur il faut donc :

1. qu'un fichier exécutable nommé `python`{.fichier} (ou  `python.exe`{.fichier} sous windows) soit présent dans un des dossiers du path
2. qu'il existe un fichier nommé `mon_script.py`{.fichier} dans le dossier courant du terminal
{% endnote %}

### <span id="which"></span> Quelle commande ?

La commande exécutée d'une ligne de commande est un fichier présent dans le path. S'il existe plusieurs possibilités, c'est la 1ère rencontrée qui est utilisée. Il existe une commande shell pour déterminer le chemin absolu de la commande utilisée :

* [`which`{.language-}](https://linux.die.net/man/1/which) sous unix/mac.
* [`get-command`{.language-}](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.2) sous powershell

Ainsi `which python`{.language-} sous unix/mac et `get-command python`{.language-} sous powershell vont donner le chemin absolu vers le python utilisé.

## Opérations sur les dossiers/fichiers

### Opérations sur le dossier courant

#### Où ?

La commande shell `pwd`{.language-} donne le dossier courant du terminal.

#### Changer le dossier courant

Pour changer de dossier courant, on utiliser la commande shell `cd`{.language-} suivi d'un chemin absolu ou relatif vers un autre dossier.

Par exemple, sur mon mac, je crée un nouveau terminal. Par défaut, son dossier courant est la maison. La commande `pwd`{.language-} me rend en effet : `/Users/fbrucker`{.fichier}.

Si je veux aller dans le dossier contenant ma plus belle photo d'Ada Lovelace, je peux taper :

* un chemin absolu : `cd /Users/fbrucker/Desktop`{.language-}
* un chemin relatif : `cd Desktop`{.language-}, ou encore `cd ./Desktop`{.language-}

{% attention %}
Notez que je ne peux pas aller dans un fichier.

Si j'avais tapé `/Users/fbrucker/Desktop/ada_lovelace.png`{.language-} j'aurais eu une erreur. Sur mon mac, ça dit : `cd: not a directory: /Users/fbrucker/Desktop/ada_lovelace.png`
{% endattention %}

Sous unix, le caractère `~` est équivalent au chemin absolu vers la maison. En tapant `cd ~`{.language-} je me retrouve alors directement à la maison. De là, `cd ~/Desktop`{.language-} m'envoie dans le dossier `/Users/fbrucker/Desktop`{.fichier} quelque soit l'endroit où je me trouve.

#### Fichier et dossiers du dossier courant

La commande `ls`{.language-} donne les dossiers et les fichiers du dossier courant.

La commande `ls`{.language-} est en fait plus générale car on peut l'utiliser avec un paramètre qui est un chemin absolu ou relatif où lister les fichiers/dossiers. Par exemple, sur mon mac, si je tape :

```shell
ls /
```

J'obtiens tous les dossier de la racine :

```shell
Applications Users        cores        home         sbin         var
Library      Volumes      dev          opt          tmp
System       bin          etc          private      usr
```

La commande `ls`{.language-} a beaucoup de paramètres possible. Dans le monde du terminal, une commande va faire une unique chose mais de plein de façon disponible. C'est souvent ce qui fait peur, mais au final on utilisera jamais toutes les possibilités. Par exemple la [documentation de la commande ls](http://manpagesfr.free.fr/man/man1/ls.1.html) nous permet :

* afficher toutes les informations :
  * unix/mac : `ls -l`{.language-}
  * powershell : `ls`{.language-}. L'instruction `ls`{.language-} sous powershell est équivalente à [`Get-ChildItem`{.language-}](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
* voir les fichiers cachés :
  * unix/mac : `ls -a`{.language-}
  * powershell : `ls -Force`{.language-}
* voir tous les fichiers et récursivement :
  * `ls -R`{.language-}. Si je veux voir tous les fichiers depuis la racine, je peux taper : `s -R /`{.language-} (attention ça va prendre du temps...)
  * `ls -Depth 3`{.language-}. Sous powershell, il faut donner le nombre de récursion que 'on peut faire. Ici 3.
* ...

{% info %}

N'hésitez pas à aller voir la documentation :

* [ls du powershell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem) alias vers la commande `Get-ChildItem`{.language-}
* [ls unix](http://manpagesfr.free.fr/man/man1/ls.1.html)

{% endinfo %}

### Création et suppression de fichiers/dossiers

#### Créer un dossier

Commande :

```shell
mkdir <chemin absolu ou relatif vers le dossier à créer>
```

Par exemple : `mkdir truc/chose`{.language-}  crée le dossier chose dans le dossier truc lui même placé dans le dossier courant (si le dossier *"./truc"* n'existe pas, il y a une erreur)

{% info %}
Documentation :

* [mkdir du powershell](https://ss64.com/ps/new-item.html) qui est un alias vers la commande `new-item`{.language-}
* [mkdir unix](https://linux.die.net/man/1/mkdir)

{% endinfo %}

#### Supprimer un fichier/dossier

```shell
rm <chemin absolu ou relatif vers le fichier à supprimer>
rm -r <chemin absolu ou relatif vers le dossier à supprimer>
```

{% info %}
Documentation :

* [rm du powershell](https://ss64.com/ps/remove-item.html) redirige vers la commande `remove-item`{.language-}
* [rm unix](https://linuxtect.com/linux-rm-command-tutorial/) La commande `rm`{.language-} a beaucoup, beaucoup de paramètres possibles

{% endinfo %}

### On vérifie qu'on a compris

Faite le jeu ci-après (c'est un genre de [MUD](https://fr.wikipedia.org/wiki/Multi-user_dungeon) solitaire), fait pour comprendre et utiliser le terminal unix :

{% lien %}
[Perdu dans un monde étrange](http://luffah.xyz/bidules/Terminus/)
{% endlien %}

Les commandes que vous verrez sont toutes utilisables avec les terminaux Linux et Macos et la plupart fonctionnent également sous powershell (ou possèdent des équivalent, comme la commande `cat`{.language-} qui est la commande `Get-Content`{.language-} par exemple)

## <span id="path"></span> Path

Le **path** regroupe un ensemble de dossiers où le système ira regarder pour savoir quelle commande exécuter.

### Connaître le path

Dans un terminal, tapez :
{% details "Windows  11" %}

```
$env:Path
```

{% enddetails %}

{% details "Systèmes Unix" %}

```
echo $PATH
```

{% enddetails %}

Cela affichera les différents dossiers du path séparé par des :

* `:` sous Unix
* `;` sous Windows

### Modification du path

Dan un terminal, on peut modifier la variable contenant le path pour ajouter un dossier.

Par exemple, pour ajouter le dossier `/users/franc/bin`{.fichier} au début du path :

{% details "Système Unix" %}

On suppose que le shell est celui par défaut ([bash](https://www.gnu.org/software/bash/) sous Linux/Ubuntu et [zsh](https://www.zsh.org/) sous Macos) :

```
export PATH="/users/franc/bin:$PATH"
```

{% enddetails %}

{% details "Système Windows 11" %}

```
$env:Path = "C:\users\franc\bin;" + $env:Path
```

{% enddetails %}

Ces modifications ne sont pas permanentes, elles ne sont valable que dans la fenêtre du terminal. Ouvrez une nouvelle fenêtre terminal et votre modification ne sera pas effectuée.

### <span id="modification-permanente-path"></span> Modification permanente du path

On a parfois besoin de modifier de façon permanente le path. Les méthodes utilisées pour cela sont différentes sous unix/mac et windows.

Pour ceci, Il faut faire la modification précédente à chaque fois que l'on ouvre un terminal. Pour éviter de devoir taper la commande à chaque fois, on va l'ajouter au fichier de configuration du terminal.s

{% attention %}
Ce ne sont pas des modifications courantes, on peut très bien essayer de s'en passer si la modification de fichiers de configuration fait un peu peur.
{% endattention %}

{% details "sous Windows 11" %}

Depuis le menu démarrer, allez dans les `paramètres` puis dans `informations système`. Il faut ensuite cliquer sur `Paramètres avancés du système` :

![paramètres avancés du système](parametres-avancés-systèmes.png)

Pour arriver à cette fenêtre :

![path 1](path-changement-1.png)

En cliquant sur `variables d'environnement` vous pourrez modifier la variable `PATH` :

![path 2](path-changement-2.png)

{% enddetails %}
{% details "sous Macos" %}

Par défaut le shell utilisé est [zsh](https://www.zsh.org/). Son fichier de configuration lu au login est un fichier nommé `.zprofile`{.fichier} qui est dans votre dossier personnel (la maison). Vous pouvez éditer ce fichier et ajouter la ligne de modification à la fin de celui-ci.

On peut aussi le faire directement avec la commande :

```
echo 'export PATH="/users/franc/bin:$PATH"' >> $HOME/.zprofile
```

Qui ajoute la ligne `export PATH="/users/franc/bin:$PATH"`{.language-} à la fin du fichier `.zprofile`{.fichier} de la maison.

{% info %}
<https://www.zerotohero.dev/zshell-startup-files/>
{% endinfo %}

{% enddetails %}

{% details "sous Linux/Ubuntu" %}

Par défaut le shell utilisé est [bash](https://www.gnu.org/software/bash/). Son fichier de configuration lu au login est un fichier nommé `.bash_profile{.fichier} qui est dans votre dossier personnel (la maison). Vous pouvez éditer ce fichier et ajouter la ligne de modification à la fin de celui-ci.

On peut aussi le faire directement avec la commande :

```
echo 'export PATH="/users/franc/bin:$PATH"' >> $HOME/.bash_profile
```

Qui ajoute la ligne `export PATH="/users/franc/bin:$PATH"`{.language-} à la fin du fichier `.bash_profile`{.fichier} de la maison.

{% info %}
<https://opensource.com/article/17/6/set-path-linux>
{% endinfo %}
{% info %}
<http://mywiki.wooledge.org/DotFiles>
{% endinfo %}
{% enddetails %}

## Pour aller plus loin

* [tutoriel Linux/Ubuntu : terminal pour les débutants](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
* [tutos windows powershell](https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1)
* [propriétés du l'application terminal sous mac](https://support.apple.com/fr-fr/guide/terminal/welcome/mac)
