---
layout: layout/post.njk

title: Message Authentification Code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

## Attaque

### Taille du MAC

Remarquez qu'un MAC peut toujours être attaqué avec une probabilité au moins négligeable. Pour cela, il suffit de générer tous les tag possibles, il y en a $2^h$, pour obtenir une probabilité de succès de $1/2^h$. Ceci impose que la taille du tag doit être supérieure à $\mathcal{O}(\log_2(n))$ pour que l'adversaire ne puisse avoir une attaque brute force avec un gain non négligeable.

### Replay attack

Même s'il est impossible de forger un MAC valide, rien n'empêche un attaquant de ré-envoyer un message valide ! Ceci peut avoir son importance si ce message vous envoie de l'argent...

Le MAC ne prévient pas ce genre de soucis directement mais on peut, à la place de signer uniquement $m$, signer $ m || T$ où $T$ est :

- un numéro de transaction
- un code temporel

C'est ensuite à l'application réceptrice du message de vérifier que le message est bien valide et n'a pas été ré-envoyé.

## Comment créer des MAC

{% note "**MAC à taille fixe**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une PRF, alors :

- $S(k, m) = F(k, m)$
- $V(k, m, t) = (F(k, m) == t)$

Est un MAC sécurisé pour tout message de taille $n$.
{% endnote %}
{% details "preuve" %}

Soit $F$ une PRF, $(S, V)$, le MAC qui lui est associé et $A$ un algorithme efficace permettant de gagner au jeu *existential forgery against a chosen message attack* contre $(S, V)$ avec une probabilité $\epsilon(n)$.

Soit $H$ une fonction réellement aléatoire et $(S^\star, V^\star)$, le MAC qui lui est associé. L'algorithme $A$ ne peut gagner au jeu qu'avec une probabilité inférieure à $1/2^n$ puisque $H$ est uniformément répartie.

On peut maintenant créer un algorithme efficace $B$ jouant au jeu de la distinguabilité pour la PRF F :

```
    testeur ND                                     adversaire
    -----------                             ----------------------
 b  |         |             m               |              ------|
--->|  k, H   |<----------------------------|--------------|    ||
    |         |  F(k, m) si b=1 sinon H(m)  |              |    ||
    |         |-----------------------------|------------->|    ||
    |         |                             | m'   (m', t) | A  ||
    |         |<----------------------------|---  <--------|    ||
    |         | F(k, m') si b=1 sinon H(m') | r            ------|    
    |         |-----------------------------|--->                | rép(b)=(r==t)
    |         |                             |                    |-------------->   
    -----------                             ----------------------
```

Cet adversaire est efficace puisque A l'est et on a les probabilités :

- $Pr[B(F(k,\cdot), 1) = 1] = \epsilon(n)$
- $Pr[B(F(k,\cdot), 0) = 1] \leq 1/2^n$

Son avantage est donc $\epsilon(n) - 1/2^n$. Or $F$ est une PRF cet avantage ne peut être que négligeable : $\epsilon(n)$ est négligeable.

{% enddetails %}

## MAC à taille variable

L'idée est de découper le message en paquets de taille identique et d'appliquer itérativement des MAC à taille fixe. Il faut bien sur encoder tout le message et pas juste une partie, sinon il est facile pour un attaquant de forger un nouveau message ayant même tag qu'un message précédent

### Méthode

Pour garantir un la sécurité du PAD, le plus simple est d'utiliser 2 clés de chiffrement :

- $k_1 = F(k, 0)$
- $k_2 = F(k, 1)$

Puis d'itérer sur des tailles fixe de message

1. on découpe le message en d messages $m_i$
2. $t_0 = 0$
3. $t_i = F(k_1, t_{i-1} \oplus m_i)$
4. si le dernier message est plus petit que $n$ on concatène avec 10000 avant de le chiffrer en $t_l$
5. en fin on applique la seconde clé pour rendre le MAC final : $F(k_2,t_l)$.

### Attention

Il Faut cependant faire **très** attention à ce que l'on fait

#### Place du $\oplus$

1. Faire un XOR de tous les bouts de messages puis appliquer un MAC à taille fixe n'est pas ok non plus car il suffit d'ajouter deux block identiques pour avoir le même XOR
2. faire un MAC sur chaque bout puis un XOR est aussi pas bon puisque l'ordre des paquets n'est pas important dans cette construction : on peut forger un nouveau message ayant même tag en inversant deux bout de messages

#### Padding

Attention à la forme du Padding si le padding est une constante, on peut forger un autre message :

$mi  || 0000$ = même hash que $m_{i+1} || 000$ avec $m_{i+1} = m_i || 0$

On peut par exemple prendre un padding valant :

- 1000000...
- la taille du message nnnnnn

#### Utilisation de deux clés

Si on ne prend pas de seconde clé, ce n'est pas sécurisé :

$(m || t \opus m, t)$ est un nouveau message si $t=F(k, m)$

1. $t_1 = F(k, m)$
2. $t_2 = F(k, t \oplus t \oplus m) = F(k, m) = t$
