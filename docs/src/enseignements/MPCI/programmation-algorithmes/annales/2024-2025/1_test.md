---
layout: layout/post.njk

title:  "sujet Test 1 : algorithmie et preuve"
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

### Type de rendu

Rendu sur feuille.

### Éléments de notation

1. Écriture sous la forme d'un pseudo-code correct
2. Lorsque l'on vous demande de donner un algorithme, il faudra toujours prouver :
   - sa finitude
   - son exactitude

Ne tartinez pas des pages et des pages de démonstration. Allez directement au fait et si c'est évident, dites le.

## Sujet

Dans la suite de ce test, on supposera connu l'algorithme suivant qui rend le successeur d'un entier positif :

```pseudocode
algorithme succ(n: entier) → entier:
    rendre n + 1
```

### Question 1

On considère le programme suivant définis pour tous `a`{.language-} et `b`{.language-} entiers positifs :

```pseudocode
programme somme(a: entier, b: entier) → entier:
    i := 0
    j := a
    tant que i ≠ b:
        i ← succ(i)
        j ← succ(j)
    rendre j
```

#### 1.1

Montrez que l'expression `a + i = j`{.language-} est un invariant de boucle du programme `somme`{.language-}.

#### 1.2

Montrez que `somme`{.language-} est un algorithme et utilisez l'invariant de la question 1.1 pour prouver que `somme(a, b) = a + b`{.language-} pour tous `a`{.language-} et `b`{.language-} entiers positifs.

### Question 2

En utilisant uniquement `somme`{.language-}, donnez un algorithme itératif permettant de calculer le produit de deux entiers passés en paramètre. Sa signature doit être :

```pseudocode
produit(a: entier, b: entier) → entier
```

Et on doit avoir l'égalité `produit(a, b) = a * b`{.language-} pour tous `a`{.language-} et `b`{.language-} entiers positifs ou nuls.

### Question 3

En utilisant uniquement `succ`{.language-} comme opération arithmétique donnez un algorithme permettant de calculer le prédécesseur d'un entier positif passé en paramètre. Sa signature doit être :

```pseudocode
pred(a: entier) → entier
```

Et on doit avoir pour tout `a`{.language-} entier positif ou nul :

- `pred(a) = a - 1`{.language-} si `a > 0`{.language-}
- `pred(0) = 0`{.language-}

### Question 4

#### 4.1

En utilisant `succ`{.language-} et `pred`{.language-} comme opérations arithmétiques, donnez un algorithme récursif permettant de calculer la somme de deux entiers passés en paramètre. Sa signature doit être :

```pseudocode
somme_rec(a: entier, b: entier) → entier
```

Et on doit avoir l'égalité `somme_rec(a, b) = a + b`{.language-} pour tous `a`{.language-} et `b`{.language-} entiers positifs ou nuls.

#### 4.2

En utilisant uniquement `somme_rec`{.language-} et `pred`{.language-}, donnez un algorithme récursif permettant le produit de deux entiers passés en paramètre. Sa signature doit être :

```pseudocode
produit_rec(a: entier, b: entier) → entier
```

Et on doit avoir l'égalité `produit_rec(a, b) = a * b`{.language-} pour tous `a`{.language-} et `b`{.language-} entiers positifs ou nuls.
