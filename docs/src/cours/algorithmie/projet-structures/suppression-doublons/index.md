---
layout: layout/post.njk

title: Suppressions de doublons

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

Même structure que pour l'exercice précédent.

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression de doublon en conservant l'ordre

Utilisez la question précédente pour écrire un algorithme résolvant le problème suivant :

- Données : Une liste `L`{.language-}.
- Rendre : Une liste `L_2`{.language-} ne contenant qu'une seule occurrence de chaque valeur de `L`{.language-} et en conservant le même ordre.

Quel est sa complexité ?

### Suppression de doublon d'une liste ordonnée

Même question que précédemment, mais on considère que la liste `L`{.language-} en entrée est triée. Donnez un algorithme en $\mathcal{O}(n)$ pour résoudre ce problème, où $n$ est le nombre d'éléments de `L`{.language-}.

### Suppression de doublon d'une liste sans ordre

Si l'ordre des éléments de `L_2`{.language-} n'est pas important, proposez une meilleure solution à la deuxième question.
