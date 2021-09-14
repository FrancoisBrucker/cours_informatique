---
layout: page
title:  "Installation et prise en main de vscode"
categories: 
    - installation 
    - configuration
---


Installation et premières configurations de [visual studio code](https://code.visualstudio.com/) (vsc).
<!--more-->

## Introduction

Si vous ne l'avez pas déjà fait, téléchargez [vscode](https://code.visualstudio.com/) le et installez le.

vscode permet, comme dans tout éditeur de texte, d'éditer et de créer des fichiers texte mais aussi de gérer des *workspace* qui sont des dossiers contenant des projets.

Ces projets peuvent être de natures diverses, comme des projts web, du python, des rapports, etc. 

Pour ce tutoriel, vous allez :

1. commencez par créer un dossier que vous appellerez *"premier-projet-vsc"* avec votre explorateur de fichier,
2. dans vscode, choisissez : "*menu File > open*" puis naviguez jusqu'à votre dossier *"premier-projet-vsc"*. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

Vous devez obtenir quelque chose du style (pris sous mac mais ça devrait être quasi-pareil sous linux et windows) :
![vsc-depart]({{ "/assets/tutos/vsc-projets/premier-projet.png" | relative_url }}){:style="margin: auto;display: block;width: 500px"}

## tour du propriétaire

Nous venons de créer un nouveau projet, que vscode appelle un [workspace](https://code.visualstudio.com/docs/editor/workspaces#_how-do-i-open-a-vs-code-workspace).

> Un *workspace* dans vscode est un endroit pour lequel on peut avoir ses propres préférences et spécificités.  

La barre d'activité de la fenêtre vscode (les icônes sur la gauche de la fenêtre), vous permet de choisir une icône qui correspond (de haut en bas) :

* aux fichiers et sous-dossiers de votre workspace (pour l'instant il n'y a rien)
* à une recherche de texte dans votre projet
* à la gestion des sources
* au débogage
* à la gestion des extensions de vscode
* à la gestion des comptes
* aux préférences de vscode

>Les différentes parties de l'interface de la fenêtre  vscode est expliquée [dans la doc](https://code.visualstudio.com/docs/getstarted/userinterface).

Vous devriez aussi avoir un onglet ouvert qui s'appelle *welcome*. Vous pouvez la fermer en cliquant sur la croix à droite de son nom.

### installation d'extensions

Pour l'instant vscode nous parle anglais. Remédions tout de suite à cela en installant le pack français.

1. cliquez sur l'icône de gestion des extensions ou *menu View > Extensions*.
2. dans la barre de recherche, tapez *French Language Pack for Visual Studio Code*
3. cliquez sur l'application correspondante (ça devrait être la première)
4. un onglet détaillant l'extension est apparu  : cliquez sur install pour l'installer. vscode va se redémarrer en français.

![extensions vscode]({{ "/assets/tutos/vsc-projets/vsc-extensions.png" | relative_url }}){:style="margin: auto;display: block"}

> Félicitations : votre vscode est en français maintenant. Ses menus sont devenus : *Fichier*, *Edition*, *Sélection*, *Affichage*, *Atteindre*, *Exécuter*, *Terminal*, *Fenêtre* et *Aide*.

### barre de statut

> Créez un nouveau fichier *menu Fichier > Nouveau Fichier* et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom *"hello.txt"*.
{: .note}

Vscode à compris que c'était du texte, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)).

La barre de statut est très utile, elle regroupe plein d'infos relative au fichier courant :

* où on est : Ln 1; Col 1
* l'[encodage des caractères](https://www.w3.org/International/questions/qa-what-is-encoding.fr) : [UTF-8](https://fr.wikipedia.org/wiki/UTF-8). Vous ne **devez jamais** avoir autre chose lorsque vous écrivez du texte.
* l'[encodage des fin de ligne](https://fr.wikipedia.org/wiki/Fin_de_ligne) : LF (sous unix/mac) ou CRLF (sous windows). On ne s'en occupe pas trop, vscode gère tout ça pour nous
* le langage : ici texte brut
* d'autres trucs selon les extensions que vous avez ajouté.

### dictionnaire

Ecrivons du texte dans notre fichier (l'onglet nommé *"hello.txt"*) :

```text

Bnjour Monde !
```

Puis sauvez le fichier (*menu Fichier > Enregistrer*).

> Si vous fermez malencontreusement votre onglet (en cliquant sur la croix à droite du nom), vous pouvez toujours retrouver ce fichier en ouvrant l'explorateur (*menu Affichage > Explorateur*, ou en cliquant sur la 1ère icône de la barre d'activité) et en sélectionnant le fichier.

Félicitations, vous venez d'écrire votre premier texte en vscode avec un grosse faute de français !

Bon, c'est pas trop de notre faute vu que c'tait pas souligné en rouge. Remédions à cela en ajoutant un dictionnaire à vscode : installez l'extension [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright) qui ajoute un correcteur orthographique à vscode.

Ouf, "Bnjour" est bien souligné en rouge. Si vous allez dessus avec le curseur, une ampoule jaune va apparaitr : Elle va vous proposer "Bonjour".

> Vous pourrez ajouter les mots nouveaux soit au dictionnaire de l'utilisateur (*user*), soit juste pour ce projet (*workspace*).

### palette de commande {#palette-de-commande}

Ce qu'il y a de bien avec vscode c'est que toute commande est aussi appelable par son nom grâce à la [palette de commande](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) : *menu Affichage >  Palette de commandes...*. Vous pouvez taper "save" par exemple pour voir toutes les commandes qui contiennent save, dont celle qui sauve des fichiers *File: Save*. C'est super utile pour trouver une commande dont ne peut que deviner le nom.

> le nom des commandes est en anglais. Tapez donc des mots anglais dans la palette de commandes. Les différentes commandes seront listées sur deux lignes  la première — en Français — décrivant la commande, et la seconde — en anglais — donnant le nom de la commande.
{: .attention}

Les commandes de la palette de commande sont accessible si la ligne commence par un ">". S'il y a un "?" c'est l'aide et s'il n'y a retrouve des fichiers ouverts. 

Par exemple : taper *>spellright* dans la palette de commande. Toutes les commandes relatives au dictionnaire (extesion *spellright*) sont disponibles. En particulier le choix de la langue.

### vscode, les préférences : sauvegarde automatique

La [documentation de vscode sur les préférences](https://code.visualstudio.com/docs/getstarted/settings) est très bien faite. On retiendra que l'on peut avoir des préférences différentes par "utilisateur" (*user*) ou par "espace de travail" (*workspace*).

> Le fichiers stockant des préférences utilisateurs [dépend du système d'exploitation](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations), si vous modifiez des préférences pour l'espace de travail, undossier *".vscode"* sera créé à la racine de votre projet, et il contiendra un fichier *"settings.json"* contenant les différentes préférences.

Personnellement, s'il y a bien une chose qui m'ennuie c'est de constamment sauver mes fichiers. Si je fais une modification de mes fichiers, c'est parce que j'en ai besoin je ne vois pas l'intérêt de devoir sauver pour confirmer. Heureusement, vscode permet (comme tout éditeur qui se respecte) de faire ça en modifiant ses préférences :

> Allez dans les préférences de vscode : *icône engrenage (en bas à gauche de la fenêtre vscode) > Paramètres*.
{: .note}

Un onglet nommé *Paramètre* s'ouvre Il contient :

* une barre de recherche
* deux panels : *Utilisateur* et *Espace de travail*. Par défaut, on est positionné sur *Utilisateur* (c'est en sur-brillance).

>Dans le panel *Utilisateur* choisissez *Editeur de texte > Fichiers* puis cherchez *Auto Save*.
{: .note}

On peut ensuite régler ce paramètre sur *afterDelay* puis changer le délai dans le champ *Auto Save Delay*. J'ai mis 5000, ce qui fait qu'après 5 secondes de repos mon fichier est sauvé automatiquement.

> On aurait pu aussi taper "auto save" dans la barre de recherche pour obtenir directement les champs possibles. Ce qui est très pratique lorsque l'on se doute du nom du paramètre que l'on veut changer.

Le paramètre d'*Auto Save* dans le panel *Espace de travail* devrait toujours être sur *off*. Si vous le modifiez, un dossier de préférence *".vscode"* va être créé dans votre projet.


## pour aller plus loin

> TBD : autres tutos
{: .note}

* markdown
* python : linter, black et compagnie.
* git et merge (?)


