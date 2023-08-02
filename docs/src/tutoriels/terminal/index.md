---
layout: layout/post.njk

title: Terminal
tags: ['tutoriel', 'système', 'terminal']
authors:
    - François Brucker

eleventyNavigation:
    prerequis:
        - "../fichiers-navigation/"


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Tutoriels
---

Qu'est-ce que le terminal ? Comment le trouver et taper des commandes.

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

Il y plusieurs moyen d'accéder à l'application terminal.

### Via des menus

{% details "sous Windows 11" %}

Dans le menu démarrer choisissez `toutes les applications` en haut à droite de la fenêtre. Le terminal est à la lettre `T` :

![terminal sous windows](powershell-menu-démarrer.png)

Le terminal s'appelle aussi parfois [powershell](https://learn.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.3), à ne pas confondre avec *l'invite de commande* (commande `cmd`) qui est là pour des raisons de compatibilités mais qu'il ne faut jamais utiliser soit même.

{% enddetails %}
{% details "sous Macos" %}

[l'aide de Mac](https://support.apple.com/fr-fr/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac) pour trouver le terminal.

L'application se trouve dans le dossier `/Application/utilitaires`{.fichier} que l'on peut facilement atteindre avec le `finder` :

1. `menu Aller > utilitaires``
2. une nouvelle fenêtre `finder` apparaît : double-cliquez sur l'icône "Terminal".

Une fois dans l'application `Terminal` vous pouvez ouvrir une nouvelle fenêtre dans le menu *Shell > Nouvelle Fenêtre > Nouvelle fenêtre avec le profil - ...* (les "..." correspondent à votre profil de fenêtre).

{% enddetails %}

{% details "sous Linux/Ubuntu" %}
Rechercher terminal dans les applications :

![trouver le terminal](ubuntu-terminal-open.png)

Vous pouvez aussi utiliser le raccourci clavier clobal `<CTRL> + <ALT> + T` :

{% enddetails %}

### <span id="explorateur"></span>Via l'explorateur de fichier

L'[explorateur de fichier](../fichiers-navigation/#explorateur) est un moyen simple d'accéder à un terminal directement placé dans le dossier voulu.

{% details "sous Windows 11" %}

Dans l'explorateur cliquez droit sur le dossier, puis choisissez `Ouvrir dans le Terminal` :

![trouver le terminal Macos](./windows-terminal-open.png)

{% enddetails %}
{% details "sous Macos" %}

Dans le finder cliquez droit sur le dossier, puis choisissez `services > Nouveau terminal au dossier` :

![trouver le terminal Macos](Macos-terminal-open.png)

{% enddetails %}

{% details "sous Linux/Ubuntu" %}

Cliquer croit sur un dossier dans l'explorateur et choisissez `Open in Terminal` :

![trouver le terminal Linux/Ubuntu](ubuntu-terminal-open.png)

{% enddetails %}

### Via un IDE

La plupart des éditeurs de textes permettent d'ouvrir directement des terminaux. Si vous utilisez [vscode](https://code.visualstudio.com/) par exemple, vous pouvez directement ouvrir un terminal (voir [le tuto](../vsc-terminal){.interne}).

## Épingler le terminal

{% note %}
Le terminal est super utile, ça vaut le coup d'ajouter un raccourci pour lui, histoire de l'avoir toujours sous la main.
{% endnote %}
{% details "sous Windows 11" %}
Cliquer droit sur l’icône terminal dans la barre des taches et cliquer sur `Épingler à la barre des tâches` :

![épingler](powershell-fenêtre-épingler.png)
{% enddetails %}
{% details "sous Macos" %}
Avec une fenêtre finder dans le dossier `Applications/Utilitaires` glisser/déposez l’icône du terminal dans la barre des tâches.
{% enddetails %}
{% details "sous Linux/Ubuntu" %}
Cliquer droit sur l’icône terminal dans la barre des taches et cliquer sur `add to favorites`:

![add to favorites](./ubuntu-terminal-favoris.png)
{% enddetails %}

## Utiliser le terminal

Maintenant que vous avez trouvé le terminal, ouvrez une fenêtre terminal. Vous êtes devant ce qu'on appelle un *prompt*. On attend que vous tapiez des commandes.

{% note %}
C'est simple à utiliser. On tape une commande, on appuie sur entrée et la commande s'exécute.
{% endnote %}

Ces commandes peuvent être de 2 types :

* soit des noms de fichiers qui sont *exécutables* (ce sont des programmes)
* soit des instructions compréhensibles par le terminal comme `ls` par exemple.

{% aller %}
[Utiliser le terminal](../terminal-utilisation){.interne}
{% endaller %}
