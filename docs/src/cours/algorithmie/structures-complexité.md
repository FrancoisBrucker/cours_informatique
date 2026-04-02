---
layout: layout/post.njk

title: Mesures de complexités pour des structures et leurs méthodes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à dispatcher bien


Comparons l'usage les différentes structures de stockage de données en notre possession :

- tableaux :
  - structure simple
  - intérêt : accès au $i$ème élément se fait en $\mathcal{O}(1)$
  - défaut : structure statique, on ne peut ajouter/supprimer des éléments
  - utilisation : si contrôle stricte de la complexité en temps et en espace crucial
- pile :
  - gestion de flux : LIFO
  - utilisation : à la place d'une récursion
- file :
  - gestion de flux : FIFO
  - utilisation : buffer
- listes :
  - structure passe partout
  - intérêt : ajout et suppression en fin de liste en $\mathcal{O}(1)$, accès au $i$ème élément se fait en $\mathcal{O}(1)$
  - défaut : supprimer/ajouter le $i$ème élément se fait en $\mathcal{O}(n-i)$ où $n$ est la taille de la liste.
  - utilisation : à la place d'un tableau si on autorise une taille variable et un pic de complexité de temps en temps
- dictionnaires :
  - clé et valeurs
  - intérêt : ajout et suppression et accès à un élément en $\mathcal{O}(1)$ en moyenne.
  - défaut : pas d'ordre entre en les éléments stockés, complexité max en $\mathcal{O}(n)$ où $n$ est le nombre d'éléments stockés
  - utilisation : lorsque les données ne sont pas des indices et que la complexité en moyenne suffit
- listes chaînées :
  - structure par morceaux où maillon = chaîne
  - intérêt : ajout et suppression en milieu de liste en $\mathcal{O}(1)$
  - défaut : trouver le $i$ème élément se fait en $\mathcal{O}(i)$.
  - utilisation : pour les programmes récursifs et ceux où on modifie souvent le nombre de données stockées tout en conservant l'ordre des données restantes


 <!-- TBD à dispatcher

#### Complexités des structures linéaires

Les différences structures linéaires que l'on a vu vont avoir des complexités différentes selon l'opération réalisée. Une analyse fine du problème à résoudre ou de l'algorithme à coder est souvent nécessaire pour choisir la structure la plus adaptée, c'est à dire :

1. Utiliser celle qui permettra d'obtenir la complexité la plus faible (utiliser des listes chaînées plutôt que des listes dans des algorithmes récursif par exemple)
2. Utiliser celle dont l'utilisation sera la plus simple sans sacrifier totalement complexité (utiliser des dictionnaires plutôt que des listes si les données ne sont pas des indices par exemple)

- tableaux :
  - création : $\mathcal{O}(1)$
  - suppression : $\mathcal{O}(1)$
  - accéder et modifier un élément via son indice : $\mathcal{O}(1)$
- pile :
  - création : $\mathcal{O}(1)$
  - suppression : $\mathcal{O}(1)$
  - append et pop : $\mathcal{O}(1)$
- file :
  - création : $\mathcal{O}(1)$
  - suppression : $\mathcal{O}(1)$
  - append et pop : $\mathcal{O}(1)$
- liste :
  - création : $\mathcal{O}(1)$
  - suppression : $\mathcal{O}(1)$
  - accéder et modifier un élément via son indice : $\mathcal{O}(1)$
  - ajouter un dernier élément : $\mathcal{O}(1)$ (en amortie)
  - supprimer le dernier élément : $\mathcal{O}(1)$ (en amortie)
- dictionnaire :
  - création : $\mathcal{O}(1)$
  - suppression : $\mathcal{O}(n)$ (avec $n$ la taille des éléments stockés)
  - accéder et modifier un élément via sa clé : $\mathcal{O}(1)$ en moyenne ($\mathcal{O}(n)$ avec $n$ la taille des éléments stockés si on a vraiment pas de chance)
  - ajouter un élément : $\mathcal{O}(1)$ en moyenne ($\mathcal{O}(n)$ avec $n$ la taille des éléments stockés si on a vraiment pas de chance)
  - supprimer un élément : $\mathcal{O}(1)$ en moyenne ($\mathcal{O}(n)$ avec $n$ la taille des éléments stockés si on a vraiment pas de chance)

## Complexité de structure en python

On prend ici l'exemple de python et on analyse la complexité de quelques structures iconiques du langage

### Listes

Le langage python ne connaît pas les tableaux. Il utilise la [liste](https://docs.python.org/fr/3/tutorial/introduction.html#lists) à la place. On a donc comme complexité :

- **créer et supprimer une liste** de taille $n$ en $\mathcal{O}(1)$ opérations
- **récupérer et affecter** l'objet d'indice $i$ d'une liste (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations
- **augmenter la taille** d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
- **supprimer le dernier élément** d'une liste se fait en $\mathcal{O}(1)$ opérations

### Itérateur

La gestion des boucles `pour chaque`{.language-} en python se fait via des itérateurs. Ce sont de petits programmes dont le but est de donner le prochain élément. Par exemple :

```python
for x in range(1000000):
  print(x)
```

Ne commence pas par créer la liste allant de 0 à 999999, mais produit un itérateur qui rend la prochaine valeur en $\mathcal{O}(1)$.

On a pris ce parti pour l'écriture des boucles en pseudo-code :

```pseudocode
pour chaque x de [0 .. 1000000[:
  affiche x à l'écran
```

Prend $\mathcal{O}(1)$ instructions et ne crée pas l'intervalle en entier.

### Opérations sur les listes python

On a dit que l'on pouvait considérer que la création d'une liste, d'un tableau et d'une chaîne de caractères comme valant $\mathcal{O}(1)$. Ceci était un raccourci qu'il nous faut maintenant expliciter car il peut induire en erreur lorsque l'on considères des opérations sur les conteneurs comme la concaténation.

Les opérations de création d'un conteur (comme un tableau, une liste, un ensemble, ou encore un dictionnaire) possédant $n$ objets est usuellement de complexité en $\mathcal{O}(n)$.

Si $n$ est une constante la complexité de création est bien $\mathcal{O}(1)$. Comme dans le cas suivant :

```python
x = [1, 2, 3]
```

Mais si $n$ n'est pas une constante, comme dans le cas ci-après, on ne peut plus assimiler $\mathcal{O}(n)$ à $\mathcal{O}(1)$ :

```python
def duplique(x):
  return list(x)
```

La complexité de la fonction `duplique(x: list) -> list`{.language-} n'est **pas** $\mathcal{O}(1)$ mais bien $\mathcal{O}(\text{len}(x))$.

{% attention %}
La complexité des opérations créant des conteneurs dépend toujours de leurs tailles.
{% endattention %}

De là :

- la création d'un conteneur contenant tous les éléments d'un autre conteneur, comme `list(x)`{.language-}, , est de complexité $\mathcal{O}(n) + C$ où :
  - $n$ est la taille du conteneur dupliqué
  - $C$ la complexité de créer un conteneur vide (ici $\mathcal{O}(1)$)
- la création d'un conteneur résultant de la concaténation de deux conteurs, comme $x + y$ si $x$ et $y$ sont de conteneurs, est de complexité $\mathcal{O}(n_1 + n_2) + C$ où :
  - $n_1$ et $n_2$ sont les tailles des deux conteneurs
  - $C$ la complexité de créer un conteneur vide (ici $\mathcal{O}(1)$) -->
