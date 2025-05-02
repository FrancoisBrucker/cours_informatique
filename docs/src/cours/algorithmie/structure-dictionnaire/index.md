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

## Structures associées

La fonction de hachage va permettre de rajouter une indirection au tableau de stockage des données de la structure. On va voir deux utilisations possible :

- le tableau associatif (les dictionnaires de python)
- les ensembles

### Tableau associatifs

{% aller %}
[Tableaux associatifs](tableau-associatif){.interne}
{% endaller %}

### Ensembles

> TBD ensembles

## Exercices

> TBD beaucoup utilisé en code car on gagne vraiment du temps
> TBD exo O(n) en moyenne vs O(n^2). Avec tableau associatif pour compter ou ensemble pour savoir si on l'a déjà vu.
>
### <span id="exercice-fondamental"></span>Exercice fondamental

Exercice fondamental pour comprendre l'intérêt des dictionnaires.

- données :
  - une liste de $n$ prix différents deux à deux : $p_i$ ($0 \leq i < n$)
  - un crédit : $C$
- Question : donner deux indices $i$ et $j$ tels que $p_i + p_j = C$. On suppose qu'il existe toujours une solution.

On va essayer de répondre à cet exercice de trois façons différentes, toutes avec des complexités différentes. Une fois n'est pas coutume on écrira les algorithmes en python, car les dictionnaires sont bien plus souvent utilisés en programmation qu'en algorithmie. Si vous n'avez pas de notion pratique sur les dictionnaires en python, n'hésitez pas à aller jeter un coup d'œil à :

{% lien %}
[Dictionnaires python](/cours/coder-et-développer/bases-programmation/conteneurs/#ensembles-dictionnaires){.interne}
{% endlien %}

#### Deux boucles for imbriquées

Comme il faut trouver deux indices différents dans la liste $p$ (à $n$ éléments), deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Code python :

```python
def recherche(p):
    for i in range(n):
        for  in range(i + 1, n):
            if p[i] + p[j] == C:
                return (i, j)
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

Code python :

```python
def recherche(p):

    p2 = sorted(p)

    i = 0
    j = n-1
    while p2[i] + p2[j] != C:
        if p2[i] + p2[j] < C:
            i += 1
        else:
            j -= 1

        if i > j:
            return None
    
    i2 = None
    j2 = None
    for k in range(len(p)):
        if p[k] == p2[i]:
            i2 = k
        elif p[k] == p2[j]:
            j2 = k

    return (i2, j2)
```

Notez que cette solution est aussi en $\mathcal{O}(n\cdot log(n))$ en moyenne car le tri utilisé par python est de complexité $\mathcal{O}(n\cdot log(n))$ en moyenne.

{% enddetails %}

#### Avec un dictionnaire

Solution en $\mathcal{O}(n)$ en moyenne et complexité maximale $\mathcal{O}(n^2)$

L'idée est de mettre les prix en clé et les indices en valeur.

{% exercice %}
Créer cet algorithme et calculez-en sa complexité.
{% endexercice %}
{% details "solution" %}

Code python v1 :

```python
def recherche(p):
    d = dict()

    for i in range(n):
        d[p[i]] = i

    for u in range(n):
        p2 = C - p[u] 
        if p2 in d:
            v = d[p2]
            return min(u, v), max(u, v)
```

Sans tout remplir, qui évite un `max`{.language-} et est plus idiomatique :

```python
def recherche(p):
    d = dict()

    for j in range(n):
        if C - p[j] in d:
            return (d[C-p[j]], j)
        d[p[j]] = j
    return None
```

{% enddetails %}

#### Expérimentation

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant au moins une solution.
{% endexercice %}
{% details "solution" %}

> TBD On tire des pi au hasard dans [1, pmax] sans remise (avec choice) puis on choisi i et j avec C = pi + pj

{% enddetails %}

{% exercice %}
Proposez une méthode permettant de générer une instance du problème admettant exactement une solution.
{% endexercice %}
{% details "solution" %}

> TBD On tire des di dans [-m, m] tel que si di est tiré, on ne peut plus tirer -di (on met tout ca dans des ensembles) pi = C/2 + di pour i ≤ n-2. Les deux derniers sont choisis  pour que la somme fasse C.

{% enddetails %}

{% faire %}
Implémentez en python les 3 algorithmes précédent pour montrer voir la rapidité croissantes avec laquelle ces problèmes sont traités
{% endfaire %}
