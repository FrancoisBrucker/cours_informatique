---
layout: page
title:  wsl ou linux dans windows
tags: système terminal
categories: 
    - installation
    - WSL
authors: 
    - François Brucker
---

Comment installer et bien préparer wsl pur le développement.

<!--more-->

## Introduction

[WSL](https://docs.microsoft.com/en-us/windows/wsl/) signifie *Windows Subsystem for Linux* et consiste à installer une distribution linux qui cohabite dans votre windows;

Ce n'est ni un dual boot ni une machine virtuelle. L'intérêt principal est que les port de la machine sont partagées entre windows et WSL, ce qui en fait une machine de développement web idéale.

> WSL 2 est de plus indispensable si vous voulez utiliser [docker](https://www.docker.com/) sous windows.

Nous verrons ici comment installer le système et les divers outils que l'on peut utiliser.
A priori seule l'installation et la mise à jour sont indispensable. Le reste c'est pour un usage plus intensif de la WSL en tant qu'outil de développement.

## installation

Trop rien à dire. Suivez la doc : <https://docs.microsoft.com/en-us/windows/wsl/install>.

Il suffit de taper la commande suivant dans un powershell en mode admin :

```shell
wsl --install
```

Ca va préparer l'installation, puis après un reboot, finaliser l'installation. 

> Si vous ne précisez pas la distribution, vous aurez une ubuntu.

Une fois l'installation terminée, vous pourrez ouvrir un terminal unix dans votre windows.

> Vous n'avez pas de fenêtre graphique par défaut sous WSL, vous n'avez accès qu'aux commandes unix en terminal. C'est comme si vous étiez sur un serveur distant à la maison.
{: .attention}

## mise à jour

Dons le terminal de votre ubuntu (ou debian), vous pouvez mettre à jour les différents packages installées :

```sh
sudo apt update
sudo apt upgrade
```

On peut maintenant installer nos packages :

```sh
sudo apt install ssh
sudo apt install vim
```

Vous pourrez ensuite utiliser `apt-get` pour [installer d'autres packages](http://www.octetmalin.net/linux/tutoriels/apt-get.php).

> Le gestionnaire de package de ubuntu et debian est identique, c'est [apt](https://doc.ubuntu-fr.org/apt).


## les fichiers

WSL et windows sont deux systèmes d'exploitation différents qui cohabitent sur une même machine. On a donc pas accès immédiatement aux fichiers de l'un dans l'autre système, mais ce n'est pas très compliquer de le faire.

### les fichiers windows sous wsl

Les fichiers windows sont accessible depuis wsl via le répertoire `/mnt/`

### les fichiers wsl sous windows

Les fichiers wsl sont accessible depuis l'[explorateur windows](https://devblogs.microsoft.com/commandline/whats-new-for-wsl-in-windows-10-version-1903/). Dans un terminal wsl, il suffit de taper les commandes suivantes :

```shell
cd ~
explorer.exe .
```

Une fenêtre de l'explorateur doit s'ouvrir dans le dossier home de votre compte wsl.

## ssh-agent

Cette partie est plus problématique. On ne peut a-priori utiliser l'agent ssh de windows dans wsl. Il faut en créer un pour wsl.

On va suivre les instructions de [ce site](https://www.scivision.dev/ssh-agent-windows-linux/) et ajouter à la fin de notre `~/.bashrc` les lignes suivantes qui permettrons d'avoir un ssh-agent d'opérationnel en wsl :

```sh
if [ -z "$(pgrep ssh-agent)" ]; then
   rm -rf /tmp/ssh-*
   eval $(ssh-agent -s) > /dev/null
else
   export SSH_AGENT_PID=$(pgrep ssh-agent)
   export SSH_AUTH_SOCK=$(find /tmp/ssh-* -name agent.*)
fi
```

Ceci permettra de lancer un agent à chaque fois qu'une fenêtre wsl sera ouverte.

> Cette configuration a cependant toujours 2 agents différent, celui de windows et celui de wsl. Selon qu'on cherche à se connecter depuis windows ou depuis wsl, on utilisera l'un ou l'autre des agents.

## les fenêtres

Utiliser une fenêtre unix dans un windows n'est pas une procédure simple. En effet, le protocole utilisé pour ouvir des fenêtre dans le monde unix (nommé [X11](https://fr.wikipedia.org/wiki/X_Window_System)) est différent de celui utilisé par windows.

Il faut installer un serveur x11 dans windows pour pouvoir ouvrir des fenêtres unix dans windows.

Pour faire nos tests de fenêtre on utilisera la commande `xeyes`. Il faut commencer par l'installer

```sh
sudo apt install x11-apps
```

Il faut procéder en 2 temps :

* avoir un serveur X sous windows
* dire à ubuntu d'utiliser le serveur X de windows comme gestionnaire de fenêtres

### lancer un serveur X sous windows

On va installer [vcxsrv](https://sourceforge.net/projects/vcxsrv/).

Vous lancez un serveur X en exécutant `XLaunch`. Les paramètres du serveur X sont :

* Multiple windows et display windows -1 (paramètres par défaut),
* Start no client (paramètres par défaut),
* cochez toutes les cases. Celles déjà cochées (clipoard, Primary Selection ; Native opengl) celle qui n'est pas cochée par défaut (Disable access control)

Une fois le serveur X lancé, windows comprend le protocole X11.

### associer le serveurs aux fenêtres depuis wsl

Maintenant que votre serveur X est lancé il faut l'associer aux fenêtre depuis wsl. Il faut dire à WSL quel serveur X utiliser pour ses fenêtre. 

[Ceci se fait](https://stackoverflow.com/questions/61110603/how-to-set-up-working-x11-forwarding-on-wsl2/61110604#61110604) en positionnant deux variables :

```sh
export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0
export LIBGL_ALWAYS_INDIRECT=1
```

Vous pouvez ensuite taper `xeyes`` dans un terminal wsl et vous obtiendrez une paire d'yeux qui vous regarde.

> Vous pouvez ajouter les deux lignes ci-dessus à votre fichier `~/.bashrc` pour qu'il soit exécuté à chaque session si vous le souhaitez.

## brew

[brew](https://brew.sh/index_fr) est un célèbre installeur de packages sous macos. Nous allons également l'installer pour wsl, histoire de n'avoir qu'une commande pour l'installation de package quelque soit le système utilisé.

Pour [installer brew](https://docs.brew.sh/Homebrew-on-Linux), il faut commencer par installer des packages avec apt :

```sh
sudo apt-get install build-essential curl file git
```

Une fois tout ça d'installé, on peut installer brew :

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Lisez ce que vous dit brew et faites les dernières manipulations :

* faire en sorte de retrouver la commande brew l'ajoutant dans le `PATH`
* installer `gcc`

On teste si on arrive à installer des choses :

```sh
brew install hello
hello
```

## wsl et vscode

<https://code.visualstudio.com/docs/remote/wsl>