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
- <https://www-sop.inria.fr/members/Frederic.Havet/Cours/proba-notes.pdf>

{% endlien %}

Comme on est en informatique, on va considérer des ensembles finis ou au pire dénombrable.

## Probabilités

### Définitions

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

Le couple $(\Omega, \mathbb{P})$ est appelé **_espace probabilité_**.
{% endnote %}
{% info %}
Notez que la définition dénombrable généralise bien la définition du cas fini puisqu'une suite finie $(A_n)_{1\leq n \leq N}$ d'éléments deux à deux disjoints peut s'écrire comme une suite infinie où $A_n =\emptyset$ pour tout $n > N$.
{% endinfo %}

> TBD exemple avec P(n) = 1/(n + 1)^2 et P(0) = 0

On a les propriétés suivantes :

{% note "**Proposition**" %}

On a :

- $\mathbb{P}(\Omega) = 1$
- $\mathbb{P}(\Omega\backslash A) = 1 - \mathbb{P}(A)$
- $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$
- $A$ et $B$ sont **_indépendants_** si $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

{% endnote %}

> TBD reprendre les propositions de : <http://vonbuhren.free.fr/Prepa/TSI2/probabilites_univers_denombrable_cours.pdf>

### Conditionnement

{% note "**Définition**" %}

Soit $\mathbb{P}$ une probabilité sur $\Omega$. La **_probabilité de $B$ sachant $A$_** est définie (pour $A, B \subseteq \Omega$) telle que :

<div>
$$
\mathbb{P}_A(B) = \mathbb{P}(B \vert A)\coloneqq \frac{\mathbb{P}(B \cap A)}{\mathbb{P}(A)}
$$
</div>

{% endnote %}

Cette probabilité décrit le fait que l'on ne considère que les évènements où $A$ est réalisé. C'est bien une probabilité :

{% note "**Proposition**" %}

Soit un univers $(\Omega, P)$ un espace probabilisé.

Pour tout $A \subseteq \Omega$ la fonction $\mathbb{P}_A : \mathcal{P}(\Omega) \rightarrow [0, 1]$.

{% endnote %}
{% details "preuve", "open" %}

clair.

{% enddetails %}

> TBD thm 4.8 et 4.9 de "probabilité pour les non probabilistes

## Variables aléatoires

Les événements se manifestent via des **_variable aléatoire_**. L'univers étant souvent soit inconnu soit trop compliqué pour en tirer quoi que ce soit d'utile.

> TBD : deux trucs qui bougent avec le "sachant B"

### Définitions et notations

{% note "**Définition**" %}

Une **_variable aléatoire_** $X$ est une fonction $X : \Omega \rightarrow \mathcal{U}$ ($U$ quelconque a priori) où $(\Omega, \mathbb{P})$ est un espace probabilisé. On note alors :

- $\mathbb{P}\\{X = u\\} \coloneqq \mathbb{P}(X^{-1}(u))$
- $\mathbb{P}\\{X \in U\\} \coloneqq \mathbb{P}(X^{-1}(U))$, $u \subseteq \mathcal{U}$

On dira que $X(\omega) = u$ est une **_réalisation_** de la variable aléatoire $X$. Cette réalisation est de probabilité $\mathbb{P}\\{X = u\\}$.
{% endnote %}
{% attention %}
Ne confondez pas la variable aléatoire et ses réalisations.
{% endattention %}

Comme une variable aléatoire est indissociable de sa mesure de probabilité associée et que l'espace $\Omega$ sous-jacent est très souvent inutile (et inconnu), on utilisera souvent la notation suivante :

{% note "**Définition**" %}

On définit :

<div>
$$
u \xleftarrow{\mathbb{P}} \mathcal{U}
$$
</div>

Comme étant une variable aléatoire :

- prenant ses valeurs dans $\mathcal{U}$
- suivant la loi de probabilité $\mathbb{P}$

{% endnote %}

Ce qui nous permet d'écrire de façon synthétique :

{% note "**Définition**" %}

<div>
$$
{\Pr}_{u \xleftarrow{\mathbb{P}} \mathcal{U}}[u = x] \coloneqq \mathbb{P}\{(u \xleftarrow{\mathbb{P}} \mathcal{U})^{-1}(x)\}
$$
</div>

{% endnote %}

S'il n'y a pas ambiguïté, on se permettra même d'écrire :

- ${\Pr}[u = x]$ si l'on s'intéresse aux réalisations de la variable aléatoire $X$
- ${\Pr}[X = x]$ si l'on veut expliciter la variable aléatoire $X$

### Uniformité et Indépendance

{% note "**Définition**" %}

Une variable aléatoire ets dite **_uniforme_** si $\Pr[X = x]$ est une constante pour tout $x \in U$. On la notera $u \xleftarrow{R} \mathcal{U}$.

{% endnote %}

{% note "**Définition**" %}

Deux variables aléatoires $X : \Omega \rightarrow \mathcal{U}$ et $Y : \Omega \rightarrow \mathcal{U}'$ sur le même espace probabilisé sont **_indépendantes_** si les évènements qui les dirigent sont eux mêmes indépendants, c'est à dire que $X^{-1}(U) \cap Y^{-1}(U') = \varnothing$ quelques soient $U \subseteq \mathcal{U}$ et $V \subseteq \mathcal{U}'$.
{% endnote %}

Comme on a rarement accès à l'espace probabilisé sous-jacent, ce qui va nous intéresser lorsque deux variables aléatoires sont indépendantes c'est la conséquence suivante (triviale) :

{% note "**Proposition**" %}
Pour deux variables aléatoires indépendantes $X$ et $Y$ prenant leurs valeurs dans $\mathcal{U}$ et $\mathcal{U}'$ respectivement, on a quelques soient $U \subseteq \mathcal{U}$ et $V \subseteq \mathcal{U}'$ :

<div>
$$
\Pr[X \in V, Y \in V'] = \Pr[X \in V] \cdot \Pr[Y \in V']
$$
</div>
{% endnote %}

### Espérance

> TBD espérance $\mathbb{E}[X]$ (vous verrez aussi $\mathbb{E}(X)$ ou même $\mathbb{E}X$. Nous on utilise les crochet pour rester cohérente avec notre notation pour les probabilités de variables aléatoires)
>
> - linéarité de l'espérance
> - il existe 1 qui vaut l'espérance

### Exemple

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

## Fonction génératrice

> TBD utiliser les fct génératrice pour la combinatoire.
>
## Méthode probabiliste

- simple
- avec alteration
- lemme local de Lova

> TBD trouver un exemple pas graphe.