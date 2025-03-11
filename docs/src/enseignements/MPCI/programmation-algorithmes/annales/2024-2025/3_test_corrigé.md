---
layout: layout/post.njk

title:  "corrigé Test 3 : complexité"
---

## Barème

Une note sur 7 répartie comme suit :

- 1pt pour la question 1.1
- 1pt pour la question 1.2
- 2pt pour la question 1.3
- 0.25pt pour la question 2.1
- 0.75pt pour la question 2.2
- 0.75pt pour la question 2.3
- 0.25pt pour la question 2.4
- .5pt pour la question 3.1
- .5pt pour la question 3.2

La note sur $20$ finale est obtenue en multipliant la note sur 7 par $4$.

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question correctement (ce qui garantit le 12/20)
- **un bon élève** doit parvenir à réussir à faire la première question parfaitement
- **un très bon élève** à avancé dans la question 2.

{% endnote %}

La question la plus importante était la 1.3. On pouvait s'en passer mais du coup il fallait faire presque tout le reste du test. J'ai noté un petit relâchement sur les notes. Soit vous avez moins préparé le test soit vous avez moins compris cette partie du cours. Dans les 2 cas, il faut plus réviser votre cours.

La question 1 était une application directe du problème de l'exponentiation : les questions 1.1 et 1.2 auraient du être cadeau (et c'est loin d'être le cas...). Enfin, la question 1.3 a fait peur à tout le monde alors que le fonctionnement de l'algorithme est identique à celui de l'exponentiation rapide : vous auriez du tenter de le prouver. Il n'était pas nécessaire de trouver exactement l'invariant de boucle, on pouvait s'en sortir avec une récurrence bien sentie.

La ventilation des notes est :

|note/20  |≤8  | ]8, 10[ | [10, 12[      | [12, 14]    | ]14, 16]  | = 20
|---------|----|------------|------------|-------------|-----------|---------
|nombre   | 10 |  6         |  12        |  9          |  5        | 1
|rang min | 43 | 33         | 27         | 11          |  6        | 1

- moyenne : 10.64/20
- écart-type : 3.15/20
- médiane : 10.80/20

## Erreurs fréquemment rencontrées

- algorithme = finitude ; correction pas obligé
- complexité : on passe toujours dans le /2
- attention aux bornes du 2.3

## Corrigé

### 1 un algorithme de multiplication

On suppose que les entiers sont positifs.

Cet algorithme doit vous rappeler très fortement l'algorithme de l'exponentiation rapide. Il est basé sur le même principe et tout ce qu'on a fait pour l'un (complexité et preuve) marche pour l'autre.

{% lien %}
L'algorithme est connu sous le nom de [multiplication russe, ou encore multiplication du paysan russe](https://fr.wikipedia.org/wiki/Technique_de_multiplication_dite_russe).
{% endlien %}

#### 1.1

Le programme `mul`{.language-} est un algorithme car la variable `x`{.language-} décroît strictement à chaque itération en restant positive (donc elle vaudra 0 à un moment).

#### 1.2

Á chaque étape on divise la variable `x`{.language-} par 2. L'argument est alors le même que pour la factorisation rapide : il y a au plus $\log_2(x)$ itérations de l'algorithme. Comme toutes les autres opérations sont en $\mathcal{O}(1)$, on en déduit que la complexité totale de l'algorithme est en $\mathcal{O}(\ln(x))$.

#### 1.3

Pour démontrez que `mul(x, y) = x * y`{.language-} on utilise l'invariant : `X * Y = r + x * y`{.language-} avec `X`{.language-} et `Y`{.language-} les paramètres initiaux.

C'est invariant est quasiment le même que celui de l'exponentiation indienne. On vérifie aisément qu'il fonctionne.

{% attention %}
La variable `x`{.language-} est **toujours** divisée par 2 : c'est ce qui fait la différence avec l'exponentiation indienne.
{% endattention %}

### 2 représentation binaire des nombres

#### 2.1

L'entier $n$ est pair si et seulement si $T_n[0] = 0$

#### 2.2

##### 2.2.1

Une unique boucle de $\mathcal{O}(T.\mbox{\tiny longueur})$ et le reste des lignes est en $\mathcal{O}(1)$ : l'algorithme est de complexité $\mathcal{O}(T.\mbox{\tiny longueur})$.

##### 2.2.2

Si $n = \sum_{0\leq i < T.\mbox{\tiny longueur}}2^i\cdot T[i]$, alors $2n \sum_{1\leq i \leq T.\mbox{\tiny longueur}}2^i\cdot T[i-1]$ ce qui correspond à ce que fait l'algorithme.

Le fait que $T[i-1] = 0$ permet de dire que le tableau représentant $2n$ peut avoir la même taille que $T$.

##### 2.3

```pseudocode
algorithme div2(T: [bit]):
    pour chaque i de [0, T.longueur - 1[:
        T[i] ← T[i+1]
    T[-1] ← 0
```

Le raisonnement est identique que pour  prouver `mul2(T: [bit])`{.language-} :

Si $n = \sum_{0\leq i < T.\mbox{\tiny longueur}}2^i\cdot T[i]$, alors $n/2 = \sum_{0 \leq i < T.\mbox{\tiny longueur} - 1}2^i\cdot T[i+1]$ ce qui correspond à ce que fait l'algorithme.

Le fait que $T[0] = 0$ permet d'assurer le fait que l'entier représenté par $T$ soit pair et donc divisible par 2.

#### 2.4

La taille doit être égale à $T_x.\mbox{\tiny longueur} + T_y.\mbox{\tiny longueur}$.

### 3 adaptation de l'algorithme

#### 3.1

On suppose que l'on a une méthode `add(Tx, Ty)`{.language-} qui fait l'addition `x+y`{.language-} et la réaffecte dans le tableau `Tx`{.language-}. Sa complexité est en $\mathcal{O}(Tx.\mbox{\tiny longueur})$

```pseudocode
algorithme mul(Tx: [bit], Ty: [bit]) → [bit]:
    Ty' ← un tableau de taille Tx.longueur + Ty.longueur
    R ← un tableau de taille  Tx.longueur + Ty.longueur

    Ty'[i] ← 0 si i > Ty.longueur

    pour chaque i dans [0, Tx.longueur + Ty.longueur[:
        R[i] ← 0
        si i <Ty.longueur:
            Ty'[i] ← Ty[i]
        sinon:
            Ty'[i] ← 0

    pour chaque i dans [0, Tx.longueur[:
        si Tx[i] == 1:
            add(R, T'y)
        mul2(T'y)
    
    rendre R
```

#### 3.2

La complexité est en $\mathcal{O}(Tx.\mbox{\tiny longueur} \cdot Ty.\mbox{\tiny longueur})$.

<!--

### 4 Pour aller plus loin un autre algorithme

> TBD add en log n
> TBD soustraction et division : <https://leria-info.univ-angers.fr/~jeanmichel.richer/ensl1i_base_de_l_info_1_sub_div.php>
> TBD mul plus long c;est pour ça qu'on considère plus gros.
> TBD si taille fixe ok.
>
> TBD avons nous eu raison de choisir 1 et 1 pour mul et 1

### 5 Pour aller plus loin un autre algorithme

> TBD Kolmogorov et Karatsuba.
>
> TBD pour aller plus loin et en faire un long exo
> TBD <https://en.wikipedia.org/wiki/Karatsuba_algorithm>
>
> TBD pour ne pas conclure on ne sais pas jusqu'ou on peut aller. 

-->
