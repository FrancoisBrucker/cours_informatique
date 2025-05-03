---
layout: layout/post.njk
title: "Structures de dictionnaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Outre les les listes, la seconde structure dynamique la plus utilisée en code est sans conteste les dictionnaires, aussi appelés tableaux associatifs.

Cette structure est basée sur les fonctions de hash (ou de hachage) qui assure une complexité en moyenne performante.

## Fonctions de hash

{% aller %}
[Fonctions de hachage](fonctions-hash){.interne}
{% endaller %}

## Structure associée : le tableau associatif

La fonction de hachage va permettre de rajouter une indirection au tableau de stockage des données de la structure et créer une structure de données fondamentale :

{% aller %}
[Tableaux associatifs](tableau-associatif){.interne}
{% endaller %}

Cette structure est intensivement utilisé en code, en particulier en python :

{% lien %}
[Dictionnaires python](/cours/coder-et-développer/bases-programmation/conteneurs/#ensembles-dictionnaires){.interne}
{% endlien %}

## Exercices

### Ensembles

{% exercice %}
Montrer que l'on peut définir une structure d'ensemble en utilisant les tableaux associatifs.
{% endexercice %}
{% details "corrigé" %}
On a uniquement besoin des clés.

```pseudocode
structure Ensemble:
    attributs:
        T: TableauAssociatif<booléen>

    méthodes:
        fonction add(x: [bit]) → ∅:
            T[x] ← Vrai
        
        fonction delete(x: [bit]) → ∅:  # supprime x de self = self.in(x)
            T.delete(x)

        fonction in(x: [bit]) → booléen:  # x est dans self = self.in(x)
            rendre T.in(x)

```

Si on veut avoir un type particulier d'élément dans l'ensemble on utilise la structure de [tableau associatif à deux types génériques](./tableau-associatif/#structure-deux-types-génériques) :

```pseudocode
structure Ensemble<Type>:
    attributs:
        T: TableauAssociatif<Type, booléen>

    méthodes:
        fonction add(x: Type) → ∅:
            T[x] ← Vrai
        
        fonction delete(x: Type) → ∅:  # supprime x de self = self.in(x)
            T.delete(x)

        fonction in(x: Type) → booléen:  # x est dans self = self.in(x)
            rendre T.in(x)

```

{% enddetails %}
{% exercice %}
Implémentez la méthode intersection. Elle devra être de complexité moyenne égale à la taille du plus petit ensemble.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure Ensemble<Type>:
    attributs:
        T: TableauAssociatif<Type, booléen>

    méthodes:
        fonction add(x: Type) → ∅:
            T[x] ← Vrai
        
        fonction delete(x: Type) → ∅:  # supprime x de self = self.in(x)
            T.delete(x)

        fonction in(x: Type) → booléen:  # x est dans self = self.in(x)
            rendre T.in(x)
        
        fonction intersection(e: Ensemble<Type>) → Ensemble<Type>:
          si T.taille > e.T.taille:
              a, b ← e, self
          sinon:
                a, b ← self, e
          c ← nouveau Ensemble<Type>
          pour chaque x de a:
              si x est dans b:
                  c.add(x)
          rendre c

```

{% enddetails %}

On suppose maintenant que nos données soient des entiers entre 0 et n.

{% exercice %}
Explicitez une structure de données permettant de faire mieux que la structure de l'ensemble définie précédemment pour l'ajout la suppression et l'appartenance.

Quelle complexité a-t-elle pour l'intersection ?
{% endexercice %}
{% details "corrigé" %}

Il suffit d'utiliser un tableau de $n + 1$ booléen. Les complexités d'ajout et de suppression sont de complexité (maximale) $\mathcal{O}(1)$.

La complexité de l'intersection est en revanche plus grande, $\mathcal{O}(n)$, puisqu'on ne sait pas a priori si un indice est dans la structure, il faut aller le vérifier dans le tableau.

{% enddetails %}
{% exercice %}
Quand utiliser une structure plutôt que l'autre ?
{% endexercice %}
{% details "corrigé" %}

Si $n$ est pas trop grand ou que l'on ne fait pas beaucoup d'intersection ou que l'on a pas besoin de connaître l'objet d'indice $i$ la seconde structure est plus avantageuse.

Ceci est souvent le cas en algorithmie mais pas en code.

{% enddetails %}

### <span id="exercice-fondamental"></span>Exercice fondamental

Exercice fondamental pour comprendre l'intérêt des dictionnaires.

- données :
  - une tableau de $n$ prix différents deux à deux : $p_i$ ($0 \leq i < n$)
  - un crédit : $C$
- Question : donner deux indices différents $i$ et $j$ tels que $p_i + p_j = C$. On suppose qu'il existe toujours une solution.

On va essayer de répondre à cet exercice de trois façons différentes, toutes avec des complexités différentes.

#### Deux boucles for imbriquées

Comme il faut trouver deux indices différents dans le tableau d'entiers $p$ (à $n$ éléments), deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

```pseudocode
algorithme recherche(p : [entier], C: entier) → (entier, entier):
    pour chaque i de [0, p.longueur[:
        pour chaque j de [i+1, p.longueur[:
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
    pour chaque i de [0, p.longueur[:
        p2[i] ← (p[i], i)

    trie p2 par ordre lexicographique croissant  

    i ← 0
    j ← p2.longueur -1

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
    d ← nouveau TableauAssociatif<entier, entier>

    pour chaque i de [0, p.longueur[:
        d[p[i]] ← i

    pour chaque u de [0, p.longueur[:
        p2 ← C - p[u] 
        si p2 est dans d:
            v ← d[p2]
            rendre min(u, v), max(u, v)
```

Seconde version sans tout remplir, qui évite les `min`{.language-} et `min`{.language-} et somme toute plus élégante :

```python
algorithme recherche(p : [entier], C: entier) → (entier, entier):
    d ← nouveau TableauAssociatif<entier, entier>

    pour chaque i de [0, p.longueur[:
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

On tire des p[i] au hasard dans [1, pmax] sans remise puis on choisi deux indices i et j et on pose C = p[i] + p[j]

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
