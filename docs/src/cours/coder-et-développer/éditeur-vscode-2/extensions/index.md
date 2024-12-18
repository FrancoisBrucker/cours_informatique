---
layout: layout/post.njk

title: Outils Complémentaires

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

VScode étant IDE très utilisé, il possède de nombreuses extensions permettant de personnaliser au mieux son expérience de développement. [On a déjà installé des extensions vscode](/cours/coder-et-développer/éditeur-vscode/prise-en-main#extensions){.interne}, nous allons dans cette partie nous focaliser sur celles permettant d'optimiser le développement.

## Python

{% aller %}
[extensions pour python](./python){.interne}
{% endaller %}

## Markdown

{% aller %}
[extensions pour utiliser markdown](./markdown){.interne}
{% endaller %}
