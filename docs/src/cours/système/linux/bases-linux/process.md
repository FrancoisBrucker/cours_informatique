---
layout: layout/post.njk

title: Process

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://www.youtube.com/watch?v=ls5cGi12kGw&list=PLtK75qxsQaMKLUENMaPlD_O2qS8ZBGjuy>

- , kill/fg/bg
- 
- suspendre une commande avec ctrl+Z qui envoie le signal `SIGSTOP`

> TBD quand on parlera process > Idem pour le process qui hérite des droits du fichier qui l'exécute

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

- kill de process (un autre terminal)
