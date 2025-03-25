---
layout: layout/post.njk

title:  "corrigé Test 4 : tris"
---

## Barème

Une note sur 7 répartie comme suit :

- 1pt pour la question 1.1
- 1pt pour la question 1.2
- 2pt pour la question 2.1
- 1pt pour la question 2.2.1
- 1pt pour la question 2.2.2
- 1pt pour la question 2.2.3

La note sur $20$ finale est obtenue en multipliant la note sur 7 par $3$.

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question parfaitement et à comprendre que l'algorithme est en fait le tri par insertion (ce qui garantit le 14/20 avec les divers questions)
- **un bon élève** doit parvenir à réussir à justifier parfaitement la question 2.2
- **un très bon élève** à tout fait

{% endnote %}

J'ai été la gentillesse même dans mes corrections, d'où la moyenne élevée. Cependant pour beaucoup c'est encore bien flou et on sent que vous marchez sur une glace très fine. Reprenez ces notion à tête reposé et comprenez les, elles sont cruciales.

La ventilation des notes est :

|note/20  |≤8  | ]8, 10[ | [10, 12[      | [12, 14]    | ]14, 16]  | > 16
|---------|----|------------|------------|-------------|-----------|---------
|nombre   | 3  |  6         |  8         |  15         |  6        | 5
|rang min | 43 | 38         | 32         | 23          |  11       | 5

- moyenne : 12.38/20
- écart-type : 3.27/20
- médiane : 12.38/20

## Erreurs fréquemment rencontrées

### Complexité du tri

Vos justifications sont souvent bancales quand elles ne sont pas fausses ! Ne confondez pas cette notion avec la complexité minimale d'un algorithme particulier.

Enfin, si vous donnez deux algorithme de tri particuliers, ils ne peuvent être tout deux que des majorants de la complexité du problème ! C'est trouver un minorant (dans notre cas le nombre de tests à effectuer pour distinguer parmi n! cas) qui est compliqué.

{% attention %}
Reprenez le corrigé et apprenez la justification par cœur.
{% endattention %}

## Corrigé

### 1 Complexités

#### 1.1

La complexité du problème du tri est en $\Theta(n\ln(n))$ car :

La complexité d'un problème algorithmique est la complexité (maximale) la plus faible d'un algorithme le résolvant.

Pour le tri :

1. cette complexité est en $\Omega(n\ln(n))$ car tout algorithme doit discriminer parmi $n!$ ordres possibles, donc on avoir $\Omega(\log_2(n!)) = \Omega(n\ln(n))$ tests.
2. cette complexité est en $\mathcal{O}(n\ln(n))$ car c'est la complexité du tri fusion

On en conclut que la complexité du tri est en $\Theta(n\ln(n))$.

#### 1.2

La complexité en moyenne d'un algorithme est l'espérance de la complexité pour toutes les entrées possibles (par défaut on choisit un modèle où les entrées sont équiprobables).

Pour la calculer en pratique, on choisit des entrées au hasard et on mesure la moyenne du temps pris par l'algorithme pour se terminer.

### 2 Algorithme

```pseudocode
algorithme tri(T: [entier]):
   i ← 1
   tant que i < T.longueur:
      si T[i - 1] ≤ T[i]:
         i ← i + 1
      sinon:
         T[i], T[i - 1] ← T[i - 1], T[i]
         i ← max(1, i - 1)
```

#### 2.1

Cet algorithme ressemble furieusement à un tri par insertion...

Pour le démontrer on procède par récurrence sur la taille du tableau, puisque l'algorithme va se comporter de la même manière pour $T$ et $T[:-1]$.

Pour un tableau de longueur 2, l'algorithme va fonctionner. On suppose la propriété vraie pour une longueur de $n$ et on regarde ce qu'il se passe pour une longueur de $n+1$.

Par hypothèse de récurrence, l'algorithme trie $T[:-1]$. Pour le tableau $T$ en entrée il va donc arriver une itération où $i$ va valoir $T.\mbox{\small longueur} - 1$. On a alors 2 cas :

- soit $T[-1] \geq T[-2]$ et on incrémente $i$ ce qui met fin à l'algorithme : le tableau est trié
- soit $T[-1] < T[-2]$ et, comme pour le tri par insertion, on place sa valeur au bon endroit dans le tableau par échange. Une fois l'élément bien placé, $i$ va s'incrémenter jusqu'à valoir la taille du tableau et l'algorithme va s'arrêter.

#### 2.2

##### 2.2.1

En reprenant la preuve précédente, on arrive à créer l'équation de récurrence suivante :

<div>
$$
C(n) = C(n-1) + \mathcal{O}(n)
$$
</div>

Puisque trié $T$, de complexité $C(n)$ revient au maximum à :

1. trier $T[:-1]$, de complexité $C(n-1)$
2. placer le dernier élément par échange à sa place $\mathcal{O}(n)$ échanges
3. incrémenter $i$ jusqu'à ce qu'il vale la taille du tableau en $\mathcal{O}(n)$ itérations

Cette équation se résout en $C(n) =  \mathcal{O}(n^2)$

##### 2.2.2

Si le tableau est déjà trié, $i$ n'est jamais décrémenté et on s'arrête en $\mathcal{O}(n)$ itérations. La complexité pour un tableau trié est ainsi de $\mathcal{O}(n)$.

##### 2.2.3

En moyenne, l'indice $i$ va remonter de la moitié de la taille du tableau pour insérer le nouvel élément, ce qui donne une complexité totale de $\mathcal{O}(n^2)$ opérations.
