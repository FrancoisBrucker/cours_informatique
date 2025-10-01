---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On note $n_1$ et $n_2$ les longueur des chaines $S_1$ et $S_2$ respectivement.

## Sous-séquence

```pseudocode
algorithme sous_sequence(S1: chaîne, S2: chaîne) → booléen:
    i1 ← 0
    i2 ← 0
    tant que i1 < S1.longueur et i2 < S2.longueur:
        si S2[i2] == S1[i1]:
            i2 ← i2 + 1
        i1 ← i1 + 1

    rendre i2 == S2.longueur
```

Comme `i1`{,language-} augmente à chaque itération, la boucle va forcément s'arrêter ce qui finira l'algorithme.

Enfin l'algorithme fonctionne car `i2`{,language-} est incrémenté à la première occurrence possible.

Sa complexité est en $\mathcal{O}(\max(n_1, n_2))$. Cet algorithme est linéaire il est optimal.

## Sous-mot

L'algorithme suivant regrade toutes les possibilités pour $S_2$ d'être un sous-mot de $S_1$. Il s'arrête à la première possibilité. Dans le pire des cas, il va effectuer $\mathcal{O}(n_1 \cdot n_2)$ opérations.

```pseudocode
algorithme sous_mot(S1: chaîne, S2: chaîne) → booléen:
    
    pour chaque i1 de [0 .. S1.longueur[:
        i2 ← 0
        stop ← Faux
        tant que (stop == Faux) et (i2 < S2.longueur):
            si S2[i2] == S1[i1 + i2]:
                i2 ← i2 + 1
            sinon:
                stop ← Vrai
        
        si i2 == S2.longueur:
            rendre Vrai

    rendre Faux
```

Si tous les caractères de $S_2$ sont différents, il n'est pas nécessaire de tout recommencer. On peut utiliser l'optimisation suivante, qui donne la complexité voulue :

```pseudocode
algorithme sous_mot(S1: chaîne, S2: chaîne) → booléen:
    i1 ← 0
    tant que i1 < S1.longueur:
        i2 ← 0        
        stop ← Faux
        tant que (stop == Faux) et (i2 < S2.longueur):
            si S2[i2] == S1[i1 + i2]:
                i2 ← i2 + 1
            sinon:
                stop ← Vrai
        
        si i2 == S2.longueur:
            rendre Vrai
        i1 ← i1 + i2

    rendre Faux
```

## Permutation circulaire

La solution est optimale puisqu'elle est en $\mathcal{O}(n)$

```pseudocode
algorithme permutation(S: [caractère], k: entier) → [caractère]:
    S2 ← un tableau de n caractères

    pour chaque i de [0 .. k [:
        S2[i] ← S[S.longueur-k + i]
    pour chaque i de [k .. S.longueur[:
        S2[i] ← S[i-k]
    
    rendre S2
```

L'algorithme ci-dessus rend un tableau, il est donc facile de faire le décalage.

Si on droit qu'à un nombre constant de variables ceci n'est plus possible. Il faut ruser en utilisant des retournements

```pseudocode
algorithme retournement(S: [caractère]) → ∅:
    pour chaque i de [0 .. S.longueur // 2[:
    S[i], S[S.longueur - 1 - i] ← S[S.longueur - 1 - i], S[i]

```

Comme $(A^R)^R =  A$ et $(AB)^R = B^RA^R$, on a :

<div>
$$
(A^RB^R)^R = ((B^R)^R)((A^R)^R) = BA
$$
</div>

L'algorithme de permutation est alors tout simple :

<span id="algorithme-permutation"></span>

```pseudocode
algorithme permutation(S: [caractère], k: entier) → ∅:
    retournement(S[:-k])
    retournement(S[k:])
    retournement(S)

```

Et sa complexité est bien $\mathcal{O}(n-k) + \mathcal{O}(k) + \mathcal{O}(n) = \mathcal{O}(n)$.
