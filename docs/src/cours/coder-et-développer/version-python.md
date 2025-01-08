---
layout: layout/post.njk

title: Interpréteurs python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous sommes actuellement (janvier 2025) à la version 3.13 de python. Il n'est souvent pas nécessaire d'avoir la toute dernière version de python pour exécuter un programme, toute version 3 de python pas trop ancienne doit convenir.

{% note %}
Si vous installez python pour la première fois sur votre ordinateur, choisissez d'installer la dernière version stable de python 3.
{% endnote %}

Une version de python est composée de 3 nombres [MAJOR.MINOR.PATCH](https://semver.org/) :

1. **MAJOR** : pour nous sera 3.
2. **MINOR** : chaque année une nouvelle itération arrive, avec son lot de nouveautés en terme de structures de données ou de bibliothèques.
3. **PATCH** : correctifs.

Chaque année sort une nouvelle version de python (voir les différentes [versions de python](https://devguide.python.org/versions/#versions)), les anciennes versions sont maintenues 5 ans avant d'être considérées comme obsolètes. Chaque version vient avec son [changelog](https://fr.wikipedia.org/wiki/Changelog), qui donne ses nouveautés et changements par rapport à la version précédente (voir le [changelog des différentes versions de python](https://docs.python.org/fr/3/whatsnew/changelog.html#changelog))

{% info %}
La version majeur actuelle de python est 3, il n'y pas prévu d'en changer avant un certain temps.
{% endinfo %}

## <span id="quel-python-jai"></span> J'ai quoi comme python ?

Pour connaître la version spécifique de python, on peut utiliser [la constante `version`du module `sys`de python](https://docs.python.org/fr/3/library/sys.html#sys.version) :

```python
import sys
print(sys.version)
```

qui rend chez moi :

```shell
3.13.1 (main, Dec  3 2024, 17:59:52) [Clang 16.0.0 (clang-1600.0.26.4)]
```

C'est à dire que j'utilise la version 3.13.1 de python et que mon interpréteur a été compilé par [Clang](https://clang.llvm.org/) (c'est sur un mac).

On peut aussi le faire sur uN terminal :

```
python --version
```

Chez moi ça rend :

```
Python 3.13.1
```

{% info %}
Pour connaître tous les paramètres possible, on peut soit se référer à la [documentation](https://docs.python.org/3/using/cmdline.html), soit taper : `python --help`
{% endinfo %}

## Et python 2 ?

Depuis le 1er janvier 2020, la version majeure 2 de python est obsolète, **il ne faut plus l'utiliser**. Vos programmes seront en effet difficilement maintenable, peu utilisable et vous passerez pour un (gros) nul.

Il n'y a **aucune** bonne raison d'utiliser la version 2 de python pour écrire des programmes actuellement.

{% attention %}
Il existe sur le net encore beaucoup d'exemples utilisant la version 2 de python, ou certains profs un peu feignant qui ne passent pas leurs exemples/cours en python 3. Plutôt que d'utiliser python2, il est recommandé de convertir ces programmes dans la version 3 et de demander la mise à jour des cours...
{% endattention %}

## <span id="interpréteur-emplacement"></span>Emplacement de votre interpréteur

L'interpréteur python est un programme comme un autre. Il est parfois utile de savoir dans quel dossier il se trouve. Il existe pour cela des commandes terminal bien pratique :

{% details "sous Windows 11", "open" %}

```
get-command python
```

{% enddetails %}

{% details "sous Linux/Ubuntu et Macos", "open" %}

```shell
which python
```

Ou, si `python` est un alias vers `python3` (sous Macos par exemple):

```shell
which python3
```

{% enddetails %}

La commande devrait vous rendre l'emplacement sur votre disque dur de votre interpréteur. Vérifiez le avec un explorateur de fichier.
