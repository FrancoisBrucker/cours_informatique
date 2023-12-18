---
layout: layout/post.njk

title: "Outils complémentaires pour Vsc et python : black"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

[Black](https://black.readthedocs.io/en/stable/index.html) est un bijou. Ne pas l'utiliser tout le temps est bête.

Son but est de re-formater sans faute de style tout programme python.

<!-- fin résumé -->

## <span id="installation-black"></span> Installation

Dans un [terminal](../terminal){.interne}, qui peut être [celui de vscode](../vsc-terminal#terminal-intégré){.interne} tapez la commande :

{% details "sous linux et mac" %}

`python3 -m pip install black`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install black`

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode en installant l'[extension vscode](/tutoriels/éditeur-vscode/prise-en-main#extensions){.interne} nommée "*black formatter*" de microsoft.

## Utilisation

En cliquant droit sur du code puis choisir "Mettre le document en forme" utilisera black pour mettre en forme le code python.

Vous pouvez aussi :

* exécuter directement la commande *format document* dans [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande){.interne}.
* cocher le paramètre `editor.formatOnSave` dans les préférences.

## Black dans le terminal

```shell
python -m black mon-fichier.py
```
