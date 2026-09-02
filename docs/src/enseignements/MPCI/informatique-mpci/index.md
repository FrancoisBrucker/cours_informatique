---
layout: layout/post.njk 
title: "L'informatique en licence MPCI"

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---


> TBD la matière informatique. Matière "incarnée". 
> TBD c'est neuf. C'est rien de ce que vous avez vu avant mais ca y ressemble...
Les UEes.

## Prérequis ?

> TBD pas besoin d'en avoir fait avant (en plus souvent les meilleurs c'est pas eux)
> TBD courbe de dunke-bidule.
> TBD prérequis : un cerveau en état de marche, de la motivation.
> TBD soyez pro actif, demandez au prof

## UEes d'informatique de la licence MPCI

{% info %}
Certaines fiches UEes ne sont pas encore à jour. Le descriptif à jour est alors présenté ci-après/
{% endinfo %}

### L1

Les 4 UE de L1 sont des UEes de Tronc Commun. Elles ont pour but d'enseigner le _lire-écrire-compter_ de l'informatique :

- concevoir un algorithme résolvant un problème simple,
- écrire un programme en python,
- compter le nombre d'opérations que va effectuer un algorithme avant de s'arrêter

Le langage de programmation utilisé est le python qui est un langage généraliste à la fois très algorithmique et tres facile d'utilisation. Il est le langage le plus utilisé dans le monde scientifique et académique ainsi qu'en entreprise pour gérer des projets de taille moyenne.

#### S1

##### _Données, calcul en informatique_ (18h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/UE/3SMP/SMP1U25?external=1)
{% endlien %}

On y verra comment l'informatique représente ses données à partir d'une suite de 0 et de 1 :

- entiers,
- approximation de réels,
- caractères

Et comment elle les manipule en utilisant le calcul booléen.

##### _Bases de programmation_ (36h)

{% lien %}
[Fiche UE](https://formations.univ-amu.fr/UE/3SMP/SMP1U24?external=1)
{% endlien %}

On y verra les principe de programmation communs à tous les langages informatique (variable, tests et boucles) et comment créer des programmes python (itératifs et récursifs) à partir de ces briques élémentaires.

#### S2

##### _Programmation objet_ (18h)

{% lien  %}
*fiche UE pas à jour*
{% endlien %}

Cette UE est consacrée à l'étude d'un projet informatique : de sa structure à son développement. Elle est séparé en deux partie, la première consacrée aux outils utilisés et la seconde au développement proprement dit.

Nous présenterons dans un premier temps les outils nécessaires au développement un projet informatique : un interpréteur python pour exécuter le code (installation en locale d'un interpréteur), l'intégration de fonctionnalités tierces qui dispense de tout recoder à chaque projet (utilisation du gestionnaire de modules `pip`) et un éditeur de code puissant (nous utiliserons vscode). 

Pour garantir la pérennité d'un projet informatique dans le temps il faudra mettre en oeuvre des techniques permettant non seulement de vérifier expérimentalement la véracité des fonctions codées (avec des tests ciblés,dit unitaires) mais également de permettre ses modifications sans crainte de faire régresser le code (en faisant des tests une partie intégrante du projet).

Nous montrerons ensuite un style de programmation, _la programmation objet_, qui permet segmenter le code en unités fonctionnelles (les objets) interdépendantes. Ce type de programmation structurée permet de gérer u projet dans le temps et avec de nombreux développeurs. Il est est soutenu par des outils permettant :

- une représentation synthétique (diagramme UML) des différentes interactions dans le projet,
- de garantir au client que les fonctionnalités attendues sont bien codées via l'utilisation de _user stories_.

##### _Algorithmie 1 (bases)_ (36h)

{% lien  %}
*fiche UE pas à jour*
{% endlien %}

Cette UE est consacrée à l'étude théorique des algorithmes. 

On commencera par ce poser la question de ce qu'est un algorithme, de ce qu'il peut et (surtout) ne peut pas faire. Une fois ces questions métaphysiques abordées nous présenterons le langage des algorithmes, une façon non ambiguë de les décrire : le pseudo-code.

Nous nous attellerons ensuite à la production d'algorithme (itératif et récursif) permettant de résoudre des problèmes simples (il faudra démonter que notre algorithme résout bien le problème demandé) le plus rapidement possible (en estimant la complexité d'un algorithme, c'est à dire le nombre d'opérations qu'ils effectuent avant de s'arrêter). 

Ces problématiques (écrire un algorithme résolvant le plus vite possible un problème donné) seront illustrés par deux problèmes fondamentaux (et très prisée des informaticiens) : 
- le problème de l'exponentiation de deux entiers,
- le problème du tri d'une liste finie d'entiers.

Enfin, nous étudierons comment créer des structures de données, en particuliers celles utilisées par tout développeur python : les listes et les dictionnaires. Ces structures linéaires sont non seulement utiles en pratique mais permettent aussi d'aborder des notions (un peu) plus avancée en algorithmie comme les fonctions de hachage et la notion de complexité amortie.

### L2

#### S3

##### _Bases de données et Data science_ (20h)

{% lien  %}
*fiche UE pas à jour*
{% endlien %}

Ce cours propose une initiation progressive aux bases de données relationnelles et à leur exploitation en contexte analytique. Il débute par une introduction à l’algèbre relationnelle, cadre théorique fondamental permettant de comprendre la logique des opérations sur les données. Les étudiants y découvrent les opérateurs essentiels et acquièrent les bases conceptuelles nécessaires pour formuler des requêtes de manière rigoureuse.

Cette approche formelle est mise en pratique avec l’apprentissage des requêtes SQL. Après une présentation des commandes fondamentales et des bonnes pratiques, les TD et TP permettent d’écrire et exécuter des requêtes sur des bases relationnelles simples. Un premier devoir surveillé vient renforcer l’acquisition conjointe de l’algèbre relationnelle et du SQL (requêtes).
La progression se poursuit avec quelques principes guidant la création d’une base SQL et l’étude des contraintes d’intégrité, afin de faire comprendre le rôle crucial du schéma, de la modélisation et des règles de cohérence dans la qualité des données. Les étudiants découvrent ensuite un écosystème plus large autour de la donnée : l’utilisation conjointe de SQLite3 et de pandas en Python, puis une première exposition à SQLAlchemy, afin de relier les bases de données à un environnement de programmation courant en data science, favorisant la reproductibilité (CM, TD et TP).

Enfin, le cours s’ouvre sur une initiation aux perspectives d’analyse prédictive : statistiques descriptives d’un jeu de données tabulaire issu d’une base SQL, visualisations des données, mesures de corrélation/causalité, prétraitements, puis introduction à la classification avec _scikit-learn_, via l’algorithme des $k$-plus proches voisins dont la complexité sera étudiée, et illustrée sur une base de données réelles. Le cours se conclut par un TP évalué qui relie l’ensemble des compétences : partir d’une base relationnelle réelle, définir une tâche de prédiction, organiser les données pour la réaliser (via requêtes SQL), et mener une première démarche complète d’analyse prédictive de données.

##### _Structure de données - arbres et graphes_ (30h)

#### S4

Premiers cours d'options. On s'adresse à des étudiants voulant approfondir leurs connaissances en informatique.

> TBD encore utile à tous, mais pas indispensable pour ceux ne voulant pas faire de l'informatique leur majeur/mineur.

##### _Langages, Automates, Grammaires_ (38h)
##### _Algorithmie 2 (résolution de problèmes)_ (38h)

{% lien  %}
*fiche UE pas à jour*
{% endlien %}

Cette UE se propose de donner des méthodes de résolution de problèmes connus et des techniques pour les adapter à de nouveaux problèmes. 

Pour cela on commencera par étudier la structure des problèmes solvable par un algorithme (classes P, NP, coNP, ...). De cette étude on dégagera 3 classes de problèmes fondamentaux : 
- la classe $P$ des problèmes solvables en temps polynomial,
- la classe $NP$ des problèmes dont on peut vérifier une solution potentielle en est une en en temps polynomial
- la classe des problèmes $NP$-complets représentés par le problème SAT

De cette étude on exhibera des problèmes ainsi que des algorithmes permettent de les résoudre soit de façon exacte soit de façon approchée. Ces algorithmes pourront être généralisés en méthodes que l'on pourra mobiliser pour forger des algorithmes permettant résoudre des problèmes similaires : algorithmes gloutons, diviser pour régner, programmation dynamique, ...

Enfin, on étudiera une structure très générale, le graphe, que l'on montrera capable de modéliser nombre de problèmes d'optimisation courant. Ceci nous ouvre une autre possibilité pour résoudre un problème : on commence par le modéliser sous la forme d'un problème de graphe connu, puis on utilise des algorithmes de résolution de celui-ci pour résoudre notre problème.

Le langage d'application de cette UE sera le go qui permet une gestion plus fine de la mémoire et des types que le python et est ainsi utilisé pour des projet informatiques important.

### L3

> TBD cours de spécialité.
>  
#### S5

##### _Intelligence Artificielle et Machine Learning_ (40h)
##### _Algorithmie 3 (avancé)_ (40h)

{% lien  %}
*fiche UE pas à jour*
{% endlien %}

Cette UE est consacré à l'étude d'algorithmes complexes (et jolis). Elle est composée de deux partie, la première consacrée au graphes (problèmes de coloration, de planarité et de couplage/couverture) et la seconde consacré aux algorithmes de résolution de problèmes classiques efficaces (calcul de la médiane en temps linéaire, programmation dynamique, ...)


#### S6

##### _Calculabilité et Sémantique_ (36h)
##### _Logique_ (24h)


## Projets

> TBD projet académique
> TBD PPPE site.

## Stages possibles