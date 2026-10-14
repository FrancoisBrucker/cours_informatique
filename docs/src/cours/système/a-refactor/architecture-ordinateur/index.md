---
layout: layout/post.njk

title: Architecture d'un ordinateur

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Carte mère

{% aller %}
[Carte mère](./carte-mère)
{% endaller %}

## Mémoire

{% aller %}
[Mémoire](./mémoire)
{% endaller %}

## Processeur

{% aller %}
[Processeur](./processeur)
{% endaller %}

## Périphériques

On y accède via des protocoles d'accès. Ensuite chaque type de périphérique aura un ou plusieurs protocoles permettant son utilisation.

Exemple du réseau :

- protocole d'accès à la carte : PCie
- protocole d'utilisation :
  - TCP
  - UDP
  - ...

Les périphériques présents sur tous les ordinateurs sont les périphériques de stockage, dont nous allons parler plus précisément :

{% aller %}
[Disques durs et autres périphériques de stockage](./device-stockage)
{% endaller %}

## <span id="général"></span>Version détaillée

> TBD : à refaire.

![schéma détaillé](schéma-détaillé-ordinateur.png)
