---
layout: layout/post.njk
title: Classes et objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un objet est un bout de code auquel est associé :

- des fonctionnalités (des méthodes) qui sont communes à tous les objets de sa classe
- des choses à lui tout seul (sa structure de donnée interne qui constitue ses attributs) qui lui permettent de se différentier des autres objets de sa classe même s'il a les mêmes fonctionnalités.

Un objet, n'est donc pas isolé, il partage ses fonctionnalités avec tous les objets de sa _classe_.

## Utiliser des objets

Lorsque l'on écrit du code python, on ne fait que manipuler des objets. Les entiers, les chaines de caractères, les listes et même les fonctions **sont** des objets :

```python
i = 43
s = "coucou"
l = [1, 2, 3]
f = lambda x: x - 1
```

On peut utiliser des objets via des opérateurs ou des fonctions. Par exemple :

```python
print(f(i))
```

{% exercice %}
Que fait le code précédent ?
{% endexercice %}
{% details "corrigé" %}

Dans un interpréteur :

```python
>>> i = 43
>>> s = "coucou"
>>> l = [1, 2, 3]
>>> f = lambda x: x - 1
>>> print(f(i))
42

```

Il affiche le résultat de la fonction `f`{.language-} (qui rend un entier valant son paramètre d'entrée moins 1) avec comme paramètre l'entier associé à la variable `i`{.language-} (un entier valant 43).
{% enddetails %}

Mais un objet est plus que ça. Il contient à la fois **des données** (les différents caractères d'une chaîne de caractères par exemple) et **des méthodes** permettant d'opérer dessus. Par exemple :

```python
print(s.upper())
```

{% exercice %}
Que fait le code précédent ?
{% endexercice %}
{% details "corrigé" %}

Dans un interpréteur :

```python
>>> i = 43
>>> s = "coucou"
>>> l = [1, 2, 3]
>>> f = lambda x: x - 1
>>> print(s.upper())
COUCOU

```

Il affiche le résultat de la méthode `upper`{.language-} appliquée à l'objet associé à la variable `s`{.language-}.
{% enddetails %}

Les méthodes sont spécifiques à des types d'objets particulier, ainsi le code suivant ne fonctionne pas, la méthode `upper`{.language-} n'**est pas définie** pour les entiers :

```python
print(i.upper())
```


{% exercice %}
Que fait le code précédent ?
{% endexercice %}
{% details "corrigé" %}

Dans un interpréteur :

```python
>>> print(i.upper())
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    print(i.upper())
          ^^^^^^^
AttributeError: 'int' object has no attribute 'upper'
```

Python rend une erreur. Nous comprendrons sa signification profonde plus tard, pour l'instant cela nous indique juste que la méthode `upper`{.language-} n'existe pas pour les entiers : `'int' object has no attribute 'upper'`{.language-}
{% enddetails %}

Les méthodes sont ainsi associées au type de l'objet. Ce sont des fonctions définis dans l'espace de nom de la classe associé. Ainsi comme le type d'une chaîne de caractères est `str`{.language-} en python :

```python
>>> type(s)
<class 'str'>
```

On peut tout à fait écrire :

```python
print(str.upper(s))
```

Où on utilise directement la fonction `upper` des chaînes de caractères. Remarquez que dans ce cas il faut expliciter le paramètre. 

Une classe :

- permet de créer un type d'objet (une structure de donnée précise)
- définit les opérations (méthodes) utilisables par ces objets.

Un objet issu d'une certaine classe :

- possède la même structure de données que les autres objets de la classe mais les valeurs de celle-ci lui sont uniques : ses **attributs**
- possède un lien vers les **méthodes** (définies dans sa classe) qu'il peut utiliser via la [notation pointée](../../bases-programmation/espace-nommage/#notation-pointée){.interne} : `objet.méthode(paramètre_1, ..., paramètre_n)`{.language-}

{% attention2 "**À retenir**" %}
La programmation objet n'a pas pour but de révolutionner votre façon de programmer. Elle permet juste de bien mettre en œuvre les paradigmes de développement que l'on a vus jusqu'à présent. Il est fortement conseillé de _coder objet_ car :

- cela favorise la factorisation du code ([on ne se répète pas](../../écrire-code/coder#DRY){.interne}) : on ne définit ses méthodes qu'une seule fois dans les classes
- lisibilité avec la notation `.`{.language-} : on sait clairement à qui s'applique telle ou telle méthode
- compartimentation du code : chaque partie du code et chaque opération est compartimentée, ce qui permet de les tester et des améliorer indépendamment du reste du code.
- plutôt que de créer un gros programme complexe, on crée plein de petits programmes indépendants (les objets) qui interagissent entre eux.
{% endattention2 %}

{% info %}
Ces principes sont mis en œuvre de façon différentes selon les langages mais on retrouvera toujours ces notions.
{% endinfo %}

## Exemples de classes en python

Ce qui caractérise un objet est ce qu'on peut faire avec, c'est à dire ses méthodes. Une classe regroupe un ensemble de méthodes permettant de résoudre un problème spécifique. Que ce problème soit lié au type de données (chaîne de caractères, entier, ...) qu'à leurs usages (mesurer le temps, graphiques, ...).

Voyons quelques exemple de classes python et leurs usages.

### Chaîne de caractères

Les chaines de caractères sont des objets de la classe ([str](https://docs.python.org/fr/3/library/string.html)) :

```python
>>> type("une chaîne")
<class 'str'>
```

Les méthodes définies dans la classe `str`{.language-}, comme `capitalize()`{.language-} par exemple sont utilisables par tous les objets de la classe `str`{.language-} (dans l'exemple ci-après par l'objet `"coucou"`{.language-} et l'objet `"toi"`{.language-}) :

```python
>>> "coucou".capitalize()
'Coucou'
>>> "toi".capitalize()
'Toi'
```

La notation pointée permet de dire que c'est la méthode à droite du `.`{.language-} que l'on cherche dans l'objet à gauche du point.

{% exercice %}
Le code suivant produit une erreur. Pourquoi ?

```python
>>> capitalize("coucou")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'capitalize' is not defined
```

{% endexercice %}
{% details "solution" %}
C'est la méthode définie dans la classe `str`{.language-} qui s'appelle `capitalize`{.language-} qui existe...
{% enddetails %}

Le résultat est différent lorsque l'on applique la méthode `capitalize`{.language-} à la chaîne de caractères `"bonjour"`{.language-} ou à la chaîne de caractères `"toi"`{.language-} car ces deux chaînes de caractères, bien que de la même classe (`str`{.language-}), sont différents : dans l'un il y a la chaîne "bonjour", dans l'autres la chaîne "toi".

Remarquez que l'application de la méthode ne change pas sa valeur :

```python
>>> s = "coucou"
>>> s.upper()
'COUCOU'
>>> print(s)
coucou
```

Pour conserver le résultat de la méthode, il faut le placer dans une autre variable :

```python
>>> s_prim = s.upper()
>>> print(s_prim)
COUCOU
>>> print(s)
coucou

```

Enfin, une méthode peut avoir des paramètres  comme la méthode [`str.center`{.language-}](https://docs.python.org/fr/3.14/library/stdtypes.html#str.center) :

```python
>>> print(s.center(25, "*"))
**********coucou*********
```

Et même rendre autre chose que son type d'origine comme la méthode [`str.count`{.language-}](https://docs.python.org/fr/3.14/library/stdtypes.html#str.count)  :

```python
>>> print(s.count("c"))
2
```

La notation pointée est très pratique puisque l'on peut chaîner les instruction. Par exemple, considérons la ligne de code :

```python
"coucou".upper().count("U")
```

Pour comprendre son exécution, on analyse la ligne :

1. on exécute la méthode `count`{.language-} de l'objet à gauche du `.`, c'est à dire `"coucou".upper()`{.language-}. **Attention** C'est bien toute la partie gauche, pas seulement jusqu'au `.`{.language-} suivant.
2. l'objet `"coucou".upper()`{.language-} est le résultat de la méthode `upper`{.language-} appliquée à l'objet à gauche du `.`, c'est à dire la chaîne de caractères `"coucou"`{.language-}.
3. le résultat de `"coucou".upper()`{.language-} est ainsi égal à l'objet `"COUCOU"`{.language-}
4. donc `"coucou".upper().count("U")`{.language-} est égal à `"COUCOU".count("U")`{.language-} qui vaut 2


### Entiers

Les entiers sont aussi des objets d'une classe : `int`{.language-}.

```python
>>> type(1)
<class 'int'>
```

Contrairement à la classe `str`{.language-}, la classe `int`{.language-} ne définit pas de méthode mais des opérations. Par exemple `__add__`{.language-} définit l'addition d'un entier par un autre objet. C'est pratique que tout soit défini dans la classe , cela nous permettra à nous aussi de faire nos propres additions.

Les trois écritures sont identiques en python, mais bien sur, nous préférerons la première, bien plus simple à écrire et à comprendre :

1. `1 + 2`{.language-}
2. `int.__add__(1, 2)`{.language-}
3. `(1).__add__(2)`{.language-}

{% info %}
Remarquez que l'opération `+`{.language-} n'est pas identique pour `1 + 2`{.language-} et `1.0 + 2`{.language-}. Dans le premier cas c'est l'addition définie dans `int`{.language-} qui est utilisé, dans le second cas c'est celle définie dans `float`{.language-}.
{% endinfo %}

En python les méthodes qui commencent et finissent par deux underscores (le caractère `_`, aussi parfois improprement appelé _tiret-du-huit_ car c'est ce caractère qui est sous le 8 pour des claviers français PC (ce n'est pas vrai sur mac et encore moins pour d'autres types de claviers)) sont des méthodes utilisées par python dans des cas spécifiques, on ne les utilisera quasi-jamais de façon explicite.

### Listes

Les entiers et les chaînes de caractères sont des objet dit **_immutable_** c'est à dire qu'aucune de leurs méthodes ne les modifient : elles ne font que rendre de nouveaux objets. Ce n'est pas le cas des listes.

```python
>>> l = [1, 2, 3]
>>> l.extend([4, 5, 6])
>>> print(l)
[1, 2, 3, 4, 5, 6]

```

La liste `l`{.language-} est **modifiée** par la méthode [`list.extend`{.language-}](https://docs.python.org/fr/3.14/library/stdtypes.html#list.extend). Le fait qu'une méthode modifie ou pas l'objet passé en paramètre n'est pas réglementé. Certaines le font d'autres non :


```python
>>> l = [1, 2, 3]
>>> l + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> print(l)
[1, 2, 3]

```

Mais souvent les méthodes qui ne rendent rien (donc qui rendent `None`) modifient les objets :

```python
>>> l = [1, 2, 3]
>>> print(l.extend([4, 5, 6]))
None

```

Terminons cette partie par deux petit exercices pour voir si vous avez compris :

{% exercice %}
Que produit le code suivant :

```python
[1, 2, 3] + "nous irons au bois"
```
{% endexercice %}
{% details "corrigé" %}
Une erreur :

```python
>>> [1, 2, 3] + "nous irons au bois"
Traceback (most recent call last):
  File "<python-input-39>", line 1, in <module>
    [1, 2, 3] + "nous irons au bois"
    ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
TypeError: can only concatenate list (not "str") to list

```

Car on ne peut additionner que deux listes.

{% enddetails %}
{% exercice %}
Que produit le code suivant :

```python
[1, 2, 3] + "nous irons au bois".split()
```

{% endexercice %}
{% details "corrigé" %}
Là ça marche car le résultat de [`str.split`{.language-}](https://docs.python.org/fr/3.14/library/stdtypes.html#str.split) est une liste :

```python
>>> [1, 2, 3] + "nous irons au bois".split()
[1, 2, 3, 'nous', 'irons', 'au', 'bois']
```

{% enddetails %}

### Complexes

Saviez-vous qu'il y a une classe pour les complexes ?

```python
>>> print(1j ** 2)
(-1+0j)
>>> z = 2 - 1j *0.5
>>> print(z)
(2-0.5j)
>>> print(type(z))
<class 'complex'>

```

Un complexe se caractérise par sa partie réelle et sa partie imaginaire. Comment y accéder?

```python
>>> x = z.real
>>> y = z.imag
>>> print(x, y)
2.0 -0.5
>>> print(type(x), type(y))
<class 'float'> <class 'float'>

```

Comment calculer le conjugué ?

```python
>>> zc = z.conjugate()
>>> print(zc, type(zc))
(2+0.5j) <class 'complex'>

```

### Dates

Ça existe et c'est très pratique !

```python
import datetime
année_scolaire = datetime.datetime(day=3, month=9, year=2024, hour=9, minute=0, second=0)
print(type(année_scolaire))
print(année_scolaire)
```

Le code précédent va afficher :

```python
<class 'datetime.datetime'>
2024-09-03 09:00:00
```

Les attributs de la date sont accessibles :

```python
print(année_scolaire.day)
print(année_scolaire.month)
print(année_scolaire.year)
print(année_scolaire.hour, année_scolaire.minute, année_scolaire.second)
```

Qui va afficher :

```python
3
9
2024
9 0 0
```

Enfin, on peut prendre la date actuelle :

```python
now = datetime.datetime.today()
print(type(now))
print(now)
```

Ce qui produira :

```python
<class 'datetime.datetime'>
2025-03-19 10:49:34.921872
```

Et on peut manipuler des dates comme des nombres :

```python
d = now - année_scolaire
print("Mon année scolaire a commencé depuis", d.days, "jours et", d.seconds, "secondes.")
```

Bref, l'usage de d'objets et de classes permet une utilisation intuitive de concepts compliqués à implémenter 

{% info %}
N'essayez pas de faire des manipulation de dates à la main, il y a plein d'exceptions qui fait que c'est l'enfer à faire correctement.
{% endinfo %}

### Graphiques

Là aussi, ce sont des objet et des classes :

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,2, figsize=(8, 2.5))
axes[0].plot([-1, 1, 5], [0, 3, 2])
axes[0].set_xlabel('Temps t')
axes[0].set_ylabel('f(t)')
axes[0].set_title('Courbe de gauche')
axes[1].plot([x for x in range(-10, 10)])
axes[1].plot([x ** 2 - 50 for x in range(-10, 10)])
axes[1].set_axis_off()
axes[1].set_title('Courbes de droite')
print(type(fig))
print(type(axes), axes.shape)
print(type(axes[0]))
plt.show()

```

Qui va écrire dans le terminal :

```python
<class 'matplotlib.figure.Figure'>
<class 'numpy.ndarray'> (2,)
<class 'matplotlib.axes._axes.Axes'>

```

Et ouvrir une nouvelle fenêtre avec le graphique suivant :

![graphique](./graphiques.png)

## <span id="compteur"></span>Créer ses propres classes

De façon générale, on peut définir un objet et une classe comme :

{% note2 "**Définition**" %}
Un **_objet_** est une structure de données (les champs de la structure de donnée sont appelés **_attributs_**) sur laquelle on peut effectuer des opérations (appelées **_méthodes_**).

Pour pouvoir facilement créer une structure particulière et donner un moyen simple d'effectuer les opérations sur celle-ci, on utilise des **_classes_** comme patron de ces objets :
- elles vont gérer la création des objets via un **_constructeur_**.
- elles contiennent dans leur espace de noms les différentes **_méthodes_** que l'on pourra appliquer

{% endnote2 %}

<div id="compteur-code"></div>

On crée une classe par rapport à un besoin que l'on veut satisfaire. Supposons que l'on veuille créer une classe compteur qui permettent d'exécuter le code suivant :

```python/
from compteur import Compteur

c1 = Compteur()
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c2.valeur)
```

Pour construire cette cette classe, il faut se poser la question :

- _"que dois-je pouvoir faire avec mon compteur ? "_ ce qui permettra de déterminer les méthodes de la classe
- _"que dois-je stocker comme information pour que les méthodes fonctionnent ?"_ ce qui permettra de déterminer les attributs de chaque objet.

### Analyse du besoin

Ici notre besoin c'est de faire marcher le bout de code d'une façon plausible. Il faut se demander ce que veut l'utilisateur de ce code python.

Le programme commence par importer le mot `Compteur`{.language-} d'un module nommé `compteur`{.language-} (donc placé dans un fichier  nommé `compteur.py` dans le dossier du projet) et on l'exécute 2 fois pour l'affecter à 2 noms différents. Pour voir ce que peut être `Compteur`{.language-}, plusieurs indices :

- cela **ne doit pas être** une fonction normale, sinon `c1`{.language-} et `c2`{.language-} seraient identiques.
- le mot `Compteur`{.language-} à une majuscule, ce qui correspond (par convention) en python à des noms de classes 

A la lecture du code, on a donc _envie_ que le code :

1. création de deux compteurs
2. en incrémente un deux fois et l'autre qu'une seule fois
3. affiche à l'écran la valeur d'un des compteurs (celui qui a été incrémenté une fois) qu'on suppose égale à 1

Un objet est un ensemble de fonctionnalités récurrentes dans un programme. Ici un compteur. Les fonctionnalités sont :

- ajouter une unité à un compteur
- connaître la valeur du compteur.

Pour que l'on puisse avoir plusieurs compteurs (si on n'a qu'un seul compteur, ce n'est pas la peine de faire des objets), il faut que chaque compteur ait une valeur à lui.

### Modélisation UML

On va essayer de comprendre le code pour produire une représentation UML de la classe `Compteur`{.language-}.

#### Bases d'UML

Pour représenter les différentes possibilités offertes par une classe on utilise l'[Unified Modeling Language (UML)](<https://fr.wikipedia.org/wiki/UML_(informatique)>)

{% lien %}
Vous pouvez suivre ce petit [tutoriel UML](https://www.sparxsystems.fr/resources/tutorials/uml/datamodel.html) pour comprendre sa notation et son utilité.
{% endlien %}

L'UML peut être très compliqué. Nous allons uniquement l'utiliser ici comme une représentation synthétique d'une classe/objet. Vous le verrez dans les exemples ci-dessous mais, en gros, une classe en UML c'est le diagramme :

![une classe UML](classes-1.png)

- pour chaque attribut on pourra préciser le _type_ (entier, chaîne de caractères, une classe particulière d'objet, ...) si c'est important
- pour chaque méthode on donnera sa [signature](https://developer.mozilla.org/fr/docs/Glossaire/Signature/Fonction) complète (son nom et ses paramètres) pour que l'on puisse l'utiliser.
- le constructeur de la classe sera désigné par le nom de la classe

On peut même combiner les diagramme UML ensemble. Par exemple un point et un polygone :

![point / polygone](uml-exemple-1.png)

Ou le classique personne et compte bancaire :

![personne / compte](uml-exemple-2.png)

#### Compteur

On souhaite créer un objet `Compteur`{.language-} qui retient le compte de quelque chose et est capable d'ajouter 1 à son compte quand on le lui demande. On suppose donc que `Compteur`{.language-} est une _classe_, par conséquent son exécution correspond à la création d'objets : `c1`{.language-} et `c2`{.language-} des objets de type `Compteur`{.language-}.

De là, `incrémente`{.language-} est une méthode de la classe `Compteur`{.language-} et `valeur`{.language-} un attribut des objets `c1`{.language-} et `c2`{.language-}

- Les objets d'une classe **partagent les mêmes méthodes**, donc `incrémente()`{.language-} doit faire la même chose pour `c1`{.language-} et `c2`{.language-}
- Les objets d'une même classe partagent la même structure de donnée (les **noms** des attributs sont les mêmes), je dois donc pouvoir écrire : `c1.valeur`{.language-}, même si ce n'est pas écrit dans le code.

Enfin, comme le code appelle `c1.incrémente()`{.language-} et `c2.incrémente()`{.language-} sans paramètre et que le retour de la méthode n'est pas conservée, cette méthode doit sûrement modifier un attribut des objets `c1`{.language-} et `c2`{.language-}, probablement `valeur`{.language-}

{% note %}
Un code dont les objets sont bien nommés doit pouvoir se lire et être interprétable sans connaître le corps des fonctions et méthodes utilisées.
{% endnote %}

En conclusion on a :

- un nom : Compteur
- une méthode (**=** fonctionnalités **=** ce qui est pareil pour tous les objets) : `incrémente()`{.language-}
- un attribut (**=** structure de donnée **=** ce qui est différent pour chaque objet) : `valeur`{.language-}

{% attention2 "**À retenir**"  %}

Pour créer un diagramme UML :

1. on commence toujours par le nom de la classe
2. on explicite ses méthodes, c'est à dire comment on va utiliser les objets (ici incrémenter un compteur).
3. on crée la structure de données qui va permettre de stocker les informations nécessaires à son utilisation : ce sont les attributs (ici un entier pour stocker le nombre de fois où on l'a incrémenté).

{% endattention2 %}

Ce qui donne le diagramme UML du compteur :

![compteur](classes-2.png)

### Implémentation en python

La modélisation UML ne nous indique pas l'implémentation des différentes méthodes, il nous indique juste comment on peut les utiliser. Pour exécuter et utiliser notre compteur, il faut le coder.

{% lien %}
N'hésitez pas à jeter un coup d'œil au [tutoriel de python sur ses classes](https://docs.python.org/fr/3/tutorial/classes.html). Ce cours est là pour vous montrer tout ce qu'il y a dedans, à part (peut-être) la partie sur l'héritage et les itérateurs.
{% endlien %}


<div id="compteur-classe"></div>

La modélisation UML se transcrit presque mot pour mot en python. En codant la classe suivante dans un fichier nommé `compteur.py`{.fichier} l'exemple va fonctionner :

```python/
class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrémente(self):
        self.valeur = self.valeur + 1

```

On va détailler plus tard les méthodes et moyens de construire des classes en python mais de l'écriture de la classe compteur on peut d'ores et déjà en déduire que :

- une classe est un bloc python
- le constructeur est une fonction définie dans le bloc de classe et qui s'appelle `__init__`{.language-}
- les attributs sont assignés dans l'espace de nom d'un objet nommé `self`{.language-} qui est le premier paramètres de toutes les fonctions définies dans la classe
- les méthodes sont des fonctions définies dans la classe

## Classes en python

### Définition de classes

La définition d'une classe est un bloc python contenant deux parties :

```python

class <nom de la classe>:
    def __init__(self, paramètre 1, ..., paramètre n):
        # création des attributs
        # initialisation de l'objet
    def méthode(self, paramètre 1, ..., paramètre n_1):
        # ...
        # instructions de la méthode
        # ...
    # autres méthodes
```

- La première partie est constituée du constructeur nommé `__init__`{.language-}
- La seconde parties est constituées des différentes méthodes

En python, toutes les méthodes sont des fonctions définies dans le bloc classe :

- le constructeur d'une classe sera **toujours** la méthode : `__init__`{.language-}. C'est une méthode spéciale.
- le 1er paramètre de chaque méthode est **toujours** `self`{.language-}. A l'exécution, python donnera à ce paramètre l'objet qui appelle la méthode, on ne le voit pas lorsque l'on écrit le code.

{% attention %}
La méthode `__init__`{.language-} n'a pas de `return`{.language-}, mais elle est utilisée dans le processus de création d'un objet.
{% endattention %}

De façon formelle :

{% note2 "**Définition**" %}
Une classe en python est un **_objet de type classe_** contenant [un espace de nommage](../../bases-programmation/espace-nommage/){.interne}.

{% endnote2 %}

Reprenons [l'exemple de la classe compteur](./#compteur-code){.interne} et examinons son exécution. à la fin de la ligne 1, on vient d'importer le module `compteur`{.language-} qui [contient uniquement une définition de classe](./#compteur-classe){.interne}, on est dans le cas suivant :

![](compteur-code-1.png)

L'espace de nommage de la classe `Compteur`{.language-} contient deux méthodes (les fonctions définies dans une classes sont appelées méthodes) :

- `__init__`{.language-} qui est le constructeur de la classe
- `incrémente`{.language-} qui est une méthode

Les deux méthodes prennent comme premier paramètre un objet nommé `self`{.language-}, qui est la manière explicite de python de montrer quel objet est utilisé lors de l'appel de méthodes :

{% note2 "**Définition**" %}
le premier paramètre de toute méthode, noté `self`{.language-}, est l'objet sur lequel on va appliquer la méthode (l'objet à gauche du `.`{.language-} lors de l'appel à celle-ci par une notation pointée).

{% endnote2 %}
{% info %}
Vous pouvez appeler ce premier paramètre comme vous voulez, mais il est **très très** déconseillé de le faire car votre code en deviendra moins lisible (tout le monde utilise le nom `self`{.language-}).
{% endinfo %}


### Création d'un objet

En python, le retour de l'**_exécution d'une classe_** (l'utilisation de la classe comme si c'était une fonction) produit un objet. Par exemple :

- `list()`{.language-} : crée un objet de type `list`{.language-} (une liste), sans paramètre.
- `int()`{.language-} : crée un objet de type `int`{.language-} (un entier) sans paramètre (c'est 0).
- `int(3.1415)`{.language-} : crée un un objet de type `int`{.language-} avec un paramètre, valant le réel 3.1415 (c'est 3)
- `float("3.1415")`{.language-} : crée un objet de type `float`{.language-} (un réel) avec un paramètre valant la chaîne de caractères `"3.1415"`{.language-}.
- `list(range(5))`{.language-} : crée un objet de type `list`{.language-} avec comme unique paramètre le résultat de la fonction `range`

{% info %}
Certains objets se créent juste avec leur valeur comme les entiers, les réels ou encore les chaines de caractères. En python `3`{.language-} est équivalent à `int(3)`{.language-} par exemple.
{% endinfo %}

Le code suivant :

```python
o = MaClasse(paramètre_1, ..., paramètre_n)
```

Va créer un objet de type `MaClasse`{.language-} en effectuant les différentes étapes suivantes :

1. créant un objet vide `o`{.language-} de type `MaClasse`{.language-} contenant un espace de nommage dont le parent est l'espace de nommage de sa classe
2. il exécute le constructeur `__init__`{.language-} sur l'objet : `MaClasse.__init__(o, paramètre 1, ..., paramètre n)`{.language-} (c'est pour ça que la méthode `__init__`{.language-} n'a pas de retour)

En prenant [l'exemple du compteur](./#compteur-code){.interne}. l'exécution de la ligne 3 (`c1 = Compteur()`{.language-}) se déroule comme suit :

1. Création d'un nouvel objet :
    ![](compteur-code-2.png)
2. Exécution du constructeur `__init__`{.language-} avec le nouvel objet en paramètre. À la fon de l'exécution du constructeur on est dans la configuration suivante :
    ![](compteur-code-3.png)

On refait pareil pour la ligne 4 (`c2 = Compteur()`{.language-}), ce qui fait qu'on se trouve dans l'état suivant :

![](compteur-code-4.png)

Comme le constructeur est toujours appliqué au nouvel objet créé chaque objet va bien avoir des attributs distincts !

{% attention2 "**À retenir**" %}
En python, les attributs d'un objet **sont explicitement créés** dans le constructeur.
{% endattention2 %}


### Exécution de méthodes

L'exécution de méthodes se fait simplement en utilisant les règles des espaces de nommages et de la notation pointée.

1. on cherche le nom (potentiellement récursivement) dans l'espace de nommage 
2. l'objet appelant est donné comme premier paramètre de la méthode.

Ainsi pour [l'exemple du compteur](./#compteur-code){.interne}, l'exécution de la ligne 5 (`c1.incrémente()`{.language-}) se déroule comme suit :

1. on cherche le nom `incrémente`{.language-} dans l'espace de nommage de `c1`{.language-}. Il n'y est pas
2. on cherche alors le nom `incrémente`{.language-} dans l'espace de nommage parent, c'est celui de sa classe et on le trouve !
3. on exécute la méthode `incrémente`{.language-} en plaçant l'objet appelant (ici `c1`{.language-}) en premier paramètre de la méthode
4. La méthode accède aux différents attributs de l'objet en utilisant la notation pointée ((ici `self.valeur`{.language-}))

Le résultat de l'exécution de la ligne 5 est alors :

![](compteur-code-5.png)

À vous pour vérifier que vous avez compris :

{% exercice %}
Donnez le schéma des espaces de nommages jusqu'après l'exécution de la ligne 7 de [l'exemple du compteur](./#compteur-code){.interne}.
{% endexercice %}
{% details "corrigé" %}
![](compteur-code-6.png)
{% enddetails  %}
{% exercice %}
Détaillez l'exécution de la ligne 9 de [l'exemple du compteur](./#compteur-code){.interne} (`print(c2.valeur)`{.language-}).
{% endexercice %}
{% details "corrigé" %}

1. on cherche à exécuter la fonction `print`{.language-} : il faut trouver l'objet qui est son premier paramètre
2. son paramètre est l'objet associé au nom `valeur`{.language-} dans l'espace de nommage de l'objet associé au nom `c2`{.language-}
3. le nom `c2`{.language-} existe dans l'espace des variables, c'est un objet de la classe `Compteur`{.language-}
4. L'espace de nommage de cet objet contient le nom `valeur`{.language-} qui est associé à un entier valant 1 : c'est notre paramètre de la fonction `print`{.language-}
5. on affiche à l'écran un entier valant 1.
{% enddetails  %}