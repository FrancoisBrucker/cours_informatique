---
layout: layout/post.njk

title: Linux

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
Merci à :

- Naïs et Florian pour [la prise de notes du premier cours](https://docs.google.com/document/d/1kUSi4F8JdOgSZs_eNxCWOhEjxX-D8YjmCUm_bdmrolM/edit?tab=t.0)

{% endinfo %}

<!-- 

> TBD <https://labex.io/linuxjourney>
> outil shell <https://www.youtube.com/watch?v=yTkygli1OeE>
> <https://www.youtube.com/watch?v=SU7i3P62cm0&list=PL0ibd6OZI4XIJzwFC6XtsgZEcjEb4J-g->
> 
 -->

{% lien %}

- [Philosophie d'Unix (featuring Kernighan avec les pieds sur le bureau)](https://www.youtube.com/watch?v=tc4ROCJYbm0)
- [histoire des termes informatiques](https://www.youtube.com/watch?v=qgwrt7vYY4U)

{% endlien %}
{% lien %}

- [The Linux Command Line](https://www.amazon.fr/Linux-Command-Line-2nd-Introduction/dp/1593279523/) (W. Shotts) et [Classic Shell  Scripting](https://www.amazon.fr/Classic-Shell-Scripting-Arnold-Robbins/dp/0596005954/) : Ce sont les « bibles » pour Linux. Il faut les lire si on veut faire du Linux de manière plus approfondie.
- [How Linux Works](https://www.amazon.fr/How-Linux-Works-Brian-Ward/dp/1718500408/r) : donne une compréhension globale de comment marche un système.
- expression régulières :
  - [Mastering Regular Expressions](https://www.amazon.fr/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/) : ce qu’on /peut faire ou non dans une expression régulière.  
  - [Sed & Awk (O'Reilly)](https://www.amazon.fr/sed-awk-Pocket-Reference-2e/dp/0596003528/) et : [Grep Pocket Reference](https://www.amazon.fr/grep-Pocket-Reference-John-Bambenek/dp/0596153600/) apprendre à manipuler les fichiers texte.

{% endlien %}

Histoire d'Unix :

- [frise historique](https://www.youtube.com/watch?v=AEsdyAeumVQ)
- les [débuts d'Unix](https://www.youtube.com/watch?v=boahlBmc-NY)
- [Ken Thompson interviewed by Brian Kernighan](https://www.youtube.com/watch?v=EY6q5dv_B-o)

Plusieurs unix, Linux en est une version. POSIX pour unifier (mais attentions aux variantes et aux extensions à POSIX qui sont système dépendant)

## Pourquoi connaître Linux

La majorité des serveurs dans le monde tournent sous Linux. Linux est libre, gratuit et puissant. Contrairement à Windows/macOS, tout peut être contrôlé par ligne de commande et est le système utilisé par les méthodes de conteneurisation comme [Docker](https://www.docker.com/).

{% attention "**À retenir**" %}
Comprendre les mécanismes d'un OS de type Unix est fondamental pour déboguer, administrer ou optimiser ses services web ou ses conteneurs.
{% endattention %}

## Installation d'un système Linux

Plusieurs installations possibles, allant d'une surcouche minimale à l'installation complète du système.

{% aller %}

1. [Installation Linux](installation-linux){.interne}
2. [Paquets utiles à installer](post-installation){.interne}

{% endaller %}

## Système Linux

> TBD ici uniquement Linux Ubuntu. Si vous êtes sous macos ou un autre unix-like parfois les commandes différeront un peu. Reportez vous au manuel de votre noyau/distribution pour connaître la syntaxe exacte si nécessaire.

### Bases

{% aller %}
[Base Linux](bases-linux){.interne}
{% endaller %}

### Shell

[Shell](shell){.interne}

## TBD refactor

> TBD [shell script et paramètres (getopts)](https://www.youtube.com/watch?v=5O4SLIDSMqg)

1. [Système d'exploitation Linux/Ubuntu](./système-exploitation-linux){.interne}
2. [Fichiers unix](fichiers){.interne}
3. [tmux](tmux){.interne}

```shell
socat \
    -v -d -d \
    TCP6-LISTEN:$(id -u),crlf,reuseaddr,fork \
    SYSTEM:"
        echo HTTP/1.1 200 OK; 
        echo Content-Type\: text/plain; 
        echo; 
        echo Coucou du serveur;
        date
    "
```

> TBD [gros serveur](https://gist.github.com/ascopes/8c86413a3976975e7e958be5f49db2f2)

> TBD file descriptor redirection `>&1` : <https://unix.stackexchange.com/questions/84620/what-does-sh-a-sh-0-0-mean>
> 
> TBD <https://unix.stackexchange.com/questions/53641/how-to-make-bidirectional-pipe-between-two-programs>

> TBD signaux : <https://pauillac.inria.fr/~remy/poly/system/camlunix/sign.html>
> TBD cours unix/caml : <https://pauillac.inria.fr/~remy/poly/system/camlunix/cours.pdf>
>   p14 liens dur/symbolique et joli arborescence
>   p17 droits
>   p51 signaux
>   communication :
>     p61 pipe
>     p77 sockets 
>     p93 http (faire un protocole ROT13 avec socat)
>   p101 thread (est-ce qu'une goroutine est un thread ?)