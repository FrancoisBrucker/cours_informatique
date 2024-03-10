---
layout: layout/post.njk 
title: "Bornes théorique de la complexité du problème du tri"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons nous intéresser à la complexité du problème du tri, indépendamment de la connaissance des algorithmes.

Commençons par une remarque d'importance :

{% attention "**À retenir**" %}
Si les éléments du tableau à trier sont tous différents, les permutations de celui-ci sont toutes différentes et une seule est la solution au problème "tri".
{% endattention %}

Par exemple, pour un tableau à trois éléments :

1. $[1, 2, 3]$
2. $[1, 3, 2]$
3. $[2, 1, 3]$
4. $[2, 3, 1]$
5. $[3, 1, 2]$
6. $[3, 2, 1]$

Quelque soit la forme de l'entrée (de 1 à 6), l'algorithme de tri doit rendre la forme 1 : un algorithme de tri doit pouvoir distinguer parmi toutes les permutations d'un tableau où toutes ses valeurs sont deux à deux différentes.

{% attention "**À retenir**" %}

Comme il y a $n!$  permutations différentes pour un tableau de taille $n$ dont les éléments sont deux à deux différents, tout algorithme de tri doit pouvoir distinguer parmi $n!$ choix.

{% endattention %}

## Borne maximum

Une première borne — irréaliste — serait de calculer toutes les $n!$ permutations d'un tableau et de vérifier pour chacune d'elle si elle est triée (avec notre algorithme de reconnaissance). En ne tenant pas en compte  l'algorithme permettant de trouver toutes les permutations d'un tableau, il faudrait déjà $\mathcal{O}(n! \cdot n)$ opérations pour toutes les tester (ce qui est trop).

Il existe des algorithmes simple de tri que vous avez sûrement déjà vu au cours de votre vie, comme par exemple [le tri par selection](./#tri-sélection){.interne} que l'on analysera ci-après. Sa complexité étant en $\mathcal{O}(n^2)$ opérations avec $n$ la taille du tableau à trier, on en conclut :

{% note "**Proposition**" %}
Une borne maximum de la complexité du problème du tri d'un tableau à $n$ éléments est $\mathcal{O}(n^2)$.
{% endnote %}

## Borne minimum

En utilisant la propriété [du nombre de cas à distinguer](../../complexité-problème/#n-test-2n){.interne} vue dans la complexité du problème de la *"recherche ordonnée"*, on en déduit que comme tout algorithme de tri d'un tableau à $n$ élément doit distinguer parmi $n!$ cas :

{% note "**{% note "**Proposition**" %}
**" %}
Une borne minimum de la complexité du problème du tri d'un tableau à $n$ éléments est $\Omega(\ln(n!))$.
{% endnote %}

Pour expliciter ce qu'est $\ln(n!)$, utilisons la propriété suivante :

{% note "**Proposition**" %}
Toute fonction en $\ln(n!) = \Theta(n\ln(n))$
{% endnote %}
{% details "preuve", "open" %}

On a :
<div>
$$
\begin{array}{rcccl}
n \cdot (n-1) \cdot \ ...\ \cdot \frac{n}{2} & \leq & n \cdot (n-1) \ ... \ \cdot 1 &\leq& n \cdot \ ...\  \cdot n \\
\frac{n}{2} \cdot \frac{n}{2} \cdot \ ...\ \cdot \frac{n}{2} & \leq & n \cdot (n-1) \ ... \ \cdot 1 &\leq& n \cdot \ ...\  \cdot n \\
\end{array}
$$
</div>

Ce qui nous donne l'encadrement :

<div>
$$
\begin{array}{rcccl}
 (\frac{n}{2})^{\frac{n}{2}} & \leq & n! &\leq& (n)^{n} \\
\end{array}
$$
</div>

Qui devient en passant au $\ln$ :

<div>
$$
\begin{array}{rcccl}
\ln((\frac{n}{2})^{\frac{n}{2}}) & \leq & \ln(n!) &\leq& \ln(n^n) \\
\frac{n}{2}\ln(\frac{n}{2}) &\leq& \ln(n!) &\leq& n\ln(n)
\end{array}
$$
</div>

Poursuivons en remarquant que puisque  $\ln(a\cdot x) = \ln(a) + \ln(x)$, on a $\ln(ax) \geq a\cdot \ln(x)$ si $\frac{\ln(a)}{a-1} \geq \ln(x)$, et donc $\ln(n/2) \geq \ln(n)/2$ pour $n \geq 2\ln(2)$. On combine cette inégalité à notre encadrement précédent pour trouver (pour $n \geq 2\ln(2)$) :

$$
\frac{n}{2}(\frac{1}{2}(\ln(n))) \leq \ln(n!) \leq n\ln(n)
$$

Ce qui se dérive directement, pour $n \geq 4 \geq 2\ln(2)$, en :

$$\frac{1}{4} \leq \frac{\ln(n!)}{n\ln(n)} \leq 1$$

Enfin, on peut montrer les équivalences de $\mathcal{O}$ :

- si $g(n)$ est en $\mathcal{O}(\ln(n!))$ il existe $N_0$ et $C$ tel que : $g(n) < C \cdot \ln(n!)$ pour n > $N_0$. On a donc $g(n) < C \cdot \ln(n!) < C \cdot n\ln(n)$ : $g(n)$ est en $\mathcal{O}(n\ln(n))$.
- si $g(n)$ est en $\mathcal{O}(n\ln(n))$ il existe $N_0$ et $C$ tel que : $g(n) < C \cdot n\ln(n)$ pour n > $N_0$. Pour $N_1 = \max(N_0, 4)$ on a donc $g(n) < C \cdot \ln(n!) < C \cdot 4 \cdot \ln(n!)$ : $g(n)$ est en $\mathcal{O}(\ln(n!))$.

{% enddetails %}

Cet equivalence nous donne finalement la borne minimum courante :

{% note "**Proposition**" %}
Tout algorithme de tri d'une liste à $n$ éléments est en $\Omega(n\ln(n))$ opérations.
{% endnote %}

Une borne min du problème du *"tri"* est donc $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau en entrée. La partie suivante montrera qu'il existe des algorithmes de tri complexité $\mathcal{O}(n\ln(n))$ ([le tri fusion par exemple](../algorithme-fusion/){.interne}), on en conclut donc un peu en avance que :


<div id="complexité-problème"></div>
{% note "**Proposition**" %}
La complexité du problème du tri est n $\Theta(n\ln(n))$ opérations.
{% endnote %}
