---
layout: layout/post.njk

title: Hash cryptographique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Pour être utilisable en cryptographie, les [fonctions de hash](/cours/algorithme-code-théorie/théorie/fonctions-hash) doivent cependant avoir [des propriétés spécifiques](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique) :

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

## Usage

### Vérification de l'intégrité d'un fichier

Si l'on connaît le hash d'un fichier et qu'il est impossible de le modifier en conservant le même hash. On peut être sur qu'un fichier n'a pas été modifié. Dans ce cadre là, on appelle cette valeur de hash le [checksum ou somme de contrôle](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le)

### Stockage des mots de passes

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.

[hash et sécurité](https://www.youtube.com/watch?v=b4b8ktEV4Bg)

checksum vs empreinte
ajout de salt : taille du sel ?

hash : comment et pourquoi faire.

## tbd

[differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)

## Comment

Plusieurs méthode de hash cryptographique existent. On peut en citer deux, issues de sha :

- [sha-1](https://fr.wikipedia.org/wiki/SHA-1) utilisé par git mais plus trop de façon cryptographique
- SHA256 (protocole [sha-2](https://fr.wikipedia.org/wiki/SHA-2))

{% info %}
On recommande actuellement d'utiliser l'algorithme SHA256 ou SHA512 pour un usage cryptographique.
{% endinfo %}

Ils sont directement utilisable :

- [sous mac](https://fre.applersg.com/check-sha1-checksum-mac-os-x) et [linux](https://www.lojiciels.com/quest-ce-que-shasum-sous-linux/) avec le programme `shasum`
- [sous windows](https://lecrabeinfo.net/verifier-integrite-calculer-empreinte-checksum-md5-sha1-sha256-fichier-windows.html) avec la commande [Get-FileHash](module) sous powershell.


## SHA

> [sha](https://www.youtube.com/watch?v=DMtFhACPnTY

[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

- SHA-1 : checksum (git ?). Attention, <https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html>. [Gitlab passe à sha-256](https://about.gitlab.com/blog/2023/08/28/sha256-support-in-gitaly/) pour ses hash
- SHA-256/512 : empreinte (crypto ?)

[Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd) : MD4, MD5, SHA-1 et SHA-2.

[Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)
sponge paradigme : SHA-3

## à quoi ça sert

> hash : correction (bit de parité, reed Solomon code)
> hash : checksum : rapide
> hash : cryptographie : sécure
