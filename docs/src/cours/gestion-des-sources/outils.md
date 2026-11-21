---
layout: layout/post.njk

title: Outils

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## App

Outre github-desktop, il existe de nombreuses application pour gérer github, citons-en deux, très utilisées :

- gratuite : <https://git-fork.com/>
- payante : <https://www.gitkraken.com/>

## TUI

{% lien %}

- [lazy git](https://github.com/jesseduffield/lazygit) ([une courte vidéo de présentation](https://www.youtube.com/watch?v=CPLdltN7wgE)) : une excellente application pour git
- [gh-dash](https://github.com/dlvhdr/gh-dash) : pour github et les pull requests

{% endlien %}

## Git avec vscode

{% info "**Documentation**" %}
<https://code.visualstudio.com/docs/editor/versioncontrol#_git-support>
{% endinfo %}

vscode permet d'utiliser directement les commandes git et possède de nombreux plugins permettant, par exemples :

- d'utiliser github avec l'[extension github](https://code.visualstudio.com/docs/editor/github)
- de voir le graphe de dépendances avec l'extension [git-graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (commande `git-graph.view` pour voir le graphe)
- de voir l'historique de modification d'un fichier avec l'extension [git-history](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (cliquer droit sur un fichier puis `Git: view file history`)
- ...

