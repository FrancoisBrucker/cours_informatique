---
layout: layout/post.njk

title: Installation de Linux/Ubuntu

eleventyNavigation:
    order: 1
    prerequis:
        - "../../../tutoriels/ordinateur-développement/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer plusieurs installations possibles de Linux.

La distribution que nous allons installer est la distribution Ubuntu. Elle est idéale pour débuter et utiliser le système d'exploitation Linux.

## WSL sous windows 11

{% aller %}
[Installation de WSL](./wsl){.interne}
{% endaller %}

## Outils Linux sous Macos

Macos est un système unix, mais ce n'est pas Linux. Son nom est [Darwin](https://fr.wikipedia.org/wiki/Darwin_(informatique)).

La plupart des commandes Linux de base fonctionneront **mais** :

* certaines options seront parfois différentes
* les applications traitant du système ne seront pas identiques (le dossier `/proc` n'existe pas sous Macos par exemple)
* Les nouveau mac sont sous architectures ARM et non x86
* ...

Ces petites différences ne sont pas gênantes du moment qu'on ne crée pas d'application systèmes. Il existe de plus un excellent gestionnaire de paquet permettant d'installer quasi tous les outils Linux disponible : [brew](https://brew.sh/index_fr), que vous avez déjà du installé si vous avez suivi le tutoriel [Ordinateur pour le développement](../../../Tutoriels/ordinateur-développement/){.interne}

## Installation sur une machine virtuelle

* sur une [VM](./VM){.interne}

## Installation desktop

> TBD sur un disque à part
> TBD sur plusiurs partitions

> TBD : créer une clé usb bootable.

* sur son disque dur
* wsl et windows

### x86

<https://doc.ubuntu-fr.org/cohabitation_ubuntu_windows>

### Mac avec un processeur ARM

{% lien %}
<https://github.com/UbuntuAsahi/ubuntu-asahi>
{% endlien %}
