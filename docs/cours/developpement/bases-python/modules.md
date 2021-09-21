---
layout: page
title:  "Bases de python : modules"
author: "François Brucker"
---

Un *module* (aussi appelé *bibliothèque* ou *library*) est un ensemble de fonctions utiles, utilisables dans de nombreux programmes. Plutôt que de refaire à chaque fois ces fonctions ou (c'est pire) de les copier/coller dans chaque programme, on les importe directement pour les utiliser.

>Il existe de nombreux modules, réalisant une foultitude d'opérations. Avant de se mettre à coder quelque chose, commencez toujours par vérifier (google
> est votre ami) s'il n'existe pas un module tout fait, vous gagnerez du temps. Python en fournit déjà de [nombreux](https://docs.python.org/3/library/index.html)

Pour utiliser un module, il faut commencer par l'importer avec la commande `import`. Par exemple avec le module `math`.

#### Importation directe du module

On met le nom complet avant chaque appel :

```python
import math
pi_sur_deux = math.pi / 2 #PI est défini dans le module math
x = math.cos(pi_sur_deux) #on utilise la fonction cosinus du module math
```

#### Importation d'une méthode particulière

Ceci peut être dangereux si des fonctions différentes possèdent le même nom.

```python
from math import cos, pi #importation directe de cos et de pi
x = cos(pi / 2)
```

#### Importation de toutes les fonctions du modules

Déconseillée dans la plupart des cas car on ne sait pas vraiment ce qui a été importé.

```python
from math import *
y = log(e)
```

#### Modules utiles

De nombreux modules existent pour python et permettent de réaliser aisément de très nombreuses tâches. Pour python, si avez les droits administrateurs on pourra utiliser l'utilitaire [pip](https://pypi.org/project/pip/) qui est l'installeur de package python3 (attention, si vous tapez juste pip, vous installerez des module pour la version 2 de python...).

Si vous n'avez pas de droits administrateur, ou pour une utilisation plus "pro" des modules, on préfèrera créer des environnements virtuels avec *virtualenv*, mais ceci  dépasse (de peu) le cadre de notre introduction à python.

>Si vous utilisez un interpréteur qui s'appelle `python3` et pas `python`, il est fort possible que le programme `python`(sans le 3) soit un interpréteur de la version 2 de python. Il vous faut alors utiliser la commande `pip3`et non `pip` (qui sera elle associée à l'interpréteur `python`)
{: .attention}

##### Le module random

> <https://docs.python.org/3/library/random.html>

Regardez [ces exemples](https://python.sdv.univ-paris-diderot.fr/08_modules/#85-module-random-generation-de-nombres-aleatoires) pour le module random.

Installé par défaut, il permet notamment de mélanger les éléments d'une liste, générer un nombre aléatoire, choisir un élément aléatoire dans une liste... Vous pouvez même simuler une loi Gaussienne (si, si).

##### openpyxl

> <http://openpyxl.readthedocs.org>

Permet de manipuler des [fichiers excel avec python](https://automatetheboringstuff.com/chapter12/).

Il s'installe avec pip : `pip install openpyxl` (ou `sudo pip3 install openpyxl` suivi de votre mot de passe si vous êtes sous unix/mac).

##### matplotlib

> <http://matplotlib.org>

Installé par défaut si vous utilisez l'interpréteur d'[anaconda](https://www.anaconda.com/), ce module permet d'afficher des graphiques en python.

##### Jupyter

> <http://jupyter.org>

Permet d'utiliser python de façon interactive (il s'installe aisément avec pip par exemple) 
