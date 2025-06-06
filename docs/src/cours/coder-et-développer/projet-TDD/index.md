---
layout: layout/post.njk 
title: "Projet : TDD"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La programmation part les tests n'est pas quelque chose d'instinctif. Elle nécessite :

1. un apprentissage (au départ on se sent nul et comme on aime pas ça on blame la méthode)
2. d'être appréhendée de façon non dogmatique (on ne test pas tout avant, on utilise juste la fonctionnalité que l'on va coder pour nous permettre de mieux la définir)

Bref, prenez la comme une voie à suivre. Une fois habitué vous ne pourrez plus vous en passer.

Nous allons suivre le livre [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example) de Kent Beck (Suivez son [twitter](https://twitter.com/kentbeck), ses posts sont souvent rigolos et toujours utiles). Initialement écrit pour le java, nous allons appliquer ses enseignements au python. Vous allez apprendre à écrire du code par les tests et pourquoi cela permet permet d'atteindre plus facilement ***le but de la programmation*** :

{% note "**Définition**" %}
Le ***But de la programmation*** est de créer du code **propre** qui **fonctionne** (*clean code that works* en version originale).
{% endnote %}

Outre la méthode, nous verrons également quelques techniques pour y arriver de façon claire et pratique, comme des règles de refactoring (issues de [Refactoring: Improving the Design of Existing Code](https://www.amazon.fr/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_2?ie=UTF8&qid=1539066441&sr=8-2) de [Martin Fowler](https://martinfowler.com) (allez voir son site, y'a moult choses chouettes sur le code, l'agile, la vie et le reste)).

Ceci devrait vous permettre de diminuer le nombre de WTFs/minute, qui est le meilleur indicateur au monde d'un bon code (issu du livre [clean code](https://www.amazon.fr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) de [Robert C. Martin](https://fr.wikipedia.org/wiki/Robert_C._Martin). Ce n'est pas un livre pour débutant mais si vous avez déjà compris le tdd, c'est un super pour finaliser votre compréhension) :

![WTFs/minute](wtfm.jpg)

{% note %}

Faites l'effort de suivre cette séance en codant **en même temps** le projet. Tout est donné mais le voir fonctionner pour de vrai est plus impressionnant que de juste le lire.

{% endnote %}

On va exécuter les tests un million de fois. Pour éviter la luxation de l'index il faut retenir les raccourcis claviers qui vont vous permettre de lancer les tests sans problème :

- dédiez un terminal pour cela. Une fois la commande tapée, il vous suffit de faire *flèche du haut* pour revenir à la commande précédente et l'exécuter
- lorsque vos tests passent, il est intéressant d'utiliser le raccourci clavier de votre éditeur pour exécuter tous les tests (sous [vscode](https://docs.microsoft.com/fr-fr/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022#bkmk_test-global-shortcuts)).

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

- d'une todo list où tous nos items à faire pour l'instant sont écrit : le *backlog*
- de fichiers de tests
- du code

On verra tout au long du cours divers patterns de test et de développement pour que tout aille pour le mieux. Notre but est ici de faire du :

{% note %}
*clean code that works*
{% endnote %}

Pour cela on va se fixer quelques règles :

- on écrit du code que si un test rate
- on élimine les duplications

Ces 2 règles impliquent un mode de fonctionnement de note production code :

{% note "**Principe du TDD**" %}

1. **rouge** :
   - écrire *rapidement* un *petit* test
   - lancer les tests et les voir planter, voir même  ne correspondre à aucun code.
2. **vert** :
   - écrire le code *minimal* qui permet de faire passer le test
   - lancer les tests et les voir tous réussir
3. **code/refactor** :
   - élimine les duplications tout en conservant la validité des tests.

La partie refactor, qui est la partie réelle où l'on code ne se fait **que sur du vert** : on est assuré de ne pas casser le code puisque les tests passent.
{% endnote %}

Cela permet de prendre du plaisir à coder :

- en écrivant du code dont est sûr qu'il ne cassera rien
- en voyant la todo list diminuer ce qui montre qu'on progresse
- comme tous les tests sont conservés on sait que l'on ne travaille pas pour rien

{% note %}
Toutes ces règles visent à diminuer la peur qui bloque tout progrès
{% endnote %}

### Code

On va développer petit à petit notre propre application de change en utilisant le TDD. La logique est :

- chaque test couvre un petit ajout d'une fonctionnalité
- la première chose à faire sera de (rapidement et salement) faire fonctionner les tests
- toute les modifications de code sont effectuées alors que les testent passent
- le refactoring est fait par petites touches

## Déroulé

{% faire  %}
Créez un dossier `projet-tdd`{.fichier} qui contiendra votre projet.
{% endfaire %}

Le déroulé du projet est séparé en trois parties :

1. [Introduction et principes de la méthode en action](projet-tdd-1){.interne}
2. [On s'entraîne](projet-tdd-2){.interne}
3. [On progresse en utilisant des design pattern](projet-tdd-3){.interne}

## Bilan

Cette méthode vous aidera à mieux coder, elle élimine la peur de faire des essais et de modifier le code. En revanche, elle n'est vraiment efficace qu'une fois bien assimilée. Avant, vous allez avoir l'impression de perdre votre temps.

Faire l'effort de maîtriser la technique, les effets vous seront bénéfique tout au long de votre vie de code.
