---
layout: layout/post.njk

title: Analyse amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il existe trois types d'analyses amortie possibles : par agrégat, comptable et par potentiel. La méthode par potentielle est la plus générale mais également la plus ardue à mettre en oeuvre. La méthode comptable est intermédiaire et la méthode par agrégat (que l'on a déjà utilisé pour les listes) est la méthode la plus simple et qui est souvent suffisante.

Pour l'exemple de l'algorithme `tous`{.language-}, l'analyse par agrégat suffit, mais on montrera aussi comment les résoudre avec la méthode comptable et par potentiel. Le résultat sera bien sur le même : $\mathcal{O}(2^n)$

## Analyse par Agrégat

{% note %}
La technique de **_l'analyse par agrégat_** consiste à considérer l'ensemble des $m$ exécutions comme un **tout**.

On évalue la complexité des $m$ opérations en même temps, sans distinguer les différentes opérations.
{% endnote %}

### <span id="compteur-agrégat"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec l'analyse par agrégats

On remarque tout d'abord que le nombre d'opérations de `successeur(N)`{.language-} dépend de l'indice du dernier `0`{.language-} dans la liste `N`{.language-} :

- si `N`{.language-} finit par la liste `[0]`{.language-} il faut de l'ordre de 1 opération à successeur (la boucle `tant que`{.language-} de la ligne 4 fait un test et aucune itération)
- si `N`{.language-} finit par la liste `[0, 1]`{.language-} il faut de l'ordre de 2 opérations à successeur (la boucle `tant que`{.language-} de la ligne 4 fait une itération)
- si `N`{.language-} finit par la liste `[0, 1, 1]`{.language-} il faut de l'ordre de 3 opérations à successeur (la boucle `tant que`{.language-} de la ligne 4 fait deux itérations)
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * i`{.language-} il faut de l'ordre de $i+1$ opérations à successeur
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur
- si `N`{.language-} finit par la liste `[1] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur

On peut partitionner l'ensemble des $2^n$ nombres binaires à $n$ bits en $n$ ensembles disjoints :

1. $\mathcal{N}_1$ tous les nombres qui finissent par `0`. Il y en a $\frac{2^n}{2}$
2. $\mathcal{N}_2$ tous les nombres qui finissent par `01`. Il y en a $\frac{2^n}{2^2}$
3. ...
4. $\mathcal{N}_i$ tous les nombres qui finissent par `0` suivi de (i-1) `1`. Il y en a $\frac{2^n}{2^i}$
5. $\mathcal{N}_n$ tous les nombres qui finissent par `0` suivi de (n-1) `1`. Il y en a $\frac{2^n}{2^n}$
6. $\mathcal{N}'_{n}$ contenant le nombre ne contenant que des `1`. Il y en a 1

Il faudra de l'ordre de $i$ opérations à `successeur(N)`{.language-} pour traiter un nombre de $\mathcal{N}_i$ et $n$ opérations pour traiter l'élément de $\mathcal{N}'_n$. Comme on a partitionné l'ensemble de toutes les entrées possibles et que notre algorithme va les utiliser tous une unique fois, on en conclut que la complexité totale de l'algorithme `tous(n)`{.language-} est :

$$
C = \sum_{i=1}^{n}i\cdot \frac{2^n}{2^i} + n = 2^n \cdot \sum_{i=1}^{n}\frac{i}{2^i} + n
$$

Calculons cette complexité :

<div>
$$
\begin{array}{rcl}
C&=& 2^n \cdot \sum_{i=1}^{n}\frac{i}{2^i} + n\\
&=& 2^n \cdot (\sum_{k=1}^n\sum_{i=k}^{n}\frac{1}{2^i}) + n\\
&=&2^n \cdot (\sum_{k=1}^n(\sum_{i=1}^{n}\frac{1}{2^i} - \sum_{i=1}^{k-1}\frac{1}{2^i})) + n\\
&=&2^n \cdot (n\cdot \sum_{i=1}^{n}\frac{1}{2^i} - \sum_{k=2}^n\sum_{i=1}^{k-1}\frac{1}{2^i}) + n
\end{array}
$$
</div>

On utilise alors le fait que : $\sum_{i=1}^{n} \frac{1}{2^i} = 1 - \frac{1}{2^{n}}$ (immédiat par récurrence mais il existe également [une preuve directe](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF)), ce qui permet d'obtenir :

<div>
$$
\begin{array}{rcl}
C&=&2^n \cdot (n\cdot \sum_{i=1}^{n}\frac{1}{2^i} - \sum_{k=2}^n\sum_{i=1}^{k-1}\frac{1}{2^i}) + n\\
&=&2^n \cdot (n\cdot (1-\frac{1}{2^n}) - \sum_{k=2}^n(1-\frac{1}{2^{k-1}})) + n\\
&=&2^n \cdot (n\cdot (1-\frac{1}{2^n}) - (n-1) -\sum_{i=1}^{n-1}(1-\frac{1}{2^{i}})) + n\\
&=&2^n \cdot (1-\frac{n}{2^n}+1-\frac{1}{2^{n-1}}) + n\\
&=&2^n \cdot (2-\frac{n+2}{2^n}) + n\\
&=&2^{n+1} \cdot (1-\frac{1}{2^n})
\end{array}
$$
</div>

## Méthode comptable

La méthode comptable va associer des coûts différents à chaque opération, appelé _coût amorti_ :

{% note %}
La **_méthode comptable_** pour calculer la complexité totale de $m$ exécutions successives d'un même algorithme consiste à associer à la $i$ème exécution de coût réel $c_i$ un **_coût amorti_** $\hat{c_i}$ tel que pour tout $1 \leq k \leq m$ :

$$
\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}
$$

L'inégalité ci-dessus assure que la complexité totale des $m$ exécutions de l'algorithme sera bien inférieure à la somme des $m$ coûts amortis.
{% endnote %}

Lorsque l'on utilise la méthode comptable, l'astuce est de choisir certains coûts supérieur au coût réel et certains coûts inférieur : certaines opérations sont crédités d'un coût additionnel qui sera débité lors d'opérations futures. Il faut cependant toujours s'assurer d'avoir un crédit suffisant pour payer les coûts futurs.

### <span id="compteur-comptable"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec la méthode comptable

Appliquons cette méthode au compteur. La complexité totale à calculer est égale au nombre de bits modifiés. Or un bit n'est mit à 0 que s'il a été mis à 1 à une étape précédente. On peut donc donner comme coût amorti :

- 2 lorsqu'un bit est positionné à 1 (on compte son coût de positionnement à 1 **et** on crédite directement son coût de positionnement à 0)
- 0 lorsqu'un bit est positionné à 0

Ces coûts amortis assurent que la somme des $k$ premiers coûts amorti est supérieur à la somme réelle des $k$ coûts.

Enfin, comme à chaque exécution de `successeur`{.language-} un unique bit est mis à 1, on en conclut que le coût amorti d'une exécution de successeur est 2. Le coût amorti de $m$ exécutions successives de `successeur`{.language-} est donc de $C = m$ : l'exécution de `tous(n)`{.language-} est de complexité $\mathcal{O}(2^n)$.

## Analyse par potentiel

Cette méthode de calcul est une généralisation des deux méthodes précédentes.

{% note %}
L'**_analyse par potentiel_** calcule la complexité totale de $m$ exécutions successives d'un même algorithme consiste à associer à la $i$ème exécution de coût réel $c_i$ un **_potentiel_** $\Omega(i)$ tel que $\Omega(i) \geq \Omega(0)$ pour tout $i \geq 1$ (on prend généralement $\Omega(0) = 0$)

Le **_coût amorti_** $\widehat{c_i}$ de la $i$ème exécution est alors défini tel que :

$$
\widehat{c_i} = c_i + \Omega(i) - \Omega(i-1)
$$

L'égalité ci-dessus assure que la complexité totale des $m$ exécutions de l'algorithme sera bien inférieure à la somme des $m$ coûts amortis.

$$
\sum_{i=1}^{m} \widehat{c_i} = \sum_{i=1}^{m} ({c_i} + \Omega(i) - \Omega(i-1)) = \sum_{i=1}^{m} {c_i} + \Omega(m) - \Omega(0) \geq \sum_{i=1}^{m} {c_i}
$$

{% endnote %}

Cette technique d'analyse vient de la physique où l'on peut associer à un système une énergie potentielle, qui sera modifiée après chaque action : $\Omega(i-1)$. Cette énergie potentielle $\Omega(i-1)$ correspond à l'état du système avant la $i$ème opération et $\Omega(i)$ son état après cette opération, rendant compte de la modification qu'à exercé l'opération sur le système.

En informatique, le potentiel sera souvent associé à la structure de donnée sous-tendant l'exécution de l'algorithme (ses paramètres, ses variables, etc).

Remarquez que toute mesure de potentielle fonctionne si $\Omega(i) \geq \Omega(0)$ pour tout $i \geq 1$, mais que pour être efficace, on va chercher à obtenir un coût amorti le plus petit possible, si possible constant. Ce faisant, la différence de potentiel absorbera les variations de coût réel sans trop les surévaluer.

### <span id="compteur-potentiel"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec l'analyse par potentiel

Le nombre de bits changés à chaque exécution de successeur dépend du nombre de 1 dans la liste passée en paramètre. Comme $\Omega(0) = 0$, on garanti que $\Omega(i) \geq \Omega(0)$ pour tout $i$, c'est une mesure de potentiel correct.

A chaque exécution de `successeur`{.language-} on a :

- k bits passés à 0
- 1 bit passé à 1

On en déduit que :

- la complexité d'exécution est de k + 1
- la différence de potentiel $\Omega(i) - \Omega(i-1)$ vaut $1 - k$

Le coût amorti d'une exécution de successeur vaut alors $\widehat{c_i} = c_i + \Omega(i) - \Omega(i-1) = 1 + k + (1-k) = 2$ quelque soit $i$.

On a donc que, encore une fois, la complexité de l'algorithme `tous(n)`{.language-} est :

$$
C \leq \sum_{i=1}^m \widehat{c_i} = \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m) = \mathcal{O}(2^n)
$$
