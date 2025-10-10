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

- $p$ premier
- $g < p$ un générateur du groupe cyclique $(\mathbb{Z}/p\mathbb{Z}^{\star}, \cdot)$

1. Échange de la première partie des clés
   - Alice choisit un nombre $a$ et envoie à Bob $A = g^a \bmod p$
   - Bob choisit un nombre $b$ et envoie à Bob $B = g^b \bmod p$
2. Constitution des clés :
   - Alice construit le secret $k = B^a \bmod p = g^{ab} \bmod p$
   - Bob construit le secret $k = A^b \bmod p = g^{ab} \bmod p$

Au final, Alice et Bob partagent un nombre $k$ compris entre $0$ et $p-1$.
{% endnote %}

## Pourquoi ça marche

1. si $n$ est premier, [$(\mathbb{Z}/p\mathbb{Z}^{\star}, \cdot)$ est un groupe cyclique](/cours/misc/corps-ZpZ/#groupe-cyclique){.interne}
2. il est très facile de faire [l'exponentiation modulaire](../../../arithmétique/corps-ZpZ#exponentiation-modulaire){.interne} dans le cas général et encore plus rapide en notation binaire
3. [le logarithme discret](/cours/misc/corps-ZpZ/#logarithme-discret){.interne} est une opération coûteuse

### Existence

Comme $g$ est un générateur d'un groupe cyclique, on peut donc avoir tout le monde en temps que $g^a$

$ab$ permet bien d'obtenir tout nombre $q$ entre $0$ et $p-1$ car :

- soit $q$ n'est pas premier et $q=ab$ avec $a$ et $b$ plus petit que $p$
- soit $q$ est premier et $p+q$ est pair, donc composé, et il existe $a$ et $b$ plus petit que $p$ tel que $ab = p + q$.

### Problème du logarithme discret

{% lien %}
<https://fr.wikipedia.org/wiki/Logarithme_discret>
{% endlien %}

Trouver $a$ à partir de $g^a$ n'est pas évident. On ne sait pas faire efficacement, alors que l'exponentiation va très vite.

> TBD <https://fr.wikipedia.org/wiki/Baby-step_giant-step>
> 
> TBD taille clé 4096b actuellement

> TBD : <https://math.mit.edu/classes/18.783/2022/LectureNotes9.pdf> et <https://www.lix.polytechnique.fr/~morain/MPRI/2013/lecture1.pdf>

> TBD montre l'algo baby step giant step qui fait partie des algos ou on échange du temps contre de la mémoire.
> 
## Attaque

> TBD beaucoup de types d'attaque diff (qui marchent).
> 
> TBD algo, authentification, side channel

### Brute force

La meilleure attaque connue est l'attaque brute force en utilisant [l'algorithme du crible général](https://fr.wikipedia.org/wiki/Logarithme_discret#Algorithmes) qui est une méthode de factorisation.

{% lien %}
<https://github.com/vbsinha/Diffie-Hellman-Attacks?tab=readme-ov-file>
{% endlien %}

Pour un nombre premier de 2058bit, l'attaque brute force en utilisant le crible général prend de l'ordre de $2^{90}$ opérations. Comme on en veut au moins $2^{128}$ pour être en sécurité : on préconise au moins 3000b actuellement.

Voir [ce doc p35](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile).

### Man in the middle

> TBD : pb d'authentification
> faire le dessin.

### <span id="side-channel-attack"></span>Side channel attack


L'exponentiation indienne peut s'écrire de façon binaire en utilisant le principe [MULTIPLY and SQUARE](/cours/misc/nombres/#exponentiation).

```
expo(x, y):
  r = 1
  pour chaque i de 0 à n-1:
    si y[i] == 1:
      r = r * x      # MULTIPLY
    x = x * x        # SQUARE
  rendre r
```

On remarque qu'il y a deux fois plus de travail lorsque $y[i]$ vaut 1 que lorsqu'il vaut 0.

> TBD le temps est aussi double puisque c'est des multiplications.
> dnc si on connait le temps mis pour que des 0 ou que des 1 on sait combien de 1 à la clé.
>
> Mais on peut faire mieux en mesurant le courant !
>
{% lien %}
[Algorithmes et simple power analysis](https://perso.telecom-paristech.fr/pacalet/HWSec/lectures/side_channels/l-nb.pdf)

{% endlien %}

{% lien %}

- [side channel attack](https://fr.wikipedia.org/wiki/Attaque_par_canal_auxiliaire)
- [cours du MIT](https://www.youtube.com/watch?v=3v5Von-oNUg)
- [exemples de side channel attack](https://www.youtube.com/watch?v=2-zQp26nbY8)

{% endlien %}

## Utilisation de courbes elliptiques

> TBD On a besoin que de l'exposant. Cela peut donc se faire dans tout groupe pas obligé d'être dans Z/pZ.
> TDB exemple avec courbe elliptique.

Un des intérêt du protocole de Diffie-Hellman est qu'il peut s'écrire sous la forme de courbes elliptiques, ce qui permet de réduire la taille de la clé tout en évitant l'attaque brute force.

> <https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques>

> TBD taille clé 256b actuellement ([courbe de Bernstein](https://fr.wikipedia.org/wiki/Curve25519))

> Renvoyer à [Courbes elliptiques](/cours/misc/courbes-elliptiques){.interne}
> pour la def et les propriétés basiques d'une courbe elliptique.
