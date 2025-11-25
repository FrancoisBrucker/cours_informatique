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


<!-- 

> TBD <https://labex.io/linuxjourney>
> outil shell <https://www.youtube.com/watch?v=yTkygli1OeE>
> <https://www.youtube.com/watch?v=SU7i3P62cm0&list=PL0ibd6OZI4XIJzwFC6XtsgZEcjEb4J-g->
> 
 -->

{% info %}
On suppose que vous avez suivi les tutos sur la [navigation dans un système de fichiers](/tutoriels/fichiers-navigation/), sur l'existence du [terminal](/tutoriels/terminal/) et [son utilisation](/tutoriels/terminal-utilisation)
{% endinfo %}

Histoire d'Unix :

- [frise historique](https://www.youtube.com/watch?v=AEsdyAeumVQ)
- les [débuts d'Unix](https://www.youtube.com/watch?v=boahlBmc-NY)
- [Ken Thompson interviewed by Brian Kernighan](https://www.youtube.com/watch?v=EY6q5dv_B-o&t=4s)

Plusieurs unix, Linux en est une version. POSIX pour unifier (mais attentions aux variantes et aux extensions à POSIX qui sont système dépendant)

1. [installation Linux](installation-linux){.interne}
2. [base Linux](bases-linux){.interne}
3. [système d'exploitation Linux/Ubuntu](./système-exploitation-linux){.interne}
4. [shell](shell){.interne}
5. [fichiers unix](fichiers){.interne}
