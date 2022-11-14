---
layout: layout/post.njk 

title: Installation de python
authors: 
    - François Brucker

tags: ['tutoriel', 'python']
---

{% chemin %}
[Tutoriels]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}

<!-- début résumé -->

Comment installer et utiliser python sur son ordinateur. On y verra différentes solutions.

<!-- fin résumé -->

## Plan

1. [qu'est que python](./#python-)
2. [installation](./#installation)
3. [tests de fonctionnement avec un terminal](./#interpréteur-id)
4. [installation de nouveaux packages](./#packages)

## <span id="python-"></span> Python ?

{% chemin %}
<https://fr.wikipedia.org/wiki/Python_(langage)>
{% endchemin %}

Stricto sensu, [Python](https://www.python.org/) est un langage de programmation initialement développé par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum) pour le bien des développeurs et de l'humanité.

Pour pouvoir écrire du code python et l'exécuter sur votre ordinateur, il vous faudra quelques outils :

* **[un éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)**. Il vous permettra d'écrire du code dans le langage python et de le sauver dans des [fichiers texte](https://fr.wikipedia.org/wiki/Fichier_texte). Par défaut, l'extension de fichier python est *".py"*. Par exemple, un fichier nommé *"hello.py"* à toute les chance d'être un programme python.
* **[un interpréteur python](https://docs.python.org/fr/3/tutorial/interpreter.html)**. C'est un programme qui *exécute* du code python. L'interpréteur python étant un programme, il est différent selon son système d’exploitation (mac, linux ou windows par exemple). Lorsque l'on *installe* python, c'est en fait l'interpréteur qu'on installe sur sa machine.
* **[des bibliothèques](https://geekflare.com/fr/popular-python-libraries-modules/)**. Une bibliothèque, module ou encore package python est un ensemble de fichiers de code permettant de réaliser une ou plusieurs taches précises (comme [numpy](https://numpy.org/) pour le calcul scientifique ou [flask](https://flask.palletsprojects.com/) pour créer des serveur web). L'utilisation de bibliothèques permet de créer rapidement des programmes python robuste et efficaces (avant de coder quelque chose, vérifiez s'il n'existe pas déjà un module le faisant... Vous gagnerez du temps). Pour installer facilement des modules, on utilise un programme nommé [`pip`](https://pypi.org/project/pip/) (package installer for python) qui va récupérer depuis le site <https://pypi.org/> (python package index) la bibliothèque demandée et va l'installer sur votre ordinateur.

### Quel python utiliser ?

**Utilisez la version 3 de python**. Il n'est pas nécessaire d'avoir la toute dernière itération de cette version (3.9.6 à l'heure où je tape ces caractères), toute version 3 de python pas trop ancienne doit convenir.

{% note %}
Si vous installez python pour la première fois sur votre ordinateur, choisissez d'installer la dernière version stable de python 3.
{% endnote %}

Une version de python est composée de 3 nombres [MAJOR.MINOR.PATCH](https://semver.org/) :

1. **MAJOR** : pour nous sera 3.
2. **MINOR** : chaque année une nouvelle itération arrive, avec son lot de nouveautés en terme de structures de données ou de bibliothèques.
3. **PATCH** : correctifs.

Chaque année sort une nouvelle version de python (voir <https://devguide.python.org/#status-of-python-branches>), les anciennes versions sont maintenues 5 ans avant d'être considérées comme obsolète. Chaque version vient avec son [changelog](https://fr.wikipedia.org/wiki/Changelog), qui donne ses nouveautés et changements par rapport à la version précédente ([ici](https://docs.python.org/release/3.9.6/whatsnew/changelog.html#changelog) le changelog de la version 3.9.6)

{% info %}
La version majeur actuelle de python est 3, il n'y pas prévu d'en changer avant un certain temps.
{% endinfo %}

### Et python 2 ?

Depuis le 1er janvier 2020, la version majeure 2 de python est **obsolète**, il est donc fortement recommandé de ne plus l'utiliser. Vos programme seront en effet difficilement maintenance et de plus en plus difficilement utilisable.

Il n'y a **aucune** bonne raison d'utiliser la version 2 de python pour écrire des programmes actuellement.

{% attention %}
Il existe sur le net encore beaucoup d'exemples utilisant la version 2 de python, ou certains profs un peu feignant qui ne passent pas leurs exemple/cours en python3. Plutôt que d'utiliser python2, il est recommandé de convertir ces programmes dans la version 3 et de demander la mise à jour des cours...
{% endattention %}

### <span id="quel-python-jai"></span> J'ai quoi comme python ?

Nous y reviendrons, mais si vous pouvez exécuter du code python mais vous ne savez pas trop quel interpréteur vous utilisez (par exemple vous utilisez [Jupyter](https://jupyter.org/) via un intranet ou [spider](https://www.spyder-ide.org/)), il existe quelques lignes de code simples pour savoir quelle version de python on utilise.

#### Python 2 ou python 3

La différence la plus visible entre une version 2 et une version 3 de python est que pour une version 3 de python, le code suivant :

```python
print "j'utilise un langage obsolète"
```

 produit l'erreur :

```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("j'utilise un langage obsolète")?
 ```

Alors que le code s'exécute sans soucis avec la version 2 de python (il écrit `j'utilise un langage obsolète`).

#### Quelle version de python

On suppose que l'on utilise la version 3 de python. Pour connaître la version spécifique de python, on peut utiliser [la constante `version`du module `sys`de python](https://docs.python.org/fr/3/library/sys.html#sys.version) :

``` python
import sys
print(sys.version)
```

qui rend chez moi :

```shell
3.9.6 (default, Jun 29 2021, 05:25:02) 
[Clang 12.0.5 (clang-1205.0.22.9)]
```

C'est à dire que j'utilise la version 3.9.6 de python et que mon interpréteur a été compilé par [Clang](https://clang.llvm.org/) (c'est sur un mac).

## <span id="installation"></span> Installation

Nous allons ici nous concentrer sur l'installation de l'interpréteur python. Il existe plusieurs façon de faire. Nous en présenterons 2 :

* solution universelle simple : installez python avec [Microsoft store](https://learn.microsoft.com/fr-fr/windows/python/beginners#install-python)
* utiliser [la distribution anaconda](./#install-anaconda).
* solution informaticienne : à privilégier si vous voulez contrôler toute votre installation (c'est bien). On utilise un [gestionnaire de package](./#gestionnaire-package-id).

{% info %}
Parfois, il n'y a rien à faire (c'est souvent le cas sous mac ou Linux qui arrivent avec des versions de python 2 et 3 déjà installées). Utilisez les [tests de reconnaissances](./#quel-python-jai) pour identifier la version de python que vous avez.
{% endinfo %}

Une fois que vous aurez installé python (ou pour savoir si vous l'avez déjà installé), vérifiez le en tentant d'[exécuter l'interpréteur python dans un terminal](./#interpréteur-id).

## <span id="install-anaconda"></span> Installation via anaconda

Suivez ce [tutoriel](../installation-anaconda) pour installer anaconda sur votre machine.

### <span id="gestionnaire-package-id"></span> Installation via un gestionnaire de package

Une bonne pratique d'installation de logiciel sur son ordinateur est d'utiliser un gestionnaire de package. Il vous permet de savoir exactement ce qui est utilisé, quelle version, et surtout gère tout seul les mise à jours.

C'est un peut plus compliqué qu'utiliser anaconda mais si vous voulez faire de l'informatique sérieuse ou sérieusement de l'informatique, il est conseillé d'utiliser cette solution.

{% details "sous mac" %}

On utilise [brew](https://brew.sh/index_fr), qu'il vous faudra tout d'abord installer. Toutes les commandes se font ensuite via le [terminal](../terminal).

Une fois brew installé, vous pouvez installer python en tapant la commande :

```
brew install python
```

{% enddetails %}

{% details "sous windows" %}

Pour l'instant téléchargez le tout depuis le store. Suivez ce [tutoriel](https://docs.microsoft.com/fr-fr/windows/python/beginners) pour l'installation.

{% enddetails %}

{% details "sous Linux" %}

```
sudo apt install -y python3-pip
```

{% enddetails %}

## <span id="interpréteur-id"></span> Utiliser l'interpréteur python

Commencer par ouvrir une fenêtre Terminal. Si vous ne savez ps ce que c'est regardez ce [tutoriel](../terminal)

### Exécution de l'interpréteur python

L'interpréteur python s'appelle soit `python`, soit `python3`. Regardez celui que vous possédez.

{% attention "Sous windows, c'est souvent `python` qu'il s'appelle, sous mac et Linux c'est `python3`." %}
Pour le reste du tuto, je considérerai que c'est `python3`. Si ca ne marche pas, supprimez le 3.
{% endattention %}

Dans un terminal, tapez la commande :

```
python3
```

Si ça a marché, l'interpréteur aura donné sa version (**assurez vous que c'est bien python 3**) et vous donnera une invite de commande qui commence par `>>>`.Vous pouvez taper une ligne de python. Lorsque vous taperez sur entrée, votre ligne sera interprétée en python et donnera le résultat.

Par exemple tapez : `print(coucou !)` et l'interpréteur vous rendra `coucou !`. On ne pourrait utiliser python que comme ça, mais ce n'est pas très pratique.

Pour quitter l'interpréteur tapez `quit()` puis appuyez sur la touche entrée.

### Version de l'interpréteur python

Beaucoup de programme supportent d'être lancé avec des paramètres, que l'on ajoute à la suite du nom. Par exemple pour connaître la version de l'interpréteur, on tape dans un terminal :

```
python3 --version
```

Chez moi ça rend :

```
Python 3.9.6
```

{% info %}
Pour connaître tous les paramètres possible, on peut soit se référer à la [documentation](https://docs.python.org/3/using/cmdline.html), soit taper : `python3 --help`
{% endinfo %}

### Emplacement de votre interpréteur

Dans un terminal tapez la commande :

{% details "sous Linux et mac" %}

```shell
which python3
```

{% enddetails %}

{% details "sous windows" %}

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
python3 -m pip --version
```

La commande devrait vous rendre le numéro de version de pip ainsi que le chemin du programme python qui lui est associé.

Les packages déjà installé par pip seront visible avec la commande :

```
python3 -m pip list
```

Si vous avez une distribution anaconda, vous devriez avoir plein de choses, sinon, beaucoup moins.

On peut maintenant utiliser pip pour installer un nouveau package. Nous allons installer [black](https://pypi.org/project/black/) qui rendra joli tous nos programmes python. Dans un terminal tapez :

```
python3 -m pip install black
```

Une fois l'installation terminée, black devrait apparaître dans la liste des packages installés (vous pouvez le voir avec `python3 -m pip list`).

### Exécuter un module dans le terminal

Une fois installé, il est tout à fait possible d'exécuter un module :

```
python3 -m <nom du module>
```

On en aura besoin pour exécuter [`black`](../vsc-python-modules-supplémentaires#black) par exemple ou encore [`pytest`](../vsc-python-modules-supplémentaires#pytest).

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
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python39.zip
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload
/usr/local/lib/python3.9/site-packages
```

Il y a plusieurs dossiers :

* `/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier *"random.py"* qui contient le code du package `random`)
* `/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
* `/usr/local/lib/python3.9/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

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
