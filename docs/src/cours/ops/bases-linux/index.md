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

1. Lire la partie Linux du tutoriel [Ordinateur pour le développement](/tutoriels/ordinateur-développement)
2. [post installation](post-installation)

* utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
