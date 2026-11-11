---
layout: layout/post.njk

title: Probabilités discrètes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- 
> TBD <https://mathoverflow.net/questions/358184/probability-of-a-random-variable-greater-than-its-expected-value>{.externe}
> chernoff bound, reverse markov inequality,
> Paley–Zygmund inequality <https://en.wikipedia.org/wiki/Paley%E2%80%93Zygmund_inequality>{.externe}
> Chebyshev inequality <https://en.wikipedia.org/wiki/Chebyshev%27s_inequality>{.externe}
> <https://www.youtube.com/watch?v=lKkyxtzz4Uo>{.externe}
> thm centrale limite : <https://www.youtube.com/watch?v=FGIxzMGE01A>{.externe} et <https://www.youtube.com/watch?v=axA1-yR-KDw>{.externe}
> convergences : <https://www.youtube.com/watch?v=KedtZmQ5GyM>{.externe} et <https://www.youtube.com/watch?v=UmSSrXr4ixM&list=PLl7EPYrsru4_usb1yKNUr8wtQGcVP9DZ6>{.externe} 
> 
-->

{% lien %}

- [proba discrete](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability){.externe}
- [Probabilités pour les non-probabilistes](https://www.amazon.fr/Probabilit%C3%A9s-pour-probabilistes-Walter-Appel/dp/2351412982){.externe}
- <https://www-sop.inria.fr/members/Frederic.Havet/Cours/proba-notes.pdf>{.externe}
- <http://vonbuhren.free.fr/Prepa/TSI2/probabilites_univers_denombrable_cours.pdf>{.externe}

{% endlien %}

Comme on est en informatique, on va considérer des ensembles finis ou au pire dénombrables.

## Probabilités

### Définitions

{% definition %}

- **_univers_** : $\Omega$ un ensemble fini.
- **_probabilité_** : $p : \Omega \rightarrow [0, 1]$ telle que $\sum\limits_{x \in \Omega} p(x) = 1$.

La probabilité $p$ est dite **_uniforme_** si $p(x) = \frac{1}{\vert \Omega \vert}$ pour tout $x \in \Omega$.
{% enddefinition %}

Par défaut, toutes les probabilités seront uniformes.

On étend la notion de probabilité aux ensembles :

{% definition %}

On définit la **_probabilité_** $\mathbb{P}(A)$ d'un **_évènement_** $A \subseteq \Omega$ comme étant :

<div>
$$
\mathbb{P}(A) \coloneqq \sum_{x \in A}p(x)
$$
</div>

{% enddefinition %}

Cette définition se généralise simplement aux ensembles dénombrables (ce qui est réaliste, à défaut d'être réel, en informatique) :

{% definition %}

- **_univers_** : $\Omega$ un ensemble dénombrable.
- **_probabilité_** : $\mathbb{P} : \mathcal{P}(\Omega) \rightarrow [0, 1]$ telle que :
  - $\mathbb{P}(\Omega) = 1$.
  - Pour toute suite $(A_n)_{n\in \mathbb{N}}$ d'éléments deux à deux disjoints de $\mathcal{P}(\Omega)$, on a : $\mathbb{P}(\bigcup\limits_n A_n) = \sum\limits_n \mathbb{P}(A_n)$

Le couple $(\Omega, \mathbb{P})$ est appelé **_espace probabilisé_**. On dit aussi que $\mathbb{P}$ est une probabilité sur $\Omega$.
{% enddefinition %}
Notez que la définition dénombrable généralise bien la définition du cas fini puisqu'une suite finie $(A_n)_{1\leq n \leq N}$ d'éléments deux à deux disjoints peut s'écrire comme une suite infinie où $A_n =\emptyset$ pour tout $n > N$.

Un exemple d'espace probabilisé pourrait être $(\mathbb{N}, \mathbb{P})$ avec $\mathbb{P}$ défini uniquement sur les entiers : $\mathbb{P}(\\{n\\}) = \frac{n}{2^{n+1}}$. On a alors $\mathbb{P}(A) = \sum_{x\in A} \mathbb{P}(\\{x\\})$. Cet exemple montre que, comme dans le cas fini, on n'a besoin que de peu d'évènements pour inférer toute la probabilité. Ce ne sont plus forcément des singletons mais des partitions de $\Omega$ que l'on appelle **systèmes complets d'évènements** :

{% definition %}

Soit $\Omega$ un ensemble dénombrable. Un **système complet d'évènements** est une suite $(A_n)_{n\in \mathbb{N}}$ d'éléments deux à deux disjoints de $\mathcal{P}(\Omega)$ telle que $\bigcup_n A_n = \Omega$.

{% enddefinition %}

On a les propriétés suivantes dont les preuves sont triviales :

{% note "**Proposition**" %}

Pour tout espace probabilisé $(\Omega, \mathbb{P})$ on a :

- $\mathbb{P}(\varnothing) = 0$
- $\mathbb{P}(\Omega) = 1$
- $\mathbb{P}(\Omega\backslash A) = 1 - \mathbb{P}(A)$
- $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$

{% endnote %}

### Indépendance

Une notion que l'on utilisera souvent est **_la notion d'indépendance entre 2 ensembles_**. L'ensemble $A$ est dit indépendant de l'ensemble $B$ si la probabilité d'être dans $A$ pour un élément de l'univers ($\frac{\mathbb{P}(A)}{\mathbb{P}(\Omega)}$) est la même que la probabilité d'être dans $A$ pour les éléments de $B$ ($\frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$). Comme $\mathbb{P}(\Omega) = 1$ on utilise la définition suivante :

{% definition %}

Soit $\mathbb{P}$ une probabilité sur $\Omega$. Les ensembles $A$ et $B$ sont dits **_indépendants_** si :

<div>
$$
\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)
$$
</div>

{% enddefinition %}

### Conditionnement

Le pendant de l'indépendance est le conditionnement où on ne considère que les probabilités où un évènement donné est réalisé. Cela permet de répondre aux questions de type _"quelle est la probabilité de $A$ sachant que $B$ est vrai ?"_. On peut alors définir la notion ainsi :

{% definition %}

Soit $\mathbb{P}$ une probabilité sur $\Omega$ et $B$ un évènement tel que $\mathbb{P}(B) > 0$. La **_probabilité de $A$ sachant $B$_** est définie telle que :

<div>
$$
\mathbb{P}_B(A) \coloneqq \mathbb{P}(A \vert B)\coloneqq \frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}
$$
</div>

{% enddefinition %}

C'est bien une probabilité :

{% note "**Proposition**" %}

Si $(\Omega, \mathbb{P})$ est un espace probabilisé alors $\mathbb{P}_B$ est une probabilité sur $\Omega$ quel que soit $B \subseteq \Omega$ tel que $\mathbb{P}(B) > 0$.

{% endnote %}
{% details "preuve", "open" %}

- $\mathbb{P}_B(\Omega) = \frac{\mathbb{P}(B\cap \Omega)}{\mathbb{P}(B)} = 1$.
- Pour toute suite $(A_n)$ d'éléments deux à deux disjoints de $\mathcal{P}(\Omega)$ la restriction de la suite $(A^\prime_n)_{n\in \mathbb{N}}$ définie telle que $A^\prime_n = A_n \cap B$ est également d'éléments deux à deux disjoints. De là : $\mathbb{P}_B(\bigcup\limits_n A_n) = \frac{\mathbb{P}((\bigcup\limits_n A_n) \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{P}(\bigcup\limits_n (A_n \cap B))}{\mathbb{P}(B)} = \frac{\mathbb{P}(\bigcup\limits_n A^\prime_n)}{\mathbb{P}(B)} = \sum\limits_n \frac{\mathbb{P}(A^\prime_n)}{\mathbb{P}(B)} = \sum\limits_n \frac{\mathbb{P}(A_n \cap B)}{\mathbb{P}(B)} = \sum\limits_n \mathbb{P}_B(A_n)$

{% enddetails %}

On a alors les deux propositions suivantes qui vont servir de cadre à l'utilisation du conditionnement :

{% note "**Proposition (Formule des probabilités totales)**" %}

Si $(\Omega, \mathbb{P})$ est un espace probabilisé et $(B_n)$ un système complet d'évènements, on a pour tout évènement $A$ :

<div>
$$
\mathbb{P}(A) = \sum\limits_n(\mathbb{P}(B_n)\cdot \mathbb{P}(A \mid B_n))
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

<div>
$$
\mathbb{P}(A) = \mathbb{P}(A \cap \Omega) = \mathbb{P}(A \cap (\bigcup_n B_n)) = \mathbb{P}( \bigcup_n (A \cap B_n)) = \sum\limits_n\mathbb{P}(A \cap B_n) = \sum\limits_n(\mathbb{P}(B_n)\cdot \mathbb{P}(A \mid B_n))
$$
</div>

{% enddetails %}

{% note "**Proposition (Théorème de Bayes)**" %}

Si $(\Omega, \mathbb{P})$ est un espace probabilisé, pour tous évènements $A$ et $B$ de probabilités non nulles on a :

<div>
$$
\mathbb{P}(A \mid B) =\frac{\mathbb{P}(A)\cdot \mathbb{P}(B \mid A)}{\mathbb{P}(B)}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

Par définition :
<div>
$$
\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B \mid A) = \mathbb{P}(B) \cdot \mathbb{P}(A \mid B)
$$
</div>

{% enddetails %}

## Variables aléatoires

Les événements se manifestent via des **_variables aléatoires_**. L'univers étant souvent soit inconnu soit trop compliqué pour en tirer quoi que ce soit d'utile.

### Définitions et notations

{% definition %}

Une **_variable aléatoire_** $X$ est une fonction $X : \Omega \rightarrow \mathcal{U}$ ($\mathcal{U}$ quelconque a priori) où $(\Omega, \mathbb{P})$ est un espace probabilisé. On note alors :

- ${\Pr}[X = u] \coloneqq \mathbb{P}(X^{-1}(\\{u\\}))$
- $\Pr[X \in U] \coloneqq \mathbb{P}(X^{-1}(U))$,
- $\Pr[X \in U \\, , \\, Y \in V] \coloneqq \mathbb{P}(X^{-1}(U) \cap Y^{-1}(V))$ (les deux variables aléatoires sont sur le même espace probabilisé)

On dira que $X(\omega) = x$ est une **_réalisation_** de la variable aléatoire $X$. Cette réalisation est de probabilité $\Pr[X = u]$.
{% enddefinition %}
{% attention %}
Ne confondez pas la variable aléatoire et ses réalisations.
{% endattention %}

Comme une variable aléatoire est indissociable de sa mesure de probabilité associée et que l'espace $\Omega$ sous-jacent est très souvent inutile (et inconnu), on l'omettra la plupart du temps.

{% retenir %}
S'il n'y a pas ambiguïté, on écrira :

- ${\Pr}[x = k]$ si l'on s'intéresse aux réalisations $X(\omega) = x$ de la variable aléatoire $X$
- ${\Pr}[X = k]$ si l'on veut expliciter la variable aléatoire $X$
 
{% endretenir %}

Enfin, pour nos cas d'application on utilisera toujours ces types de variables aléatoires :

{% definition %}
Une variable aléatoire est dite :
- **_réelle_** si elle prend ses valeurs dans $\mathbb{R}$
- **_simple_** si elle prend un nombre fini de valeurs,
- **_discrète_** si elle prend au plus un nombre dénombrable de valeurs.
{% enddefinition %}

{% retenir %}
Lorsque l'on parlera de :

- **variable aléatoire** dans le cours, elle sera **réelle et simple**. 
- **variable aléatoire discrète**, elle sera de plus **réelle**.

{% endretenir %}

Les variables aléatoires discrètes s'écrivent trivialement comme une somme d'[indicatrices](https://fr.wikipedia.org/wiki/Fonction_caract%C3%A9ristique_(th%C3%A9orie_des_ensembles)) :


{% definition %}
La fonction $\mathbb{1}_{A}$ est appelée **_indicatrice_**, **_fonction indicatrice_** ou encore **_fonction caractéristique_** et est définie telle que :

<div>
$$
\mathbb{1}_{A}(x) = 
\begin{cases}
1 & \text{si } x \in A\\
0 & \text{sinon}
\end{cases}
$$
</div>
{% enddefinition %}

{% note "**Proposition**" %}
Soit $X$ une variable aléatoire discrète de valeurs $(x_i)$ ($i \in \mathbb{N}$). On peut l'écrire sous la forme :

<div>
$$
X = \sum\limits_i x_i \mathbb{1}_{\{X = x_i\}}
$$
</div>

Réciproquement, si $(A_i)$ est un système complet d'évènements d'un espace probabilisé $(\Omega, \mathbb{P})$, et $(x_i)$ une suite dénombrable de réels (pas forcément distincts) alors la fonction :

<div>
$$
X = \sum\limits_i x_i \mathbb{1}_{A_i}
$$
</div>

est une variable aléatoire discrète.
{% endnote %}

Nos notations permettent d'étendre les définitions des évènements aux variables aléatoires.

### Conditionnement 

{% definition %}

Pour deux expressions $A$ et $B$ on définit le **_conditionnement_** comme étant :
<div>
$$
{\Pr}[A \,\vert\, B] \coloneqq \frac{\Pr[A\, , \, B]}{\Pr[B]}
$$
</div>

{% enddefinition %}

### Uniformité et Indépendance

{% definition %}

Une variable aléatoire est dite **_uniforme_** si $\Pr[X = x]$ est une constante pour tout $x \in U$. On la notera $u \xleftarrow{U} \mathcal{U}$.

{% enddefinition %}

{% definition %}

Deux variables aléatoires $X : \Omega \rightarrow \mathcal{U}$ et $Y : \Omega \rightarrow \mathcal{U}'$ sur le même espace probabilisé sont **_indépendantes_** si les évènements qui les dirigent sont eux-mêmes indépendants, c'est-à-dire que $\mathbb{P}(X^{-1}(U) \cap Y^{-1}(V)) = \mathbb{P}(X^{-1}(U)) \cdot \mathbb{P}(Y^{-1}(V))$ quels que soient $U \subseteq \mathcal{U}$ et $V \subseteq \mathcal{U}'$.
{% enddefinition %}

Comme on a rarement accès à l'espace probabilisé sous-jacent, ce qui va nous intéresser lorsque deux variables aléatoires sont indépendantes c'est la conséquence suivante (triviale) :

{% note "**Proposition**" %}
Pour deux variables aléatoires indépendantes $X$ et $Y$ prenant leurs valeurs dans $\mathcal{U}$ et $\mathcal{U}'$ respectivement, on a quels que soient $U \subseteq \mathcal{U}$ et $V \subseteq \mathcal{U}'$ :

<div>
$$
\Pr[X \in U, Y \in V] = \Pr[X \in U] \cdot \Pr[Y \in V]
$$
</div>
{% endnote %}

### Exemple : en sécurité

<!-- TBD 

utile ? 
sûrement à étoffer 

-->

En sécurité on utilisera souvent la notation suivante pour expliciter les variables aléatoires :

{% definition %}

On définit $u \xleftarrow{\mathbb{P}} \mathcal{U}$ comme étant une variable aléatoire :

- prenant ses valeurs dans $\mathcal{U}$
- suivant la loi de probabilité $\mathbb{P}$

{% enddefinition %}

Les lois de probabilités pouvant changer on les précisera si nécessaires en utilisant la notation suivante :

{% definition %}

<div>
$$
{\Pr}_{u \xleftarrow{\mathbb{P}} \mathcal{U}}[u = x] \coloneqq \Pr[(u \xleftarrow{\mathbb{P}} \mathcal{U})^{-1} = x]
$$
</div>

{% enddefinition %}

On aura typiquement :

- $\Omega = \\{0, 1\\}^n$ l'ensemble des clés
- probabilité uniforme
- la variable aléatoire associée est le chiffre : $E(k, m)$

Ou, si l'on s'intéresse à un couple $(m_0, m_1)$ de deux mots de longueur $L$ :

- l'univers est tout ce qui arrive : $\Omega = \\{0, 1\\}^L \times \\{0, 1\\}^L$ et correspond aux deux mots
- probabilité uniforme
- les variables aléatoires :
  - $M_0 : \Omega \rightarrow \\{0, 1\\}^L$
  - $M_1 : \Omega \rightarrow \\{0, 1\\}^L$

## <span id="espérance">Espérance

[La notion d'espérance](https://fr.wikipedia.org/wiki/Esp%C3%A9rance_math%C3%A9matique){.externe} en probabilité généralise la notion de moyenne.

{% definition %}

Soit $X$ une variable aléatoire de valeurs $x_i$ ($1\leq i \leq p$). **_L'espérance de $X$_** est définie telle que :

<div>
$$
\mathbb{E}[X] = \sum\limits_{i=1}^px_i\cdot \Pr[X=x_i]
$$
</div>

{% enddefinition %}

Cette définition se généralise _mutatis mutandis_ aux variables aléatoires discrètes si la somme converge :

{% definition %}

Soit $X$ une variable aléatoire discrète de valeurs $(x_i)$ ($i \in \mathbb{N}$). 

Si $\sum\limits_{i=0}^{+\infty} x_i\cdot \Pr[X=x_i]$ est définie, on l'appelle **_espérance de $X$_** et on la note $\mathbb{E}[X]$.

{% enddefinition %}

Une conséquence immédiate, qui généralise un résultat similaire pour la moyenne, mais que l'on utilise souvent lorsque l'on fait des preuves par la méthode probabiliste est :

{% note "**Proposition**" %}
Pour toute variable aléatoire $X$ (réelle et simple), si $\mathbb{E}[X] = M$, alors il existe une valeur de $X$ plus grande ou égale à $M$.
{% endnote %}
{% details "preuve", "open" %}
Si toutes les valeurs de $X$ étaient strictement plus petites que $M$, on aurait :

<div>
$$
\mathbb{E}[X] = \sum\limits_{i=1}^px_i\cdot \Pr[X=x_i] < \sum\limits_{i=1}^pM\cdot \Pr[X=x_i] = M \cdot \sum\limits_{i=1}^p \Pr[X=x_i] = M
$$
</div>

ce qui est impossible.

{% enddetails %}

### Partitionnement de l'espace

Les deux propositions suivantes sont très utilisées :

{% note "**Proposition**" %}
Soit $X$ une variable aléatoire (discrète admettant une espérance) que l'on écrit sous la forme $X = \sum_i a_i\mathbb{1}_{A_i}$ (les $a_i$ ne sont pas forcément distincts) où $(A_i)$ est une partition (système complet d'évènements) de $\Omega$. Alors :

<div>
$$
\mathbb{E}[X] = \sum\limits_{i} (a_i\cdot \mathbb{P}(A_i))
$$
</div>


{% endnote %}
{% details "preuve", "open" %}
Si la partition $(A_i)$ est finie ou dénombrable on peut rassembler ceux qui ont même valeur pour former une partition $(A'_i)$ où toutes les valeurs sont distinctes.

{% enddetails %}

Une variation de la proposition précédente pour des variables aléatoires prenant des valeurs entières, très utilisée en pratique :

{% note "**Proposition**" %}
Soit $X$ une variable aléatoire (discrète admettant une espérance) prenant ses valeurs dans $\mathbb{N}$. On a :

<div>
$$
\mathbb{E}[X] = \sum\limits_{i \geq 0} i \cdot \Pr[X = i] = \sum\limits_{i \geq 1}\Pr[X \geq i]
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

La première égalité est claire puisque les $X^{-1}(\\{ i \\})$ forment une partition de $\Omega$. Pour la seconde, on remarque que $i \cdot \Pr[X = i] = \sum_{1 \leq k \leq i} \Pr[X = i]$, et on échange les sommes : $\sum_{i \geq 0} \sum_{1 \leq k \leq i} \Pr[X = i] = \sum_{k \geq 1} \sum_{i \geq k} \Pr[X = i] = \sum_{k \geq 1}\Pr[X \geq k]$.

{% enddetails %}


### Linéarité de l'espérance

Sûrement la plus utilisée des propriétés de l'espérance. On ne démontrera ici que le cas qui nous est utile, à savoir pour les variables aléatoires simples, mais il se généralise au cas discret moyennant quelques résultats de convergence de séries infinies que nous ne verrons pas dans ce cours.

{% note "**Proposition**" %}
Soient $X$ et $Y$ deux variables aléatoires. On a :
<div>
$$
\mathbb{E}[\alpha \cdot X + \beta\cdot Y] = \alpha \cdot \mathbb{E}[X] +\beta \cdot \mathbb{E}[Y]
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

On note $X$ et $Y$ avec leurs fonctions indicatrices :

- $X = \sum\limits_i x_i \mathbb{1}_{\\{X = x_i\\}}$
- $Y = \sum\limits_j y_j \mathbb{1}_{\\{Y = y_j\\}}$

On a alors que la variable aléatoire :

<div>
$$
\alpha \cdot X = \sum\limits_i (\alpha\cdot x_i) \mathbb{1}_{\{X = x_i\}}
$$
</div>

est telle que :

<div>
$$
\mathbb{E}[\alpha \cdot X] = \alpha \cdot \mathbb{E}[X]
$$
</div>

Il nous reste à montrer que pour deux variables aléatoires $X$ et $Y$ telles que :

- $X = \sum\limits_i x_i \mathbb{1}_{\\{X = x_i\\}}$
- $Y = \sum\limits_j y_j \mathbb{1}_{\\{Y = y_j\\}}$

On a bien $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ pour conclure.

Pour cela on considère la variable aléatoire $X+Y = \sum\limits_{i, j} (x_i + y_j) \mathbb{1}_{\\{X = x_i\\} \cap \\{Y = y_j\\}}$. C'est bien une variable aléatoire puisque les $\\{X = x_i\\} \cap \\{Y = y_j\\}$ forment une partition de l'univers. Les $x_i + y_j$ ne sont pas forcément distincts mais on a vu juste avant que ce n'est pas grave.

On peut alors calculer son espérance :

<div>
$$
\begin{array}{lcl}
\mathbb{E}[X+Y] &=& \sum_{i, j}(x_i + y_j) \Pr[X = x_i, Y=y_j]\\
&=& \sum_{i}\sum_{j}(x_i + y_j) \Pr[X = x_i, Y=y_j]\\
&=& \sum_{i}(x_i \cdot (\sum_{j}\Pr[X = x_i, Y=y_j])) + \sum_{j}(y_j \cdot (\sum_{i}\Pr[X = x_i, Y=y_j]))\\
&=& \sum_{i}(x_i \cdot \Pr[X = x_i]) + \sum_{j}(y_j \cdot \Pr[Y=y_j])\\
&=& \mathbb{E}[X] + \mathbb{E}[Y]\\
\end{array}
$$
</div>
{% enddetails %}

<!-- TBD à ajouter lorsque l'on en aura besoin

## Fonction génératrice

> TBD utiliser les fct génératrice pour la combinatoire.

## Méthode probabiliste

- simple
- avec altération
- lemme local de Lovász

> TBD trouver un exemple pas graphe.
 
 -->