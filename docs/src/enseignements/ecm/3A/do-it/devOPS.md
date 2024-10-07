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

- ssh
- le shell :
  - sa configuration
  - scripting
- bases de réseau

### A faire pour la prochaine fois

> TBD