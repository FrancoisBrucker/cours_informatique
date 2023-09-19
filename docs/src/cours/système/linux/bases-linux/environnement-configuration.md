---
layout: layout/post.njk

title: Environnement et configuration

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Variables d'environnement


-[variables d'environnement](https://www.youtube.com/watch?v=1z6EUUl11qI&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs&index=2)

- [pas d'espace dans la déclaration de variable en shell](https://utcc.utoronto.ca/~cks/space/blog/unix/BourneShellObscureErrorRoots)

> TBD autre fichier lorsque l'on parlera de l'environnement. pour aller plus loin (ensuite). Lorsque l'on a parlé des variables. PWD, OLDPWD
> TBD dans les env parler de PWD et poser la question de : <https://stackoverflow.com/questions/41147818/no-man-page-for-the-cd-command>

> TBD $PATH : which, type whereis
> attention à ne pas mettre .

## Fichiers de configurations de bash

- fichiers de contrôle : .profile, .bashrc
- alias (`ls -la`, python pour python3) : which et file

## Fichiers de configurations des applications

config d'applis (helix, kitten)

- xdg config et https://github.com/b3nj5m1n/xdg-ninja 

- `.config` [organisation XDG](https://wiki.archlinux.org/title/XDG_Base_Directory)
- commande [options] paramètres. Les [dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I) que l'on peut mettre sur github pour les retrouver facilement d'une machine à l'autre

1. variables d'environnements
2. fichiers de configurations du shell
3. fichiers de configurations des applications


- shell enfant ne peut pas modifier l'environnment du parent.

- xdg config et https://github.com/b3nj5m1n/xdg-ninja 

- `.config` [organisation XDG](https://wiki.archlinux.org/title/XDG_Base_Directory)
- commande [options] paramètres. Les [dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I) que l'on peut mettre sur github pour les retrouver facilement d'une machine à l'autre
- bash .profile/.bashrc

   1. variables d'environnement
   2. shell bash file
      1. .profile, .bashrc, ... : quoi faire quand
      2. exemples de ubuntu : path, alias, etc.
