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

### Extension vscode

Pour utiliser black directement avec vscode, **installez [l'extension vscode](../../../prise-en-main#extensions){.interne}** nommée "*black formatter*" développé par microsoft.

### Module python

Dans [un terminal](../../../../ordinateur-développement/terminal){.interne}, qui peut être celui de vscode, tapez la commande :

```shell
python -m pip install black
```

Ceci vous permettra d'utiliser black dans le terminal. De plus, l'extension vscode va préférentiellement utiliser votre version de flake8 que la sienne.

## Utilisation

En cliquant droit sur du code puis choisir "Mettre le document en forme" utilisera black pour mettre en forme le code python.

Vous pouvez aussi :

* exécuter directement la commande *format document* dans [palette de commande](../../../prise-en-main#palette-de-commande){.interne}.
* cocher le paramètre `editor.formatOnSave` dans les préférences.

## Black dans le terminal

```shell
python -m black mon-fichier.py
```
