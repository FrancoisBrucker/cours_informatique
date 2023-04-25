---
layout: layout/post.njk

title: "Outils complémentaires pour Vsc et python : linter"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

<!-- fin résumé -->

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

## <span id="installation-pycodestyle"></span> Installation

Dans un [terminal](../terminal){.interne},
qui peut être [celui de vscode](./vsc-terminal#terminal-intégré){.interne} tapez la commande :

{% details "sous linux et mac" %}

`python3 -m pip install pycodestyle`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pycodestyle`

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

## <span id="configuration-pycodestyle"></span> Configuration

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

{% info %}
Notez que vous pouvez aussi accéder à ces commande via la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande){.interne},par exemple avec la commande *python: enable/disable linting*.
{% endinfo %}

## Pycodestyle dans le terminal

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py` dans un [terminal intégré](../vsc-terminal#terminal-intégré){.interne} pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

## Style

Certaines erreurs de pycodestyle sont énervante, car ce n'en sont pas vraiment (comme le nombre maximum de caractère dans une ligne). On peut le configurer pour qu'il *oublie* ces erreurs.

La liste des différentes erreur est [disponible dans la doc](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes). L'erreur de ligne trop longue est ainsi l'erreur `E501`.

Nous pouvons ajouter dans la configuration de pycodestyle pour vscode au paramètre `python.linting.pycodestyleArgs` la ligne `--ignore=E501`.
