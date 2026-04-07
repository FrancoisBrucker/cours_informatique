---
layout: layout/post.njk
title: "Projet pile et file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les piles et les files sont deux structures fondamentales en algorithmie utilisées dans de nombreux algorithmes pour résoudre des problèmes très variés.

## Parités

On se donne deux `Pile<entier>`{.language-} :

- `P1`{.language-} contenant des entiers positifs
- `P2`{.language-} une pile d'entier initialement vide

{% exercice %}

Écrire un algorithme pour copier dans une pile d'entiers `P2`{.language-} les nombres pairs contenus dans `P1`{.language-}.

- Le contenu de `P1`{.language-} après exécution de l’algorithme doit être identique à celui avant exécution.
- Les nombres pairs dans `P2`{.language-} doivent être dans l’ordre où ils apparaissent dans `P1`{.language-}.

{% endexercice %}
{% info %}
Vous pourrez utiliser une troisième pile.
{% endinfo %}
{% details "corrigé" %}

On utilise une troisième pile où on va placer tous les nombres impairs :

```pseudocode
algorithme parité(P1: Pile<entier>, P2: Pile<entier>) → ∅:
    (P3 := Pile<entier>) ← Pile<entier>{capacité: P1.capacité}
    x := entier

    tant que P1.longueur > 0:
        x ← P1.dépile()
        si x est pair:
            P2.empile(x)
        sinon:
            P3.empile(x)

    tant que P3.longueur > 0:
        x ← P3.dépile()
        P1.empile(x)
```

{% enddetails %}

## Palindromes

{% exercice %}
Montrer que l'on peut trouver si une chaîne de caractères est un palindrome en utilisant une pile et une file.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme palindrome(s: chaîne) → booléen:
    (P := Pile<caractère> )← Pile<caractère> {capacité: |s|}
    (F := File<caractère>) ← File<caractère> {capacité: |s|}

    pour chaque c de s:
        P.empile(c)
        F.enfile(c)

    c1 := caractère
    c2 := caractère
    tant que P.longueur > 0:
        c1 ← P.dépile()
        c2 ← F.defile()

        si c1 ≠ c2:
            rendre Faux
    rendre Vrai
```

L'algorithme est correct puisque la pile va dépiler de la fin vers le début et la file du début vers la fin.
{% enddetails %}
{% exercice %}
Donnez la complexité de votre algorithme.
{% endexercice %}
{% details "corrigé" %}
Les méthodes des piles et des files sont toutes en $\mathcal{O}(1)$ opérations, l'algorithme précédent est de complexité $\mathcal{O}(|s|)$.

{% enddetails %}

## Permutation circulaire

Soit $T$ un tableau d'entier.

{% exercice %}
En utilisant uniquement une file, donnez un algorithme de complexité $\mathcal{O}(T.\mbox{\small longueur})$ permettant de procéder à une permutation circulaire de $T$ de $k$ éléments ($T'[(i + k) \bmod T.\mbox{\small longueur}] = T[i]$ pour tout $i$) **in place** (on doit modifier $T$).
{% endexercice %}

{% details "corrigé" %}

```pseudocode
algorithme permutation(T: [entier], k: entier) → ∅:
    (F := File<entier>) ← File<entier>{capacité: T.longueur}

    pour chaque (i:= entier) de [0 .. T.longueur[:
        F.enfile(T[i])
    répéter k fois:
        x ← F.défile()
        F.enfile(x)

    pour chaque i de [0 .. T.longueur[:
        T[i] ← F.défile()

```

{% enddetails %}

## <span id="file-avec-pile"></span>Pile et file

On dispose uniquement de la structure de donnée de Pile et on souhaite implémenter la structure de File en utilisant deux piles `P1`{.language-} et `P2`{.language-},

{% exercice %}

Écrire la structure de File en utilisant uniquement 2 piles en attributs.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure File<T>:
    capacité : entier
    longueur : entier ← 0

    P1 : Pile<T> ← Pile<T>{capacité: capacité}
    P2 : Pile<T> ← Pile<T>{capacité: capacité}

méthode (f: File<T>) enfile(donnée: T) → vide:
    f.P1.empiler(donnée)
    f.longueur ← f.longueur + 1

méthode (f: File<T>) defile() → T:
    f.longueur ← f.longueur - 1
    si f.P2.longueur == 0:
        tant que f.P1.longueur > 0:
            x ← P1.dépiler()
            f.P2.empiler(x)
        rendre f.P2.dépiler()
```

{% enddetails %}
{% exercice %}

Quelle est la complexité de l'enfilage et du défilage avec cette structure ?
{% endexercice %}
{% details "corrigé" %}

L'enfilage sera toujours en $\mathcal{O}(1)$, mais le défilage peut prendre $\mathcal{O}({\small longueur})$ dans le pire des cas si la pile `P1`{.language-} est pleine et la pile `P2`{.language-} vide.

{% enddetails %}

## Parenthésage

{% info %}
[On a déjà vu ce problème](../../exercices-itératif-récursif/#parenthésage) mais sans pile la complexité n'était pas linéaire.
{% endinfo %}

Soit $C$ une expression arithmétique avec des parenthèses et des crochets. On cherche à savoir si le parenthésage est équilibré :

- `[3 + 3 * (1 + 3)]` sera Ok
- `[3 + 3 * (1 + 3])` sera pas Ok

On ne vérifiera pas que l'expression est arithmétiquement correcte, c'est à dire que pour nous, `[3 + + 3 (1 + 3)]` sera Ok.

{% exercice %}

Montrer que l'on peut utiliser une pile pour savoir si un parenthésage est équilibré entre les `()` et les `[]` avec une complexité linéaire.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme parenthèse(C: chaîne) → booléen:
    (P := Pile<caractère>) ← Pile<caractère>{capacité: |C|}
    pour chaque (c := caractère) de C:
        si c == "(" ou c == "[":
            P.empile(c)
        sinon si c == ")":
            si (P.longueur == 0) ou (P.dépile() ≠ "("):
                rendre Faux
        sinon si c == "]":
            si (P.longueur == 0) ou (P.dépile() ≠ "("):
                rendre Faux
    rendre Vrai
```

{% enddetails %}

## Calcul d'une expression avec deux piles

{% lien %}
<https://youtu.be/2vBVvQTTdXg?t=549&si=Nj_co0n80r08YD_z>
{% endlien %}


Soit $C$ une expression arithmétique avec uniquement des parenthèses, des `+` et des `*`. On suppose qu'elle est arithmétiquement correcte, comme `(3 + 3 * (1 + 3))`. 


{% exercice %}

Montrer que l'on peut utiliser deux piles (une pour les opérateurs et les parenthèses et l'autre pour les nombres) pour calculer $C$.
{% endexercice %}
{% info %}
Vous pourrez vous inspirer de ce qu'on a fait pour les expressions en notation polonaise inversée en stockant dans une pile les opérateurs et les parenthèses et dans l'autre les entiers.
{% endinfo %}
{% details "corrigé" %}

Il faut faire attention au fait que `*` a une priorité supérieure à `+` : `3 + 4 * 3 = 15`. On suppose que l'on a un type opérateur (pour + et *) et un type expression qui contient :

- des parenthèses
- des opérateurs
- des entiers


```pseudocode

algorithme évalue(expression: chaîne) → entier:
    op := opérateur ou parenthèse
    x := entier
    y := entier

    (P1 := Pile<opérateur ou parenthèse>) ← Pile<opérateurs ou parenthèse>{capacité: |expression|}
    (P2 := Pile<entier>) ← Pile<entier>{capacité: |expression|}
    pour chaque c de expression:
        si c est un entier:
            P2.empile(c)
        sinon si c est un opérateur:
            tant que (P1.longueur > 0):                # évaluation comme notation polonaise inversée
                op ← P1.dépile()
                si op a une priorité inférieure à c:
                    p1.empile(op)
                    break
                y ← P2.dépile()
                x ← P2.dépile()
                P2.empile(x `op` y)
            P1.empile(c)
        sinon si c == "(":
            P1.empile(c)
        sinon si c == ")":
            tant que (P1.longueur > 0):              # évaluation comme notation polonaise inversée
                op ← P1.dépile()
                si op == "(":
                    break
                y ← P2.dépile()
                x ← P2.dépile()
                P2.empile(x `op` y)

    tant que (P1.longueur > 0):                     # en notation polonaise inversée
        op ← P1.dépile()
        y ← P2.dépile()
        x ← P2.dépile()
        P2.empile(x `op` y)

    rendre P2.dépile()
```

{% enddetails %}

