---
layout: page
title:  "Installation W10 pour le développement"
category: tutorial
tags: combat w10
---


# Préparation

Pour éviter tout conflit avec une configuration existante, on utilisera une installation fraîche de la dernière version de W10.
On va suivre la procédure de [mirosoft](https://support.microsoft.com/fr-tn/help/4000735/windows-10-reinstall)
Pour éviter tout soucis ou regrets :

- **notez** le numéro de série de votre W10 ou ayez votre compte d'activé
  - sauvegardez vos données (vos images, vos documents, etc)
  - notez tous les programmes que vous voulez conserver
  
# Réglages

## confidentialité

Une fois l'installation terminée, vous pouvez cliquer sur **non** à chaque fois que Windows (ou Cortana) vous demande de partager vos données.
- Allez dans `Démarrer > Paramètres > Confidentialité` et vérifier pour chaque onglet à gauche que les paramètres d'envoi de vos données vous satisfont (je ne donne que ce que je considère être le stricte nécessaire, à chacun de faire comme il le souhaite)
- pour les paramètres de sécurité, vous pouvez toujours aller voir la [cnil](https://www.cnil.fr/fr/reglez-les-parametres-vie-privee-de-windows-10-apres-installation) ou [ce site](http://www.win10.fr/reglages-confidentialite-windows10)

## compte

J'utilise un compte local et pas mon compte Microsoft pour me connecter. Assurez vous que le nom de votre compte ne contient aucun espace ou accent (on le voit avec l'explorateur de fichier `c:\Utilisateurs`) et que c'est un compte administrateur.


## Windows update

Vérifier que votre système est à jour en cliquant sur `Démarrer > Paramètres > mise à jour et sécurité > Windows update`

## Version du système
Pour installer la wsl 2, il faut nécessairement avoir une version de w10 supérieure ou égale à la 2004.
Pour connaître votre version : `Menu Démarrer > Paramètres > Système > information système` Dans la partie Spécification de Windows.

## explorer

Affichez les fichier caché dans l'explorer. Cela va être utile à de nombreuses reprises. Pour cela, ouvrez un explorateur de fichier puis choisissez affichage et cochez la case *Éléments masqués*


# Premières installations indispensable
## un navigateur
Prenez celui de votre choix, personnellement j'utilise [chrome](https://www.google.com/intl/fr_fr/chrome/) que je mets en navigateur par défaut.

## drivers

  - carte graphique
  - clavier/souris si nécessaire
  - imprimante
  - autres trucs bas niveau (icloud drive, tablette, ...)

## Un éditeur de texte
On en installera d'autres par la suite, mais il est toujours appréciable d'avoir un éditeur de texte sous la main pour modifier rapidement un fichier de conf. J'utilise [notepad++](https://notepad-plus-plus.org/downloads/) pour ce genre d'opérations.

# Autres installations non développement

## outil de décompression

Il y en a plusieurs. [7zip](https://www.7-zip.org/) est simple d'utilisation et très complet.

## utilitaires de tout les jours

Non indispensable mais que vous utilisez tous les jours

  - steam, gog, epic, battle.net, origin, uplay, etc
  - vlc, office 360
  - discord
  - ...
  
# Développement

Pour utiliser une machine windows en développement, il va être nécessaire d'installer plusieurs logiciels qui vous nous permettre d'utiliser peu ou prou windows comme une machine unix

## openssh

Protocole de communication sécurisé. On en installera un autre avec la wsl2mais c'est pas mal d'avoir celui de widows opérationel.

### client
Le client openssh de windows devrait être installé. Pour le vérifier, aller dans `démarrer > Paramètres > Applications > fonctionnalités facultatives` et vérifiez que *Client OpenSSH* est installé (si vous cliquez dessus, il vous propose de le désinstaller. ne le faites pas...).

### serveur ssh

  1. Cliquez sur ajouter une fonctionnalité et installez le /serveur OpenSSH/
  2. la configuration initiale du serveur se fait via le powershell. Ouvrez un terminal `powershell` en mode administrateur (taper `powershell` dans la barre de recherche puis choisissez *Exécuter en tant qu'administrateur*). On copie colle les lignes de [la doc](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse#initial-configuration-of-ssh-server)  qui vont permette au serveur ssh de se lancer à chaque démarrage : 
     ~~~ powershell
     Start-Service sshd
     # OPTIONAL but recommended:
     Set-Service -Name sshd -StartupType 'Automatic'
     # Confirm the Firewall rule is configured. It should be created automatically by setup.
     Get-NetFirewallRule -Name *ssh*
     # There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled
     # If the firewall does not exist, create one
     New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
     ~~~
     
Une fois le serveur ssh configuré redémarrer votre ordinateur.

Si la configuration précédente ne fonctionne pas, essayer de suivre les instruction de [cette question](https://stackoverflow.com/questions/52113738/starting-ssh-agent-on-windows-10-fails-unable-to-start-ssh-agent-service-erro). Ils vous conseillent de commencer par l'arrêter puis le mettre en manuel. 

### doc
- https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse
- https://stackoverflow.com/questions/52113738/starting-ssh-agent-on-windows-10-fails-unable-to-start-ssh-agent-service-erro

### vérifier que ça fonctionne
Ouvrez une fenêtre powershell   et, en remplaçant login par votre login unix de l'école tapez la commande : `ssh-add -l`

Vous devriez avoir une phrase vous disant que l'agent n'a pas d'identité. Si vous n'avez pas d'agent installé (ou si vous l'avez stoppé) cela devrait vous dire qu'on arrive pas à se connecter à l'agent.


## wsl 2

Wsl 2 est une installation linux qui cohabitera avec votre windows. Vous interagirez via une fenêtre terminal (*NB:* coller = click droit).

### installation

On suit les directives de [la doc](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10). Vous installerez une distribution *debian*. Lorsque vous lancerez l'application, elle se met à jour. Profitez en pour cliquer-droit sur l'îcone et de cocher /épingler à la barre des tâches/. Comme ça vous aurez toujours un terminal sous la main.

On vous demandera de créer un nom de compte. Perso, je choisit toujours le même login qui correspond à celui de l'école.

### mise à jour

~~~ sh
sudo apt update
sudo apt upgrade
~~~

On peut maintenant installer nos package
~~~ sh
sudo apt install ssh
sudo apt install vim
~~~

### ssh-agent

On va suivre les instructions de [ce site](https://www.scivision.dev/ssh-agent-windows-linux/) et ajouter à la fin de notre `~/.bashrc` les lignes suivantes qui permettrons d'avoir un ssh-agent d'opérationnel en wsl.

~~~ sh
if [ -z "$(pgrep ssh-agent)" ]; then
   rm -rf /tmp/ssh-*
   eval $(ssh-agent -s) > /dev/null
else
   export SSH_AGENT_PID=$(pgrep ssh-agent)
   export SSH_AUTH_SOCK=$(find /tmp/ssh-* -name agent.*)
fi
~~~

Cette configuration a cependant toujours 2 agents différent, celui de windows et celui de wsl. Selon qu'on cherche à se connecter depuis windows ou depuis wsl, on utilisera l'un ou l'autre des agents.

### les fichiers

  - les fichiers windows sont accessible depuis wsl via le répertoire `/mnt/``
  - les fichiers wsl sont accessible depuis l'[explorateur windows](https://devblogs.microsoft.com/commandline/whats-new-for-wsl-in-windows-10-version-1903/). Dans un terminal wsl, tapez les commandes suivante :
    ~~~ sh
    cd ~
    explorer.exe .
    ~~~
    

  Une fenêtre d'explorateur doit s'ouvrir dans le dossier home de votre compte wsl.

### les fenêtres

Les fenêtres unix fonctionnent avec un protocole x11. Il faut installer un serveur x11 dans windows pour pouvoir ouvrir des fenêtres unix dans windows.

Pour faire nos tests de fenêtre on utilisera la commande `xeyes`. Il faut commencer par l'installer

~~~ sh
sudo apt install x11-apps
~~~

#### lancer un serveur X sous windows

On va installer [vcxsrv](https://sourceforge.net/projects/vcxsrv/).

Vous lancez un serveur X en exécutant `XLaunch`. Les paramètres du serveur X sont :
    
  - Multiple windows et display windows -1 (paramètres par défaut),
  - Start no client (paramètres par défaut),
  - cochez toutes les cases. Celles déjà cochées (clipoard, Primary Selection ; Native opengl) celle qui n'est pas cochée par défaut (Disable access control)

#### associer le serveurs aux fenêtres depuis wsl

Maintenant que votre serveur X est lancé il faut l'associer aux fenêtre depuis wsl. [ceci se fait](https://stackoverflow.com/questions/61110603/how-to-set-up-working-x11-forwarding-on-wsl2/61110604#61110604) en positionnant deux variables :

~~~ sh
export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0
export LIBGL_ALWAYS_INDIRECT=1
~~~

Vous pouvez ensuite taper `xeyes`` dans un terminal wsl et vous obtiendrez une paire d'yeux qui vous regarde.

Vous pouvez ajouter les deux ligne ci-dessus à votre fichier `~/.bashrc` pour qu'il soit exécuté à chaque session si vous le souhaitez.

### brew

[brew](https://brew.sh/index_fr) est un célèbre installeur de packages sous macos. Nous allons également l'installer pour wsl, histoire de n'avoir qu'une commande pour l'installation de package quelque soit le système utilisé.

Pour [installer brew](https://docs.brew.sh/Homebrew-on-Linux), il faut commencer par installer des packages avec apt :
~~~ sh
sudo apt-get install build-essential curl file git
~~~

Une fois tout ça d'installé, on peut installer brew :

~~~ sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
~~~

Lisez ce que vous dit brew et faites les dernières manipulations :

- faire en sorte de retrouver la commande brew l'ajoutant dans le `PATH`
  - installer `gcc`

On teste si on arrive à installer des choses :

~~~ sh
brew install hello
hello
~~~

## python

Avoir un interpréteur python est très pratique pour faire de petits programmes et/ou de la data science. Pour le dev proprement dit, python sera installé sur la wsl, voir installé pour chaque projet, mais pour des besoins plus ponctuel on va installer anaconda sur la système windows. 

### anaconda

Anaconda est une distribution python oriente data science. Commençons par l'[installer](https://www.anaconda.com/products/individual) :

  - on utilisera la version windows 64bits utilisant `python3`,
  - installez la pour tous les utilisateurs
  - laissez coché la case qui lie l'interpréteur python d'anaconda au système.

Anaconda est maintenant installé sur votre disque dur dans le dossier : `c:\ProgramData\Anaconda3` et vous trouverez un dossier *Anaconda3* dans le menu démarrer

#### jupyter

Depuis le *menu démarrer > Anaconda3* vous pouvez lancer le programme `Anaconda navigator`` qui vous permettra d'exécuter jupyter sur votre navigateur.

#### installer de nouveau packages dans anacoda

Vous pouvez le faire via anaconda navigator, mais le plus simple est encore d'installer directement.

Cliquer sur /menu démarrer > Anaconda3 > Aanconda powershell prompt/. Une fenêtre poershell se lance aliée avec l'interpréteur python d'anaconda.

Vous pouvez ainsi taper directement la commande pip pour installer des modules python :
- tapez /python/ dans cette fenêtre et vous exécuterez l'interpréteur pyhton d'anaconda (/exit()/ puis entrée ou control+D pour sortir de l'interpréteur)
- La commande /pip list/ va lister tous les modules que vous avez installé par exemple.
 
### pycharm

Installez [pycharm professionnel](https://www.jetbrains.com/fr-fr/pycharm/download/). En tant qu'étudiant vous pouvez obtenir une licence gratuite du logiciel. Faites le pour pouvoir utiliser les fonctionnalités avancées de pycharm, comme l'utilisation d'un python de wsl.

Une fois l'installation terminée créer un nouveau projet en utilisant l'interpréteur d'anaconda. Pour cela, une fois avoir choisi de faire un nouveau projet :

  1. choisissez /existing interpreter/ puis cliquez sur les /.../
  2. cliquez sur /Conda Environment/ puis sur les /.../ pour trouver l'interpréteur.
     Si vous avez installé anaconda pour tous les utilisateur, il doit se trouver dans `c:\ProgramData\Anaconda3\Scripts\python.exe`
  3. Avant de cliquer sur *Ok*, n'oubliez pas de cocher la case *Make available to all projects* pour ne pas avoir a rechercher l'interpréteur à chaque fois.
  4. Votre interpréteur est crée, vous pouvez maintenant cliquer sur *Create* pour générer votre projet.

Créer un fichier `hello_world.py` :

~~~ python
print("hello world!")
~~~

Puis exécutez le pour vérifier que tout fonctionne.

>**odds and ends** :
>
>  - Il est possible que le triangle vert de l'exécution ne soit pas disponible. C'est le cas lorsque pycharm *"travaille"* : la ligne de status, tout en bas de la fenêtre, indique en bleue *process running...* (vous pouvez cliquer dessus pour voir ce que pycharm est entrain de faire). Une fois qu'il a fini de travailler, vous pourrez exécuter votre code.
>  - j'ai récemment eu des soucis avec pycharm qui ne voulait pas se relancer après l'avoir fermé. C'est parce que le programme pycharm ne s'était pas bien arrêté. Donc `ctrl+alt+supr > gestionnaire des taches > processus en arrière plan` et cherchez pycharm. Fermez le et on peut réouvrir le programme.
  

### un python dans wsl et son utilisation dans pycharm

Pour utiliser python sur la wsl, on peut l'installer avec `brew` :

~~~ sh
brew install python3
~~~

Ce qui est chouette avec pycharm, c'est qu'il peut utiliser un interpréteur python distant. Faisons en sorte que le pycharm sous windows utilise l'[interpréteur python de la wsl](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html) :

  - dans un shell wsl tapez `which python3` pour connaître l'emplacement de l'interpréteur python3 (c'est celui de brew que l'on vient d'installer)
  - Ouvrez un projet pycharm existant (le hello world de l'installation d'anacoda par exemple) et allez dans les *file > settings > project interpreter*. Cliquez sur l'engrenage à droite du nom de votre interpreteur :
      1. choisissez wsl (à gauche, c'est le manchot)
      2. choisissez existing environnment puis cliquez sur les *...*
      3. retrouvez le chemin de l'interpréteur de wsl. Le chemin commence forcément par `\\wsl\Debian\`

Une fois que pycharm aura fini d'analyser le nouvel interpréteur, vous pourrez exécuter le fichier.

Vous pouvez même [configurer le terminal](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html#wsl-terminal) pour que ce soit celui du wsl et pas celui de votre windows.

>**odds and ends** :
>
>  - en créant un nouveau projet, ça ne marche pas. Il faut modifier un projet existant. Je ne sais pas pourquoi.

## docker
## virtualbox

## sdkman

# autres
- scoop
- git bash ?


