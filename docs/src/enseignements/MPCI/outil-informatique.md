---
layout: layout/post.njk 
title: "S1 : L'ordinateur comme outil"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Pour parodier [full metal jacket](https://www.youtube.com/watch?v=fr_hvg7tNbQ) :

> Ça, c'est mon ordi. Il y en a beaucoup comme ça, mais lui, c'est le mien. Mon ordi, c'est mon meilleur ami.

Le but de cette séance est de vous donner les connaissances nécessaire pour avoir un ordinateur pour le développement.

1. [Un ordinateur pour le développement](/tutoriels/ordinateur-développement){.interne}
2. [installation de python](/tutoriels/installation-python/#installation){.interne}
3. [vscode et python](/tutoriels/vsc-python){.interne}

{% info %}
Si vous débutez sous Linux/Ubuntu, cela vaut le coup de lire le tuto ci-après, qui liste différents paquets, utiles : [post-installation](/cours/système/bases-linux/post-installation/){.interne}
{% endinfo %}
