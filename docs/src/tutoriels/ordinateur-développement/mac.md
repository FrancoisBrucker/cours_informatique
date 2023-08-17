---
layout: layout/post.njk

title: Système Mac

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



1. installer [xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
2. installez les *developper tools* en tapant la commande `xcode-select --install` dans un terminal
3. installez [docker desktop](https://www.docker.com/)
4. si vous avez un mac avec une puce arm, il vous faudra peut-être installer Rosetta. Dans un terminal tapez la commande `softwareupdate --install-rosetta`


## Tutos linux

* windows powershell : <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
* l'application terminal sous mac : <https://support.apple.com/fr-fr/guide/terminal/welcome/mac>
* utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
