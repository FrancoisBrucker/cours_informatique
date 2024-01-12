---
layout: layout/post.njk

title: Déboguer son code


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD
> TBD debugger : <https://www.youtube.com/watch?v=7qZBwhSlfOo> <https://www.youtube.com/watch?v=KEdq7gC_RTA&list=PLQzZ4krxwT9Yay3kz8ly4wXiYJHzMtsWi>
>
> - montrer les appels successifs aux fonctions : stacks
> - montrer les variables
> - montrer l'exécution de l'interpréteur, une ligne à près l'autre, puis exécution des fonctions.
> - utiliser les watch à la place des prints
> - faire une fonction récursive pour montrer les appels.
> - step_into ne marche qu'avec nos fonctions, pas ceux de python (on ne connaît pas le code de print par exemple.)
