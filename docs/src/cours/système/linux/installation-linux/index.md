---
layout: layout/post.njk

title: Installation de Linux/Ubuntu

eleventyNavigation:
    prerequis:
        - "/cours/coder-et-développer/ordinateur-développement/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer plusieurs installations possibles de Linux.

La distribution que nous allons installer est la distribution Ubuntu. Elle est idéale pour débuter et utiliser le système d'exploitation Linux.

## Installation minimale

On utilise au maximum le système existant, mac ou Windows 11. On arrive à une solution satisfaisante bien que non complète.

### WSL sous windows 11

{% aller %}
[Installation de WSL](./wsl){.interne}
{% endaller %}

### Outils Linux sous Macos

Macos est un système unix, mais ce n'est pas Linux. Son nom est [Darwin](https://fr.wikipedia.org/wiki/Darwin_(informatique)). La plupart des commandes et des façons de faire Linux fonctionneront, il est donc courant de ne pas avoir besoin de Linux lorsque l'on est sous mac.

Cependant :

* certaines options de commandes seront parfois différentes
* les applications traitant du système ne seront pas identiques (le dossier `/proc` n'existe pas sous Macos par exemple)
* les exécutables sont au format [Mach-O](https://fr.wikipedia.org/wiki/Mach-O) et non [elf](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)
* Les nouveau mac sont sous architecture ARM et non x86
* le système est propriétaire, il est parfois difficile de
* ...

Ces petites différences ne sont pas gênantes du moment qu'on ne crée pas d'application systèmes. Il existe de plus un excellent gestionnaire de paquet permettant d'installer quasi tous les outils Linux disponible : [brew](https://brew.sh/index_fr), que vous avez déjà du installé si vous avez suivi le tutoriel [Ordinateur pour le développement](../../../Tutoriels/ordinateur-développement/){.interne}

## Installation sur une machine virtuelle

{% aller %}
[Installation de Linux/Ubuntu sur une machine virtuelle](./VM){.interne}
{% endaller %}

## Installation desktop

{% aller %}
[Installation de Linux/Ubuntu sur une machine](./desktop){.interne}
{% endaller %}
