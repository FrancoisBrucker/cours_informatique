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
3. [commandes](./commandes){.interne}
4. [droits et utilisateurs](droits-utilisateurs){.interne}
5. et popd man et leurs options
6. hiérarchie des dossiers
7. process, stdin/out/err, pipe, kill/fg/bg
8. environnement
9. bash files
10. script -> DM



- commande [options] paramètres
- utiliser un terminal linux/(les commandes fonctionnent aussi avec le terminal mac) : <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>

- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)

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
- [pas d'espace dans la déclaration de variable en shell](https://utcc.utoronto.ca/~cks/space/blog/unix/BourneShellObscureErrorRoots)

- amusons nous avec dd : <https://www.youtube.com/watch?v=hsDxcJhCRLI>
- kill de process (un autre terminal)
