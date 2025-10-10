---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

Pour chiffrer un message on va utiliser le protocole suivant (on vérifiera plus tard que cela fonctionne bien) :

1. Alice et/ou Bob doivent créer une nombres aléatoires servant de clé.
2. Alice et Bob doivent s'échanger une clé de taille petite par rapport à la taille du message à échanger mais choisie uniformément parmi toutes les clé possibles
3. cette clé doit permettre de générer une clé plus grosse de taille égale au message à échanger
4. on chiffre le message avec le code de Vernam que l'on peut ensuite transmettre

Pour que tout fonctionne sans accros il faut que chaque étape soit "_sécurisée_" (on définira précisément ce terme plus tard) en particulier :

1. il faut pouvoir se partager un secret via un canal public
2. il faut que l'algorithme de génération de clé plus grosse soit connu de tous **mais** que ce soit impossible de connaître la séquence finale si on a pas la clé de départ
3. C'est la seule étape qui pour l'instant est sécurisée si on ne répète pas la clé puisqu'il n'y a pas de différence entre un message chiffré et un mot aléatoire.

## 1. Génération de nombres aléatoires

> TBD le lancer de dés.
Mais ne le faites pas vous même dans votre tête. Les humains ne sont pas bon pour faire du hasard :

{% lien %}
<https://www.youtube.com/watch?v=tP-Ipsat90c>
{% endlien %}

Si on utilise un ordinateur c'est possible :

{% lien %}
<https://www.random.org/>
{% endlien %}

Souvent [dans le processeur](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#ig_expand=5627&cats=Random) ou via le [système d'exploitation](https://en.wikipedia.org/wiki//dev/random) :

```shell
xxd < /dev/random
```

Ou de façon plus "lisible" :

```shell
echo "hasard : "$(base64 </dev/random 2>/dev/null| head -c 100)
```

Mais ce n'est pas simple à faire vraiment.

Utilise des méthodes qui collecte de l'entropie puis la supprime sous la forme de nombres aléatoires

> TBD avec entropie, quantique, etc.

## 2. Partage de clé

{% aller %}
[Partager la clé](partager-secret){.interne}
{% endaller %}

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
