---
layout: layout/post.njk

title: Organisation d'un disque système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lorsque l'on démarre un ordinateur, [on a vu](../../but/#démarrage){.interne} qu'est chargé le bootloader qui permet de charger le noyau. Ces deux éléments doivent être lues sur un des disque dur de l'ordinateur et font partie du système d'exploitation. De plus un système va avoir besoin de tout un tas de fichiers de configurations et d'un endroit où il va ranger les différents logiciels qu'il utilisera. 

L'organisation de cette structure est différente selon les OS mais on retrouvera toujours ces éléments.


## Fichiers système

### Bootloader et noyau

Le bootloader et le noyau se trouvent dans [une partition spéciale](https://fr.wikipedia.org/wiki/Partition_(informatique)) du disque dur de démarrage.

### Dossier système

Va contenir tous les fichiers nécessaires au bon fonctionnement du système :

- les fichiers de configurations
- les applications système (comme systemd sous linux par exemple)
- [les bibliothèques dynamiques](https://fr.wikipedia.org/wiki/Dynamic_Link_Library)

### Application

Dossier contenant les applications reconnues par le système. Si vous installez un logiciel dans un dossier différent il se peut qu'il ne soit pas automatiquement reconnu.

## Dossiers Utilisateurs

Un dossier spécifique à chaque utilisateur. Il va contenir tous ses fichiers de données, mais également :

- ses fichiers de configuration
- ses programmes

## Disques de données

Outre le disque système, un ordinateur peut posséder de nombreux autres disques soit fixe, soit amovibles (comme des clés usb)
