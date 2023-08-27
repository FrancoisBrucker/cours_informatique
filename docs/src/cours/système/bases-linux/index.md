---
layout: layout/post.njk

title: Bases Linux

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Bases d'un système Linux.

1. Lire la partie Linux du tutoriel [Ordinateur pour le développement](/tutoriels/ordinateur-développement){.interne}
2. [post installation](post-installation){.interne}
3. droits et utilisateurs
4. cd ls, pushd et popd man et leurs options
5. hiérarchie des dossiers
6. process
7. environnement

* utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
