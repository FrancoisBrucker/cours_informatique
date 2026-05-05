---
layout: layout/post.njk

title:  "Gestion des dépendances"
tags: ['tutoriel']

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Les dépendances d'un projet sont de deux ordres :

- la version du langage : chaque nouvelle version peut amener son lot de modifications par rapport à des versions antérieures
- les modules externes : un projet peut utiliser des dizaines de bibliothèques différentes qu'il faut installer pour être utilisé

Nous allons ici nous concentrer sur la façon de faire de python, chaque langage va avoir ses propres façon de faire pour gérer ces deux problèmes.

## Interpréteur

Lorsque l'on veut utiliser l'interpréteur python exécuter un programme informatique que l'on aura développé, il faut s'assurer que chaque exécution du programme soit identique. Pour éviter les effets de bords (anciennes variables déclarées, modules importées, etc) Il est indispensable de pouvoir :

1. créer un nouvel interpréteur python pour **_chaque_** exécution du programme.
2. écrire notre programme en-dehors de tout interpréteur

### Versions de l'interpréteur

{% aller %}
[Version de l'interpréteur python](version-python){.interne}
{% endaller %}

### Modules utilisables

Chaque version de python va posséder :

- ses propres modules comme `math`{.language-}, `random`{.language-} ou encore `sys`{.language-}
- les modules installés par `pip`.


Les dossiers où python va cherchez ces modules sont listés dans la variable `sys.path` et dépendent de l'interpréteur utilisé (c'est pour ça qu'on installe les différents modules en utilisant la commande `python -m pip` et non directement le programme `pip`, car l'interpréteur pour lequel sera installé le module est ainsi explicite).

{% faire %}
Vous pouvez les voir en exécutant le code :

```python
import sys
for dossier in sys.path:
   print(dossier)
```
{% endfaire %}

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

## Gestion des modules

Chaque projet va dépendre de modules externes que vous avez installés avec `pip`. Mais lorsque vous voulez partager votre travail avec d'autres personnes, il leur faudra aussi installer les différents modules pour utiliser votre projet. De plus, certains de ces modules pourraient être incompatible avec leur version de python ou des modules qu'ils utilisent par ailleurs.

Python règle ces deux problèmes d'un seul coup en utilisant des environnements virtuels :

{% aller %}
[Environnements virtuels](environnements-virtuels){.interne}
{% endaller %}
