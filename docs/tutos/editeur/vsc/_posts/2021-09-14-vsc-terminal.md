---
layout: page
title:  "vsc et terminal"
categories: 
    - installation 
    - configuration
    - terminal
---

Les différentes manières d'invoquer un terminal avec  [visual studio code](https://code.visualstudio.com/) (vsc)
<!--more-->

## terminal

> <https://code.visualstudio.com/docs/editor/integrated-terminal>

Le [terminal]({% post_url tutos/systeme/2021-08-24-terminal %}) est le meilleur ami du développeur. Il faut pouvoir créer un temrinal très rapidment, et à l'endroit où l'on veut. Vscode permet de faire ça et de multiples façons.

## palette de commande

Si vous tapez *">terminal"* dans la [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande), vous verrez toutes les commandes qui ont temrinal dans leur nom. Il y a des commandes spécifiques à un langage (javascript, python, etc) et certaines très générales comme : *Open New External Terminal* qui ouvre un terminal dans le dossier de votre projet.

## intégration dans vscode {#terminal-integre}

On peut aussi ouvrir un terminal Directement dans node : *"menu Affichage > Terminal"*. Ce qui donne quelque chose du type :

![terminal dans vscode]({{ "/assets/cours/web/numerologie/vsc-terminal.png" | relative_url }}){:style="margin: auto;display: block"}

Les différents panels du dessus du terminal (PROBLEMeES, OUTPUT, CONSOLE DE DEBOGAGE et TERMINAL) dans vscode sont des sorties d'autres processus.

on reste donc 99% du temps sur *TERMINAL* (qui est en sur-brillance).

> On peut supprimer (en cliquant sur la poubelle) et créer (*menu Terminal > Nouveau terminal*) autant de terminal que l'on le veut. On peut aussi juste fermer la fenêtre du terminal en cliquant sur la croix.

Notez bien que  *"menu Affichage > Terminal"* ouvre le terminal courant, il n'en recrée pas un. C'est donc la commande à utiliser par défaut pour garder l'historique de ses commandes en utilisant la flèche du haut, qui remets la dernière commande utilisée. Lorsque vous voulez recréer un terminal, c'est dans *menu Terminal > Nouveau Terminal*.
