---
layout: layout/post.njk
title: Problème de l'arrêt d'un algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La notion d'algorithme stipule qu'il doit, à partir d'une entrée, rendre un calcul en un temps fini.

[La définition d'un algorithme](../définition/#règles-générales){.interne} stipule qu'un algorithme doit respecter 4 propriétés. Les 3 premières sont faciles à vérifier, il suffit que :

- la description de chaque instruction et leurs enchaînements soient compréhensible s'il doit être exécuté par un humain
- le code soit syntaxiquement correct s'il est écrit sous la forme d'un programme.

Mais quand est-il de la quatrième condition, celle qui demande que l'algorithme s'arrête après un temps fini quelque soit son entrée ? On verra que cette question est cruciale et... compliquée. Commençons par définir un algorithme qui ne fini pas forcément :

{% note "**Définition**" %}
On appelle **_programme_** un texte respectant les trois premières propriétés de [la définition d'un algorithme](../définition/#règles-générales){.interne} :

1. il est constitué d'un **suite fini d'instructions**, chacune décrite avec **un nombre fini de symboles**
2. un humain doit pouvoir suivre chaque étape avec **un papier et un crayon**
3. exécuter une instruction **ne doit pas nécessiter d'intelligence** (à part celle pour comprendre l'instruction)

{% endnote %}

C'est pourquoi lorsque l'on vous demande de trouver un algorithme, il faut toujours se poser la question de la terminaison de votre programme.

## Problème de l'arrêt

Savoir si un programme va s'arrêter, ou pas, sur une entrée donnée est un problème compliqué. Il y a bien sur des cas simples, comme celui-ci qui ne s'arrête pas :

```text
Nom : vérité
Entrées :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "L'informatique c'est vraiment super chouette !"
```

Ou celui-ci qui l'est clairement :

```text
Nom : compte à rebours
Entrées :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "L'informatique c'est vraiment super méga chouette !"
        décrémenter la valeur de n de 1
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
Testez le programme `syracuse`{.language-} pour quelques entrées. Vous verrez que très rapidement $n$ va tendre vers 1.

{% endfaire %}

Le problème de l'arrêt d'un programme est donc une notion qui peut-être compliquée : savoir si un programme est un algorithme ne peut se faire qu'en analysant le programme proprement dit.

{% lien %}
Un algorithme physique de division qui ne s'arrête pas tout le temps :
[Une calculatrice ancienne tente de diviser par zéro](https://www.youtube.com/watch?v=JU9ICaPZUCg)
{% endlien %}

Il n'y a pas de méthode générale pour le faire et c'est ce que nous allons démontrer.

Supposons que l'on puisse automatiser le processus de vérification, il existe alors un algorithme permettant de le faire, nommons le `stop`{.language-} :

<div id="algorithme-STOP"></div>

```text
Nom : stop
Entrée :
    n : un entier représentant un programme
Sortie :
    rend 1 si le programme en entrée est un algorithme
    rend 0 sinon
```

On passe en entrée de notre algorithme `stop`{.language-} [un entier encodant un programme](../définition/#encodage-algorithme), comme on l'a déjà fait.

{% info %}
Notez que la solution consistant à exécuter le programme en entrée pour voir s'il s'arrête n'est pas une solution valide pas car si ce dernier ne s'arrête pas `stop`{.language-} ne s'arrêtera pas non plus, ce qui est impossible puisque c'est un algorithme.
{% endinfo %}

C'est [Alan Turing](https://fr.wikipedia.org/wiki/Alan_Turing) lui-même qui a montré qu'un tel algorithme ne peut exister dans le cadre de ses machines (c'est [le problème de l'arrêt de la machine de Turing](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)) :

{% note "**Théorème**" %}
L'algorithme `stop`{.language-} n'existe pas.
{% endnote %}
{% details "preuve", "open" %}
Supposons que `stop`{.language-} soit un algorithme et construisons le programme suivant :

```text
Nom : oups
Programme :
    si le retour de l'algorithme stop avec comme entrée le numéro de oups vaut 1:
        faire une boucle infinie
```

Le programme `oups`{.language-} ne peut exister. En effet :

- `oups`{.language-} est programme, il a donc bien un numéro $N$,
- si `oups`{.language-} est un algorithme alors `stop(N)`{.language-} va rendre 1 ce qui fait que `oups`{.language-} ne s'arrêtera pas,
- si `oups`{.language-} n'est pas un algorithme alors `stop(N)`{.language-} va rendre 0 ce qui fait que `oups`{.language-} s'arrêtera.

Si `oups`{.language-} ne peut pas exister, `stop`{.language-} ne le peut pas non plus, ce qui contredit notre hypothèse.

{% enddetails %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (donc en temps fini) qu'auraient tout les algorithmes et qui les différencieraient des programmes. Si on peut montrer qu'un programme s'arrête, il faut faire la preuve pour cet algorithme spécifiquement.

{% attention "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** démontrer qu'ils s'arrêtent. Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un programme s'arrête.
{% endattention %}

## Que calcule un algorithme

{% lien %}
Cette partie est consacrée au [Théorème de Rice](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice)
{% endlien %}

S'il est impossible de savoir si un programme s'arrête ou pas a priori, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'un algorithme possède une _propriété_ donnée, et ce, quelque soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% note "**Définition**" %}
Une **_propriété_** est un ensemble non vide $P$ de programmes.

Un programme $A$ **_vérifie la propriété $P$_** s'il existe un programme $A' \in P$ tel que $A$ et $A'$ coincident pour toute entrée :

- $A(n)$ ne s'arrête pas si $A'(n)$ ne s'arrête pas,
- $A(n) = A'(n)$ sinon.

{% endnote %}

La notion de propriété permet de rendre compte du sens des programmes, de ce qu'ils font. La encore on va donner un résultat négatif. Il n'existe pas de propriété commune à tous les programmes respectant une propriété, et ce, quelque soit la propriété :

<div id="théorème-rice"></div>
{% note "**Théorème (Rice)**" %}
Quelque soit la propriété $P$, l'algorithme suivant n'existe pas :

```text
Nom : propriété-P
Entrée :
    n : un entier représentant un programme
Sortie :
    1 si l'algorithme en entrée vérifie la propriété P
    0 sinon
```

{% endnote %}
{% details "preuve", "open" %}
Soit $A_0 \in P$ et $A$ un programme. On peut alors construire l'algorithme suivant :

```text
Nom : vérifie-P
Entrée :
    n : un entier
Sortie :
    A(n)
    A_0(n)
```

L'algorithme `vérifie-P`{.language-} vérifie la propriété $P$ si et seulement si $A$ est un algorithme (s'il s'arrête).

On en conclut que l'algorithme `propriété-P`{.language-} appliqué au numéro associé à `vérifie-P`{.language-} va rendre 1 si le programme `A` s'arrête et 0 sinon : c'est `stop`{.language-} !

Comme l'algorithme `stop`{.language-} ne peut pas exister, `propriété-P`{.language-} non plus.

{% enddetails %}

Ceci signifie que pour toute propriété voulu sur la sortie d'un algorithme il existe une infinité de façon différente de faire. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, et il n'existe pas de preuve générale.

Réciproquement, quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront. Il est par exemple impossible de savoir si un programme calcule $n!$, en revanche il est parfois possible de démonter qu'un programme donné calcule ou pas $n!$.

Il est donc nécessaire :

- de prouver individuellement tout algorithme que l'on conçoit
- de tester personnellement toute fonction que l'on code

{% attention "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** :

1. expliciter ce que vous pensez qu'il fait
2. démontrer qu'il le fait

Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un programme fait ce que l'on pense qu'il fait, et ce quelque soit ce qu'on pense qu'il fait.
{% endattention %}
