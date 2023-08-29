---
layout: layout/post.njk

title: Post installation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Que faire juste après l'installation de Linux/Ubuntu

## Mise à jour des paquets

Dans un terminal, vous pouvez tapez les commandes :

* `sudo apt update`{.language-} pour mettre à jour la liste des paquets ubuntu disponibles
* `sudo apt upgrade`{.language-} pour mettre à jour les paquets ubuntu installés
* `sudo snap refresh`{.language-} pour mettre à jour les paquets snap.

## Réglage de l'horloge

Voir [horloge UTM](https://wiki.archlinux.org/title/System_time_(Français)), surtout si vous avez également windows 11 sur votre machine et que voulez que l'heure soit la même sur les deux systèmes.

## Paquets utiles à installer

* [graphicsMagic](http://www.graphicsmagick.org/)
  * gestion de tous les types d'images permet manipuler, convertir, redimensionner tout type d'image en ligne de commande.
  * `sudo apt install graphicsmagick`
* [gimp](https://www.gimp.org/)
  * création et manipulation d'images
  * `sudo snap install gimp`
* [chrome](https://www.google.com/chrome/)
  * navigateur populaire. Version Chromium pour Linux.
  * `sudo snap install chromium`
* [inkscape](https://inkscape.org/fr/)
  * dessins vectoriels
  * `sudo apt  install inkscape`
* [mpv](https://mpv.io/) ou [vlc](https://www.videolan.org/)
  * lecteur multimedia, le premier est à la mode le second l'a été
  * `sudo apt install mpv` ou `sudo apt install vlc-bin`
* [git](https://git-scm.com/)
  * gestion des sources. Vous en aurez besoin tôt ou tard.
  * `sudo apt install git`
* [latex](https://doc.ubuntu-fr.org/latex)
  * écriture de documents scientifiques
  * `sudo apt install texlive-full` (attention, c'est long)

## Liste des paquets disponibles

{% attention %}

Notion avancé. Cette partie est ici pour la complétion. Un tuto devrait bientôt venir.

Donc si vous ne comprenez rien à cette partie c'est :

1. normal
2. que vous n'en avez pas besoin

{% endattention %}

Les différents paquets disponibles sont rangés par sites. La liste des différents sites disponible est rangé dans le fichier `/etc/apt/sources.list`{.fichier}.

C'est une notion avancée, mais il est parfois utile d'ajouter des sites lorsque l'on installer des packages bien spécifiques. Il faut alors faire deux choses :

1. ajouter le site dans le fichier `/etc/apt/sources.list`{.fichier}
2. autoriser l'installation de paquets depuis ce site en ajoutant la signature électronique du site à la liste des sites autorisés.

Ci-après deux tutoriels avancés pour comprendre comment faire :

* [signature électronique](/cours/système/cryptographie/#signature){.interne}
* [dossiers de sites ubuntu](https://automateinfra.com/2021/04/14/how-to-work-with-ubuntu-repository/)
* [signature électronique des sites](https://www.digitalocean.com/community/tutorials/how-to-handle-apt-key-and-add-apt-repository-deprecation-using-gpg-to-add-external-repositories-on-ubuntu-22-04)
