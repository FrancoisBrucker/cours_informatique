---
layout: page
title:  "Projet numérologie : niveau 1/partie 1/préparation"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})/[niveau 1]({% link cours/web/projets/numerologie/niveau-1/index.md %})/[partie 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/index.md %})/[préparation]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/1-preparation.md %})
{: .chemin}

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons tous les outils nécessaires.

## outils

D'après les [prérequis du projet]({% link cours/web/projets/numerologie/index.md %}#prérequis), vous avez :

* [vscode](https://code.visualstudio.com/)
* [node](https://nodejs.org/en/) que vous pouvez exécuter dans un [terminal]({% post_url tutos/systeme/2021-08-24-terminal %})

## projet

### workspace

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle *workspace*.

1. Commencez par créer le dossier *"numerologie"*
2. dans vscode, choisissez : "*Menu File > open*" puis naviguez jusqu'à votre dossier *"numerologie"*. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

> Lorsque l'on code et que l'on ne veut pas de problèmes, les noms de fichiers doivent êtres sans espaces et sans accents.

Vous devez obtenir quelque chose du style :
![projet vide]({{ "/assets/cours/web/numerologie/vsc-projet-vide.png" | relative_url }}){:style="margin: auto;display: block"}

## vscode le tour du propriétaire

Nous venons de créer un nouveau projet, que vscode appelle un [workspace](https://code.visualstudio.com/docs/editor/workspaces#_how-do-i-open-a-vs-code-workspace).

> Un *workspace* dans vscode est un endroit pour lequel on peut avoir ses propres préférences et spécificités.  

Sur la gauche de la fenêtre vscode, le menu vous permet de choisir une icône qui correspond (de haut en bas) :

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

![extensions vscode]({{ "/assets/cours/web/numerologie/vsc-extensions.png" | relative_url }}){:style="margin: auto;display: block"}

> Félicitations : votre vscode est en français maintenant. Ses menus sont devenus : *Fichier*, *Edition*, *Sélection*, *Affichage*, *Atteindre*, *Exécuter*, *Terminal*, *Fenêtre* et *Aide*.

### barre de statut

> Créez un nouveau fichier *menu Fichier > Nouveau Fichier* et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom *"mes_tests.js"*.
{: .note}

Vscode à compris que c'était du javascript, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)).

La barre de statut est très utile, elle regroupe plein d'infos relative au fichier courant :

* où on est : Ln 1; Col 1
* l'[encodage des caractères](https://www.w3.org/International/questions/qa-what-is-encoding.fr) : [UTF-8](https://fr.wikipedia.org/wiki/UTF-8). Vous ne **devez jamais** avoir autre chose lorsque vous écrivez du texte.
* l'[encodage des fin de ligne](https://fr.wikipedia.org/wiki/Fin_de_ligne) : LF (sous unix/mac) ou CRLF (sous windows). On ne s'en occupe pas trop, vscode gère tout ça pour nous
* le langage : ici javascript
* d'autres trucs selon les extensions que vous avez ajouté.

## premier programme javascript

Commençons notre voyage dans le monde merveilleux de la programmation web serveur, en écrivant notre premier programme javascript dans le fichier *"numerologie/"mes_tests.js" :

```javascript
nom = "monde"

console.log("bonjour " + nom + " !")
```

> Puis sauvez le fichier (*menu Fichier > Enregistrer*).
{: .note}

### exécution dans le terminal

Ce qu'il y a de bien avec vscode c'est que toute commande est aussi appelable par son nom grâce à la [palette de commande](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) : *menu Affichage >  Palette de commandes...*. Vous pouvez taper "save" par exemple pour voir toutes les commandes qui contiennent save, dont celle qui sauve des fichiers *File: Save*. C'est super utile pour trouver une commande dont ne peut que deviner le nom.

> le nom des commandes est en anglais. Tapez donc des mots anglais dans la palette de commandes. Les différentes commandes seront listées sur deux lignes  la première — en Français — décrivant la commande, et la seconde — en anglais — donnant le nom de la commande.
{: .attention}

Les commandes de la palette de commande sont accessible si la ligne commence par un ">". S'il y a un "?" c'est l'aide et s'il n'y a retrouve des fichiers ouverts. Par exemple :

> tapez dans la palette ">terminal".
{: .note}

Il doit y avoir une commande s'appelant *Open New External Terminal". Choisissez là et appuyez sur entrée pour l'exécuter. Un nouveau terminal s'ouvre directement dans le dossier de votre projet. Magique non ?

>On peut Maintenant exécuter notre fichier en tapant dans ce nouveau terminal : `node mes_tests.js`.
{: .note}

On peut aussi ouvrir un terminal Directement dans node : *"menu Affichage > Terminal"*.

![terminal dans vscode]({{ "/assets/cours/web/numerologie/vsc-terminal.png" | relative_url }}){:style="margin: auto;display: block"}

Les différents panels du dessus du terminal (PROBLEMeES, OUTPUT, CONSOLE DE DEBOGAGE et TERMINAL) dans vscode sont des sorties d'autres processus dont on a pas besoin pour l'instant : on reste donc sur *TERMINAL* (qui est en sur-brillance).

> On peut supprimer (en cliquant sur la poubelle) et créer (*menu Terminal > Nouveau terminal*) autant de terminal que l'on le veut. On peut aussi juste fermer la fenêtre du terminal en cliquant sur la croix.

Notez bien que  *"menu Affichage > Terminal"* ouvre le terminal courant, il n'en recrée pas un. C'est donc la commande à utiliser par défaut pour garder l'historique de ses commandes en utilisant la flèche du haut, qui remets la dernière commande utilisée.

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
