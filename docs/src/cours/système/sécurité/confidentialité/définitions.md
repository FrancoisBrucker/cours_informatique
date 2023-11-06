---
layout: layout/post.njk

title: Définitions de la confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous avons démontré précédemment que le code de Vernam est inviolable sans la connaissance de la clé. Mais y en a-t-il d'autres ?

[Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon#Information_theory), dans son article séminale de 1949 sur la théorie de l'information donne une définition d'un code assurant une confidentialité parfaite :

{% note "**Définition**" %}
Un code $(E, D)$ assure une ***confidentialité parfaite*** si :

- la clé $k$ est uniforme $k \xleftarrow{R} \mathcal{K}$
pour tous messages $m$ et $m'$ de même taille et tout chiffre $c$ :

<div>
$$
Pr[E(k, m) = c] = Pr[E(k, m') = c]
$$
</div>

{% endnote %}

Un code assurant une confidentialité parfaite ne doit donner aucune information sur $k$ ou $m$ en ne sachant que $E(k, m)$, ce qui se traduit par le fait que :

- tout message peut donner un chiffre donné si on choisit la bonne clé
- et avec la même probabilité

{% note "**Théorème**" %}
Le code de Vernam assure une confidentialité parfaite.
{% endnote %}
{% details "preuve" %}

La variable aléatoire $(k \xleftarrow{R} \mathcal{K}) \oplus m$ est uniforme quelque soit $m$ : la probabilité d'obtenir n'importe quel chiffre est ainsi une constante et vaut $\frac{1}{\vert C\vert}$ ce qui est indépendant de $m$.

{% enddetails %}

## jeu du chiffrement

La confidentialité parfaite peut s'écrire sous la forme d'un *jeu* où si un adversaire présente deux messages et qu'on lui en rend un des deux chiffré, il ne peut déterminer lequel c'est avec ue probabilité supérieure à $1/2$.

Formalisons ce jeu à deux joueurs :

- un ***adversaire*** qui essaie de trouver une information
- un ***testeur*** qui fournit des données à l'adversaire.

Le jeu consiste alors en 6 étapes :

1. le testeur choisit uniformément une clé $k$
2. un bit $b \in \\{0, 1\\}$ est fournit au testeur choisi de façon uniforme
3. l'adversaire **choisit** deux messages $m_0$ et $m_1$ à donner au testeur
4. le testeur renvoie à l'adversaire $E(k, m_b)$
5. l'adversaire répond un bit $b'$
6. l'adversaire :
   - gagne si $b = b'$
   - perd si $b \neq b'$

```
    
     testeur                      adversaire
    ---------        m0, m1      ------------
 b  |   k   | <----------------- |          |  rép(b) = b'
--->|       |       E(k,mb)      |          | ------------>
    |       | -----------------> |          |
    ---------                    ------------
```

L'adversaire possède un ***[avantage](https://en.wikipedia.org/wiki/Advantage_(cryptography))*** si la probabilité que rép(b) coïncide avec $b$ est supérieure à 1/2 :

{% note "**Définition**" %}
L'avantage dans un jeu est définit telle que :

$$
2\cdot \vert Pr[rép(0) = 1] - Pr[rép(1) = 1] \vert - 1
$$

L'avantage est une mesure allant de 0 (pas d'avantage) à 1 (l'adversaire gagne tout le temps).
{% endnote %}

{% info %}
On a bien sur : $\vert Pr[rép(0) = 1] - Pr[rép(1) = 1] \vert = \vert Pr[rép(0) = 0] - Pr[rép(1) = 0] \vert$
{% endinfo %}

On a clairement que :

{% note %}
Confidentialité parfaite et avantage nul au jeu du chiffrement sont deux notions équivalentes.
{% endnote %}

Shannon montre cependant que cette définition est trop restrictive en pratique :

{% note "**Théorème**" %}
Un code à confidentialité parfaite nécessite un nombre de clés différentes supérieure ou égale au nombre de messages à chiffrer.
{% endnote %}
{% details "preuve" %}

Soit $k^{\star} \in K$, $m^{\star} \in M$ et notons $c^{\star} = E(k^{\star}, m^{\star})$. L'ensemble $M' = \\{m \vert E(k, m)=c^{star}, k \in K\\}$ doit être égal à $M$ pour garantir la confidentialité parfaite et comme sa taille est plus petite que $\vert K \vert$, il faut que $\vert K \vert \geq \vert M \vert$

{% enddetails %}

De là, tout comme le code de Vernam, si on encode des mots de $\\{0, 1\\}^L$, il faut que la taille de la clé soit plus grande que $L$.

Ceci rend les code à confidentialité parfaite inutile en pratique : si on peut se partager un secret de taille $L$, pourquoi ne pas directement se partager le message ?

Il faut donc :

1. relâcher la contrainte de confidentialité parfaite
2. assumer que l'on donnera de toute façons des informations à l'adversaire.
3. faire en sorte de quantifier la quantité d'information consentie.

> TBD : On sait qu'il vq y avoir un avantage, mais encore faut-il pouvoir le trouver puis l'exploiter en temps polynomial

## Sémantiquement Sécurisée

On suppose que :

- les adversaires n'ont à leurs dispositions que des algorithmes ***efficaces***, c'est à dire polynomiaux
- qu'on ne veut consentir qu'un avantage ***négligeable***

{% note "**Définition**" %}
Une fonction $f(n)$ est ***négligeable*** si $f(n) = \mathcal{O}(1/n^d)$ pour tout entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

De ces considérations on peut définir :

{% note "**Définition**" %}
Une méthode de chiffrement est ***sémantiquement sécurisée*** (*Semantically secured*) si tout algorithme efficace ne peut obtenir qu'un avantage négligeable au jeu du chiffrement.
{% endnote %}

{% lien %}
[Indistinguabilité calculatoire](https://fr.wikipedia.org/wiki/Indistinguabilit%C3%A9_calculatoire)
{% endlien %}

{% note "**Définition**" %}
Le couple $(E, D)$ d'algorithmes efficaces est une ***méthode de chiffrement sémantiquement sécurisée*** si :

- $D(k, E(k, m)) = m$
- tout algorithme efficace n'a qu'un avantage négligeable au jeu du chiffrement.
{% endnote %}

## En pratique

La négligeabilité permet de définir théoriquement les avantages que l'on peut accepter de la part de l'adversaire.

### Valeurs numériques

Le gain ne doit pas permettre de créer des algos en effectuant l'algorithme $1/\epsilon$ fois.

Si plus petit que $1/2^{30}$ pas ok. Cela ne fait d'un millions de fois. On peut considérer que $1/2^{80}$ ça devient raisonnable et devient comparable au brute force.

### Négligeable

Propagation de la négligeabilité :

- $p(n) \cdot \epsilon$ reste négligeable si $\epsilon$ l'est
- $\epsilon + \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont

On utilise le chiffre de Vernam mais notre générateur aléatoire n'est pas parfaitement uniforme, il va donner 1 avec une probabilité 1/2 + $\epsilon$.

On chiffre avec un biais $\epsilon$

- $m_0 = 0.....0$
- $m_1 = 1....1$

On regarde $c$ et on rend 0 s'il y a plus de 0 que de 1. Comme il y aura $n\epsilon$ plus de 1 que l'uniforme, notre avantage est de $n\epsilon$ qui reste négligeable si $\epsilon$ l'est.

{% lien %}
Exemple tiré de :
<https://www.di.ens.fr/brice.minaud/cours/2019/MPRI-1.pdf>
à partir de la page 20
{% endlien %}

## Chiffre utilisable en pratique

Réciproquement, pour qu'une méthode de chiffrement puisse être utilisé en pratique, il faut pouvoir avoir deux choses :

- des clés de petites tailles par rapport au message à faire passer
- des algorithmes de complexité linéaires pour chiffrer et déchiffrer les messages.

Même si on s'autorise théoriquement des algorithmes polynomiaux, en pratique, efficaces veut plutôt dire linéaire car il faut que ces algorithmes puissent chiffrer de très nombreuses données. Efficace prend donc deux significations différentes, selon que l'on cherche à prouver théoriquement des résultats où que l'on veuille en pratique chiffrer des données. L'un ne va cependant pas sans l'autre.

Ces deux contraintes vont forcément nous faire passer des informations à l'adversaire. Selon le type d'information que l'on ne veut pas divulguer on va utiliser une méthode plutôt qu'une autre.
