---
layout: layout/post.njk

title: "Outils complémentaires pour Vsc et python : code coverage"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## <span id="installation-coverage"></span> Installation

### Coverage pour pytest

On va utiliser le _code coverage_ de pytest :

```
python -m pip install pytest-cov
```

Ce module python installe deux choses :

- le module de couverture de code [coverage](https://coverage.readthedocs.io/en/7.4.1/)
- l'utilisation de coverage avec pytest : [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)

### Extension vscode

Puis l'extension de vscode qui permet de rendre compte du coverage dans l'interface. Tapez [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) dans le _menu affichage > extensions_.

## <span id="code-coverage"></span> Utilisation

### Utiliser coverage sans pytest

En 2 temps :

- exécution de la couverture de code : `python -m coverage run [mon_fichier]`. Cette exécution crée un fichier `.coverage`{.fichier} qui contient le rapport d'exécution
- visualisation du rapport : `python -m coverage report`

{% lien %}
Il est possible de paramétrer très finement le rapport. Lisez la documentation pour voir toutes les possibilités :

<https://coverage.readthedocs.io/en/7.1.0/cmd.html#coverage-summary-coverage-report>

{% endlien %}

### Couverture de code avec pytest

Dans un terminal tapez `python -m pytest --cov=.`. Cela exécute les tests à partir du dossier courant (`.`) avec le coverage qui sera retourné au format texte.

Si l'on veut les ligne manquantes, on peut utiliser la commande : `--cov-report term-missing`

Enfin, pour avoir un rapport html complet on peut utiliser la ligne : `python -m pytest --cov=. --cov-report html`.

### Utilisation de l'extension \*_Coverage Gutters_

La commande `python -m pytest --cov=.` crée un fichier de coverage qui s'appelle `.coverage`. Il n'est cependant pas lisible dans ce format par défaut par l'extension. Il faut générer un format de sorti en [xml](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) avec la commande : `python -m pytest --cov=.  --cov-report xml:cov.xml`

{% info %}
Si le petit _watch_ n'est pas visible dans la barre de status, vous pouvez le faire à la main dans avec la [palette de commande](../../../prise-en-main/#palette-de-commande){.interne}
_Coverage Gutters: Display Coverage_.
{% endinfo %}
