---
layout: layout/post.njk

title: "Projet : calcul de complexité"

eleventyNavigation:
  prerequis:
    - /cours/algorithmie/projet-itératif-récursif/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples d'algorithme pour le calcul de la complexité. Nous allons reprendre les algorithmes que nous avons crée précédemment dans la partie [calcul et preuve d'algorithmes](../projet-itératif-récursif){.interne} en utilisant ceux proposés dans la correction.

Nous allons aller de plus en plus vite, à mesure que nous gagnons en automatisme.

## Concaténation

```pseudocode/
algorithme concaténation(début: [entier], fin: [entier]) → [entier]
    t ← tableau de taille début.longueur + fin.longueur
    i ← -1

    pour chaque j de [0, début.longueur - 1]:
        i ← i + 1
        t[i] ← début[j]
  
    pour chaque j de [0, fin.longueur - 1]:
        i ← i + 1
        t[i] ← fin[j]

    rendre t
```

{% exercice %}
Quelle est la complexité de l'algorithme `concaténation`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

Les lignes 1, 5 et 9 définissent des blocs, les autres sont des instructions composées d'instructions basiques (affectations, sommes et lectures) toutes en $\mathcal{O}(1)$ : la complexité va être égale au nombre de fois où chaque ligne est exécutée. Calculons la en regroupant les lignes de l'algorithme en _paquets_ :

1. boucle 5-7
2. boucle 9-11
3. le reste

Les lignes du paquet 1 vont être exécutées autant de fois que la boucle va itérer, c'est à dire `début.longueur`{.language-} fois. La complexité du paquet 1 est donc : $\mathcal{O}(1) \cdot \mbox{début.longueur} = \mathcal{O}(\mbox{début.longueur})$

De la même manière, les lignes du paquet 2 vont être exécutées autant de fois que la boucle va itérer, c'est à dire `fin.longueur`{.language-} fois. La complexité du paquet 2 est donc : $\mathcal{O}(\mbox{fin.longueur})$.

Enfin, les lignes du paquet 3 vont toutes être exécutées 1 fois : la complexité totale de l'exécution de toutes les lignes du paquet 3 va être $\mathcal{O}(1)$.

La complexité totale est donc en $\mathcal{O}(\mbox{début.longueur} + \mbox{fin.longueur})$.

{% enddetails %}

## Suppression de valeurs

### Itératif

```pseudocode/
algorithme supprime(t: [entier], v: entier) → [entier]
    nombre ← 0
    pour chaque e de t:
        si e == v:
            nombre ← nombre + 1
    t2 ← tableau de taille t.longueur - nombre

    j ← 0
    pour tout i allant de 0 à t.longueur - 1:
        si t[i] ≠ v:
            t2[j] ← t[i]
            j ← j + 1
    
    rendre t2
```

{% exercice %}
Quelle est la complexité de l'algorithme `supprime`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

### Récursif

```pseudocode/
algorithme supprime_rec(t: [entier], v: entier) → [entier]
    si t.longueur == 0:
        rendre t

    t2 ← tableau de longueur t.longueur - 1
    pour i allant de 0 à t2.longueur - 1:
        t2[i] ← t[i + 1]
    
    si t[0] == v:
        rendre concaténation([], supprime_rec(t2, v))
    sinon:
        rendre concaténation([t[0]], supprime_rec(t2, v))
```

{% exercice %}
Quelle est la complexité de l'algorithme `supprime_rec`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

## Retournement d'un tableau

## Factorielle

> TBD terminale = for

## Fibonacci

{% aller %}
[Suite de Fibonacci](fibonacci){.interne}
{% endaller %}

## McCarty

## Triangle de Pascal

{% aller %}
[Triangle de Pascal](triangle-pascal){.interne}
{% endaller %}
