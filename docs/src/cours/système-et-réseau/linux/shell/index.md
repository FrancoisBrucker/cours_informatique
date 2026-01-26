---
layout: layout/post.njk

title: Shell

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD voir <http://aral.iut-rodez.fr/fr/sanchis/enseignement/bash/>
>
> TBD variable substitution : <https://www.ibm.com/docs/en/aix/7.1.0?topic=shell-parameter-substitution-in-korn-posix>
>
> POSIX shell documentation : <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html>
{% lien %}

- [quelques liens](https://www.youtube.com/watch?v=Jllnhid7O7w)
- [Cheat sheet par type](https://github.com/lazyoracle/linux-cheatsheet)
- [Cheat sheet terminal et liste commandes](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)

{% endlien %}

Le shell est ce via quoi on exécute des commandes.

## Exécution de commandes

> simple
> retour 0 = ok et sinon message d'erreur
> shell et sous-shell ()
> globing *
> $(), $(())
> redirection entrée/sortie/erreur
> TBD lien <https://matthieu-moy.fr/spip/IMG/pdf/sh.pdf>
>
> utilisation du [process substitution](https://tldp.org/LDP/abs/html/process-sub.html) : <https://www.youtube.com/watch?v=2A4bs40scSo>
> à mettre dans les pipe et named pipe car c'est en fait ça. Voir la même chose en sh avec des named pipe : <https://stackoverflow.com/questions/38796224/posix-shell-equivalent-to> ou wvec des fichiers <https://www.shellcheck.net/wiki/SC3001>

## Variables d'environnement

Le shell est ce via quoi on exécute des commandes. Pour que l'environnement de travail soit :

- vérifiable
- modifiable

Pour cela le shell possède des **_variables_** que l'on peut manipuler:

{% aller %}

[Variables shell](variables){.interne}

{% endaller %}

Certaines variables sont dites d'**_environnement_** car elles sont comprises par le shell et permettent la personnalisation de son environnement :

{% aller %}

[Variables d'environnement](variables-environnement){.interne}

{% endaller %}

## Configuration

{% aller %}

[Configuration du shell](configuration){.interne}

{% endaller %}

## Scripting

{% aller %}

[Scripting](scripting){.interne}

{% endaller %}

## Exercices

{% aller %}

[exercices](exercices){.interne}

{% endaller %}
