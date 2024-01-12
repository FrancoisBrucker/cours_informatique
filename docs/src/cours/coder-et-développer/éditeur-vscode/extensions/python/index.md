---
layout: layout/post.njk

title: Outils complémentaires pour Vsc et python
tags: ['tutoriel', 'éditeur', 'vsc', 'python']
authors:
    - François Brucker


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce tutoriel se consacre à l'installation d'extensions non fondamentales mais bien sympathiques pour le développement en python avec vscode.

## <span id="pytest"></span> Tests

{% aller %}
[Installation de pytest](pytest){.interne}
{% endaller %}

## <span id="flake8"></span> Linter

{% aller %}
[Installation de flake8](flake8){.interne}

{% endaller %}

## <span id="black"></span> Black

{% aller %}
[Installation de black](black){.interne}
{% endaller %}

## <span id="code-coverage"></span> Couverture de code

{% aller %}
[Installation de coverage](code-coverage){.interne}
{% endaller %}
