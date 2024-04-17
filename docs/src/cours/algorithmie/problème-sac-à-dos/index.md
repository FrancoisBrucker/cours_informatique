---
layout: layout/post.njk
title: Problème du sac à dos

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le problème du sac à dos est un problème fondamental en algorithmie, nombre de problèmes courant pouvant se modéliser sous cette forme.

## Sac à dos fractionnel

{% lien %}
[sac à dos fractionnel](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos#Variables_continues)
{% endlien %}

Commençons par une version simplifiée du problème, dit du **_sac à dos fractionnel_** :

{% note "**Problème**" %}
On possède $n$ poudres différentes (ou liquide, ou tout autre produit pouvant être fractionné), chaque poudre $i$ étant décrite par :

- sa quantité disponible en kilo : $k_i$
- son prix au kilo : $p_i$

On dispose d'un sac pouvant contenir $K$ kilos de poudre et on cherche une répartition de poudre permettant de maximiser la valeur du sac.
{% endnote %}

Par exemple, on a un sac à dos de 20kg et six poudres de paramètres :


- poudre 1 : 15kg et un prix de 9€ le kilo
- poudre 2 : 2kg et un prix de 16€ le kilo
- poudre 3 : 4kg et un prix de 8€ le kilo
- poudre 4 : 1kg et un prix de 6€ le kilo
- poudre 5 : 6kg et un prix de 3€ le kilo
- poudre 6 : 80kg et un prix de 10€ le kilo

Le sac peut contenir soit :

- 20kg de la poudre 6, pour un profit de 200€,
- 14kg de la poudre 1 et 6kg de la poudre 5, pour un profit de 114€,
- 1kg de la poudre 1 à 5 et le reste (15kg) en poudre 6, pour un profit de 192€,
- ...

### Algorithme glouton

Le problème du sac à dos fractionnel peut se résoudre par un algorithme glouton : à chaque étape on ajoute une poudre et on essaie d'en mettre le plus possible. Comme on veut maximiser le profit, on trie les poudres par prix au kilo décroissant.

On obtient donc in fine l'algorithme suivant, écrit en python :

```python
def sac_a_dos_fractionel(produits, masse_totale):
    produits.sort(key=lambda x: -x[0])
    sac_a_dos = []
    for i in range(len(produits)):
        prix, kilo, nom = produits[i]

        if masse_total >= kilo:
            sac_a_dos.append((nom, kilo))
            masse_totale -= kilo
        else:
            sac_a_dos.append((nom, masse_totale))
            masse_totale = 0

    return sac_a_dos
```

- entrée : liste de produits, chaque produit étant une liste [prix au kilo, kg, nom]
- sortie : liste de produits [nom, kilo] où nom est le nom du produit dans la liste d'entrée et kilo, le nombre de kilo pris.

On trie la liste dans le code. Comme le 1er élément de chaque liste est le prix au kilo, le résultat sera une liste de produit trié par prix au kilo croissante. On la retourne (avec la méthode `reverse()`{.language-}) pour avoir les produit triés par prix au kilo décroissant.

La complexité de cet algorithme est déterminée par le tri, puisque l'intérieure de la boucle for est en temps constant.

{% info %}
- Astuce du tri : lorsque l'on trie une liste de liste, python utilise l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique). Cela permet ici de trier sur les prix volumique tout en conservant l'indice du tableau d'origine (le deuxième élément de la liste n'intervient dans le tri que si les 2 premiers éléments sont identique, ce qui ne change pas le tri par prix volumique)
- attention, les méthodes de liste `sort`{.language-} et `reverse`{.language-} ne rendent rien. Elles modifient la liste. De là `l.sort().reverse()`{.language-} **ne fonctionne pas** puisque cette commande signifie que l'on applique la méthode `reverse` à l'objet donné en retour de `l.sort()`{.language-}. Or comme `l.sort()`{.language-} ne rend rien elle retourne l'objet `None`{.language-} (l'objet _rien du tout_ en python) qui ne possède pas de méthode `reverse`{.language-}. C'est ce que dit le message d'erreur quand on essaie de le faire : `AttributeError: 'NoneType' object has no attribute 'reverse'`{.language-} (le type de l'objet `None`{.language-} (comme le tpe des entier est `int`{.language-} ou le type des réels est `float`{.language-}) est `NoneType`{.language-} (il a un type à lui)).

{% endinfo %}

En reprenant l'exemple, l'algorithme rend comme composition du sac à dos :

- les 2kg de la poudre 2
- 18kg de la poudre 6

Pour un profit de 208€

### Preuve d'optimalité

Cet algorithme glouton est même optimal !

On peut remarquer que l'algorithme glouton prend toujours tout le produit disponible jusqu'au dernier choix où il ne prend qu'une fraction de celui-ci (la place restante) pour finir de remplir le sac-à-dos .

Pour notre solution, on note $(k_0, k_1, \dots, k_n)$ les kilos choisis dans l'ordre de choix de l'algorithme glouton.
On suppose que notre solution n'est pas optimale et, parmi toutes les solutions optimales possible, on en prend une qui correspond le plus longtemps possible avec la solution rendue par l'algorithme. Soit alors $0 \leq i <n$ le plus petit indice telle que la solution optimale et celle rendue par l'algorithme est différente. La solution optimale est alors $(k_0, \dots, k_{i-1}, k'_i, \dots, k'_n)$.

On peut enfin, sans perte de généralité, choisir la solution optimale ayant $k_i'$ le plus grand possible parmi toutes les solutions optimales coïncidant avec la solution de l'algorithme glouton jusqu'à $k_{i-1}$.

Jusqu'à l'étape $i-1$ tous les choix sont identiques donc une fois placés les $i$ premiers produits (les produits d'indices $0$ à $i-1$) avec le même kilo, il reste la même place dans le sac-à-dos et pour notre algorithme et pour la solution optimale. De là, par construction de l'algorithme glouton (on prend à chaque choix soit tout le produit soit juste assez pour finir de remplir tout le sac) les kilos $k'_i$ de la solution optimale pour le produit d'indice $i$ est forcément plus petit strictement que $k_i$.

Donc :

- soit $k'_j = 0$ pour tout $j > i$ et notre solution est meilleure que la solution optimale, ce qui est impossible par hypothèse,
- soit il existe $k'_j >0$ pour un $j>i$. On peut alors diminuer d'un kilo $k_j'$ pour augmenter d'un kilo $k_i'$ et obtenir une solution strictement meilleure que la solution optimale : c'est impossible.

Notre hypothèse arrivant à une contradiction, elle était fausse : la solution de l'algorithme glouton est optimale.

## Problème du sac à dos

{% lien %}
[Problème du sac à dos](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos)
{% endlien %}

Le fait de pouvoir fractionner les éléments est un cas particulier heureux, mais ce n'est pas la norme, pensez à un déménagement : les déménageurs ne peuvent prendre qu'un bout du canapé sous prétexte qu'il ne rentre pas en entier dans le camion... La formalisation classique du sac à dos ne permet pas de scinder des objets :

{% note "**Problème**" %}
On possède $n$ aliments (de 1 à $n$), chacun décrit par :

- sa quantité nutritive : $p_i$ ($1 \leq i \leq n$)
- sa masse en kilo : $k_i$ ($1 \leq i \leq n$)

On dispose d'un sac pouvant contenir $K$ kilos et on cherche à maximiser la quantité nutritive emmenée.
{% endnote %}

Ce problème se décline de plein de façons pratique :

- en remplaçant la masse par le volume on peut remplir un camion de déménagement au maximum théorique
- mais aussi le stockage de fichiers (les aliments) sur un disque dur (le sac à dos) de capacité limité (la quantité nutritive est la taille de chaque fichier)
- ou encore maximiser la charge d'un générateur
- ...

Comme on ne peut pas découper les aliments au contraire du sac à dos fractionnel, on a le résultat suivant :

{% note "**Proposition**" %}
La solution optimale d'un problème du sac à dos est inférieure à la solution optimale des mêmes données appliquée au problème du sac à dos fractionnel
{% endnote %}
{% details "preuve", "open" %}
La solution optimale du problème du sac à dos est une solution admissible au problème du sac à dos fractionnel, son optimum est donc nécessairement plus grand.
{% enddetails %}

## Algorithme glouton

Comme les solutions du sac à dos sont des solutions admissible du sac à dos fractionnel, on peut tenter d'adapter l'algorithme glouton (optimal) précédent au problème du sac à dos :

```python
def sac_a_dos_glouton(aliments, masse_totale):
    aliments.sort(key=lambda x: -x[0] / x[1])
    sac_a_dos = []

    for i in range(len(aliments)):
        p, k, nom = aliments[i]

        if masse_total >= k:
            sac_a_dos.append(nom)
            masse_totale -= k

    return sac_a_dos
```

- entrée : liste d'aliments, chaque aliment étant une liste [prix, kg, nom]
- sortie : liste de noms d'aliments choisis pour être dans le sac à dos 

On a ici trié les aliment par valeur nutritive par kilo décroissante.

Reprenons l'exemple et modifions le pour que l'on ne puisse pas prendre une fraction de poudre :

- poudre 1 : 15kg et un prix de 135€, prix de 9€ le kilo
- poudre 2 : 2kg et un prix de 28€, prix de 16€ le kilo
- poudre 3 : 4kg et un prix de 32€, prix de 8€ le kilo
- poudre 4 : 1kg et un prix de 6€, prix de 6€ le kilo
- poudre 5 : 6kg et un prix de 18€, prix de 3€ le kilo
- poudre 6 : 80kg et un prix de 800€, prix de 10€ le kilo

En maximisant le profit, l'algorithme glouton préconise de prendre les poudres 1, 2 et 4 pour un profit de 157€. On se rend cependant compte que cette solution n'est plus maximale ! En effet prendre les poudres 1, 3 et 4 rapporte un profit de  173€.

On peut même montrer que l'algorithme glouton ne possède pas de garantie :

{% exercice %}
Montrer que pour 2 aliments seulement, le rapport entre la solution optimale et la solution de l'algorithme glouton peut-être aussi grand que l'on veut.
{% endexercice %}
{% details "corrigé" %}

Si l'on prend les aliments :

- aliment 1 : de valeur nutritive 2 et de poids 1,
- aliment 2 : de valeur nutritive K et de poids K, qui correspond à la masse totale que peut contenir le sac à dos.

Le glouton privilégiera toujours l'aliment 1 alors que c'est l'aliment 2 qu'il faut choisir. Comme on peut faire grossir la capacité du sac, le rapport entre la valeur optimale et celle donnée par le glouton peut être aussi grand que l'on veut.
{% enddetails %}

On peu alors vouloir modifier l'algorithme glouton pour considérer la valeur nutritive totale et pas celle au kilo (on trouve alors l'optimum pour l'exemple) mais ce n'est pas non plus super :


{% exercice %}
Montrer que le rapport entre la solution optimale et la solution de l'algorithme glouton modifiée peut-être aussi grand que l'on veut.
{% endexercice %}
{% details "corrigé" %}

Si l'on prend $K+1$ aliments :

- aliment 1 : de valeur nutritive 2 et de poids $K$, qui correspond à la masse totale que peut contenir le sac à dos.
- aliment 2 à $K+1$ : de valeur nutritive 1 et de poids 1

Le glouton privilégiera toujours l'aliment 1 alors que c'est les aliments 2 à $K+1$ qu'il faut choisir. Comme on peut faire grossir la capacité du sac, le rapport entre la valeur optimale et celle donnée par le glouton peut être aussi grand que l'on veut.
{% enddetails %}

Tout n'est cependant pas perdu car on peut modifier l'algorithme glouton pour qu'il soit à performance garantie.

## Algorithme à performance garantie

Lors de l'exécution de l'algorithme glouton, soit $i^\star$ la première étape telle que l'aliment ne peut pas être ajouté dans le sac. On a alors :

- $\sum_{i < i^\star} k_i \leq K$
- $\sum_{i < i^\star} k_i + k_{i^\star} > K$
- la solution du sac à dos fractionnel associé est : $\sum_{i < i^\star} p_i + (\frac{K-\sum_{i < i^\star} k_i}{k_{i^\star}}) \cdot p_{i^\star}$

Des constatations ci-dessus on peut alors constituer l'algorithme suivant (en supposant sans perte de généralité que $k_i \leq K$ pour tout $i$ donc que tous les aliments rentrent dans le sac) :

1. on trie tous les aliments par valeur nutritionnelle au kilo décroissante
2. on note $i^\star$ le premier élément dans cet ordre tel que $\sum_{i \leq i^\star} k_i > K$
3. l'algorithme rend $\max(\sum_{i < i^\star} p_i, p_{i^\star})$.

Cette simple modification permet de garantir la solution obtenue :

{% exercice %}
En utilisant le fait que $a + b \leq 2\cdot \max(a, b)$, montrer la la solution de l'algorithme ne peut pas être moins que 2 fois moins bonne que la solution optimale.
{% endexercice %}
{% details "solution" %}
> TBD
{% enddetails %}

## TBD

> TBD généralisation aux sac à dos multi-dimentionnels ie. les problèmes de découpe.
> TBD subset sum

> TBD : peut se reécrire de plein de façons. 

> TBD tres bien car il y a tout et bien d'autrers choses pour resoudre ce probleme.

> <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2017KnapSack.pdf>

> <https://datamove.imag.fr/denis.trystram/SupportsDeCours/SlidesApproximationKnapsack.pdf>
> <https://www.i2m.univ-amu.fr/perso/jean-philippe.preaux/PDF/pdf_proteges/OptimisationCombinatoire/Heuristiques2.pdf>
> <https://tarakc02.github.io/branch-and-bound/>
> <https://dept-info.labri.fr/ENSEIGNEMENT/projet2/supports/Sac-a-dos/Le-probleme-du-sac-a-dos.pdf>

meet in the middle : <https://en.wikipedia.org/wiki/Knapsack_problem>
<https://interstices.info/le-probleme-du-sac-a-dos/>
<https://www.youtube.com/watch?v=MacVqujSXWE>
branch and bound : <https://www.youtube.com/watch?v=E7hJXsywOdA>

> suite super croissante, c'est facile
> <https://www.bibmath.net/crypto/index.php?action=affiche&quoi=moderne/sacados#google_vignette> algo ? <https://laure.gonnord.org/pro/teaching/MIF30/guillet_yombi_rapport.pdf> <https://laure.gonnord.org/pro/teaching/MIF30/projets2009/guillet_yombi_expose.pdf
## Sac à dos entier

> glouton marche pas
> programmation dynamique
> attention à la complexité

> programmation en 0/1 vs programmation linéaire : écrire les matrices

## Heuristique

> performance garantie
> branch and bound ? génétique ?


## TP

<https://informatique.ens-lyon.fr/concours-info/2011/sujet-jour5-2011.pdf>
