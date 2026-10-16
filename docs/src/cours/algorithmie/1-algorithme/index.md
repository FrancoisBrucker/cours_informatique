---
layout: layout/post.njk

title: "Partie I : Écrire des algorithmes"
eleventyNavigation:
  prerequis: 
    - "/cours/coder-et-développer/apprendre-programmation/concepts/"

eleventyComputed:  
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce que devrait connaître tout ingénieur en algorithmie.

## Algorithmes et programmes

### Définitions

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques)
{% endaller %}

### Pseudo code

> TBD ici `ref x type`{.language-} ceci permettra de définir plus tard var avec les pointeurs.
> TBD tout est ue référence vers un objet en mémoire

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire les algorithmes en pseudo code](./pseudo-code)
{% endaller %}

### Thèse de Church-Turing

Le pseudo-code permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant [un langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation){.externe}.

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

La réciproque n'est pas prouvée mais de nombreux indices (nous en verrons plusieurs dans la seconde partie de ce cours) tendent à penser que c'est vrai. On supposera donc vrai la proposition suivante, communément admise :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes : tout algorithme peut être écrit en pseudo-code.
{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church){.externe}.
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}

Voir [cette excellente vidéo d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws){.externe} pour une introduction en douceur à la problématique.

{% endlien %}

### Autres modèles

Le modèle du pseudo-code n'est pas la seule façon d'écrire des algorithmes. La célèbre machine de Turing que l'on verra bien plus tard en est un exemple. Mais il y en a beaucoup, beaucoup d'autres tous équivalent entre eux. Nous ne rentrerons pas dans les détails ici, nous voulons juste montrer que l'on peut très bien écrire des algorithmes en utilisant autre chose que du pseudo-code. En revanche tous les modèles que nous verrons ne peuvent pas coder plus de choses, ils permettent juste d'écrire différemment les mêmes programmes.

Les programmes écrit sous la forme de pseudo-code sont équivalents (on le verra) aux algorithmes écrits grâce à une machine de Turing. Les modèles équivalents sont alors dit **_Turing complet_** :

{% definition %}
Un système est dit [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet){.externe} si tout programme du système peut s'écrire en pseudo-code et réciproquement.
{% enddefinition %}

Avoir un modèle Turing Complet nous assure, en suivant la thèse de Church-Turing, que ce modèle peut calculer tous les algorithmes.

### Lambda calcul

Le lambda calcul est une autre forme d'écriture équivalent au pseudo-code. On doit ce modèle à Church, qui était le directeur de thèse de Turing. C'est une version bien plus _matheuse_ de l'algorithmie puisqu'elle ne s'intéresse qu'aux fonctions et ne parle jamais d'algorithme.

On peut cependant coder en lambda calcul, c'est ce qu'on appelle la programmation fonctionnelle et elle est possible avec des langages comme le [Haskell](https://www.haskell.org/){.externe} (il en existe d'autres, comme le [Ocaml](https://ocaml.org/){.externe} par exemple (n')utilisé (qu')en prépa).

{% lien %}

Pour apprendre Haskell et les langages fonctionnels :

1. <https://github.com/system-f/fp-course>{.externe}
2. <https://haskell.mooc.fi/>{.externe}
3. <https://www.youtube.com/playlist?list=PLF1Z-APd9zK7usPMx3LGMZEHrECUGodd3>{.externe}
4. [introduction au langage Haskell](https://www.youtube.com/watch?v=UhM_H3lFk_Q){.externe} et au [lambda calcul](https://www.youtube.com/watch?v=_n4LIt2WPzE){.externe}
5. [playlist](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV){.externe}
6. <https://learnyouahaskell.com/>{.externe}

{% endlien %}

Cette façon de programmer est très liée aux types et a permis quelques avancées dans la vérification automatique des types.

{% lien %}

- [Catégories et types](https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/){.externe}
- [preuve de programme et types](https://ncatlab.org/nlab/show/computational+trilogy){.externe}
{% endlien %}

### Automates cellulaires

La plupart des [automates cellulaires](https://fr.wikipedia.org/wiki/Automate_cellulaire){.externe} sont Turing-complet. C'est le cas du célèbre [jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie){.externe}, mais aussi d'automates bien plus simple :

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110){.externe}.

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

### Langages exotiques

Si la plupart des langages informatiques sont clairement Turing complet, il existe des langages bizarres, nommé [langages de programmation exotiques](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique){.externe}, qui sont aussi Turing complet. Ces langages tendent à être minimalistes et cherchent à posséder soit le nombre minimal d'instructions comme le célèbre [Brainfuck](https://www.google.com/search?q=brainfuck){.externe}, à être marrant comme le [Piet](https://www.dangermouse.net/esoteric/piet.html){.externe} dont le but est de créer des programmes sous la forme d'un tableau de [Piet Mondrian](https://fr.wikipedia.org/wiki/Piet_Mondrian){.externe} ou encore à faire des ponts entre disciplines comme le [Fractran](https://www.youtube.com/watch?v=GIPtnEIQCBM){.externe}.

### Autres trucs

Ne nombreuses applications ou jeux sont Turing-complet par inadvertence. Par exemple :

- [Legend of Zelda: Tears of the Kingdom](https://www.youtube.com/watch?v=5u6BN1p0Uo8){.externe}
- [Powerpoint](https://www.youtube.com/watch?v=uNjxe8ShM-8){.externe}
- [Les trains de Factorio](https://www.youtube.com/watch?v=NCC2Fd8qxv4){.externe}




<!-- 
### Pseudo code

> TBD ici `ref x type`{.language-} ceci permettra de définir plus tard var avec les pointeurs.
> TBD tout est ue référence vers un objet en mémoire

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire les algorithmes en pseudo code](./pseudo-code)
{% endaller %}

### Thèse de Church-Turing

Le pseudo-code permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant [un langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation){.externe}.

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

La réciproque n'est pas prouvée mais de nombreux indices (nous en verrons plusieurs dans la seconde partie de ce cours) tendent à penser que c'est vrai. On supposera donc vrai la proposition suivante, communément admise :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes : tout algorithme peut être écrit en pseudo-code.
{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church){.externe}.
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}

Voir [cette excellente vidéo d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws){.externe} pour une introduction en douceur à la problématique.

{% endlien %}

### Autres modèles

Le modèle du pseudo-code n'est pas la seule façon d'écrire des algorithmes. La célèbre machine de Turing que l'on verra en partie II en est un exemple. Mais il y en a beaucoup, beaucoup d'autres tous équivalent entre eux :

{% aller %}
[Autres modèles](./autres-modèles)
{% endaller %}

## Problème algorithmique

Un algorithme est sensé faire quelque chose : à partir de données passées en entrée (ses paramètres) il va produire une sortie. Cette sortie dépend de ses paramètres et répond à une question ou plus généralement résout un problème. Définissons ceci sous la forme de "_problème_" à résoudre _via_ un algorithme :

{% definition %}
Un **_problème_** est un texte composé de 3 parties :

- **Nom** : le nom du problème
- **Entrées** : les paramètres dont on a besoin
- **Sortie** : la solution recherchée

{% enddefinition %}

Par exemple :

<span id="problème-max-tableau"></span>

{% note "**Problème**" %}

- **Nom** : MAX
- **Entrée** : un tableau d'entiers
- **Sortie** : l'entier maximum du tableau

{% endnote %}

Comme tout problème n'admet pas forcément un algorithme pour le résoudre (par exemple [la complexité de Kolmogorov](./bases-théoriques/calculabilité/#complexité-Kolmogorov), ["quand est-ce qu'on mange ?"](https://www.youtube.com/watch?v=w1hdRjPVejA&list=OLAK5uy_ntRz4sFNPNVhiGTyVR4VsePZzmGG7OPFM&index=11){.externe} ou encore ["le sens de la vie ?"](https://www.youtube.com/watch?v=LAwDWZoETk4){.externe}), on se restreindra ici aux problèmes algorithmiques :

<span id="problème-algorithmique"></span>

{% definition %}
**_Un problème est algorithmique_** s'il existe un algorithme pour le résoudre, c'est à dire que cet algorithme :

- prend en paramètres les entrées du problème
- donne en sortie la solution recherchée.

{% enddefinition %}

Mais comment prouver qu'un algorithme répond bien au problème posé ? Il faut le prouver. 

## Preuve d'algorithme


<!-- TBD 

expliciter ce qu'est la preuve par récurrence <https://fr.wikipedia.org/wiki/Raisonnement_par_r%C3%A9currence>{.externe} : axiome ou démonstration si ensemble. Ici démonstration car tout est fini. (à démontrer)

-->

<!-- Puisqu'il n'existe [aucune méthode générale pour savoir ce que fait un algorithme](./bases-théoriques/arrêt-rice/#théorème-rice) on ne peut jamais être sur _a priori_ qu'un algorithme donné résout le problème attendu : il faut faire une démonstration spécifique pour chaque algorithme.

Par exemple l'algorithme suivant :

<span id="algorithme-pgcd"></span>

```pseudocode
algorithme pgcd(a: entier, b: entier) → entier:  # a, b ≥ 0
    a', b' := entier
    tant que min(a, b) > 0:
        a' ← max(a, b) - min(a, b)
        b' ← min(a, b)
        a, b ← a', b'
    
    rendre max(a, b)
```

On peut facilement prouver qu'il calcule bien le pgcd de deux nombres positifs car chaque boucle `tant que`{.language-} correspond exactement à une récursion de [la définition récurrente du pgcd que l'on a démontré précédemment](./bases-théoriques/calculabilité/#algorithme-euclide). Ce n'est pas la peine d'en faire des tonnes (notre remarque précédente suffit), mais il est nécessaire de justifier tout ce que l'on fait/écrit.

Si la preuve n'est pas évidente, il existe des méthodes qui fonctionnent souvent :

{% aller %}
[Prouver des algorithmes](./prouver-un-algorithme)
{% endaller %}

## <span id="entraînement-preuve"></span>On s’entraîne : création d'algorithmes itératifs et récursifs

Une série de problème algorithmique à résoudre par des algorithmes simples et clairs. Le but d'un algorithme papier est d'être compris. Faites l'effort de préférer des noms de variables explicites.

{% aller %}
[Projet : Écrire et prouver des algorithmes itératifs et récursifs](./projet-itératif-récursif)
{% endaller %}

Techniques à connaître pour la mise en oeuvre et l'utilisation d'algorithmes récursifs :

{% aller %}
[Projet : techniques de récursion](./projet-techniques-de-récursion)
{% endaller %}

On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-itératif-récursif)
{% endaller %}

## Complexité d'un algorithme

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12){.externe}
{% endlien %}

Cette partie s'intéresse à la notion de complexités pour un algorithme.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs)
{% endaller %}

Maintenant que l'on peut calculer les complexités, on peut reprendre les algorithmes itératifs et récursifs que [nous avons crées précédemment](./projet-itératif-récursif) :

{% aller %}
[Projet : calculer des complexités d'algorithmes itératifs et récursifs](./projet-calcul-complexite)
{% endaller %}

On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-calculs-compexités)
{% endaller %}

## Complexité d'un problème

Cette notion est centrale en algorithmie, nous en reparlerons encore tout au log de ce cours.

{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème)
{% endaller %}

Projets :

{% aller %}
1. [Calculer $x^n$](./projet-exponentiation)
2. [Les suites additives](./projet-suite-additive)
{% endaller %}

On s'entraîne :

{% aller %}
[Projet : calculs de complexités de problèmes algorithmiques](./projet-complexité-problème)
{% endaller %}

On vérifie qu'on sait faire avec un projet sans corrigé :

{% aller %}
[exercices : problème du doublon](./exercices-problème-doublons)
{% endaller %}

## Complexité en moyenne

{% aller %}
[Complexité en moyenne](./complexité-moyenne)
{% endaller %} -->

<!-- TBD

- ajouter un projet de de code. avec tableaux numpy, split de valeurs, enlever le ramasse=miette etc pour bien calculer en moyenne en code

- ajouter des exercices avec l'ordi avec plusieurs algos pour un même problème puis amélioration de la constantes multiplicative.

## Problème du tri

-->


<!-- TBD tri par monotonie, voir comment on peut l'améliorer en in place  et finir sur tim sort -->

<!-- {% aller %}
[Problème du tri](./problème-tris)
{% endaller %}


> TBD ici complexité amortie.

## On s'entraîne

### Complexité

Comme exercice et pour référence, calcul de sommes classiques et utiles en complexité :

<span id="sommes-classiques"></span>

{% aller %}
[Calcul de sommes classiques](./projet-sommes-classiques/)
{% endaller %}

{% aller %}
[Calcul d'équations classiques](./projet-équations-classiques/)
{% endaller %}

### Résolution d'algorithmes classiques

{% aller %}
[Algorithmes classiques](./projet-algorithmes-classiques)
{% endaller %}

### On vérifie qu'on sait faire

> TBD ajouter permutations ET MPCI 2025
 -->
