---
layout: layout/post.njk

title: Tmux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

[Tutorial](https://www.youtube.com/watch?v=Yl7NFenTgIo)

{% endlien %}

{% faire %}
Créez le script final de la video suivante pour vos déploiement sur les serveurs de production :

[tmux in 100 seconds](https://www.youtube.com/watch?v=vtB1J_zCv8I)

{% endfaire %}

## Signaux

[Liste des signaux](https://fr.wikipedia.org/wiki/Signal_(informatique)#Liste_des_signaux).

- [SIGKILL (numéro POSIX 9)](https://en.wikipedia.org/wiki/Signal_(IPC)#SIGKILL)
- [SIGSTOP (numéro POSIX 19)](https://en.wikipedia.org/wiki/Signal_(IPC)#SIGSTOP)

<https://faculty.cs.niu.edu/~hutchins/csci480/signals.htm>

### fg et bg

<http://igm.univ-mlv.fr/~allali/enseignement/prog_unix/documents/Stage_Unix/Stage_Unix_processus.html>

### trap

<https://www.learnlinux.org.za/courses/build/shell-scripting/ch12s03>

#### rot13.sh

```shell
#! /bin/sh

while read line; do
  echo $line | tr 'A-Za-z' 'N-ZA-Mn-za-m'
done
```

#### insupportable.sh

```shell
#! /bin/sh

while true
do
    sleep ${2:-1}
    echo ${1:-"Never Gonna Give You Up"}
done
```

```shell
trap 'echo "je suis immourable ! MOUAHAHAHA"' SIGINT
```

```shell
trap 'echo "je suis immourable ! MOUAHAHAHA"' SIGINT 15 
```

#### C'est aussi utile

<https://quennec.fr/trucs-astuces/syst%C3%A8mes/gnulinux/programmation-shell-sous-gnulinux/aspects-avanc%C3%A9s-de-la-programmation-shell/gestion-des-signaux/utiliser-trap-%C3%A0-partir-dun-script-shell>

## Refactor

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