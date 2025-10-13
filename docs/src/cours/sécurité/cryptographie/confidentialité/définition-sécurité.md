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

> TBD 2 types -> temps et méthode.
> TBD temps est

## Sécurisé en temps

Une méthode de chiffrement sera dite $(t, \epsilon)$-sécurisée si tout algorithme passant $t$ secondes à résoudre le problème ne peut réussir à résoudre le problème avec une probabilité supérieure à $0\leq \epsilon \leq 1$.

Comme l'algorithme brute force teste une clé en plus d'une opération, toute méthode de chiffrement sera au maximum $(t, \frac{t}{2^s})$-sécurisée où $s$ est la taille de la clé et $t$ le temps mis pour tester une clé.

{% info %}
On peut aussi mesurer le nombre d'opérations mis pour exécuter l'algorithme puis mesurer sa probabilité de réussite. On aura alors une sécurité définie par nombre d'opérations effectuées.
{% endinfo %}

Il est crucial de garder ceci en tête pour toujours vérifier que la méthode brute force ne soit pas utilisable en pratique.

{% exercice %}
Quelle taille de clé faut-il avoir pour qu'un algorithme brute force tournant pendant 35 ans ne puisse avoir qu'une chance en 100 siècles de déchiffrer un message ?
{% endexercice %}
{% details "corrigé" %}
100 siècles vaut environ $2^{39}$ secondes et 35 ans environ $2^{30}$ secondes. on veut donc que notre méthode soit : $(2^{30}, 2^{-39})$-sécurisée.

L'algorithme étant brute force, on a : $2^{-39} = \frac{2^{30}}{2^s}$ ce qui donne $s = 69$.

Attention, les algorithmes tournent souvent en parallèle pour diminuer leur temps de calcul. C'est pourquoi, actuellement, on recommande des tailles de clés d'au moins 128bits.
{% enddetails %}

> TBD dire si algo expo ok : un algo poly sera inefficace devant un ensemble de solution expo.
> c'est cette notion algorithmique que l'on va utiliser pour quantifier l'information fuitée.
> 
## <span id="sémantiquement-sécurisé"></span>Sémantiquement Sécurisée

> TBD commencer par les distribution à comparer. La fuite est la différence à l'uniforme dans le cas de la confidentialité parfaite. Mais plus généralement à une distribution connue.
> 
La méthode précédente donne idée de la sécurité _actuelle_ d'une méthode de chiffrement puisqu'elle mesure le nombre d'opérations ou le temps pris pour décrypter une méthode de chiffrement. Cela ne dit rien de ce qui pourra se passer dans 5 ou 10 ans lorsque les ordinateurs iront plus vite ou que les méthodes de résolutions seront plus évoluées. De plus, un algorithme brute force qui teste toutes les possibilités aura toujours un avantage de 1 (ou quasi 1 si l'on prend en compte les collisions) si on lui laisse un temps exponentiel par rapport à la taille de la clé pour s'exécuter.

Il faut donc d'un côté :

- trouver une autre mesure que le temps pour déterminer la sécurité,
- ne prendre en compte que les adversaires s'exécutant en temps raisonnable

La solution est d'utiliser la complexité algorithmique et son analyse asymptotique. On considérera alors :

- des clés assez grandes pour que l'attaque brute force nécessite un temps exponentiel non réalisable
- les adversaires qui ont une chances de terminer assez rapidement, c'est à dire ceux dont les algorithmes de résolution sont polynomiaux,
- qu'un avantage est acceptable s'il est  exponentiellement petit par rapport à la taille de la clé.

Par exemple l'algorithme brute force pour lequel on ne lui accorde qu'un nombre d'exécution polynomial, disons $\mathcal{O}(s^d)$, aura un avantage de $\epsilon(s) = \frac{1}{2^{s-d}}$ qui devient exponentiellement petit lorsque la taille de la clé $s$ augmente !

{% note "**Définition**" %}
Pour calculer une complexité, il faut connaître la taille de l'entrée, c'est à dire les informations données à l'adversaire.

De façon classique, la taille de cette entrée ($n$), nommé **_paramètre de sécurité_**, consiste en la taille de la clé (valant $s$) plus la taille du message à chiffrer (valant $t$) :

<div>
$$
n \coloneqq s+t
$$
</div>

{% endnote %}

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


> TBD dépend du temps pour tester 1 clé. Essayons d'en faire abstraction
> .
Définissons formellement les adversaire et les avantages que l'on admet pour qu'une méthode soit sécurisée.

{% lien %}

- [semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
- [fonction négligeable](https://en.wikipedia.org/wiki/Negligible_function)

{% endlien %}

On suppose que :

- les adversaires n'ont à leurs dispositions que des algorithmes **_efficaces_**, c'est à dire polynomiaux
- qu'on ne veut consentir qu'une possibilité de réussite **_négligeable_**

{% note "**Définition**" %}
Une fonction $f(n)$ est **_négligeable_** si $f(n) = \mathcal{O}(1/n^d)$ pour tout entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

De ces considérations on peut définir :

{% note "**Définition**" %}
Une méthode de chiffrement est **_sécurisée_** (_Semantically secured_) si tout algorithme efficace ne peut obtenir qu'un avantage négligeable au jeu du chiffrement.
{% endnote %}

{% lien %}
[Indistinguabilité calculatoire](https://fr.wikipedia.org/wiki/Indistinguabilit%C3%A9_calculatoire)
{% endlien %}

La négligeabilité se compose tout comme la polynomialité (somme et produit de polynôme restent des polynôme) :

- $p(n) \cdot \epsilon$ reste négligeable si $\epsilon$ l'est
- $\epsilon + \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont
- $\epsilon \cdot \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont

## Avantage

> TBD crypto toujours reconnaire au mieux une proba par rapport à une autre.