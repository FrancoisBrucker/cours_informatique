---
layout: layout/post.njk 
title: Terminal

tags: ['tutoriel', 'système', 'terminal']
---

{% chemin %}
[Tutoriels]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}

<!-- début résumé -->

Qu'est-ce que le terminal ? Comment le trouver et taper des commandes.

<!-- fin résumé -->

## Introduction

Le terminal est l'outil utilisé pour taper des commandes qui seront ensuite exécutées par votre ordinateur. On appelle ça le [CLI](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande).

Même si cela est intimidant, le CLI est le moyen le plus efficace d'interagir avec votre ordinateur car, contrairement aux applications :

* on peut ajouter des paramètres aux instructions
* on gère facilement les entrées et les sorties des commandes
* c'est automatisable par des scripts.

Enfin, c'est souvent la seule façon d'interagir avec un ordinateur distant.

Vous pouvez a priori utiliser votre ordinateur uniquement avec un terminal. L'interface graphique n'est qu'un ajout sympathique mais non indispensable à l'utilisation d'un ordinateur. Alors bien sur vous n'utiliserez pas le terminal tout le temps mais savoir s'en servir pourra vous faire gagner un temps fou lorsque vous faites de l'informatique.

{% info %}
Utiliser le terminal vous procure en plus ce petit sentiment grisant d'[être en prise directe avec la matrice](https://www.youtube.com/watch?v=MvEXkd3O2ow).
{% endinfo %}

## Accéder au terminal

### Via l'éditeur

La plupart des éditeurs de textes permettent d'ouvrir directement des terminaux. Si vous utilisez [vscode](https://code.visualstudio.com/) par exemple, vous pouvez directement ouvrir un terminal (voir [le tuto](../vsc-terminal/vsc-terminal.md %})).

### Via une application

Selon votre système d'application, le terminal va se trouver à des endroits différents :

{% details "sous linux" %}

[Tuto pour Ubuntu](https://doc.ubuntu-fr.org/terminal)

{% enddetails %}

{% details "sous mac" %}
Le [terminal](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) se trouve dans le dossier `/Application/utilitaires`{.fichier}

Avec le `finder` :

1. *menu Aller*,
2. dans ce menu choisissez "utilitaires",
3. une nouvelle fenêtre `finder` apparaît : double-cliquez sur l'icône "Terminal".

Une fois dans l'application `Terminal` vous pouvez ouvrir une nouvelle fenêtre dans le menu *Shell > Nouvelle Fenêtre > Nouvelle fenêtre avec le profil - ...* (les "..." correspondent à votre profil de fenêtre).

{% enddetails %}

{% details "sous windows" %}

Le terminal s'appelle *powershell* sous w10.

Pour ouvrir une fenêtre powershell, cliquez droit sur le drapeau windows tout à gauche de la barre des tâches puis choisissez d'ouvrir une fenêtre powershell (ce n'est pas la peine qu'elle soit en mode administrateur)

Il existe une autre sorte de terminal sous windows, *l'invite de commande*. Pour la lancer tapez `cmd` dans la barre de recherche (juste à droite du drapeau windows tout à gauche de la barre des tâches) puis appuyez sur la touche entrée.

{% attention %}
N'utilisez pas l'invit de commande (`cmd`), qui n'a pas évolué depuis les années 80. Y taper des commandes est un vrai calvaire.

Les commandes utilisables sous l'invite de commandes et powershell sont différentes. Donc si vous suivez un tutos vérifiez bien qu'il est compatible avec powersell.
{% endattention %}

{% enddetails %}

{% note %}
Le terminal est super utile, ça vaut le coup d'ajouter un raccourci pour lui, histoire de l'avoir toujours sous la main.
{% endnote %}

## Utiliser le terminal

Maintenant que vous avez trouvé le terminal, ouvrez une fenêtre terminal. Vous êtes devant ce qu'on appelle un *prompt*. On attend que vous tapiez des commandes. Ces commandes peuvent être de 2 types :

* soit des noms de fichiers qui sont *exécutables* (ce sont des programmes)
* soit des instructions compréhensibles par le terminal comme `ls` par exemple.

{% note %}
C'est simple à utiliser. On tape une commande, on appuie sur entrée et la commande s'exécute.
{% endnote %}

Si vous voulez plus de renseignements sur la navigation et l'exécution de fichiers, vous pouvez suivre [ce tuto](../terminal-utilisation)

## Autres tutos

* windows powershell : <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
* l'application terminal sous mac : <https://support.apple.com/fr-fr/guide/terminal/welcome/mac>
* utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
