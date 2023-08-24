---
layout: layout/post.njk

title: Sous-système Windows pour Linux (WSL)

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Sous-système Windows pour Linux (WSL, Windows System for Linux)](https://learn.microsoft.com/fr-fr/windows/wsl/) est un moyen simple d'installer Linux sur un ordinateur disposant de Windows 11, car il permet de faire cohabiter les deux systèmes en une même session.

Si vous voulez apprendre ou utiliser Linux à son plein potentiel il est mieux d'installer Linux/Ubuntu sur un système à part, mais pour débuter ; se familiariser avec les commandes ou créer des applications Linux c'est un bon point de départ.

## Procédure d'installation

Nous allons suivre les instruction de la [page d'installation de la WSL de Microsoft]((https://learn.microsoft.com/fr-fr/windows/wsl/install)).

### Prérequis

Pour pouvoir installer la wsl, il faut que votre système ait quelques options d'installées :

Dans la barre de recherche, tapez `fonctionnalités` pour accéder aux fonctionnalités windows :

![fonctionnalités Windows](fonctionnalités.png)

Une fois l'application lancée, cochez les fonctionnalités suivantes pour les activer :

* "hyper-V"
* "Plateforme machine virtuelle"
* "sous-système windows pour Linux"

![fonctionnalités à activer](fonctionnalités-wsl.png)

### Installation

Dans un terminal tapez la commande :

```
wsl --install -s ubuntu
```

Pour installer une distribution Linux/Ubuntu. Pour le login, choisissez le même que celui de l'école/fac.

## Exécuter un terminal Linux

Accéder au système Linux se fait via un terminal Linux. Il y a deux moyens de le faire.

### Via un terminal powershell

Vous pouvez exécuter un terminal Linux depuis un terminal powershell en tapant la commande `wsl` :

![wsl powershell](wsl-powershell.png)

### Via le menu terminal épinglé

Sur l'onglet terminal épinglé, en choisissant la ligne `ubuntu` :

![wsl menu épinglé](wsl-menu-épinglé.png)

## Application graphique

A priori, les applications graphiques (X11) de Linux sont directement utilisables avec la WSL.

Vous pouvez suivre [ce tutoriel](https://learn.microsoft.com/fr-fr/windows/wsl/tutorials/gui-apps) pour vérifier que tout est ok, mais ça devrait être le cas par défaut.
