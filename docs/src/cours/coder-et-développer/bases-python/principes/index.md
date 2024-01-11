---
layout: layout/post.njk

title: Principes de python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

*Python* est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

- il n'y a pas d'exception
- il y a très peu de vocabulaire de base
- il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur.

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle ***code*** ou ***programme***) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé ***interpréteur python***.

## Interpréteur python

L'interpréteur python comme intermédiaire entre le code python et son exécution.

{% aller %}
[Interpréteur](interpréteur){.interne}
{% endaller %}

## Commentaires

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

## Objets

Tout sur les objets courant que vous manipulerez en python.

{% aller %}
[Objets types et types d'objets](objets-types){.interne}
{% endaller %}

## Variables

Principe de l'affectation des variables en python.

{% aller %}
[Variables](variables){.interne}
{% endaller %}

## Opérations sur les objets

Créer de nouveaux objets avec d'autres objets.

{% aller %}
[Opérations sur les objets](opérations){.interne}
{% endaller %}
