---
layout: layout/post.njk
title: "Projet : utilisation de listes et de dictionnaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les listes, les dictionnaires et les ensembles permettent d'écrire bien plus facilement des algorithmes qu'avec des tableaux. S'il n'y a aucune contre-indication pour l'utilisation de listes (les complexités sont les mêmes qu'avec un tableau), il faut cependant être contient que l'utilisation de dictionnaires n'est optimale (en $\mathcal{O}(1)$) qu'en moyenne.


## <span id="exercice-fondamental"></span>Exercice fondamental

Exercice fondamental pour comprendre l'intérêt des dictionnaires et des listes.

<span id="problème-crédit"></span>

{% note "**Problème**" %}

- **Nom** : crédit
- **Entrées** :
  - un tableau de $n$ prix différents deux à deux : $p_i$ ($0 \leq i < n$)
  - un crédit : $C$
- **Question** : donner deux indices différents $i$ et $j$ tels que $p_i + p_j = C$. On suppose qu'il existe toujours une solution.

{% endnote %}

On remarque que cet exercice ressemble fort à 2-SUM, mais faisons comme si de rien n'était pour l'instant et essayons de résoudre ce problème de trois façons différentes, toutes avec des complexités différentes.

#### Deux boucles for imbriquées

Comme il faut trouver deux indices différents dans le tableau d'entiers $p$ (à $n$ éléments), deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

```pseudocode
algorithme recherche(p : [entier], C: entier) → (entier, entier):
    pour chaque (i := entier) de [0 .. p.longueur[:
        pour chaque (j := entier) de [i+1 .. p.longueur[:
            si p[i] + p[j] == C:
                rendre (i, j)
    
    rendre ∅  # ne devrait pas arriver
```

Deux boucles imbriquées et le reste en $\mathcal{O}(1)$ : la complexité totale est en $\mathcal{O}(n^2)$.

{% enddetails %}

#### Une boucle et un tri

On trie la liste (ce qui donne la complexité de la solution) puis il suffit de remarquer que :

- si $P[i] + P[j] > C$ alors $P[i'] + P[j'] > C$ pour tous $i' \leq i$ et $j' \geq j$
- si $P[i] + P[j] < C$ alors $P[i'] + P[j'] < C$ pour tous $i' \geq i$ et $j' \leq j$

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

On utilise une astuce permettant de trier le tableau tout en conservant les indices.

```pseudocode
algorithme recherche(p : [entier], C: entier) → (entier, entier):

    p2 ← tableau de (entier, entier) p.longueur élément  # astuce !
    pour chaque i de [0 .. p.longueur[:
        p2[i] ← (p[i], i)

    trie p2 par ordre lexicographique croissant  

    (i := entier) ← 0
    (j := entier) ← p2.longueur -1

    tant que (i < j) et (p2[i][0] + p2[j][0] != C):
        si p2[i][0] + p2[j][0] < C:
            i ← i + 1
        sinon :
            j ← j - 1

        si i ≥ j:
            rendre ∅  #  ne devrait pas arriver
        sinon: 
            rendre (p2[i][1], p2[j][1])
```

{% enddetails %}

#### Avec un dictionnaire

Solution en $\mathcal{O}(n)$ en moyenne et complexité maximale $\mathcal{O}(n^2)$

L'idée est de mettre les prix en clé et les indices en valeur.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Première version :

```python
algorithme recherche(p : [entier], C: entier) → (entier, entier):
    d ← nouveau Dictionnaire<entier, entier>

    pour chaque (i := entier) de [0 .. p.longueur[:
        d[p[i]] ← i

    pour chaque (u := entier) de [0 .. p.longueur[:
        p2 ← C - p[u] 
        si p2 est dans d:
            v ← d[p2]
            rendre min(u, v), max(u, v)
```

Seconde version sans tout remplir, qui évite les `min`{.language-} et `min`{.language-} et somme toute plus élégante :

```python
algorithme recherche(p : [entier], C: entier) → (entier, entier):
    d ← nouveau Dictionnaire<entier, entier>

    pour chaque (i := entier) de [0 .. p.longueur[:
        si C - p[i] est dans d:
            rendre (d[C-p[i]], i)
        d[p[i]] ← i

    rendre ∅  #  ne devrait pas arriver
```

{% enddetails %}

#### Expérimentation

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant au moins une solution.
{% endexercice %}
{% details "solution" %}

On tire des `p[i]`{.language-} au hasard dans `[1, pmax]`{.language-} sans remise puis on choisi deux indices i et j et on pose `C = p[i] + p[j]`{.language-}

{% enddetails %}

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant exactement une solution.
{% endexercice %}
{% details "solution" %}

On tire p[0] et p[1] au hasard dans [1, pmax] et on pose p[0] + p[1] = C.

On tire ensuite n-2 nombres d[i] dans [-m, m] tel que si d[i] est tiré, on ne peut plus tirer -d[i] (on met tout ca dans des ensembles).

On pose ensuite p[i+2] = C/2 + d[i] pour 0 ≤ i < n-2.

{% enddetails %}

{% faire %}
Implémentez en python les 3 algorithmes précédent pour montrer voir la rapidité croissantes avec laquelle ces problèmes sont traités
{% endfaire %}
{% details "code python des trois algorithmes" %}

```python
def recherche(p, C):
    for i in range(n):
        for  in range(i + 1, n):
            if p[i] + p[j] == C:
                return (i, j)
```

```python
def recherche(p, C):
    p2 = [(p[i], i) for i in range(len(p))]
    p2.sort

    i = 0
    j = len(p) - 1
    while p2[i][0] + p2[j][0] != C:
        if p2[i][0] + p2[j][0] < C:
            i += 1
        else:
            j -= 1

        if i > j:
            return None
        else:
          u = p2[i][1]
          v = p2[j][1]
          return min(u, v), max(u, v)
```

```python
def recherche(p, C):
    d = dict()

    for j in range(n):
        if C - p[j] in d:
            return (d[C-p[j]], j)
        d[p[j]] = j
    return None
```

{% enddetails %}

## Tri par monotonie

Utilisation des listes pour faire grossir des tableaux.

{% note2 "**Définition**" %}
Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. 
{% endnote2 %}

Par exemple si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

{% exercice %}
Donnez un algorithme qui, étant donné un tableau $T$ construit une liste de listes d'entiers $L$ tel que chaque élément de $L$ soit une monotonie de $T$ (et vice versa).
{% endexercice %}
{% info %}
À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.
{% endinfo %}
{% details "corrigé" %}

> TBD

{% enddetails %}

{% exercice %}
Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. 
{% endexercice %}
{% info %}
Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.
{% endinfo %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}


Cet algorithme est en fait une variante d'un algorithme vu en cours. 

{% exercice %}
Lequel ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

## Doublons dans deux listes

> TBD doublon dans une liste (voir exo tutorat):
> - sans rien
> - avec listes et delete (avec astuce du pop du dernier si on s'en fiche de l'ordre en dupliquant les listes)
> - avec ensemble