---
layout: layout/post.njk
title: "exercices : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

À chaque fois, on vous demande d'écrire un algorithme puis de le prouver.

## Arithmétique

### Entier vers décimal

{% faire %}

Écrivez (et prouvez) un algorithme de signature `base10(entier) -> [entier]`{.language-} rendant la forme décimale (un tableau de chiffres allant de 0 à 9) d'un entier. On doit avoir :

```pseudocode
base10(123) = [3, 2, 1]
```

{% endfaire %}

### Étendre

{% faire %}

Écrivez (et prouvez) un algorithme de signature `étendre([entier], n) -> [entier]`{.language-} qui ajoute n 0 en à la fin du tableau. Par exemple :

```pseudocode
étendre([3, 2, 1], 4) = [3, 2, 1, 0, 0, 0, 0]
```

{% endfaire %}

### Décimal vers entier

{% faire %}

Écrivez (et prouvez) un algorithme de signature `entier([entier]) -> entier`{.language-} rendant la valeur d'un entier écrit en forme décimale. On doit avoir :

```pseudocode
entier([3, 2, 1]) = 123
```

{% endfaire %}


### Somme

{% faire %}

Écrivez (et prouvez) un algorithme permettant de calculer la somme de 2 nombres donnés sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `somme([entier], [entier]) -> [entier]`{.language-}

{% endfaire %}

### Soustraction

{% faire %}

Écrivez un algorithme permettant de calculer la soustraction de 2 nombres donnés sous leur forme décimale (un tableau de chiffres allant de 0 à 9). Cet algorithme devra être de signature : `soustraction(n: [entier], m: [entier]) -> [entier]`{.language-} et tel que `soustraction(n, m) = base10(|entier(n)-entier(m)|)`{.language-}

{% endfaire %}


## Bon parenthésage

### Uniquement des parenthèses

{% faire %}

Écrivez un algorithme permettant de savoir si une chaîne de caractères uniquement formée  des caractères `"("` et `")"` est un bon parenthésage ou pas. Ainsi :

- `parenthèses("(())()") = Vrai`{.language-}
- `parenthèses("(())()(") = Faux`{.language-}

{% endfaire %}


### Parenthèses et lettres

{% faire %}

Même question que précédemment mais la chaîne de caractère contient des lettres de l'alphabet en plus des parenthèses ouvrante et fermantes.
{% endfaire %}


### Parenthèses, crochets et lettres

{% faire %}

Même question que précédemment mais la chaîne de caractère contient des crochets ouvrant (`"["`) et fermants (`"]"`) en plus des des lettres de l'alphabet et des parenthèses ouvrante et fermantes.
{% endfaire %}
{% info %}
Vous pourrez créer un algorithme récursif qui utilise le fait que si les chaînes `s1` et `s2` sont des parenthésages corrects alors :

- la chaîne  `s1 + s2` est un parenthésage correct.
- la chaîne  `s = "(" + s1 + ")" + s3` est un parenthésage correct.
- la chaîne  `s = "[" + s1 + "]" + s3` est un parenthésage correct.

{% endinfo %}
