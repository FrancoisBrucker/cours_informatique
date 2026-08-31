---
layout: layout/post.njk

title: Interagir avec le système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un système est fait pour être utilisé. Il doit pour cela permettre :

- de stocker des données, 
- de permettre à différents utilisateurs d'utiliser l'ordinateur en toute sécurité,
- de facilité la vie aux utilisateur en leur permettant de lancer des application ou de modifier leur système de façon conviviale.

C'est ce que nous voir maintenant en voyant les principes qui sous-tendent ces mécaniques et comment on peut les utiliser au quotidien. 

## Fichiers et dossiers

{% aller %}
[Fichiers et Dossiers](fichiers-dossiers){.interne}
{% endaller %}

## Utilisateurs et droits

{% aller %}
[Utilisateurs et droits d'utilisation](./utilisateurs-droits){.interne}
{% endaller %}

## Organisation disque dur système

{% aller %}
[Organisation d'un disque système](./disque-système){.interne}
{% endaller %}

## Applications

D'un point de vue système, il existe des applications utiles à connaître pour pouvoir efficacement s'en server.

### Terminal

Le terminal permet d'exécuter rapidement des commandes. Il est fondamental que vous sachiez vous en servir

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

### Gestionnaire de paquet

{% aller %}
[Gestionnaire de paquets](gestionnaire-paquets){.interne}
{% endaller %}

### Applications utiles

Quelques applications sont indispensables pour utiliser son ordinateur pour le développement. Nous allons présenter ici les plus importantes, installées par défaut et que tout utilisateur doit avoir constamment sous la main.

#### Un navigateur

Il en existe de nombreux et tout système en a un par défaut ([edge](https://fr.wikipedia.org/wiki/Microsoft_Edge), [safari](<https://fr.wikipedia.org/wiki/Safari_(navigateur_web)>), [chrome](https://www.google.com/chrome/) ou [firefox](https://fr.wikipedia.org/wiki/Mozilla_Firefox)).

#### Un outil de compression/décompression de fichiers

Compresser ou décompresser des fichiers est indispensable. Un outil de compression est déjà installé pour les trois systèmes. Pour l'utiliser depuis un explorateur de fichier, il suffit de cliquer droit sur le dossier ou le fichier que vous voulez compresser et choisissez l'item `compresser` du menu.

#### Un éditeur de texte à tout faire

On a souvent besoin de lire ou d'éditer un fichier texte rapidement, que ce soit lire un readme, éditeur un fichier de configuration, corriger rapidement un faute dans un fichier Latex, etc.

Nous en donnons 3, un par système d'exploitation qui ont l'avantage d'être directement utilisable et qui possèdent une interface graphique.

{% details "sous Windows 11" %}
Je conseille d'installer [notepad++](https://notepad-plus-plus.org/)

{% enddetails %}
{% details "sous Macos" %}

J'aime utiliser l'éditeur [coteditor](https://coteditor.com/) pour les petites manipulations de fichiers.

{% enddetails %}
{% details "sous Linux/Ubuntu" %}
Par défaut, Ubuntu installe l'application `Éditeur de texte` qui permet d'éditer et de modifier des fichiers textes.

{% enddetails %}

#### Un IDE générique

Un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) permet de créer rapidement des projets. Il en existe de nombreux, allant du très générique au très particulier.

Actuellement, l'éditeur générique en vogue est [vscode](https://code.visualstudio.com/).

##  Bonus : Installation d'un nouveau système

{% aller %}
[Nouvelle installation d'un système](système-installation){.interne}
{% endaller %}

