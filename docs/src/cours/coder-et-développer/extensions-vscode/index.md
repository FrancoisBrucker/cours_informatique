---
layout: layout/post.njk

title: Outils Complémentaires vscode

eleventyNavigation:
  prerequis:
    - "../../../bases-programmation/éditeur-vscode/"
    - "../../../connaissances-système-minimales/terminal/terminal-vscode/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD chapeau

VScode étant IDE très utilisé, il possède de nombreuses extensions permettant de personnaliser au mieux son expérience de développement. [On a déjà installé des extensions vscode](/cours/coder-et-développer/éditeur-vscode/prise-en-main#extensions){.interne}, nous allons dans cette partie nous focaliser sur celles permettant d'optimiser le développement.

## <span id="code-coverage"></span> Couverture de code

> TBD à déplacer à la toute fin

{% aller %}
[Installation de coverage](code-coverage){.interne}
{% endaller %}
