---
layout: page
title:  Installation de python
tags: installation python
authors: 
    - François Brucker
---

Comment installer et utiliser python sur son ordinateur. On y verra différentes solutions.

<!--more-->

## plan

1. [qu'est que python](#python-)
2. [installation](#installation)
   * [anaconda](#anaconda-id)
   * [gestionnaire de paquet](#gestionnaire-package-id)
3. [tests de fonctionnement avec un terminal](#interpreteur-id)
4. [installation de nouveaux packages](#packages)


## python ?

> <https://fr.wikipedia.org/wiki/Python_(langage)>

Stricto sensu, [Python](https://www.python.org/) est un langage de programmation initialement développé par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum) pour le bien des développeurs et de l'humanité.

Pour pouvoir écrire du code python et l'exécuter sur votre ordinateur, il vous faudra quelques outils :

* **un [éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)**. Il vous permettra d'écrire du code dans le langage python et de le sauver dans des [fichiers texte](https://fr.wikipedia.org/wiki/Fichier_texte). Par défaut, l'extension de fichier python est *".py"*. Par exemple, un fichier nommé *"hello.py"* à toute les chance d'être un programme python.
* **un [interpréteur python](https://docs.python.org/fr/3/tutorial/interpreter.html)**. C'est un programme qui *exécute* du code python. L'interpréteur python étant un programme, il est différent selon son système d'exploitiation (mac, linux ou windows par exemple). Lorsque l'on *installe* python, c'est en fait l'interpréteur qu'on installe sur sa machine.
* **des bibliothèques**. Une bibliothèque, module ou encore package python est un ensemble de fichiers de code permettant de réaliser une ou plusieurs taches précises (comme [numpy](https://numpy.org/) pour le calcul scientifique ou [flask](https://flask.palletsprojects.com/) pour créer des serveur web). L'utilisation de bibliothèques permet de créer rapidement des programmes python robuste et efficaces (avant de coder quelque chose, vérifiez s'il n'existe pas déjà un module le faisant... Vous gagnerez du temps). Pour installer facilement des modules, on utilise un programme nommé [*"pip"*](https://pypi.org/project/pip/) (package installer for python) qui va récupérer depuis le site [PyPi](https://pypi.org/) (python package index) la bibliothèque demandée et va l'installer sur votre ordinateur. 


### quel python utiliser ?

**Utilisez la version 3 de python**. Il n'est pas nécessaire d'avoir la toute dernière itération de cette version (3.9.6 à l'heure où je tape ces caractères), toute version 3 de python pas trop ancienne doit convenir. 

>Si vous installez python pour la première fois sur votre ordinateur, choisissez d'installer la dernière version stable de python 3.

Une version de python est composée de 3 nombres [MAJOR.MINOR.PATCH](https://semver.org/) :

1. **MAJOR** : pour nous sera 3. 
2. **MINOR** : chaque année une nouvelle itération arrive, avec son lot de nouveautés en therme de structures de données ou de bibliothèques. 
3. **PATCH** : correctifs.


Chaque année sort une nouvelle version de python (voir <https://devguide.python.org/#status-of-python-branches>), les anciennes versions sont maintenues 5 ans avant d'être considérées comme obsolète. Chaque version vient avec son [changelog](https://fr.wikipedia.org/wiki/Changelog), qui donne ses nouveautés et changements par rapport à la version précédente ([ici](https://docs.python.org/release/3.9.6/whatsnew/changelog.html#changelog) le changelog de la version 3.9.6)

> La version majeur actuelle de python est 3, il n'y pas prévu d'en changer avant un certain temps. 

### et python 2 ?

Depuis le 1er janvier 2020, la version majeure 2 de python est **obsolète**, il est donc fortement recommandé de ne plus l'utiliser. Vos programme seront en effet difficilement maintenance et de plus en plus difficilement utilisable.

> Il n'y a **aucune** bonne raison d'utiliser la version 2 de python pour écrire des programmes actuellement.
La version de python . Il n'est pas nécessaire
python2 vs python3

> Il existe sur le net encore beaucoup d'exemples utilisant la version2 de python, ou certains profs un peu feignant qui ne passent pas leurs exemple/cours en python3. Plutôt que d'utiliser python2, il est recommandé de convertir ces programmes dans la version 3 et de demander la mise à jour des cours...
{: .attention}

### j'ai quoi comme python ?

Nous y reviendrons, mais si vous savez exécuter du code python mais vous ne savez pas trop quel interpréteur vous utilisez (par exemple vous utilisez [jupiter](https://jupyter.org/) via un intranet ou [spider](https://www.spyder-ide.org/)), il existe quelques trucs simple pour savoir quelle version de python on utilise.

#### python 2 ou python 3

La différence la plus visible entre une version 2 et une version 3 de python est que pour une version 3 de python, le code suivant :

``` python
print "j'utilise un langage obsolète"
``` 

 produit l'erreur : 
 ```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("j'utilise un langage obsolète")?
 ```

Alors que le code s'exécute sans soucis avec la version 2 de python (il écrit `j'utilise un langage obsolète`).

#### quelle version de python

On suppose que l'on utilise la version 3 de python. Pour connaitre la version spécifique de python, on peut utiliser [la constante `version`du module `sys`de pyhton](https://docs.python.org/fr/3/library/sys.html#sys.version) :

``` python
import sys
print(sys.version)
```

qui rend chez moi : 

```
3.9.6 (default, Jun 29 2021, 05:25:02) 
[Clang 12.0.5 (clang-1205.0.22.9)]
```

C'est à dire que j'utilise la version 3.9.6 de python et que mon interpréteur a été compilé par [Clang](https://clang.llvm.org/) (c'est sur un mac).

## installation

Nous allons ici nous concentrer sur l'installation de l'interpréteur python. Il existe plusieurs façon de faire. Nous en présenterons 2 :

* solution universelle simple : utilisez la [distribution anaconda](#anaconda-id)
* solution informaticienne : à privilégier si vous voulez contrôler toute votre installation (c'est bien). On utilise un [gestionnaire de package](#gestionnaire-package-id).

> Parfois, il n'y a rien à faire (c'est souvent le cas sous mac ou linux qui arrivent avec des versions de python 2 et 3 déjà installées).

Une fois que vous aurez installé python (ou pour savoir si vous l'avez déjà installé), vérifiez le en tentant d'[exécuter l'interpréteur python dans un terminal](#interpreteur-id).

### installation d'anaconda {#anaconda-id}

[Anaconda](https://www.anaconda.com/) est une entreprise gérant des distributions python orientés data-science. L'intérêt d'une telle distribution est qu'elle regroupe et installe de nombreux utilitaires. Le côté négatif est que l'on ne maîtrise pas les paquets installés et l'installation de paquets supplémentaires est parfois problématique. 

Cependant, pour une utilisation basique de python ou une utilisation via jupyter, c'est une solution tout à fait satisfaisante car facile à mettre en œuvre sans être informaticien.

#### Téléchargement de l'installeur

Nous allons télécharger la distribution open-source d'anaconda [ici](https://www.anaconda.com/products/individual). Choisissez la version 64bit graphique correspondant à votre système d'installation, puis cliquez sur l'installeur.


Lors de l'installation vous pourrez choisir de faire une installation uniquement pour vous ou pour tous les utilisateurs. Choisissez **pour tous les utilisateurs**.
  * **de personnaliser votre installation**. Vous aurez une option, initialement cochée, qui fera en sorte qu'anaconda soit votre distribution python par défaut. Personnellement je décoche cette option car je gère mes version de python moi-même. Si vous être un 1A ou un 2A novice, laissez là cochée. Si vous êtes un 3A DFS, décochez là.

> Si vous avez une ancienne version d'anaconda et que vous souhaitez installer une mise à jour, il vous faudra commencer par supprimer le dossier contenant l'ancienne version
{: .attention}

> Anaconda change le chemin par défaut python pour que ce soit celui d'anaconda qui soit utilisé.
> 
>  Sous mac et linux cela se passe en modifiant le fichier de configuration du shell (entre `conda initialize`). 


#### test de la distribution

Anaconda a installé des choses, en particulier l'application *Anaconda-Navigator* qui vous permet de lancer toutes les applications liées à Anaconda.

Lancez l'application *Notebook* puis :

  1. créez un nouveau notebook `python3`.
  2. dans la cellule tapez `print("Hello world!")`
  3. cliquez sur l'icone *Exécuter* sur la bannière de titre ou appuyer sur `shift + entrée`.
  
  Vous devriez voir le texte `Hello World` en sortie de votre cellule.
  
### anaconda avec un terminal 

Dans l'*anaconda navigator*, cliquez sur *Environnements* dans le menu de gauche (c'est le deuxième choix, après *Home* et avant *Learning*).

Vous devez avoir un unique environnement : *base (root)*. Un environnement est un interpréteur python et tous ses packages installés. On aura parfois envie de créer ses propres environnements pour installer soit une version spécifique de python, soit n'installer que certains packages.

Pour l'instant utilisons l'environnement de base. En cliquant sur le triangle vert à droite de l'environnement *base (root)*, vous pouvez cliquer sur *open terminal*, ce qui ouvrira un terminal. Une fois le terminal ouvert, remarquez qu'à gauche de l'invit de commande vous avez `(base)` d'acrit. Ceci montre quel environnement python vous avez.

Vos pouvez [connaitre l'interpréteur](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/python-path/).

### installation via un gestionnaire de package {#gestionnaire-package-id}

Une bonne pratique d'installation de logiciel sur son ordinateur est d'utiliser un gestionnaire de package. Il vous permet de savoir exactement ce qui est utilisé, quelle version, et surtout gère tout seul les mise à jours. 

C'est un peut plus compliqué qu'utiliser anaconda mais si vous voulez faire de l'informatique sérieuse ou sérieusement de l'informatique, il est conseillé d'utiliser cette solution.


{% details sous mac %}

On utilise [brew](https://brew.sh/index_fr). Toutes les commandes se font via le [terminal](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) (il est dans Applications/utilitaires)

Une fois brew installé, vous pouvez installer python en tapant la commande : 

```shell
brew install python
``` 
{% enddetails %}

{% details sous windows %}

Pour l'instant téléchargez le tout depuis le site de python. Il se placera automatiquement dans les logiciels installés. C'est pas super mais ça marche.

<https://www.python.org/downloads/>

{% enddetails %}


{% details sous linux %}

> TBD : avec apt-get ?
{: .danger}

{% enddetails %}


## utiliser l'interpréteur python {#interpreteur-id}

### terminal {#ouvrir-terminal-id}

Pour utiliser l'interpréteur python, on ne peut pas directement double-cliquer sur son nom car il ne possède pas d'interface graphique : il faut l'exécuter en mode ligne de commande, via un terminal (pour faire mode, on peut dire [CLI](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)). 

Trouver l'application terminal : 

{% details sous mac %}
Le [terminal](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) se trouve dans /Application/utilitaires (finder : menu Aller > Applications puis allez dans le dossier utilitaires). Vous pouvez ensuite cliquer sur l'icône terminal.

Le terminal est super utile, ça vaut le coup d'ajouter un raccourci dans la barre du finder.

{% enddetails %}

{% details sous linux %}

Si vous êtes sous linux vous devriez savoir ouvrir un terminal. C'est souvent une application avec une télévision comme icône.

{% enddetails %}

{% details sous windows %}

Vous pouvez utiliser l'invit de commande mais c'est une torture (tapez `cmd` dans l'invit de recherche), ou utiliser le [power-shell](https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1) qui est semblable au terminal du mac/unix. Pour ouvrir une fenêtre powersheel, il y a [plusieurs possiblités](https://lecrabeinfo.net/ouvrir-powershell-sur-windows-10.html)

{% enddetails %}

Une fois l'application trouée, exécutez là. Une fenêtre doit s'ouvrir, vous permettant de taper des commandes. 

> N'ayez pas peur. C'est simple à utiliser. On tape une commande, on appuie sur entrée et la commande s'exécute. 
>Vous pouvez a priori utiliser votre ordinateur uniquement avec un terminal. L'interface graphique n'est qu'un ajout sympathique mais non indispensable à l'utilisation d'n ordinateur. 

Si vous voulez utiliser pleinement votre ordinateur, voir devenir informaticien/ne plus tard, il est important que vous sachiez vous en servir (en plus d'avoir cette petite sensation d'interagir directement avec la matrice lorsque l'on tape des commande en mode CLI). Donc autant l'utiliser le plus souvent possible histoire de s'habituer.

### exécution de l'interpréteur python

L'interpréteur python s'appelle soit *"python"*, soit *"python3"*. Regardez celui que vous possédez.

> Sous windows, c'est souvent *"python"* qu'il s'appelle, sous mac et linux c'est *"python3"*. Pour le reste du tuto, je considérerai que c'est *"python"*.

Dans un terminal, tapez la commande : 
```shell
python
```

Si ça a marché, l'interpréteur aura donné sa version (**assurez vous que c'est bien python 3**) et vous donnera une invite de commande qui commence par `>>>`.Vous pouvez taper une ligne de python. Lorsque vous taperez sur entrée, votre ligne sera interprétée en python et donnera le résultat. 

Par exemple tapez : `print(coucou !)`et l'interpréteur vous rendra `coucou !`. On ne pourrait utiliser python que comme ça, mais ce n'est pas très pratique. 

Pour quitter l'interpréteur tapez `quit()` puis appuyez sur la touche entrée.

### version de l'interpréteur python

Beaucoup de programme supportent d'être lancé avec des paramètres, que l'on ajoute à la suite du nom. Par exemple pour connaître la version de l'interpréteur, on tape dans un terminal : 

```shell
python --version
```
Chez moi ça rend : 
```
Python 3.9.6
```

> Pour connaitre tous les paramètres possible, on peut soit se référer à la [documentation](https://docs.python.org/3/using/cmdline.html), soit taper : `python --help`

### emplacement de votre interpréteur 

Dans un terminal tapez la commande : 
* `which python` sur un mac ou un linux,
* `where python` sur un windows,

La commande devrait vous rendre l'emplacement sur votre disque dur de votre interpréteur. Vérifiez le avec un explorateur de fichier.


## packages

Python vient avec une [liste de packages](https://docs.python.org/3/library/) bien fournie. On peut les utiliser via le mot clé `import` en python. Il en existe une foultitude d'autres qui permettent d'aider à coder rapidement. La liste des différents packages est disponible sur <https://pypi.org/>

### installation avec pip

Pour installer de nouveaux packages python, on utilise la commande `pip`.

> si votre interpréteur python est *"python3"*, vous devez utiliser la commande *"pip3"*

Testez le en ouvrant un terminal et en tapant : 
```shell
pip --version
``` 

La commande devrait vous rendre le numéro de version de pip ainsi que le chemin du programme python qui lui est associé. 

Les packages déjà installé par pip seront visible avec la commande : 
```shell
pip list
``` 

Si vous avez une distribution anaconda, vous devriez avoir plein de choses, sinon, beaucoup moins.



> Il est crucial de vérifier que pip est bien lié à l'interpréteur python que vous voulez. Sinon, vous installerez des packages pour un mauvais interpréteur.
{: .attention}

On peut maintenant utiliser pip pour installer un nouveau package. Nous allons installer [black](https://pypi.org/project/black/) qui rendra joli tous nos programmes python. Dans un terminal tapez :
```shell
pip install black
``` 

Une fois l'installation terminée, black devrait apparaitre dans la liste des packages installés (vous pouvez le voir avec `pip list`).

### où sont les packages ?

 Les répertoires où python va cherchez les packages est dans la liste `sys.path`. 

vous pouvez le voir en exécutant le code :
```python
import sys
for dossier in sys.path:
   print(dossier)
```
chez moi, ce programme rend : 

```
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python39.zip
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9
/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload
/usr/local/lib/python3.9/site-packages
```

Il y a plusieurs dossiers :
* *"/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9"* contient les packages de bibliothèque standard (il contient par exemple un fichier *"random.py"* qui contient le code du package `random`)
* *"/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload"* contient les packages python qui ne sont pas écrit en python mais en C
* *"/usr/local/lib/python3.9/site-packages"* qui contient les packages qui seront installés par pip.



> La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilsant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connait.
{: .attention}

## éditeur

Il en existe une multitude. Prenez en un qui permettent non seulement d'écrire aisément du code python mais aussi d'exécuter facilement tout ce qui va avec écrire du code :

* coloration syntaxique
* nommage et renommage de variables sur tout un projet
* lancer des tests
* ...

J'en conseille 2 :
* [visual studio code](https://code.visualstudio.com/)
* [pycharm](https://www.jetbrains.com/fr-fr/pycharm/)

Il existe également d'autres façon d'utiliser python, en mode interactif par exemple en utilisant [jupyter](https://jupyter.org/) avec anaconda, ou encore [colab](https://colab.research.google.com).


