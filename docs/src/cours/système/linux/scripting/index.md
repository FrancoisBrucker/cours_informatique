---
layout: layout/post.njk

title: Scripting

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le scripting c'est l'exécution de fichiers textes pour résoudre un problème spécifique. Un langage de script est un langage interprété. Cela peut-être :

- du shell
- mais aussi python
- ou d'autres langage de script comme le awk

## Exécution d'un fichier texte

{% lien %}
[shebang](https://fr.wikipedia.org/wiki/Shebang)
{% endlien %}

Le fonctionnement est divinement simple. Lors de 'exécution du fichier, le noyau vérifie s'il commence par `#!` si oui la fin de la ligne correspond à un programme auquel on passe en 1er paramètre le fichier à exécuter.

Par exemple si on a le fichier exécutable suivant, nommé `bonjour` :

```
#! /usr/bin/python

print("Coucou monde !")
```

Les deux commandes suivantes sont équivalente (si on est dans le dossier contenant le fichier) :

- `bonjour`
- `/usr/bin/python bonjour`

{% lien %}
[Histoire du shebang](https://www.in-ulm.de/~mascheck/various/shebang/#blankrequired)
{% endlien %}

C'est la raison fondamentale pour laquelle les commentaires dans un langage de script est toujours le `#`, la première ligne contenant le shebang n'est pas interprétée lors de l'exécution du script.

Il y a deux moyens classique d'utiliser le shebang :

- appeler directement le programme : `/bin/bash`
- passer via env : `/usr/bin/env bash`

La différence es que pour le deuxième appel, c'est le bash du PATH qui est pris et pas celui du système. Ces deux programmes pouvant être différent. Si pour bash il y a peu de risque, pour python est est courant d'avoir plusieurs versions d'installées.

{% lien %}
[Quel shebang utiliser](https://www.baeldung.com/linux/bash-shebang-lines)
{% endlien %}

## Interpréteurs

### python

- <https://dev.to/husseinalamutu/bash-vs-python-scripting-a-simple-practical-guide-16in> : manipulation fichier, bash plus utile que python.

[python stdin](https://www.digitalocean.com/community/tutorials/read-stdin-python)

### bash

{% aller %}
[bash scripting](bash){.interne}
{% endaller %}

Exercices :

- [petits scripts bash](exercices){.interne}
- [DM](DM){.interne}

### sed/awk

{% aller %}
[sed-awk](sed-awk){.interne}
{% endaller %}

## Bibliographie

- [classic shell scripting](https://doc.lagout.org/operating%20system%20/linux/Classic%20Shell%20Scripting.pdf)