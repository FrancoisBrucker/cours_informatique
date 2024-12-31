---
layout: layout/post.njk

title: Coder et développer
tags: ["cours", "code", "python"]
authors:
  - François Brucker

resume: "Ce cours est dédié au code informatique. Comment l'écrire, le tester et l'exécuter."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce cours est dédié au code informatique. On utilisera le language python comme support car c'est un langage très utilisé et qui permet de mettre en lumière tous les aspects du développement d'un code informatique. La très grande majorité des concepts que l'on verra seront cependant transposables dans d'autres langages (comme le javascript ou encore ruby par exemple).

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

<!-- fin résumé -->

## <span id="bases"></span>Bases

{% aller %}
[Bases de la programmation](bases-programmation){.interne}
{% endaller %}

Une fois les bases acquises, terminez cette partie en faisant le tutoriel de python qui reprend tout ce que nous avons vu de façon plus détaillée :

{% lien %}
<https://docs.python.org/fr/3/tutorial/index.html>
{% endlien %}

## <span id="s-équiper"></span> S'équiper pour le développement


### Un ordinateur pour le développement

- connaissances minimales du fonctionnement d'un ordinateur (application, process, mémoire)
- dossiers/fichiers
- terminal pour exécuter des commandes/applications

{% aller %}
[Un ordinateur pour le développement](ordinateur-développement){.interne}
{% endaller %}

### Installation d'un interpréteur

Lorsque l'on veut utiliser l'interpréteur python exécuter un programme informatique que l'on aura développé, il faut s'assurer que chaque exécution du programme soit identique.
Pour éviter les effets de bords (anciennes variables déclarées, modules importées, etc) Il est indispensable de pouvoir :

1. créer un nouvel interpréteur python pour **_chaque_** exécution du programme.
2. écrire notre programme en-dehors de tout interpréteur

{% aller %}
[Installer python](installer-python){.interne}
{% endaller %}

> TBD vscode terminal, installation de modules __name__, __file__, etc.

{% aller %}
[Prendre en main l'éditeur vscode](éditeur-vscode/prise-en-main/){.interne}
{% endaller %}

## <span id="développer"></span>Développer

> TBD refaire on fait des fichiers et on importe des choses sans l'avoir défini avant.

{% aller %}
[Écrire et exécuter du code](développement){.interne}
{% endaller %}

Python gère les noms de variables via un concept appelé espace de noms. Il est crucial de comprendre comment cela fonctionne pour ne pas laisser par au doute quand à savoir quelle variable est utilisée quand :

> TBD exercices : plein de fonctions différentes à créer (voir partie algorithmie ?). Utilisation de listes, suppression de doublon, recursion (flocon de koch ?) etc
>
> TBD faire de petits programmes

{% aller %}

> TBD : mettre espace de nom dans bases de python.

[Espace de nommage](espace-nommage){.interne}

> TBD exercices : variables locales vs globales/fonctions/ajout d'éléments dans une liste

{% endaller %}

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

> TBD ici versions de python

{% aller %}
[Déboguer son code](debugger){.interne}
{% endaller %}

> TBD exercices/projet

## Gestion des dépendances

On a utilisé [pip](<https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets)>) pour installer des modules python comme [pytest](https://docs.pytest.org/) (voir [partie modules](installer-python/#modules){.interne}). Nous allons voir dans cette partie comment créer ses propres modules et la gestion des modules par projets.

### Un interpréteur par projet

{% aller %}
[Environnements virtuels](environnements-virtuels){.interne}
{% endaller %}

## Stockage des données

### En mémoire

{% aller %}
[Données en mémoire](données-mémoire){.interne}
{% endaller %}

### Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

> TBD méthodes de chaines de caractères :
>
> - split
> - caractères spéciaux : tabulation, fin de ligne
> - strip
> - supprimer les accents. transformation et ascii. voir partie data

### Sur des fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

## Archétype de programmation

### Programmation objet

La programmation objet est un principe de programmation utilisé par la quasi-totalité des langages de programmation. Nes nuances existent bien sur, la programmation objet en rust n'est pas la même qu'en java par exemple, mais quelques principes fondateurs sont utilisés partout.

Nous allons dans cette partie du cours nous atteler à montrer ces principes et leur utilité dans le cadre du langage python.

{% aller %}
[Programmation objet](programmation-objet){.interne}
{% endaller %}

### Programmation évènementielle

La programmation évènementielle est un principe de développement très utilisé dans le développement de [GUI](https://fr.wikipedia.org/wiki/Interface_graphique). Le principe est de coder des _réactions_ qui seront exécutées lorsqu'un utilisateur effectuera une action spécifique (générant un _évènement_) comme cliquer sur quelque chose, appuyer sur une touche, etc.

{% aller %}
[Programmation évènementielle](programmation-évènementielle){.interne}
{% endaller %}

## Maintenir et développer du code sûr

### Programmation par les tests

On a pris l'habitude d'écrire des tests pour se rassurer quant à l'exactitude de nos fonctions. Mais pourquoi pas ne pas écrire les tests avant ? C'est le parti pris osé (mais très efficace) de la [programmation par les tests (_Test Driven Development_, ou _TDD_)](https://fr.wikipedia.org/wiki/Test_driven_development) que l'on vous propose d'essayer dans le projet ci-après.

{% aller %}
[Projet de programmation par les tests](projet-TDD){.interne}
{% endaller %}

### Couverture de code

La couverture de code est un outils essentiel lorsque l'on programme par les tests et plus généralement lorsque l'on code tout court. Cet outil permet de vérifier les lignes de codes qui sont testées (_ie._ couvertes).

{% aller %}
[Couverture de code](couverture-de-code){.interne}
{% endaller %}

## MISC modules

> TBD odds and ends

### packages

Lorsqu'un module devient important, il devient compliqué de mettre tout son code dans un seul fichier. On a alors coutume de rassembler tout le code du module dans un dossier que python appelle _package_.

{% lien %}
[package en python](https://docs.python.org/fr/3/tutorial/modules.html#packages)
{% endlien %}

Comme l'import d'un module revient à exécuter un fichier et qu'importer un package revient à importer un dossier, python exécute le fichier `__init__.py`{.fichier} présent dans le dossier.

{% note %}
Un _package_ est un dossier contenant un fichier `__init__.py`{.fichier}.

- importer le dossier revient à exécuter le fichier `__init__.py`{.fichier}.

- exécuter le dossier avec l'interpréteur revient à exécuter le fichier `__main__.py`{.fichier}.

{% endnote %}

### Où sont les modules python

Les dossiers où python va cherchez les modules sont listés dans la variable `sys.path` et dépendent de l'interpréteur utilisé :

{% attention %}
Il faut installer les modules en utilisant `python -m pip` et non directement le programme `pip`, car l'interpréteur pour lequel sera installé le module est ainsi explicite.
{% endattention %}

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

- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier _"random.py"_ qui contient le code du package `random`)
- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
- `/opt/homebrew/lib/python3.11/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

{% attention %}
La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilisant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connaît.
{% endattention %}

### Exécution de modules

#### Exécution d'un module comme un programme

On peut utiliser l'interpréteur python pour exécuter un module. Par exemple notre fichier `mon_module.py`{.fichier} précédent :

```shell
python mon_module.py
```

Si vous avez fait les exercices précédents votre fichier `mon_module.py`{.fichier} devrait être :


> TBD 
Il n'y a pas de différence fondamentale entre un programme et un module en python. C'est juste un programme dont on garde trace de son espace de noms `global`{.language-} après exécution.

#### Exécution d'un module python

Pour exécuter un module python on peut utiliser l'option `-m` de l'interpréteur python.

{% lien %}
[Option `-m` de l'interpréteur Python](https://docs.python.org/fr/3/using/cmdline.html#cmdoption-m)
{% endlien %}

On l'a déjà fait à de multiples reprises en utilisant le module pip :

```shell
python -m pip
```

Le résultat de la commande précédente dans le terminal affichera l'aide de `pip`{.fichier}.

{% faire %}
Exécutez le module `random`{.language-} de python dans le terminal avec la commande : `python -m random`.
{% endfaire %}

Si vous exécutez le module python `random`{.language-}, vous verrez s'afficher tout un tas de choses sur l'écran :

```shell
$ python -m random

0.000 sec, 10000 times random()
avg 0.498948, stddev 0.285393, min 1.74181e-05, max 0.999923

0.003 sec, 10000 times normalvariate(0.0, 1.0)
avg -0.00160272, stddev 1.00174, min -3.42565, max 3.90493

0.003 sec, 10000 times lognormvariate(0.0, 1.0)
avg 1.64736, stddev 2.19193, min 0.0147119, max 65.9514

0.004 sec, 10000 times vonmisesvariate(0.0, 1.0)
avg 3.11325, stddev 2.28549, min 0.000433248, max 6.28223

0.009 sec, 10000 times binomialvariate(15, 0.6)
avg 8.9936, stddev 1.89413, min 2, max 15

[...]
```

Ces lignes montrent le temps mis pour générer des nombres aléatoires selon plusieurs lois de probabilités.

Mais pourquoi ces lignes ne s'affichent-elles pas lorsque l'on importe le module random ?

#### Variable `__name__`{.language-}

{% lien %}
[`__name__`{.language-} et `__main__`{.language-} en python](https://docs.python.org/fr/3.12/library/__main__.html)
{% endlien %}

Python distingue les deux types d'exécutions d'un programme via la variable spéciale `__name__`{.language-} :

- elle vaut la chaîne de caractères `"__main__"`{.language-} si le fichier est exécuté directement
- elle vaut le nom du fichier s'il est exécuté via un import

{% faire %}
Créez un fichier nommé `test_exécution.py`{.fichier} et copiez/collez y le code suivant :

```python
print(__name__)
```

Exécutez le fichier précédant directement avec l'interpréteur puis via un import. Vous pourrez créez puis exécuter un fichier contenant uniquement la ligne de code `import test_exécution`{.language-}.
{% endfaire %}

Cette différence dans le nom d'une variable permet de différentier les deux types d'exécution et est parfois utilisé pour séparer le programme principal d'un fichier du reste du code avec :

```python
# code pouvant être importé

if __name__ == "__main__":
    # code du programme principal
```
