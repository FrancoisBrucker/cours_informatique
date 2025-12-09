---
layout: layout/post.njk

title: Installation desktop

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Installation de Linux/Ubuntu sur un véritable ordinateur. On conservera le système d'origine (Macos ou Windows), à chaque démarrage, le [boot-loader](https://fr.wikipedia.org/wiki/Chargeur_d%27amor%C3%A7age) vous demandera de choisir sur quel système démarrer.

{% attention %}
Lorsque l'on installe un nouveau système sur son ordinateur, **tout** peut arriver, même si on pense savoir ce que l'on fait.

Il faut donc être préparé à tout perdre : **SAUVEGARDEZ** vos données avant de tenter l'installation de Linux/Ubuntu.

Lisez le [tutoriel d'installation d'un nouveau système](/tutoriels/ordinateur-développement/installation-nouveau-système) pour voir tout ce à quoi il faut penser.
{% endattention %}

## Système initial Windows 11

Pour installer une Machine Linux/Ubuntu sur un ordinateur physique, on procède comme pour une machine virtuelle. La seule différence est qu'il faut créer une clé USB bootable permettant de démarrer la machine.

### USB bootable

{% lien %}
<https://doc.ubuntu-fr.org/tutoriel/obtenir_cd_ubuntu#creer_une_cle_usb_amorcable>
{% endlien %}

### Installation d'Ubuntu en conservant Windows 11

Si vous avez une machine pas trop vieille (moins de 10ans), vous devriez avoir un système EFI. La double installation est aisée en suivant le tuto suivant :

{% lien %}
<https://doc.ubuntu-fr.org/uefi#installer_rapidement_ubuntu_sur_un_pc_recent_sans_se_soucier_de_l_efi>
{% endlien %}

## Système initial Macos avec un processeur ARM

{% lien %}
<https://github.com/UbuntuAsahi/ubuntu-asahi>
{% endlien %}

## Réglage de l'horloge

Une fois votre système installé, il peut être utile de régler votre horloge sur la carte mère, surtout si vous avez également windows 11 sur votre machine et que voulez que l'heure soit la même sur les deux systèmes :

{% lien %}
[horloge UTM](https://wiki.archlinux.org/title/System_time_(Français))
{% endlien %}
