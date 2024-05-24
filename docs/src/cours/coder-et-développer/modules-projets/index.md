---
layout: layout/post.njk

title: Modules et projet

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Tout projet informatique va dépendre de modules extérieurs pour son exécution. Ces modules vont être de deux ordres :

- ceux liés à l'exécution du programme, comme pyglet, matplotlib ou encore numpy
- ceux liés au développement comme pytest

La gestion de ces modules peut s'avérer fastidieuse car :

1. si vous partagez votre code, il faut une liste des modules dont dépend votre projet pour être utilisé et qu'il faut installer
2. il faut faire attention aux versions car un changement de version d'un module peut entraîner des changements dans son comportement et casser votre projet

La première solution qui vient à l'esprit est de distribuer les modules en même temps que votre projet, dans un dossier dédié. C'est cependant une **très mauvaise idée** ! En effet :

- vous vous privez des développements futurs et des corrections de bug des modules. Il vous faut redistribuer votre projet à chaque mise à jour des modules, en plus de chaque mise à jour de votre code
- vous perdez de la place et si vous utilisez un contrôleur de version (comme git) vous allez à la fois stocker votre code et du code tierce.
- certains modules peuvent être compliqué à installer et dépendent de bibliothèque de votre système. Copier leur code uniquement ne suffira pas à les installer proprement

Les remarques ci-dessus mènent à une unique conclusion :

{% note %}
Il faut utiliser un outil de gestion des dépendances qui s'occupera d'installer, de maintenir à jour et d'éviter les incompatibilités d'une liste de modules dont dépend le projet.
{% endnote %}

## Environnement Virtuel

Python ajoute une contrainte supplémentaire à la gestion des dépendances : les modules dépendent d'un interpréteur.

Si l'on a plusieurs interpréteurs installés, on peut avoir un module installé pour 1 interpréteur mais pas pour un autre. Pour s'assurer d'installer un module pour le bon interpréteur on utilise `pip` avec celui-ci en utilisant la commande (que l'on a utilisée à chaque installation de module) :

```shell
[nom de l'interpréteur] -m pip install [nom du module]
```

Si l'on veut par exemple installer le module `numpy`{.language-} pour l'interpréteur python dans le dossier `/usr/bin/` on utilise la commande :

```shell
/usr/bin/python3 -m pip install numpy
```

Pour que chaque projet ait ses propres modules d'installer pour éviter les incompatibilités, il n'y a qu'une solution :

{% note %}
Il faut installer un interpréteur spécifique pour chaque projet python. On appelle ceci un [environnement virtuel](https://en.wikipedia.org/wiki/Virtual_environment_software)
{% endnote %}

### module `venv`{.language-}

{% lien %}
[Module `venv`{.language-}](https://docs.python.org/fr/3/library/venv.html)
{% endlien %}

Il existe plusieurs modules permettant de créer et/ou gérer des environnements virtuels, nous allons utiliser ici celui fourni par python : `venv`{.language-}.

{% faire %}

1. Créez un nouveau projet avec vscode que vous placerez dans un dossier nommé `environnement_virtuel/`{.fichier}.
2. Créez un fichier `main.py`{.fichier} contenant le code :

    ```python
    import sys

    print(sys.executable)
    ```

{% endfaire %}

Vous pouvez exécuter le fichier `main.py`{.fichier} pour connaître le chemin vers l'interpréteur utilisé. Dans mon cas, lorsque j'exécute le fichier via un terminal j'obtiens :

```shell
$ python main.py
/opt/homebrew/opt/python@3.12/bin/python3.12

```

Installons un nouvel interpréteur dans le dossier du projet.

{% faire %}
Dans un terminal, assurez vous d'être dans le dossier du projet (`environnement_virtuel/`{.fichier}), puis tapez la commande :

```shell
python -m venv venv/
```

{% endfaire %}

La commande précédente va utiliser le module `venv`{.language-} de python pour créer tout ce qui est nécessaire à un environnement virtuel dans le dossier `venv/`{.fichier} du projet.

> TBD : vérifier avec windows 11.

Pour python un environnement virtuel contient :

- un interpréteur : `venv/bin/python`{.fichier}
- ses modules associés : `venv/lib/python3.12/site-packages/`{.fichier} (chez moi. Vous aurez peut-être une autre version de python). A priori, il n'y a que pip d'installé en plus des modules livrés directement avec python

Pour utiliser le nouvel interpréteur, on donne son chemin :

{% faire %}
Dans un terminal, assurez vous d'être dans le dossier du projet (`environnement_virtuel/`{.fichier}), puis tapez la commande :

```shell
venv/bin/python main.py
```

{% endfaire %}

Dans mon cas, j'obtiens :

```shell
$ venv/bin/python main.py
/Users/fbrucker/Documents/projets/environnement_virtuel/venv/bin/python

```

Ce n'est bien plus le même interpréteur qui a exécuté notre fichier.

Les packages installés sont visible en utilisant le module pip pour le nouvel interpréteur :

```shell
$ venv/bin/python -m pip list
Package Version
------- -------
pip     24.0
```

À comparer avec les modules installés pour l'interpréteur classique :

```shell
$ python -m pip list
Package           Version
----------------- -----------
appnope           0.1.4
asttokens         2.4.1
cffi              1.16.0
comm              0.2.2
contourpy         1.2.1
cycler            0.12.1

[...]

tornado           6.4
traitlets         5.14.2
wcwidth           0.2.13
wheel             0.43.0

```

> TBD activate avec le terminal ou vscode.

>
> liste des packages pour s'en rappeler et ne donner que cette liste et le code, pas l'environnement virtuel.
>
> dire qu'on peut faire mieux avec un outil dedié, poetry.
>

<https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>
> <https://code.tutsplus.com/understanding-virtual-environments-in-python--cms-28272t>
<https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html>

<https://medium.com/@sukul.teradata/understanding-python-virtual-environments-using-venv-and-virtualenv-283f37d24b13>
<https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html>
<https://linuxfr.org/news/python-partie-7-environnements-virtuels>

## poetry

3. requierment.txt pour sauver les modules utilisés ainsi que leurs versions.


<https://python-poetry.org/>

plutôt que de mettre les python alternatifs dans le projet, il les place tous au même endroit.

> Gestions des dépendances d'un projet.
