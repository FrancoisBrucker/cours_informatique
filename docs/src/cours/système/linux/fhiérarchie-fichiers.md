---
layout: layout/post.njk

title: Hiérarchies des fichiers

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://man.archlinux.org/man/file-hierarchy.7>

config d'applis (helix, kitten)

- xdg config et https://github.com/b3nj5m1n/xdg-ninja 

- `.config` [organisation XDG](https://wiki.archlinux.org/title/XDG_Base_Directory)
- commande [options] paramètres. Les [dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I) que l'on peut mettre sur github pour les retrouver facilement d'une machine à l'autre
