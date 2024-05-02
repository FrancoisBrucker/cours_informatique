---
layout: layout/post.njk

title: Modules python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> reprendre partie module et comment ça marche en cherchant un module python
> montrer le chemin
> on a vu avec un fichier et l'espace de nom associé
> parfois nested. Travailler avec des dossiers et `__init__.py`{.fichier}


## Où sont les modules ?

Les dossiers où python va cherchez les modules sont listés dans la variable `sys.path`.

vous pouvez le voir en exécutant le code :

```python
import sys
for dossier in sys.path:
   print(dossier)
```

Chez moi, sur un mac où python est installé avec [brew](https://brew.sh/) ce programme rend :

```shell
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
/Users/fbrucker/Library/Python/3.11/lib/python/site-packages
/opt/homebrew/lib/python3.11/site-packages
/opt/homebrew/lib/python3.11/site-packages/gpg-1.22.0-py3.11-macosx-13-arm64.egg
/opt/homebrew/opt/python-tk@3.11/libexec
```

Il y a plusieurs dossiers :

- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier _"random.py"_ qui contient le code du package `random`)
- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
- `/opt/homebrew/lib/python3.11/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

{% attention %}
La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilisant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connaît.
{% endattention %}

### Modules et projets

> TBD C'est un vrai soucis. plusieurs projet avec des modules pythons incompatibles, ou des modules inutiles pour certains projets.
> TBD : pour éviter les soucis. il faut n'avoir que les modules utiles pour chaeu projet.
> Environnement d'exécution.

> dépendances dans un projet

#### Environnements virtuels

> TBD venv

<https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>

> <https://code.tutsplus.com/understanding-virtual-environments-in-python--cms-28272t>
> <https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html>
> <https://python-poetry.org/>
> <https://linuxfr.org/news/python-partie-7-environnements-virtuels>

#### poetry

plutôt que de mettre les python alternatifs dans le projet, il les place tous au même endroit.

> Gestions des dépendances d'un projet.
