---
layout: layout/post.njk

title: Installation de Linux/Ubuntu

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Installation d'une distribution Linux/Ubuntu.

## Machine Virtuelle

{% lien %}

* Pour une machine x86 <https://www.virtualbox.org/>
* Pour un mac ARM <https://www.parallels.com/>

{% endlien %}

Une machine virtuelle est une application permettant de simuler un ordinateur.

### Virtual Box


## Machine x86

{% lien %}

* <https://doc.ubuntu-fr.org/installation>
* <https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview>

{% endlien %}

### <span id="x86-VM"></span>Machine Virtuelle

Virtual Machine

### <span id="x86-dual-boot"></span>dual boot

## Mac avec processeur ARM

### <span id="ARM-VM"></span>Machine Virtuelle

{% info %}

À l'heure où je tape ces caractères (août 2023), Virtual desktop ne fonctionne pas (ou très mal) avec les processeurs ARM. J'utilise [parallels](https://www.parallels.com/fr/) avec mon mac avec un processeur ARM.

{% endinfo %}

### <span id="ARM-dual-boot"></span>dual boot

{% lien %}
<https://github.com/UbuntuAsahi/ubuntu-asahi>
{% endlien %}
