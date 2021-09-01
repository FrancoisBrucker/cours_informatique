---
layout: page
title:  "Les cours"
tags: informatique graphes
author: "François Brucker"
---


Gestion de version. On verra un peu de théorie et surtout de la pratique pour l'utilisation de git et github au quotidien.

> TBD : mise au propre
{: .note}

## Installation

### Github


[github](https://github.com/) est le site qui va nous permettre de conserver et partager nos projets. 

Créez vous un compte en utilisant une adresse "pro", c'est ce compte qui pourra faire office de *book* sur votre cv.

 > Utilisez une adresse, genre un gmail, qui pourra vous suivre tout au long de votre vie et de vos différents emplois.

Nous utiliserons essentiellement la ligne de commande, mais parfois, il est bon de pouvoir utiliser une application. Téléchargez et installez l'[application desktop](https://desktop.github.com/) de github.

### git

{% details Linux %}

> <https://git-scm.com/download/linux>

```shell
apt-get install git
```

{% enddetails %}

{% details Mac %}

> on utilise <https://brew.sh/>

```shell
brew install git
```

{% enddetails %}

{% details Windows %}

> <https://gitforwindows.org/>

Gardez les paramètres par défaut lors de l'installation à part pour le choix de l'éditeur par défaut. Remplacez *vim* par *notepad++* par exemple (si vous n'avez pas [notepad++](https://notepad-plus-plus.org/), installez le.)

{% enddetails %}


### clé ssh

> TBD
{: .note}


## Plan

* [git et github]({% link cours/git_et_github/git_et_github.md %})
* [les commandes indispensables]({% link cours/git_et_github/git_commands.md %})
* [git rebase, la tronçonneuse magique]({% link cours/git_et_github/git_rebase.md %})
* [les commits atomiques]({% link cours/git_et_github/git_commits_atomiques.md %})
