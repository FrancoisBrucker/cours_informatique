---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le processus d'envoi d'un message confidentiel entre Alice et Bob décrit précédemment doit être ajusté pour être réaliste :

```
    Alice    |  Eve   |     Bob
-------------|--------|--------------
    m, k     |        |      k
E(k, m) = c -|-- c ---|----> c
             |        | D(k, c) = m
             |        |
espace privé | public |    privé
```

On va petit à petit modifier ce schéma pour le rendre utilisable en pratique. Commençons tout d'abord par fixer le code utilisé. On utilise le chiffre de Vernam car il possède deux avantages imbattables :

- il est à confidentialité parfaite
- il est de complexité linéaire et très facile à implémenter

On obtient alors le schéma suivant :

```
    Alice    |  Eve   |     Bob
-------------|--------|--------------
    m, k     |        |      k
  k ⊕ m = c -|-- c ---|----> c
             |        |  k ⊕ c = m
             |        |
espace privé | public |    privé
```

Pour que le chiffre de Vernam fonctionne, il faut que la clé soit générée de façon uniforme. Attelons-nous à ça.

## Génération de clés uniformes

La clé générée doit être uniforme pour qu'un attaquant potentiel ne puisse pas avoir le moindre indice sur celle-ci. Ceci est impossible à faire avec un algorithme qui est par définition déterministe. On utilise ainsi des systèmes physiques (souvent couplés à des algorithmes et intégré directement sur le processeur) appelé _**TRNG**_ pour _True Random Number Generator_ pour cela.

Nous ne rentrerons pas en détail ici sur les moyens de générer de tels nombres, le lecteur intéressé pourra visiter le lien suivant :

{% info %}

Pour en savoir plus :

[_True Random Number Generator_](/cours/misc/aléatoire/nombres-aléatoires){.interne}

{% endinfo %}

Ce qu'il faut en retenir pour nous c'est que :

{% attention "**À retenir**" %}
Générer des nombre vraiment aléatoire avec un ordinateur est possible en utilisant des systèmes physiques embarqués. C'est cependant un processus compliqué et coûteux en temps.
{% endattention %}

## Partager la clé

Il est cependant irréaliste qu'Alice et Bob aient connaissance de la clé avant de se transmettre un message, sinon aucune communication sécurisée ne serait possible entre 2 ordinateurs. Il faut utiliser un moyen pour qu'Alice et/ou Bob puissent générer une clé puis se la transmettre de façon sécurisée.

Ceci est possible en utilisant des problèmes dont que l'on ne sait pas algorithmiquement résoudre efficacement :

{% aller %}
[Partager de secret](partager-secret){.interne}
{% endaller %}

Le schéma de transmission confidentiel devient alors :

```
    Alice    |         |     Bob
    privé    | public  |    privé
-------------|---------|--------------
     m       |         |
             |         |
     a ---v  |         |  v--- b           # générés par un TRNG
     k <--===|= A = B =|===--> k           # protocole de partage de clé sécurisé
             |         |
  k ⊕ m = c -|--- c ---|----> c
             |         |  k ⊕ c = m
             |         |
```

## Notion de sécurité

La sécurisation du protocole de transmission de la clé par le protocole de Diffie-Hellmann dépend de la complexité du meilleur algorithme (connu) permettant de résoudre le problème du logarithme discret. Elle dépend du ratio entre le temps nécessaire pour le décrypter et la durée de vie du message.

Formalisons ce concept avec la notion de fonctions à sens unique.

### Fonctions à sens unique

{% lien %}
[One way function](https://en.wikipedia.org/wiki/One-way_function)
{% endlien %}

En gros, une fonction $f$ est à sens unique s'il est :

- facile de calculer $f(x) = y$ avec un algorithme efficace
- impossible de trouver $x$ sachant $f(y)$ avec un algorithme efficace

Ce qui donne la définition suivante :

{% note "**Définition**" %}
Une fonction $f: {0, 1}^t \rightarrow {0, 1}^t$ dont il existe un algorithme efficace pour la calculer est **_à sens unique_** si pour tout algorithme efficace $A$, la probabilité suivante est négligeable :
<div>
$$
\Pr_{x \xleftarrow{U} \{0, 1\}^t}[f(F(f(x))) = f(x)]
$$
</div>

{% endnote %}

En utilisant les définitions de efficace et négligeable suivantes :

{% note "**Définition**" %}

- une fonction $f(n)$ est **_efficace_** si $f(n) = \mathcal{O}(n^d)$ pour **un** entier $d$.
- une fonction $f(n)$ est **_négligeable_** si $f(n) = \mathcal{O}(1/n^d)$ pour **tout** entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

L'intérêt de cette formalisation est que négligeabilité se compose tout comme l'efficacité (somme et produit de polynôme restent des polynômes) :

- $p(n) + p(n)$ reste efficace si $p(n)$ et $p(n)$ le sont
- $p(n) \cdot p(n)$ reste efficace si $p(n)$ et $p(n)$ le sont
- $\epsilon(n) + \epsilon(n)'$ reste négligeable si $\epsilon(n)$ et $\epsilon(n)'$ le sont
- $\epsilon(n) \cdot \epsilon(n)'$ reste négligeable si $\epsilon(n)$ et $\epsilon(n)'$ le sont
- $p(n) \cdot \epsilon(n)$ reste négligeable si $\epsilon(n)$ l'est et $p(n)$ est efficace

{% attention "**À retenir**" %}

On supposera toujours pour la suite que :

- les adversaires n'ont à leurs dispositions que des algorithmes **_efficaces_**, c'est à dire polynomiaux
- qu'on ne veut consentir qu'une possibilité de réussite **_négligeable_**

{% endattention %}

On voit bien l'intérêt pour le chiffrement de ce type de fonction : on cache dans le résultat d'une fonction ce que l'on veut transmettre. C'est ce qu'on a fait avec le logarithme discret dans le protocole de Diffie-Hellman et que l'on fera avec le problème d la factorisation lorsque l'on étudiera le problème de l'authentification.

Ces deux problèmes sont (très fortement) soupçonnées de faire partie de ce type de fonctions. Seulement soupçonné car on a la proposition suivante :

{% note "**Proposition**" %}
S'il existe des fonctions à sens unique, alors $P \neq NP$
{% endnote %}
{% details "preuve", "open" %}
Dérive directement de ce que l'[on a vu avec le problème SAT](/cours/algorithmie/problème-SAT/#algorithme-SAT){.interne} : il est équivalent pour SAT de trouver une entrée si on a la solution que de trouver la solution si on a une entrée. On a donc l'implication suivante : Si $P = NP$ alors il ne peut exister de fonction à sens unique.
{% enddetails %}

Notez que :

- la réciproque n'est pas démontrée
- il y a très peu de chance qu'on arrive à en exhiber une fonction à sens unique

Tout algorithme de chiffrement est ainsi basé sur des suppositions. Pour éviter de tout construire sur du sable, on cherche à avoir au moins des preuves de constructions pour qu'il suffise de changer un algorithme si devient clair que le problème associé n'est pas à sens unique plutôt que de changer toute la méthode. C'est le but de la section suivante.

### Sémantiquement sécurisé

Si les meilleurs algorithmes de résolution sont connus (ce qui n'est jamais vraiment assuré) on peut déterminer une taille de clé qui garantissent un temps de décryptage trop important. Formalisons cette notion :

{% aller %}
[Sémantiquement sécurisée](définition-sécurité){.interne}
{% endaller %}

## Transmission

La méthode de chiffrement utilisant le code de Verna n'est pas directement utilisable en pratique car, la clé de chiffrement ne devant pas être répétée pour garantir l'inviolabilité du chiffrement, il faudrait utiliser le protocole de Diffie-Hellman pour générer des clés différentes pour chaque partie du message à chiffrer ce qui est trop coûteux en temps et empêcherait.

On utilise donc un générateur de nombre pseudo-aléatoire cryptographique (_Cryptographic Pseudo-Random Number Generator_) pour générer assez de bit à partir de la clé pour chiffrer le message entier :

```
    Alice    |         |     Bob
    privé    | public  |    privé
-------------|---------|--------------
     m       |         |
             |         |
     a ---v  |         |  v--- b           # générés par un TRNG
     k <--===|= A = B =|===--> k           # protocole de partage de clé sécurisé
             |         |
  G(k) = K   |         |  G(k) = K         # générés par un CPRNG
             |         |
  K ⊕ m = c -|--- c ---|----> c
             |         |  K ⊕ c = m
```

{% aller %}
[Nombres pseudo aléatoires cryptographiques](nombres-pseudo-aléatoires-cryptographiques){.interne}
{% endaller %}

Avoir un CPRNG suffit pour garantir un chiffrement de Vernam sémantiquement sécurisé :

<span id="chiffre-CPRNG"></span>

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$ est un  CPRNG, alors :

- $E(k, m) = G(k) \oplus m$
- $D(k, m) = E(k, m)$

est une méthode de chiffrement sécurisée.
{% endnote %}
{% details "preuve", "open" %}

Soit $A$ un algorithme efficace d'aun adversaire du jeu de la reconnaissance avec deux mots $m_0$ et $m_1$. Son avantage vaut :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_2) = 1] \vert\\
&=& \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1]-\\
&& (\Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_2) = 1] -\Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1]) \vert\\
\end{array}
$$
</div>

Comme $u\xleftarrow{U}\\{0, 1\\}^t\oplus m_1$ est une variable uniforme ([on l'a démontré](../chiffre-vernam/#uniforme){.interne}) on a $u\xleftarrow{U}\\{0, 1\\}^t\oplus m_1 = u\xleftarrow{U}\\{0, 1\\}^t\oplus m_2 = u\xleftarrow{U}\\{0, 1\\}^t$ et donc :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1] -\\
&& (\Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_2) = 1] -\Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_2) = 1]) \vert\\
&=& \vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1] \vert +\\
&& \vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_2) = 1] -\Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_2) = 1] \vert
\end{array}
$$
</div>

On peut supposer sans perte de généralité que :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &\leq&2\cdot\vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1] \vert
\end{array}
$$
</div>

L'algorithme $A'$ tel que $A'(x) = A(x \oplus m_1)$ est un algorithme qui reconnaît $G$. Comme $G$ est un CPRNG, son avantage $\epsilon(A')$ ne peut être que négligeable et comme :

<div>
$$
\begin{array}{lcl}
\epsilon(A') &=& \vert \Pr_{k\xleftarrow{U}\{0, 1\}^s}[A(G(k)\oplus m_1) = 1] - \Pr_{u\xleftarrow{U}\{0, 1\}^t}[A(u\oplus m_1) = 1] \vert
\end{array}
$$
</div>

On en déduit que $\epsilon(A)$ est aussi négligeable ce qui conclut la preuve.

{% enddetails %}

## Message de taille variable

Les générateurs de nombres pseudo-aléatoires ne permettent pas de générer des mots de tailles arbitraires. Certains peuvent être très grand (comme les lsfr ou le Blum-blum-shub) d'autres de tailles fixes et petites (chacha20 ne peut produire que des mots de longueur 512b).

Le schéma de transmission se complexifie encore en ajoutant une boucle de chiffrement :

```
    Alice     |         |     Bob
    privé     | public  |    privé
--------------|---------|--------------
     m        |         |
              |         |
     a ---v   |         |  v--- b           # générés par un TRNG
     k <--====|= A = B =|===--> k           # protocole de partage de clé sécurisé
              |         |
---->         |         |
|             |         |
|  G(ki) = K  |         |  G(ki) = K         # générés par un CPRNG
|             |         |
| K ⊕ mi = c -|--- c ---|----> c
|             |         |  K ⊕ c = mi
|             |         |  m = mi || m
----          |         |    
```

Notez qu'il ne faut pas répéter la clé !

{% exercice %}
Montrez que si l'on encode plusieurs parties de message avec la même clé, le chiffre n'est pas sémantiquement sécurisé.

{% endexercice %}
{% details "corrigé" %}
Si l'on utilise deux fois la même clé, si deux portions de messages sont identiques alors ils auront le même chiffre. On peut alors utiliser les messages :

- $m_1 = b_1b_2$
- $m_2 = b_1b_1$

On reconnaîtra $m_1$ de m_2$ avec un avantage de 1.

{% enddetails %}

> TBD refaire l'image p12 <https://crypto.stanford.edu/~dabo/courses/cs255_winter19/lectures/PRP-PRF.pdf>

{% attention %}
Ce mode de chiffrement existe (ECB) est n'est [jamais recommandé](https://fr.eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/applications-of-block-ciphers/modes-of-operation-for-block-ciphers/examination-review-modes-of-operation-for-block-ciphers/how-does-the-electronic-codebook-ecb-mode-of-operation-work-and-what-are-its-primary-security-drawbacks/)

{% endattention %}

Voyons  comment tout ceci peut se faire de façon sécurisée :

Concaténer des blocs de messages chiffrés. On découpe le message à chiffrer $m$ en blocs $m_i$ de taille $t$ fixe que l'on traite séparément.

Plutôt que d'utiliser un générateur on utilise une [fonction pseudo-aléatoire sécurisée](../nombres-pseudo-aléatoires-cryptographiques/#PRF){.interne} (ou une [permutation](../nombres-pseudo-aléatoires-cryptographiques/#PRP){.interne}) dont on a vu que l'utilisation était identique à un générateur mais permettait d'avoir un paramètre de plus, le vecteur d'initialisation.

On va utiliser le schéma suivant pour désigner une PRF (_resp._ une PRP) $F(k, \text{iv})$ :

```
       iv   
        |   
      ----- 
 k-->|  F  |
      ----- 
        |
     F(k,iv)   
```

On a alors le schéma de chiffrement suivant, qui modifie le vecteur d'initialisation en incrémentant un compteur :

```
    iv || 01     iv || 02          iv || i           iv || l
        |            |                 |                 |
      -----        -----             -----             -----
 k-->|     |  k-->|     |  ...  k-->|     |  ...  k-->|     |
      -----        -----             -----             -----
        |            |                 |                 |
 m1---> ⊕     m2---> ⊕          mi---> ⊕          ml---> ⊕ 
        |            |                 |                 |
        v            v                 v                 v
       c1           c2                ci                cl
```

Ce schéma est bien sécurisé si $F$ l'est et que la place prise par le compteur n'est pas trop grande :

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ est une fonction pseudo-aléatoire sécurisée et $m$ un message de taille $l\cdot t$ alors :

<div>
$$
E(k, m) = (F(k, \text{iv} \;\|\; 1) \;\|\;  \dots \;\|\;  F(k, \text{iv} \;\|\; l)) \oplus m
$$
</div>

Est un chiffre sécurisé.
{% endnote %}
{% info %}
L'opérateur $\\;\\|\\;$ est la concaténation.
{% endinfo %}
{% details "preuve", "open" %}

Comme $F$ est une PRF, $F(k, \text{iv} \\;\\|\\; i)$ est indiscernable de la variable aléatoire uniforme pour tout $\text{iv} \\;\\|\\; i$. On peut ensuite utiliser le même schéma de preuve que [la preuve de l'incrémentalité d'un CPRNG](./nombres-pseudo-aléatoires-cryptographiques/#chiffre-CPRNG-incrémental){.interne} et permet de montrer que $(F(k, \text{iv} \;\|\; 1) \;\|\;  \dots \;\|\;  F(k, \text{iv} \;\|\; l))$ est indiscernable de la variable aléatoire uniforme (ici $m$ est au pire égale à la taille $t$ du message qui reste polynomial par rapport au paramètre de sécurité).

{% enddetails %}

Cette construction permet également de chiffrer **et** déchiffrer rapidement le message en parallèle. Il suffit de connaître la clé $k$ et la position du bloc à chiffrer/déchiffrer.

```
    Alice     |         |     Bob
    privé     | public  |    privé
--------------|---------|--------------
     m        |         |
              |         |
     a ---v   |         |  v--- b           # générés par un TRNG
     k <--====|= A = B =|===--> k           # protocole de partage de clé sécurisé
              |         |
--i-->        |         |
|             |         |
| F(k,        |         | F(k,              # PRF
|   iv || i)  |         |   iv || i)
|   = K       |         |   = K             
|             |         |
| K ⊕ mi = c -|--- c ---|----> c
|             |         |  K ⊕ c = mi
|             |         |  m = mi || m
----          |         |    
```

## Nonce

Le vecteur d'initialisation est souvent utilisé comme [NONCE](https://en.wikipedia.org/wiki/Cryptographic_nonce), qui comme son nom l'indique est utilisé une unique fois.

De nombreux protocoles cryptographiques l'utilise pour distinguer des encodages au sein de l'envoi d'un message pour éviter les [attaque par rejeu](https://fr.wikipedia.org/wiki/Attaque_par_rejeu). Le Nonce peut en effet être envoyé en clair, du moment que la clé est secrète.

```
    Alice     |         |     Bob
    privé     | public  |    privé
--------------|---------|--------------
     m        |         |
              |         |
     a ---v   |         |  v--- b           # générés par un TRNG
     k <--====|= A = B =|===--> k           # protocole de partage de clé sécurisé
              |         |
    N --------|---------|----> N            # Nonce    
              |         |                 
--i-->        |         |
|             |         |
| F(k,        |         | F(k,              # PRF
|   N || i)   |         |   N || i)
|   = K       |         |   = K             
|             |         |
| K ⊕ mi = c -|--- c ---|----> c
|             |         |  K ⊕ c = mi
|             |         |  m = mi || m
----          |         |    
```

## Schéma final de la transmission

En utilisant le chirrfre de Vernam, la transmission sécurisée ressemble finalement à ceci :

```
    Alice     |         |     Bob
    privé     | public  |    privé
--------------|---------|--------------
     m        |         |
              |         |
     a ---v   |         |  v--- b           # générés par un TRNG
     k <--====|= A = B =|===--> k           # protocole de partage de clé sécurisé
              |         |
    N --------|---------|----> N            # Nonce    
              |         |                 
--i-->        |         |
|             |         |
| F(k,        |         | F(k,              # PRF
|   N || i)   |         |   N || i)
|   = K       |         |   = K             
|             |         |
| K ⊕ mi = c -|--- c ---|----> c
|             |         |  K ⊕ c = mi
|             |         |  m = mi || m
----          |         |    
```

On appelle ce type de transmission [chiffrement de flux](https://fr.wikipedia.org/wiki/Chiffrement_de_flux), qui est la norme actuellement. Il permet :

- des clés de petites tailles par rapport au message à faire passer
- des algorithmes de complexité linéaires pour chiffrer et déchiffrer les messages.

On considère actuellement que si le [nombre de clés est supérieur à $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}
