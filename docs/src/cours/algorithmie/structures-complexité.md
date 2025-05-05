---
layout: layout/post.njk

title: Mesures de complexités pour des structures et leurs méthodes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Manipuler des objets ou des structures en algorithmie va nécessiter des opérations élémentaires qu'il faut compter pour en connaître la complexité. On peut classer ces manipulations en trois grandes catégories :

{% note "**Définition**" %}

Pour chaque type de donnée (base ou structure) ses **_complexités_** sont  :

- **_complexité de création_** d'un objet de ce type
- **_complexité de suppression_** d'un objet de ce type
- **_complexité d'opération_** qui regroupe la complexité de chaque opération ou méthode lié à ce type

{% endnote %}

Toutes les manipulations d'objets de type basique (booléens, bit, entiers, réels, caractères et chaines de caractères) ou de type tableau sont en $\mathcal{O}(1)$ opérations. Ce n'est plus le cas lorsque l'on utilise des types plus complexes, on l'a vue avec les listes ou les dictionnaires par exemple.

> TBD : rappel ici complexite structures connu et dire on a besoin de amortie

> TBD explicite ne code ou opn ne connait pas les fonctions ! Il faut inférer la complexité via la connaissance des algos.


## Listes de python

Le langage python ne connaît pas les tableaux. Il utilise le type [liste](https://docs.python.org/fr/3/tutorial/introduction.html#lists) à la place. Une liste peut être vue comme l'évolution du type tableau. On donne ici juste les complexités de cette structure pour que vous puissiez les utiliser dans vos programmes :

- **créer et supprimer une liste** de taille $n$ en $\mathcal{O}(1)$ opérations
- **récupérer et affecter** l'objet d'indice $i$ d'une liste (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations
- **augmenter la taille** d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
- **supprimer le dernier élément** d'une liste se fait en $\mathcal{O}(1)$ opérations

{% attention "**À retenir**" %}
Une liste peut-être vue comme un tableau dont on peut augmenter ou diminuer la taille **par la fin** en $\mathcal{O}(1)$ opérations.
{% endattention %}
{% info %}
Ne confondez pas liste et [liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e) ce n'est pas du tout la même structure !
{% endinfo %}

## Itérateur

La gestion des boucles `pour chaque`{.language-} en python se fait via des itérateurs. Ce sont de petits programmes dont le but est de donner le prochain élément. Par exemple :

```python
for x in range(1000000):
  print(x)
```

Ne commence pas par créer la liste allant de 0 à 999999, mais produit un itérateur qui rend la prochaine valeur en $\mathcal{O}(1)$.

On a pris ce parti pour l'écriture des boucles en pseudo-code :

```pseudocode
pour chaque x de [0, 999999]:
  affiche à l'écran x
```

Prend $\mathcal{O}(1)$ instructions et ne crée pas l'intervalle en entier.

Vous verrez parfois l'écriture alternative qui explicite l'itérateur et est considérée comme équivalente :

```pseudocode
pour x allant de 0 à 999999:
  affiche à l'écran x
```

## Opérations sur les listes python

On a dit que l'on pouvait considérer que la création d'une liste, d'un tableau et d'une chaîne de caractères comme valant $\mathcal{O}(1)$. Ceci était un raccourci qu'il nous faut maintenant expliciter car il peut induire en erreur lorsque l'on considères des opérations sur les conteneurs comme la concaténation.

Les opérations de création d'un conteur (comme un tableau, une liste, un ensemble, ou encore un dictionnaire) possédant $K$ objets est usuellement de complexité en $\mathcal{O}(K)$.

Si $K$ est une constante la complexité de création est bien $\mathcal{O}(1)$. Comme dans le cas suivant :

```python
x = [1, 2, 3]
```

Mais si $K$ n'est pas une constante, comme dans le cas ci-après, on ne peut plus assimiler $\mathcal{O}(K)$ à $\mathcal{O}(1)$ :

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
  - $C$ la complexité de créer un conteneur vide (souvent $\mathcal{O}(1)$)
- la création d'un conteneur résultant de la concaténation de deux conteurs, comme $x + y$si $x$ et $y$ sont de conteneurs, est de complexité $\mathcal{O}(n_1 + n_2) + C$ où :
  - $n_1$ et $n_2$ sont les tailles des deux conteneurs
  - $C$ la complexité de créer un conteneur vide (souvent $\mathcal{O}(1)$)

## Fonctions et méthodes données de python

Il faut connaître les différentes complexités des méthodes et fonctions utilisées. Ne vous laissez pas méprendre. Ce n'est pas parce qu'elle font 1 seule ligne que leur complexité est en $\mathcal{O}(1)$. Par exemple la complexité de la méthode `index`{.language-} des listes ((comme une `l.index("?")`{.language-}) ou encore  la méthode `max`{.language-} de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Sont de complexité $\mathcal{O}(n)$  où $n$ est la taille de la liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

{% attention %}
Lorsque vous utilisez des fonctions et des méthodes en python, **il faut toujours vérifier la complexité de celles-ci**. Ce n'est pas toujours $\mathcal{O}(1)$.
{% endattention %}
