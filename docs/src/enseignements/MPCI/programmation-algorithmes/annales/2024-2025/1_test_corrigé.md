---
layout: layout/post.njk

title: "sujet Test 1 : algorithmie et preuve"
authors:
  - François Brucker
---

## Barème

Une note sur 4 répartie comme suit :

- 2,5pt pour la question 1
- 1 pt pour la question 2 (1/2 pour l'algorithme, 1/2 pour la preuve)
- 1 pt pour la question 3 (1/2 pour l'algorithme, 1/2 pour la preuve)
- 1 pt pour la question 4 (1/2 pour l'algorithme, 1/2 pour la preuve)

La note sur $20$ finale est obtenue en multipliant la note sur 4 par $4$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question parfaitement (ce qui garantit le 10/20), et commencer la seconde question.
- **un bon élève** doit parvenir à réussir les 2 premières questions parfaitement. Ce qui lui permet d'avoir 3.5/5 et donc 14/20
- **un très bon élève** fait plus que les 2 premières questions parfaitement.

{% endnote %}

La ventilation des notes est :

|note/20  |≤8  | [10, 11] | [11.2, 13]  | [13.2, 14]    | [14.8, 16]  | [16.4, 20]  |
|---------|----|------------|------------|--------------|-------------|-------------|
|nombre   | 6  |  10        |  9         |  12          |  2          | 4           |
|rang min | 43 | 32         | 27         | 15           | 6           | 4           |

- moyenne : 11.85/20 (2.96/5.5)
- écart-type : 3.66/20 (0.91/5.5)
- médiane : 12.70/20 (3.18/5.5)

Je suis globalement content de vous, vous avez globalement tous travaillé pour le test. Quelques notes sont cependant préoccupantes et il faudra vraiment travailler sa production de code et comprendre comment tout ceci fonctionne ensemble.

## Erreurs fréquemment rencontrées

### Question 1

Vous baratinez trop. Allez directement à l'essentiel. Cela vous permettra d'aller plus vite et satisfera le correcteur qui n'aura pas à lire tout un tas de mots inutiles.

### Question 2

- Beaucoup de personnes ne justifient pas leur algorithme.
- attention à vos conditions d'arrêt ! Elles sont souvent fantaisistes
- vos boucles doivent mimer l'algorithme 1. Un `pour chaque i de [1, b-1]` ne fonctionne pas (je n'ai cependant pas compté cela entièrement faux)

### Question 3

Créer le prédécesseur ($a-1$) en utilisant $a-2$ (rendre `succ(a-2)`) n'est pas correct...

## Corrigé

### Question 1

#### 1.1

- initialisation : à la fin de la 1ère itération on a $i = 1$ et $j = a + 1$, l'invariant est vérifié.
- on suppose l'invariant vrai à la fin de l'itération i. A la fin de l'itération `i + 1`{.language-} on a : $a' = a$ ; $i' = i + 1$ ; $j' = j + 1$.
- comme `a + i = j`{.language-}, on a `a' + (i' - 1) = (j'-1)`{.language-} et donc `a' + i' = j'`{.language-}

#### 1.2

La variable `i`{.language-} augmente de 1 à chaque itération. Comme `b` est un entier positif il arrivera une itération (possiblement la première si $b = 0$) où `i == b` et la boucle s'arrêtera : le programme s'arrête quelque soit l'entrée, c'est un algorithme.

En utilisant l'invariant de la question 1.1 on a `a' + i' = j'`{.language-} à la sortie de l'algorithme. À ce moment là $i = b$ et donc le retour de l'algorithme, j, vaut bien $a+b$.

### Question 2

L'algorithme est presque identique à somme :

```pseudocode
algorithme produit(a: entier, b: entier) → entier
    i := 0
    j := 0
    tant que i ≠ b:
        i ← succ(i)
        j ← somme(j, a)
    rendre j
```

L'invariant que l'on va utiliser est : `a * i = j`{.language-}.

Il se démontre de façon identique à la question 1.1. en remplaçant les `+ 1`{.language-} par des `+ a`{.language-}

{% info %}
Si la démonstration du 1.1 est bien faite, la _démonstration_ précédente suffit amplement.
{% endinfo %}

### Question 3

En utilisant uniquement `succ`{.language-} comme opération arithmétique donnez un algorithme permettant de calculer le prédécesseur d'un entier positif passé en paramètre. Sa signature doit être :

```pseudocode
algorithme pred(a: entier) → entier
    si a == 0:
        rendre 0

    i := 0
    tant que succ(i) ≠ a:
        i ← succ(i)
    rendre i

```

Le programme va s'arrêter puisque a est un entier positif. De plus, si $a = 0$ on a bien `pred(a) = 0`{.language-} et sinon, la boucle s'arrête lorsque `succ(i) == a`{.language-} et on rend donc bien `pred(a) = a - 1`{.language-}.

### Question 4

#### 4.1

```pseudocode
algorithme somme_rec(a: entier, b: entier) → entier:
    si b == 0:
        rendre a
    rendre somme_rec(succ(a), pred(b))

```

La preuve se fait par une récurrence triviale sur $b$ en utilisant le fait que : $a + b = (a + 1) + (b-1)$

#### 4.2

```pseudocode
algorithme produit_rec(a: entier, b: entier) → entier:
    si b == 0:
        rendre 0
    si pred(b) == 0:
        rendre a

    rendre somme_rec(produit_rec(a, pred(b)), a)
```

La preuve se fait par une récurrence triviale sur $b$ en utilisant le fait que : $ab = a(b-1) + a$. Attention au cas $b=0$ qui doit rendre 0 et pas a.
