---
layout: layout/post.njk 
title: "Projet : objets dés"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../coder-ses-objets/"
---

<!-- début résumé -->

Projet sur le codage d'objets en python. On verra comment créer petit à petit un objet qui corresponde à nos attentes en termes de fonctionnalités tout en étant agréable à utiliser.

<!-- end résumé -->

{% note "**Méthode de conception**" %}
Lorsque l'on crée un objet qui correspond à un objet réel, il faut faire en sorte que le code l'utilise comme on le ferait dans la réalité.
{% endnote %}

Nous allons montrer le principe précédent en créant petit à petit une classe permettant de jouer aux dés. La classe `Dé`{.language-} doit être capable de :

* créer un objet sans paramètre (sa position est alors 1),
* créer un objet avec une position initiale différente de 1,
* connaître et donner la position du dé,
* lancer un dé en utilisant une méthode nommée `lancer()`{.language-} qui ne rend **rien**, mais change la position du dé de façon aléatoire.

La position du dé doit être un entier entre 1 et 6.

{% faire %}

1. Proposez une modélisation UML de la classe `Dé`{.language-}.
2. Donnez des exemples de code qui manipulent des objets de cette classe, comme :
   * créer un objet
   * afficher sa position à l'écran
   * modifier la valeur de sa position
   * lancer le dé

{% endfaire %}

Faites en particulier attention à la façon dont vous voulez lancer le dé.

### Projet vscode

{% faire %}
Créez un dossier `projet-dés`{.fichier} sur votre ordinateur et ouvrez-le avec visual studio code pour un faire votre projet.
{% endfaire %}

{% faire %}

En créant des fichiers *jouets* dans votre projet, vérifier que :

* le [linter]({{ "/tutoriels/vsc-python-modules-supplémentaires/pycodestyle" }}#black)  est activé
* [black]({{ "/tutoriels/vsc-python-modules-supplémentaires/black" }}) fonctionne
* vous pouvez faire du [code coverage]({{ "/tutoriels/couverture-de-code" }})
{% endfaire %}

### User stories

{% note "Définition" %}
Une [user story](https://fr.wikipedia.org/wiki/R%C3%A9cit_utilisateur) est un récit qui nous permet de savoir comment et par qui va être utilisé notre code.
{% endnote %}

L'idée est d'écrire une succession d'actions faites par un utilisateur typique afin de réaliser une tâche précise avec notre programme. Par exemple :
{% note "**User story**" %}

* Nom : "Aléatoire ?"
* Utilisateur : un professeur.
* Story : On vérifie que le lancé de dé ressemble à de l'aléatoire.
* Actions :
  1. créer un dé sans paramètre
  2. afficher à l'écran sa position (ça doit être 1)
  3. lancer le dé 10 fois et affiche la position du dé après chaque lancé. Quelle est la probabilité que le dé ne change jamais ?).

{% endnote %}

Essayons de voir ce que donnerait cette user story si on devait la coder :

{% exercice %}

En utilisant la modélisation UML du Dé, codez la user story "Aléatoire" en python dans le fichier `story_aléatoire.py`{.fichier}.

{% endexercice %}
{% details "corrigé" %}
Il y a une probabilité de $\frac{1}{6^{10}} = 1.6 \cdot 10^{-8}$ que le dé ne change jamais de position en 10 lancés.

La user story donnerait en python :

```python
from dé import Dé

# 1. créer un dé sans paramètre
dé = Dé() 

# 2. afficher à l'écran sa position (ça doit être 1)
print(dé.position)

# 3. lancer le dé 10 fois et affiche la position du dé après chaque lancé
for i in range(10):
   dé.lancer()
   print(dé.position)
```

{% enddetails %}

Comme pour l'instant rien n'est codé :

{% faire %}
Commentez les codes python de la user story. A chaque fois que l'on codera une fonctionnalité, on dé-commentera ce qui marchera. A la fin de la session de code, votre user story devra être opérationnelle.
{% endfaire %}

La user story fait office de **test fonctionnel** qui permet de vérifier que le code correspond aux attentes des utilisateurs.

{% note %}
Un programme aura :

* **toujours** des [tests unitaires](https://fr.wikipedia.org/wiki/Test_unitaire) car ils garantissent que ce que vous avez codé est correct
* **très souvent** des [tests fonctionnels](https://en.wikipedia.org/wiki/Functional_testing) car ils garantissent que ce que vous avez codé pourra être utile

On exécutera la batterie de tests unitaires à chaque fois que l'on code ou que l'on modifie une fonction, les tests fonctionnels sont exécutés a chaque fois que l'on achève une fonctionnalité.

{% endnote %}
{% info %}
Les fonctionnalités développées doivent toutes faire parti d'au moins une user story, sinon c'est [YAGNI]({{ "../../coder"  }}#YAGNI).
{% endinfo %}

## Code

### Classe vide

{% faire %}
Crée un ficher `dé.py`{.fichier} contenant une classe `Dé`{.language-} vide et testez avec la fonction de test `test_init()`{.language-} dans un fichier `test_dé.py`{.fichier} que l'on peut créer des objets de cette classe.
{% endfaire %}

{% faire %}
Dé-commentez la première partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

### Attribut `position`{.language-}

{% faire %}
Ajoutez l'attribut position au dé et assurez vous qu'il est bien initialisé à 1 dans un test nommé `test_position()`{.language-}.
{% endfaire %}

{% faire %}
Dé-commentez la seconde partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

Finalisons les différentes initialisations possible de l'attribut `position`{.language-} :

{% faire %}
Faites en sorte que l'on puisse choisir la position initiale du dé dans le constructeur. Par défaut, la position du dé doit toujours être de 1. Ajoutez un test correspondant dans le test `test_position()`{.language-}.
{% endfaire %}

### Méthode `Dé.lancer()`{.language-}

{% info %}
Dans la documentation et lorsque l'on décrit une méthode, som nom de la méthode est toujours accolé au nom de la classe qui la définit. Par exemple :  `Dé.lancer()`{.language-} signifie :

* la méthode `lancer`{.language-} de la classe `Dé`{.language-}
* cette méthode ne prend pas de paramètre.

{% endinfo %}
{% attention %}
Lorsque l'on décrit une méthode, on ne montre jamais `self`{.language-}. Ce n'est en effet pas un paramètre de la méthode à proprement parlé, c'est l'**objet** de la méthode : il est à gauche du `.`{.language-} lors de l'appel de la fonction.

On pourrait (mais on ne le fait pas parce que c'est moins clair) replacer le code suivant :

```python
>>> un_dé = Dé()
>>> un_dé.lancer()
```

Par le code ci-après qui est équivalent :

```python
>>> un_dé = Dé()
>>> Dé.lancer(un_dé)
```

{% endattention %}

Il ~~nous~~ vous reste à coder la méthode `Dé.lancer()`{.language-} :

{% faire %}
Codez la méthode `Dé.lancer()`{.language-} qui modifie aléatoirement la position du dé appelant par un entier allant de 1 à 6.
{% endfaire %}

Il est impossible de tester le hasard (on pourrait n'avoir pas de chance et lancer 10 fois le dé sans que la position ne change **sans** que ce soit mal codé), on ne va donc uniquement tester ici que le fait que la méthode lancer s'exécute sans soucis et le résultat reste cohérent :

{% faire %}
Ajouter un test nommé `test_lancer()`{.language-} qui vérifie que la position d'un dé après un lancer est toujours entre 1 et 6.
{% endfaire %}

Vous pouvez maintenant voir si la user story fonctionne :

{% faire %}
Dé-commentez la dernière partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

### Couverture de code

Avant de coder le programme principal :

{% faire %}

1. vérifiez que les tests unitaires fonctionnent
2. vérifiez que vous avez bien 100% de [couverture de code]({{ "/tutoriels/couverture-de-code" }}).
3. vérifiez que vos user stories sont toutes fonctionnelles

{% endfaire %}

## Programme principal

{% faire %}
Créez un fichier `main.py`{.fichier} qui :

1. demande à l'utilisateur :
   * la position initiale du dé
   * la valeur pour laquelle arrêter les lancers
2. lance le dé jusqu'à tant que la valeur demandée par l’utilisateur soit trouvée.
3. le programme affiche le nombre de lancer nécessaire (cela peut être 0)

{% endfaire %}

## Lancers multiples

Pour l'instant, l'utilisation de la méthode `lancer`{.language-} est laborieuse :

* pour connaître la nouvelle position du dé il faut d'abord lancer le dé puis regarder sa position
* pour lancer deux fois le dé, il faut faire deux lignes

Ce serait tellement bien si on pouvait faire quelques chose du style :

* `print(dé.lancer().position)`{.language-} pour lancer le dé puis retrouver sa position dans la même ligne
* `dé.lancer().lancer()`{.language-} pour lancer le dé deux fois de suite.

{% exercice %}
Comment réaliser cela ?
{% endexercice %}
{% details "solution" %}
Il suffit que la méthode rende l'objet (c'est à dire `self`{.language-}) !
{% enddetails %}

{% faire %}
Modifiez le code, les tests et le programme principal pour mettre en œuvre cette modification.
{% endfaire %}

## Accès indirect à un attribut (*getter* et *setter*)

Lorsqu'un attribut d'un objet est soumis à un contrôle, par exemple position qui ne peut prendre comme valeur des entiers entre 1 et 6, il est de coutume de ne pas accéder directement à celui-ci, mais de passer par des méthodes pour le modifier et y accéder

### Mutateur ou *setter*

{% note %}
Un ***mutateur*** (***setter***) est une méthode dont le but est de modifier un attribut. On la nomme usuellement : `set_[nom de l'attribut](nouvelle_valeur)`{.language-}
{% endnote %}

{% faire %}
Créez une méthode `Dé.set_position(nouvelle_position)`{.language-} qui modifie la position du dé.

Faites en sorte que la position ne puisse être plus petite que 1 (si `nouvelle_position`{.language-} < 1  alors l'attribut vaut 1) ni plus grande que 6 (si `nouvelle_position`{.language-} > 6  alors l'attribut vaut 6).

Créez un test pour la méthode `Dé.set_position(nouvelle_position)`{.language-} et modifiez, s'ils y en a, les tests qui modifient directement l'attribut positions pour qu'ils utilisent le *setter*.

{% endfaire %}

Le but est de faire disparaître l'utilisation directe de l'attribut dans le code. Une fois qu'on ne le verra plus, c'est comme s'il n'existait plus.

Avant de continuer, nous allons éliminer les 2 constantes non nommées 1 et 6 que nous venons certainement de créer (si vous ne l'avez pas fait, bravo !).

Les nombres 1 et 6 sont les bornes du dé, il faut les nommer en tant que tel, sinon on va oublier leur signification et le code sera plus dire à modifier plus tard :

<span id="mantra-no-magic-numbers"></span>
{% note "**Coding mantra**" %}

[NO MAGIC NUMBER](https://fr.wikipedia.org/wiki/Nombre_magique_(programmation)#Constantes_num%C3%A9riques_non_nomm%C3%A9es)
{% endnote %}

{% faire %}
Ajouter les constantes `MIN_VALEUR = 1`{.language-} et `MAX_VALEUR = 6`{.language-} dans le fichier `dé.py`{.fichier} et utilisez les dans tout le code. Y compris le test du lacer de dé.
{% endfaire %}

{% info %}
Changer ses valeurs changera la nature de tous les dés crées.

{% endinfo %}

### Accesseur ou *getter*

Si l'on veut accéder à un attribut sans l'utiliser directement, il faut le faire *via* une méthode. Cela peut être pratique si l'attribut n'est pas directement donné dans l'objet mais est construit (par exemple des coordonnées polaires d'un objet point2D où ses attributs sont en réalité ses coordonnées cartésiennes)

{% faire %}
Créez une méthode `Dé.get_position()`{.language-} qui rend la position du dé.

Créez un test pour cette méthode.
{% endfaire %}

Afin de faire disparaître l'existence de l'attribut dans le code :

{% faire %}
 modifiez tous les tests et les codes des programmes qui utilisent directement l'attribut `position`{.language-} pour qu'ils utilisent l'accesseur.
{% endfaire %}

On peut maintenant rendre l'attribut `position`{.language-} privé.

{% note "**Définition**" %}
Un attribut ***privé*** est un attribut qui ne doit pas être utilisé autre-part que dans les définitions de méthodes de la classe. Les attribut directement utilisables dans le code sont dit ***public***.

Tout code voulant accéder ou modifier à cet attribut **doit** passer par son accesseur/mutateur.
{% endnote %}

En python, un attribut privé est précédé d'**un** `_`{.language-}. Par exemple, l'attribut `position`{.language-} est public alors que l'attribut `_position`{.language-} est privé.

{% faire %}
Rendez l'attribut `position`{.language-} de la classe `Dé`{.language-} privé.
{% endfaire %}

En python, la notion d'attribut privé ou public n'existe pas vraiment, ce sont juste des conventions entre codeur. Il est ainsi tout à fait possible d'utiliser un attribut privé partout (mais c'est *bad karma*). Le seul endroit où l'utilisation directe d'un attribut privé est autorisé, c'est dans le test de son accesseur.

### <span id="property"></span> Property

Python a une superbe fonctionnalité qui permet d'utiliser les accesseur les mutateur *comme* si l'on utilisait directement un attribut !

{% lien %}
[Le décorateur `@property`{.language-}](https://docs.python.org/fr/3.11/library/functions.html#property)
{% endlien %}

La façon la plus clair d'utiliser cela est d'utiliser des [décorateurs](https://realpython.com/primer-on-python-decorators/). Leur utilisation générale en programmation dépasse le cadre de ce cours, nous allons juste utiliser ceux de python permettant de décorer des accesseurs et des mutateurs ici.

Considérons une classe qui possède, entre autres choses un attribut nommé `toto`{.language-} :

```python

class MaClasse:
   def __init__(self):
      # ...

      self.toto = 0

      # ...
   
   # ...

```

Cet attribut est public et on peut l'utiliser librement :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.toto = 42
>>> print(mon_objet.toto)
```

Si l'on rend cet attribut privé, il faut utiliser des accesseurs/mutateurs :

```python

class MaClasse:
   def __init__(self):
      self._toto = 0
   
   def get_toto(self):
      return self._toto

   def set_toto(self, nouveau_toto):
      self._toto = nouveau_toto

```

C'est plus safe, car maintenant, on peut faire attention à ce que l'on donne comme valeur à l'attribut, mais son utilisation est bien plus lourde :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.set_toto(42)
>>> print(mon_objet.get_toto())
```

Python permet de combiner les deux approches avec les décorateurs `@property`{.language-} :

```python

class MaClasse:
   def __init__(self):
      self._toto = 0
   
   @property
   def toto(self):
      return self._toto

   @toto.setter
   def toto(self, nouveau_toto):
      self._toto = nouveau_toto

```

Ce qu'on a fait :

* on *décore* la première méthode `MaClasse.toto()`{.language-} par le décorateur `@property`{.language-} pour lui signifier que cette méthode est l'accesseur de l'attribut `toto`{.language-}
* on *décore* la seconde méthode `MaClasse.toto()`{.language-} par le décorateur `@toto.setter`{.language-} pour signifier que cette méthode est le mutateur de l'attribut `toto`{.language-}

L'utilisation est alors pratique comme un attribut public et safe comme un attribut privé :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.toto = 42  # c'est le mutateur qui est utilisé par directement l'attribut
>>> print(mon_objet.toto)  # c'est l'accesseur qui est utilisé par directement l'attribut
```

{% faire %}
Utilisez l'attribut privé `Dé._position`{.language} avec un décorateur `@property`{.language-}.

Modifiez tous les tests et les programmes principaux.
{% endfaire %}

## Finalement

{% faire %}
Vérifier que tout fonctionne :

* les tests
* la user story
* le programme principal

{% endfaire %}
