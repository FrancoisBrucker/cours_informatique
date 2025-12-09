---
layout: layout/post.njk

title: Linux
authors:
    - "François Brucker"

eleventyNavigation:
    prerequis:
        - "/cours/coder-et-développer/ordinateur-développement/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD ici intro de Naïs

<!-- 

> TBD <https://labex.io/linuxjourney>
> outil shell <https://www.youtube.com/watch?v=yTkygli1OeE>
> <https://www.youtube.com/watch?v=SU7i3P62cm0&list=PL0ibd6OZI4XIJzwFC6XtsgZEcjEb4J-g->
> 
 -->

{% lien %}

- [Philosophie d'Unix (featuring Kernighan avec les pieds sur le bureau)](https://www.youtube.com/watch?v=tc4ROCJYbm0)
- [histoire des termes informatiques](https://www.youtube.com/watch?v=qgwrt7vYY4U)

{% endlien %}

Histoire d'Unix :

- [frise historique](https://www.youtube.com/watch?v=AEsdyAeumVQ)
- les [débuts d'Unix](https://www.youtube.com/watch?v=boahlBmc-NY)
- [Ken Thompson interviewed by Brian Kernighan](https://www.youtube.com/watch?v=EY6q5dv_B-o)

Plusieurs unix, Linux en est une version. POSIX pour unifier (mais attentions aux variantes et aux extensions à POSIX qui sont système dépendant)

## Installation d'un système Linux

Plusieurs installations possibles, allant d'une surcouche minimale à l'installation complète du système.

{% aller %}

1. [Installation Linux](installation-linux){.interne}
2. [Paquets utiles à installer](post-installation){.interne}

{% endaller %}

## Système Linux

1. [Base Linux](bases-linux){.interne}
2. [Système d'exploitation Linux/Ubuntu](./système-exploitation-linux){.interne}
3. [Shell](shell){.interne}
4. [Fichiers unix](fichiers){.interne}
