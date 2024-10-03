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

Support de cours : [Le cours de système](/cours/système){.interne}.
{% endlien %}

## Cours 1

### Programme

- Ordinateur
  - [partie matériel](/cours/système/architecture-ordinateur/)
  - [partie logicielle](/cours/système/système-exploitation/)
- [Base de Linux](/cours/système/linux/bases-linux/)

### A faire pour la prochaine fois

{% faire %}
[Exercices dans le terminal](/cours/système/linux/bases-linux/exercices/)

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