---
layout: layout/post.njk

title: Éditeur vscode
tags: ['tutoriel', 'éditeur', 'vsc']
authors:
    - François Brucker

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Configuration et utilisation de l'éditeur de texte [visual studio code (vsc)](https://code.visualstudio.com/).

## Installation

Si vous ne l'avez pas déjà fait :

{% faire %}
Téléchargez [vscode](https://code.visualstudio.com/) et installez le.
{% endfaire %}
{% info %}
Sous Linux/Ubuntu, choisissez l'[installation via snap](https://code.visualstudio.com/docs/setup/linux#_snap) dans un terminal :

```
sudo snap install --classic code
```

{% endinfo %}

## Bases

Commençons par faire le tour du propriétaire :

{% aller %}
[Prise en main](prise-en-main){.interne}
{% endaller %}

## vscode et python

{% aller %}
[vscode et python](python){.interne}
{% endaller %}

## Préférences

Vscode possède une foultitude de préférences qui le rendent très modulable et lui permettent de s'adapter à (presque) toutes vos envies et besoins.

Je vous conseille très fortement d'aller y jeter un coup d'œil :

{% lien %}
[préférences vscode](https://code.visualstudio.com/docs/getstarted/settings)

{% endlien %}
