---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "DevOps"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Linux et compagnie.

{% lien %}

Support de cours : [Le cours de système et réseau](/cours/système-et-réseau){.interne}.
{% endlien %}

## Cours 1

### Programme

Base de Linux

- Ordinateur
  - [partie matériel](/cours/système-et-réseau/architecture-ordinateur/){.interne}
  - [partie logicielle](/cours/système-et-réseau/système-exploitation/){.interne}
- [Base de Linux](/cours/système-et-réseau/linux/bases-linux/){.interne}

### A faire pour la prochaine fois

{% faire %}
[Exercices dans le terminal](/cours/système-et-réseau/linux/bases-linux/exercices/){.interne}

Et m'envoyer un compte rendu par mail.
{% endfaire %}

## Cours 2

### Programme

Système Linux et connexions distantes

- [ssh](/cours/système-et-réseau/ssh/){.interne} :
  - principe
  - connexion à aioli
- [bases de réseau](/cours/système-et-réseau/réseau/){.interne}

### A faire pour la prochaine fois

{% faire %}

- se connecter depuis son ordinateur personnel à aioli
- mettre un fichier html dans son dossier static et le voir s'afficher sur un navigateur

{% endfaire %}

## Cours 3

- [organisation d'un système Linux](/cours/système-et-réseau/linux/système-exploitation-linux/){.interne}
- [le shell](/cours/système-et-réseau/linux/shell/){.interne} :
  - sa configuration
  - scripting

{% faire %}
[Exercices de scripting](/cours/système-et-réseau/linux/shell/exercices/){.interne}
{% endfaire %}

- mise en production :
  - déploiement
  - démon
  - log
- séparer développement et de production via des variables d'environnement
- gestion des bases données
- mots de passes et git

### Préparation

{% faire %}
Venez avec vos sites en local, genre réact, vue.
{% endfaire %}

### A faire

Sur aioli

1. fichier html static
2. serveur :
   1. nc et vérifier qu'on y accède
   2. node basique et vérifier que tout fonctionne
3. survivre à la déconnexion :
   1. nohup
   2. tmux (ou screen) <https://brainhack-princeton.github.io/handbook/content_pages/hack_pages/tmux.html>
4. npm en front
5. script d'installation :
   1. sur aioli
   2. chez soit qui pousse le tout avec un scp/git et configure là-bas (<https://stackoverflow.com/questions/18522647/run-ssh-and-immediately-execute-command>)
   3. env dev et prod : <https://nodejs.org/en/learn/command-line/how-to-read-environment-variables-from-nodejs>
6. redirection de ports
