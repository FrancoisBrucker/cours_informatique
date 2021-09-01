---
layout: page
title:  Nouvelle installation de son système
tags: système terminal
category: installation
authors: 
    - François Brucker
---

Comment bien préparer son ordinateur pour faire du développement. On ne montrera ici que le départ, c'est à dire l'installation fraiche d'un système sur lequel on pourra ensuite installer — proprement — les divers outils et logiciels utiles pour le développement.

<!--more-->

## Introduction

Pouvoir développer des logiciels et exécuter ses propres programmes nécessite quelques connaissances et compétences.

Rien d'insurmontable, mais si on ne le fait pas on a vite un système instable où rien de marche comme il faudrait. 

Il faut résister à la tentation de faire n'importe quoi en espérant que ça passe car, au bout du compte, on perd plus de temps à réparer qu'on en gagne à installer sans préparation.

> Il est recommandé de partir d'un système propre est vierge. En effet, si quelque chose ne fonctionne pas c'est souvent parce qu'on a précédemment installé quelque chose d'incompatible en suivant sans comprendre un tuto de l'internet.


A la fin de ce tuto vous devez avoir :
* un système d'installation sain
* un gestionnaire de package
* un éditeur de texte

## Un nouveau compte 

Si vous ne vous pouvez pas réinstaller un nouveau système, pour que tout se passe au mieux assurez vous que votre compte :

* soit un compte administrateur (pouvant exécuter sudo si vous êtes sous linux)
* votre login ne doit contenir aucun espace, ni accent.

> le login est différent de votre nom. 
{: .attention}
compte admin :  sans accent ni espace

* administrateur sous windows/mac
* pouvant exécuter sudo sous linux

> Il peut être utile d'avoir un compte uniquement pour travailler/développer et un autre pour jouer. Ceci évitera déjà les conflits de configuration.

## Un nouveau système

Il est souvent possible de réinstaller un nouveau système en conservant vos données. C'est souvent très pratique mais pour une première fois, je vous conseille de faire une installation sur un disque vierge, c'est à dire en ne **conservant rien** de ce qu'il y avait sur votre disque dur.

Installer un nouveau système nécessite de reformater votre disque dur. Avant cela il vous faut faire trois choses :

* sauvegardez vos données sur une clé pour que vous puissiez facilement les remettre sur votre nouveau système
* vérifier les différentes applications actuellement installées et listez celles que vous voulez à nouveau installer.
* lister les différents compte et mots de passe dont vous aurez besoin (wifi, steam, google, ...)

> Avec le cloud ([icloud](https://support.apple.com/fr-fr/guide/icloud/welcome/icloud) sur mac ou [onedrive](https://www.microsoft.com/fr-fr/microsoft-365/onedrive/online-cloud-storage) sous windows) les données personnelles sont souvent déjà sauvegardées. Mais il faut se souvenir du login/mot de passe pour réactiver le tout sur le nouveau système.


> Notez votre wifi et son mot de passe, ou mieux connectez le réseau directement avec un fil si possible pour votre installation.
{: .attention}

### Linux

{% details détails %}

> TBD
{: .note}

{% enddetails %}

### Mac
{% details détails %}

> <https://support.apple.com/fr-fr/guide/mac-help/mchlp1599/mac>

Le plus simple est d'installer une nouvelle version du système en utilisant internet. Redémarrez votre ordinateur en maintenant enfoncé les touches :  *"Maj + Option + Commande + R enfoncées"*

> Notez votre login et mot de passe icloud. Vous en aurez besoin à l'installation
{: .attention}

#### finder

Le finder est l'outil principal qui vous permettra de naviguer dans les fichiers. Pour qu'il soit un peut plus facile d'y naviguer :
* *menu présentation > personnaliser la barre d'outils...* ajoutez le "chemin" (trois barres horizontales) aux outils du finder en le glissant/déposant.
* ajoutez le dossier "*Départ*", aussi appelé "*maison*" (le dossier principal de l'utilisateur) et le dossier "*applications*" aux éléments à la gauche du finder. Pour cela, choisissez le dossier dans le menu *Aller* puis  avec l'outils chemin que l'on vient d'ajouter sélectionnez le dossier parent(Par exemple pour la maison, le dossier parent est "Utilisateurs" et pour application, le dossier parent est “Macintosh HD"). Vous pouvez ensuite glisser/déposer le dossier à gauche du finder.

#### terminal

Le terminal va être un outil fondamental en développement. Ajoutez le aux icônes du finder. Il est dans le dossier Utilitaires de application.

#### drivers 

* imprimante
* autres trucs bas niveau (icloud drive, tablette, ...)

{% enddetails %}

### Windows

{% details détails %}

> Notez le numéro de série de votre windows 10. Vous en aurez besoin à l'installation
{: .attention}

On va suivre la procédure de [mirosoft](https://support.microsoft.com/fr-fr/windows/r%C3%A9installer-windows-d8369486-3e33-7d9c-dccc-859e2b022fc7#ID0EBD=Windows_10) en suivant les instructions de *Installer une nouvelle installation Windows 10 à l’aide d’un support d’installation*.


#### confidentialité

Une fois l'installation terminée, allez dans `Démarrer > Paramètres > Confidentialité` et vérifier pour chaque onglet à gauche que les paramètres d'envoi de vos données vous satisfont.


>Pour les paramètres de sécurité, vous pouvez toujours aller voir la [cnil](https://www.cnil.fr/fr/reglez-les-parametres-vie-privee-de-windows-10-apres-installation) ou [ce site](http://www.win10.fr/reglages-confidentialite-windows10)

#### compte

J'utilise un compte local et pas mon compte Microsoft pour me connecter. Assurez vous que le nom de votre compte ne contient aucun espace ou accent (on le voit avec l'explorateur de fichier `c:\Utilisateurs`) et que c'est un compte administrateur.


#### Windows update

Vérifier que votre système est à jour en cliquant sur `Démarrer > Paramètres > mise à jour et sécurité > Windows update`

#### Version du système

Pour connaître votre version : `Menu Démarrer > Paramètres > Système > information système` Dans la partie Spécification de Windows.

> Pour installer la wsl 2, il faut nécessairement avoir une version de w10 supérieure ou égale à la 2004.

#### explorer

Affichez les fichier caché dans l'explorateur de fichiers. Cela va être utile à de nombreuses reprises. Pour cela, ouvrez un explorateur de fichier puis choisissez affichage et cochez la case *Éléments masqués*

#### drivers 

* carte graphique
* clavier/souris si nécessaire
* imprimante
* autres trucs bas niveau (icloud drive, tablette, ...)

{% enddetails %}

## Applications indispensables

### Un navigateur

Prenez celui de votre choix, personnellement j'utilise [chrome](https://www.google.com/intl/fr_fr/chrome/) que je mets en navigateur par défaut.

### Un éditeur de texte

On en installera d'autres par la suite, mais il est toujours appréciable d'avoir un éditeur de texte sous la main pour modifier rapidement un fichier de conf. 

Selon le système d'exploitation, mon éditeur à tout faire est différent : 

{% details Linux %}

Comme j'utilise linux essentiellement en ligne de commande, mon éditeur de choix est [vim](https://www.vim.org/). Bon, il peut faire un peu peur mais si vous voulez faire de l'informatique votre métier et que vous devrez vous connecter sur des ordinateurs uni distant (un serveur web par exemple) connaitre vim est un gain de temps considérable.

Sinon, pourquoi pas [Atom](https://atom.io/) ?

{% enddetails %}
{% details Mac %}

J'utilise [Textmate](https://macromates.com/).

{% enddetails %}
{% details Windows %}

J'utilise [notepad++](https://notepad-plus-plus.org/downloads/).

{% enddetails %}

### Un gestionnaire de package

N'installez **RIEN** sans avoir un installeur de package qui vous permettra de savoir ce que vous avez installé et de mettre à jour le tout.

{% details Linux %}
Déjà installé par défaut. Cela dépend de votre distribution linux, mais c'est souvent 
[Apt-get](https://doc.ubuntu-fr.org/apt-get). Donc rien à faire.

{% enddetails %}

{% details Mac %}

Pasz vraiment de choix, on installe [brew](https://brew.sh/) et plus vite que ça !

{% enddetails %}

{% details Windows %}

Comme j'installe que peu de choses sous windows, je n'utilise pas vraiment de gestionnaire de paquet dédié (ce qui est mal). Je laisse windows gérer le tout dans le menu application des paramètres. 

Il en existe plusieurs mais je ne sais pas trop le quel est le mieux. Trois alternatives a priori : 
* [winget](https://docs.microsoft.com/fr-fr/windows/package-manager/winget/). 
* [chocolately](https://chocolatey.org/)
* [scoop.sh](https://scoop.sh/)

<https://nodachisoft.com/common/en/article/en000009/>


{% enddetails %}

### outils de compression

{% details Linux %}

Surement déjà installé. 

{% enddetails %}

{% details Windows %}

Surement déjà installé.

{% enddetails %}

{% details Windows %}

Il y en a plusieurs. [7zip](https://www.7-zip.org/) est simple d'utilisation et très complet.

{% enddetails %}


### utilitaires de tous les jours

Non indispensable mais que vous utilisez tous les jours

* steam, gog, epic, battle.net, origin, uplay, etc
*  vlc, office 360
* discord
* ...

