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

- shell enfant ne peut pas modifier l'environnment du parent.

- xdg config et https://github.com/b3nj5m1n/xdg-ninja 

- `.config` [organisation XDG](https://wiki.archlinux.org/title/XDG_Base_Directory)
- commande [options] paramètres. Les [dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I) que l'on peut mettre sur github pour les retrouver facilement d'une machine à l'autre
- bash .profile/.bashrc

   1. variables d'environnement
   2. shell bash file
      1. .profile, .bashrc, ... : quoi faire quand
      2. exemples de ubuntu : path, alias, etc.
