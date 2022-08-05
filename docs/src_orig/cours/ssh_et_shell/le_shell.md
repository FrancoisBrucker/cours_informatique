---
layout: page
title:  "Shell"

category: cours
tags: 
author: Valentin Defrance
---


## Qu'est-ce que c'est ?

Un [shell](https://fr.wikipedia.org/wiki/Shell_Unix#Shells) Unix est un interpréteur de commande destiné aux systèmes d'exploitation Unix et qui permet d'accéder aux fonctionalités internes du système.

Ils existe plusieurs variantes de shell. À l'origine , l'interpréteur de commandes par défaut était sh et à donné naissances à diverse variantes dont csh étendu en tcsh ou ksh ou encore rc... Mais aujourd'hui bash, s'inspirant de sh, ksh, et csh, est le shell le plus répandu, bien qu'il existe d'autres interpréteurs de commandes, comme zsh, ou ash.

* sh : Bourne Shell. L'ancêtre de tous les shells.
* bash : Bourne Again Shell. Une amélioration du Bourne Shell, disponible par défaut sous Linux et Mac OS X.
* ksh : Korn Shell. Un shell puissant assez présent sur les Unix propriétaires, mais aussi disponible en version libre, compatible avec bash.
* csh : C Shell. Un shell utilisant une syntaxe proche du langage C.
* tcsh : Tenex C Shell. Amélioration du C Shell.
* zsh : Z Shell. Shell assez récent reprenant les meilleures idées de bash, ksh et tcsh.


Nous nous intéresseront plus particulièrement aux shells bash et aux distribution [Debian](https://www.debian.org/index.fr.html) et [ubuntu](https://ubuntu.com/) pour l'installation de packages.

## Les Bases

* La touche `tab` permet l'auto-complétion d'une commande en cours d'écrtiture.
* Afin de coller une commande du presse-papier dans le Shell, il faut effectuer un clic droit dans celui-ci.
* La commande `man [commande]` permet d'afficher l'aide d'une commande, pour celà il vous faudra probablement installer le paquet manuel au préalable (`sudo apt install man` (il faut remplacer `apt` par `brew` sur Mac)).
* La commande `ls` permet d'obtenir la liste et les caractéristiques des fichiers contenus dans un répertoire. Si aucun argument n'est donné, la commande “ls” affiche la liste des noms de fichiers du répertoire courant. Cette commande possède plusieurs options (`ls -[Option1][Option2]`) permettant d'afficher un résultat différent :
  * `ls -p` : Cette option permet de distinguer les répertoires des fichiers dans le retour de commande en ajoutant `/` après le nom de chaque répertoire .
  * `ls -a` : Ajoute à la liste des répertoires les répertoires cachés (ceux dont le nom commence par "`.`")
  * `ls -l` : permet d'afficher une liste détaillée des caractéristiques de chaque fichier du répertoire. Il est d'usage d'ajouter l'option -h à -l afin d'obtenir les informations de poids d'occupation en plus lisible pour un humain plutôt qu'en octet et donc d'utiliser `ls -lh`. Avec cette option ls va adapter son affichage en utilisant l'unité la plus adaptée.
  * `ls -R` : pour récursif, permet d'afficher une liste des caractéristiques de chaque fichier dans tous les répertoires à partir d'où nous sommes.
  * `ls -lR` : permet d'afficher une liste des caractéristiques de chaque fichier de tous les répertoires à partir d'où nous sommes avec les caractéristiques des droits.
  * `ls -t` : permet de trier le contenu des répertoires en fonction de la date et non pas en ordre alphabétique. Les fichiers les plus récents sont présentés en premier.
  * `ls -u` : permet d'employer la date des derniers accès aux fichiers plutôt que la date de modification, autant pour l’affichage (option -l) que pour le tri (option -t).
  * `ls -d` : permet d'afficher une liste des répertoires sans leur contenu à partir d'où nous sommes.
* La commande `echo` dans un terminal ou en console, affiche le texte rédigé en argument (voir [documentation echo](https://debian-facile.org/doc:systeme:echo))

## Compte de l'administrateur (root)

Le compte de l’administrateur (root) ou super-utilisateur ou encore utilisateur privilégié permet d'effectuer les opérations d’administration du système suivantes :

lire, écrire et effacer n’importe quel fichier du système quelles que soient ses permissions

Définir l'appartenance et les permissions de n’importe quel fichier du système

définir le mot de passe de n’importe quel utilisateur non-privilégié du système

vous connecter à n’importe quel compte sans mot de passe.

La puissance illimitée du compte de l’administrateur fait que vous devez être attentif et responsable lorsque vous l’utilisez.

sudo : Sudo (Parfois considéré comme l'abréviation de Super-user do) est un programme dont l'objectif de permettre à l'administrateur du système d'autoriser certains utilisateurs à exécuter des commandes en tant que superutilisateur et peut être nécessaire pour l'installations de divers paquets. (ATTENTION : n'utilisez jamais sudo sur une commande dont vous ne connaissez pas les effets)

## Variables

Les [variables](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/) sont composées d'un nom et d'une valeur associée. Il existe sous Linux deux principaux types de variables : les variables d'environnement et les variables de shell. Les variables ont le format suivant :

~~~ shell
KEY=value
KEY="Some other value"
KEY=value1:value2
~~~

* Le nom des variable est sensible aux majuscules et aux miniscules, par convention les variables d'environnement ont un nom en majuscule.
* Quand on assigne plusieurs valeurs à une variable, elles doivent être séparées par `:`
* Il n'y a pas d'espaces avant et après le symbole `=`

Les variables d'environnement sont des variables héritées du système et sont disponible sur tout le système.

Les variables de shell sont des variables qui ne s'appliquent que sur l'instance shell actuelle.

La commande la plus utilisée pour afficher le contenu d'une variable est la commande `printenv`, si le nom d'une variable est donné en argument, la commande renverra le contenu de la variable, si aucun argument n'est donné, la commande affichera la liste de toutes les variables d'environnement.

~~~ shell
printenv HOME
~~~

Output : `/home/username`

Voici une liste des variables d'environnement les plus courantes :

* `USER` L'actuel utilisateur connecté
* `HOME` Le répertoire principal de l'utilisateur actuel
* `SHELL` Le chemin vers le shell de l'utilisateur actuel
* `LOGNAME` Le nom de l'utilisateur actuel
* `PATH` Une liste des répertoires qui seront cherchés lors de l'exécution d'une commande : lors de l'exécution d'une commande, le système va chercher un exécutable dans ces répertoires (dans l'ordre d'affichage) et va exécuter le premier exécutable trouvé
* `LANG` Les paramètres locaux actuels

## Navigation dans les répertoires

La commande `cd` (Change Directory) est utilisée pour changer de répertoire de travail, c'est l'une des commandes les plus basiques et l'une des plus fréquemment utilisée.

La commande `cd` peut s'utiliser de deux manières différentes. Soit avec un chemin relatif, soit avec un chemin absolu.  Le chemin absolu ou complet débute à la racine (root) du système `/`, le chemin relatif démarre au niveau de votre répertoire actuel.

Par exemple, imaginons que je veuille me rendre au répertoire Downloads présent dans mon répertoire username, je peux le faire de manière relative :

~~~ shell
cd Downloads
~~~

Je peux aussi m'y rendre de manière absolue :

~~~ shell
cd /home/username/Downloads
~~~

Compléments :

* La commande `pwd` permet d'afficher le chemin (path) de votre répertoire de travail actuel.
* Le chemin de votre répertoire de travail est affiché avant le symbole `$` sur l'invite de commandes. Le symbole `~` représente votre répertoire de travail par défaut, c'est à dire celui dans lequel vous vous retrouverez au démmarage de votre système, de plus la commande `cd` sans arguments vous renverra directement dans votre répertoire par défaut. (dans mon cas /home/username)
* Le répertoire actuel est représenté par (`.`), le répertoire parent par (`..`). Taper `cd ..` vous ramènera au répertoire parent de votre répertoire de travail actuel
* La commande `cd -` vous ramènera à votre précédant répertoire de travail (en intervertissant les variables PWD et OLDPWD qui sont respectivement votre répertoire de travail et votre précédant répertoire de travail)
* Le caractère `\` permet d'ignorer un caractère spécial comme un espace : si un de vos dossier s'appelle "pourquoi pas", il sera nécessaire de l'écrire "/pourquoi\ pas"
* Appuyer sur `tab` après la commande cd permet de lister les répertoires fils disponibles

Exemple : cette ligne de commande vous ramène deux répertoires parents en arrière puis au répertoire Downloads

~~~ shell
cd /../../Downloads
~~~

## Installation de paquets

Pour installer un paquet, il faut utiliser la commande suivante :

~~~ shell
sudo apt install packageName
~~~

L'utilisation de sudo est nécessaire afin d'exécuter la commande avec les droits nécessaires pour télécharger le paquet. (Sur Mac, `apt` est remplacé par `brew`). Par exemple si nous voulons installer *vim* qui est une version plus puissante de l'éditeur de texte *vi*, il faudra entrer la commande :

~~~ shell
sudo apt install vim
~~~

## vim

Comme dit précédemment, [vim](https://wiki.debian.org/fr/vim) est un éditeur de texte en mode console. Vous pouvez aussi juste afficher le contenu d'un fichier avec la commande `cat /chemin/de/votre/fichier` (ou `cat nomDuFichier` en chemin relatif). De même avec la commande `vim`. Par exemple pour ouvrir le fichier *"readme.txt"* de mon répertoire de travail, je dois taper une des deux commandes :

~~~ shell
vim readme.txt
vim /home/username/readme.txt
~~~

Le contenu du fichier est ainsi affiché dans le terminal et il est possible de déplacer le curseur avec les flêches. Cependant il n'est pas possible d'éditer du texte car nous somme dans le mode normal de vim. Pour éditer le texte nous allons devoir passer en mode insertion.

* `i` : insertion du texte juste avant la position courante du curseur
* `I` : insertion du texte juste au début de la ligne courante
* `a` : insertion du texte juste après la position courante du curseur
* `A` : insertion du texte à la fin de la ligne courante

Pour le mode insertion. Il est possible de modifier le texte à peu près comme dans un éditeur de texte graphique. Il ne manque que l'utilisation de la souris.

Pour enregistrer les modifications, il suffit de quitter le mode insertion avec la touche Esc (Echap), puis on tape :

* `:w` pour enregistrer
* `:q` pour quitter
* `:wq` pour enregistrer et quitter
* `:x` pour enregistrer et quitter
* `:q!` ignorer les modifications

## Pipes et redirections

La redirection de sortie `>` permet d'indiquer à un processus que tout ce qui devrait aller sur la sortie standard (par défaut, le terminal), doit plutôt être stocké dans un fichier. Par exemple, la commande `echo "Hello World" > salut.txt` écrasera le fichier salut.txt pour y écrire "Hello World". Si ce fichier n'existe pas, il sera alors créé. (on peut remplacer `>` par `>>` pour ajouter une ligne à la fin du fichier plutôt que de l'écraser).

La redirection d'entrée `<` permet d'indiquer à un processus qu'il doit utiliser un fichier comme entrée standard. Par exemple, la commande `cat < salut.txt` affichera donc "Hello World" (le contenu du fichier salut.txt) dans la console.

Le caractère pipe est `|`, il est le caractère présent sur la touche `6` du clavier. Les tubes ou pipes permettent de rediriger directement le canal de sortie d'une commande vers le canal d'entrée d'une autre commande et de créer des chaînes de commandes. Cette fonctionnalité peut permettre par exemple de compresser un fichier, l'envoyer sur un autre ordinateur et le décompresser en une seule ligne de code.

Pour plus d'information concernant les redirections : [Lien utile](https://putaindecode.io/articles/maitriser-les-redirections-shell/)

## Cheat-Sheet

Voici une [Cheat-Sheet]({% link cours/ssh_et_shell/shell_cheat_sheet.md %}) récapitulant la plupart des commandes dont vous aurez besoin.
