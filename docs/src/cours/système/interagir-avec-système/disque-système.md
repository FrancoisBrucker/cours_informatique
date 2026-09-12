---
layout: layout/post.njk

title: Organisation d'un disque système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD montrer une partition d'un disque dur

Le disque dur du système a une structure particulière car il doit :

- permettre l'exécution du noyau
- contenir les divers fichiers et application du système


L'organisation de cette structure est différente selon les OS mais on retrouvera toujours ces éléments.

## Bootloader et partitions

Lorsque l'on démarre un ordinateur, il faut commencer par trouver le noyau du système d'exploitation appelé **_bootloader_**. Le bootloader et le noyau se trouvent dans [une partition spéciale](https://fr.wikipedia.org/wiki/Partition_(informatique)) du disque dur de démarrage.

{% note2 "**Définition**" %}
[Une **_partition_**](https://fr.wikipedia.org/wiki/Partition_(informatique)) est une partie d'un disque dur. 
{% endnote2 %}

Un disque dur système possédera toujours au moins 2 partitions :

- celle du bootloader qui est toute petite et contient uniquement le noyau
- une partition plus grande contenant le reste du système

Il peut en avoir bien plus : certains système ont ainsi une partition réservée aux utilisateur, une autre pour les applications, etc. La raison est que les partitions sont isolées les unes des autres, en casser une ne détruit pas les autres par exemple.


## Dossiers système

Si le noyau du système se trouve sur la partition du _bootloader_, tout le reste du système se trouve sur la partition principale dans un au plusieurs dossiers. 

L'organisation spécifique de ces dossiers dépend du système d'exploitation, par exemple sous windows presque tout est rangé dans le dossier `\system`{.fichier} alors que sous Linux le système est réparti dans plusieurs dossiers. En revanche, on retrouvera toujours les même composants suivant.

### Fonctionnement interne du système

Répartis dans plusieurs dossiers et contient tous les fichiers nécessaires au bon fonctionnement du système :

- les fichiers de configurations
- les applications système (comme systemd sous linux par exemple)
- [les bibliothèques dynamiques](https://fr.wikipedia.org/wiki/Dynamic_Link_Library)

### Applications

Dossier contenant les applications reconnues par le système. Si vous installez un logiciel dans un dossier différent il se peut qu'il ne soit pas automatiquement reconnu.

## Dossiers Utilisateurs

Un dossier spécifique à chaque utilisateur, aussi appelé **_Maison_**. Il va contenir tous ses fichiers de données, mais également :

- ses fichiers de configuration
- ses programmes

## Disques de données

Outre le disque système, un ordinateur peut posséder de nombreux autres disques soit fixe, soit amovibles (comme des clés usb).
