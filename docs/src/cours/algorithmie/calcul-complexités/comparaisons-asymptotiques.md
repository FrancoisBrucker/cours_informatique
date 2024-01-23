---
layout: layout/post.njk

title: Comparaisons asymptotiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les comparaisons asymptotiques servent à comparer l'*allure* de deux fonctions à l'infini : plus grande, plus petite ou équivalente.

On considérera dans la suite de ce cours uniquement des fonctions **positives**, ce qui est le cas lorsque l'on appliquera à la mesure de complexité. Donc :

{% attention %}
Certaines équivalences ci-dessous ne sont vraies que dans le cas de fonctions positives.
{% endattention %}

## *Fonctions* asymptotiques

On montre 3 *fonctions* asymptotiques, a plus utilisée étant la fonction $\mathcal{O}()$

### Les $\mathcal{O}()$ pour majorer

Les *grand O*, $\mathcal{O}()$, permettent de caractériser les fonctions qui en majorent une autre.

{% note %}
Une fonction <span>$f(N)$</span> est en $\mathcal{O}(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot f'(N)$ pour tout $N > N_0$.
{% endnote %}

Connaître le comportement en $\mathcal{O}$ de $f(N)$  nous donne un majorant de son *allure* lorsque $N$ devient grand.

Par abus de langage, on notera :

- $\mathcal{O}(f(N))$ plutôt que : soit $f'(N)$ une fonction en $\mathcal{O}(f(N))$
- $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
- $\mathcal{O}(f(N)) \Rightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$"
- $\mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$ et réciproquement"

### Les $\Omega()$ pour minorer

De façon symétrique, on défini les *grand Omega*, $\Omega()$, qui permettent de caractériser les fonctions qui en minorent une autre.

{% note %}
Une fonction <span>$f(N)$</span> est en $\Omega(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) > c_0 \cdot f'(N)$ pour tout $N > N_0$.
{% endnote %}

La fonction $\Omega$ est le symétrique de la fonction $\mathcal{O}$ :

<span id="omega-GO"></span>
{% note %}
$f(N) = \mathcal{O}(g(N)) \Leftrightarrow g(N) = \Omega(f(N))$
{% endnote %}
{% details  "preuve" %}
Si $f(N) = \mathcal{O}(g(N))$, il existe  $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$. Les fonctions étant positives, on a $c_0 > 0$ et donc $\frac{1}{c_0} \cdot f(N) <  g(N)$ pour $N > N_0$ : $g(N) = \Omega(f(N))$

Réciproquement, si $g(N) = \Omega(f(N))$, il existe  $c_0$ et $N_0$ tels que $c_0 \cdot f(N) < g(N)$ pour $N > N_0$. Les fonctions étant positives, on a $c_0 > 0$ et donc $\frac{1}{c_0} \cdot g(N) >  f(N)$ pour $N > N_0$ : $f(N) = \mathcal{O}(g(N))$

{% enddetails %}

### Les $\Theta()$ pour les équivalences

{% note %}
Une fonction <span>$f(N)$</span> est en $\Theta(f'(N))$ si :

- <span>$f(N)$</span> est en $\mathcal{O}(f'(N))$
- <span>$f(N)$</span> est en $\Omega(f'(N))$
{% endnote %}

La fonction $\Omega$ est le symétrique de la fonction $\mathcal{O}$ :

{% note %}
$f(N) = \Theta(g(N)) \Rightarrow g(N) = \Theta(f(N))$
{% endnote %}
{% details  "preuve" %}
Clair grace à [la propriété précédente](./#omega-GO){.interne}.
{% enddetails  %}

### Usage

Les fonctions asymptotiques permettent d'utiliser :

- des fonctions plus simple que les solution exactes.
- de ne pas s'occuper des constantes puisque (on va le démontrer) une fonction en $\mathcal{O}(\text{constante})$ est également en $\mathcal{O}(1)$
- de ne pas s'occuper de la proportionnalité car (on va le démontrer) une fonction en $\mathcal{O}(\text{constante} \cdot f(N))$ est également en $\mathcal{O}(f(N))$

## <span id="arithmétique"></span>Arithmétique des fonctions asymptotiques

Commençons par deux règles liant les 3 fonctions :

{% note %}
$f(N) = \Theta(g(N)) \Leftrightarrow f(N) = \Omega(g(N)) \text{ et } g(N) = \Omega(f(N))$
{% endnote %}
{% details  "preuve" %}
Immédiat grace à la définition de $\Theta()$ et à [la propriété liant $\Omega$ et $\mathcal{O}$](./#omega-GO){.interne}.
{% enddetails  %}
{% note %}
$f(N) = \Theta(g(N)) \Leftrightarrow f(N) = \mathcal{O}(g(N)) \text{ et } g(N) = \mathcal{O}(f(N))$
{% endnote %}
{% details  "preuve" %}
Immédiat grace à la définition de $\Theta()$ et à [la propriété liant $\Omega$ et $\mathcal{O}$](./#omega-GO){.interne}.

{% enddetails  %}

La règle suivante va se retrouver fort utile :

<span id="OA-constantes"></span>
{% note "**Règle des constantes**" %}
$ A = \Theta(1)$, avec $A$ une constante strictement positive.
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) < c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) < c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

Enfin, les règles suivantes (si les fonctions sont positives) permettent de combiner les fonctions asymptotiquement comparables. Elles sont explicitées avec les $\mathcal{O}()$ mais fonctionnent également avec les $\Omega()$ et les $\Theta$ :
<span id="OA-sommes"></span>
{% note "**Règle des sommes**" %}
En combinant les $\mathcal{O}$ pour $f$ et $g$, deux fonctions positives :

$\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) + g'(N) < c_0 f(N) +  c'_0 g(N) < \max(c_0, c'_0) \cdot (f(N) + g(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) + g'(N) = \mathcal{O}(f(N) + g(N))$.

{% enddetails %}

<span id="OA-produits"></span>
{% note "**Règle des produits**" %}
En combinant les $\mathcal{O}$ pour $f$ et $g$ deux fonctions positives :

$\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) \cdot g'(N) <  c_0f(N) \cdot c'_0g(N) = c_0c'_0 \cdot (f(N)g(N)) $ pour $N > \max(N_0, N'_0)$.

{% enddetails %}

Les trois règles suivantes permettent de négliger les fonctions majorées. Elles fonctionnent dans l'autre sens pour les $\Omega$ et ne fonctionnent pas pour les $\Theta$ :

{% note "**Règle des polynômes**" %}
$\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$
{% endnote %}
{% details "preuve" %}

Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$.

Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p < N^p \cdot (2 \cdot N^{q-p}) = c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$  et $p \leq q$. Donc $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

{% note "**Règle des sommes négligeables**" %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$ pour f, g et h des fonctions positives.
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$.

Si $f'(N) = \mathcal{O}(f(N) + g(N) + h(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) + g(N) + h(N))$ pour $N > N'_0$.

De là, $f'(N) < c'_0 c_0 g(N) + c'_0 g(N) + c'_0 h(N)$ pour $N > \max( N_0, N'_0 )$ ce qui implique $f'(N) < c'_0 \cdot (c_0 + 1) g(N) + c'_0h(N) < c'_0 \cdot (c_0 + 1) (g(N) + h(N))$ pour $N > \max(N_0, N'_0)$

On a bien : $f'(N) = \mathcal{O}(g(N) + h(N))$

{% enddetails %}

{% note "**Règle des produits négligeables**" %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$ pour f, g, h et h' des fonctions positives.

{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$. Les fonctions étant positives, on pet considérer sans perte de généralité que $c_0 > 1$

Si $f'(N) = \mathcal{O}(f(N)\cdot g(N) \cdot h(N) + h'(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) \cdot g(N) \cdot h(N) + h'(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 (c_0 g(N) \cdot g(N) \cdot h(N) + h'(N)$ pour $N > \max(N_0, N'_0)$ ce qui implique $f'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 h'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 c_0h'(N) < c'_0c_0 \cdot (g(N)^2 \cdot h(N) + h'(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) = \mathcal{O}((g(N))^2 \cdot h(N) + h'(N))$

{% enddetails %}

## Exercices

> TBD