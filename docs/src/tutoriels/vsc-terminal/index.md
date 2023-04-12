---
layout: layout/post.njk

title: Vsc et terminal
tags: ['tutoriel', 'vsc', 'terminal', 'système']
authors: 
    - François Brucker

eleventyNavigation:
  key: "Vsc et terminal"
  parent: Tutoriels

  prerequis:
      - '../vsc-installation-et-prise-en-main/'
      - '../terminal/'
---

<!-- début résumé -->

Les différentes manières d'invoquer un terminal avec  [visual studio code](https://code.visualstudio.com/). C'est un condensé de la documentation officielle qui bien plus complète : <https://code.visualstudio.com/docs/editor/integrated-terminal>

<!-- fin résumé -->

## Palette de commande

Si vous tapez `>terminal` dans la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande), vous verrez toutes les commandes qui ont terminal dans leur nom. Il y a des commandes spécifiques à un langage (javascript, python, etc) et certaines très générales comme : *Open New External Terminal* qui ouvre un terminal dans le dossier de votre projet.

## <span id="terminal-intégré"></span> Intégration dans vscode

### Ouvrir un terminal

On peut ouvrir un terminal dans : *menu Affichage > Terminal*. Ce qui donne quelque chose du type :

![terminal dans vscode](./vsc-terminal.png)

Les différents panels du dessus du terminal (`PROBLEMES`, `OUTPUT`, `CONSOLE DE DEBOGAGE` et `TERMINAL`) dans vscode sont des sorties d'autres processus.

on reste donc 99% du temps sur `TERMINAL` (qui est en sur-brillance).

### Supprimer un terminal

On peut supprimer (en cliquant sur la poubelle) et créer (*menu Terminal > Nouveau terminal*) autant de terminal que l'on le veut. On peut aussi juste fermer la fenêtre du terminal en cliquant sur la croix.

### Créer un nouveau terminal

Notez bien que *menu Affichage > Terminal* ouvre le terminal courant, il n'en recrée pas un. C'est donc la commande à utiliser par défaut pour garder l'historique de ses commandes en utilisant la flèche du haut, qui remets la dernière commande utilisée.

Lorsque vous voulez créer un nouveau terminal, c'est dans *menu Terminal > Nouveau Terminal*.
