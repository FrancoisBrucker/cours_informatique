---
layout: layout/post.njk 
title: Complexité max/min

eleventyNavigation:
    order: 1
    prerequis:
        - "../../pseudo-code/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On se donne des outils pour mesurer (théoriquement et en pratique) les performances d'un algorithme

<!-- end résumé -->


## Complexité d'un algorithme


> TBD : ici

### Nombre d'opérations basiques

{% note %}
La **complexité** (aussi parfois appelée **complexité maximale**) d'un algorithme est le **nombre maximum d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{% endnote %}

La **taille** d'une entrée est proportionnelle au nombre de cases mémoires que celle-ci nécessite.

{% info %}
Lorsque vous entendrez parler de *complexité* d'un algorithme, ce sera par défaut **toujours** la complexité maximale.
{% endinfo %}

Il arrive que certains algorithmes aient un comportement très différent selon les entrées. Parler seulement de la complexité (nombre maximum d'opérations) ne permet alors pas de le caractériser complètement. On parlera  aussi de :

{% note %}
La **complexité minimale** d'un algorithme est le **nombre minium d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{% endnote %}

Lorsque l'on calcule une complexité (maximale ou minimale) sous la forme d'un $\mathcal{O}(f(N))$, on tentera bien sur de trouver la fonction $f(N)$ la plus petite possible.

### <span id="temps-exécution"></span> Temps d'exécution

Un moyen efficace de mesurer la complexité d'un algorithme écrit sous la forme d'un code exécutable est de mesurer le temps mis par son exécution pour un jeu d'entrée donné.

{% note %}
La **complexité en temps** d'un algorithme est le temps mis pour l'exécuter en utilisant un jeu de donné **pour lequel la complexité (max) est atteinte** et d'une taille totale donnée.
{% endnote %}

Le temps pris sera bien sur différent si l'on prend une machine plus puissante ou si l'on change le code de l'algorithme mais **l'évolution de la complexité en temps par rapport à la taille des données est toujours proportionnelle à la complexité**. Pour le voir, il suffit de mesurer la durée d'exécution de chaque instruction basique et de la borner par le max :

{% note %}
Complexité et complexité en temps sont deux notions équivalentes.
{% endnote %}

{% attention %}
Si vous ne prenez **pas** un jeu de donné pour lequel la complexité de l'algorithme est atteinte, vous ne mesurez **pas** la complexité temporelle de l'algorithme...
{% endattention %}

### Taille mémoire

{% note %}
La **complexité en espace** d'un algorithme est le nombre maximum de cases mémoires utilisées pour l'exécuter en utilisant un jeu de donnés de taille donnée.
{% endnote %}

Comme la complexité, on la mesurera avec des $\mathcal{O}$.

La complexité en espace n'est pas forcément atteinte pour un jeu de données donnant la complexité de l'algorithme, mais **la complexité en espace sera toujours plus faible que la complexité** (visiter une case mémoire nécessitant une opération élémentaire).

### Complexité de méthodes ou de structures

Lorsque l'on code un algorithme, on a coutume (et c'est très bien) d'utiliser des fonctions, des méthodes ou des structures que l'on n'a pas écrites. Il faut en revanche bien connaître leurs complexités pour ne pas commettre d'erreur de calcul.

{% note %}
Lorsque l'on calcule une complexité toutes les méthodes et fonctions doivent être examinées
{% endnote %}

#### Complexité de structure

En informatique, les **objets que l'on manipule ont des types**. On connaît déjà des [objets basiques](../pseudo-code#objets-basique){.interne} qui sont de types booléens, entiers, réels ou encore chaines de caractères pour lesquels toutes les opérations basiques que l'on peut effectuer avec eux sont en $\mathcal{O}(1)$ opérations. Ce n'est plus le cas lorsque l'on utilise des type plus complexes, composé de types basiques comme les conteneurs comme les tableaux, ou encore les listes de python. Pour pouvoir calculer la complexité d'un algorithme les utilisant, il faut connaître les complexités de ses opérations. Souvent, les opérations suivantes suffisent :

{% note %}
Pour chaque type de donnée, il faut connaître la complexité de :

* la création d'un objet de ce type
* la suppression d'un objet de ce type
* chaque méthode liée au type

{% endnote %}

Prenons le type [tableau](../structure-de-données/tableau){.interne} comme exemple. Un tableau est un conteneur pouvant contenir $n$ objets (on appelle $n$ la taille d'un tableau). On peut accéder et affecter un objet au tableau grâce à un indice allant de $0$ à $n-1$ : si `t`{.language-} est un tableau `t[i]`{.language-} correspond à l'objet d'indice $i$ du tableau.

Avec un tableau on peut faire uniquement 3 choses :

* **créer un tableau** de taille $n$ en $\mathcal{O}(1)$ opérations
* **supprimer un tableau** est possible en $\mathcal{O}(1)$ opérations
* **récupérer et affecter** l'objet d'indice $i$ du tableau (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations

{% attention %}
il est **impossible** de redimensionner un tableau. Sa taille est **fixée** à la création. Toute méthode qui vise à augmenter ou diminuer la taille d'un tableau recrée un nouveau tableau et copie tous les éléments de l'ancien tableau dans le nouveau.
{% endattention %}

Le langage python ne connaît pas les tableaux. Il utilise le type [liste](../structure-de-données/liste){.interne} à la place. Une liste peut être vue comme l'évolution du type tableau. On donne ici juste les complexités de cette structure pour que vous puissiez les utiliser dans vos programmes :

* **créer et supprimer une liste** de taille $n$ en $\mathcal{O}(1)$ opérations
* **récupérer et affecter** l'objet d'indice $i$ d'une liste (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations
* **augmenter la taille** d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
* **supprimer le dernier élément** d'une liste se fait en $\mathcal{O}(1)$ opérations

{% note %}
Une liste peut-être vue comme un tableau dont on peut augmenter ou diminuer la taille **par la fin** en $\mathcal{O}(1)$ opérations.
{% endnote %}

{% attention %}
Ne confondez pas liste et [liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e) ce n'est pas du tout la même structure !
{% endattention %}

#### Fonction et méthodes données

Il faut connaître les différentes complexités des méthodes et fonctions utilisées. Ne vous laissez pas méprendre. Ce n'est pas parce qu'elle font 1 seule ligne que leur complexité est en $\mathcal{O}(1)$. Par exemple la complexité de la méthode `max`{.language-} de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Est de complexité $\mathcal{O}(n)$  où $n$ est la taille de la liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

{% attention %}
Lorsque vous utilisez des fonctions et des méthodes en python, **vérifier toujours** la complexité de celles-ci. Ce n'est pas toujours $\mathcal{O}(1)$.
{% endattention %}

## <span id="exemple-recherche"></span> Exemple de la recherche d'un élément dans un tableau

Prenons par exemple l'algorithme suivant, écrit en python :

```python#
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

Cet algorithme recherche si le paramètre `valeur`{.language-} est un élément de `tableau`{.language-}.

Calculons ses complexités maximale et minimale. Commençons par regarder les complexités de chaque ligne :

1. définition de la fonction : $C_1 = \mathcal{O}(1)$
2. une boucle `for`{.language-} de $k$ itérations
3. un test entre 2 variables : $C_3 = \mathcal{O}(1)$
4. un retour de fonction $C_4 = \mathcal{O}(1)$
5. un retour de fonction : $C_5 = \mathcal{O}(1)$

Comme il y a 2 retours de fonctions (lignes 4 et 5), la complexité sera soit :

* $C = C_1 + k \cdot (C_3) + C_5 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1)) + \mathcal{O}(1)$ si on utilise la sortie de la ligne 5 (on est jamais passé par le ligne 4)
* $C' = C_1 + k \cdot (C_3) + C_4 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1) + \mathcal{O}(1))$ si on utilise la sortie de la ligne 4 en passant lors de la dernière itération de la boucle `for`{.language-} de la ligne 2

Les deux cas se simplifient en : $\mathcal{O}(k)$

En effet $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$ on a $C = C' = \mathcal{O}(1) + k \cdot (\mathcal{O}(1))$. De là, $C = C' = \mathcal{O}(1) + \mathcal{O}(k) = \mathcal{O}(k)$

On cherche le cas le pire, c'est à dire lorsque $k$ est maximum, donc lorsque la boucle `for`{.language-} parcourt tout le tableau, c'est à dire pour deux cas :

* l'élément recherché n'est pas dans le tableau
* l'élément recherché est le dernier élément du tableau

On en conclut que :

{% note %}
La complexité de l'algorithme `est_dans_tableau`{.language-} est $\mathcal{O}(n)$ où $n$ est la taille du tableau qui est un paramètre d'entrée.
{% endnote %}

La complexité minimale est quant à elle atteinte lorsque l'on ne parcourt pas notre boucle, c'est à dire lorsque la valeur recherchée est la 1ère valeur du tableau :

{% note %}
La complexité minimale de l'algorithme `est_dans_tableau`{.language-} est $\mathcal{O}(1)$.
{% endnote %}


