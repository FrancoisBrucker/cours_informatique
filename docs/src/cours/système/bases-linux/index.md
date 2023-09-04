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

- utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>

## process

gtop pour voir la hiérarchie des process
créer des process par clone d'un process (on choisit ce qu'on partage avec le père), ex une commande shell : comment ça marche le clone/fork
ps, kill, suspend, fg,
tuer une fenêtre
tmux/screen ou nohup pour détacher un process de son père.

<https://www.scaler.com/topics/process-management-in-linux/>

un terminal a :

- un foreground job
- plusieurs background job (avec &)

Mais c'est toujours le père. Des signaux permettent de communiquer :
- stop et bg pour le foreground
- read/write sur le terminal