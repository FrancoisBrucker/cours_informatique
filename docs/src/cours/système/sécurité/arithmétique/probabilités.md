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
[proba discrete](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability)
{% endlien %}

Comme toujours, l'infini n'existe pas en vrai. Toutes nos probabilités seront sur des univers finis.

- ***univers*** : $\Omega$ un ensemble fini.
- ***probabilité*** : $P : \Omega \rightarrow [0, 1]$ tel que $\sum_{x \in \Omega} P(x) = 1$.

La probabilité $P$ est ***uniforme*** si $P(x) = \frac{1}{\vert \Omega \vert}$ pour tout $x \in \Omega$. Par défaut, toutes les probabilités seront uniforme.

Un ***évènement*** $A \subseteq \Omega$ est de probabilité $Pr_P[A] = \sum_{x \in A}P(x)$. On a :

- $Pr_P[U] = 1$
- $Pr_P[U\backslash A] = 1 - Pr_P[A]$
- $Pr_P[A \cup B] = Pr_P[A] + Pr_P[B] - \cdot Pr_P[A\cap B]$
- $A$ et $B$ sont ***indépendants*** si $Pr_P[A \cap B] = Pr_P[A] \cdot Pr[B]$

On omettra la probabilité $P$ et écrira $Pr[A]$ à la place de $Pr_P[A]$ s'il n'y a pas d’ambiguïté.

Les événements se manifestent via des ***variable aléatoire*** $X$, définies telle que : $X : \Omega \rightarrow U$ ($U$ quelconque a priori). On note alors :

- $Pr[X = x] = Pr[X^{-1}(v)]$
- $Pr[X \in V] = Pr[X^{-1}(V)]$ avec $V \subseteq U$

Une variable aléatoire sera dite ***uniforme*** si $Pr[X = x]$ est une constante pour tout $x \in U$. On la notera $X \xleftarrow{R} \mathcal{U}$

Deux variables aléatoires $X : \Omega \rightarrow U$ et $Y : \Omega \rightarrow U'$ sont ***indépendantes*** si les évènements qui les dirigent sont eux mêmes indépendants :
$Pr[X \in V, Y \in V'] = Pr[X \in V] \cdot Pr[Y \in V']$.

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
