---
layout: layout/post.njk 
title: "Projet : TDD"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../projet-héritage/"
---

<!-- début résumé -->

Nous allons dans cette séance suivre ici le livre [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example) de Kent Beck (Suivez son [twitter](https://twitter.com/kentbeck), ses posts sont souvent rigolos et toujours utiles).

Initialement écrit pour le java, nous allons appliquer ses enseignements au python.

<!-- end résumé -->

En suivant le déroulé du livre [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example), vous allez apprendre à écrire du code par les tests.
Vous allez y apprendre la pratique d'un bon code :

{% note "But de la programmation :" %}
Créer du code **propre** qui **fonctionne**

(*clean code that works* en version originale)
{% endnote %}

Outre la méthode, nous verrons également quelques techniques pour y arriver de façon claire et pratique, comme des règles de refactoring (issues de [Refactoring: Improving the Design of Existing Code](https://www.amazon.fr/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_2?ie=UTF8&qid=1539066441&sr=8-2) de [Martin Fowler](https://martinfowler.com) (allez voir son site, y'a moult choses chouettes sur le code, l'agile, la vie et le reste)).

Ceci devrait vous permettre de diminuer le nombre de WTFs/minute, qui est le meilleur indicateur au monde d'un bon code (issu du livre [clean code](https://www.amazon.fr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) de [Robert C. Martin](https://fr.wikipedia.org/wiki/Robert_C._Martin). Ce n'est pas un livre pour débutant mais si vous avez déjà compris le tdd, c'est un super pour finaliser votre compréhension) :

![WTFs/minute](wtfm.jpg)

{% note %}

Faites l'effort de suivre cette séance en codant **en même temps** le projet. Tout est donné mais le voir fonctionner pour de vrai est plus impressionnant que de juste le lire.

{% endnote %}

On va exécuter les tests un million de fois. Pour éviter la luxation de l'index il faut retenir les raccourcis claviers qui vont vous permettre de lancer les tests sans problème :

* dédiez un terminal pour cela. Une fois la commande tapée, il vous suffit de faire *flèche du haut* pour revenir à la commande précédente et l'exécuter
* lorsque vos tests passent, il est intéressant d'utiliser le raccourci clavier de votre éditeur pour exécuter tous les tests (sous [vscode](https://docs.microsoft.com/fr-fr/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022#bkmk_test-global-shortcuts)).

## Projet

Vous allez créer dans cette séance une application de change entre Franc suisse (CHF) et dollars US ($).

|qui     |combien| prix   | total       |
|--------|-------|--------|-------------|
| Apple  | 1000  | $200   | $200 000    |
| Nestlé | 400   | 80 CHF |  32 000 CHF |
|             **total** ||| **$248 000**|

Avec le taux de conversion : 1 CHF = $0.5

### Comment ?

En programmant par les tests bien sur !

On commence par une todo list qui regroupe tout ce que l'on pense faire pour l'instant. Cette liste va diminuer lorsque l'on avancera sur le projet et grossir lorsque notre connaissance du projet va s'affiner.

Nous n'utiliserons pas ici notre code. Mais il faudra tout faire *from scratch*. On aura donc besoin :

* d'une todo list où tous nos items à faire pour l'instant sont écrit : le *backlog*
* de fichiers de tests
* du code

On verra tout au long du cours divers patterns de test et de développement pour que tout aille pour le mieux. Notre but est ici de faire du :

{% note %}
*clean code that works*
{% endnote %}

Pour cela on va se fixer quelques règles :

* on écrit du code que si un test rate
* on élimine les duplications

Ces 2 règles impliquent un mode de fonctionnement de note production code :

{% note "**Principe du TDD**" %}

1. **rouge** :
   * écrire *rapidement* un *petit* test
   * lancer les tests et les voir planter, voir même  ne correspondre à aucun code.
2. **vert** :
   * écrire le code *minimal* qui permet de faire passer le test
   * lancer les tests et les voir tous réussir
3. **code/refactor** :
   * élimine les duplications tout en conservant la validité des tests.

La partie refactor, qui est la partie réelle où l'on code ne se fait **que sur du vert** : on est assuré de ne pas casser le code puisque les tests passent.
{% endnote %}

Cela permet de prendre du plaisir à coder :

* en écrivant du code dont est sûr qu'il ne cassera rien
* en voyant la todo list diminuer ce qui montre qu'on progresse
* comme tous les tests sont conservés on sait que l'on ne travaille pas pour rien

{% note %}
Toutes ces règles visent à diminuer la peur qui bloque tout progrès
{% endnote %}

### Code

On va développer petit à petit notre propre application de change en utilisant le TDD. La logique est :

* chaque test couvre un petit ajout d'une fonctionnalité
* la première chose à faire sera de (rapidement et salement) faire fonctionner les tests
* toute les modifications de code sont effectuées alors que les testent passent
* le refactoring est fait par petites touches

## Déroulé

{% faire  %}
Créez un dossier `projet-tdd`{.fichier} qui contiendra votre projet.
{% endfaire %}

Le déroulé du projet est séparé en trois parties :

1. [projet : TDD 1/3](projet-tdd-1) (introduction et principes de la méthode en action)
2. [projet : TDD 2/3](projet-tdd-2) (on s'entraîne)
3. [projet : TDD 3/3](projet-tdd-3) (on progresse en utilisant des design pattern)

## Bilan

Cette méthode vous aidera à mieux coder, elle élimine la peur de faire des essais et de modifier le code. En revanche, elle n'est vraiment efficace qu'une fois bien assimilée. Avant, vous allez avoir l'impression de perdre votre temps.

Faire l'effort de maîtriser la technique, les effets vous seront bénéfique tout au long de votre vie de code.
