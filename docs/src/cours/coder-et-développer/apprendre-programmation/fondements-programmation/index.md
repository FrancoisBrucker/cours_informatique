---
layout: layout/post.njk

title: Fondements de la programmation (avec python)
authors:
  - François Brucker
  - Pierre Brucker

eleventyNavigation:
    prerequis:
        - "/cours/système/ordinateur-programmes-OS/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir dans cette partie tout ce qui est nécessaire pour exécuter et créer son propre code python. Tout ce que l'on verra ici est applicable pour tous les langages de programmation.

_Python_ est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

- il n'y a pas d'exception
- il y a très peu de vocabulaire de base
- il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur. Ceci nécessite de communiquer avec lui via des instructions qui sont structurés comme un langage. Nous allons montrer ici les fondement de tout langage de programmation.

Nous allons aborder tout ceci en 4 parties :

1. Nous verrons dans [la première partie](./#partie-1){.interne} comment exécuter du code  python
2. Dans [la seconde partie](./#partie-2){.interne} nous nous intéresserons aux objets manipulées par le languages
3. [La troisième partie](./#partie-3){.interne} quant à elle sera consacrée à la structuration du code en blocs permettant d'avoir des comportements différents selon les données manipulées
4. Enfin, [la quatrième partie](./#partie-4){.interne} vous apprendra comment créer vos propres fonctions

À l'issue de ces 4 parties, vous aurez les connaissances nécessaires pour créer à partir de rien du code qui puisse répondre à vos besoins.

## <span id="partie-1"></span>Exécuter du code python

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle **_code_** ou **_programme_**) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé **_interpréteur python_**.

{% aller %}
[Exécuter du code python](./exécuter-code/){.interne}
{% endaller %}

## <span id="partie-2"></span>Manipuler des objets

{% aller %}
[Écrire du code python](./écrire-code/){.interne}
{% endaller %}

## <span id="partie-3"></span>Structurer son code

{% aller %}
[Structure de contrôle en python](./structure-code/){.interne}
{% endaller %}


## <span id="partie-4"></span>Écrire ses fonctions
{% aller %}
[Écrire ses propres fonctions en python](./écrire-fonctions/){.interne}
{% endaller %}