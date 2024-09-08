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

- la description de chaque instruction et leurs enchaînements soient compréhensible s'il doit être exécuté par u humain
- le code soit syntaxiquement correct s'il est écrit sous la forme d'un programme.

Mais quand est-il de la quatrième condition, celle qui demande que l'algorithme s'arrête après un temps fini quelque soit sont entrée ? On le verra cette question est cruciale et... compliquée. Commençons par définir un algorithme qui ne fini pas forcément :

{% note "**Définition**" %}
On dira qu'un texte respectant les trois premières propriétés de [la définition d'un algorithme](../définition/#règles-générales){.interne} est un ***programme***.
{% endnote %}

C'est pourquoi lorsque l'on vous demande de trouver un algorithme, il faut toujours se poser la question de la terminaison de votre programme.

## Problème de l'arrêt

Savoir si un programme va s'arrêter, ou pas, sur une entrée donnée est un problème compliqué. IL y a bien sur des cas simples, comme celui-ci qui ne s'arrête pas :

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
        dire à voix haute le nombre n
        n = n - 1
```

Mais si on prend le programme suivant qui implémente [la célèbre conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```text
Nom : syracuse
Entrées : 
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 1:
        si n est pair:
            n = n / 2
        sinon:
            n = 3n + 1
    rendre 1
```

On ne sait pas (pas de démonstration) s'il s'arrête quelque soit $n$ ou pas.

{% lien %}

De nombreux travaux ont été fait pour connaître mieux ce problème. Vous pouvez allez jeter un coup d'œil aux liens suivant pour (beaucoup plus d'informations) :

- <https://www.cristal.univ-lille.fr/~jdelahay/SIME/Cours/Syracuse_poly.pdf>
- <https://hal.science/hal-01593181v3/document>

{% endlien %}

{% faire %}
Testez le programme `syracuse`{.language-} pour quelques entrées. Vous verrez que très rapidement $n$ va tendre vers 1.

{% endfaire %}

Le problème de l'arrêt d'un programme est donc une notion qui peut-être compliquée.

Bref, savoir si un programme est un algorithme ne peut se faire qu'en analysant le programme proprement dit. Il n'y a pas de méthode générale pour le faire et c'est ce que nous allons démontrer.

Supposons en effet que l'on puisse automatiser le processus de vérification, il existe alors un algorithme permettant de le faire, nommons le `stop`{.language-} :

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
Une démonstration étant un algorithme (une preuve est finie et s'appuie sur un nombre fini d'axiomes), si une méthode formelle de vérification existe, c'est un algorithme !
{% endinfo %}

On ne donne pas le code de cet algorithme parce que ce n'est pas évident à faire a priori. On ne peut bien sûr pas exécuter l'algorithme en entrée pour savoir s'il s'arrête car s'il ne s'arrête pas, notre algorithme n'en est pas un puisque lui non plus ne s'arrêtera pas. Si `stop`{.language-} existe il doit être plus malin que ça.

Mais arrêtons le suspens tout de suite, [Alan Turing](https://fr.wikipedia.org/wiki/Alan_Turing) lui-même a montré qu'un tel algorithme ne peut exister dans le cadre de ses machine ([le problème de l'arrêt de la machine de Turing](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)) :

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

Le programme `oups`{.language-} est infernal. En effet :

- `oups`{.language-} est programme, il a donc bien un numéro $N$,
- si `oups`{.language-} est un algorithme alors `stop(N)`{.language-} va rendre 1 ce qui fait que `oups`{.language-} ne s'arrêtera pas,
- si `oups`{.language-} n'est pas un algorithme alors `stop(N)`{.language-} va rendre 0 ce qui fait que `oups`{.language-} s'arrêtera.

Bref, `oups`{.language-} ne peut pas exister et donc `stop`{.language-}, notre hypothèse, non plus.

{% enddetails %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (donc en temps fini) qu'auraient tout algorithme. Si on peut montrer qu'un programme s'arrête, il faut faire la preuve pour cet algorithme spécifiquement.

La conclusion de cette partie est pratique :

{% note "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** démontrer qu'ils s'arrêtent. Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un programme s'arrête.
{% endnote %}

## Que calcule un algorithme

{% lien %}
Cette partie est consacrée au [Théorème de Rice](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice)
{% endlien %}

S'il est impossible de savoir si un programme  s'arrête ou pas a priori, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'un algorithme possède une *propriété* donnée, et ce, quelque soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% note "**Définition**" %}
Une ***propriété*** est un ensemble non vide $P$ de programmes.

Un programme $A$ ***vérifie la propriété $P$*** s'il existe un programme $A' \in P$ tel que $A$ et $A'$ coincident pour toute entrée :

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

On en conclut qu'il ne peut exister une machine décidant si un programme vérifie une propriété que si l'algorithme `stop`{.language-} existe, ce qui est impossible.

{% enddetails %}

Ceci signifie que pour toute propriété voulu sur la sortie d'un algorithme il existe une infinité de façon différente de faire. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, et il n'existe pas de preuve générale.

Réciproquement, quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront.

Par exemple : il est indécidable de savoir si un programme calcule $n!$, en revanche il est parfois possible de démonter qu'un programme donné calcule ou pas $n!$.

Il est donc nécessaire :

- de prouver individuellement tout algorithme que l'on conçoit
- de tester personnellement toute fonction que l'on code

Si on sait ce que l'on veut faire, on peut créer des algorithme (exemple des fonctions calculables), mais si on a un programme savoir s'il s'arrête est compliqué et si on a un algorithme savoir ce qu'il fait l'est aussi.

La conclusion de cette partie est pratique :

{% attention "**À retenir**" %}
Lorsque vous créez des algorithmes, il faut **toujours** :

1. expliciter ce que vous pensez qu'il fait
2. démontrer qu'il le fait bien

Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un programme fait ce que l'on pense qu'il fait, et ce quelque soit ce qu'on pense qu'il fait.
{% endattention %}
