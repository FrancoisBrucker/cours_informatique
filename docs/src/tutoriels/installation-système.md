---
layout: layout/post.njk 
title: Nouvelle installation de son système

tags: ['tutoriel', 'système']

authors: 
    - François Brucker
---

{% chemin %}
[Tutoriels]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}

<!-- début résumé -->

Comment bien préparer son ordinateur pour faire du développement. On ne montrera ici que le départ, c'est à dire l'installation fraîche d'un système sur lequel on pourra ensuite installer — proprement — les divers outils et logiciels utiles pour le développement.

<!-- fin résumé -->

## Introduction

Pouvoir développer des logiciels et exécuter ses propres programmes nécessite quelques connaissances et compétences.

Rien d'insurmontable, mais si on ne le fait pas on a vite un système instable où rien de marche comme il faudrait.

Il faut résister à la tentation de faire n'importe quoi en espérant que ça passe car, au bout du compte, on perd plus de temps à réparer qu'on en gagne à installer sans préparation.

{% note "**Important :**" %}
Il est **indispensable** de partir d'un système propre est vierge. En effet, si quelque chose ne fonctionne pas c'est souvent parce qu'on a précédemment installé quelque chose d'incompatible en suivant sans comprendre un tuto de l'internet.
{% endnote %}

A la fin de ce tutoriel vous devez avoir :

* un système d'installation sain
* un gestionnaire de package
* un éditeur de texte

## Un nouveau compte

Si vous ne vous pouvez pas réinstaller un nouveau système, pour que tout se passe au mieux :

{% note %}
assurez vous que votre compte :

* soit un compte administrateur (pouvant exécuter sudo si vous êtes sous linux)
* votre nom de compte ne doit contenir **aucun** espace, ni accent.
{% endnote %}

## Un nouveau système

Il est souvent possible de réinstaller un nouveau système en conservant vos données. C'est souvent très pratique mais pour une première fois, je vous conseille de faire une installation sur un disque vierge, c'est à dire en ne **conservant rien** de ce qu'il y avait sur votre disque dur.

### Préparation

Installer un nouveau système nécessite de reformater votre disque dur. Avant cela il vous faut faire trois choses :

{% faire %}

* sauvegardez vos données sur une clé pour que vous puissiez facilement les remettre sur votre nouveau système
* vérifier les différentes applications actuellement installées et listez celles que vous voulez à nouveau installer.
* lister les différents compte et mots de passe dont vous aurez besoin (wifi, steam, google, ...)

{% endfaire %}

L'installation devra très certainement aller sur internet pour récupérer les données du système ou retrouver vous données sauvegardées sur le cloud ([icloud](https://support.apple.com/fr-fr/guide/icloud/welcome/icloud) sur mac ou [one drive](https://www.microsoft.com/fr-fr/microsoft-365/onedrive/online-cloud-storage) sous windows). POur que tout se passe au mieux :

{% faire %}

* notez le login et le mot de passe du cloud pour pouvoir y accéder lors de l'installation
* notez le nom de votre wifi et son mot de passe.
{% endfaire %}

### Installation

{% faire %}
Procédez à l'installation de votre système en suivant les recommandations ci-après.
{% endfaire %}

#### Sous mac

{% lien %}
<https://support.apple.com/fr-fr/guide/mac-help/mchlp1599/mac>
{% endlien %}

Le plus simple est d'installer une nouvelle version du système en utilisant internet. Redémarrez votre ordinateur en maintenant enfoncé les touches :  *"Maj + Option + Commande + R enfoncées"*

{% attention %}
Notez votre login et mot de passe icloud. Vous en aurez besoin à l'installation
{% endattention %}

Une fois votre système installé, il faudra également installer [xcode](https://apps.apple.com/fr/app/xcode/id497799835?mt=12). Prenez votre mal en patience, ça va prendre du temps...

#### Sous Windows

{% lien %}
<https://support.microsoft.com/fr-fr/windows/r%C3%A9installer-windows-d8369486-3e33-7d9c-dccc-859e2b022fc7>

En suivant les instructions de *Installer une nouvelle installation à l’aide d’un support d’installation*.
{% endlien %}

{% attention "**Recommendations :**"  %}

* Notez le numéro de série de votre windows. Vous en aurez besoin à l'installation
* utilisez un compte local et pas mon compte Microsoft pour me connecter
* Assurez vous que le nom de votre compte ne contient aucun espace ou accent (on le voit avec l'explorateur de fichier `c:\Utilisateurs`)
* Assurez vous que vous créez un compte administrateur.
{% endattention %}

## Premières configuration

{% faire %}
Procédez aux premières configuration pour finaliser l'installation minimale de votre système.
{% endfaire %}

### Sous mac { #configuration-sous-mac }

#### finder

Le finder est l'outil principal qui vous permettra de naviguer dans les fichiers. Pour qu'il soit un peut plus facile d'y naviguer :

{% faire "**pour un mac**" %}

* *menu présentation > personnaliser la barre d'outils...* ajoutez le "chemin" (trois barres horizontales) aux outils du finder en le glissant/déposant.
* ajoutez le dossier "*Départ*", aussi appelé "*maison*" (le dossier principal de l'utilisateur) et le dossier "*applications*" aux éléments à la gauche du finder. Pour cela, choisissez le dossier dans le menu *Aller* puis  avec l'outils chemin que l'on vient d'ajouter sélectionnez le dossier parent(Par exemple pour la maison, le dossier parent est "Utilisateurs" et pour application, le dossier parent est “Macintosh HD"). Vous pouvez ensuite glisser/déposer le dossier à gauche du finder.

{% endfaire %}

#### drivers mac

* icloud drive
* imprimante
* tablette graphique si vous en avez une

### Sous windows { #configuration-sous-mac }

#### Windows update

Vérifier que votre système est à jour :

{% faire "**pour un windows**" %}
Cliquez sur `Démarrer > Paramètres > mise à jour et sécurité > Windows update`
{% endfaire %}

#### drivers windows

* carte graphique
* clavier/souris si nécessaire
* imprimante

## Applications indispensables

{% faire %}
Il reste à installer trois applications indispensables pour une utilisation de votre système pour le développement :

* un navigateur internet
* un outils de compression/décompression de fichiers
* un éditeur de texte
* si vous êtes sous mac, un gestionnaire de packages

{% endfaire %}

### Un navigateur

Prenez celui de votre choix, personnellement j'utilise [chrome](https://www.google.com/intl/fr_fr/chrome/) que je mets en navigateur par défaut.

### Outils de compression pour windows

Compresser ou décompresser des fichiers est indispensable. Sous linux et mac un outil de compression est déjà installé, mais ce n'est pas le cas sous windows.

Il y en a plusieurs, mais je vous conseille :

{% faire "**pour un windows**" %}
d'installer [7zip](https://www.7-zip.org/) est simple d'utilisation et très complet.
{% endfaire %}

### Un éditeur de texte

On en installera d'autres par la suite, mais il est toujours appréciable d'avoir un éditeur de texte sous la main pour modifier rapidement un fichier de configuration.

Selon le système d'exploitation, mon éditeur à tout faire est différent :

* windows : j'utilise [notepad++](https://notepad-plus-plus.org/downloads/).
* mac : j'utilise [Textmate](https://macromates.com/).
* linux : [Atom](https://atom.io/)

### Un gestionnaire de package sous mac

N'installez **aucun logiciel unix** sous mac à la main. Utilisez toujours [brew](https://brew.sh/) pour le faire.

{% faire "**pour un mac**" %}
Installez [brew](https://brew.sh/)
{% endfaire %}

## Utilitaires de tous les jours

Non indispensable mais que vous utilisez tous les jours

* steam, gog, epic, battle.net, origin, u-play, etc
* vlc, office 360
* discord
* ...
