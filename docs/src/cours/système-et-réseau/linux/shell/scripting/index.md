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
- ou d'autres langage de script comme awk, perl, ruby, …

Le fonctionnement est divinement simple. Lors de 'exécution du fichier, le noyau vérifie s'il commence par `#!`, appelé [shebang](https://fr.wikipedia.org/wiki/Shebang).

Si oui la fin de la ligne correspond au chemin absolu d'un programme auquel on passe en 1er paramètre le fichier à exécuter.

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

- appeler directement le programme : `/usr/bin/python`
- passer via env : `/usr/bin/env python`

La différence est que pour le deuxième appel, c'est le bash du PATH qui est pris et pas celui dans `/bin`. Ces deux programmes pouvant être différent. bash peut être dans `/bin`, dans `/usr/bin`, dans `/usr/local/bin` ou encore ailleurs selon le système et la méthode d'installation, pour python il est courant d'avoir plusieurs versions d'installées. En revanche, tous les systèmes ont `/usr/bin/env`.

{% lien %}
[Quel shebang utiliser](https://www.baeldung.com/linux/bash-shebang-lines)
{% endlien %}

## Shell scripting

Si vous n'avez pas besoin des spécificités de bash on a l'usage d'utiliser les commandes fondamentales des shell de type sh. Nous allons voir ci-après les commandes bash, car elles permettent de faire parfois des choses plus poussées. 

{% aller %}

- [bash scripting](bash){.interne}

{% endaller %}

Plusieurs sortes de shell (sh : shell historique, bash : shell par défaut dans Linux, zsh : shell par défaut macos, ...)

{% info %}

perso : mon shell c'est zsh mais les script je les écris en (ba)sh. Si vous êtes administrateur système et que vous voulez que vos scripts fonctionnent partout, il existe des machines sans bash, utilisez juste sh.
{% endinfo %}

- [sh ou bash pour nos scripts ?](https://www.youtube.com/watch?v=8L7cM4q6TL8)
- le script se fait avec le shell le plus courant : bash (présent sous macos)
- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)

## Interpréteurs de script

Tout programme qui peut exécuter un fichier texte passé en paramètre fonctionne. Le plus classique étant bien sur le shell mais, comme on vient de le voir on peut le faire en python.

### python

- <https://dev.to/husseinalamutu/bash-vs-python-scripting-a-simple-practical-guide-16in> : manipulation fichier, bash plus utile que python.

[python stdin](https://www.digitalocean.com/community/tutorials/read-stdin-python)

### sed/awk

Une autre alternative courante est d'utiliser des commandes permettant de traiter des données comme sed ou encore awk  :

{% aller %}
[sed-awk](sed-awk){.interne}
{% endaller %}

## Bibliographie

- [classic shell scripting](https://doc.lagout.org/operating%20system%20/linux/Classic%20Shell%20Scripting.pdf)


{% exercice %}
Créez un fichier nommé `bonjour`{.fichier} contenant :

```
#! /usr/bin/env python
print("bonjour !")
```

Placez le dans votre dossier `$HOME/.local/bin` et faites en sorte de pouvoir l'exécuter de partout en modifiant le path.
{% endexercice %}
{% details "solution" %}

- créer le fichier au bon endroit
- modifier les droits pour le rendre exécutable
- dans le fichier `.profile`, modifier le `$PATH` pour qu'il accepte le chemin `export PATH=${PATH}:${HOME}/.local/bin`

{% enddetails %}