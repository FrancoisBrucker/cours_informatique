---
layout: layout/post.njk
title: Problème de l'arrêt d'un programme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La notion d'algorithme stipule qu'il doit, à partir d'une entrée, rendre un calcul en un temps fini.

[La définition d'un algorithme](../définition/#définition-règles-générales){.interne} stipule qu'un algorithme doit respecter 4 propriétés. Les 3 premières sont faciles à vérifier, il suffit que :

- la description de chaque instruction et leurs enchaînements soient compréhensible s'il doit être exécuté par un humain
- le code soit syntaxiquement correct s'il est écrit sous la forme d'un programme.

Mais quand est-il de la quatrième condition, celle qui demande que l'algorithme s'arrête après un temps fini quelque soit son entrée ? On verra que cette question est cruciale et... compliquée. Commençons par définir un algorithme qui ne fini pas forcément :

{% note2 "**Définition**" %}
On appelle **_programme_** un texte respectant les trois premières propriétés de [la définition d'un algorithme](../définition/#définition-règles-générales){.interne} :

1. il est constitué d'un **suite fini d'instructions**, chacune décrite avec **un nombre fini de symboles**
2. un humain doit pouvoir suivre chaque étape avec **un papier et un crayon**
3. exécuter une instruction **ne doit pas nécessiter d'intelligence** (à part celle pour comprendre l'instruction)

{% endnote2 %}

C'est pourquoi lorsque l'on vous demande de trouver un algorithme, il faut toujours se poser la question de la terminaison de votre programme.

{% attention %}
On va se placer ici, [sans perte de généralité](../définition/#définition-algorithme-canonique){.interne}, dans le cadre des programmes prenant en paramètre (au plus) un entier et rendant un entier (par défaut `0`).

Un algorithme est alors un programme qui s'arrête pour tout entier passé en paramètre.
{% endattention %}

## Problème de l'arrêt

Savoir si un programme va s'arrêter, ou pas, sur une entrée donnée est un problème compliqué. Il y a bien sur des cas simples, comme celui-ci qui s'arrête : 

```text
Nom : compte à rebours
Entrées :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "Explosion dans"
        dire a voix haute la valeur de n
        dire à voix haute : "secondes"
        attendre 1 seconde
        décrémenter la valeur de n de 1
    dire à voix haute : "BOUM."
```

Ou celui-ci qui ne s'arrête pas :

```text
Nom : vérité
Entrées :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "L'informatique c'est magnifique !"
```


Mais si on prend le programme suivant qui implémente [la célèbre conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```text
Nom : syracuse
Entrées :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 1:
        si n est pair:
            diviser n par 2
        sinon:
            multiplier n par 3 et lui ajouter 1
    rendre 1
```

On ne sait pas (on a pas de démonstration) s'il s'arrête quelque soit $n$ ou pas.

{% lien %}

De nombreux travaux ont été fait pour connaître mieux ce problème. Vous pouvez allez jeter un coup d'œil aux liens suivant pour (beaucoup) plus d'informations :

- <https://www.cristal.univ-lille.fr/~jdelahay/SIME/Cours/Syracuse_poly.pdf>
- <https://hal.science/hal-01593181v3/document>

{% endlien %}

{% faire %}
Testez le programme `syracuse`{.language-} pour quelques entrées. Vous verrez que très rapidement $n$ va être égal à 1.

{% endfaire %}

Le problème de l'arrêt d'un programme est donc une notion qui peut-être compliquée : savoir si un programme est un algorithme ne peut se faire qu'en analysant le programme proprement dit.

{% lien %}
Un algorithme physique de division qui ne s'arrête pas tout le temps :
[Une calculatrice ancienne tente de diviser par zéro](https://www.youtube.com/watch?v=JU9ICaPZUCg)
{% endlien %}

Il n'y a pas de méthode générale pour le faire et c'est ce que nous allons démontrer.

Supposons que l'on puisse automatiser le processus de vérification, il existe alors un algorithme permettant de le faire, nommons le `stop`{.language-}. Il prend en paramètre un entier représentant un programme ([on sait qu'on peut le faire](../définition/#proposition-encodage-algorithme){.interne}):

<div id="algorithme-STOP"></div>

```text
Nom : stop
Entrée :
    n : un entier représentant un programme
Sortie :
    rend 1 si le programme en entrée est un algorithme
    rend 0 sinon
```

Notez que la solution consistant à exécuter le programme en entrée pour voir s'il s'arrête n'est pas une solution valide pas car si ce dernier ne s'arrête pas `stop`{.language-} ne s'arrêtera pas non plus, ce qui est impossible puisque c'est un algorithme. C'est [Alan Turing](https://fr.wikipedia.org/wiki/Alan_Turing) lui-même qui a montré qu'un tel algorithme ne peut exister dans le cadre de ses machines (c'est [le problème de l'arrêt de la machine de Turing](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)) :

{% note "**Théorème**" %}
L'algorithme `stop`{.language-} n'existe pas.
{% endnote %}
{% details "preuve", "open" %}
Supposons que `stop`{.language-} soit un algorithme et construisons le programme suivant :

```text
Nom : oups
Programme :
    si le retour de l'algorithme stop avec comme entrée le numéro de oups vaut 1 (si stop(oups) == 1):
        faire une boucle infinie
    sinon:
        rendre 0
```

Le programme `oups`{.language-} ne peut exister. En effet :

- `oups`{.language-} est programme, il a donc bien un numéro $N$,
- si `oups`{.language-} est un algorithme alors `stop(N)`{.language-} va rendre 1 ce qui fait que `oups`{.language-} ne s'arrêtera pas,
- si `oups`{.language-} n'est pas un algorithme alors `stop(N)`{.language-} va rendre 0 ce qui fait que `oups`{.language-} s'arrêtera.

Si `oups`{.language-} ne peut pas exister, `stop`{.language-} ne le peut pas non plus, ce qui contredit notre hypothèse.

{% enddetails %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (donc en temps fini et donc pouvant être écrite comme un algorithme puisqu'une preuve mathématique est un algorithme et réciproquement) qu'auraient tout les algorithmes et qui les différencieraient des programmes. Si on peut montrer qu'un programme s'arrête, il faut faire la preuve pour ce programme spécifiquement.

{% attention2 "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** démontrer qu'ils s'arrêtent. Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un programme s'arrête.
{% endattention2 %}

## Que calcule un algorithme

{% lien %}
Cette partie est consacrée au [Théorème de Rice](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice)
{% endlien %}

S'il est impossible de savoir a priori si un programme s'arrête ou pas, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'un algorithme possède une _propriété_ donnée, et ce, quelque soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% note2 "**Définition**" %}
Une **_propriété_** $P$ est un sous-ensemble non triviales d'algorithmes :

- il existe au moins un algorithme dans $P$
- il existe au moins un algorithme qui n'est pas dans $P$

Un algorithme $A$ **_satisfait la propriété_** $P$ s'il existe $A'\in P$ tel que $A$ et $A'$ coïncident pour chaque entrée.
{% endnote2 %}

La notion de propriété permet de rendre compte du sens des algorithmes, de ce qu'ils font : les programmes faisant la même chose font partie de la même propriété. 

Par exemples :

- l'ensemble des algorithmes calculant le double d'un entier passé en paramètre est une propriété :
  - il existe des algorithme permettant de le faire (par exemple [cet algorithme](https://fr.wikipedia.org/wiki/Technique_de_l%27addition))
  - il existe des algorithmes qui ne calculent pas le carré de leur entrée
- l'ensemble des algorithmes de valeurs bornées par $K$ est une propriété :
  - l'algorithme constant rendant $K$ satisfait la propriété
  - l'algorithme constant rendant $K+1$ ne satisfait pas la propriété


On va donner un résultat négatif : il n'existe pas d'algorithme permettant de savoir si un programme respecte une propriété donnée. Il faut faire la démonstration pour chaque programme **et** chaque propriété.

<div id="théorème-rice"></div>
{% note "**Théorème (Rice)**" %}
Quelque soit la propriété $P$, l'algorithme suivant n'existe pas :

```text
Nom : propriété-P
Entrée :
    n : un entier représentant un programme
Sortie :
    1 si le programme en entrée vérifie la propriété P
    0 sinon
```

{% endnote %}
{% details "preuve", "open" %}
Soit $A_0 \in P$ et $A$ un programme. On peut alors construire le programme suivant :

```text
Nom : stop-via-P
Entrée :
    n : un entier
Programme :
    A(n)
    rendre A_0(n)
```

Le programme `stop-via-P`{.language-} vérifie la propriété $P$ si et seulement si $A$ est un algorithme (s'il s'arrête). On en conclut que l'algorithme `propriété-P`{.language-} appliqué au numéro de `stop-via-P`{.language-} va rendre 1 si le programme `A` s'arrête et 0 sinon : c'est une autre façon d'écrire le programme `stop`{.language-} !

Comme l'algorithme `stop`{.language-} ne peut pas exister, `propriété-P`{.language-} non plus.

{% enddetails %}

Ceci signifie que pour toute propriété voulu sur la sortie d'un algorithme il existe une infinité de façon différente de faire. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, et il n'existe pas de preuve générale.

Réciproquement, quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront. Il est par exemple impossible de savoir si un programme calcule $n!$, en revanche il est parfois possible de démonter qu'un programme donné cle fait.

Il est donc nécessaire :

- de prouver individuellement tout algorithme que l'on conçoit
- de tester personnellement toute fonction que l'on code

{% attention2 "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** :

1. expliciter ce que vous pensez qu'il fait
2. démontrer qu'il le fait

Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un algorithme fait ce que l'on pense qu'il fait et ce, quelque soit ce qu'on pense qu'il fait.
{% endattention2 %}
