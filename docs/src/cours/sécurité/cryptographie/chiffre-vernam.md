---
layout: layout/post.njk

title: Chiffre de Vernam

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La version informatisée du [OTP](../codes-historiques){.interne} est appelée [chiffre de Vernam](https://www.cryptage.org/vernam.html).

Ici les messages, les chiffres et les clés sont des mots de $\\{0, 1\\}^L$ et on a, avec $\oplus$ le ou exclusif binaire.

{% lien %}
Le ou exclusif en plus d'être simple à calculer est plein de super propriétés et c'est pour ça qu'il est utilisé partout :

<https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/xor/>

{% endlien %}

## Définition

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

```shell
❯ echo -n "fascina" | xxd -ps
66617363696e61
❯ echo -n "message" | xxd -ps
6d657373616765
❯ printf "0x%x\n" $((0xb040010080904 ^ 0x66617363696e61))
0x6d657373616765
❯ echo 0x6d657373616765 | xxd -r ; echo
message
❯ 
```

Intuitivement, comme $k$ peut être ce que l'on veut, $k \oplus m$ l'est aussi. En particulier pour tous $m$ et $c$ on peut trouver $k$ tel que $c = k \oplus m$ (il suffit de prendre $k = c \oplus m$).

En conséquence, un attaquant devant un message crypté de peut le décrypter s'il ne connaît pas $k$ puisque $m$ pouvant être tout élément de $\\{0, 1\\}^L$

## Confidentialité parfaite

Formalisons cette intuition.

{% note "**Théorème**" %}
Soit $X$ une variable aléatoire uniforme sur $\\{0, 1\\}$ et $Y_i$ $L$ variables aléatoires ur $\\{0, 1\\}$. On suppose que $X$ est indépendant de $Y_i$ pour tout $i$.

La variable aléatoire $C_1\dots C_L$ telle que $C_i = X \oplus Y_i$ pour tout $i$ est uniforme sur $\\{0, 1\\}^L$
{% endnote %}
{% details "preuve", "open" %}
Plaçons nous à un index $i$ fixé. On a :

<div>
$$
Pr[C_i = 0] = Pr[X = 0, Y = 0] + Pr[X = 1, Y = 1]
$$
</div>

Comme $X$ et $Y_i$ sont indépendants pour tout $i$, on a : $Pr[X = a, Y_i = b] = Pr[X = a]\cdot Pr[Y_i = b]$. Donc :

- $Pr[X = 0, Y_i = 0] = Pr[X = 0]\cdot Pr[Y_i = 0] = .5\cdot Pr[Y_i = 0]$
- $Pr[X = 1, Y_i = 1] = Pr[X = 1]\cdot Pr[Y_i = 1] = .5\cdot (1-Pr[Y_i = 0])$

Ce qui entraîne que $Pr[X \oplus Y_i = 0] = Pr[X = 0, Y_i = 0] + Pr[X = 1, Y_i = 1] = .5$, et donc que $X \oplus Y_i$ est une variable aléatoire uniforme.

{% enddetails %}

On déduit du résultat précédent que si la clé est une variable aléatoire uniforme indépendante du texte à chiffrer, le chiffre $c$ ne donne aucune information sur $m$. Ce résultat est remarquable car il ne présuppose rien sur le message $m$ et prouve bien l'inviolabilité du code de Vernam.

Enfin, un chiffre $c$ peut être issu de n'importe quel message original $m$, il suffit de choisir $k = c\oplus m$.

{% attention "**À retenir**" %}

Tout code doit avoir une clé choisie uniformément et indépendante du message.

{% endattention %}

[Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon#Information_theory), dans son article séminale de 1949 sur la théorie de l'information donne une définition d'un code assurant une confidentialité parfaite :

<span id="confidentialité-parfaite"></span>

{% note "**Définition**" %}
Un code $(E, D)$ assure une **_confidentialité parfaite_** si pour :

- tous messages $m$ et $m'$ de même taille
- tout chiffre $c$
- les clés $k$ suivent une loi uniforme $k \xleftarrow{U} \mathcal{K}$

On a :

<div>
$$
\Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m) = c] = \Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m') = c]
$$
</div>

{% endnote %}

Un code assurant une confidentialité parfaite ne doit donner aucune information sur $k$ ou $m$ en ne sachant que $E(k, m)$, ce qui se traduit par le fait que :

- tout message peut donner un chiffre donné si on choisit la bonne clé et avec la même probabilité
- un chiffre donné peut être associé à n'importe quel message selon la clé choisie.

{% note "**Théorème**" %}
Le code de Vernam assure une confidentialité parfaite.
{% endnote %}
{% details "preuve", "open" %}

La variable aléatoire $(k \xleftarrow{U} \mathcal{K}) \oplus m$ est uniforme quelque soit $m$ : la probabilité d'obtenir n'importe quel chiffre est ainsi une constante et vaut $\frac{1}{\vert \mathcal{C}\vert}$ ce qui est indépendant de $m$.

{% enddetails %}

Un attaquant n'a aucune idée de ce que peut être le message puisque tout message peut donnée un chiffre donné : il suffit de prendre la clé $k = $c \oplus m$.

## Confidentialité parfaite et taille de clé

La code de Vernam semble parfait il est à la fois rapide à faire et inviolable. Son seul défaut est la longueur de la clé qui doit être la même que celle du message. Mais alors, si on peut se partager un secret de taille $L$, pourquoi ne pas directement se partager le message ?

Ceci est cependant une condition nécessaire et suffisante pour tout code à confidentialité parfaite :

{% note "**Théorème**" %}
Un code à confidentialité parfaite nécessite un nombre de clés différentes supérieur ou égal au nombre de messages à chiffrer.
{% endnote %}
{% details "preuve", "open" %}

Soit $k^{\star} \in \mathcal{K}$, $m^{\star} \in \mathcal{M}$ et notons $c^{\star} = E(k^{\star}, m^{\star})$. S'il existe un message $m'$ tel que $E(k, m') \neq c^\star$ quelque soit la clé $k$ alors $\Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m') = c^\star] = 0 < \Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m^\star) = c^\star]$ et le code ne peut être à confidentialité parfaite.

On en déduit que l'ensemble $\mathcal{M}' = \\{m \vert E(k, m)=c^{\star}, k \in \mathcal{K}\\}$ des messages chiffrés en $c^\star$ doit être égal à $\mathcal{M}$ et comme $\vert \mathcal{M}' \vert \leq \vert \mathcal{K} \vert$ on a que $\vert \mathcal{M} \vert \leq \vert \mathcal{K} \vert$.

{% enddetails %}

Tout code utilisable en pratique aura une taille de clé plus petite que le message, on sera donc **assuré** que de l'information sera donné à l'adversaire. Il faudra s'assurer que cette information ne puisse pas être exploitée facilement.

## Attention aux conditions d'utilisation

Le code de Vernam est à confidentialité parfaite mais il y a des conditions d'utilisation très stricte pour que ce soit vrai. Nous allons montrer ici que si on ne les respecte pas, les conséquences peuvent être désastreuses.

### xor-trick

Attention aux propriétés cachées du $\oplus$. Supposons que $x$ et $y$ soit deux mots de $\\{0, 1\\}^n$ et observez la séquence suivante :

<div>
$$
\begin{array}{l}
x = x \oplus y\\
y = x \oplus y\\
x = x \oplus y\\
\end{array}
$$
</div>

À la fin de ces 3 opérations, les variables $x$ et $y$ ont été échangées !

On utilise les propriétés suivantes, en particulier les 2 dernières :

- $x \oplus y = y \oplus x$
- $(x \oplus y) \oplus z = x \oplus (y \oplus z)$
- $x \oplus x = \mathbb{0}$
- $x \oplus \mathbb{0} = x$

Qui sont évidentes mais est à la base de nombres d'astuces potentiellement dévastatrice pour le secret. voir le lien ci-dessous pour quelques exemples :

{% lien %}
<https://florian.github.io/xor-trick/>
{% endlien %}

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

### Authentification

Rien ne garanti que c'est bien l'expéditeur voulu qui a envoyé le message :

```
           cle k                   cle k'
Alice <-------------> Mallory <--------------> Bob

```

Si Mallory se fait passer d'un côté pour Bob et de l'autre côté pour Alice, aucun des deux ne peut le soupçonner.
