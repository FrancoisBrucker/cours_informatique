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

1. système
   1. [système d'exploitation](./système-exploitation){.interne}
   2. [architecture d'un ordinateur](./architecture-ordinateur){.interne}
   3. [structures de données utiles](./structures-données-système){.interne}
   4. [Linux](linux){.interne}
2. [langage C](./langage-c){.interne}
3. gestion des fichiers
   1. [Fichiers Unix](fichiers){.interne}
   2. [fichiers en **C**](fichiers-C){.interne}
   3. [memory mapping](memory-mapping){.interne}
4. sockets et C
5. threads
6. docker
7. [cryptographie](./cryptographie){.interne}
8. [ssh](./ssh){.interne}
9. [sockets](./sockets-réseaux){.interne}

{% info %}
Les documentations techniques que l'on donnera ici seront toujours en anglais. Faite l'effort de vous y mettre. Les documentations anglaises :

* seront toujours à jours
* vous parlez au monde entier en Anglais, il y aura toujours une réponse à vos questions si vous les formulez en anglais
* connaître l'anglais est requis dans votre futur métier, quelqu'il soit.

{% endinfo %}
