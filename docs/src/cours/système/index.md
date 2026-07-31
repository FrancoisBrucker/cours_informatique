---
layout: layout/post.njk

title: Système
tags: ['cours', 'unix', 'système']
authors:
    - "François Brucker"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours de système.

## Partie I : Ordinateur et Programmes

{% aller %}
[Ordinateur et Programmes](ordinateur-programmes){.interne}
{% endaller %}


## Linux

{% aller %}
[Linux](linux){.interne}
{% endaller %}

## refactor

> TBD refactor shell <https://effective-shell.com/part-1-transitioning-to-the-shell/navigating-your-system/>
> TBD <https://tuteurs.ens.fr/unix/> et shell variables <https://tuteurs.ens.fr/unix/shell/variable.html>
> TBD découper en parties plus digeste
> TBD jail : <https://www.youtube.com/watch?v=rGdylV-Up_E>
> TBD opérateurs shell <https://quennec.fr/book/export/html/272>
> TBD fibo en sh : <https://quennec.fr/node/640>

1. Système
   1. [Architecture d'un ordinateur](./architecture-ordinateur){.interne}
   2. [Système d'exploitation](./système-exploitation){.interne}
   3. [Structures de données utiles](./structures-données){.interne} et [Structures de données système](./structures-données-système){.interne}
   4. [concurrence](./concurrence) et 
2. Langages
    1. [langage **C**](./langage-c){.interne}
    2. assembleur
    3. ABI
3. Gestion des fichiers
   1. [Fichiers en **C**](fichiers-C){.interne}
   2. [Memory mapping](memory-mapping){.interne}
4. Gestion des process
   1. signaux (SIGINT et ctrl+C), attention on ne peut pas tout faire dans une gestion de signal
   2. [fork](./fork)
   3. pipe (passe dans le fork)
5. [Concurrence](./concurrence)
   1. [IPC](./ipc)
      1. fifo, message queues
      2. file locking
   2. Threads
      1. mutex (métaphores ?)
      2. opérations atomique
6.  Docker
7.  [outil système](./radare2)

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
