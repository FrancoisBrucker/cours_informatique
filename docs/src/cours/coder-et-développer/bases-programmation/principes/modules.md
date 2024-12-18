---
layout: layout/post.njk
title: Modules

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
Utilisez un notebook de <https://notebook.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

Un _module_ (aussi appelé _bibliothèque_ ou _library_) est un ensemble de fonctions utiles, utilisables dans de nombreux programmes. Plutôt que de refaire à chaque fois ces fonctions ou (c'est pire) de les copier/coller dans chaque programme, on les importe directement pour les utiliser.

Certains modules sont très utiles en python scientifique :

- [numpy](https://numpy.org/) : très utilisé pour ses structures de matrices et tableaux
- [matplotlib](https://matplotlib.org/) : pour créer des graphiques en python
- [scipy](https://scipy.org/) : résolution d'équations différentielles
- [pillow](https://pillow.readthedocs.io/en/stable/) : gestion d'images
- [sklearn](https://scikit-learn.org/stable/) : machine learning

Ils ne viennent pas automatiquement lorsque l'on installe python, mais beaucoup sont déjà installés si vous utilisez l'interpréteur de [spyder](https://www.spyder-ide.org/) ou encore les notebooks de <https://colab.research.google.com>. Nous plus tard comment installer ses propres modules, pour l'instant nous allons uniquement utiliser ceux fournis par python (et ils sont déjà nombreux).

{% note %}
Il existe de nombreux modules, réalisant une foultitude d'opérations. Avant de se mettre à coder quelque chose, commencez toujours par vérifier (google
est votre ami) s'il n'existe pas un module tout fait, vous gagnerez du temps. Python en fournit déjà de [nombreux](https://docs.python.org/3/library/index.html)
{% endnote %}

## Utiliser un module

Pour utiliser un module, il faut commencer par l'importer avec la commande `import`{.language-}. Par exemple avec le module `math`{.language-}.

Il existe plusieurs façon de faire, mais toutes fonctionnent sur le même principe : python va lire le module et associer les noms qu'il trouve à un espace de nom. Le mot clé utilisé est `import <nom de module>`{.language-} ou une de ses variations.

### Importation directe du module

On met le nom complet avant chaque appel :

```python
import math
pi_sur_deux = math.pi / 2
x = math.cos(pi_sur_deux)
```

Lors de la ligne `import math`{.language-} python crée un espace de nom qu'il appelle `math`{.language-}. Il lit ensuite math avec cet espace de nom. Donc tout ce qui est défini dans math, le sera dans l'espace de nom nommé `math`. On accède ensuite aux noms de math par la notation `.`.

{% note %}
La notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`
{% endnote %}

### Importation d'une méthode particulière

Ceci peut être dangereux si des fonctions différentes possèdent le même nom.

```python
from math import cos, pi #importation directe de cos et de pi
x = cos(pi / 2)
```

Lors de la ligne `from math import cos, pi`{.language-} python crée un espace de nom pour l'import. Il lit ensuite math avec cet espace de nom. Une fois la lecture finie, il cherche les noms `cos` et `pi` et les associe à l'espace de nom **global**.

{% info %}
Dans cette façon de faire, on associe des noms du module math à l'espace de nom global. Il n'y a aucune manière d'accéder aux autres noms défini dans math avec cette façon de faire.
{% endinfo %}

### Importation de toutes les fonctions du modules

Déconseillée dans la plupart des cas car on ne sait pas vraiment ce qui a été importé.

```python
from math import *
y = log(e)
```

Lors de la ligne `from math import *`{.language-} python lit le module math **dans** l'espace de nom **global**.

### Importation de modules sous la forme d'alias

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

## Exercices avec le module random

Un module très utile dans python est le module [random](https://docs.python.org/fr/3/library/random.html)

Utilisez le pour répondre aux questions suivantes :

{% faire %}
Générez un entier aléatoire entre 10 et 234.
{% endfaire %}
{% details "solution" %}

On utilise la fonction [`randrange`{.language-} du module `random`{.language-}](https://docs.python.org/fr/3/library/random.html#random.randrange) :

```python
>>> import random
>>> random.randrange(10, 235)
51
```

{% enddetails %}

{% faire %}
Générez un nombre réel uniformément dans $[0, 1[$
{% endfaire %}
{% details "solution" %}

On utilise la fonction [`random`{.language-} du module `random`{.language-}](https://docs.python.org/fr/3/library/random.html#random.random) :

```python
>>> import random
>>> random.random()
0.07350177375024702
```

{% enddetails %}

{% faire %}
Choisissez 2 éléments **avec** remise de la liste `["pomme", "abricot", "orange", "cerise"]`{.language-}
{% endfaire %}
{% details "solution" %}

On utilise la fonction [`choices`{.language-} du module `random`{.language-}](https://docs.python.org/fr/3/library/random.html#random.choices) :

```python
>>> import random
>>> random.choices(["pomme", "abricot", "orange", "cerise"], k=2)
['pomme', 'pomme']
```

{% enddetails %}

{% faire %}
Choisissez 2 éléments **sans** remise de la liste `["pomme", "abricot", "orange", "cerise"]`{.language-}
{% endfaire %}
{% details "solution" %}

On utilise la fonction [`sample`{.language-} du module `random`{.language-}](https://docs.python.org/fr/3/library/random.html#random.sample) :

```python
>>> import random
>>> random.sample(["pomme", "abricot", "orange", "cerise"], k=2)
['cerise', 'pomme']
```

{% enddetails %}
