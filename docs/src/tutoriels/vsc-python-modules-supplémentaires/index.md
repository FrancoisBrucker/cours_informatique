---
layout: layout/post.njk

title: Outils complémentaires pour Vsc et python
tags: ['tutoriel', 'vsc', 'python']
authors: 
    - François Brucker

eleventyNavigation:
  prerequis:
      - '../vsc-python/'

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title }}"
        parent: Tutoriels
---

<!-- début résumé -->

Ce tutoriel se consacre à l'installation d'extensions non fondamentales mais bien sympathiques pour le développement en python avec vscode.

<!-- fin résumé -->

## <span id="pytest"></span> Tests

{% aller %}
[Installation de pytest](pytest)
{% endaller %}

## <span id="pycodestyle"></span> Linter

{% aller %}
[Installation de pycodestyle](pycodestyle)

{% endaller %}

## <span id="black"></span> Black

{% aller %}
[Installation de black](black)
{% endaller %}

## <span id="code-coverage"></span> Couverture de code

{% aller %}
[Installation de coverage](code-coverage)
{% endaller %}
