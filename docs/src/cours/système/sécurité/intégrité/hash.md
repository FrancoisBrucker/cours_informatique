---
layout: layout/post.njk

title: Hash et sécurité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> def, sécurité sémantique, comment en faire à partir de PRP.

Pour être utilisable en cryptographie, les [fonctions de hash](/cours/algorithme-code-théorie/théorie/fonctions-hash) doivent cependant avoir des propriétés spécifiques.

Deux types de fonctions sont utilisés en sécurité :

1. fonction de hash avec une clé, appelé MAC
2. fonction de hash avec sans clé, appelé hash cryptographique

## MAC

### Définitions

Un ***MAC, Message authentification code*** est constitué d'une paire :

- $S: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^h$ qui ***signe*** en produisant un ***tag*** (en utilisant une clé $k$ un message $m$)
- $V: \\{0, 1\\}^s \times \\{0, 1\\}^n \times \\{0, 1\\}^h \rightarrow \\{0, 1\\}$ qui ***vérifie*** (en utilisant une clé $k$, un message $m$ et son tag potentiel)
- $V(k, m, S(k, m)) = 1$

Un MAC est ***sécurisé*** si un adversaire efficace ne peut gagner le jeu suivant, nommé ***existential forgery against a chosen message attack***, qu'avec un avantage négligeable :

1. le testeur choisit uniformément une clé $k$
2. l'adversaire **choisit** q messages $m_1$ et $m_{q}$ à donner au testeur
3. le testeur renvoie à l'adversaire les $q$ messages signés $S(k, m_1), \dots S(k, m_q)$
4. l'adversaire répond un couple $(m, t)$ où $m \notin \\{m_1, \dots, m_q\\}$
5. l'adversaire gagne si $V(k, m, t) = 1$

```
    
     testeur                            adversaire
    ---------        m1, ..., mq       ------------
    |   k   | <----------------------- |          |  
    |       |  S(k,m1), ..., S(k,mq)   |          |
    |       | -----------------------> |          |
    |       |           (m, t)         |          |
    |       | <----------------------- |          |
    ---------                          ------------

```

Ce jeu simule le fait qu'un attaquant peut influencer la teneurs de messages envoyés (en comptant sur un reply lors d'un envoie de mail par exemple) et ne peut forger à son tout un MAC valide.

### Attaque

#### Taille du MAC

Remarquez qu'un MAC peut toujours être attaqué avec une probabilité au moins négligeable. Pour cela, il suffit de générer tous les tag possibles, il y en a $2^h$, pour obtenir une probabilité de succès de $1/2^h$. Ceci impose que la taille du tag doit être supérieure à $\mathcal{O}(\log_2(n))$ pour que l'adversaire ne puisse avoir une attaque brute force avec un gain non négligeable.

#### Replay attack

Même s'il est impossible de forger un MAC valide, rien n'empêche un attaquant de ré-envoyer un message valide ! Ceci peut avoir son importance si ce message vous envoie de l'argent...

Le MAC ne prévient pas ce genre de soucis directement mais on peut, à la place de signer uniquement $m$, signer $ m || T$ où $T$ est :

- un numéro de transaction
- un code temporel

C'est ensuite à l'application réceptrice du message de vérifier que le message est bien valide et n'a pas été ré-envoyé.

### Comment créer des MAC

{% note "**MAC à taille fixe**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une PRF, alors :

- $S(k, m) = F(k, m)$
- $V(k, m, t) = (F(k, m) == t)$

Est un MAC sécurisé pour tout message de taille $n$.
{% endnote %}
{% details "preuve" %}

Soit $F$ une PRF, $(S, V)$, le MAC qui lui est associé et $A$ un algorithme efficace permettant de gagner au jeu *existential forgery against a chosen message attack* contre $(S, V)$ avec une probabilité $\epsilon(n)$.

Soit $H$ une fonction réellement aléatoire et $(S^\star, V^\star)$, le MAC qui lui est associé. L'algorithme $A$ ne peut gagner au jeu qu'avec une probabilité inférieure à $1/2^n$ puisque $H$ est uniformément répartie.

On peut maintenant créer un algorithme efficace jouant au jeu de la distinguabilité pour la PRF F :

```
    testeur ND                                     adversaire
    -----------                             -------------------------
 b  |         |             m               |              ------   |
--->|  k, H   |<----------------------------|--------------|    |   |
    |         |  F(k, m) si b=1 sinon H(m)  |              |    |   |
    |         |-----------------------------|------------->|    |   |
    |         |                             | m'   (m', t) | A  |   |
    |         |<----------------------------|---  <--------|    |   |
    |         | F(k, m') si b=1 sinon H(m') | r            ------   |    
    |         |-----------------------------|--->                   | rép(b) = (r == t)
    |         |                             |                       |------------------->   
    -----------                             -------------------------
```

Cet adversaire est efficace puisque A l'est et comme A gagne avec un avantage :

- $\epsilon(n)$ si la sortie est la PRF : $D(F(k,\cdot)) = \epsilon(n)$
- inférieur à $1/2^n$ si la sortie est la fonction aléatoire : $D(f) \leq 1/2^n$

L'avantage de l'adversaire pour le jeu de la non distinguabilité est supérieur à $\epsilon(n) - 1/2^n$. Comme $F$ est une PRF cet avantage ne peut être que négligeable et donc $\epsilon(n)$ est négligeable.

{% enddetails %}

Taille non fixée :

1. concaténation avec compteur
2. xor

> TBD : gaffe si pas de compteur on peut forger un message.
> TBD : gaffe au padding si cte pas ok. '10000' utilisé ou 'nnnnnn' avec n taille du message.

## Hash cryptographique

{% lien %}
[Hash cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)
{% endlien %}

> pas de clé. donc la sécurité doit venir d'autre part.
> 
> résistant à la collision
>

> TBD reprendre la déf ci-dessous et la remettre avec non collision
{% note "**Définition**" %}
Une fonction de hachage $f$ doit avoir les pro propriétés suivantes pour être  ***cryptographique***:

1. elles doivent être utiles (déterministe, facilement calculable et uniforme)
2. une petite modification de l'entrée doit produire une grosse modification du hash
3. en connaissant une valeur de hash $h$ il est très difficile de retrouver un $a$ tel que $f(a) = h$
4. en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% endnote %}

### Usage

La non collision permet de stocker les sha plutôt que les valeurs exactes :

- mots de passe
- git

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.

ajout de salt : taille du sel ?

### Comment créer des hash cryptographiques

#### taille fixée


#### taille non fixée

[Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd) : MD4, MD5, SHA-1 et SHA-2.

[Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)
sponge paradigme : SHA-3

### Attaque

> TBD attaque [differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)
> TBD attaque brute force par anniversaire


> 

Ici l'utilité réside dans le fait qu'en pratique :

- la fonction de hash est une injection
- il est impossible de trouver un objet ayant un hash donné.

La fonction de hash ($f$) peut alors être utilisée comme une serrure ($x$) qui ne s'ouvre que si l'on a la bonne clé (un $a$ tel que $f(a) = x$).

Craquer une fonction hash cryptographique revient soit :

- à pouvoir trouver 2 éléments $a$ et $a'$ tels que $f(a) = f(a')$ : trouver des collision montrerait que la fonction n'est pas injective et donc $a$ n'est pas une clé unique
- pouvoir trouver $a$ tel que $f(a) = x$ en ne connaissant que $x$ : revient à forger une clé en ne connaissant que la serrure.

> TBD : attaque par date d'anniversaire en modifiant 2 documents de façon aléatoire (ajouter des espaces/entrée, backspace, ...).
> by the way : toujours modifier un document que l'on signe, du coup on est dan le trouver un identique.