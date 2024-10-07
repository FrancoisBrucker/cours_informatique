---
layout: layout/post.njk

title: Codes historiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



En analysant 4 codes historiques, on verra quelques concepts utile pour l'analyse.

## Code de césar

### <span id="César-chiffre"></span>Chiffrement

Chaque lettre est décalée dans l'alphabet :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m) &=& m + k \mod 26\\
    D(k, c) &=& c - k \mod 26\\
  \end{array}
\right.
$$
</div>

{% info %}
Le [ROT(13)](https://fr.wikipedia.org/wiki/ROT13), César où $k=13$ est l'ancêtre du floutage NSFW.
{% endinfo %}

Le code de César est un exemple de ***Codage par flux*** (*stream cipher*) : chaque lettre est chiffrée une à une avec le même algorithme.

### <span id="César-analyse"></span>Cryptanalyse

1. Ne résiste pas au calcul exhaustif des clés : 26
2. Ne résiste pas à l'analyse en [fréquence de chaque lettre](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d'apparition_des_lettres)

> TBD : le montrer

## Vigenère

### <span id="Vigenère-chiffre"></span>Chiffrement

Remplace la clé unique par un tableau de clés $k =[k_0,\dots, k_{p-1}]$

Le chiffrement de $m = m_0 \dots m_L$ en $c = c_0 \dots c_L$ de fait avec l'équation :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m_i) &=& m_i + k_{(i \mod p)} \mod 26\\
    D(k, c_i) &=& c_i - k_{(i \mod p)} \mod 26\\
  \end{array}
\right.
$$
</div>

Le code de Vigenère est un exemple de ***Codage par blocs*** (*bloc cipher*) :  : chaque bloc de $p$ lettres est codé avec le même algorithme.

### <span id="Vigenère-analyse"></span>Chiffrement

{% lien %}
[Chiffre de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)
{% endlien %}

1. Calcul exhaustif des clés : $26^p$, si $p \geq 30$ alors environ $2^{128}$ opérations, c'est safe.
2. si la clé est choisie de façon aléatoire, par bloc cela semble sécurisé, chaque lettre peut équiprobablement être choisie. Mais :
   1. si on a la taille on refait de l'analyse par fréquence
   2. [on peut trouver la taille](https://www.bibmath.net/crypto/index.php?action=affiche&quoi=poly/viganalyse)

> TBD : le montrer
> <https://www.youtube.com/watch?v=yHXOnCKh4iE>

### One time Pad (OTP)

L'idée est de faire un Vigenère avec comme taille de clé le message !

C'est la technique du :
{% lien %}
[masque jetable](https://fr.wikipedia.org/wiki/Masque_jetable), *One Time Pad*.
{% endlien %}

Technique utilisée pour le téléphone rouge lors de la guerre froide.

{% info %}
[Chiffre du Che](https://www.bibmath.net/crypto/index.php?action=affiche&quoi=moderne/che)
{% endinfo %}

> TBD en faire un.

## Chiffre Vernam

La version informatisée du OTP est appelée [chiffre de Vernam](https://www.cryptage.org/vernam.html).

Ici les messages, les chiffres et les clés sont des mots de $\\{0, 1\\}^L$ et on a, avec $\oplus$ le ou exclusif binaire :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m) &=& k \oplus m\\
    D(k, c) &=& E(k, c) = k \oplus c\\
  \end{array}
\right.
$$
</div>

On a bien $m = k \oplus c$ puisque $k \oplus k \oplus m = m$.

> TBD en faire un.

Intuitivement, comme $k$ peut être ce que l'on veut, $k \oplus m$ l'est aussi. En particulier pour tous $m$ et $c$ on peut trouver $k$ tel que $c = k \oplus m$ (il suffit de prendre $k = c \oplus m$).

En conséquence, un attaquant devant un message crypté de peut le décrypter s'il ne connaît pas $k$ puisque $m$ pouvant être tout élément de $\\{0, 1\\}^L$

Formalisons cette intuition.

{% note "**Théorème**" %}
Si $X$ et $Y$ deux variables aléatoires indépendantes sur $M = \\{0, 1\\}$ et telle que $X$ soit uniforme.

Alors la variable aléatoire $X \oplus Y$ est uniforme sur $\\{0, 1\\}^L$
{% endnote %}
{% details "preuve", "open" %}
Plaçons nous à un index $i$ fixé. On a :

- $Pr[X_i = 0] = Pr[X_i = 1] = .5$ car la variable aléatoire $X$ est uniforme et il y a exactement la moitié de M dont le $i$ème indice vaut 0 (pour l'autre moitié cet indice vaut 1).
- $Pr[Y_i = 0] = p_i$ et donc $Pr(Y_i = 1) = 1-p_i$

Comme $(X \oplus Y)_i$ vaut 0 que si $X_i$ et $Y_i$ valent conjointement 0 ou 1, on en déduit que :

$$
Pr[(X \oplus Y)_i = 0] = Pr[X_i = 0, Y_y = 0] + Pr[X_i = 1, Y_y = 1]
$$

Comme $X$ et $Y$ sont indépendants, $X_i$ et $Y_i$ le sont également et on a : $Pr[X_i = a, Y_y = b] = Pr[X_i = a]\cdot Pr[Y_y = b]$. Donc :

- $Pr[X_i = 0, Y_y = 0] = Pr[X_i = 0]\cdot Pr[Y_y = 0] = .5\cdot p_i$
- $Pr[X_i = 1, Y_y = 1] = Pr[X_i = 1]\cdot Pr[Y_y = 1] = .5\cdot (1-p_i)$

Ce qui entraîne que $Pr[(X \oplus Y)_i = 0] = Pr[X_i = 0, Y_y = 0] + Pr[X_i = 1, Y_y = 1] = .5$, et donc que $(X \oplus Y)$ est une variable aléatoire uniforme.

{% enddetails %}

On déduit du résultat précédent que si la clé est une variable aléatoire uniforme indépendante du texte à chiffré, le chiffre $c$ ne donne aucune information sur $m$. Ce résultat est remarquable car il ne présuppose rien sur le message $m$ et prouve bien l'inviolabilité du code de Vernam.

Enfin, un chiffre $c$ peut être issu de n'importe quel message original $m$, il suffit de choisir $k = c\oplus m$.

{% note %}

Ceci pose les bases que tout code doit avoir une clé choisie uniformément et indépendante du message.

{% endnote %}

Attention cependant.

### Ne répétez pas la clé

La code de Vernam est inviolable si on ne possède aucune information supplémentaire. Si on chiffre deux messages différents avec la même clé $k \oplus m$ et $k \oplus m'$, Eve na qu'à combiner les deux messages chiffrées pour faire disparaître la clé : $k \oplus m \oplus k \oplus m' = k \oplus k \oplus m \oplus m' = m \oplus m'$. De là, si Eve sait que le message est en Français, il lui suffit de déplacer des mots sur le code pour voit apparaître d'autres mots :

```
  Je suis très bien protégé
+ Il mangeait des escargots
  XXXXXXXXXXXXXXXXXXXXXXXXX
```

En faisant glisser "suis" par exemple, lorsqu'il arrive sur l'emplacement de la première ligne on obtient :

```
     suis
  Je suis très bien protégé
+ Il mangeait des escargots 
  XXXmangXXXXXXXXXXXXXXXXXX
```

Ce qui nous donne :

- une position dans le premier mot
- un début de mot dans la seconde phrase que l'on peut chercher à completer

```
     mangeait
  Je suis très bien protégé
+ Il mangeait des escargots 
  XXX        XXXXXXXXXXXXXX
     suis trè 
```

Et petit à petit on casse le chiffre....

{% info %}
C'est arrivé en vrai.
[Projet Venona](https://fr.wikipedia.org/wiki/Projet_Venona)

{% endinfo %}

### <span id="Vernam-intégrité"></span>Intégrité

Si le message est inviolable, il n'est pas infalsifiable.

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
------------------------------
  YYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

Certes. Mais je peux ajouter des informations si je le désire

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
------------------------------
  YYYYYYYYYXXXXXXXXYYYYYYYYYYY
```

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
+ 0000000009999999€00000000000
------------------------------
  YYYYYYYYYZZZZZZZZYYYYYYYYYYY
```

Ce qui est donne une fois déchiffré :

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
+ 0000000009999999€00000000000
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
------------------------------
  Je donne 9999999€ à François
```

Ce qui est super Sympa de votre part !

Ça à l'air un peu tiré par les cheveux vu comme ça, mais si vous chiffrés des mails par exemple, ils commencent tous par un champ `FROM` et un champ `TO`, si le cryptanalyse sait ce que vous codez et que c'est issu d'un protocole, il y a de forte chances qu'il y ait des paramètres à emplacement fixe que l'on peut modifier.
