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

<!-- début résumé -->

Installation, configuration et utilisation de l'éditeur de texte [visual studio code (vsc)](https://code.visualstudio.com/).

<!-- fin résumé -->

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

## Prise en main

{% aller %}
[Prise en main](prise-en-main){.interne}
{% endaller %}

{% aller %}
[Utilisation du terminal](terminal){.interne}
{% endaller %}

## vscode et python

{% aller %}
[Utilisation de python](python){.interne}
{% endaller %}

{% aller %}
[Modules supplémentaires](python-suppléments){.interne}
{% endaller %}