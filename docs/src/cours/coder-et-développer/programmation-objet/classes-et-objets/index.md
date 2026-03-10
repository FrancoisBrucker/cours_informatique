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

Un objet, n'est donc pas isolé, il partage ses fonctionnalités avec tous les objets de sa _classe_. Pour s'y retrouver entre, classes, objets méthode et attribut et trouver qui appartient à qui, python utilise les [espaces de noms](../../bases-programmation/espace-nommage/){.interne} (_namespaces_). Cela lui permet de réutiliser le même code pour plusieurs objets.

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

Ici notre besoin c'est de faire marcher le bout de code d'une façon plausible. Il faut se demander ce que veut l'utilisateur.


C'est du python.

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

#### Classes en python

La définition d'une classe est un bloc python :

```python

class <nom de la classe>:
    def __init__(self, paramètre 1, ..., paramètre n):
        instruction 1
        ...
        instruction p
    def méthode 1(self, paramètre 1, ..., paramètre n_1):
        instruction 1
        ...
        instruction p_1
        ...
    def méthode m(self, paramètre 1, ..., paramètre n_m):
        instruction 1
        ...
        instruction p_m
```

En python :

- le constructeur d'une classe sera **toujours** la méthode : `__init__`{.language-}. C'est une méthode spéciale.
- le 1er paramètre de chaque méthode est **toujours** `self`{.language-}. A l'exécution, python donnera à ce paramètre l'objet qui appelle la méthode, on ne le voit pas lorsque l'on écrit le code.

{% attention %}
La méthode `__init__`{.language-} n'a pas de `return`{.language-}, mais elle est utilisée dans le processus de création d'un objet.
{% endattention %}

`self`{.language-} peut souvent paraître magique. Une façon simple de comprendre ce qu'il fait est :

{% note %}
le premier paramètre de la définition d'une méthode noté `self`{.language-}, est l'objet à gauche du `.`{.language-} lors de l'appel à celle-ci par une notation pointée.

C'est la manière explicite de python de montrer quel objet est utilisé lors de l'appel de méthodes.
{% endnote %}
{% info %}
Vous pouvez appeler ce premier paramètre comme vous voulez, mais c'est **très très** déconseillé car votre code en deviendra moins lisible (tout le monde utilise le nom `self`{.language-}).
{% endinfo %}

#### Création d'un objet

En python, le retour de l'**_exécution d'une classe_** (l'utilisation de la classe comme si c'était une fonction) produit un objet. Par exemple :

```python
NomDeLaClasse(paramètre_1, ..., paramètre_n)
```

Ainsi :

- `list()`{.language-} : crée un objet de type `list`{.language-} (une liste), sans paramètre.
- `int()`{.language-} : crée un objet de type `int`{.language-} (un entier) sans paramètre (c'est 0).
- `int(3.1415)`{.language-} : crée un un objet de type `int`{.language-} avec un paramètre, valant le réel 3.1415 (c'est 3)
- `float("3.1415")`{.language-} : crée un objet de type `float`{.language-} (un réel) avec un paramètre valant la chaîne de caractères `"3.1415"`{.language-}.
- `list(range(5))`{.language-} : crée un objet de type `list`{.language-} avec comme unique paramètre le résultat de la fonction `range`

{% info %}
Certains objets se créent juste avec leur valeur comme les entiers, les réels ou encore les chaines de caractères. En python `3`{.language-} est équivalent à `int(3)`{.language-} par exemple.
{% endinfo %}

Python exécute cette instruction de création en :

1. créant un objet vide `o`{.language-} de type `MaClasse`{.language-}
2. il associe à l'objet un espace de nom dont le parent est l'espace de nom de sa classe
3. il exécute le constructeur `__init__`{.language-} sur l'objet : `MaClasse.__init__(o, paramètre 1, ..., paramètre n)`{.language-} (c'est pour ça que la méthode `__init__`{.language-} n'a pas de retour)
4. il rend l'objet `o`{.language-}

#### Compteur

La classe python qui correspond à l'UML précédent est celle-ci, contenu dans le fichier `compteur.py`{.fichier}, placé dans le même dossier que le fichier `main.py`{.fichier} :

```python
class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrémente(self):
        self.valeur = self.valeur + 1

```

La classe `Compteur`{.language-} contient :

- `__init__`{.language-} est le constructeur : **on déclare tous les attributs d'un objet dans celui-ci**.
- une méthode : `incrémente`{.language-}


Par exemple dans le code la ligne `c1.incrémente()`{.language-} sera transformée par python en : `Compteur.incrémente(c1)`{.language-} qui peut se lire : on exécute la fonction `incrémente`{.language-} de l'espace de noms du bloc `Compteur`{.language-} avec comme paramètre `c1`{.language-}.

La première façon d'écrire (`c1.incrémente()`{.language-}) est plus simple à comprendre **pour un humain** et évite les erreurs (la méthode est appliquée à l'objet à gauche du point), alors que la seconde est plus facile à comprendre **pour un ordinateur** en utilisant les espaces de noms et le passage explicite de l'objet appelant.

### Exécution du code

{% note %}
Lorsque l'on définit une classe, python lui associe un espace de noms. Les différents noms définit dans la classes y seront consignés.
{% endnote %}

Dans l'exemple du compteur, lorsque le fichier `main.py`{.fichier} importe le fichier `compteur.py`{.fichier}, la classe `Compteur`{.language-} y est définie. Dans son namespace seront alors placés les noms :

- `__init__`{.language-}
- `incrémente`{.language-}

Qui correspondent aux noms des 2 méthodes définies dans la classe.

De même :

{% note %}
Lorsque l'on crée un objet, python lui associe un espace de noms.

Son espace de noms parent est celui de sa classe.
{% endnote %}

L'espace de noms de l'objet est important, il est utilisé à chaque notation pointée. Par exemple dans la méthode `__init__`{.language-}, la ligne `self.valeur = 0`{.language-} crée un objet entier (valant 0) et l'affecte au nom `valeur`{.language-} dans l'espace de noms de l'objet nommé `self`{.language-}.

Reprenons le code de `main.py`{.fichier}, et exécutons le ligne à ligne :

```python/
from compteur import Compteur

c1 = Compteur()
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c2.valeur)
```

1. lorsque python commence l'exécution du fichier, il crée le namespace global. C'est le namespace le plus haut.
2. `from compteur import Compteur`{.language-} :
   1. cherche un fichier `compteur.py`{.fichier} dans le répertoire courant.
   2. on crée un espace de noms `compteur`
   3. Python exécute le fichier `compteur.py`{.fichier} (il lit chaque ligne) dans l'espace de noms `compteur`.
   4. Une fois ceci fait, il prend le nom `Compteur`{.language-} dans cet espace et l'ajoute dans l'espace de noms `global`. On peut donc utiliser le nom `Compteur`{.language-}
3. `c1 = Compteur()`{.language-} :
   - en informatique `=`{.language-} n'est pas symétrique. A gauche un nom à droite un objet. Ici ceci signifie que l'on ajoute le nom `c1`{.language-} au namespace global et que sa valeur sera le résultat de `Compteur()`{.language-}
   - `Compteur()`{.language-} : est le résultat de l'exécution du nom `Compteur`{.language-}. Les parenthèses (et les paramètres éventuels) après un nom l'exécute. (si on avait juste écrit `c1 = Compteur`{.language-} on aurait alors eu un nom `c1`{.language-} qui sera égal à la classe `Compteur`{.language-}).
   - `Compteur()`{.language-} Exécuter une classe revient à :
     - créer un objet vide et lui associer un espace de noms vierge
     - chercher la méthode `__init__`{.language-} de la classe et l'exécuter en passant le nouvel objet en premier paramètre :
       - pour exécuter une fonction on crée un namespace pour elle.
       - on place le nom `self`{.language-} qui vaut ici le nouveau namespace créé
       - la première ligne crée le nom `valeur`{.language-} dans l'espace de noms de l'objet `self`{.language-}
       - la fonction étant terminée, on supprime l'espace de noms de la fonction (qui contenait le nom `self`{.language-})
       - on rend l'objet
   - l'objet créé est associé au nom `c1`{.language-} dans le namespace `global`
4. idem que la ligne précédente avec un nouvel objet
5. `c1.incrémente()`{.language-} : python cherche le nom `incrémente`{.language-} dans l'espace de noms de l'objet nommé `c1`{.language-}.
   1. Il regarde d'abord dans l'objet de nom `c1`{.language-}. Ça n'y est pas (dans l'espace de noms de `c1` il n'y a que le nom `valeur`{.language-}).
   2. Il regarde donc dans l'espace de noms parent : l'espace de noms de de la classe. Il y est puisqu'`incrémente`{.language-} est une fonction définie.
   3. On peut maintenant exécuter cette fonction. Comme pour toutes les fonctions définies dans une classe et utilisée par un objet, le premier paramètre est l'objet (le self). Ce mécanisme permet d'utiliser les noms définis dans l'espace de noms de l'objet (ici la valeur de l'objet).
6. idem que la ligne d'avant
7. idem que la ligne d'avant
8. `print(c1.valeur)`{.language-} : comme pour la ligne 5, python cherche le nom `valeur`{.language-} dans l'espace de noms de l'objet nommé `c1`{.language-}. Il le trouve et le rend.

{% note %}
`objet.nom`{.language-} est **toujours** résolu de façon identique en python : on commence par chercher le nom dans l'objet et si on ne le trouve pas on cherche dans sa classe.
{% endnote %}
