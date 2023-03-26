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

{% attention %}
N'oubliez pas qu'il faut utiliser le programme python associé à vscode. Ce ne sera pas toujours juste `python`.

Référez vous à [ce tutoriel]({{ "/tutoriels/vsc-python" }}#quel-python) pour le trouver facilement.
{% endattention %}

## <span id="installation-coverage"></span> Installation

### Coverage pour pytest

On va utiliser le *code coverage* de pytest :

{% details "sous linux et mac" %}

`python3 -m pip install pytest-cov`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pytest-cov`

{% enddetails %}

Ce module python installe deux choses :

* le module de couveture de code [coverage](https://coverage.readthedocs.io/en/6.3.1/index.html)
* l'utilisation de coverage avec pytest : [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)

### Extension vscode

Puis l'extension de vscode qui permet de rendre compte du coverage dans l'interface. Tapez [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) dans le *menu affichage > extensions*.

## <span id="code-coverage"></span> Utilisation

### Utiliser coverage sans pytest

En 2 temps :

* exécution de la couverture de code : `python3 -m coverage run [mon_fichier]`. Cette exécution crée un fichier `.coverage`{.fichier} qui contient le rapport d'exécution
* visualisation du rapport : `python3 -m coverage report`

{% lien %}
Il est possible de paramétrer très finement le rapport. Lisez la documentation pour voir toutes les possibilités :

<https://coverage.readthedocs.io/en/7.1.0/cmd.html#coverage-summary-coverage-report>

{% endlien %}

### Couverture de code avec pytest

Dans un terminal tapez `python3 -m pytest --cov=.`. Cela exécute les tests à partir du dossier courant (`.`) avec le coverage qui sera retourné au format texte.

Si l'on veut les ligne manquantes, on peut utiliser la commande : `--cov-report term-missing`

Enfin, pour avoir un rapport html complet on peut utiliser la ligne : `python3 -m pytest --cov=. --cov-report html`.

### Utilisation de l'extension **Coverage Gutters*

La commande `python3 -m pytest --cov=.` crée un fichier de coverage qui s'appelle `.coverage`. Il n'est cependant pas lisible dans ce format par défaut par l'extension. Il faut générer un format de sorti en [xml](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) avec la commande : `python3 -m pytest --cov=.  --cov-report xml:cov.xml`

{% info %}
Si le petit *watch* n'est pas visible dans la barre de status, vous pouvez le faire à la main dans avec la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande))
 *Coverage Gutters: Display Coverage*.
{% endinfo %}
