---
layout: layout/post.njk

title: Système et réseau
tags: ['cours', 'unix', 'système']
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


<!-- début résumé -->

Cours d'introduction au système. La partie ops de dev**ops**.

<!-- fin résumé -->

Nous verrons dans ce cours quelques fondamentaux de ce que doit savoir un développeur s'il veut pouvoir comprendre et interagir avec son administrateur système et un serveur distant (unix).

1. Système
   1. [Architecture d'un ordinateur](./architecture-ordinateur){.interne}
   2. [Système d'exploitation](./système-exploitation){.interne}
   3. [Structures de données utiles](./structures-données-système){.interne}
   4. [Linux](linux){.interne}
2. [Bases de réseau](réseau){.interne}

1. Langages
    1. [langage **C**](./langage-c){.interne}
    2. assembleur
    3. ABI
2. Gestion des fichiers
   1. [Fichiers en **C**](fichiers-C){.interne}
   2. [Memory mapping](memory-mapping){.interne}
   3. [Fichiers Unix](fichiers){.interne}
3. Gestion des process
   1. signaux (SIGINT et ctrl+C), attention on ne peut pas tout faire dans une gestion de signal
   2. fork
   3. pipe (passe dans le fork)
4. [clients serveurs](./client-serveur){.interne}
5. Sécurité
   1. [cryptographie](./cryptographie){.interne}
   2. [OpenPGP](./openpgp){.interne}
   3. [ssh](./ssh){.interne}
6. Concurrence
   1. IPC
      1. fifo, message queues
      2. file locking
   2. Threads
      1. mutex (métaphores ?)
      2. opérations atomique
7.  docker

{% info %}
Les documentations techniques que l'on donnera ici seront toujours en anglais. Faite l'effort de vous y mettre. Les documentations anglaises :

- seront toujours à jours
- vous parlez au monde entier en Anglais, il y aura toujours une réponse à vos questions si vous les formulez en anglais
- connaître l'anglais est requis dans votre futur métier, quelqu'il soit.

{% endinfo %}

> TBD : structures de données utiles. Ajouter :
> dire que c'est de l'algorithmie "terrain". Tout est compté au bit pres.
>
> - fifo (communication)
> - tcp : communication sécurisé incertain
> - sécurité : registre à décalage
> - protocole : header/body
>
> TBD :
>
> - interfacer C et python
> - bibliothèques C utiles (glib, gestion des fichiers)
> - commencer rapidement par une install de Linux pour pouvoir commencer le DM de suite.
> - faire un page générale avec les détails dans d'autres fichiers. Ceci permettra d'en parler sans rentrer dans les détails.
> - parler du fait que RSA n'est pas quantique (à cause de la factorisation) et que c'est pour ça que l'authentification commence à être sous d'autre formes (logarithme discret + courbes elliptiques)
