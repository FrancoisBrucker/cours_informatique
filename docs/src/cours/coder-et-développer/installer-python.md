---
layout: layout/post.njk 

title: Installation d'un interpréteur python

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous sommes actuellement (décembre 2023) à la version 3.13 de python. Il n'est souvent pas nécessaire d'avoir la toute dernière version de python pour exécuter un programme, toute version 3 de python pas trop ancienne doit convenir.

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

### <span id="installation-développement"></span>Installation pour le développement

Cette partie concerne les personnes voulant coder avec python. Il pourra être utile que vous commenciez par vous familiariser avec votre système avant de procéder à l'installation :

{% details "sous Windows 11" %}
Utilisez le Microsoft store.

{% lien %}
[Tutoriel d'installation](https://learn.microsoft.com/fr-fr/windows/python/beginners#install-python)
{% endlien %}
{% enddetails %}

{% details "sous Linux/Ubuntu" %}
Python est installé par défaut, mais il ne contient pas le module pip permettant d'installer de nouveaux modules à python. Pour installer pip, tapez dans un [terminal](../terminal){.interne} :

```
sudo apt install python3-pip
```

De plus, le python d'installé ne contient pas non plus le module [Tkinter](https://docs.python.org/fr/3/library/tkinter.html). Ceci pose des problèmes lorsque l'on veut utiliser le [module turtle](https://docs.python.org/fr/3/library/turtle.html).

Pour installer une version de python avec Tkinter, tapez dans un [terminal](../terminal){.interne} :

```
sudo apt install python3-tk
```

Enfin, la commande pour taper python est `python3`. Pour avoir le même comportement que sous windows où cette commande s'appelle juste `python`, vous pouvez installer :

```
sudo apt install python-is-python3
```

Vous pourrez uniquement taper `python` dans un terminal pour exécuter l'interpréteur python,
{% enddetails %}

{% details "sous Macos" %}
De même que sous Linux/Ubuntu, python est installé par défaut, mais pas le module [Tkinter](https://docs.python.org/fr/3/library/tkinter.html). Ceci pose des problèmes lorsque l'on veut utiliser le [module turtle](https://docs.python.org/fr/3/library/turtle.html).

Il va falloir installer python avec [brew](../brew){.interne} puis. Dans un [terminal](../terminal){.interne} tapez :

```
brew install python-tk
```

Enfin, la commande pour taper python est `python3`. Pour avoir le même comportement que sous windows où cette commande s'appelle juste `python`, vous pouvez taper dans un terminal :

```shell
echo "alias python=python3" >> ~/.zshrc
```

{% enddetails %}

### <span id="quel-python-jai"></span> J'ai quoi comme python ?

Nous y reviendrons, mais si vous pouvez exécuter du code python mais vous ne savez pas trop quel interpréteur vous utilisez (par exemple vous utilisez [Jupyter](https://jupyter.org/) via un intranet, [spider](https://www.spyder-ide.org/) ou <https://basthon.fr/>), il existe quelques lignes de code simples pour savoir quelle version de python on utilise.

Pour connaître la version spécifique de python, on peut utiliser [la constante `version`du module `sys`de python](https://docs.python.org/fr/3/library/sys.html#sys.version) :

``` python
import sys
print(sys.version)
```

qui rend chez moi :

```shell
3.11.4 (main, Jun 20 2023, 17:23:00) [Clang 14.0.3 (clang-1403.0.22.14.1)]
```

C'est à dire que j'utilise la version 3.11.4 de python et que mon interpréteur a été compilé par [Clang](https://clang.llvm.org/) (c'est sur un mac).

### Et python 2 ?

Depuis le 1er janvier 2020, la version majeure 2 de python est obsolète, **il ne faut plus l'utiliser**. Vos programmes seront en effet difficilement maintenable, peu utilisable et vous passerez pour un (gros) nul.

Il n'y a **aucune** bonne raison d'utiliser la version 2 de python pour écrire des programmes actuellement.

{% attention %}
Il existe sur le net encore beaucoup d'exemples utilisant la version 2 de python, ou certains profs un peu feignant qui ne passent pas leurs exemples/cours en python 3. Plutôt que d'utiliser python2, il est recommandé de convertir ces programmes dans la version 3 et de demander la mise à jour des cours...
{% endattention %}

## <span id="interpréteur-id"></span> Utiliser l'interpréteur python

Commencer par ouvrir une fenêtre Terminal. Si vous ne savez pas ce que c'est lisez ce [tutoriel](../terminal){.interne}

### Exécution de l'interpréteur python

{% faire %}
Ouvrez un terminal et tapez la commande `python` puis appuyez sur la touche entrée.
{% endfaire %}
{% info %}
Si vous n'avez pas suivi la méthode d'installation pour Linux/Ubuntu ou que vous êtes sous mac, il est possible que vous deviez taper la commande `python3` pour avoir un interpréteur python.
{% endinfo %}

Si ça a marché, l'interpréteur aura donné sa version (**assurez vous que c'est bien python 3**) et vous donnera une invite de commande qui commence par `>>>`.Vous pouvez taper une ligne de python. Lorsque vous taperez sur entrée, votre ligne sera interprétée en python et donnera le résultat.

{% faire %}

1. Tapez  la commande python : `print(Bonjour monde !)` et assurez vous du résultat pour être sur que tout se passe comme prévu et que votre interpréteur fonctionne.
2. quittez l'interpréteur pour revenir au terminal en tapant la commande `quit()`.

{% endfaire %}

### Version de l'interpréteur python

Beaucoup de programme supportent d'être lancé avec des paramètres, que l'on ajoute à la suite du nom. Par exemple pour connaître la version de l'interpréteur, on tape dans un terminal :

```
python --version
```

Chez moi ça rend :

```
Python 3.11.5
```

{% info %}
Pour connaître tous les paramètres possible, on peut soit se référer à la [documentation](https://docs.python.org/3/using/cmdline.html), soit taper : `python --help`
{% endinfo %}

### Emplacement de votre interpréteur

L'interpréteur python est un programme comme un autre. Il est parfois utile de savoir dans quel dossier il se trouve. Il existe pour cela des commandes terminal bien pratique :

{% details "sous Windows 11" %}

```
get-command python
```

{% enddetails %}

{% details "sous Linux/Ubuntu et Macos" %}

```shell
which python
```

Ou, si `python` est un alias vers `python3` (sous Macos par exemple):

```shell
which python3
```

{% enddetails %}

La commande devrait vous rendre l'emplacement sur votre disque dur de votre interpréteur. Vérifiez le avec un explorateur de fichier.

## <span id="packages"></span> Packages

Python vient avec une [liste de packages](https://docs.python.org/fr/3/library/) bien fournie. On peut les utiliser via le mot clé `import` en python. Il en existe une foultitude d'autres qui permettent d'aider à coder rapidement. La liste des différents packages est disponible sur <https://pypi.org/>

{% info %}
Avec <https://colab.research.google.com> il est même possible d'[installer ses propres modules](https://colab.research.google.com/notebooks-analyse/snippets/importing_libraries.ipynb#scrollTo=kDn_lVxg3Z2G).
{% endinfo %}

### Installation avec pip

Pour installer de nouveaux packages python, on utilise la commande `pip`.

Testez le en ouvrant un terminal et en tapant :

```
python -m pip --version
```

La commande devrait vous rendre le numéro de version de pip ainsi que le chemin du programme python qui lui est associé.

Les packages déjà installé par pip seront visible avec la commande :

```
python -m pip list
```

Si vous avez une distribution anaconda, vous devriez avoir plein de choses, sinon, beaucoup moins.

On peut maintenant utiliser pip pour installer un nouveau package. Nous allons installer [black](https://pypi.org/project/black/) qui rendra joli tous nos programmes python. Dans un terminal tapez :

```
python -m pip install black
```

Une fois l'installation terminée, black devrait apparaître dans la liste des packages installés (vous pouvez le voir avec `python -m pip list`).

### Exécuter un module dans le terminal

Une fois installé, il est tout à fait possible d'exécuter un module :

```
python -m <nom du module>
```

Par exemple pour exécuter le module random de python, vous pouvez taper tans un terminal la commande : `python -m random`. Cette exécution va montrer un panel des possibilités du module random de python.

### Où sont les packages ?

Les dossiers où python va cherchez les packages sont listés dans la variable `sys.path`.

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

* `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier *"random.py"* qui contient le code du package `random`)
* `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
* `/opt/homebrew/lib/python3.11/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

{% attention %}
La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilisant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connaît.
{% endattention %}

## Éditeur

Il en existe une multitude. Prenez en un qui permettent non seulement d'écrire aisément du code python mais aussi d'exécuter facilement tout ce qui va avec écrire du code :

* coloration syntaxique
* nommage et re-nommage de variables sur tout un projet
* lancer des tests
* ...

Je conseille d'utiliser [visual studio code](https://code.visualstudio.com/), mais il en existe beaucoup d'autres selon vos envies et/ou besoin.
