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

{% note %}
Une structure de données permettant de gérer un flux de données doit avoir au moins trois méthodes :

- `push(donnée: type des données stockées) -> vide`{language-pseudocode} : une méthode de **stockage** d'une donnée dans la structure
- `pop() -> type des données stockées`{language-pseudocode} une méthode permettant de **rendre** une donnée stockée, la donnée est également supprimée de la structure
- `number() -> int`{language-pseudocode} une méthode permettant de connaître le nombre de données actuellement stockées dans la structure

{% endnote %}

Une structure générale serait alors (en ajoutant des méthodes pour savoir si la structure peut accueillir des données) :

```pseudocode
structure Flux:
    création(taille: entier) → Flux
    méthodes:
        méthode push(donnée: entier) → vide
        méthode pop() → entier
        méthode number() → entier
        méthode empty() → booléen  # Vrai si vide
        méthode full() → booléen   # Vrai si plein
```

Les structures de gestion de flux de données se distingue selon que la donnée rendue soit :

- la plus récente
- la plus ancienne
- la plus ancienne ou la plus ancienne
- ...

{% info %}
La gestion de flux de données de priorités différentes sera vu plus tard, lorsque l'on étudiera les arbres.
{% endinfo %}

## La pile

La pile est la structure de données qui rend toujours la donné la plus récente :

{% aller %}
[La pile](pile){.interne}
{% endaller %}

## La file

La pile est la structure de données qui rend toujours la donné la plus ancienne :

{% aller %}
[La file](file){.interne}
{% endaller %}

## Deques

{% lien %}
<https://en.wikipedia.org/wiki/Double-ended_queue>
{% endlien %}

> listes chaînées très utilisé en système et en algo lorsque l'on a besoin uniquement d'accéder au suivant. définition récursive : x : liste base de tous les langages fonctionnels comme le lisp (rappelez vous la fonction de McCarty) ou encore le haskell.

> TBD : deques circulaires

## Exercices

### Expression avec deux piles

Mais on peut faire encore mieux en utilisant de deux piles une opération et une nombre. Samelson et bauer

### palindrome

> TBD exercice : file et pile pour reconnaître les palindromes
