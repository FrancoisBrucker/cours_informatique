---
layout: layout/post.njk

title: Sémantiquement sécurisé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La sécurité d'une méthode de chiffrement va dépendre, certes de la méthode employée, mais surtout du temps et des moyens mis en œuvre par l'attaquant.

En effet on a vu que seule une clé égale à la taille du message pouvait garantir [une confidentialité parfaite](../../chiffre-vernam/#confidentialité-parfaite){.interne}, or ceci est irréalisable en pratique puisque deux ordinateurs doivent pouvoir communiquer de façon sécurisée sans s'être au préalable rencontré : toute méthode réaliste de chiffrement va laisser fuiter de l'information.

Enfin comme la taille des clés est finie un algorithme brute force arrivera toujours _in fine_ à casser décrypter le message chiffré. Selon les moyens et les personnes impliquées (d'un adolescent dans sa chambre à un état) cela pourra prendre plus ou moins de temps.

## Sécurisé en temps

{% note "**Définition**" %}
Une méthode de chiffrement est **_$(t, \epsilon)$-sécurisée_** si tout algorithme passant $t$ secondes à résoudre le problème ne peut réussir à résoudre le problème avec une probabilité supérieure à $0\leq \epsilon \leq 1$.
{% endnote  %}

L'intérêt de la $(t, \epsilon)$-sécurité est qu'elle peut se mesurer expérimentalement. Par exemple si un algorithme brute force teste le déchiffrement pour toutes les clés de taille $s$ possibles et met $t$ secondes pour en tester une, sa probabilité de réussite au bout de $T$ seconde sera de $T \cdot (t/2^s)$. Ceci nous donne une borne maximum pour toute méthode de chiffrement :

{% attention "**À retenir**" %}
Toute méthode de chiffrement avec une clé de $s$ bit est au mieux $(t, \frac{t}{2^s})$-sécurisée avec $t$ le temps mis pour déchiffrer un message.
{% endattention  %}

Il est crucial de garder ceci en tête pour toujours vérifier que la méthode brute force ne soit pas utilisable en pratique. Pour cela on commence par déterminer la durée de vie du message chiffré :

{% exercice %}
Quelle taille de clé faut-il avoir pour qu'un algorithme brute force tournant pendant 35 ans ne puisse avoir qu'une chance en 100 siècles de déchiffrer un message ?
{% endexercice %}
{% details "corrigé" %}
100 siècles vaut environ $2^{39}$ secondes et 35 ans environ $2^{30}$ secondes. on veut donc que notre méthode soit : $(2^{30}, 2^{-39})$-sécurisée.

L'algorithme étant brute force, on a : $2^{-39} = \frac{2^{30}}{2^s}$ ce qui donne $s = 69$.

Attention, les algorithmes tournent souvent en parallèle pour diminuer leur temps de calcul. C'est pourquoi, actuellement, on recommande des tailles de clés d'au moins 128bits.
{% enddetails %}

La notion de $(t, \epsilon)$-sécurité est indissociable de l'algorithme qui décrypte et donc de sa complexité. Si l'algorithme est polynomial le ratio entre ce qu'il peut tester (de l'ordre de $\mathcal{O}(n^k)$) et l'espace à tester (de l'ordre de $\mathcal{O}(2^n)$) va très rapidement tendre vers 0 ($10/2^{10}$ vaut déjà 10^{-3}) et si l'algorithme est exponentiel il prendra rapidement trop de temps.

## Paramètre de sécurité

Lorsque l'on calcule la complexité des algorithmes de décryptage on le fait (comme toujours) par rapports à la taille de ses entrées. Les entrées correspondent aux différents paramètres de la méthode de chiffrement :

{% note "**Définition**" %}
Pour calculer une complexité, il faut connaître la taille de l'entrée, c'est à dire les informations données à l'adversaire.

De façon classique, la taille de cette entrée ($n$), nommé **_paramètre de sécurité_**, consiste en la taille de la clé (valant $s$) plus la taille du message à chiffrer (valant $t$) :

<div>
$$
n \coloneqq s+t
$$
</div>

{% endnote %}

Ce paramètre de sécurité permet d'exprimer la $(t, \epsilon)$-sécurité non plus en fonction du temps, mais comme un nombre d'opération. Tout comme le passage de la complexité temporelle (mesurable) à la complexité en nombre d'opérations (calculable) permet une étude plus théorique des performances d'un algorithme, le paramètre de sécurité va nous permettre de comparer les algorithme de déchiffrement de façon générale et abstraite.

Par exemple l'algorithme brute force pour lequel on ne lui accorde qu'un nombre d'exécution polynomial, disons $\mathcal{O}(s^d)$, aura un avantage de $\epsilon(s) = \frac{1}{2^{s-d}}$ qui devient exponentiellement petit lorsque la taille de la clé $s$ augmente !

L'augmentation de la taille des clés va certes avoir un effet sur le temps d'exécution mais ce sera surtout sur l'avantage que cela se fera sentir, s'il est exponentiellement petit par rapport au paramètre de sécurité :

{% exercice %}
On suppose que l'exécution d'un adversaire de complexité temporelle (en secondes) $n^3$ ait un avantage de $\min(1, \frac{2^{40}}{2^n})$.

Pour $n=40$, combien faut-il de temps pour qu'il puisse décrypter la méthode de façon certaine ? Quel est son avantage pour $n=50$ et en combien de temps s'exécute-t-il ?
{% endexercice %}
{% details "corrigé" %}

Pour $n=40$, il aura besoin de $40^3$ secondes pour s'exécuter, c'est à dire un peut moins de 18 heures, et son avantage de sera de 1.

Pour $n=40$, il aura besoin de $50^3$ secondes pour s'exécuter, c'est à dire un peut moins de 35 heures, mais son avantage ne sera plus que de $10^{-3}$.
{% enddetails %}

Autre exemple, où la vitesse de calcul ne bénéficie pas forcément à l'adversaire :

{% exercice %}
Supposons qu'une méthode de chiffrement se chiffre et se déchiffre en $n^2$ opérations et qu'un adversaire possède un algorithme en $n^4$ pour le décrypter.

Soit $n=50$. Si l'on prend un ordinateur qui va 16 fois plus vite, quelle est la taille de $n$ que l'on peut se permettre en gardant le même temps de chiffrement ? Que s'est-il passé pour l'adversaire ?
{% endexercice %}
{% details "corrigé" %}

On cherche $n'$ tel que : $16\cdot 50^2 = n'^2$, c'est à dire $n' = 200$. On a pu augmenter le paramètre de sécurité de 4.

Pour l'adversaire, c'est moins profitable puisque son temps d'exécution est multiplié par $200^4/50^4 = 256$.
{% enddetails %}

Cette méthode permet de formaliser :

- l'utilisation de clés assez grandes pour que l'attaque brute force nécessite un temps exponentiel non réalisable
- l'utilisation d'adversaires dont les algorithmes de décryptage sont polynomiaux,
- que donner de l'information à un attaquant est acceptable s'il est exponentiellement petit par rapport à la taille de la clé.

C'est cette dernière notion que nous allons maintenant formaliser.

## <span id="sémantiquement-sécurisé"></span>Sémantiquement Sécurisée
{% lien %}

- [semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
- [fonction négligeable](https://en.wikipedia.org/wiki/Negligible_function)

{% endlien %}

Commençons par définir une fonction négligeable :

{% note "**Définition**" %}
Une fonction $f(n)$ est **_négligeable_** si $f(n) = \mathcal{O}(1/n^d)$ pour tout entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

L'intérêt de cette formalisation est que négligeabilité se compose tout comme la polynômialité (somme et produit de polynôme restent des polynômes) :

- $p(n) \cdot \epsilon$ reste négligeable si $\epsilon$ l'est
- $\epsilon + \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont
- $\epsilon \cdot \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont

{% lien %}
[Indistinguabilité calculatoire](https://fr.wikipedia.org/wiki/Indistinguabilit%C3%A9_calculatoire)
{% endlien %}

Puis utilisons là pour définir formellement une méthode sécurisée.

{% note "**Définition**" %}
Une méthode de chiffrement est **_sémantiquement sécurisée_** (_Semantically secured_) si elle est $(1, f(n))$-sécurisé avec $f(n)$ une fonction négligeable pour tout algorithme de déchiffrement polynomial.
{% endnote %}

Au final pour construire une méthode de chiffrement :

{% attention "**À retenir**" %}

On supposera toujours pour la suite que :

- les adversaires n'ont à leurs dispositions que des algorithmes **_efficaces_**, c'est à dire polynomiaux
- qu'on ne veut consentir qu'une possibilité de réussite **_négligeable_**

{% endattention %}

## Avantage

> TBD crypto toujours reconnaire au mieux une proba par rapport à une autre.