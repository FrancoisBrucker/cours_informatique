---
layout: layout/post.njk

title: "Outils complémentaires pour Vsc et python : code coverage"

eleventyNavigation:
  key: "Outils complémentaires pour Vsc et python : code coverage"
  parent: "Outils complémentaires pour Vsc et python"
---

<!-- début résumé -->

Permet de voir le code couvert par les tests.

<!-- fin résumé -->

## <span id="installation-coverage"></span> Installation

### Coverage pour pytest

On va utiliser le *code coverage* de pytest :

{% details "sous linux et mac" %}

`python3 -m pip install pytest-cov`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pytest-cov`

{% enddetails %}

### Extension vscode

Puis l'extension de vscode qui permet de rendre compte du coverage dans l'interface. Tapez [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) dans le *menu affichage > extensions*.

## <span id="code-coverage"></span> Utilisation

La documentation complète du module est disponible à cette adresse : <https://pytest-cov.readthedocs.io/en/latest/>.

Ce module utilise [coverage](https://coverage.readthedocs.io/en/6.3.1/index.html), qui est le module de couverture de code utilisé. Il est très configurable.

### Sans l'extension

Dans un terminal tapez `python3 -m pytest --cov=.`. Cela exécute les tests à partir du dossier courant (`.`) avec le coverage qui sera retourné au format texte.

Si l'on veut les ligne manquantes, on peut utiliser la commande : `--cov-report term-missing`

Enfin, pour avoir un rapport html complet on peut utiliser la ligne : `python3 -m pytest --cov=. --cov-report html`.

### Utilisation de l'extension

La commande `python3 -m pytest --cov=.` crée un fichier de coverage qui s'appelle `.coverage`. Il n'est cependant pas lisible dans ce format par défaut par l'extension. Il faut générer un format de sorti en [xml](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) avec la commande : `python3 -m pytest --cov=.  --cov-report xml:cov.xml`

{% info %}
Si le petit *watch* n'est pas visible dans la barre de status, vous pouvez le faire à la main dans avec la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande))
 *Coverage Gutters: Display Coverage*.
{% endinfo %}
