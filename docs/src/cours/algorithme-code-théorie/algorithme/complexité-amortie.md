---
layout: layout/post.njk 
title: Complexité amortie

eleventyNavigation:
  key: "Complexité amortie"
  parent: Algorithme
---

{% prerequis "**Prérequis** :" %}

* [Complexité max/min](../complexité-max-min)

{% endprerequis %}

<!-- début résumé -->

Définition, utilité et utilisation de la complexité amortie d'un algorithme.

<!-- end résumé -->

Si lors de l'exécution d'un algorithme $A$, une opération $O$ (ou une fonction) de celui-ci se répète plusieurs fois et que sa
complexité diffère selon les fois, le calcul de la complexité de $A$ va nécessiter une analyse fine de la complexité totale de **toutes** les opérations $O$.

{% note %}
L'***analyse amortie*** est des techniques permettant de calculer globalement la complexité maximale $C* de $m$ exécutions successives d'un algorithme.

La ***complexité amortie*** de cet algorithme est alors $\frac{C}{m}$.
{% endnote %}
{% attention %}
La complexité amortie est un calcul (fin) de complexité maximale, ce n'est **pas** une [complexité en moyenne](../complexité-moyenne)
{% endattention %}

Pour illustrer ces techniques d'analyse amortie nous allons utiliser l'exemple fil rouge du
On peut 
Lorsque les temps d'exécution d'un même algorithme peuvent varier fortement selon ses paramètres, on a vu que l'on peut calculer sa complexité en moyenne pour se donner une idée de la complexité attendue avec un jeu de paramètres donné, mais quelconque.

Il existe cependant un cas où l'on peut faire bien mieux : lorsque l'on effectue plusieurs fois le même sur de

 algorithme 
> TBD : lorsque l'on a des opérations de coût différents et que l'on veut une complexité exacte ou
> que l'on a $m$ exécution successives avec certaines qui coûtent cher et d'autres non..
> TBD : exemple du compteur avec les 3 façon de le calculer
