---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien "**Bibliographie**" %}

- "random number generators : principles and practices de David Johnston"
- "Introduction to modern cryptography de Jonathan Katk et Yehuda Lindell"

{% endlien %}

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

> TBD CPRNG -> permutation
> TBD historiquement AES mais maintenant chacha20 (de Bertstein, celui des courbes elliptiques)







## Schéma final de la transmission

Pour qu'une méthode de chiffrement puisse être utilisé en pratique, il faut pouvoir avoir deux choses :

- des clés de petites tailles par rapport au message à faire passer
- des algorithmes de complexité linéaires pour chiffrer et déchiffrer les messages.

Même si on s'autorise théoriquement des algorithmes polynomiaux, en pratique, efficaces veut plutôt dire linéaire car il faut que ces algorithmes puissent chiffrer de très nombreuses données en peu de temps. Efficace prend donc deux significations différentes, selon que l'on cherche à prouver théoriquement des résultats où que l'on veuille en pratique chiffrer des données. L'un ne va cependant pas sans l'autre.

Ces deux contraintes vont forcément nous faire passer des informations à l'adversaire. Selon le type d'information que l'on ne veut pas divulguer on va utiliser une méthode plutôt qu'une autre.


> rappel définition securisé, avantage, etc.




1. Alice et/ou Bob doivent créer un nombre aléatoire de façon uniforme servant de clé.
2. Alice et Bob doivent s'échanger une clé de taille petite par rapport à la taille du message à échanger mais choisie uniformément parmi toutes les clé possibles
3. cette clé doit permettre de générer une clé plus grosse de taille égale au message à échanger (on verra pourquoi)
4. on chiffre le message avec le code de Vernam que l'on peut ensuite transmettre

```
    Alice    |        |     Bob
    privé    | public |    privé
-------------|--------|--------------
      m      |        |     
      k <----|--------|----> k
  G(k) = K   |        |  G(k) = K    
E(K, m) = c -|-- c ---|----> c
             |        | D(K, c) = m
             |        |
```

Pour que tout fonctionne sans accros il faut que chaque étape soit "_sécurisée_" (on définira précisément ce terme plus tard) en particulier :

1. il faut créer une clé uniforme.
2. il faut pouvoir se partager un secret via un canal public
3. il faut que l'algorithme de génération de clé plus grosse soit connu de tous **mais** que ce soit impossible de connaître la séquence finale si on a pas la clé de départ
4. il faut que $c$ soit uniforme pour ne pas

```
           k                   k
           |                   |
           v                   v
        -------             -------
       |       |           |       |
 m --> |   E   | --> c --> |   D   | --> m
       |       |           |       |
        -------             -------
```

Deux types d'attaques :

- brute-force : énumération des clés
- connaissances supplémentaires :
  - _a priori_ sur $m$ si l'attaque est chiffre seul
  - acquises si on peut avoir ou produire des couples (message, chiffre)

On considère actuellement que si le [nombre de clés est supérieur à $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}

## Génération de nombres pseudo-aléatoires

{% lien %}
<https://en.wikipedia.org/wiki/Random_number_generation>
{% endlien %}

Clé initiale doit être uniforme. Puis on étend à la taille du message à chiffrer. En partant d'une clé aléatoire sur $k$ bits un algorithme $G()$ permettant de produire $k <<t$ bits que l'on cherche à être le plus aléatoire possible :

```
  ---------
  | k bit |
  ---------
  :        \
  :         \
  :          \
  :           \
  --------------
  |G(k) à t bits|
  --------------
```

Comme $G$ est un algorithme il est **déterministe** mais si la suite $G(k)$ possède des propriétés statistiques relevant de l'aléatoire, on dira que $G$ est un générateur de nombre pseudo-aléatoire.

Ca existe :

- [les nombres pseudo-aléatoire de python](https://docs.python.org/fr/3.14/library/random.html). Fonctionnent avec une seed.
- le modulo $x_{n+1} = a \cdot x_n + b \pmod p$ avec $p$ un nombre premier.

Ou encore les décimales de pi à partir de la $k$ème
voir des méthodes plus sophistiquée comme [les lsfr](./Rapport_de_Stage_Laura_Michelutti.pdf).

Mais attention doit être "sécurisé" ! On ne doit pas pouvoir prédire la suite à partir d'un échantillon. Ceci peut se faire si un attaquant peut envoyer des messages à chiffrer :

```
  kkkkkkk
+ 0000000
----------
  kkkkkkk
```

On retrouve Xn puis si modulo je connais la suite.

Ces générateur (python, ou encore le modulo avec un entier premier) sont parfait pour prédire le monde physique, les sorties sont bien uniformes et indétectables de l'aléatoire, mais pour les applications crypto on veut en plus non-prédictible.

Du coup $\pi$ marche pas non plus trop (<https://mathoverflow.net/questions/26942/is-pi-a-good-random-number-generator> et <https://www2.lbl.gov/Science-Articles/Archive/pi-random.html>).

Et les lsfr il faut travailler.

{% lien %}
[Différences entre les différents générateur pseudo-aléatoires](https://fr.eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/stream-ciphers/stream-ciphers-random-numbers-and-the-one-time-pad/examination-review-stream-ciphers-random-numbers-and-the-one-time-pad/what-are-the-key-differences-between-true-random-number-generators-trngs-pseudorandom-number-generators-prngs-and-cryptographically-secure-pseudorandom-number-generators-csprngs/)
{% endlien %}

<!-- > TBD TP
>
> - lsfr avec python etc.
> - les décimales de pi :
>   - <https://www.youtube.com/watch?v=FDXf1XxCXAk>
>   - sont aléatoires si tu ne sais pas que c'est elles.
>   - prendre les bits de la représentation binaire des décimales de pi et leur faire passer des tests d'aléatoire. -->

### Nombres pseudo-aléatoires cryptographique

On a utilisé plusieurs fois le terme "sécurisé" avec des notions différentes :

- la sécurité du partage de la clé était basé sur la **difficulté algorithmique** du logarithme discret.
- générateur de nombre pseudo-aléatoire est sécurisé s'il est **non prédictible**

Essayons de formaliser tout ça en une seule définition qui va permettre de créer des système de chiffrement que l'on pourra démontrer sécurisé (au oins en théorie).

{% aller %}
[Définitions de la confidentialité](définitions){.interne}
{% endaller %}

Le message ne doit pouvoir être lu que par son destinataire. Comment partager la clé en secret ?

## Chiffrer un message

Les algorithmes de chiffrement classiques ne permettent pas de chiffrer des message de taille quelconque. Ils sont conçus pour chiffrer des blocs de taille fixes.

### Chiffrer un message de taille fixe

{% aller %}
[Chiffrer un bloc](chiffrer-un-bloc){.interne}
{% endaller %}

### Chiffrer un message de taille quelconque

Il existe historiquement deux types de codes même si les différences commencent à s'estomper entres eux :

- les codes en flux qui vont se comporter comme le code de Vernam
- les code en bloc qui vont découper le message en blocs et chiffrer chacun d'entre eux avec un permutation.

{% aller %}
[Schéma général](./schéma-général){.interne}
{% endaller %}

> <https://www.youtube.com/watch?v=G2TYtN2qJls&list=PLbdXd8eufjyWStIhgGkstZi-cvHhUPatc>
> 
### Attention aux implémentations

Les [side channel attacks](partager-secret/#side-channel-attack){.interne} permettent, on l'a vue, de tirer parie de l'implémentation de l'algorithme pour obtenir un avantage npn négligeable. Pour qu'aucune information ne transparaisse, il faut que l'algorithme :

1. fasse tout le temps la même chose
2. consomme la même énergie
3. ...

Bref, n'implémentez pas vous même les algorithmes, prenez des implémentations éprouvées.

{% lien %}

- [channel attack exemples](https://www.youtube.com/watch?v=GPwNFrpd1KU)
- [Attaques sur Machines embarquées](https://www.ssi.gouv.fr/agence/publication/combined-fault-and-side-channel-attack-on-protected-implementations-of-aes/)

{% endlien %}

## Générer des clés

### Générateur de nombre aléatoire cryptographique

> TBD LSFR

{% lien %}
Rapport de stage sur les codes LSFR : [projet codes LSFR](Rapport_de_Stage_Laura_Michelutti.pdf)
{% endlien %}

### Trouver la clé

Il faut utiliser des générateur avec entropie. Il n'est pas utile de retrouver le nombre ensuite.

> TBD `/dev/random`{.fichier} ou `/dev/urandom`{.fichier}
> TBD : faire grossir partie [aléatoire](aléatoire){.interne}

### Key derivation function

{% lien %}
[Key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function)
{% endlien %}

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque messages. La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (_source key_)
- une constante $CTX$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(\text{SK}, \text{CTX} || i)$, où $i$ est un compteur.
