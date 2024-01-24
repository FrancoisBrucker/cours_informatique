---
layout: layout/post.njk

title: Mesures de complexités pour des méthodes et des structures

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lorsque l'on code un algorithme, on a coutume (et c'est très bien) d'utiliser des fonctions, des méthodes ou des structures de données que l'on n'a pas écrites. Il faut en revanche bien connaître leurs complexités pour ne pas commettre d'erreur de calcul.

{% note "**À retenir**" %}
Lorsque l'on calcule une complexité toutes les méthodes et fonctions doivent être examinées.
{% endnote %}

## Complexité de structure

En informatique, les **objets que l'on manipule ont des types**. On connaît déjà des [objets basiques](../pseudo-code#objets-basique){.interne} qui sont de types booléens, entiers, réels ou encore chaines de caractères pour lesquels toutes les opérations basiques que l'on peut effectuer avec eux sont en $\mathcal{O}(1)$ opérations. Ce n'est plus le cas lorsque l'on utilise des type plus complexes, composé de types basiques comme les tableaux, ou encore les listes de python. Pour pouvoir calculer la complexité d'un algorithme les utilisant, il faut connaître les complexités de ses opérations. Souvent, les opérations suivantes suffisent :

{% note "**À retenir**" %}
Pour chaque type de donnée, il faut connaître la complexité de :

- la création d'un objet de ce type
- la suppression d'un objet de ce type
- chaque méthode liée au type

{% endnote %}

### Tableaux

Prenons [le type tableau](../../écrire-algorithmes/pseudo-code/#tableaux) comme exemple. Un tableau est un conteneur pouvant contenir $n$ objets (on appelle $n$ la taille d'un tableau). On peut accéder et affecter un objet au tableau grâce à un indice allant de $0$ à $n-1$ : si `t`{.language-} est un tableau `t[i]`{.language-} correspond à l'objet d'indice $i$ du tableau.

Avec un tableau on peut faire uniquement 3 choses :

- **créer un tableau** de taille $n$ en $\mathcal{O}(1)$ opérations
- **supprimer un tableau** est possible en $\mathcal{O}(1)$ opérations
- **récupérer et affecter** l'objet d'indice $i$ du tableau (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations

{% attention %}
il est **impossible** de redimensionner un tableau. Sa taille est **fixée** à la création. Toute méthode qui vise à augmenter ou diminuer la taille d'un tableau recrée un nouveau tableau et copie tous les éléments de l'ancien tableau dans le nouveau.
{% endattention %}

### Listes

Le langage python ne connaît pas les tableaux. Il utilise le type [liste](https://docs.python.org/fr/3/tutorial/introduction.html#lists) à la place. Une liste peut être vue comme l'évolution du type tableau. On donne ici juste les complexités de cette structure pour que vous puissiez les utiliser dans vos programmes :

- **créer et supprimer une liste** de taille $n$ en $\mathcal{O}(1)$ opérations
- **récupérer et affecter** l'objet d'indice $i$ d'une liste (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations
- **augmenter la taille** d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
- **supprimer le dernier élément** d'une liste se fait en $\mathcal{O}(1)$ opérations

{% note "**À retenir**" %}
Une liste peut-être vue comme un tableau dont on peut augmenter ou diminuer la taille **par la fin** en $\mathcal{O}(1)$ opérations.
{% endnote %}

{% attention %}
Ne confondez pas liste et [liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e) ce n'est pas du tout la même structure !
{% endattention %}

## Fonctions et méthodes données

Il faut connaître les différentes complexités des méthodes et fonctions utilisées. Ne vous laissez pas méprendre. Ce n'est pas parce qu'elle font 1 seule ligne que leur complexité est en $\mathcal{O}(1)$. Par exemple la complexité de la méthode `max`{.language-} de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Est de complexité $\mathcal{O}(n)$  où $n$ est la taille de la liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

{% attention %}
Lorsque vous utilisez des fonctions et des méthodes en python, **il faut toujours vérifier la complexité de celles-ci**. Ce n'est pas toujours $\mathcal{O}(1)$.
{% endattention %}
