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

### Couple de parenthèses

{% faire %}

Si `s`{.language-} est une chaîne de caractères uniquement formée de parenthèses ouvrante et fermante, écrivez un algorithme de signature `couple(s: chaîne, i: entier) -> entier`{.language-} qui rend l'index de la parenthèse associée à celle d'indice `i`{.language-} ou -1 si elle n'existe pas (et `s` n'est pas un bon parenthésage). Par exemple :

- `parenthèses("(())()", 0) = 3`{.language-}
- `parenthèses("(())()(", 5) = 4`{.language-}
- `parenthèses("()))", 2) = -1`{.language-}

{% endfaire %}


### Parenthèses et lettres

{% faire %}

Écrivez un algorithme permettant de savoir si une chaîne de caractères uniquement formée  des caractères `"("` et `")"` et des lettres de l'alphabet est un bon parenthésage.

{% endfaire %}

### Parenthèses, crochets et lettres

{% faire %}

Même question que précédemment mais la chaîne de caractère contient des crochets ouvrants (`"["`) et fermants (`"]"`) en plus des lettres de l'alphabet et des parenthèses ouvrantes et fermantes.
{% endfaire %}
{% info %}
Vous pourrez créer un algorithme récursif qui utilise le fait que si les chaînes `s1` et `s2` sont des parenthésages corrects alors :

- la chaîne  `s1 + s2` est un parenthésage correct.
- la chaîne  `s = "(" + s1 + ")" + s3` est un parenthésage correct.
- la chaîne  `s = "[" + s1 + "]" + s3` est un parenthésage correct.

{% endinfo %}

## Polynômes

### Valeur

{% faire %}
écrivez une fonction `valeur`{.language-} telle que

- **paramètres d'entrée** :

  1. une liste de $n+1$ réels $[a_0, \dots, a_n]$ $n \geq 0$
  2. un réel $x$

- **sortie** :
  - $\sum_{i=0}^na_i x^i$
{% endfaire %}
{% info %}
On pourra supposer que la fonction puissance $x^n$ existe pour tout réel $x$ et tout entier positif $n$.
{% endinfo %}

### Somme

{% faire %}
Écrivez une fonction `somme`{.language-} telle que

- **paramètres d'entrée** :

  1. une liste de réels $[a_0, \dots, a_n]$
  2. une liste de réels $[b_0, \dots, b_m]$

- **sortie** :
  - $[a_0 + b_0, \dots, a_n+b_n]$ si $n = m$
  - $[a_0 + b_0, \dots, a_n+b_n, b_{n+1}, \dots, b_m]$ si $n < m$
  - $[a_0 + b_0, \dots, a_m+b_m, a_{m+1}, \dots, a_n]$ si $m < n$

{% endfaire %}

### Produit

{% faire %}
Écrivez une fonction `produit`{.language-} telle que

- **paramètres d'entrée** :
  1. une liste de réels $[a_0, \dots, a_n]$
  2. une liste de réels $[b_0, \dots, b_m]$
- **sortie** (on suppose):
  - une liste $[c_0, \dots, c_{m+n}]$ telle que $c_k = \sum_{i+j=k}a_ib_j$ pour tout $0\leq k \leq m+n$
{% endfaire %}
