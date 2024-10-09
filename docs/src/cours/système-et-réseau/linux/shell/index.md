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

[DM](DM){.interne}

{% endaller %}
