---
layout: layout/post.njk

title: Shell

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Essayer d'être portable. On fait du du bash (voir du sh) pour pouvoir être exécuté partout

- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

Taper des commandes = script. Comme python. Il faut trouver un moyen de faire des bouts de commandes san les executer a=à la fin d'une ligne. Python fait des blocs. shell fait autrement. De plus, tout est orienté commandes sans pratiquement aucune surcouche du shell (on le verra avec les if/then/else qui fonctionnent bien différemment du reste des langages de programmation)

<https://www.gnu.org/software/bash/manual/html_node/>

<https://www.shellcheck.net/>

## Gestion des paramètres

> TBD : $0, $1, $@

## Fonctions

> fonction qui rendent des entier (retour d'instruction et que le reste c'est des sorties standards)

## Structures de contrôle

> structures de contrôle if/then/else. et le fait que c'est des retours de commande

[boucles en bash](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)

> TBD if then else est fait avec les retour de commandes. Ce n'est PAS une expression. Exemple avec plusieurs lignes.
> `[` est une commande ! C'est pour a qu'il y a le ; avant le then.

## Autres shell

Plusieurs sortes de shell (sh : shell historique, bash : shell par défaut dans Linux, zsh : shell par défaut macos, ...)

perso : mon shell c'est zsh mais les script je les écris en (ba)sh.

- [sh ou bash pour nos scripts ?](https://www.youtube.com/watch?v=8L7cM4q6TL8)

- le script se fait avec le shell le plus courant : bash (présent sous macos)
- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```

https://itslinuxfoss.com/how-parse-json-shell-scripting-linux/
