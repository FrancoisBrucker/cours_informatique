---
layout: page
title:  "vsc et terminal"
tags: 
    - installation 
    - configuration
    - terminal
---

Utiliation du terminal avec vscode

<!--more-->

> prérequis
>
>* [vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %})
>* [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %})
>
{: .chemin}

Les différentes manières d'invoquer un terminal avec  [visual studio code](https://code.visualstudio.com/). C'est un condensé de la documentation officielle qui bien plus complète : <https://code.visualstudio.com/docs/editor/integrated-terminal>

<!--more-->

## palette de commande

Si vous tapez *">terminal"* dans la [palette de commande]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#palette-de-commande.md), vous verrez toutes les commandes qui ont terminal dans leur nom. Il y a des commandes spécifiques à un langage (javascript, python, etc) et certaines très générales comme : *Open New External Terminal* qui ouvre un terminal dans le dossier de votre projet.

## intégration dans vscode {#terminal-integre}

### ouvrir un terminal

On peut ouvrir un terminal dans le menu : *"Affichage > Terminal"*. Ce qui donne quelque chose du type :

![terminal dans vscode]({{ "/assets/tutos/vsc-projets/vsc-terminal.png" | relative_url }}){:style="margin: auto;display: block"}

Les différents panels du dessus du terminal (PROBLEMES, OUTPUT, CONSOLE DE DEBOGAGE et TERMINAL) dans vscode sont des sorties d'autres processus.

on reste donc 99% du temps sur *TERMINAL* (qui est en sur-brillance).

### supprimer un terminal

On peut supprimer (en cliquant sur la poubelle) et créer (*menu Terminal > Nouveau terminal*) autant de terminal que l'on le veut. On peut aussi juste fermer la fenêtre du terminal en cliquant sur la croix.

### créer un nouveau terminal

Notez bien que *"menu Affichage > Terminal"* ouvre le terminal courant, il n'en recrée pas un. C'est donc la commande à utiliser par défaut pour garder l'historique de ses commandes en utilisant la flèche du haut, qui remets la dernière commande utilisée.

Lorsque vous voulez créer un nouveau terminal, c'est dans *menu Terminal > Nouveau Terminal*.
