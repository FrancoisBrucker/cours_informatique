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
- [organisation d'un système Linux](/cours/système-et-réseau/linux/système-exploitation-linux/){.interne}
- [le shell](/cours/système-et-réseau/linux/shell/){.interne} :
  - sa configuration
  - scripting
- [bases de réseau](/cours/système-et-réseau/réseau/){.interne}

### A faire pour la prochaine fois

{% faire %}
[Exercices de scripting](/cours/système-et-réseau/linux/shell/exercices/){.interne}
{% endfaire %}

## Cours 3

On fait du web.

### Préparation

{% faire %}
Venez avec vos sites en local, genre réact, vue.
{% endfaire %}
