---
layout: layout/post.njk

title: Système Mac

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



1. installer un éditeur à tout faire. J'utilise la version gratuite de [bbedit](http://www.barebones.com/products/bbedit/).
2. placer le [terminal](https://support.apple.com/fr-fr/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac) dans le finder
3. installer [xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
4. installez les *developper tools* en tapant la commande `xcode-select --install` dans un terminal
5. installer [brew.sh](https://brew.sh/index_fr) en suivant ses recommendations
6. installez [docker desktop](https://www.docker.com/)
7. installez [virtualbox](https://www.virtualbox.org/) si vous n'avez pas un mac avec une puce M1. Sinon vous pouvez installer la version d'évaluation de parallels.
8. si vous avez un mac avec une puce arm, il vous faudra peut-être installer Rosetta. Dans un terminal tapez la commande `softwareupdate --install-rosetta`


## Tutos linux

* windows powershell : <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
* l'application terminal sous mac : <https://support.apple.com/fr-fr/guide/terminal/welcome/mac>
* utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
