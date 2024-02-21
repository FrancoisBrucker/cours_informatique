---
layout: layout/post.njk

title: "Corrigé Test 2 : preuve et complexité"
authors:
  - François Brucker
---

## Barème


## Corrigé

### 1. Présence

La fonction `est_présent_rec(chaine, caractère, indice)`{.language-} est de signature : `est_présent_rec(chaine: str, caractère: str, indice: int) -> bool`{.language-}.

#### Terminaison

Elle n'a pas d'appel récursif si `indice`{.language-} est plus grand ou égal à la taille de la chaîne et si elle en a un il a la même chaine en paramètre et un indice strictement plus grand : la récursion va forcément s'arrêter. La fonction `est_présent_rec(chaine, caractère, indice)`{.language-} est donc un algorithme ce qui implique que la fonction `est_présent(chaine, caractère, indice)`{.language-} en est un également.

#### Preuve

On montre par récurrence que la fonction `est_présent_rec(chaine, caractère, indice)`{.language-} rend :

- `True`{.language-} s'il existe un indice `i`{.language-}  plus grand ou égal à indice tel que `chaine[i] == caractère`{.language-}
- `False`{.language-} sinon.

1. La propriété est trivialement vraie pour `indice > len(chaine) - 1`{.language-}
2. Si la propriété est vraie pour `indice+1`{.language-} la structure de la fonction fait qu'elle est vraie pour `indice`{.language-}

Les deux points ci-dessus montrent la propriété par récurrence.

On en déduit que la fonction `est_présent(chaine, caractère)`{.language-} rend :

- `True`{.language-} s'il existe un indice `i`{.language-} tel que `chaine[i] == caractère`{.language-}
- `False`{.language-} sinon.

#### Complexité

La complexité de la fonction `est_présent(chaine, caractère)`{.language-} est égale à la complexité de la fonction `est_présent_rec(chaine, caractère, 0)`{.language-}

On a l'équation de récurrence suivante pour la complexité de la fonction `est_présent_rec(chaine, caractère, indice)`{.language-} en notant $n$ la différence entre la longueur de chaine et indice :

$$
C(n) = \mathcal{O}(1) + C(n-1)
$$

Ce qui donne une complexité de $C(n) = \mathcal{O}(n)$, et on en déduit que la complexité de `est_présent(chaine, caractère)`{.language-} est en $\mathcal{O}(\text{len(chaine)})$.

### 2. Lettre dupliquée

```python
def possède_caractère_dupliqué(chaine):
    for i in range(len(chaine)):
        if est_présent_rec(chaine, chaine[i], i + 1):
            return True
    return False
```

Clair de part la définition de la fonctjion `est_présent_rec`{.language-}.

La complexité de la fonction `est_présent_rec`{.language-}. est en $ \mathcal{O}(n)$ où la différence entre la longueur de chaine et i. `possède_caractère_dupliqué`{.language-} est donc composée de deux boucles imbriquées dépendantes l'une de l'autre mais dont la seconde est strictement décroissante. Le cours donne alors comme complexité le produit des nombres max d'itérations fois la complexité de la boucle intérieure donc $\mathcal{O}(\text{len(chaine)}^2)$ ici.

Si les deux premiers caractères sont identique, `est_présent_rec`{.language-} ne va pas faire de récursions et dans ce cas là il faut $\mathcal{O}(1)$ opérations pour exécuter l'algorithme.

### 3. Bit dupliqué

La chaine qui commence par "0" puis ne possède que des 1 va nécessiter $\mathcal{O}(\text{len(chaine)})$ opérations. Toute chaine ne peut en avoir plus puisque sur les 3 premiers éléments ("000", "001", "010", "011", et les complémentaires), il y aura forcément une répétition.

La complexité de l'algorithme pour des chaines ne possédant qu'au plus 2 caractères différents est donc de $\mathcal{O}(\text{len(chaine)})$.
