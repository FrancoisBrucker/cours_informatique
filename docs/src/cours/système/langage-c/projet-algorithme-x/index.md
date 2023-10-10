---
layout: layout/post.njk

title: "Projet : Algorithme X"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but de ce projet est de résoudre un problème d'optimisation : la couverture exacte d'une matrice binaire.

Vous créerez un programme complet géré avec un `Makefile`{.fichier} et autant d'unités fonctionnelles que nécessaire.

Le projet doit contenir :

- un fichier `Makefile`{.fichier} qui doit contenir :
  - une règle par défaut `all` qui créera tous les exécutables
  - une règle par exécutable
- un dossier `src/`{.fichier} contentant les sources de votre projet
- un dossier `dist/`{.fichier} qui contiendra les fichiers exécutables de votre projet
- un fichier `readme.md`{.fichier} explicatif contenant les différentes règles du makefile permettant de générer les exécutables particuliers et la documentation pour les utiliser.

## Problème

L'algorithme X permet de résoudre optimalement un problème NP-complet nommé [problème de la couverture exacte](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_couverture_exacte). Il admet une formulation ensembliste et une formulation matricielle.

{% note "**formulation ensembliste**" %}

Soient $X$ un ensemble fini et $\mathcal{A}$ un ensemble de sous-ensembles de $X$

Une ***couverture exacte*** est un sous-ensemble $\mathcal{A}'$ de $\mathcal{A}$ tel que tout élément de $X$ se retrouve dans **exactement** un ensemble de $\mathcal{A}'$.
{% endnote %}

Notez que l'on ne suppose pas qu'il existe une solution au problème.

Informatiquement parlant, on préfère une formulation matricielle, utilisant des matrices binaires :

{% note "**définition**" %}

Une ***matrice binaire*** est une matrice à $n$ lignes et $m$ colonnes
<div>
$$
M = (m_{i,j})_{1\leq i \leq n, 1\leq j \leq m}
$$
</div>

dont les éléments sont soient 0 soit 1 : $M[i][j] = m_{i,j} \in \\{0, 1\\}$ pour toutes ligne $i$ et colonne $j$.

{% endnote %}

On peut alors définir le problème de la couverture exacte matricielle :

{% note "**formulation matricielle**" %}

Soit $M$ une matrice binaire à $n$ lignes et $m$ colonnes. Une ***couverture exacte*** de $M$ est un ensemble $I$ de lignes tel que pour toute colonne $1 \leq j \leq m$, il existe exactement un élément $i$ de $I$ tel que $m_{i, j} = 1$.
{% endnote %}

Ce problème est NP-complet, c'est à dire qu'on ne connaît pas d'autre algorithme que de tester toutes les solutions possible.

## Génération d'instances

Vous allez créez une unité fonctionnelle dont le but est de générer des instances matricielle au problème.

Vous créerez également un fichier `main_instance.c`{.fichier} (avec une règle spéciale dans la `Makefile`) permettant de créer un exécutable qui affiche le résultat de chacune de vos fonctions de créations d'instances.

Vous créerez dans cet exécutable une matrice de chaque type (assez grosse pour avoir des choses à générer mais assez petite pour tenir sur un écran). Vous utiliserez l'implémentation sous la forme d'un pointeur opaque de l'[exercice matrice](../exercices/#matrice){.interne}

### Instances quelconques

{% faire %}
En utilisant la fonction crée dans l'[exercice de probabilité](../exercices/#proba-aléatoire){.interne}, créez une fonction permettant de créer une instance du problème. Sa signature doit être :

```c
matrice_t instance_quelconque(size_t nombre_ligne, size_t nombre_colonnes, double proba)
```

La fonction doit générer une matrice binaire avec une proportion de 1 égale à `proba`{.language-}.
{% endfaire %}

La fonction ci-dessus génère une matrice binaire, mais il n'est pas sur qu'e;;e possède une couverture exacte. Pour nos tests, il sera important d'avoir des cas particuliers d'instances qui ont ou qui n'ont pas de solutions.

### Instances sans solution

Soit $M$ une matrice binaire carrée à $p=2n+1$ lignes. Si $m_{i, j} = 1$ si et seulement si :

- $j = i$
- ou $j = i + 1 \text{ mod } p$

Alors il est clair que $M$ ne peut avoir de couverture exacte. Pour *cacher* la couverture exacte, on peut permuter les lignes et les colonnes de $M$ de façon aléatoire.

{% faire %}
Créez une telle fonction. Sa signature doit être :

```c
matrice_t instance_sans_solution(size_t p)
```

{% endfaire %}

### Instances avec solution

Soient $(m_1, \dots, m_k)$ une suite de $k$ entiers strictement positifs  et $M$ une matrice binaire à $n > k$ lignes et $\sum m_j$ colonnes telle que :

- pour $1 \leq i \leq k$ :
  - $m_{i, j} = 1$ si $\sum_{l<i } m_l < j \leq \sum_{l\leq i} m_l$
  - $m_{i, j} = 0$ sinon
- pour $i > k$ : $m_{i, j} = 1$ avec une probabilité de .5

Il est clair que la matrice $M$ admet une couverture exacte en considérant ses $k$ premières lignes. Pour *cacher* la couverture exacte, on peut permuter les lignes et les colonnes de $M$ de façon aléatoire.

{% faire %}
Créer une fonction de signature :

```c
matrice_t instance_solution(k, m)
```

Qui crée une matrice carrée $M$ avec les $m_k$ pris aléatoirement entre $1$ et $m$
{% endfaire %}
{% info %}
Vous pourrez utiliser les fonctions vues dans l'[exercice aléatoire](../exercices/#nombres-aléatoire){.interne} pour vous aider. En particulier :

- la fonction [`int aleatoire_int(int min, int max)`](../exercices/#entier-aléatoire) pour générer des nombres aléatoires entre 1 et m et ainsi créer les $m_k$.
- la fonction [`int aléatoire_01(double proba)`](../exercices/#proba-aléatoire) pour générer les lignes strictement plus grandes que $k$

Les deux fonctions ci-dessus vous permettrons de créer la matrice $M$, qu'il vous suffira ensuite de mélanger.

{% endinfo %}

## Algorithme

On peut utiliser l'algorithme récursif suivant :

```
def couverture_exacte(M, lignes_restantes, colonnes_restantes, solution_courante):
    Si colonnes_restantes est vide:
        return solution_courante
  
    Soit c le plus petit indice de colonnes_restantes tel qu'il existe un élément l de lignes_restantes avec M[l][c] = 1.
    
    Si c n'existe pas:
        return NULL
    l' = -1;

    Tant qu'il existe une ligne l>l' de lignes_restantes avec M[l][c] = 1 :
        soit l le plus petit l > l' de lignes_restantes avec M[l][c] = 1
        lignes_restantes' = lignes_restantes
        colonnes_restantes' = colonnes_restantes
        solution_courante' = solution_courante + [l]
        pour chaque colonne c" de colonnes_restantes:
            Si M[l][c"] == 1:
                supprimer c" de colonnes_restantes'
                supprimer de lignes_restantes' toutes les lignes l" telles que M[l"][c"] == 1
        
        s = couverture_exacte(M, lignes_restantes', colonnes_restantes', solution_courante')
        si s est non NULL:
            return s
    return NULL

```

{% faire %}
Quels paramètre utiliser pour exécuter l'algorithme ?
{% endfaire %}
{% faire %}
Démontrez que cet algorithme retourne toujours une solution et que cette solution vaut :

- `NULL` si la matrice n'admet pas de couverture exacte
- une couverture exacte de $M$ si le retour est non `NULL`

{% endfaire %}

{% faire %}
Implémentez cet algorithme.

Vous utiliserez les [listes implémentés dans l'exercice](../exercices/#liste) pour gérer les paramètres `lignes_restantes`{.language-}, `colonnes_restantes`{.language-} et `solution_courante`{.language-}.
{% endfaire %}
{% faire %}
Créez 3 exécutables prenant chacun un paramètre :

- `solution` : qui génère une matrice aléatoire ayant une solution avec le paramètre, l'affiche, cherche une solution puis affiche le résultat de l'algorithme.
- `impossible` : qui génère une matrice aléatoire n'ayant pas de solution avec le paramètre, l'affiche, cherche une solution puis affiche le résultat de l'algorithme.
- `possible` : qui génère une matrice aléatoire carrée générique avec le paramètre, l'affiche, cherche une solution puis affiche le résultat de l'algorithme.
{% endfaire %}
{% faire %}
A partir de quelle taille, le temps mis pour résoudre le problème devient trop grand ?
{% endfaire %}
{% info %}
Vous pourrez utiliser la commande [`time`](https://linuxize.com/post/linux-time-command/) pour mesurer le temps
{% endinfo %}

## Amélioration

Notre algorithme est une variante grossière d'un algorithme de Knuth pour résoudre le problème :

{% lien %}
[Algorithme X](https://fr.wikipedia.org/wiki/Algorithme_X_de_Knuth)
{% endlien %}

### Colonne min

L'algorithme de Knuth ne prend pas la première colonne venue, il choisit celle avec le minimum de 1 restant.

{% faire %}
Codez cette variante et montrez qu'elle est plus rapide pour trouver une solution que l'algorithme originel.
{% endfaire %}

### Dancing links

{% info %}
Cette partie est optionnelle.
{% endinfo %}

Knuth utilise des listes doublement chaînées pour accélérer le processus. Comprenez comment il fait et pourquoi cette solution est à la fois efficace et élégante.
