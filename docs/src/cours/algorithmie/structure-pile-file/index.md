---
layout: layout/post.njk
title: "Structure de pile et file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



Lorsqu'un algorithme doit gérer un _flux_ de données (des données à traiter vont arriver tout au long de son exécution), il doit être capable de stocker les données arrivantes avant de pouvoir les traiter une à une.

{% note2 "**Définition**" %}
Une structure de données `Flux<T>`{.language-} permettant de gérer un flux de données de type `T`{.language-} (tout type fonctionne) doit avoir au moins deux méthodes :

- `(f: Flux<T>) push(donnée: T) → ∅`{language-pseudocode} : une méthode de **stockage** d'une donnée dans la structure
- `(f: Flux<T>) pop() → T`{language-pseudocode} une méthode permettant de **rendre** une donnée stockée, la donnée est également supprimée de la structure

Et deux attributs :

- `longueur: entier`{language-} permettant de connaître le nombre de données actuellement stockées dans la structure
- `capacité: entier`{language-} permettant de connaître le nombre total de données que peut stocker la structure

{% endnote2 %}

Les structures de gestion de flux de données se distinguent selon que la donnée rendue soit :

- la plus récente
- la plus ancienne
- la plus prioritaire
- ...

{% info %}
La gestion de flux de données de priorités différentes sera vu plus tard, lorsque l'on étudiera les arbres.
{% endinfo %}

## Pile

La pile est la structure de données qui rend toujours la donnée la plus **récemment** stockée :

{% aller %}
[La pile](pile){.interne}
{% endaller %}

## File

La pile est la structure de données qui rend toujours la donné la plus **anciennement** stockée :

{% aller %}
[La file](file){.interne}
{% endaller %}

## Deques

Souvent, la pile et la file sont réunies en une seule structure : [le **_deque_** (_"doubled ended queue"_)](https://en.wikipedia.org/wiki/Double-ended_queue) :

```pseudocode
structure Deque<T>:
    longueur: entier
    capacité: entier

    # ...

méthode (f: Deque<T>) enfile(donnée: T) → ∅
méthode (f: Deque<T>) défile() → T
méthode (f: Deque<T>) empile(donnée: T) → ∅
méthode (f: Deque<T>) dépile() → T
```

{% exercice %}
Montrer que l'on peut facilement créer une structure de Deck en ajoutant des méthodes `empile` et `dépile` des piles à [une structure de file](./file/#structure).
{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure Deque<T>:
    longueur: entier
    capacité: entier

    (données: [T]) ← [T]{longueur: capacité}
    début: entier ← capacité - 1
    fin: entier ← 0

méthode (d: Deque<T>) enfile(donnée: T) → ∅:
    d.données[d.fin] ← donnée
    d.fin ← (d.fin + 1) % d.capacité

    d.longueur ← d.longueur + 1

méthode (d: Deque<T>) défile() → T:
    d.longueur ← d.longueur - 1
    d.début ← (f.début + 1) % d.capacité
    rendre d.données[début]

méthode (d: Deque<T>) empile(donnée: T) → ∅:
        d.données[d.fin] ← donnée
        d.fin ← (d.fin + 1) % d.capacité
méthode (d: Deque<T>) dépile() → T:
        d.fin ← (d.fin - 1 + d.capacité) % d.capacité
        rendre d.données[fin]

```

{% enddetails %}

C'est souvent la structure de Deque qui est utilisée par défaut et remplace les structures de pile et file car elle combine les deux structures sans perte de complexité.

{% info %}
En python, c'est [la classe deque](https://docs.python.org/fr/3.13/library/collections.html#collections.deque) du module [collections](https://docs.python.org/fr/3.13/library/collections.html) qui contient une série de classes implémentant des structures de données utiles.

{% endinfo %}

## On s'entraîne

{% aller %}
[Projet pile et file](projet-pile-file){.interne}
{% endaller %}
