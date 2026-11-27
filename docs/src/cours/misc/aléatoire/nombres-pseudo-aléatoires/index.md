---
layout: layout/post.njk

title: Nombres Aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



> TBD cherche à être uniforme
> xorshift


D. Knuth cite dans le volume 2 de [Art of computer programming](https://www.amazon.fr/Art-Computer-Programming-Seminumerical-Combinatorial/dp/0137935102/) près d'une dizaine d'application où l'on a besoin de nombres aléatoires (simulation, échantillonnages, jeu, ...). Cependant, à part l'usage de [générateurs aléatoires physiques](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_al%C3%A9atoires_mat%C3%A9riel) ou encore l'utilisation de [tables](https://fr.wikipedia.org/wiki/Table_de_nombres_al%C3%A9atoires), l'aléatoire semble cependant hors de portée d'un ordinateur, par essence déterministe.

Si un algorithme ne ne peut "créer" de nombres aléatoires, le relancer avec les mêmes paramètres redonnera exactement les mêmes résultats, on peut cependant des nombres ayant _l'air_ d'être aléatoire. Ces nombres sont alors appelés **_nombres pseudo-aléatoires_**.

Il nous faut cependant avant tout définir précisément ce qu'aléatoire veut dire avant de montrer deux méthodes permettant d'en générer.

{% attention %}
En tant qu'informaticien, nous ne nous intéresserons qu'à la génération d'entiers (première partie) voir juste de bits (seconde partie).
{% endattention %}

> TBD dire aléatoire à k=seed fixé. p61 intro modern crypto.


Un suite finie ne peut être considérée aléatoire qu'à l'aune d'un ensemble déterminé de tests qu'elle satisfait. De plus, on veut pouvoir générer des suite avec des algorithmes efficaces (_ie._ polynomiaux). On obtient alors la définition générale suivante :

{% definition %}
Une séquence finie $(x_i)_{0 \leq i < n}$ de $n$ entiers positifs inférieur strictement à $m$ d'entiers est **_[pseudo-aléatoire](https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire)_** si elle :

- est générée par un algorithme polynomial à un paramètre, noté **_graine_** (**_seed_** en anglais)
- elle ne peut être distinguée d'une suite aléatoire via un ensemble de tests statistiques.
{% enddefinition %}
{% info %}
  On laisse à dessein le soin à l'utilisateur de déterminer quels tests doit satisfaire les suites, ils seront différents selon les applications souhaitées.
{% endinfo %}

Nous verrons dans la suite deux exemples d'algorithmes permettant de générer des nombres pseudo-aléatoires et déterminerons les propriétés attendues. Ces propriétés pourront être théoriques ou pratiques.

Chaque générateur pseudo-aléatoire est créé selon des critères particuliers. On va distinguer deux usages principaux des générateurs de nombres aléatoires :

- simulation physique : on s'attachera à l'uniformité des résultats selon de nombreux critères testables. Correspond à la grande majorité des générateurs utilisés
- cryptographie : on s'attachera à rendre non prédictible le résultat. Ce sont des générateurs spécialisés.

N'utilisez pas de générateurs non prévus pour l'usage que vous en ferez : si vous faites de la cryptographie utilisez des générateurs fait pour ça.

### Générateur du système

Le système utilise une méthode mixte pour générer des nombres aléatoires.

Il utilise une méthode purement aléatoire pour générer une graine, heure courante, nombre de fichiers ouverts, température, etc, puis utilise un algorithme pseudo-aléatoire pour générer une séquence de nombres.

{% lien %}
[Générateur de Linux : `/dev/random`{.fichier}](https://en.wikipedia.org/wiki//dev/random)
{% endlien %}

### En shell

> TBD avec apport d'entropie.
> TBD en shell : <https://www.geeksforgeeks.org/linux-unix/random-shell-variable-in-linux-with-examples/>


{% details "sous Linux/mac" %}

{% lien %}
<https://heitorpb.github.io/bla/bash-random-numbers/>
{% endlien %}

Terminal unix :

C'est le pseudo-fichier `/dev/random/`{.fichier} qui crée des nombres aléatoire :

```shell
xxd -b -c1 </dev/random
```

Que l'on peut ensuite transformer en suite de  0 et de 1 :

```shell
xxd -b -c1 </dev/random | cut -d" " -f2 | tr -d "\n"
```

Ou encore en utilisant [le codage base64](https://fr.wikipedia.org/wiki/Base64) pour que ce soit un peut plus  "lisible" :

```shell
echo "hasard : "$(base64 </dev/random 2>/dev/null| head -c 100)
```
{% enddetails %}
{% details "sous Windows" %}
[Avec une commande powershell](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.5) (attention pas cryptographique) :

```shell
powershell -command "[Convert]::ToBase64String((1..64|%{[byte](Get-Random -Max 256)}))"
```
{% enddetails %}

## Générateurs de nombres pseudo-aléatoires

Nous allons voir trois exemples de générateurs de nombres aléatoire et en étudier les propriétés.

### Générer un nombre

On utilise le modulo pour générer une suite de nombres.

{% aller %}
[Modulo comme générateur](modulo)
{% endaller %}s

### Générer un bit

On utilise un registre à décalage pour générer une suite de bits.

{% aller %}
[Registres comme générateur](lfsr)
{% endaller %}

### Générateur de python

> TBD : Mersenne twister


- différence entre
  - aléatoire physique
  - aléatoire cryptographique
- entropie ?

[Registre à décalage](https://fr.wikipedia.org/wiki/Registre_%C3%A0_d%C3%A9calage_%C3%A0_r%C3%A9troaction_lin%C3%A9aire)
