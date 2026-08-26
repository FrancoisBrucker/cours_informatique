---
layout: layout/post.njk

title: Apprendre la programmation
tags: ["code", "python"]
authors:
  - François Brucker

resume: "Ce cours est dédié au code informatique. Comment l'écrire, le tester et l'exécuter."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce cours est dédié au code informatique. _Coder_, c'est passer d'un _algorithme papier_ (pseudo-code ou idées) à un programme informatique, appelé **code**. Par extension, on inclura dans cette partie la modification d'un code existant. Le **but** d'un code est d'être exécuté par un ordinateur pour réaliser une tâche.

Pour permettre son exécution, le code est écrit dans un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation). Celui-ci **dépend de la tâche à réaliser** : le code est un outil il faut utiliser celui qui est le plus adapté au résultat voulu.

{% info %}
Nous utilisons ici [le python](https://www.python.org/) car notre but est ici :

- de coder des algorithmes classiques et python est très proche du pseudo-code.
- d'apprendre les bonnes pratiques de développement et python est un langage qui permet de les apprendre simplement

Enfin, python est un langage très utilisé dans le monde, que ce soit par des informaticiens ou part des personnes devant utiliser du code informatiques au quotidien (scientifiques, ingénieurs en tous genres, data scientists, etc).
{% endinfo %}

La très grande majorité des concepts que l'on verra seront transposables dans d'autres langages.

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

{% attention "**IA et code**" %}

Les agents IA sont de formidables accélérateurs en développement, **mais** :

- ils n'inventent rien de neuf : ils ne peuvent répondre qu'à des problèmes déjà résolus,
- ils peuvent (vont parfois) halluciner et donner des solutions qui semblent corrects mais sont fausses en réalité

En temps que développeur **vous avez l'obligation** :

- de préparer le terrain aux agent étant le plus explicite possible dans vos demandes
- de toujours vérifier le code produit
- de connaître le fonctionnement de votre projet et pouvoir modifier le code si nécessaire


Pour cela : 

- vous devez **appendre** le cours 
- **faire vous même** les exercices et les TDs pour assimiler les concepts
- utiliser l'IA dans les projets plus long en vérifiant chaque étape produite

{% endattention %}

## Partie I : Concepts

Les différents concepts de la programmation avec des objets. On apprendra tout ça avec python, mais cela vous aidera dans tous les langages, en particulier ceux à objets.

{% aller %}
[Concepts de programmation et application en python](./concepts){.interne}
{% endaller %}
 
Avant de passer à la partie II, vérifiez bien que vous avez acquis les concepts en faisant [les exercices finaux de la partie I](./concepts/#exercices-fin){.language-}. 

{% attention %}
Ne passez pas à la partie suivante sans avoir fait **et compris** [les 84 mono-lignes en python](./concepts/mono-lignes/){.interne}, on est parfois surpris de voir qu'on ne maîtrise finalement pas ce que l'on croyait savoir...
{% endattention %}

## Partie II : Développement d'un projet

La première partie nous a appris les concepts fondamentaux d'un langage de programmation à objet et nous a permis d'écrire et d'exécuter un (petit) programme python. Cette partie nous permettra de passer à l'échelle en créant des programmes sur plusieurs fichiers.

{% aller %}
[Coder des projets en python](./coder-projets){.interne}
{% endaller %}

## Partie III : Programmation objet et évènementielle

La programmation objet est un principe de programmation utilisé par la quasi-totalité des langages de programmation. Nes nuances existent bien sur, la programmation objet en rust n'est pas la même qu'en java par exemple, mais quelques principes fondateurs sont utilisés partout.

Nous allons dans cette partie du cours nous atteler à montrer ces principes et leur utilité dans le cadre du langage python.

{% aller %}
[Programmation objet](programmation-objet){.interne}
{% endaller %}

La programmation évènementielle est un principe de développement très utilisé dans le développement de [GUI](https://fr.wikipedia.org/wiki/Interface_graphique). Le principe est de coder des _réactions_ qui seront exécutées lorsqu'un utilisateur effectuera une action spécifique (générant un _évènement_) comme cliquer sur quelque chose, appuyer sur une touche, etc.

{% aller %}
[Programmation évènementielle](programmation-évènementielle){.interne}
{% endaller %}


## Partie IV : Partager ses projets

> TBD environnement virtuel + github sous la forme d'un


## Partie V : Pour aller plus loin

> TBD package et anatomie d'un espace de nommage. TDD. code coverage


### <span id="gestion-dépendances"></span>Gestion des dépendances

{% aller %}
[Gestion des dépendances](gestion-dépendances){.interne}
{% endaller %}

### Couverture de code

La couverture de code est un outils essentiel lorsque l'on programme par les tests et plus généralement lorsque l'on code tout court. Cet outil permet de vérifier les lignes de codes qui sont testées (_ie._ couvertes).

{% aller %}
[Couverture de code](couverture-de-code){.interne}
{% endaller %}

### Programmation par les tests

On a pris l'habitude d'écrire des tests pour se rassurer quant à l'exactitude de nos fonctions. Mais pourquoi pas ne pas écrire les tests avant ? C'est le parti pris osé (mais très efficace) de la [programmation par les tests (_Test Driven Development_, ou _TDD_)](https://fr.wikipedia.org/wiki/Test_driven_development) que l'on vous propose d'essayer dans le projet ci-après.

{% aller %}
[Projet de programmation par les tests](projet-TDD){.interne}
{% endaller %}

### Packages

Lorsqu'un module devient important, il devient compliqué de mettre tout son code dans un seul fichier. On a alors coutume de rassembler tout le code du module dans un dossier que python appelle _package_. Ces packages pourront ensuite être réutilisés dans d'autres projets, voir être directement placés sur <https://pypi.org/> pour être utilisés par d'autres.

{% lien %}
[package en python](https://docs.python.org/fr/3/tutorial/modules.html#packages)
{% endlien %}

Comme l'import d'un module revient à exécuter un fichier et qu'importer un package revient à importer un dossier, python exécute le fichier `__init__.py`{.fichier} présent dans le dossier.

{% note %}
Un _package_ est un dossier contenant un fichier `__init__.py`{.fichier}.

- importer le dossier revient à exécuter le fichier `__init__.py`{.fichier}.

- exécuter le dossier avec l'interpréteur revient à exécuter le fichier `__main__.py`{.fichier}.

{% endnote %}

Enfin, on peut faire en sorte que nos modules/packages soient exécutables directement avec un interpréteur :

{% aller %}
[Exécuter des modules python](exécution-modules){.interne}
{% endaller %}
