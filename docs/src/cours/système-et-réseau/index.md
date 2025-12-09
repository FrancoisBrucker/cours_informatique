---
layout: layout/post.njk

title: Système et réseau
tags: ['cours', 'unix', 'système']
authors:
    - "François Brucker"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours de système et de réseau. La partie ops de dev**ops**.

Nous verrons dans ce cours quelques fondamentaux de ce que doit savoir un développeur s'il veut pouvoir comprendre et interagir avec son administrateur système et un serveur distant (unix).

## Bases

### Système

{% aller %}
[Principes et utilisation d'un système d'exploitation](bases-système){.interne}
{% endaller %}

### Réseau

{% aller %}
[Principes et utilisation du réseau](bases-réseau){.interne}
{% endaller %}

## Linux

{% aller %}
[Linux](linux){.interne}
{% endaller %}

## refactor

> TBD découper en partie plus digeste
> TBD jail : <https://www.youtube.com/watch?v=rGdylV-Up_E>

1. Système
   1. [Architecture d'un ordinateur](./architecture-ordinateur){.interne}
   2. [Système d'exploitation](./système-exploitation){.interne}
   3. [Structures de données utiles](./structures-données-système){.interne}
   4. 
2. [connexions ssh](./ssh){.interne}
3. [Bases de réseau](réseau){.interne}
4. [clients serveurs](./client-serveur){.interne}

5. Langages
    1. [langage **C**](./langage-c){.interne}
    2. assembleur
    3. ABI
6. Gestion des fichiers
   1. [Fichiers en **C**](fichiers-C){.interne}
   2. [Memory mapping](memory-mapping){.interne}
7. Gestion des process
   1. signaux (SIGINT et ctrl+C), attention on ne peut pas tout faire dans une gestion de signal
   2. fork
   3. pipe (passe dans le fork)
8. Concurrence
   1. IPC
      1. fifo, message queues
      2. file locking
   2. Threads
      1. mutex (métaphores ?)
      2. opérations atomique
9. docker

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
