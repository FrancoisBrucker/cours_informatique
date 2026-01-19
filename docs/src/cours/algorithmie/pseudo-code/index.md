---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un algorithme](../bases-théoriques/définition/#définition-règles-générales){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain.

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur. Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

<span id="règles"></span>
{% note "**Définition**" %}
Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante.
{% endnote %}

Les langages de programmation classiques comme [python](https://www.python.org/), [go](https://go.dev/) ou encore [rust](https://www.rust-lang.org/fr) se transcrivent aisément en pseudo-code et réciproquement. Ce sont deux notions équivalentes :

- on utilisera le pseudo-code pour l'étude théorique des algorithmes
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python.

## Éléments de pseudo-code

### Briques de base

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
[Briques de base](briques-de-base){.interne}
{% endaller %}

### Algorithmes en pseudo-code

Un programme et un algorithme doivent posséder des paramètres d'entrées
En pseudo-code, un algorithme est une suite d'instructions qui, a partir de paramètres d'entrée, rend une sortie. Considérons par exemple la description de  l'algorithme de recherche d'un élément dans une liste :

```text
Nom : recherche
Entrées :
    T : un tableau d'entiers
    x : un entier
Programme :
    parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai"
    Sinon rendre "Faux"
```

En pseudo-code, cela va donner ça :

<div id="problème-recherche"></div>

```pseudocode
algorithme recherche(T: [entier],
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Le programme est un bloc. La definition du bloc (jusqu'aux `:`{.language-}) est constitué :

1. du mot-clé `algorithme`{.language-} qui détermine la nature du bloc
2. suit le du nom du programme
3. puis ses paramètres d'entrées entre parenthèses. Chaque paramètre est décrit par son nom suivit de son type
4. enfin, le type de sortie de l'algorithme qu'on fait précéder d'une flèche.

Si on a besoin d'information supplémentaire pour qu'un lecteur puisse mieux comprendre le pseudo-code on peut ajouter des commentaires en les faisant commencer par un `#`{.languages-}.  Ne mettez pas trop de commentaires, normalement le pseudo-code et le nom des variables doit suffire. On a ici juste décrit ce que fait l'algorithme avec ses paramètres d'entrées.

{% lien %}
La description des types de paramètres est reprise du format python : <https://docs.python.org/fr/3.13/library/typing.html>
{% endlien %}

Terminons par un petit exercice :

<span id="algorithme-nombre-occurrences"></span>

{% exercice %}
Adaptez le pseudo code de l'algorithme `recherche(T: [entier], x: entier) → booléen){.language-} précédent pour créer l'algorithme :

```pseudocode
nombre(T: [entier], x: entier) → entier
```

Cet algorithme  rend le nombre de fois où `x`{.language-} est présent dans `T`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme nombre(T: [entier], x: entier) → entier:
    nb ← 0
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

{% enddetails %}

### Fonctions

Un algorithme est constitué uniquement d'instructions de base. Mais rien n'empêche de réutiliser des algorithmes déjà écrit en les appelant par leur nom. Ces algorithmes intermédiaires sont appelées **_fonctions_**.

{% aller %}
[Fonctions](fonctions){.interne}
{% endaller %}

## Écrire du bon pseudo-code

Un bon pseudo-code doit être compréhensible en tant que tel, sans commentaires.

Pour cela il faut :

- expliciter la signature de vos algorithme
- utiliser des noms de variables ou de fonctions explicites et utile à la compréhension
- séparer les différentes parties d'un algorithmes en fonctions au nom explicite.

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

## Opérateurs utilisés en pseudo-code

Plusieurs opérateurs ressemblant à l'égalité sont utilisés en pseudo-code, attention à bien comprendre leurs différences.

- `x := y`{.language-} : on remplace x par y à chaque fois qu'on le voit
- `x ← y`{.language-} : on affecte x à la valeur de y
- `x = y`{.language-} : avec les définitions de x et y les 2 variables sont toujours égales (c'est une conséquence)
- `x == y`{.language-} : vrai si la valeur de x vaut la valeur de y et faux sinon

## _"Abus"_ de notation

On se permettra, lorsque l'instruction est assez claire de procéder à des raccourci pour rendre le pseudocode plus digeste. Attention, la plupart de ces opérations ne seront pas des opérations élémentaires !

{% aller %}
[Abus de notation](abus){.interne}
{% endaller %}

### Définitions de variables

Le but d'un pseudo-code est d'être explicite, c'est pourquoi :

- les variables doivent être définies avant d'être utilisée
- une variable ne peut contenir que des objets d'un type donné

Mais cela ne doit pas rendre le code lourd. On se permettra donc, **lorsqu'il n'y a pas d’ambiguïté possible**, l'abus de notations qui crée et affecte une variable en une seule fois :

- comme : `(a := entier) ← 3`{.language-}
- voir : `a := 3`{.language-} lorsque le type de la variable est clair (ici un entier)
- ou encore, mais uniquement si cela rend le code plus clair : `a ← 3`{.language-}.

Vous verrez aussi parfois cet opérateur remplacé par le mot "soit", en particulier lorsqu'il y a plusieurs variables à créer :

{% algorithme %}
#pseudocode-list(line-numbering: none)[
  + *soient* $a$, $b$ et $c$ trois *entiers*
]
{% endalgorithme %}

### Répétitions

```pseudocode
répéter k fois:
    ...
```

Pour :

```pseudocode
pour chaque i de [1 .. k]:
    ...
```

#### Répétitions par borne

Tout un tas de variations sont possibles, du moment que ce soit compréhensible. Par exemple :

```pseudocode
pour i de a à b:
    ...
```

Ou encore :

```pseudocode
pour i=a à i=b:
    ...
```

Pour :

```pseudocode
pour chaque i de [a .. b]:
    ...
```

#### Répétitions à pas fixé

```pseudocode
pour i de a à b par par pas de k:
    ...
```

ou encore :

```pseudocode
pour chaque i de [a .. b] par pas de k:
    ...
```

pour :

```pseudocode
i ← a
tant que i ≤ b:
  ...

  i ← i + k
```

### Affectation d'une tranche de tableau

```pseudocode
T[a:b] ← k
```

pour :

```pseudocode
pour chaque i de [a .. b[:
    T[i] ← k
```

Fonctionne aussi pour :

```pseudocode
T[:] ← k
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. T.longueur[:
    T[i] ← k
```

Ou encore à :

```pseudocode
T[a:b] ← T'[a':]
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. b-a[:
    T[a + i] ← T'[a' + i]
```

{% attention %}
Les affectations de tranches ne sont **pas** une instruction simple, mais nécessitent plusieurs instructions : ceux de la boucle sous-jacente.

Ainsi, le code suivant nécessite $1 + j - i$ instructions (1 instruction de création du nouveau tableau puis j-i affectations) :

```pseudocode
T' ← un nouveau tableau contenant T[i:j]  # j - i + 1 instructions en 1 ligne
```

{% endattention %}

### Concaténation

Avec deux tableaux :

```pseudocode
T := T1 + T2
```

pour :

```pseudocode
T ← un nouveau tableau de taille T1.longueur + T2.longueur

pour chaque i de [0 .. T1.longueur[:
    T[i] ← T1[i]
pour chaque i de [0 .. T2.longueur[:
    T[T1.longueur + i] ← T2[i]

```
