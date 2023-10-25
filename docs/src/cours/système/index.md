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

1. Système
   1. [Système d'exploitation](./système-exploitation){.interne}
   2. [Architecture d'un ordinateur](./architecture-ordinateur){.interne}
   3. [Structures de données utiles](./structures-données-système){.interne}
   4. [Linux](linux){.interne}
2. [langage **C**](./langage-c){.interne}
3. Gestion des fichiers
   1. [Fichiers en **C**](fichiers-C){.interne}
   2. [Memory mapping](memory-mapping){.interne}
   3. [Fichiers Unix](fichiers){.interne}
4. Gestion des process
   1. signaux (SIGINT et ctrl+C), attention on ne peut pas tout faire dans une gestion de signal
   2. fork
   3. pipe (passe dans le fork)
5. Réseau
   1. [Bases de réseau](réseau){.interne}
   2. [sécurité](./sécurité){.interne}
   3. [clients serveurs](./client-serveur){.interne}
6. Concurrence
   1. IPC :
      1. file locking
      2. fifo, message queues
   2. Threads
      1. mutex (métaphores ?)
      2. opérqtion atomique
7. docker

{% info %}
Les documentations techniques que l'on donnera ici seront toujours en anglais. Faite l'effort de vous y mettre. Les documentations anglaises :

* seront toujours à jours
* vous parlez au monde entier en Anglais, il y aura toujours une réponse à vos questions si vous les formulez en anglais
* connaître l'anglais est requis dans votre futur métier, quelqu'il soit.

{% endinfo %}
