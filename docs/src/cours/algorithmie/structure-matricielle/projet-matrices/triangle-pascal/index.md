---
layout: layout/post.njk

title: Triangle de Pascal

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[corrigé](./corrigé){.interne}
{% endlien %}

Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal), avec $1\leq k \leq n$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1 \text{ pour tout } n\geq 0
$$
</div>

[On a déjà vu](../../exercices-calculs-compexités/#triangle-de-pascal){.interne} l'approche récursif. Passons à l'approche itérative. 

## V1

{% faire %}
Créez un algorithme rendant une matrice triangulaire inférieure $B$ telle que $B[n][k] = \binom{n}{k}$.

Sa signature devra être :

```pseudocode
algorithme binom_matrice(n: entier) → [[entier]]:
```

Vous pourrez créer itérativement chaque ligne en utilisant la ligne créé à l'itération précédente pour créer la ligne actuelle.
{% endfaire %}

{% faire %}
Utilisez l'algorithme `binom_matrice(n: entier) → [[entier]]`{.language-} pour créer l'algorithme itératif de signature :

```pseudocode
algorithme binom(n: entier, k:entier) → entier
```

calculant $\binom{n}{k}$.

Donnez-en sa complexité spatiale et temporelle.

{% endfaire %}

## V2

Comme l'algorithme `binom_matrice(n: entier) → [[entier]]`{.language-} n'a besoin que de la ligne précédente pour créer la ligne de l'itération actuelle, on peut améliorer la complexité spatiale de l'algorithme `binom(n: entier, k:entier) → entier`{.language-} :

{% faire %}
Créez l'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} qui à partir de la liste $l= [\binom{n}{0}, \dots, \binom{n}{n}]$ rend la liste $[\binom{n+1}{0}, \dots, \binom{n+1}{n+1}]$

Donnez-en sa complexité spatiale et temporelle.

{% endfaire %}
{% faire %}
Utilisez l'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} pour améliorer la complexité spatiale de l'algorithme `binom(n: entier, k:entier) → entier`{.language-}.

{% endfaire %}

Enfin, pour calculer `binom(n: entier, k:entier) → entier`{.language-} on a pas besoin de toute la ligne de la matrice :

{% faire %}
Modifiez l'algorithme `ligne_suivante`{.language-} pour le rendre de signature `ligne_suivante(l: [entier], k: entier) → [entier]`{.language-} tel que si  $l= [\binom{n}{0}, \dots, \binom{n}{\min(k, n)}]$ rend le tableau $[\binom{n+1}{0}, \dots, \binom{n+1}{\min(k, n+1)}]$.

Utilisez le dans `binom(n: entier, k:entier) → entier`{.language-} pour que sa complexité spatiale soit en $\mathcal{O}(k)$.
{% endfaire %}

## v3

Il faut 2 tableaux de taille au plus $k$ pour faire fonctionner l'algorithme précédent. On peut faire mieux !

On va ici utiliser des listes car on va chercher à modifier et à faire grandir le paramètre d'entrée, ce qu'on ne peut pas faire avec un tableau.

{% exercice %}
En remplissant la ligne courante de droite à gauche montrez que l'on peut modifier `ligne_suivante`{.language-} pour le rendre de signature `ligne_suivante(l: Liste<entier>, k: entier) → [entier]`{.language-} telle que si $l= [\binom{n}{0}, \dots, \binom{n}{\min(k, n)}]$ en entrée, elle est modifiée en la liste $[\binom{n+1}{0}, \dots, \binom{n+1}{\min(k, n+1)}]$.

Utilisez le dans `binom(n: entier, k:entier) → entier`{.language-}.

{% endexercice %}

Cette dernière optimisation ne change pas la complexité spatiale en $\mathcal{O}$, elle ne fait que la diminuer par 2. Cette optimisation est cependant significative si $k$ est grand.
