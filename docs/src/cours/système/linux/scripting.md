---
layout: layout/post.njk

title: Shell scripting

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le scripting c'est l'exécution de fichiers textes pour résoudre un problème spécifique. Un langage de script est un langage interprété. Cela peut-être :

- du shell
- mais aussi python
- ou d'autres langage de script comme le awk

<https://linuxhint.com/20_awk_examples/>

Nous allons ici montrer comment exécuter des scripts avec le shell bash.

> TBD : $0, $1, $@
> structures de contrôle if/then/else. et le fait que c'est des retours de commande
> fonction qui rendent des entier (retour d'instruction et que le reste c'est des sorties standards)

## exécution d'un fichier texte

[shebang](https://fr.wikipedia.org/wiki/Shebang)

## Lecture de l'entrée standard

- python
- shell 

- [python stdin](https://www.digitalocean.com/community/tutorials/read-stdin-python)
- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

[quel shebang utiliser](https://www.baeldung.com/linux/bash-shebang-lines)
exemple + DM

<https://www.youtube.com/watch?v=8L7cM4q6TL8>

- curl un fichier puis grep dessus
- donner des ressources (yt, man) pour comprendre les outils utilisés
- shebang. Faire avec python.
- diff entre `/usr/bin/python3` et `/usr/bin/env python3`
- on fait du shell scripting
- <https://dev.to/husseinalamutu/bash-vs-python-scripting-a-simple-practical-guide-16in> : manipulation fichier, bash plus utile que python.

> TBD if then else est fait avec les retour de commandes. Ce n'est PAS une expression. Exemple avec plusieurs lignes.
> `[` est une commande ! C'est pour a qu'il y a le ; avant le then.

<https://www.gnu.org/software/bash/manual/html_node/>

- plusieurs sortes de shell (sh : shell historique, bash : shell par défaut dans Linux, zsh : shell par défaut macos, ...)
- le script se fait avec le shell le plus courant : bash (présent sous macos)
- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)



Taper des commandes = script. Comme python. Il faut trouver un moyen de faire des bouts de commandes san les executer a=à la fin d'une ligne. Python fait des blocs. shell fait autrement. De plus, tout est orienté commandes sans pratiquement aucune surcouche du shell (on le verra avec les if/then/else qui fonctionnent bien différemment du reste des langages de programmation)



1. exos : prendre un yt pour faire des exos
2. shell script

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```
https://itslinuxfoss.com/how-parse-json-shell-scripting-linux/