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

Dans un [terminal](../terminal),
qui peut être [celui de vscode](../vsc-terminal#terminal-intégré) tapez la commande :

{% details "sous linux et mac" %}

`python3 -m pip install black`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install black`

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

## <span id="configuration-black"></span> Configuration

A priori tout est ok sans aucune autre configuration sous vscode. On peut lister deux paramètre auxquels faire attention :

* `python.formatting.blackPath`: qui vaut `black` par défaut
* `python.formatting.provider` : qui donne l'outil de formatage de fichier par défaut utilisé, et qui vaut `black` par défaut.

## Utilisation

Si vous avez le paramètre `editor.formatOnSave` de coché à chaque sauvegarde de votre fichier, il sera reformaté. Notez que cela ne marche pas si votre fichier est sauvegardé automatiquement après un délai.

Vous pouvez aussi :

* exécuter directement la commande *format document* dans [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande).
* utiliser son [raccourci clavier](https://code.visualstudio.com/docs/editor/codebasics#_formatting)

## Black dans le terminal

{% details "sous linux et mac" %}

`python3 -m black mon-fichier.py`

{% enddetails %}

{% details "sous windows" %}

`python -m black mon-fichier.py`

{% enddetails %}

