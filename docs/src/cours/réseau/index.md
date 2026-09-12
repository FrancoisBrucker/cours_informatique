---
layout: layout/post.njk

title: Réseau
tags: ['cours', 'réseau']
authors:
    - "François Brucker"

date: 2026-01-06

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours de système et de réseau. La partie ops de dev**ops**.

Nous verrons dans ce cours quelques fondamentaux de ce que doit savoir un développeur s'il veut pouvoir comprendre et interagir avec son administrateur système et un serveur distant (unix).


## Réseau


### Réseau

{% aller %}
[Principes et utilisation du réseau](bases-réseau){.interne}
{% endaller %}

### ssh

{% aller %}
[Connexions ssh](./ssh){.interne}
{% endaller %}

## refactor

> TBD refactor shell <https://effective-shell.com/part-1-transitioning-to-the-shell/navigating-your-system/>
> TBD <https://tuteurs.ens.fr/unix/> et shell variables <https://tuteurs.ens.fr/unix/shell/variable.html>
> TBD découper en partie plus digeste
> TBD jail : <https://www.youtube.com/watch?v=rGdylV-Up_E>
> TBD opérateurs shell <https://quennec.fr/book/export/html/272>
> TBD fibo en sh : <https://quennec.fr/node/640>

1. [Bases de réseau](réseau){.interne}
2. [clients serveurs](./client-serveur){.interne} (socket)
3. [Redirection de ports](redirection-ports-ssh){.interne}
4.  Docker : interfaces réseau

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
