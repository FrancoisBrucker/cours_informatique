---
layout: layout/post.njk

title: Interagir avec le système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un système est fait pour être utilisé.
> TBD pour l'instant OS = exécution de programmes en parallèle et accès aux devices 
> il reste 3 choses :
> 1. données
> 2. qui les utilise (séparer le système d'un utilisateur normal et plusieurs utilisateurs)
> 3. comment les utiliser : application et terminal

- dossier / fichier
- application utiles
- terminal
- installation nouveau système optionnel.

## Fichiers et dossiers

{% aller %}
[Fichiers et Dossiers](fichiers-dossiers){.interne}
{% endaller %}

## Utilisateurs et droits

{% aller %}
[Utilisateurs et droits d'utilisation](./utilisateurs-droits){.interne}
{% endaller %}
 
## Organisation disque dur système

> TBD reprendre dans la partie refactor.
> TBD montrer les système de fichiers (FAT vs extfs ou nfat, ...)
> TBD système / applications / utilisateur /
> TBD montrer une partition d'un disque dur
> partie cachée (bootloader) pour le noyau.
> dans la partie refactor.
> donner la commande unix et une copie d'écran windows.

## Applications

> TBD utiles pour administrer et utiliser efficacement un système

### Terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

### Gestionnaire de paquet 
> TBD à déplacer de système installation

### Applications utiles
> TBD à déplacer de système installation


##  Bonus : Installation d'un nouveau système

{% aller %}
[Nouvelle installation d'un système](système-installation){.interne}
{% endaller %}

