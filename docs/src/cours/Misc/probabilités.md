---
layout: layout/post.njk

title: Probabilités discrètes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [proba discrete](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability)
- [Probabilités pour les non-probabilistes](https://www.amazon.fr/Probabilit%C3%A9s-pour-probabilistes-Walter-Appel/dp/2351412982)

{% endlien %}

Comme on est en informatique, on va considérer des ensembles finis ou au pire dénombrable.

## Probabilités

{% note "**Définition**" %}

- **_univers_** : $\Omega$ un ensemble fini.
- **_probabilité_** : $p : \Omega \rightarrow [0, 1]$ telle que $\sum_{x \in \Omega} p(x) = 1$.

{% endnote %}

La probabilité $p$ est dite **_uniforme_** si $p(x) = \frac{1}{\vert \Omega \vert}$ pour tout $x \in \Omega$. Par défaut, toutes les probabilités seront uniforme.

On étant la notion de probabilité aux ensembles :

{% note "**Définition**" %}

Un **_évènement_** $A \subseteq \Omega$ est de **_probabilité_** $\mathbb{P}(A)$ définie telle que :

<div>
$$
\mathbb{P}(A) \coloneqq \sum_{x \in A}p(x)
$$
</div>

{% endnote %}

Cette définition se généralise simplement aux ensembles dénombrables (ce qui est réaliste (à défaut d'être réel) en informatique) :

{% note "**Définition**" %}

- **_univers_** : $\Omega$ un ensemble dénombrable.
- **_probabilité_** : $\mathbb{P} : \mathcal{P}(\Omega) \rightarrow [0, 1]$ telle que :
  - $\mathbb{P}(\Omega) = 1$.
  - Pour toute suite $(A_n)_{n\in \mathbb{N}}$ d'éléments deux à deux disjoints de $\mathcal{P}(\Omega)$, on a : $\mathbb{P}(\cup_n A_n) = \sum_n \mathbb{P}(A_n)$

{% endnote %}
{% info %}
Notez que la définition dénombrable généralise bien la définition du cas fini puisqu'une suite finie $(A_n)_{1\leq n \leq N}$ d'éléments deux à deux disjoints peut s'écrire comme une suite infinie où $A_n =\emptyset$ pour tout $n > N$.
{% endinfo %}

> TBD exemple avec P(n) = 1/(n + 1)^2 et P(0) = 0

On a les propriétés suivantes :

{% note "**Proposition**" %}
> TBD reprendre les propositions de : <http://vonbuhren.free.fr/Prepa/TSI2/probabilites_univers_denombrable_cours.pdf>

On a :

- $\mathbb{P}(\Omega) = 1$
- $\mathbb{P}(\Omega\backslash A) = 1 - \mathbb{P}(A)$
- $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$
- $A$ et $B$ sont **_indépendants_** si $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

{% endnote %}

## Variables aléatoires

Les événements se manifestent via des **_variable aléatoire_**. L'univers étant souvent soit inconnu soit trop compliqué pour en tirer quoi que ce soit d'utile.

{% note "**Définition**" %}

Une **_variable aléatoire_** $X$ est une fonction $X : \Omega \rightarrow U$ ($U$ quelconque a priori). On note alors :

- $\mathbb{P}\\{X = v\\} \coloneqq \mathbb{P}(X^{-1}(v))$
- $\mathbb{P}\\{X \in V\\} \coloneqq \mathbb{P}(X^{-1}(V))$, $V \subseteq \Omega$

{% endnote %}

Pour bien faire la différence entre les deux notions, on utilisera la notation :

{% note "**Définition**" %}

<div>
$$
{\Pr}_{\mathbb{P}}[X] \coloneqq \mathbb{P}\{X\}
$$
</div>

S'il n'y a pas ambiguïté, on omettra la probabilité $p$ et on écrira $\Pr[X]$ à la place de $\Pr_{\mathbb{P}}[X]$. On peut complètement ignorer l'univers sous-jacent et ne travailler qu'avec les variables aléatoires.

{% endnote %}

Une variable aléatoire sera dite **_uniforme_** si $\Pr[X = x]$ est une constante pour tout $x \in U$. On la notera $X \xleftarrow{R} \mathcal{U}$

Deux variables aléatoires $X : \Omega \rightarrow U$ et $Y : \Omega \rightarrow U'$ sont **_indépendantes_** si les évènements qui les dirigent sont eux mêmes indépendants :
$\Pr[X \in V, Y \in V'] = \Pr[X \in V] \cdot \Pr[Y \in V']$.

En sécurité, on aura typiquement :

- $\Omega = \\{0, 1\\}^n$ l'ensemble des clés
- probabilité uniforme
- la variable aléatoire associée est le chiffre : $E(k, m)$

Ou, si l'on s'intéresse à un couple $(m_0, m_1)$ de deux mots de longueurs $L$ :

- l'univers est tout ce qui arrive : $\Omega = \\{0, 1\\}^L \times \\{0, 1\\}^L$ et correspond aux deux mots
- probabilité uniforme
- les variables aléatoires :
  - $M_0 : \Omega \rightarrow \\{0, 1\\}^L$
  - $M_1 : \Omega \rightarrow \\{0, 1\\}^L$

> TBD : deux trucs qui bougent avec le "sachant B"

> TBD espérance
> - linéarité de l'espérance
> - il existe 1 qui vaut l'espérance

## Fonction génératrice

> TBD utiliser les fct génératrice pour la combinatoire.
>
## Méthode probabiliste

- simple
- avec alteration
- lemme local de Lova

> TBD trouver un exemple pas graphe.