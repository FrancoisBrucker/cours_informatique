---
layout: layout/post.njk 
title: "Structure de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../complexité-max-min/"
---

<!-- début résumé -->

Qu'est ce qu'une structure de données et comment travailler avec.

<!-- end résumé -->

Dans un ordinateur, tout n'est qu'une suite de bits (valant 0 ou 1) et pour un processeur le seul type de données reconnue est l'entier de taille 64 bits (allant de 0 à $2^{64}-1 = 18446744073709551615$). Dès lors que l'on veut manipuler autre chose (comme des approximation de réels, des caractères, etc) il faut :

* **représenter** ce type avec des entiers de taille 64 bits, nommée [structure de données](https://fr.wikipedia.org/wiki/Structure_de_données)
* construire les différentes **façons d'interagir** avec avec ce type (en utilisant uniquement les moyens donnés par le processeur, c'est à dire la manipulation d'entiers)

{% note %}
Dans le [formalisme objet](../../code/programmation-objet) :

* la structure de données est l'ensemble des attributs
* les façons d'agir est les méthodes
{% endnote %}

La façon dont est organisé la structure est indissociable de ce que l'on peut en faire et surtout en combien de temps. Il est donc souvent utile de savoir comment sont structurés des types courant pour comprendre la complexité de ses méthodes.

## Types et structures basiques

Pour aider le développeur ou l'algorithmicien dans sa tâche, la plupart des langages mettent à disposition des types basiques et des conteneurs génériques que l'on peut utiliser à notre guise pour créer d'autres structures.

{% note %}
On considère que l'on a à notre disposition :

* [les 6 types basiques du pseudo-code](../pseudo-code#objets-basique) : vide, booléens, entiers, réels, complexes, caractères
* les conteneurs de la forme [chaînes de caractères](../structure-chaîne-de-caractères), [tableaux](../structure-tableau), [listes](../structure-liste) et [dictionnaires](../structure-dictionnaire)

{% endnote %}

## Créer ses propres structures

Une structure est composée d'une suite finie de champs composés chacun d'un type connu.

Créer une structure et les méthodes permettant de la manipuler est donc identique à la création d'objet en [programmation objet](../../code/programmation-objet) mais vu sous l'angle algorithmique. On s'intéresse ici à créer les structures les plus efficaces possibles d'un point de vue complexité.

Une structure de donnée peut être à visée très générale comme les listes ou les dictionnaires (on les considère d'ailleurs utilisable par défaut dans tout langage de programmation) ou uniquement créé pour résoudre un problème spécifique rapidement.

## Complexités

Lorsque l'on manipule une structure de donnée, il est indispensable de connaître les complexités liées à la manipulation de la structure, ceci permettant de connaître la complexité de chaque méthode.

{% note %}
Pour chaque structure de données, il faut connaître la complexité de :

* la création de la structure
* la suppression de la structure
* chaque méthode permettant de la manipuler

{% endnote %}

Pour arriver à facilement connaître les complexité ci-dessus, on procède récursivement pour chaque champ jusqu'à obtenir des champs de type/structures basiques ou dont les complexités sont connues.

## Exemples

### Fraction

> TBD exemple de la fraction creation comme 2 element ou un tableau a deux éléments, suppression, irréductible ([euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide))

### Champs de bits

> TBD creation, manipulation avec et et ou
