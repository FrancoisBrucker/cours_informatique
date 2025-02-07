---
layout: layout/post.njk

title: Problème du tri

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Étude du problème du tri et implémentation de quelques algorithmes pour _voir_ les différentes façon de trier et leurs complexités.

Les informaticiens adorent [les algorithmes de tris](https://fr.wikipedia.org/wiki/Algorithme_de_tri). Pas parce qu'ils aiment l'ordre — loin de là — mais parce qu'il existe des millions de façons différentes de trier.

{% info %}
Les algorithmes de tri que nous verrons dans cette partie nous permettrons non seulement de mettre en oeuvre tout ce que nous avons vu sur les techniques de preuves et de calcul de complexités, mais également d'apprendre de nouveaux outils, comme le master theorem.
{% endinfo %}

Commençons par définir le problème :

{% note "**Problème**" %}

- **Nom** : tri
- **Entrées** : un tableau d'entiers
- **Sortie** : un tableau contenant les valeurs du tableau en entrée triées selon l'ordre croissant

{% endnote %}

## Reconnaissance

Commençons par travailler sur un problème connexe au problème du tri, celui de savoir si un tableau d'entiers est trié ou non. Le problème du tri présuppose en effet que l'on sache ce qu'est un tableau trié et, en creux, qu'on puisse vérifier (rapidement) qu'un tableau est trié ou non.

{% aller %}
[Reconnaissance d'un tableau trié](./reconnaissance){.interne}
{% endaller %}

Pouvoir vérifier qu'une solution à un problème en est vraiment une est un point crucial en algorithmie. Nous y reviendrons intensivement lorsque nous parlerons de classes de problèmes.

## <span id="tris-simples"></span>Algorithmes Tris simples

Deux Algorithmes simples pour trier un tableau.

### Tri par sélection

Le plus simple des algorithmes de tri, pour s'échauffer.

{% aller %}
[Tri par sélection](./algorithme-sélection){.interne}
{% endaller %}

### Tri par insertion

Son implémentation va nécessiter d'utiliser une nouvelle technique, le placement de sentinelles, et démontrer ses complexités va demander un peu de travail car son nombre d'instructions est très variable selon le tableau donné en paramètre.

{% aller %}
[Tri par insertion](./algorithme-insertion){.interne}
{% endaller %}

### Exercices : variantes

{% lien %}
[The Simplest Sorting Algorithm](https://www.youtube.com/watch?v=_W0yUJlscRA)
{% endlien %}
{% info %}

[La chaîne Youtube Polylog](https://www.youtube.com/@PolylogCS) est très bien ! Son niveau moyen est pour l'instant au-dessus de ce que l'on connaît ou que l'on sait faire, mais on abordera petit à petit toutes les notions qu'ils abordent et à l'issue du cours vous serez à l'aise avec son contenu.

{% endinfo %}

Vous allez voir quelques variantes surprenante de tris simple.

Commençons par un petit échauffement. Sélection est identique à l'algorithme ci-dessous :

```pseudocode/
algorithme sélection(T: [entier]) → ∅:
    pour chaque i de [0, T.longueur[:
        pour chaque j de [i + 1, T.longueur[:
            si T[j] < T[i]:
                T[i], T[j] ← T[j], T[i]
```

{% exercice %}
Pourquoi ?
{% endexercice %}
{% details "corrigé" %}
A chaque fois qu'un nombre `T[j]`{.language-} strictement plus petit que `T[i]`{.language-} est trouvé pour un $j > i$, on échange les deux valeurs. A la fin de l'itération le plus petit élément de `T[i:]`{.language-} est placé en position `T[i]`{.language-}.

L'invariant de la boucle 2-5 est donc identique à celui de l'algorithme par sélection que nous avons prouvé pour le précédent algorithme.
{% enddetails %}

Et maintenant un peu de magie :

```pseudocode/
algorithme sélection_opposé(T: [entier]) → ∅:
    pour chaque i de [0, T.longueur[:
        pour chaque j de [0, T.longueur[:
            si T[j] < T[i]:
                T[i], T[j] ← T[j], T[i]
```

Il ressemble à un croisement improbable entre tri par sélection et tri par insertion.

{% exercice %}
Exécutez l'algorithme sur le tableau [1, 3, 2, 6, 4, 5]
{% endexercice %}
{% details "corrigé" %}

On note le tableau chaque fin de boucle 2-5 :

1. [1, 3, 2, 6, 4, 5]
2. [3, 1, 2, 6, 4, 5]
3. [3, 2, 1, 6, 4, 5]
4. [6, 3, 2, 1, 4, 5]
5. [6, 4, 3, 2, 1, 5]
6. [6, 5, 4, 3, 2, 1]

{% enddetails %}

Comme vous l'avez remarqué, l'algorithme suivant trie aussi, mais dans le sens opposé.

{% exercice %}
Pourquoi ?
{% endexercice %}
{% details "corrigé" %}

La première boucle 2-5 (pour i=0) fait comme le tri par sélection : elle place le plus petit élément en tête de tableau.

A partir de la seconde boucle, on peut montrer que chaque boucle va trier les i+1 premiers éléments du tableau par ordre décroissant. Il se comporte comme le tri par insertion, adaptons son invariant de boucle à cet algorithme.

Par récurrence, on suppose vrai à la fin de l'itération $i$. Au début de l'itération $i+1$, les éléments de 0 à i sont triés par ordre décroissant avec le plus petit élément du tableau à la position $i$, lorsque j va progresser, il va commencer par placer $T[i+1]$ dans sa position dans le tableau (le plus petit indice i' tel que $T[i'] < T[i+1]$), puis placer l'indice échangé à sa nouvelle place et ainsi de suite jusqu'à placer le plus petit élément du tableau en position $i+1$.

{% enddetails %}

Et terminons cette partie en montrant que cette dernière itération est bien un algorithme de tri :

```pseudocode/
algorithme sélection_opposé(T: [entier]) → ∅:
    pour chaque i de [0, T.longueur[:
        pour chaque j de [0, T.longueur[:
            si T[i] < T[j]:
                T[i], T[j] ← T[j], T[i]
```

{% exercice %}
Pourquoi ?
{% endexercice %}
{% details "corrigé" %}

C'est exactement la même preuve que précédemment en remarquant qu'à la fin de la première boucle 2-5 (pour i=0) l'algorithme place le plus grand élément en tête de tableau.

A partir de la seconde boucle, chaque boucle va trier les i+1 premiers éléments du tableau par ordre croissant.

{% enddetails %}

## Complexité du problème du tri

{% aller %}
[Complexité du problème](./complexité-problème){.interne}
{% endaller %}

## <span id="tris-optimaux"></span>Algorithmes de tris optimaux

### Tri fusion

Le tri fusion utilise une technique de création d'algorithme classique nommée _diviser pour régner_ et nous utiliserons le très utile master Theorem pour en calculer la complexité.

{% aller %}
[Algorithme du tri fusion](./algorithme-fusion){.interne}
{% endaller %}

### Tri de python

L'algorithme [timsort](https://en.wikipedia.org/wiki/Timsort) est l'algorithme utilisé par python pour trier des listes :

```python
T = [1, 3, 2, 6, 4, 5]
T.sort()

print(T)
```

Ce tri est **in place** et est un mix entre le tri fusion et le tri par insertion. C'est un tri très efficace puisque :

{% note "**Complexités du timsort**" %}
Pour un tableau de taille $n$, l'algorithme [timsort](https://en.wikipedia.org/wiki/Timsort) a :

- une complexité de $\mathcal{O}(n\ln(n))$
- une complexité min de $\mathcal{O}(n)$ pour les tableaux (_presque_) trié
- une complexité en moyenne de $\mathcal{O}(n\ln(n))$

{% endnote %}

{% info %}
Ne perdez donc pas de temps à recoder un algorithme de tri : utilisez celui de python !
{% endinfo %}

## Cas du tri rapide

Le tri rapide est, malgré sa simplicité apparente, le plus difficile à implémenter proprement et pour en calculer la complexité. Il vous apprendra à avoir une intuition de la complexité d'un algorithme.

{% aller %}
[Algorithme du tri rapide](./algorithme-rapide){.interne}
{% endaller %}

## Implémentations

Projet de développement pour voir les tris se trier.

{% aller %}
[Projet implémentation des algorithmes de tri](./projet-tris){.interne}
{% endaller %}
