---
layout: layout/post.njk

title: Bus

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La communication du processeur avec le reste du monde, c'est à dire avec le user agent qui est le point de regroupement de tous les devices, se fait uniquement avec un unique bus. Ce bus est composé de 3 canaux pour permettre d'accéder à une donnée :

- **contrôle** : que veut-on faire : lire (faire entrer dans le processeur)/écrire (faire sortir la donnée)
- **adresse** : où commence la donnée à lire/écrire
- **donnée** : la donnée à lire ou à écrire

La taille du canal de donnée varie selon les ordinateurs, mais une bonne approximation est de considérer qu'elle est de 64bits, transmis de façon parallèle.

## Canal de contrôle

{% lien %}
[Canal de contrôle](https://en.wikipedia.org/wiki/Control_bus)
{% endlien %}

Détermine :

- l'action à mener : essentiellement lire ou écrire des données, mais peut aussi être des actions de maintenance ou une demande d'interruption de la part d'un device.
- la taille des données transférées : une puissance de 2, jusqu'à la taille du canal de donnée, usuellement 64bits

## Canal d'adresse

{% lien %}
[Canal d'adresse](https://en.wikipedia.org/wiki/Bus_(computing)#Address_bus)
{% endlien %}

La partie adresse du bus doit permettre de déterminer à la fois déterminer le device et l'endroit sur celui-ci où lire/écrire l'information. Par exemple, si la taille du bus d'adresse est de 64 bit, on peut (c'est un exemple) :

- réserver 4bits pour le choix du device (on a $2^4=16$ possibilités, de $0000$ à $1111$)
- réserver 60bits pour l'adresse ce qui fait un adressage de $2^{60}$ bit, donc 4503 terabyte (voir [$10^{12}$ bytes](https://fr.wikipedia.org/wiki/Mod%C3%A8le:Unit%C3%A9s_de_bytes)). Ce qui est pas mal puisque la norme haute en RAM est actuellement 128 gigabyte ($10^{9}$ bytes).

Ce qui nous laisse la place d'accéder à tous les devices branchés :

- un byte de la mémoire RAM
- un accès série à un device :
  - disque dur,
  - écran,
  - clavier,
  - etc

Cette technique d'adressage unifiée est appelée [IO memory mapping](https://en.wikipedia.org/wiki/Memory-mapped_I/O_and_port-mapped_I/O). L'intérêt est d'ajouter une couche d'indirection (rappelez vous la règle fondamentale de l’ingénierie logicielle), le processeur n'a pas à avoir plusieurs jeux d'instructions selon le device auquel il veut accéder, tout est unifié.

{% lien %}
[Mise en œuvre électronique](https://www.youtube.com/watch?v=2Cbcb2yGjiM)
{% endlien %}

L'exemple précédent est très simplifié car les devices hors mémoire n'ont pas besoin de beaucoup d'adressage. Il est en effet impossible d'accéder directement à tout byte. La communication avec ces devices se fait par un protocole similaire aux protocoles de communication réseaux la communication via des paquets de taille fixe, en lecture et en écriture : l'essentiel de la communication passe par la partie donnée du bus et non la partie adresse.

Ceci pose cependant un problème car l'accès à chaque byte d'un disque dur va mobiliser le processeur et l'accès à un disque dur est relativement lent par rapport à la vitesse d'un processeur, ce qui ralentie inutilement le système puisque le processeur va passer son temps à attendre que l'accès disque soit terminé. Pour palier ce problème on utilise un procédé nommé [Direct Memory Access](https://en.wikipedia.org/wiki/Direct_memory_access). Par exemple pour lire des données :

1. plutôt que d'envoyer les données lues au processeur, on les envoie en mémoire RAM
2. plutôt que de demander 1 byte à la fois, on en demande directement 4KiB (on demande une [page](https://en.wikipedia.org/wiki/Page_(computer_memory)) de donnée)
3. une fois la demande de lecture de la page faite par le processeur au device, le device communique directement avec la RAM via le System Agent pour effectuer le transfert byte à byte du device à la RAM
4. une fois la page transférée le device génère une [Interruption](https://fr.wikipedia.org/wiki/Interruption_(informatique)) pour prévenir le processeur de la fin du traitement.

{% lien %}
Ue série de vidéos explicatives sur ces mécaniques :

1. [I/O](https://www.youtube.com/watch?v=nnO2OfSTVbA&list=RDCMUCOPmCMY3ROyg04_y5bYPyyw&index=7)
2. [I/O memory mapping](https://www.youtube.com/watch?v=xNH1e5snIEY&list=RDCMUCOPmCMY3ROyg04_y5bYPyyw&index=1)
3. [les interruptions](https://www.youtube.com/watch?v=dDA3PUr16As&list=RDCMUCOPmCMY3ROyg04_y5bYPyyw&index=4)
4. [Direct memory Access](https://www.youtube.com/watch?v=M16l_ymlfcs&list=RDCMUCOPmCMY3ROyg04_y5bYPyyw&index=8)
{% endlien %}

Ces IO mapping sont placés dans la partie réservée au noyau d'un OS :

- un process ne peut y accéder directement
- elles ne rentre pas en conflit avec l'organisation de la mémoire utilisateur

## Canal donnée

Le canal de donnée est le nombre de byte que l'on peut transférer. Sa taille est une puissance de 2 bit. Actuellement au moins 64b et souvent 128b pour pouvoir transférer deux qword en une fois.

La taille *logique* de transfert étant toujours 64b = 8B.
