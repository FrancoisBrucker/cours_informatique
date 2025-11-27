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

{% lien %}

- [quelques liens](https://www.youtube.com/watch?v=Jllnhid7O7w)
- [Cheat sheet par type](https://github.com/lazyoracle/linux-cheatsheet)
- [Cheat sheet terminal et liste commandes](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)

{% endlien %}

Le shell est ce via quoi on exécute des commandes.

## Exécution de commandes

> simple
> retour 0 = ok et sinon message d'erreur
> redirection entrée/sortie/erreur

## Variables d'environnement

Pour que l'environnement de travail soit :

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
