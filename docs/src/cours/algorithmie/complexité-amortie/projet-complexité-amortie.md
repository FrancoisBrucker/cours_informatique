---
layout: layout/post.njk

title: "Projet : calculs de complexité amortie"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Entraînons nous à comprendre puis à maîtriser ce concept.

## Analyse amortie

Reprenons l'exemple de la Pile et de sa méthode `k-dépile`{.language-} utilisée dans la partie complexité amortie.

{% exercice %}
Calculer la complexité de l'algorithme $A$ en utilisant l'analyse par agrégat.
{% endexercice %}
{% details "corrigé" %}
Au cours des $m$ exécutions, on peut considérer ue l'on a fait appel :

- $m'$ fois à la fonction `k-dépile`{.language-},
- $m''$ fois à la fonction `empile`{.language-},
- $m - m' - m''$ fois à la fonction `nombre`{.language-}.

Le nombre total d'éléments dépilés au cours des $m'$ exécutions de la fonction `k-dépile`{.language-} ne peut excéder le nombre total $m''$ d'éléments empilés. La complexité totale des $m'$ exécutions de `k-dépile`{.language-} vaut donc $\mathcal{O}(m' + m'')$.

Comme la complexité d'un appel à `empile`{.language-} ou à `nombre`{.language-} vaut invariablement $\mathcal{O}(1)$, on en conclut que la complexité totale recherchée vaut :

$$
C = \mathcal{O}(m' + m'') + \mathcal{O}(m'') + \mathcal{O}(m - m' - m'') = \mathcal{O}(m + m'') = \mathcal{O}(m)
$$

{% enddetails %}
{% exercice %}
Calculer la complexité de l'algorithme $A$ en utilisant l'analyse par potentiel.

Pourquoi est-il judicieux d'utiliser comme potentiel le nombre d'élément dans la pile après l'exécution de l'instruction $i$ ?
{% endexercice %}
{% details "corrigé" %}

Soit $\Omega(i)$ le nombre d'élément dans la pile après l'exécution de l'instruction $i$. Ce potentiel est motivé par le fait que la seule méthode ayant un coût variable est `k-dépile`{.language-} et elle dépend du nombre d'éléments à dépiler, c'est à dire indirectement au nombre d'élément dans la pile.

Comme la pile est initialement vide on a bien $\Omega(i) \geq \Omega(0)$ pour tout $i$. Le coût amorti de chaque opération est alors :

- le coût amorti de `nombre`{.language-} est $1$ puisque la pile de change pas $\Omega(i) = \Omega(i - 1)$
- le coût amorti de `empile`{.language-} est $2$ puisque le coût réel est 1 et la pile à un élément de plus après l'opération ($\Omega(i) = \Omega(i - 1) + 1$)
- le coût amorti de `k-dépile`{.language-} est $1$ puisque le coût réel est de $1 + k$ et la pile à $k$ éléments de moins après l'opération ($\Omega(i) = \Omega(i - 1) - k$)

Le coût amorti peut être borné par 2 pour chaque opération, on a donc :

$$
C \leq \sum_{i=1}^m \widehat{c_i} \leq \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m)
$$

{% enddetails %}

## Calcul de complexité amortie

{% lien %}
C'est l'exercice 4 de [cette planche d'exercices](https://www.irif.fr/~francoisl/DIVERS/m1algo-td11-2324.pdf)
{% endlien %}

On calcule la complexité amortie de $m$ exécutions successives exécutions de l'algorithme $A$. On note $c(i)$ la complexité de la $i$ ème exécution.

On vous demande de calculer la complexité amortie en $\mathcal{O}$ de l'exécution de $A$ pour différentes valeurs de $c(i)$.

{% exercice %}

<div>
$$
c(i)=
\begin{cases}
i \text{ si }i=2^k\\
1 \text{ sinon }\\
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

La complexité totale vaut :

<div>
$$
C = \sum_{1\leq i \leq m}c(i) = m\sum_{1\leq i \leq m}1 + \sum_{0\leq k \leq \log_2(m)}(2^k-1) = m -\log_2(m)+2m-1
$$
</div>

La complexité amortie est en $\mathcal{O}(1)$.
{% enddetails %}

{% exercice %}

$c(i)$ vaut la plus petite puissance de 2 divisant $i$

{% endexercice %}
{% details "corrigé" %}

pour les $m$ itérations :

- la moitié est divisible uniquement par 2
- le quart est divisible uniquement par 4
- ...
- $\frac{1}{2^k}$ est divisible uniquement par $2^k$

La complexité totale vaut alors :

<div>
$$
C = \sum_{0\leq k \leq \log_2(m)}\frac{m}{2^k}\cdot 2^k = m\log_2(m)
$$
</div>

La complexité amortie est en $\mathcal{O}(\ln(m))$
{% enddetails %}

{% exercice %}

$c(i)$ vaut le plus grand $k$ tel que $2^k$ divise $i$

{% endexercice %}
{% details "corrigé" %}
Le calcul est presque identique à l'exercice précédent. La complexité totale vaut alors :

<div>
$$
C = \sum_{0\leq k \leq \log_2(m)}\frac{m}{2^k}\cdot k
$$
</div>

Comme $\sum_{0\leq k \leq n}\frac{k}{2^k} \leq 2$ ([on l'a vu](../projet-sommes-classiques/){.interne}), on a $C \leq 2m$ et la complexité amortie est en $\mathcal{O}(1)$
{% enddetails %}

## File et pile

On reprend l'exercice de construction d'[une file avec deux piles](../structure-pile-file/#file-avec-pile){.interne}

{% exercice %}

Quelle est la complexité amortie de l'enfilage et du défilage avec cette structure ?

{% endexercice %}
{% details "corrigé" %}

On peut calculer la complexité totale de $m$ enfilage et/ou défilage par méthode comptable exactement comme note pile avec la méthode `k-dépile`{.language-}. En effet une fois enfilé une donnée ne sera placée dans la seconde pile qu'une seule fois.

On obtient la même fonction de coût et donc la même complexité amortie : $\mathcal{O}(1)$. Cette structure qui semblait un brin fantaisiste est donc tout aussi optimale que la structure classique de file en complexité.

{% enddetails %}

## <span id="exercice-liste-suppression-ajout"></span> Ajout et suppression dans une liste

> TBD faire un mix avec 8.2 : <https://www.di.ens.fr/~fouque/articles/poly-algo.pdf> avec comptage et potentiel pour l'ajout simple.
> TBD voir aussi le poly de pascal.
> TBD à faire (dire que c'est dur)

<div id="preuve-liste-suppression-ajout"></div>
{% exercice %}
$N$ utilisations successives des méthodes d'ajout ou de suppression du dernier élément d'une liste prend $\mathcal{O}(N)$ opérations au maximum.
{% endexercice %}
{% details "preuve" %}

> TBD le faire.

{% enddetails %}
