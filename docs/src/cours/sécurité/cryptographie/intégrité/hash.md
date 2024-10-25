---
layout: layout/post.njk

title: Hash cryptographiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Hash cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)
- [Hash propriétés et autres](https://membres-ljk.imag.fr/Bruno.Grenet/IntroCrypto/4.HashFunctions.pdf)

{% endlien %}

Une fonction de hash cryptographique doit être conçue pour éviter les collisions, c'est à dire qu'en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% note "**Définition**" %}
Une fonction $H: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est une fonction de ***hash cryptographique*** si elle est résistante aux collisions.

Tout algorithme efficace ne peut rendre un couple $(x, x')$ tel que $H(x) = H(x')$ qu'avec un avantage négligeable.
{% endnote %}

On peut relâcher la condition de résistance à la collision en :

1. ***résistant à la seconde pré-image*** : étant donné $x$, il est difficile de trouver $x'$ tel que $H(x) = H(x')$

2. ***résistant à la pré-image*** : étant donné $y$, il est difficile de trouver $x$ tel que $H(x) = y$

La première condition étant plus restrictive que la condition 2.

## Usage

### Intégrité non sécurisée

On accole le hash au message envoyé : $m || H(m)$

Le message est bien transmis si le hash du message arrivé correspond au hash concaténé. Couple $(S, V)$ signe et vérifie :

- $S(m) = H(m)$
- $V(m, h) = (H(m) == h)$

Mais peut- être changé par un attaquant. Donc uniquement preuve de transmission correct d'un message dans un canal pouvant être bruité, mais pas susceptible d'être attaqué.

### Stockage sécurisé

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.

Pour rendre les attaques par dictionnaire (on stocke une suite de mots et leurs hash) plus difficile, on ajoute du bruit sous la forme d'un mot concaténé, appelé *sel* à ce que le l'on hash. On obtient le couple signature, vérification :

- $S(m) = SALT || H(SALT || m)$
- $V(m, t) = H(t[:p] || m) = t[p:]$ où $p$ est la longueur du sel

### Clés

La non collision permet de rechercher les hash plutôt que les valeurs exactes dans une liste stockant toutes les données. C'est la technique utilisée par Git pour gérer les ajouts, suppressions et modifications de code dans un projet.

{% info %}
Git utilise par défaut la fonction de hash SHA-1.
{% endinfo %}

## Attaque

{% lien %}
[Attaque des fonction de hash](https://people.cs.uchicago.edu/~davidcash/284-autumn-21/12-hash.pdf)
{% endlien %}

### Attaque des anniversaires

L'attaque générique des anniversaires est l'attaque brute force associée aux fonctions de hash cryptographique.

Grace au [paradoxe des anniversaires](/cours/algorithmie/structure-conteneurs/fonctions-hash/#paradoxe-anniversaires){.interne}, on sait qu'il suffit de $2^{n/2}$ mots de $\\{0, 1\\}^n$ pour avoir une probabilité supérieure à 1/2 d'avoir deux éléments $x$ et $x'$ tels que $H(x) = H(x')$.

Il n'est pas nécessaire de stocker tous les mots en mémoire, on peut montrer qu'il suffit de :

{% note "**Algorithme attaque par point fixe**" %}

1. prendre $x_1 = y_1$ un mot aléatoire de $\\{0, 1\\}^n$
2. créer itérativement $x_i = H(x_{i−1})$ et $y_i = H(H(y_{i−1}))$ jusqu'à ce que $x_m = y_m$
3. on a alors $H(x_{m−1}) = H(H(y_{m−1}))$ si $x_{m-1} \neq H(y_{m−1})$ (ce qui est très probable)

Il faut, comme l'attaque brute force du dictionnaire de l'ordre de $\mathcal{O}(2^{n/2})$ opération avant de trouver une collision

{% endnote %}
{% details "preuve", "open" %}

C'est l'[algorithme du lièvre et de la tortue](https://fr.wikipedia.org/wiki/Algorithme_du_li%C3%A8vre_et_de_la_tortue).

L'ensemble d'arrivée de $H$ étant fini, il va exister, pour tout $x$, un entier $p$ tels que $H^p(x) = H^q(x)$ avec $q > p$.

On pose :

- $\lambda = p$
- $\mu = q-p$

Soit $x$ le plus petit entier tel que $\lambda +x$ soit un multiple de $\mu$. On a $0 \leq x \leq \mu$ puisque la division euclidienne de $\lambda$ par $\mu$ donne $\lambda = q\cdot \mu +r$ et donc $x=\mu-r$

 On a alors : $2(\lambda +x) = \lambda +x + k\cdot \mu$ et donc $H^{2(\lambda +x)}(x) = H^{\lambda +x}(x)$.

> TBD aussi en analysant si lapin en arrière de k de la tortue sur le cycle : à l'étape d'après k-1 en arrière.

{% enddetails %}

Notez que si l'attaque des anniversaires ne donne pas de garanties sur les deux mots que l'on trouve, il est très facile de modifier 2 documents différents de façon aléatoire un très grand nombre de fois, ce qui va garantir de tomber sur une collision tout en ayant deux texte se ressemblant.

{% info %}
La technique précédente permet de présenter deux textes différents de même hash en :

1. écrivant deux textes différents
2. modifier aléatoirement les deux textes en ajoutant des espaces, des retours chariots ou backspace. Bref plein de choses qui ne se voient pas une fois.
3. au bout de $2^{n/2}$ modifications, on a deux deux texte de même hash où le contenu *visible* est celui des deux textes initiaux.

Il suffit ensuite de faire signer la version $A$ du texte puis de présenter la version $B$, prétendument signée.

Il faut toujours modifier un peu un document que l'on signe, histoire que l'attaquant doive tout refaire.
{% endinfo %}

### Differential Analysis

{% lien %}

[differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)

{% endlien %}

> TBD : à étoffer

## Construction

### A longueur fixée

{% lien %}
[Construction Davies–Meyer](https://fr.wikipedia.org/wiki/Construction_de_Davies-Meyer)
{% endlien %}

On utilise la construction Davies–Meyer qui permet de transformer [un PRP](../../confidentialité/chacha20/#PRP){.interne} $P : \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ ($P(k, x)$ est une permutation aléatoire de $x$) en hash à taille fixe.

On fait rentrer le message là où normalement arrive la clé. Et un utilisant une constante $\text{IV}$ (initial value) à la place de la où habituellement se place un message.

<div>
$$
H(m) = P(m, \text{IV})
$$
</div>

Ce qui donne schéma :

```
         m |
           |
       ---------
IV ----|   v   |--- XOR ---
    |  |       |     |
    |  ---------     |
    |                |
    ------------------               
```

{% note "**Théorème**" %}

Si le bloc est une PRP, alors la résistance à la collision est maximale.
{% endnote %}
{% details "preuve", "open" %}
> TBD : preuve avec <https://crypto.stackexchange.com/questions/8023/why-are-the-davies-meyer-and-miyaguchi-preneel-constructions-secure>

{% enddetails %}
{% info %}
[article de la preuve](<https://www.cs.ucdavis.edu/~rogaway/papers/hash.pdf>)
{% endinfo %}

> TBD : [pseudo-random function et permutation pareil sous le paradoxe anniversaire](https://crypto.stackexchange.com/questions/75304/what-is-the-difference-between-pseudorandom-permutation-pseudorandom-function-bl)

### A longueur variable

{% lien %}

- [Construction de Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd)
- [Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)

{% endlien %}

On utilise la construction de Merkel-Damgard pour étendre la portée du hash à taille fixe.

```
        m1 |                           mi |                
           |                              |                
       --------- H1                   --------- Hi           
IV ----|   v   |--- XOR --- ... ------|   v   |--- XOR --- .... Hm
    |  |       |     |             |  |       |     |     
    |  ---------     |             |  ---------     |      
    |                |             |                |      
    ------------------             ------------------           
```

On ajoute un padding à la fin qui consiste en :

<div>
$$
m || 10\dots 0 || \text{taille du message}
$$
</div>

Le message final doit bien faire une taille multiple de la taille du hash à taille fixe. Si le message est déjà de la bonne taille on ajoute tout de même un bloc ne contenant que le padding et la taille.

{% note "**Théorème**" %}
Si le bloc est résistant à la collision, la construction l'est.
{% endnote %}
{% details "preuve", "open" %}
Supposons qu'il y ait une collision :

On a alors $H_n = H'_{n'}$ ce qui implique :

<div>
$$
P(H_{m-1}, m_n \ ||\  \text{pad}) = P(H'_{m'-1}, m'_{n'} \ ||\  \text{pad}')
$$
</div>

De là si :

<div>
$$
m_n \ ||\  \text{pad} \neq m'_{n'} \ ||\  \text{pad}
$$
</div>

On a découvert une collision interne ce qui est improbable. Donc :

<div>
$$
m_n \ ||\  \text{pad} = m'_{n'} \ ||\  \text{pad}'
$$
</div>

Alors :

1. $\text{pad} = \text{pad}'$ ce qui implique que les deux messages ont la même taille
2. $m_n = m'_n$ : les messages ont la même fin

On conclut la preuve en remarquant que si $H_{m-1}$ est différent de ${H'}_{m-1}$ on a une collision ce qui est improbable. Les deux sont alors égaux et poursuit par récurrence.

{% enddetails %}

Les fonctions de hash très utilisés que sont les SHA-1 et SHA-2 sont basées sur ce principe.

{% info %}
SHA-3 est basé sur une autre construction : les [sponge function](https://en.wikipedia.org/wiki/Sponge_function)
{% endinfo %}
