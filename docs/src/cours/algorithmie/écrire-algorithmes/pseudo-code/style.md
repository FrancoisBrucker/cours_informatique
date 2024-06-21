---
layout: layout/post.njk
title: Comment écrire du pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le pseudo-code est une représentation d'un algorithme. Son but est de :

- démontrer que l'algorithme fait bien ce qu'on pense qu'il fait
- calculer ses performances :
  - nombre d'instructions utilisées
  - nombre de cases mémoire utilisées

## Choses indispensables

Pour réaliser cela le plus simplement possible, on voudra **toujours** :

- qu'il soit lisible,
- qu'il soit juste,
- en connaître les performances.

### Lisible

Le but d'un algorithme papier est d'être compris. On utilisera pour l'écrire une série de règles compréhensibles par tout le monde : le pseudo-code. Ce n'est ni une langue ni un langage.

préférez des noms de variables explicites et n'hésitez pas à séparer votre pseudo-code en fonctions pour qu'il soit plus clair.

{% note "**N'oubliez pas**" %}
Les fonctions doivent être décrites si elles ne sont pas immédiatement compréhensibles.
{% endnote %}

### Preuve

On **démontrera** le fonctionnement de l'algorithme en utilisant des preuves mathématiques.

### Performances

On calculera la complexité de l'algorithme :

- nombre d'instructions
- place en mémoire

Ces complexités dépendent des paramètres de l'algorithme et, parfois de circonstances extérieures comme l'état du réseau par exemple.

## Choix des noms des termes et variables utilisés ?

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

Les trois pseudo-code suivant sont ainsi équivalent :

```python
for i in range(10):
    affiche à l'écran i
```

```python
pour chaque entier i allant de 0 à 9:
    print(i)
```

```c
for (i=0 ; i < 10 ; i++) {
    printf(i);
}
```
