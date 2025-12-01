---
layout: layout/post.njk

title: Principes de python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

_Python_ est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

- il n'y a pas d'exception
- il y a très peu de vocabulaire de base
- il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur.

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle **_code_** ou **_programme_**) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé **_interpréteur python_**.

## Interpréteur python

L'interpréteur python comme intermédiaire entre le code python et son exécution.

{% aller %}
[Interpréteur](interpréteur){.interne}
{% endaller %}

## Éléments de langage

On va lister les concepts fondamentaux qui permettent d'utiliser l'interpréteur python. Ces concepts sont identiques pour tous (ou quasi tous) les langages de programmation objet.

### Commentaires

Commençons par ne **pas** écrire du python. Dans une ligne de code python, tout ce qui suit un `#`{.language-} n'est pas lu.

Par exemple, le code suivant écrit dans une console ne produit pas d'erreur (il n'est même pas lu...) :

```python
>>> # coucou python !
```

Alors que le même code sans `#`{.language-} est interprété par python et comme ce n'est pas du python cela produit une erreur :

```python
>>> coucou python !
  File "<stdin>", line 1
    coucou python !
           ^
SyntaxError: invalid syntax
```

### Objets et variables

Les **_objets_** de python correspondent à tout ce qui est manipulé : le but d'un programme python est de créer et de rendre des objets. Une **_variable_** est un nom qui va représenter un objet.

{% attention %}
Une variable n'est **pas** un objet, ce n'est qu'un moyen d'y accéder.
{% endattention %}

#### Objets

Tout sur les objets courant que vous manipulerez en python.

{% aller %}
[Objets types et types d'objets](objets-types){.interne}
{% endaller %}

#### Variables

Principe de l'affectation des variables en python.

{% aller %}
[Variables](variables){.interne}
{% endaller %}

#### Opérations sur les objets

Créer de nouveaux objets avec d'autres objets.

{% aller %}
[Opérations sur les objets](opérations){.interne}
{% endaller %}

### Fonctions et méthodes

Les fonctions et méthodes permettent d'utiliser les objets de python de façon pratique et puissante.

{% aller %}
[Fonctions et méthodes](fonctions-méthodes){.interne}
{% endaller %}

## Modules

Les [modules](https://docs.python.org/fr/3/tutorial/modules.html) pythons sont des espaces de noms regroupant diverses fonctions pouvant être utilisées une fois _chargé_.

{% aller %}
[Modules](modules){.interne}
{% endaller %}

> TBD notation pointée.
> 
## Espace de nommage

<!-- 
> TBD à déplacer, après avoir vu les structures de dictionnaires et de listes. à mettre dans la partie débuggeur, bien plus tard

> TBD reprendre avec la partie variable qui commence à en parler. Le mettre après coder ses fonctions/modules.
>
> Le voir avec le débogeur : stackframe = espace de nommage.
> 
 -->

On a vu que les variables étaient des noms permettant d'acceder aux objets, qui sont les seules choses que l'on peut manipuler en python. Python stocke ces variables dans des [espaces de nommage](https://docs.python.org/fr/3.13/glossary.html#term-namespace) (_namespace_ en anglais)

{% aller %}
[Espace de nommage](espace-nommage){.interne}
{% endaller %}
