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

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [flake8](https://flake8.pycqa.org/en/latest/) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

## <span id="installation-flake8"></span> Installation

Dans un [terminal](../terminal){.interne}, qui peut être [celui de vscode](./vsc-terminal#terminal-intégré){.interne} tapez la commande :

```shell
python -m pip install flake8
```

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode après avoir installé l'[extension vscode](/tutoriels/éditeur-vscode/prise-en-main#extensions){.interne} nommée "*flake8*" développé par microsoft.

## Utilisation

Une fos installée, l'extension est automatiquement activée et elle va souligner en rouge toute faute de  style.

## flake8 dans le terminal

Vous pouvez aussi toujours exécuter la commande `flake8 mon-fichier.py` dans un [terminal intégré](../vsc-terminal#terminal-intégré){.interne} pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.
