---
layout: layout/post.njk

title: "Outils complémentaires pour Vsc et python : pytest"
authors:
  - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous utilisons [pytest](https://docs.pytest.org/) comme bibliothèque de test.

{% lien %}
[tests avec vscode](https://code.visualstudio.com/docs/python/testing)
{% endlien %}

## <span id="installation-pytest"></span> Installation

```shell
python -m pip install pytest
```

## <span id="configuration-pytest"></span> Configuration

1. dans les préférences (_menu file/code > Préférences > settings_) tapez `python.testing.pytestEnabled` dans la barre de recherche et cochez la case. Ceci dit à vscode que notre framework de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (dans la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande){.interne}) : _python : Configure tests_ on choisit _pytest_ puis _. (root)_ qui donne le dossier de départ où aller chercher nos tests

## <span id="utilisation-pytest"></span> Utilisation

{% faire %}
Créez un fichier que vous appellerez `test_projet.py`{.fichier} dans votre projet. Collez-y- le code suivant :

```python
def test_oui():
    assert 4 == 2 + 2


def test_non():
    assert "4" == 2 + 2
```

{% endfaire %}

Le fichier créé est un fichier de test. Il faut l'utiliser via la bibliothèque `pytest` que vous venez d'installer. Ceci peut se faire directement avec vscode en ouvrant la fenêtre de tests avec _Menu Affichage testing_ (le petit erlenmeyer de la [barre d'activité](https://code.visualstudio.com/docs/getstarted/userinterface)).

En suite le menu _TESTING_ en haut de cette nouvelle fenêtre vous permet :

- redécouvrir les tests
- exécutez les tests.
- ...

![tests](../python-pytest-env.png)

On peut également directement utiliser pytest avec le terminal, en tapant `python -m pytest` alors que vous êtes dans le dossier du projet.
