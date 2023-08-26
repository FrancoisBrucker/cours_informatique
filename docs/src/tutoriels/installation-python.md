---
layout: layout/post.njk 

title: Installation de python
authors: 
    - François Brucker
tags: ['tutoriel', 'python']

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Tutoriels
---

<!-- début résumé -->

Comment installer et utiliser python sur son ordinateur. On y verra différentes solutions.

<!-- fin résumé -->

## Plan

1. [Qu'est ce que python](./#python-){.interne}
2. [Installation](./#installation){.interne}
3. [Tests de fonctionnement avec un terminal](./#interpréteur-id){.interne}
4. [Installation de nouveaux packages](./#packages){.interne}

## <span id="python-"></span> Python ?

{% lien %}
<https://fr.wikipedia.org/wiki/Python_(langage)>
{% endlien %}

Stricto sensu, [Python](https://www.python.org/) est un langage de programmation initialement développé par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum) pour le bien des développeurs et de l'humanité.

Pour pouvoir écrire du code python et l'exécuter sur votre ordinateur, il vous faudra quelques outils :

* **[un éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)**. Il vous permettra d'écrire du code dans le langage python et de le sauver dans des [fichiers texte](https://fr.wikipedia.org/wiki/Fichier_texte). Par défaut, l'extension de fichier python est *".py"*. Par exemple, un fichier nommé *"hello.py"* à toute les chance d'être un programme python.
* **[un interpréteur python](https://docs.python.org/fr/3/tutorial/interpreter.html)**. C'est un programme qui *exécute* du code python. L'interpréteur python étant un programme, il est différent selon son système d’exploitation (mac, linux ou windows par exemple). Lorsque l'on *installe* python, c'est en fait l'interpréteur qu'on installe sur sa machine.
* **[des bibliothèques](https://geekflare.com/fr/popular-python-libraries-modules/)**. Une bibliothèque, module ou encore package python est un ensemble de fichiers de code permettant de réaliser une ou plusieurs taches précises (comme [numpy](https://numpy.org/) pour le calcul scientifique ou [flask](https://flask.palletsprojects.com/) pour créer des serveur web). L'utilisation de bibliothèques permet de créer rapidement des programmes python robuste et efficaces (avant de coder quelque chose, vérifiez s'il n'existe pas déjà un module le faisant... Vous gagnerez du temps). Pour installer facilement des modules, on utilise un programme nommé [`pip`](https://pypi.org/project/pip/) (package installer for python) qui va récupérer depuis le site <https://pypi.org/> (python package index) la bibliothèque demandée et va l'installer sur votre ordinateur.

### Quel python utiliser ?

**Utilisez la version 3 de python**. Il n'est pas nécessaire d'avoir la toute dernière itération de cette version (3.11.5 en août 2023), toute version 3 de python pas trop ancienne doit convenir.

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

### <span id="quel-python-jai"></span> J'ai quoi comme python ?

Nous y reviendrons, mais si vous pouvez exécuter du code python mais vous ne savez pas trop quel interpréteur vous utilisez (par exemple vous utilisez [Jupyter](https://jupyter.org/) via un intranet ou [spider](https://www.spyder-ide.org/)), il existe quelques lignes de code simples pour savoir quelle version de python on utilise.

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

## <span id="installation"></span> Installation

Nous allons ici nous concentrer sur l'installation de l'interpréteur python. Il existe plusieurs façon de faire, nous avons choisi celle qui est le plus adaptée à l'enseignement.

### Installation pour le développement

Cette partie concerne les personnes voulant coder avec python. Il pourra être utile que vous commenciez par vous familiariser avec votre système avant de procéder à l'installation :

{% aller %}
[Configurer un ordinateur pour le développement](../ordinateur-développement){.interne}
{% endaller %}

Maintenant que vous avez les connaissances et outil nécessaire, on peut procéder à l'installation de python.

{% details "sous Windows 11" %}
Utilisez le Microsoft store.

{% aller %}
[Tutoriel d'installation](https://learn.microsoft.com/fr-fr/windows/python/beginners#install-python)
{% endaller %}
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

### <span id="install-anaconda"></span>Python pour la DataScience

Si vous voulez utiliser python essentiellement via des [notebooks](https://jupyter.org/), c'est à dire lorsque vous utilisez python pour faire de l'analyse des données par exemple, vous pouvez utiliser [Anaconda](https://www.anaconda.com/) qui regroupe python, des bibliothèques de DataScience, et des moyens de les utiliser.

{% aller %}
[Tutoriel d'installation d'Anaconda](../installation-anaconda){.interne}.
{% endaller %}

{% attention %}
La distribution anaconda est faite pour être utilisée telle quelle. Il est parfois difficile d'ajouter des modules python spécifiques non initialement prévu.

Si vous voulez faire de l'informatique/algorithme en python, on préférera une autre distribution python.
{% endattention %}

## <span id="interpréteur-id"></span> Utiliser l'interpréteur python

Commencer par ouvrir une fenêtre Terminal. Si vous ne savez ps ce que c'est regardez ce [tutoriel](../terminal){.interne}

### Exécution de l'interpréteur python

{% info %}
L'interpréteur python s'appelle soit `python`, soit `python3`.

Dans la partie [installation](./#installation){.interne} on a fait en sorte que ce soit `python` pour les 3 systèmes d'exploitation. Si vous ne l'avez pas fait tapez `python3` à la place de `python` lors de l'appelle de la commande python.
{% endinfo %}

Dans un terminal, tapez la commande :

```
python
```

Si ça a marché, l'interpréteur aura donné sa version (**assurez vous que c'est bien python 3**) et vous donnera une invite de commande qui commence par `>>>`.Vous pouvez taper une ligne de python. Lorsque vous taperez sur entrée, votre ligne sera interprétée en python et donnera le résultat.

Par exemple tapez : `print(coucou !)` et l'interpréteur vous rendra `coucou !`. On ne pourrait utiliser python que comme ça, mais ce n'est pas très pratique.

Pour quitter l'interpréteur tapez `quit()` puis appuyez sur la touche entrée.

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

Dans un terminal tapez la commande :

{% details "sous Linux/Ubuntu et Macos" %}

```shell
which python
```

Ou, si `python` est un alias vers `python3` (sous Macos par exemple):

```shell
which python3
```

{% enddetails %}

{% details "sous Windows 11" %}

```
get-command python
```

{% enddetails %}

La commande devrait vous rendre l'emplacement sur votre disque dur de votre interpréteur. Vérifiez le avec un explorateur de fichier.

## <span id="packages"></span> Packages

Python vient avec une [liste de packages](https://docs.python.org/3/library/) bien fournie. On peut les utiliser via le mot clé `import` en python. Il en existe une foultitude d'autres qui permettent d'aider à coder rapidement. La liste des différents packages est disponible sur <https://pypi.org/>

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

On en aura besoin pour exécuter [`black`](../vsc-python-modules-supplémentaires#black){.interne} par exemple ou encore [`pytest`](../vsc-python-modules-supplémentaires#pytest){.interne}.

### Où sont les packages ?

 Les répertoires où python va cherchez les packages est dans la liste `sys.path`.

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

Je conseille d'utiliser [visual studio code](https://code.visualstudio.com/)

Il existe également d'autres façon d'utiliser python, en mode interactif par exemple en utilisant [Jupyter](https://jupyter.org/) avec anaconda, ou encore [Colab](https://colab.research.google.com).
