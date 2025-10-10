---
layout: layout/post.njk

title: Code RSA

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Chiffrement RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA)
- [preuves RSA]([chiffrement RSA](https://www.youtube.com/watch?v=Xlal_d4zyfo))

{% endlien %}

Cet algorithme a été présenté en 1977 par Ronald Rivest, Adi Shamir et Leonard Adleman. Le chiffrement RSA s’appuie sur le fait que factoriser un produit de deux nombres premiers distincts est difficile.

Le code RSA est basé sur des principes arithmétiques. Le message à coder/décoder sera donc un entier $m$.

{% info %}
Pour bien appréhender cette partie, il faudra avoir quelques connaissances basiques sur les [modulo](https://fr.wikipedia.org/wiki/Modulo_(op%C3%A9ration)). En particulier :

- $x \equiv y \pmod{n}$ signifie que $x - y$ est un multiple de $n$
- $x \equiv y \pmod{n} \equiv (y + kn) \pmod{n}$ pour tout entier relatif $k$
- $(x + y) \pmod{n} \equiv [(x \pmod{n}) + (y \pmod{n})] \pmod{n}$
- $xy \pmod{n} \equiv [(x \pmod{n})\cdot(y \pmod{n})] \pmod{n}$
- $k (x \pmod{n}) \equiv kx \pmod{n}$

{% endinfo %}

## Principe

Soient $p$ et $q$ deux nombres premiers différents, strictement plus grand que 1, et tels que $pq > m$. On note :

- $n = pq$
- $\phi(n) = (p-1)(q-1)$

On peut alors choisir un entier $e$ (plus $\phi(n)$ est grand, plus il en existe) tel que :

- $0 < e < \phi(n)$
- $e$ est premier avec $\phi(n)$ (le seul diviseur commun à $e$ et $\phi(n)$ est 1)

{% note "codage" %}
Le couple $(e, n)$ constitue la **clé de chiffrement** et la fonction de codage est $f(m) = m^e \pmod{n}$

{% endnote %}

Soit alors $d$ l'unique entier tel que :

- un entier $0 < d < \phi(n)$
- $e\cdot d \equiv 1 \pmod{n}$ (il existe un entier $k$ tel que $e\cdot d = 1 + k \cdot \phi(n)$)

{% note "décodage" %}
Le couple $(d, n)$ constitue la **clé de déchiffrement** et la fonction de décodage est $f^{-1}(m) = m^d \pmod{n}$

{% endnote %}

## Existence et calcul de $d$

L'existence de $d$ est lié à une conséquence du [théorème de Bézout](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bachet-B%C3%A9zout) :

{% note "Théorème de Bézout" %}

Deux entiers positifs $a$ et $b$ sont premiers entre eux si et seulement il existe deux entiers relatifs $x$ et $y$ tels que :

<div>
$$
ax + by = 1
$$
</div>

{% endnote %}
{% details "preuve" %}
Commençons par supposer que $a$ et $b$ sont premiers entre eux.

L'ensemble $A = \\{ax + by>0 \mid x, y \in \mathbb{Z} \\}$ est non vide ($a+b > 0$), il contient donc un plus petit élément que l'on note $c=ax_0 + by_0$.

La division euclidienne de $a$ par $c$ donne : $a = qc+r$ avec $0 \leq r < c$. Comme $r = a-qc = a-q(ax_0 + by_0) = a(1-qx_0)+b(-qy_0)$ et que $r < c$, il ne peut être dans $A$. Ceci implique que $r=0$ et que $c$ divise $a$.

Le même raisonnement en utilisant la division euclidienne de $b$ par $c$ donne que $c$ divise $b$. Comme $a$ et $b$ sont premiers entre eux, $c$ ne peut valoir que 1.

Réciproquement, supposons qu'il existes deux entiers naturels $x$ et $y$ tels que $ax + by = 1$. Si $p$ est un diviseur commun à $a$ et $b$, on a $a=pa'$ et $b=pb"$ et donc $pa'x+pb'y = p(a'x+b'y) = 1$ ce qui implique que $p$ divise $1$ : $p = 1$.
{% enddetails %}
{% note "Corollaire" %}
Si entiers positifs $a$ et $b$ sont premiers entre eux, il existe un unique $0< x < b$ tel que  :

<div>
$$
ax = 1 + by
$$
</div>

Avec $y$ un entier positif.

{% endnote %}
{% details "preuve" %}
Commençons par montrer qu'il existe une solution avec $x$ et $y$ positifs.

Comme $a$ est premier avec $b$ le théorème de Bézout indique qu'il existe deux entiers relatifs $x$ et $y$ tels que $ax + by = 1$, donc $ax = 1 + b(-y)$

De plus les entiers $a$ et $b$ étant positifs donc $x$ et $y$ sont de signe différents. Si $y>0$ il existe $k > 0$ tel que $ka > y$ et on a $ax + kab = 1 - by + kab$. L'égalité précédente donne  $a(x + kb) = 1 + b(ka - y)$avec $x + kb$ et  $ka - y$ positifs.

Continuons en montrant qu'il existe une solution telle que $0 \leq x < b$. On utilise pour cela la division euclidienne de $x$ par $b$ : $x = bq+r$ et $0\leq r < b$ ce qui donne $a(bq+r) = 1 + by$ et donc $ar = 1 + b(y-bq)$. Comme $r$ est positif, $ar$ l'est, donc $b(y-bq)$ aussi et $0\leq y-bq$ : il existe une solution telle que $x<b$.

Enfin, si $ax=1+by$ et $ax'=1+by'$ alors $a(x-x') = b(y-y')$ et comme $a$ et $b$ sont premiers entre eux $b$ divise $x-x'$. Il n'y a donc au plus qu'une seule solution telle que $x <b$.

{% enddetails %}

On vient de montrer que pour tout couple d'entiers $a < b$ premiers entre eux, il existe un unique entier $a' < b$ tel que : $aa' \equiv 1 \pmod{b}$. Cet entier est appelé [inverse modulaire](https://fr.wikipedia.org/wiki/Inverse_modulaire).

{% lien %}
Voir le code RSA en action :
<https://www.onebigfluke.com/2013/11/public-key-crypto-math-explained.html>
{% endlien %}

## Preuve des bijections

Le fait que les fonctions $f =  m^e \pmod{n}$ et $f^{-1} =  m^d \pmod{n}$ sont bien inverse l'une de l'autre pour l'ensemble des entiers inférieurs à $n$ est due à un autre résultat de la théorie des nombre nommé le [petit théorème de Fermat](https://fr.wikipedia.org/wiki/Petit_th%C3%A9or%C3%A8me_de_Fermat) :

{% note "petit théorème de Fermat" %}
Si $p$ est un nombre premier et que $a$ est un entier alors : $a^{p} - a$ est un multiple de $p$

{% endnote %}
{% details "preuve" %}
Nous allons le faire par récurrence.

Si $a=1$, $a^{p}-a = 0$ qui est bien un multiple de $p$. On suppose la propriété vraie pour $a \geq 1$ et on s'intéresse à $a+1$ :

$$
(a+1)^{p}-(a+1) = \sum_{i=0}^pC_p^ia^i1^{p-i} -(a+1) = 1 + \sum_{i=1}^{p-1}C_p^ia^i + a^p -(a+1) = \sum_{i=1}^{p-1}C_p^ia^i + (a^p-a)
$$

Comme par hypothèse de récurrence $p$ divise $(a^p-a)$, il nous reste à prouver que $p$ divise $\sum_{i=1}^{p-1}C_p^ia^i$. Nous allons le faire en montrant que $p$ divise $C_p^i$ pour tout $0 < i <p$. En effet :

$$
C_p^i = \frac{p!}{i!(p-i)!} = p \frac{(p-1)!}{i!(p-i)!} = p \frac{\Pi_{j=1}^{p-i+1}(p-j)}{i!}
$$

Et comme $p$ ne peut diviser aucun $j$ pour tout $0 < j < p$ on en conclut que comme il est de plus premier, il ne peut pas non plus diviser $\Pi_{1\leq j \leq i}j = i!$ Ceci prouve que puisque $C_p^i$ est un entier, la quantité $\frac{\Pi_{j=1}^{p-i+1}(p-j)}{i!}$ est entière : $p$ divise $C_p^i$ pour tout $0 < i <p$.

$p$ divise bien $(a+1)^{p}-(a+1)$ s'il divise $a^{p}-a$, ce qui conclut la preuve par récurrence.

{% enddetails %}

On a $f(f^{-1}(m)) = m^{ed} \pmod{n}$. Comme $e\cdot d = 1 + k \cdot \phi(n)$ on a :

<div>
$$
\begin{array}{lcl}
m^{ed} &=&  m^{ed}\\
&=& m \cdot m^{ k \cdot \phi(n)}\\
&=& m \cdot (m^{p-1})^ {k(q-1)}\\
&=& m \cdot (m^{q-1})^ {k(p-1)}\\
\end{array}
$$
</div>

Si $m$ est un multiple de $p$ alors $m^{ed} \equiv 0 \pmod{p} \equiv m \pmod{p}$

Si $m$ n'est pas un multiple de $p$, comme $m^p-m=m(m^{p-1}-1)$ est un multiple de $p$ (petit théorème de Fermat), alors $m^{p-1}-1$ est un multiple de $p$. De là $m^{ed} = m \cdot (1 + k'p)^{k(q-1)}$ et :

<div>
$$
\begin{array}{lcl}
m^{ed} &\equiv&  [m \cdot (1 + k'p)^{k(q-1)}] \pmod{p}\\
&\equiv& [(m \pmod{p}) \cdot (((1 + k'p) \pmod{p})^{k(q-1)} \pmod{p})] \pmod{p} \\
&\equiv& [(m \pmod{p}) \cdot (1^{k(q-1)}  \pmod{p})] \pmod{p} \\
&\equiv& m \pmod{p}\\
\end{array}
$$
</div>

Pour tout $m$, $m^{ed} \equiv m \pmod{p}$ : $m^{ed} - m$ est un multiple de $p$.

Le même raisonnement avec $q$ nous donnant que $m^{ed} - m$ est un multiple de $q$ on en conclut, puisque $p$ et $q$ sont premiers, que $m^{ed} - m$ est un multiple de $pq=n$ et donc :

<div>
$$
\begin{array}{lcl}
m^{ed} &\equiv& m \pmod{n} \\
\end{array}
$$
</div>

## Algorithmes de calculs

### Calcul de d

Trouver l'inverse modulaire d'un nombre se fait usuellement en utilisant l'[algorithme d'Euclide étendu](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu), qui est une généralisation de l'[algorithme d'Euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide) qui calcule la division euclidienne.

### Calcul des codes

Calculer $f(m) = m^e \pmod{n}$ (ou $f^{-1}(m)$) se fait par exponentiation modulaire.

## Attaques

> TBD pollard's rho pour factoriser.
> 
> TBD RSA : bien choisir ses clés. Sinon multiplication de Fermat

> TBD attaques : [casser RSA](https://www.youtube.com/watch?v=-ShwJqAalOk)

pb des 0 : <https://fr.wikipedia.org/wiki/Optimal_Asymmetric_Encryption_Padding>

Basé sur le fait qu'algorithmiquement on ne sait pas efficacement [décomposer un nombre en produit de ses facteurs premiers](https://fr.wikipedia.org/wiki/D%C3%A9composition_en_produit_de_facteurs_premiers).

Pour trouver la clé secrète $(e, pq)$ en connaissant $(d, pq)$, il faut trouver $p$ et $q$ et donc décomposer $n=pq$ en produit de ses facteurs premiers : il est donc **difficile** de casser le code RSA lorsque $n$ est grand.

<https://danielpocock.com/rsa-key-sizes-2048-or-4096-bits/>
