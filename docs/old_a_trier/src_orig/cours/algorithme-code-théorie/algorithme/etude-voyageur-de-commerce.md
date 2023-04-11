---
layout: layout/post.njk 
title:  "étude : voyageur de commerce"
category: cours
---

### résolution par programmation dynamique

Générer tous les cycles prend énormément de temps. On va de plus refaire plein de fois les mêmes erreurs (faire plein de fois Brest -> Marseille -> Rennes -> Paris par exemple alors qu'on peut localement faire bien mieux) : on va utiliser une méthode de programmation appelé **programmation dynamique** qui va nous permettre de factoriser des résultats.

> La [**programmation dynamique**](https://fr.wikipedia.org/wiki/Programmation_dynamique) est une méthode de création d'algorithme basée sur le fait qu'une solution minimale est composée de sous-solutions elles-mêmes minimales.
{.note}

L'exemple classique donné pour expliquer la programmation dynamique est : si un chemin $\mathcal{C}$ le plus court entre 2 points $A$ et $B$ passe par le point $C$, alors le chemin de $A$ vers $C$ et le chemin de $C$ vers $B$ dans $\mathcal{C}$ sont tous deux minimaux (s'il existait par exemple un chemin plus court entre $A$ et $C$ il suffirait de l'emprunter et $\mathcal{C}$ ne serait plus minimal).

Le principe de création d'algorithme utilisant la programmation dynamique est alors le suivant : on essaie de créer des solution optimales avec des solutions partielles elles-même optimales.

Ceci se concrétise souvent par une équation récurrente à vérifier. Dans le cas du voyageur de commerce à $n$ villes $(v_i)_{1\leq i \leq n}$ et avec $c$ comme fonction de coût, on peut construire un algorithme de programmation dynamique en remarquant que :

> Soit $I$ un sous ensemble de $[1 \mathrel{ {.}\,{.} } n]$ contenant $1$, et $j\notin I$.
>
> Si l'on note $C(I, j)$ le coût d'un plus court chemin allant de $v_1$ à $v_j$ en utilisant que des villes de $\{ v_i \mid i \in I \}$, on peut écrire :
>
> $$
> C(I, j) = \min_{k \in I \backslash \{ 1 \}} (C(I \backslash \{ k\}, k) + c(v_k, v_j))
> $$
>
{.note}

L'équation ci-dessous nous donne un moyen de construire itérativement des chemins minimaux jusqu'à arriver au calcul final :

$$
\min_{k \in [1 \mathrel{ {.}\,{.} } n] \backslash \{ 1 \}} (C([1 \mathrel{ {.}\,{.} } n] \backslash \{ k\}, k) + c(v_k, v_1))
$$

Qui est le coût minimal du voyageur de commerce.

> En supposant que l'on connaisse $C(I, j)$ pour tous les sous-ensembles $I$ à $k$ éléments et tous les $j$, écrivez l'algorithme qui calcule tous les $C(I', j)$ pour tous les sous-ensembles $I'$ à $k+1$ éléments.
{.faire}
{% details solution %}

On a :

$$
C(I', j) =  \min_{k \in I' \backslash \{ 1 \}} (C(I' \backslash \{ k\}, k) + c(v_k, v_j))
$$

Comme j n'est pas dans $I'$, ceci est équivalent à :

$$
C(I', j) = \min_{I \cup \{ \{ k\}\} = I'} (C(I, k) + c(v_k, v_j))
$$

On peut donc écrire :

```text
    pour chaque I de E:
        pour chaque l de [1..n] qui n'est pas dans I:
            pour chaque j de [1..n] qui n'est pas dans I et qui n'est pas l:                        
                m = C(I, l) + c(v_l, v_j)
                si C(I + {l}, j) n'existe pas:
                    C(I + {l}, j) = m
                sinon:
                    C(I + {l}, j) = min(C(I + {l}, j), m)
```

La complexité de cet algorithme est en $\mathcal{O}((n-k)(n-k-1))$ pour chaque élément de $E$ et comme il y en a $2^k$ éléments, la complexité totale de cet algorithme est :
$$
\mathcal{O}(2^k(n-k)^2)
$$
{% enddetails %}

> Ecrivez l'algorithme de résolution du problème du voyageur de commerce itérativement en partant de l'ensemble $E = \{\{1\}\}$.
>
>Montrez que sa complexité peut être estimée à $\mathcal{O}(n^22^n)$.
{.faire}
{% details solution %}

Il suffit d'appliquer itérativement l'algorithme précédent jusqu'à obtenir $C(I, k)$ pour tous les sous-ensembles à $n-1$ éléments contenant 1.

La complexité totale est donc : $\mathcal{O}(\sum_{k=1}^{n-1}2^k \cdot (n-k)^2) = \mathcal{O}(n^22^n)$

{% enddetails %}

Cette complexité est importante, mais tout de même plus petite que l'énumération de tous les cycles : on ne garde qu'une solution pour un sous-ensemble donné et pas tous les cycles possibles.

