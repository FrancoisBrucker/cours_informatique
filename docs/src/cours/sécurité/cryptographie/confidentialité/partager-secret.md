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
   - Alice construit le secret $K = B^a \bmod p = g^{ab} \bmod p$
   - Bob construit le secret $K = A^b \bmod p = g^{ab} \bmod p$

Au final, Alice et Bob partagent un nombre $K$ compris entre $0$ et $p-1$.
{% endnote %}

## Pourquoi ça marche

1. si $n$ est premier, [$(\mathbb{Z}/p\mathbb{Z}^{\star}, \cdot)$ est un groupe cyclique](/cours/misc/corps-ZpZ/#groupe-cyclique){.interne}
2. il est très facile de faire [l'exponentiation modulaire](/cours/misc/corps-ZpZ/#exponentiation-modulaire){.interne} dans le cas général et encore plus rapide en notation binaire
3. [le logarithme discret](/cours/misc/corps-ZpZ/#logarithme-discret){.interne} est une opération coûteuse

### Existence

Comme $g$ est un générateur d'un groupe cyclique, on peut donc avoir tout le monde en temps que $g^a$

$ab$ permet bien d'obtenir tout nombre $q$ entre $0$ et $p-1$ car :

- soit $q$ n'est pas premier et $q=ab$ avec $a$ et $b$ plus petit que $p$
- soit $q$ est premier et $p+q$ est pair, donc composé, et il existe $a$ et $b$ plus petit que $p$ tel que $ab = p + q$.

### Algorithme de transmission

L'exponentiation modulaire peut s'écrire comme [l'exponentiation indienne](/cours/algorithmie/projet-exponentiation/étude-algorithmique/){.interne} en utilisant le principe dit de "_square and multiply_" :

```pseudocode
algorithme expo(x: entier, y: entier) → entier:
    r := 1
    tant que y > 0:
        si y est impair:
            r ← r * x mod p     # MULTIPLY
            y ← y - 1
        x ← x * x mod p         # SQUARE
        y ← y / 2
    rendre r
```

En supposant que la complexité de l'addition, la multiplication et le modulo soient de complexité $\mathcal{O}(1)$, la complexité de l'algorithme est en $\mathcal{O}(\log_2(y))$ qui correspond au nombre maximum d'itérations dans la boucle.

{% info %}
En réalité les complexité des opérations arithmétiques ne sont pas en $\mathcal{O}(1)$, mais cela ne change pas le résultat. Pour plus d'info, n'hésitez pas à consulter [cette partie du cours](/cours/algorithmie/fonctions-booléennes/){.interne}
{% endinfo %}

Si $x$, $y$ et $p$ sont stockés sur $n$ bits, la complexité est polynomiale puisque $\log_2(y) \leq n$.

### Problème du logarithme discret

{% lien %}
<https://fr.wikipedia.org/wiki/Logarithme_discret>
{% endlien %}

Trouver $x$ à partir de $y=g^x \bmod p$ n'est pas évident. En effet l'algorithme naif suivant :

```pseudocode
algorithme log(x: entier, y: entier, g: entier) → entier:
    r := 1
    pour chaque i de 0 à p-1:
        si r == y:
            rendre i
        r ← r * g mod p
```

est de complexité $\mathcal{O}(p)$ (le nombre maximum d'itérations dans la boucle) en supposant que la complexité de l'addition, la multiplication et le modulo soient de complexité $\mathcal{O}(1)$.

Comme précédemment, si les entiers sont stockés sur $n=\log_2(p)$ bits, la complexité de l'algorithme est maintenant exponentielle par rapport à la taille $n$ de l'entrée : $\mathcal{O}( \cdot 2^{log_2(p)}) = \mathcal{O}( \cdot 2^{n})$. Le nombre de possibilité à essayer va être rédhibitoire, même pour un algorithme très rapide. Par exemple, l'exécution d'un algorithme faisant 1 opération en $10^{-6}$ secondes pour calculer le logarithme discret d'une clé à $64$ bits : il va y avoir de l'ordre de $2^{64}$ opérations. Comme $10^6 \simeq 2^{20}$ il faudra environ $2^{44}$ secondes soit plus de 6 mois.

Attention cependant, le meilleur algorithme n'est souvent pas le naif ! Regardons pas exemple cet algorithme, appelé [Baby step giant step](https://fr.wikipedia.org/wiki/Baby-step_giant-step) qui échange du temps contre de la mémoire.

Son principe est simple.  


1. Si $0 < m < p$, alors la division euclidienne de $x$ par $m$ donne : $x = i \cdot m + j$ avec :

   - $0 \leq i \leq p/m$
   - $0 \leq j < m$

2. On a $y=g^x \mod p$ si et seulement si : $g^i = y \cdot ((g^{-1})^m)^j$

Ce qui donne :

```pseudocode
algorithme steps(y: entier, g: entier) → entier:
    d := Dict<entier, entier>()
    c := 1
    
    pour chaque i de 0 à p/m:       # baby step
        d[c] = i
        c ← g * c 

    si y est une clé de d:          # g^i = y  => x = i * m + 0
        rendre d[y] * m

    c ← expo(expo(g, n-2), m)       # 1/g = g^(n-2) puisque g^(n-1) = 1 (petit thm Fermat)

    pour chaque j de 1 à m-1:       # giant step
        y ← y * c
        si c est une clé de d:  # g^i = y  => x = i * m + j
            rendre d[y] * m + j
```

La complexité de l'algorithme est alors clairement de :

- $\mathcal{O}(m)$ en mémoire pour stocker toutes les valeurs dans le dictionnaire
- $\mathcal{O}(m + p/m)$ en moyenne pour la complexité pour parcourir les 2 boucles et les test (en moyenne du dictionnaire)

Pour ne pas favoriser une boucle plutôt qu'un autre on prend $m$ tel que $p/m = m$, c'est à dire $m = \sqrt{p}$.

On obtient alors une complexité en moyenne et en mémoire de $\mathcal{O}(\sqrt{p})$

{% attention2 "**À retenir**" %}
La technique qui consiste à stocker des valeurs intermédiaires pour accélérer le calcul est appelé [compromis temps/mémoire](https://fr.wikipedia.org/wiki/Compromis_temps-m%C3%A9moire) est une technique importante à connaître.

Elle ne fera cependant pas de miracle puisqu'elle est bornée par la taille la mémoire disponible.
{% endattention2  %}

Et tout d'un coup avec notre clé de 64b, notre algorithme n'aura plus besoin que de $2^{32}$ opérations. À raison d'une opération par microseconde, il ne faudra plus que 5 millisecondes pour résoudre le problème !

{% attention2 "**À retenir**" %}
On considère actuellement que si le [nombre de possibilité à tester est supérieur à $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message.
{% endattention2  %}
{% info  %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endinfo  %}

Pour une clé de 128bit et 1 opération par microsecondes :

- l'algorithme naïf prend de l'ordre de $10^{25}$ ans
- l'algorithme baby-step giant step prend de l'ordre de $584942$ ans (ce qui est encore beaucoup mais on change tout de même d'ordre de grandeur).

Les exemples précédents supposent un ordinateur avec un processeur unique et deux algorithmes non optimisés. Pour des algorithmes parallèles et optimisés on peut peut faire bien mieux.

Lorsque la puissance de calcul augmente, il suffit d'augmenter linéairement la taille de la clé puisque cela augmente exponentiellement le nombre de possibilités (doubler la vitesse d'un algorithme permet de traiter dans le même temps de clés à un bit de plus).


{% lien %}
Voir <https://math.mit.edu/classes/18.783/2022/LectureNotes9.pdf> ou encore <https://www.lix.polytechnique.fr/~morain/MPRI/2013/lecture1.pdf> pour d'autres algorithmes de résolution.
{% endlien %}


## Attaque

Il existe beaucoup de types d'attaques possibles. Explicitons-en quelques unes.

### Brute force

La meilleure attaque connue est l'attaque brute force en utilisant [l'algorithme du crible général](https://fr.wikipedia.org/wiki/Logarithme_discret#Algorithmes) qui est une méthode de factorisation.

{% lien %}
<https://github.com/vbsinha/Diffie-Hellman-Attacks?tab=readme-ov-file>
{% endlien %}

Pour un nombre premier de 2058bit, l'attaque brute force en utilisant le crible général prend de l'ordre de $2^{90}$ opérations.

On préconise donc une taille de clé de 4096b actuellement. Voir [ce doc p35](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile).

### Man in the middle

On ne cherche pas à décrypter le code, on se place en intermédiaire de la conversation :

```
    Alice    |     Mallory       |     Bob
    privé    |      public       |    privé
-------------|-------------------|--------------
     M       |                   |
             |                   |
     a ---.  |b' ---.     .--- a'|  .--- b           
          v  |      v     v      |  v
     K <--===|= A ===     === B =|===--> K'           # 2 partages de clé sécurisé
             |                   |
  K ⊕ M = C -|--- C              |
             |     K ⊕ C = M     |  
             |      K' ⊕ M = C' -|----> C'
             |                   |      K' ⊕ C' = M
```

Tout se passe comme si Alice parlait à Bob mais ils parlent tous les deux à Mallory qui fait l'intermédiaire : il se fait passer pour Bob auprès d'Alice et d'Alice auprès de Bob.

Il n'y a a priori aucun moyen de se prémunir de ce genre d'attaque si on ne possède pas un mécanisme d'authentification.


### <span id="side-channel-attack"></span>Side channel attack

L'exponentiation indienne peut s'écrire de façon binaire en utilisant le principe [MULTIPLY and SQUARE](/cours/misc/nombres/#exponentiation).

```
algorithme expo(x: [entier], y: [entier]) → [entier]:
  r := [entier]
  r ← [1, 0 .. 0]         # 64b par défaut 
  pour chaque i de 0 à n-1:
    si y[i] == 1:
      r ← mult(r, x)      # MULTIPLY
    x ← mult(x, x)        # SQUARE
  rendre r
```

On remarque qu'il y a deux fois plus de travail lorsque $y[i]$ vaut 1 que lorsqu'il vaut 0. Il est donc possible de connaître la clé :

- soit en analysant en temps réel le fonctionnement de l'algorithme
- soit en mesurant le temps mis pour réaliser l'algorithme et comparer au mis par le même algorithme avec que des 0 ou des 1 comme clé.

ça a l'air de la science fiction mais c'est tout à fait possible, ne serait-ce qu'en mesurant le courant pris par le processeur !

{% lien %}
[Algorithmes et simple power analysis](https://perso.telecom-paristech.fr/pacalet/HWSec/lectures/side_channels/l-nb.pdf)

{% endlien %}

{% lien %}

- [side channel attack](https://fr.wikipedia.org/wiki/Attaque_par_canal_auxiliaire)
- [cours du MIT](https://www.youtube.com/watch?v=3v5Von-oNUg)
- [exemples de side channel attack](https://www.youtube.com/watch?v=2-zQp26nbY8)
- [channel attack autres exemples](https://www.youtube.com/watch?v=GPwNFrpd1KU)
- [Attaques sur Machines embarquées](https://www.ssi.gouv.fr/agence/publication/combined-fault-and-side-channel-attack-on-protected-implementations-of-aes/)

{% endlien %}

## Utilisation de courbes elliptiques

Un des intérêt du protocole de Diffie-Hellmann est qu'il peut s'écrire sous la forme de courbes elliptiques, ce qui permet de réduire la taille de la clé tout en évitant l'attaque brute force.


> TBD à étoffer !

> TBD <https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/>
> TBD On a besoin que de l'exposant. Cela peut donc se faire dans tout groupe pas obligé d'être dans Z/pZ.
> TDB exemple avec courbe elliptique.
> <https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques>
> TBD taille clé 256b actuellement ([courbe de Bernstein](https://fr.wikipedia.org/wiki/Curve25519))
> Renvoyer à [Courbes elliptiques](/cours/misc/courbes-elliptiques){.interne}
> pour la def et les propriétés basiques d'une courbe elliptique.
