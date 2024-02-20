---
layout: layout/post.njk

title: Suppressions de valeurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

## Suppression d'une valeur

Écrire un algorithme permettant de résoudre le problème suivant :

- Données : Une liste `L`{.language-} et une valeur `val`{.language-}.
- Rendre : Une liste `L_2`{.language-}, restriction de `L`{.language-} aux valeurs différentes de `val`{.language-}.

Quel est sa complexité ?

## Suppression d'une valeur in-place

Écrire un algorithme permettant de supprimer une valeur d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, on ne se préoccupe pas de l'ordre des éléments dans la liste.
