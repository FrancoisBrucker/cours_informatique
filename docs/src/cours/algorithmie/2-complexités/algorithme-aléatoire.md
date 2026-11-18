---
layout: layout/post.njk

title: "Algorithmie et aléatoire"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un ordinateur et encore plus un algorithme est forcément déterministe : répéter un algorithme avec les mêmes entrées doit rendre la même sortie. Alors comment expliquer que python fournisse [le module random](https://docs.python.org/fr/3.15/library/random.html) qui génère des nombres aléatoires ([`random.random`{.language-}](https://docs.python.org/fr/3.15/library/random.html#random.random)) ou mélange des tableaux ([`random.shuffle`{.language-}](https://docs.python.org/fr/3.15/library/random.html#random.shuffle)) ?

Il y a deux techniques qu'utilise un ordinateur peut proposer de l'aléatoire :

- il demande de l'aide extérieure,
- il fait semblant.

On va montrer le principe des deux techniques dans ce qui suit. Ce ne sera cependant qu'une introduction le sujet est vaste et peut devenir vite (très) compliqué et contre intuitif. Donc dans le doute :

{% retenir %}
Ne recodez pas vos propres algorithmes pour gérer l'aléatoire : utilisez des bibliothèques ou modules développés par des professionnels.

{% endretenir %}

## Nombres aléatoire et pseudo-aléatoires

{% lien %}
[Différences entre les différents générateur pseudo-aléatoires](https://fr.eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/stream-ciphers/stream-ciphers-random-numbers-and-the-one-time-pad/examination-review-stream-ciphers-random-numbers-and-the-one-time-pad/what-are-the-key-differences-between-true-random-number-generators-trngs-pseudorandom-number-generators-prngs-and-cryptographically-secure-pseudorandom-number-generators-csprngs/){.externe}
{% endlien %}

En informatique, un générateur aléatoire
Il n'est pas nécessaire de pouvoir générer des réels en informatique, seul 1 bit suffit. 

### TRNG : nombres aléatoires

> TBD il suffit de générer soit 0 soit 1 de façon équiprobable puis on généralise aux nombres puis modulo (preuve homogène si génération homogène)

> exemple de la colline et bille au dessus au milieu

> figure fonctionnement porte : 2 états stables mais continue (car physique), donc il existe un autre état instable La moindre perturbation le fait aller d'un côté ou de l'autre.
>
> Schema avec interrupteur pour bloquer.
>
> adaptation au réel : exemple de la colline. et idem pour les interrupteur (dépasse le cadre de ce cours)
> 
> TBD coûteux en temps.

{% lien %}
<https://www.random.org/>{.externe}
{% endlien %}

Et ces méthodes sont implémentées directement [sur le processeur](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#ig_expand=5627&cats=Random){.externe}

### PRNG : Nombres pseudo-aléatoires

"Random numbers should not be generated with a method chosen at random. Some theory
should be used.” (Donald Knuth, 1969)


> TBD qu'en faire ? Prédire le monde physique (uniforme) ou la crypto (non prévisible) ?

> TBD pseudo-aléatoire (modulo et le démontrer) et aléatoire. On suppose qu'on a un truc aléatoire, genre /dev/random sous unix qui prend des paramètre extérieur pour générer de l'entropie.

> fonctionne avec un seed puis une suite
> linéaire : uniforme mais prédictible (même si on ne sort qu'une partie des bits.)

### CSPRNG : Nombres pseudo-aléatoires cryptographiques

> TBD permutations. Pas du tout uniforme. blum-blum sum : non linéaire. Pas utilisé en pratique car lent. On fait du chacha20 plutôt.
> 

## Permutation et Tableaux aléatoires

> Tableau aléatoire parler de fisher-yates et du moyen de trouver des choses aléatoires en informatique. Notion de pseudo-aléatoire et de process physique pour l'aléatoire trouver des ref.

> TBD Fisher-Yates

La complexité en moyenne est également un moyen rapide et simple d'estimer la complexité d'un code. Pour estimer la complexité en moyenne d'un algorithme codé, on mesure le temps pris par l'algorithme pour s'exécuter avec des données aléatoires et on en fait la moyenne (c'est [un estimateur sans biais de la moyenne théorique](<https://fr.wikipedia.org/wiki/Estimateur_(statistique)#Estimateur_de_la_moyenne_de_Y>)).
