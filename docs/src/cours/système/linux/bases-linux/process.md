---
layout: layout/post.njk

title: Process

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

[process](https://www.youtube.com/watch?v=ls5cGi12kGw&list=PLtK75qxsQaMKLUENMaPlD_O2qS8ZBGjuy)

{% endlien %}

Un process correspond à l'exécution d'un fichier. Les process sont organisés en arbre et descendent tous du premier process crée : `systemd`. Créer un process se fait en plusieurs temps :

1. le process appelant est dupliqué en utilisant l'appel système [fork](https://fr.wikipedia.org/wiki/Fork_(programmation)) (*ie* le shell qui lance la commande). Le process appelant est le process parent, le nouveau process le process enfant. Le fait que le process est dupliqué fait que :
   1. l'environnement des process parent et enfant est le même
   2. le propriétaire (uip) et le groupe (pid) des process parent et enfant sont les mêmes
2. on associe un numéro, le PID, à ce nouveau process. Ce numéro est unique
3. le PID du parent est associé à l'enfant via le PPID

Un process d'uid root peut changer son utilisateur et son groupe. Ceci se fait :

- au login d'un utilisateur : le premier shell de l'utilisateur possède son uid
- pour les serveurs : le groupe est positionné au groupe de l'application. Par exemple web pour un serveur web.

Enfin, certains process peuvent avoir les privilèges de `root` alors qu'ils sont exécutés par de simples utilisateur. Ces process sont lancés par des fichiers possédant le flag [setuid ou setgid](https://en.wikipedia.org/wiki/Setuid). Par exemple la commande `passwd` qui doit pouvoir être exécutée par un utilisateur mais modifier le ficheor `/etc/shadow` qui est la propriété de `root`.

## Arbre des process

```
pstree | less
top
```

## Process foreground/background

> TBD : [process management](https://www.scaler.com/topics/process-management-in-linux/)

Tout shell possède :

- au plus un process foreground qui possède l'entrée standard (par exemple top lorsqu'il est lancé)
- plusieurs process background qui possèdent la sortie et l'erreur standard

- suspendre une commande avec ctrl+Z qui envoie le signal `SIGSTOP`
- [fg et bg](https://www.redhat.com/sysadmin/jobs-bg-fg)
- exécuter une commande avec `&`

## Vie et mort d'un process

- lorsque le parent meurt il envoie un signal de fin à ses enfants.
- nohup pour ratacher un process à systemd et ainsi il ne sera supprimé que si la machine reboot
- screen ou tmux pour faire la même chose mais en mieux : ce sont des shell qui sont attaché à tmux qui est attaché à systemd. On peut y retourner si besoin

- kill PID
- kill -9 PID

créer des process par clone d'un process (on choisit ce qu'on partage avec le père), ex une commande shell : comment ça marche le clone/fork
