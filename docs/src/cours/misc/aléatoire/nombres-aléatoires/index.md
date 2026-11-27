---
layout: layout/post.njk

title: Nombres aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- 
> TBD : intro
>
> - <https://www.youtube.com/watch?v=HlnHuEEM5ts>
> - <https://www.youtube.com/watch?v=J5b4lrCCXRI>
> - <https://www.youtube.com/watch?v=4R5xnTAvBgc>
>  -->

{% lien "**Bibliographie**" %}

- "random number generators : principles and practices de David Johnston"

{% endlien %}

{% lien %}

- [une intro](https://www.youtube.com/watch?v=qt4fYKhFhFs)
- [La playlist sur tout ce que vous avez toujours voulu savoir sur les générateurs de nombres aléatoire sans oser le demander](https://www.youtube.com/watch?v=tZse1YyiHdg&list=PLZNqNoh4u1gzKMYgrrgcKK5ozNQ7f_OMP)
{% endlien %}

La solution la plus simple est de faire $n$ pile ou face pour créer un nombre aléatoire à $n$ bits. Cette solution n'est pas réaliste mais il faut utiliser un processus physique quelque-part car tout algorithme est déterministe. Il est également exclu d'utiliser des humains pour générer des suites aléatoire car l'humain n'est pas fait pour reconnaître l'aléatoire : on cherchera à avoir des suite équilibrées de 0 et de 1 ce qui n'est pas du tout aléatoire :

{% lien %}
<https://www.youtube.com/watch?v=tP-Ipsat90c>
{% endlien %}

## TRNG

Il existe des moyens de générer des nombres aléatoire, on appelle ces générateur **_TRNG_** : pour True Random Generator.

> TBD avec des dés plusieurs bits avec 1 lancé : <https://stackoverflow.com/questions/20804899/how-to-generate-an-un-biased-random-number-within-an-arbitrary-range-using-the-f/20818831#20818831>
> TBD présenter niquist
> TBD quantique, etc.
> TBD ring oscillatro : <https://www.youtube.com/watch?v=fwU8s1BMNlA> <https://www-verimag.imag.fr/~async/CCIS/talk_12/Lubicz_talk.pdf> et <https://pqshield.com/wp-content/uploads/2022/02/2021-1363.pdf>

## Entropie

Cependant créer un nombre aléatoire est un processus coûteux en temps et en énergie. On utilisera alors souvent des processus approchés pour extraire de l'aléatoire : générer $n$ bits presque aléatoires à partir de $m < n$ bits vraiment aléatoires.

> TBD à revoir et à présenter :
>
> 1. <https://www.youtube.com/watch?v=YvH53vJM69E&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=38>
> 2. des preuves : <https://people.seas.harvard.edu/~salil/pseudorandomness/extractors.pdf>




## dans le processeur


> TBD faire le vrai schéma avec l'autocorrélation. 
> dire que cela peut aussi servir à un identifiant si pas d'autocorrelation et qu'on prend des circuit avec une forte variance.

- latch bistable
- pour changer les imperfections on déplace les proba à chaque tirage : on ajoute de l'auto-correlation avec des capacités qui se chargent à gauche ou à droite. pour arriver à 50% de 1 et de 0.
- différence portes <https://pages.hmc.edu/harris/cmosvlsi/4e/lect/lect9.pdf>
- supprimer l'autocorrelation : post-processing :
  - prendre tous les k si corrélation s'atténue avec le temps
  - XOR Decimation (Décimation par XOR) : XOR consecutive bits together (e.g., \(B_{out} = B_n \oplus B_{n-1}\), or across multiple independent latches). If the serial correlation coefficient between adjacent bits is ρ, XORing k bits reduces the correlation exponentially to \(\rho ^{k}\).
  - LFSR or Cryptographic Hashing (LFSR ou hachage) : Feed the raw bitstream into a Linear Feedback Shift Register (LFSR) or a lightweight hash function (like SHA-256 or Toeplitz hashing) to whiten the output and destroy temporal dependencies.
- équiprobabilité :
  - Von Neumann Corrector (Correcteur de Von Neumann) : Read bits in non-overlapping pairs. Discard 00 and 11, output 0 for 01, and output 1 for 10. Note: This removes bias and first-order serial correlation, though it reduces your bit rate by at least 75%.

## La méthode de Lemire

> TBD faire une preuve moins Claudesque.

$L=64$, $X$ uniforme sur $[0,2^L[$, et $r=2^L \bmod n$.

```pseudocode
X ← 64 bits aléatoires
m ← X · n                      # produit sur 128 bits
l ← m mod 2^64                 # partie basse (gratuite)
si l < n:                      # test bon marché, rarement vrai
    t ← (2^64 − n) mod n       # = r : seule division, rarement exécutée
    tant que l < t:
        X ← 64 bits aléatoires
        m ← X · n
        l ← m mod 2^64
renvoyer ⌊m / 2^64⌋            # partie haute (gratuite)
```

### Complexité

- **Probabilité de rejet par tour** : $r/2^L < n/2^L$.
- **Nombre moyen de tours** : $\dfrac{1}{1-r/2^L}\le \dfrac{1}{1-n/2^{64}}$, donc pratiquement 1. Par exemple, pour $n=10^6$, la probabilité de faire un second tour est inférieure à $2^{-44}$.
- **Probabilité de calculer la division** : c'est celle de l'événement $l<n$, qui vaut moins de $n/2^{64}$ par tour.

En espérance, le coût est donc d'environ une multiplication et une comparaison, alors que le modulo coûte une division à chaque fois. Les deux consomment le même nombre de bits aléatoires, 64 par tour.

Pourquoi le caractère non borné ne gêne pas :

- **Le pire cas infini n'arrive jamais en pratique** : la probabilité de faire plus de $t$ tours est inférieure à $(n/2^{64})^t$.
- **Les deux contraintes sont indépendantes** : le théorème oblige un algorithme exact à avoir un pire cas non borné, mais rien n'empêche que son coût moyen soit très faible.

Le modulo n'est rapide que comparé au rejet naïf de la première réponse. Celui-ci tire $k=\lceil\log_2 n\rceil$ bits et rejette avec une probabilité qui peut approcher $1/2$, donc il peut faire jusqu'à 2 tours en moyenne. L'astuce de Lemire est de travailler sur 64 bits, ce qui rend le rejet très rare, et de n'appeler la division que dans ces cas rares.

### Véracité

On montre que, parmi les $2^L$ valeurs possibles de $X$, chaque sortie $h\in\{0,\dots,n-1\}$ est produite par exactement le même nombre de valeurs acceptées. L'uniformité en découle ensuite comme pour le rejet ordinaire.

Notations :
- $N=2^L$, et $X$ uniforme sur $\{0,\dots,N-1\}$.
- On écrit le produit $Xn$ par division euclidienne par $N$ : $Xn = hN + l$ avec $0\le l<N$. Ainsi $h=\lfloor Xn/N\rfloor$ est la partie haute, c'est-à-dire la sortie, et $l=Xn \bmod N$ est la partie basse.
- On écrit aussi $N = qn + r$ avec $q=\lfloor N/n\rfloor$ et $0\le r<n$.

Comme $0\le X<N$, on a $0\le Xn<nN$, donc $h\in\{0,\dots,n-1\}$.

Étape 0 : ce que teste réellement l'algorithme

L'algorithme accepte $X$ si et seulement si $l\ge r$.

Le seuil calculé est $t=(2^L-n)\bmod n$, avec une soustraction faite sur $L$ bits puisque $2^L$ ne tient pas dans un mot. Comme $2^L-n\equiv 2^L \pmod n$, on a $t = N\bmod n = r$.
Le test préliminaire « $l<n$ » n'est qu'un raccourci. Puisque $r<n$, l'inégalité $l<r$ entraîne $l<n$. Si $l\ge n$, on a donc forcément $l\ge r$, et on peut accepter sans calculer $r$.
Étape 1 : chaque sortie a exactement $q$ antécédents acceptés

Lemme. Pour tout réel $a$ et tout entier $q\ge0$, l'intervalle $[a,\,a+qn[$ contient exactement $q$ multiples de $n$.

Preuve. On a $a\le jn<a+qn$ si et seulement si $a/n\le j<a/n+q$. Un intervalle semi-ouvert de longueur $q$ contient exactement $q$ entiers, à savoir $\lceil a/n\rceil,\dots,\lceil a/n\rceil+q-1$. $\square$

Proposition. Pour tout $h\in\{0,\dots,n-1\}$, il y a exactement $q$ valeurs de $X$ acceptées et de sortie $h$.

Preuve. « $X$ accepté et de sortie $h$ » signifie que $Xn=hN+l$ avec $r\le l<N$. Autrement dit,

$$Xn\in[\,hN+r,\;(h+1)N\,[.$$

Cet intervalle a pour longueur $N-r=qn$. Par le lemme, il contient exactement $q$ multiples de $n$, soit $jn$ pour $q$ entiers $j$.

Chacun de ces multiples provient d'une seule valeur admissible de $X$, à savoir $X=j$. En effet, l'intervalle est inclus dans $[0,nN[$, donc $0\le j<N$. Il y a donc exactement $q$ valeurs de $X$ concernées. $\square$

Conséquence. En tout, $nq$ valeurs de $X$ sont acceptées et $N-nq=r$ sont rejetées.

Étape 2 : uniformité de la sortie

Un tour accepte avec probabilité $nq/N$ et rejette avec probabilité $r/N<1$. Les tours sont indépendants. On obtient donc

$$\Pr[\text{sortie}=h]=\sum_{t\ge1}\Big(\frac rN\Big)^{t-1}\frac{q}{N}=\frac{q/N}{1-r/N}=\frac{q}{N-r}=\frac{q}{qn}=\frac1n.\qquad\square$$
Intuition

Sans le rejet, $\lfloor Xn/N\rfloor$ est la méthode biaisée vue plus haut. Chaque intervalle $[hN,(h+1)N[$ contient $q$ ou $q+1$ multiples de $n$, selon les cas.

Le rejet retire les multiples qui tombent dans la tranche initiale $[hN,\,hN+r[$. Cette tranche a une longueur $r<n$, donc elle contient au plus un multiple. On retire ainsi exactement un multiple aux intervalles qui en avaient $q+1$, et aucun aux autres. Tous se retrouvent avec $q$ multiples.

Exemple : $L=2$, donc $N=4$, et $n=3$

On a $4=1\cdot3+1$, donc $q=1$ et $r=1$.

$X$	$Xn$	$h=\lfloor Xn/4\rfloor$	$l=Xn\bmod 4$	$l\ge r=1$ ?
0	0	0	0	rejeté
1	3	0	3	accepté → 0
2	6	1	2	accepté → 1
3	9	2	1	accepté → 2

Chaque sortie a exactement $q=1$ antécédent accepté. Sans le rejet, la sortie 0 aurait eu deux antécédents, $X=0$ et $X=1$ : c'est exactement le biais que le rejet supprime.




retrouver les états internes à partir des sorties pour prédire le nombre suivant.

### générateur cryptographique

perd la propriété de pouvoir tout rejouer à partir de la seed (pour tester des simulations/générer des maps sur des jeux/fare des sauvegardes plus petites)

<https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator>
<https://crypto.stackexchange.com/questions/39186/what-does-it-mean-for-a-random-number-generator-to-be-cryptographically-secure>

<https://www.schutzwerk.com/en/blog/attacking-a-rng/>
<https://crypto.stackexchange.com/questions/100503/is-mersenne-twister-hard-to-break-if-it-has-a-reduced-output>
<https://book-of-gehn.github.io/articles/2018/12/23/Mersenne-Twister-PRNG.html>

<https://en.wikipedia.org/wiki/Fortuna_(PRNG)> et update : <https://fr.wikipedia.org/wiki/Fortuna_(cryptographie)>
