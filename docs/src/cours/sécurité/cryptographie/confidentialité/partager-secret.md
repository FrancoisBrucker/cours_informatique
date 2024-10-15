---
layout: layout/post.njk

title: Partage de secret

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment se partager un secret alors que tout le monde nous espionne ? Le protocole [Diffie-Hellman](https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman) est une solution à ce problème, aidé par le fait que l'on ne sait pas tout faire en algorithmie.

{% lien %}
[le problème en quelques vidéos](https://www.youtube.com/watch?v=NmM9HA2MQGI&list=RDCMUC9-y-6csu5WGm29I7JiwpnA)
{% endlien %}

## Protocole Diffie-Hellman

{% note "**Protocole Diffie-Hellman**" %}
Dans le domaine public :

- $n$ premier
- $g < n$ un générateur du groupe cyclique $(\mathbb{Z}/p\mathbb{Z}^{\star}, \cdot)$

1. Échange de la première partie des clés
   - Alice choisit un nombre $a$ et envoie à Bob $A = g^a \mod p$
   - Bob choisit un nombre $b$ et envoie à Bob $B = g^b \mod p$
2. Constitution des clés :
   - Alice construit le secret $k = B^a \mod p = g^{ab} \mod p$
   - Bob construit le secret $k = A^b \mod p = g^{ab} \mod p$

Au final, Alice et Bob partagent un nombre $k$ compris entre $0$ et $p-1$.
{% endnote %}

## Pourquoi ça marche

> TBD renvoyer à la partie partie groupe Z/pZ du cours. Et groupe cyclique

### Existence

Comme $g$ est un générateur d'un groupe cyclique, on peut donc avoir tout le monde en temps que $g^a$

$ab$ permet bien d'obtenir tout nombre $q$ entre $1$ et $p-1$ car :

- soit $q$ n'est pas premier et $q=ab$ avec $a$ et $b$ plus petit que $p$
- soit $q$ est premier et $p+q$ est pair, donc composé, et il existe $a$ et $b$ plus petit que $p$ tel que $ab = up +q$.

### Problème du logarithme discret

Trouver $a$ à partir de $g^a$ n'est pas évident. On ne sait pas faire efficacement, alors que l'exponentiation va très vite.

> TBD taille clé 2048b actuellement

## Courbes elliptiques

> TBD le protocole fonctionne bien en utilisant des courbes elliptiques plutôt que des nombres.
> TBD introduire les courbes elliptiques à ce moment là
> TBD taille clé 256b actuellement (curve de bernstein)

## Attaque

### Side channel attack

Algorithme square and multiply : deux fois plus de travail pour un bit valant 1 que pour un bit valant 0.

### Brute force

La meilleure attaque connue est l'attaque brute force en utilisant l'algorithme du
[crible général](https://fr.wikipedia.org/wiki/Crible_alg%C3%A9brique) qui est une méthode de factorisation.

{% info %}
Pour un nombre premier de 2058bit, l'attaque brute force en utilisant le crible général prend de l'ordre de $2^{90}$ opérations.
{% endinfo %}
