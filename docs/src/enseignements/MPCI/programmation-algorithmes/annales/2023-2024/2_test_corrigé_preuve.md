---
layout: layout/post.njk

title: "Corrigé Test 2 : preuve et complexité"
authors:
  - François Brucker
---

## Barème

Une note sur 4 répartie comme suit :

- 2 points pour la question 1 répartit en :
  - 1/2 point pour la terminaison du programme
  - 1 point pour la preuve
  - 1/2 point pour le calcul et la justification de la complexité
- 1.5 point pour la question 2 répartit en :
  - 1/2 point pour le pseudo-code
  - 1/2 point pour la preuve
  - 1/2 point pour la complexité min
  - 1/2 point pour la complexité max
- .5 point pour la question 3 répartit en :

La note sur $20$ finale est obtenue en multipliant la note sur 4 par $5$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question et à entamer la seconde ce qui permet d'avoir plus de 10.
- **un bon élève** doit parvenir à finir les 2 premières questions sans trop de fautes.
- **un très bon élève** fait les 2 premières questions parfaitement.

{% endnote %}

La ventilation des notes est :

|note/4   | ]1, 1.5]   | [1.75, 2]  | ]2, 2.5]     | ]2.5, 3]    | ]3,4[       | 4  |
|note/20  | [6.3, 7.5] | [8.8, 10]  | [12.8, 15]   | [11.7, 12.5]| [17.5, 19]  | 20 |
|---------|------------|------------|--------------|-------------|-------------|----|
|nombre   |  5         |  16        |  6           |  9          | 4           | 4  |
|rang min | 40         | 24         | 18           | 9           | 5           | 1  |

- moyenne : 12.7/20 (2.41/4)
- écart-type : 3.78/20 (0.76/4)
- médiane : 11.25/20 (2.25/4)

Je suis globalement content de vous, vous avez globalement tous travaillé pour le test et la plupart des notes en dessous de 10 sont dues à un manque de rapidité. Vous n'avez pas fait d'erreurs manifeste dans vos réponses.

## Erreurs fréquemment rencontrées

### Un algorithme

Un algorithme etst un programme qui s'arrête. Lorsque l'on vous demande de justifier que c'est un algorithme, il suffit de dire que c'est du pseudo-code et de démontrer la terminaison de celui-ci.

### Justifications trop longues

Beaucop de personnes brodent leurs justifications car ils ne savent pas ce qu'il est important à dire. La jsutification d'un algorithme doit doit être clair et concise. Allez directement à l'essentiel vous fera gagner en rapidité et donc augmentera votre note drastiquement.

Dans le doute, rappelez vous cette règle immuable vraie dans les duels aux pisolets (voir [cette séquence mémorable, éclairante et très vraie du Bon, la Brute et le Truand](https://www.youtube.com/watch?v=sXE_tPTK1VI)) et en informatique :

> Quand on justifie un algorithme, on raconte pas sa vie.

### Attentions aux indices

Souvent, vous oubliez de vérifier que les deux indices sont différents dans l'algorithme de la question 2. Si on avait codé le tout, un simple test nous l'aurait fait découvrir, mais sur feuille il faut être très attentif à ce genre d'erreurs d'indice.

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
