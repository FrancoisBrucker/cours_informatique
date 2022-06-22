---
layout: page
title:  "Bases de python : modules"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

> [bases de python]({% link cours/bases-python/index.md %}) / [modules python]({% link cours/bases-python/modules.md %})
{: .chemin}


Un *module* (aussi appelé *bibliothèque* ou *library*) est un ensemble de fonctions utiles, utilisables dans de nombreux programmes. Plutôt que de refaire à chaque fois ces fonctions ou (c'est pire) de les copier/coller dans chaque programme, on les importe directement pour les utiliser.

>Il existe de nombreux modules, réalisant une foultitude d'opérations. Avant de se mettre à coder quelque chose, commencez toujours par vérifier (google
> est votre ami) s'il n'existe pas un module tout fait, vous gagnerez du temps. Python en fournit déjà de [nombreux](https://docs.python.org/3/library/index.html)
{: .note}

Pour utiliser un module, il faut commencer par l'importer avec la commande `import`. Par exemple avec le module `math`.

## utiliser un module

Il existe plusieurs façon de faire, mais toute fonctionne sur le même principe : python va lire le module et associer les nom qu'il trouve à un espace de nom. Le mot clé utilisé est **import \<nom de module\>** ou une de ses variations.

### Importation directe du module

On met le nom complet avant chaque appel :

```python
import math
pi_sur_deux = math.pi / 2 
x = math.cos(pi_sur_deux) 
```

Lors de la ligne `import math` python crée un espace de nom qu'il appelle `math`. Il lit ensuite math avec cet espace de nom. Donc tout ce qui est défini dans math, le sera dasn l'espace de nom nommé `math`. On accède ensuite aux noms de math par la notation `.`.

> la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`
{: .note}

### Importation d'une méthode particulière

Ceci peut être dangereux si des fonctions différentes possèdent le même nom.

```python
from math import cos, pi #importation directe de cos et de pi
x = cos(pi / 2)
```

Lors de la ligne `from math import cos, pi` python crée un espace de nom pour l'import. Il lit ensuite math avec cet espace de nom. Une fois la lecture finie, il cherche les noms `cos` et `pi` et les associe à l'espace de nom **global**.

> Dans cette façon de faire, on associe des noms du module math à l'espace de nom global. Il n'y a aucune manière d'accéder aux autres noms défini dans math avec cette façon de faire.

### Importation de toutes les fonctions du modules

Déconseillée dans la plupart des cas car on ne sait pas vraiment ce qui a été importé.

```python
from math import *
y = log(e)
```

Lors de la ligne `from math import *` python lit le module math **dans** l'espace de nom **global**.

### importation de modules sous la forme d'alias

Quelques bibliothèques très utilisées s'importent avec des alias par exemple :

```python
import numpy as np
```

Ou encore :

```python
import matplotlib.pyplot as plt
```

Cela permet de raccourcir le nom, il suffira de taper `plt` à la place de `matplotlib.pyplot` mais cela se fait au **détriment** de la lisibilité. Il n'est donc pas recommandé du tout de le faire avec d'autres bibliothèque même s'il est tout à fait possible d'écrire ce genre d'horreurs :

```python
import math as m
import random as r
```

## installer des modules

Suivez le [tutorial des packages]({% link _tutoriels/python/installation-de-python.md %}#packages) dans le guide d'installation de python.

## exécuter un module dans le terminal

`python3 -m <nom du module>`

On en aura besoin pour exécuter `black` par exemple ou encore `pytest`.
