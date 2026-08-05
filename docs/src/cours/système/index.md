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

## Partie I : Ordinateur, programmes et OS

{% aller %}
[Ordinateur, programmes et OS](ordinateur-programmes-OS){.interne}
{% endaller %}

## Partie II : Stocker et utiliser des données

> TBD déplacer les utilisateur/root etc dans la partie II.2 (II.1 = dossiers et fichiers, II.2 = utilisateurs et droits)

### II.1 : Dossiers et fichiers

> TBD parler des drivers et fax/ext. pas forcément spécifique à l'os (ex linux) mais pour windows pas vraiment le choix de l'orga dd. Dire qu'on en parlera bien plus précisément plus tard ?

### II.2 : Utilisateurs et droits

Si tous les process du user mode pouvaient effectuer tous les appels systèmes sans restriction cela poseraient d'énormes problèmes de sécurité (un process pourrait accéder à toute la mémoire, en particulier celle réservée à d'autres process par exemple) c'est pourquoi chaque process n'a qu'un nombre restreint de possibilités (on appelle ceci [des droits](<https://fr.wikipedia.org/wiki/Droit_d%27acc%C3%A8s_(informatique)>)) gérés via la notion d'utilisateurs.




### Utilisateurs et groupes

Du point de vue du système d'exploitation un utilisateur est une entité permettant d'exécuter des processus. L'utilisateur qui se connecte à l'ordinateur au login est donc un parmi beaucoup d'autres, la plupart n'étant pas associé à une personne physique. Les utilisateurs sont ensuite placés dans des groupes, chaque groupe ayant des droits particuliers.

{% note %}
Un utilisateur peut utiliser uniquement les éléments (logiciel, fichier, dossier, ...) qui lui appartiennent ou qui appartiennent à ses groupes.
{% endnote %}

Il existe de nombreux groupes et utilisateurs utilisés par le système pour segmenter (et donc sécuriser) les utilisations. Parmi eux, un utilisateur et un groupe se détachent car ils ont plus de droit que les autres.

#### Utilisateur `root`

L'utilisateur `root` est l'utilisateur lié au système d'exploitation. Il est le propriétaire des process (démons) et interfaces du système d'exploitation. Cet utilisateur a ainsi tous les droits (peut aller partout, réserver autant de mémoire qu'il veut, etc).

Comme **Tout** processus a un propriétaire, l'existence de cet utilisateur est garantie.

#### Groupe des administrateurs systèmes

{% lien %}
[administrateur système](https://fr.wikipedia.org/wiki/Administrateur_syst%C3%A8me)
{% endlien %}

Le groupe des administrateurs systèmes permet de modifier des paramètres systèmes d'exécuter ou stopper des démons et d'installer de nouveaux logiciels. Ces utilisateurs ont moins de pouvoirs que root qui peut tout faire mais permettent d'administrer le système au quotidien.

Cela permet, si nécessaire, d'installer ou de configurer son système sans être connecté en tant que root en utilisant [la commande sudo](https://www.linuxtricks.fr/wiki/sudo-utiliser-et-parametrer-sudoers) sous Linux par exemple.


Les démons et les interfaces sont des process comme les autres. Ils sont cependant exécutés par un utilisateur spécial, souvent nommé [`root`](https://fr.wikipedia.org/wiki/Utilisateur_root), qui est le [super-utilisateur](https://fr.wikipedia.org/wiki/Utilisateur_root) et est le représentant utilisateur du système.

quatrième couche pour les OS.

4. utilisateurs
   - qui à le droit de faire quoi


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
