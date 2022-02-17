---
layout: page
title:  "Projet numérologie : partie 1 / niveau 1 / préparation"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/index.md %}) / [préparation]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/1-preparation.md %})
{: .chemin}

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons tous les outils nécessaires.

## outils

D'après les [prérequis du projet]({% link cours/web/projets/numerologie/index.md %}#prérequis), vous avez :

* [vscode](https://code.visualstudio.com/)
* [node](https://nodejs.org/en/) que vous pouvez exécuter dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %})

## projet

Commencez par vos familiariser avec vscode si ce n'est déjà fait grâce à [ce tutoriel]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}). On supposera par la suite que vous avez lu et fait les installations de ce tutoriel.

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle *workspace*.

1. Commencez par créer le dossier *"numerologie"*
2. dans vscode, choisissez : "*Menu File > open*" puis naviguez jusqu'à votre dossier *"numerologie"*. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

> Lorsque l'on code et que l'on ne veut pas de problèmes en développement, les noms de fichiers doivent êtres sans espaces et sans accents.

On va créer notre premier fichier javascript : *menu Fichier > Nouveau Fichier* et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom *"mes_tests.js"*.

Vscode à compris que c'était du javascript, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)). Commençons notre voyage dans le monde merveilleux de la programmation web serveur, en écrivant notre premier programme javascript dans le fichier *"numerologie/"mes_tests.js" :

```javascript
nom = "monde"

console.log("bonjour " + nom + " !")
```

> Puis sauvez le fichier (*menu Fichier > Enregistrer*).
{: .note}

### exécution du code

Tapez ">terminal" dans la [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande) (*menu Affichage >  Palette de commandes...*)/ et choisissez la commande *Open New External Terminal*.

Un nouveau terminal s'ouvre directement dans le dossier de votre projet. Magique non ?

>On peut Maintenant exécuter notre fichier en tapant dans ce nouveau terminal : `node mes_tests.js`.
{: .note}

N'oubliez pas non plus le [termnial de vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre), ouvrez le (*"menu Affichage > Terminal"*) et exécutez votre code comme précédemment..
