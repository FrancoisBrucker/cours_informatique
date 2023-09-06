---
layout: layout/post.njk

title: Système
tags: ['cours', 'unix', 'système']
authors:
    - "François Brucker"

eleventyNavigation:
    prerequis:
        - "/tutoriels/ordinateur-développement/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


<!-- début résumé -->

Cours d'introduction au système. La partie ops de dev**ops**.

<!-- fin résumé -->

Nous verrons dans ce cours quelques fondamentaux de ce que doit savoir un développeur s'il veut pouvoir comprendre et interagir avec son administrateur système et un serveur distant (unix).

1. [système d'exploitation](./système-exploitation){.interne}
2. [architecture d'un ordinateur](./architecture-ordinateur){.interne}
3. [installation Linux](installation-linux){.interne}
4. [base Linux](bases-linux){.interne}
5. [système d'exploitation Linux/Ubuntu](./système-exploitation-linux)
6. shell (scripting, outils textes grep/sed/awk): <http://luffah.xyz/bidules/Terminus/>
7. docker

8. mémoire, bit.
9. [cryptographie](./cryptographie){.interne}
    [ssh](./ssh){.interne}

{% info %}
Les documentations techniques que l'on donnera ici seront toujours en anglais. Faite l'effort de vous y mettre. Les documentations anglaises :

* seront toujours à jours
* vous parlez au monde entier en Anglais, il y aura toujours une réponse à vos questions si vous les formulez en anglais
* connaître l'anglais est requis dans votre futur métier, quelqu'il soit.

{% endinfo %}
