---
layout: layout/post.njk

title: Schéma général du chiffrement

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On montre ici le schéma général qui nous permet de créer un chiffrement sémantiquement sécurisé d'un message de taille quelconque à partir d'une brique de base permettant de chiffrer une séquence de [blocs de taille fixée](../chiffrer-un-bloc){.interne}.

> TBD
>
> 1. Vernam. Mais
> 2. doit avoir une clé pour déchiffrer, donc taille max. Mais
> 3. doit réutiliser la clé ? Ajouter un paramètre
> 4. on peut maintenant chiffrer et déchiffrer des message. Mais
> 5. est-ce vraiment sécurisé ? On le vérifie avec des preuves de théorie des jeux.

> TBD attention : ECB pas semantically secure : <https://crypto.stanford.edu/~dabo/courses/cs255_winter19/lectures/PRP-PRF.pdf>

sécurité du bloc = taille de la clé ou moitié d la taille du bloc (attaque par anniversaire si pas de counter mode)

[SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)

> [tuto encryption](https://www.youtube.com/watch?v=oVCCXZfpu-w)
> TBD réorganiser.
>
> TBD dire qu'il en existe d'autres. On donne ici le plus simple sécurisé de maintenant.

### Changer de clé

Pour chiffrer un message, il faut à priori pouvoir écrire des message de taille quelconque, ce qui n'est pas pas possible avec notre générateur. De plus, on a vue qu'il ne faut pas réutiliser la clé.

Il faut donc aller plus loin pour pouvoir générer des clés selon la taille du message.

## Construction générale

Pour construire un code à flux il faut être capable de créer des générateurs pseudo-aléatoires de taille quelconque. Ceci peut être compliqué. On préfère découper le message à chiffrer $m$ en blocs $m_i$ de taille fixe que l'on traite séparément.

Il faut cependant faire **très** attention à ce que l'on fait et ne pas réutiliser les clés ! Sinon on peut très facilement déchiffrer le message comme on a vu avec le chiffre de Vernam.

On peut utiliser le fait que si $F$ est une PRF alors $F(\cdot, x)$ est un PRG quelque soit $x$.

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF et $m$ un message de taille $l\cdot n$ alors :

$$
E(k, m) = F(k, 1) \ \ ||\ \  \dots \ \ ||\ \  F(k, l) \oplus m
$$

est un codage par flus sécurisé.
{% endnote %}
{% info %}
L'opérateur `||` est la concaténation.
{% endinfo %}
{% details "preuve", "open" %}

> BD theorem 3.30 introduction to cryptography
{% enddetails %}

Cette construction permet également de déchiffrer rapidement le message en parallèle. Il suffit de connaître la clé $k$ et la position du bloc à déchiffrer.

On peut même ajouter un élément en clair dans le cryptage sans en altérer la sécurité. Le schéma général d'un codage en flux avec compteur est alors :

```
     N || 1       N || 2            N || i            N || l
        |            |                 |                 |
      -----        -----             -----             -----
 k-->|     |  k-->|     |  ...  k-->|     |  ...  k-->|     |
      -----        -----             -----             -----
        |            |                 |                 |
 m1--->XOR    m2--->XOR         mi--->XOR         ml--->XOR
        |            |                 |                 |
        |            |                 |                 |
       c1           c2                ci                cl
```

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est une secure PRF, $m$ un message de taille plus petite que $l\cdot n$ et $\text{NONCE}$ un mot de \\{0, 1\\}^p$ avec $p<n$ alors :

$$
E(k, m) = NONCE \ ||\  (F(k, NONCE \ ||\  1) \ ||\  (F(k, NONCE \ ||\  2) \ ||\  \dots \ ||\  F(k, NONCE \ ||\  l) \oplus m)
$$

est un codage par flux sécurisé.
{% endnote %}
{% details "preuve", "open" %}

> TBD : construction 3.25 Introduction to modern cryptography
> {% enddetails %}

Remarquer que le $\text{NONCE}$ est transmis en clair, ce n'est pas grave. L'utilisation de ce $\text{NONCE}$ est courante dans les méthodes de chiffrement en flux.

{% note "**Définition**" %}

Un [NONCE](https://en.wikipedia.org/wiki/Cryptographic_nonce) est un nombre utilisé une fois.

Il st utilisé dans de nombreux protocoles cryptographiques pour distinguer des encodages au sein de l'envoie d'un message.
{% endnote %}

## PRG et _prédictabilité_

{% note %}
Une suite $g(k,1), \dots g(k, m + 1)$ est non prédictible si tout algorithme efficace ne peut peut prédire $g(k, m + 1)$ sachant $g(k, 1), \dots, g(k, m)$ qu'avec un avantage négligeable.
{% endnote %}

Le générateur de nombre pseudo-aléatoire tel que $x_i = a \cdot x_{i-1} + b \mod p$ ne l'est pas, malgré le fait qu'il possède de belle propriétés statistiques si $p$ est premier. Pour qu'un générateur de nombre puisse être utilisé de façon cryptographe, on s'intéresse moins à ses propriété d'uniformité qu'à sa non prédictibilité.

Non prédictible est équivalent à non distinguable.

{% note "**Proposition**" %}
Un PRG sécurisé est non prédictible.
{% endnote %}
{% details "preuve" %}

Supposons qu'un secure PRG soit prédictible. Il existe alors un algorithme efficace A qui possède un avantage non négligeable pour déterminer le $m+1$ ème bit à partir des $m$ premiers.

On peut utiliser cet algorithme pour déterminer si $G$ est un PRG sécurisé : on ne considère que les $m+1$ premiers bits et on rend la valeur donnée par l'algorithme $A$. L'avantage est le même et est non négligeable.

{% enddetails %}

{% note "**Théorème (Yao, 1982)**" %}
Un PRG non prédictible est sécurisé.
{% endnote %}
{% details "preuve" %}
Soit $G$ un générateur non prédictible, et R un générateur aléatoire.

Supposons qu'il existe $i$ tel que que le générateur $G(k) [:i]\\; ||\\; R[i:]$ soit non sécurisé. Prenons $i$ le plus petit et soit A l'algorithme efficace qui réalise cet avantage.

Cet algorithme nous permettra de discerner $G(k) [:i-1]\\; ||\\; R[i-1:]$ de $G(k) [:i]\\; ||\\; R[i:]$ avec le même avantage et donc de prédire $G(k) [i]$ à partir de $G(k) [:i-1]$ avec encore une fois le même avantage. Ceci n'est pas possible puisque $G$ est non prédictible.

le générateur $G(k) [:i]\\; ||\\; R[i:]$ est donc sécurisé pour tout $i$ donc également pour $i=n$.

{% enddetails %}
{% info %}

- on note `||` l'opérateur de concaténation
- `m[:n]` correspond aux n-1 premiers bits de $m$
- `m[n:]` correspond à $m$ privé de ses $n-1$ premiers bits

{% endinfo %}

{% lien %}
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf)
{% endlien %}
