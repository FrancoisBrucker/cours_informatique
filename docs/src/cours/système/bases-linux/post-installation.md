---
layout: layout/post.njk

title: Post installation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Que faire après une première installation de Linux/Ubuntu

## Mise à jour des paquets

* `sudo apt update && sudo apt upgrade`
* `sudo snap refresh`

{% info %}
<https://automateinfra.com/2021/04/14/how-to-work-with-ubuntu-repository/>
{% endinfo %}

## Réglage de l'horloge

Voir [horloge UTM](https://wiki.archlinux.org/title/System_time), surtout si vous avez également windows 11 sur votre machine.

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
