---
layout: layout/post.njk

title: Outils complémentaires pour Vsc et python

eleventyNavigation:
  prerequis:
    - "../../../bases-programmation/éditeur-vscode/"
    - "../../../connaissances-système-minimales/terminal/terminal-vscode/"

authors:
    - François Brucker


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Extensions non fondamentales mais bien sympathiques pour le développement en python avec vscode.

## <span id="flake8"></span> Linter

{% aller %}
[Installation de flake8](flake8){.interne}

{% endaller %}

## <span id="black"></span> Black

{% aller %}
[Installation de black](black){.interne}
{% endaller %}
