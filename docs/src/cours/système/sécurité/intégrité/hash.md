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

{% note "**Définition**" %}

Un ***MAC, Message authentification code*** est constitué d'une paire :

- $S: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^h$ qui ***signe*** en produisant un ***tag*** (en utilisant une clé $k$ un message $m$)
- $V: \\{0, 1\\}^s \times \\{0, 1\\}^n \times \\{0, 1\\}^h \rightarrow \\{0, 1\\}$ qui ***vérifie*** (en utilisant une clé $k$, un message $m$ et son tag potentiel)
- $V(k, m, S(k, m)) = 1$
{% endnote %}

Un MAC est ***sécurisé*** si

> TBD reprendre la déf ci-dessous comme interprétation d'un MAC sécurisé.
> 
{% note "**Définition**" %}
Une fonction de hachage $f$ doit avoir les pro propriétés suivantes pour être  ***cryptographique***:

1. elles doivent être utiles (déterministe, facilement calculable et uniforme)
2. une petite modification de l'entrée doit produire une grosse modification du hash
3. en connaissant une valeur de hash $h$ il est très difficile de retrouver un $a$ tel que $f(a) = h$
4. en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% endnote %}

Ici l'utilité réside dans le fait qu'en pratique :

- la fonction de hash est une injection
- il est impossible de trouver un objet ayant un hash donné.

La fonction de hash ($f$) peut alors être utilisée comme une serrure ($x$) qui ne s'ouvre que si l'on a la bonne clé (un $a$ tel que $f(a) = x$).

Craquer une fonction hash cryptographique revient soit :

- à pouvoir trouver 2 éléments $a$ et $a'$ tels que $f(a) = f(a')$ : trouver des collision montrerait que la fonction n'est pas injective et donc $a$ n'est pas une clé unique
- pouvoir trouver $a$ tel que $f(a) = x$ en ne connaissant que $x$ : revient à forger une clé en ne connaissant que la serrure.

> TBD : attaque par date d'anniversaire en modifiant 2 documents de façon aléatoire (ajouter des espaces/entrée, backspace, ...).
> by the way : toujours modifier un document que l'on signe, du coup on est dan le trouver un identique.

### Comment créer des MAC

#### Taille entrée fixée

> TBD le prf

#### Taille non fixée

## Hash cryptographique

{% lien %}
[Hash cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)
{% endlien %}

> pas de clé. donc la sécurité doit venir d'autre part.
> 
> résistant à la collision
>
### Comment créer des hash cryptographiques

#### taille fixée


#### taille non fixée

[Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd) : MD4, MD5, SHA-1 et SHA-2.

[Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)
sponge paradigme : SHA-3


La non collision permet de stocker les sha plutôt que les valeurs exactes :

- mots de passe
- git

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.

ajout de salt : taille du sel ?

## TBD

> TBD attaque [differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)
> TBD attaque brute force par anniversaire
