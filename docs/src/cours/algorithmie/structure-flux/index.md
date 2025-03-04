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

## Variantes

### Deques

{% lien %}
<https://en.wikipedia.org/wiki/Double-ended_queue>
{% endlien %}

### Listes chaînées

{% lien %}
[Liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

Les listes chaînées sont très utilisés en algorithmie lorsque l'on a uniquement besoin de parcourir une suite d'éléments et que l'on souhaite pouvoir supprimer un élément de cette liste en temps constant.

Pouvoir supprimer un élément en temps constant nécessite de découper la liste en éléments indépendants collés les uns aux autres.

```pseudocode
structure Element:
    attributs:
        valeur: entier
        suivant: Element
        précédent: Element
    création(_valeur: entier, _suivant: Element, _précédent: Element) → Element:
        valeur ← _valeur
        suivant ← _suivant
        précédent ← _précédent
    méthodes:
        méthode ajouter(e: Element) → vide:
            e.suivant ← suivant
            suivant ← e
            e.précédent = self
        méthode supprimer() → vide:
            suivant.précédent ← précédent
            précédent.suivant ← suivant
```

{% info %}
On a utilisé le mot clé self pour parler de l'objet appelant.
{% endinfo %}

> TBD exemple d'utilisation.

Comme on a rien sans rien en algorithmie, permettre de supprimer un élément en temps constant va contraindre le fait que l'on ne peut plus aller à un élément particulier de la liste en temps constant (comme on le fait avec un tableau). On a les complexités :

- création : $\mathcal{O}(1)$
- suppression à une position donnée : $\mathcal{O}(1)$
- ajout à une position donnée : $\mathcal{O}(1)$
- aller à une position $n$ donnée : $\mathcal{O}(n)$

> TBD def récursive pour les langages fonctionnels comme le lisp (rappelez vous la fonction de McCarty) ou encore le haskell.

## Exercices

### palindrome

> TBD exercice : file et pile pour reconnaître les palindromes

### File et pile

> TBD faire une file avec 2 piles. <https://saint-francois-xavier.fr/nsi/term/2/2/2_Piles_Files.html>