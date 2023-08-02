---
layout: layout/post.njk 
title: Arrêt d'une machine de Turing et Théorème de Rice

eleventyNavigation:
    order: 4
    prerequis:
        - "../../../algorithme/définition/"
        
eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La notion d'[algorithme](../../../algorithme/définition/#algorithme) stipule qu'il doit, à partir d'une entrée, rendre un calcul en un temps fini.

Il y a donc deux conditions :

* on doit faire quelque chose
* on doit le faire en temps fini

Ces deux notions ne vont pas de soit. La définition d'une machine de Turing n'implique pas ce qu'elle fait (on ne décrit que les étapes) ni ne garantie qu'elle le fait en temps fini (le [répéteur](../définition/#exemple-répétition), par exemple est une machine qui ne s'arrête jamais).

Nous allons examiner ici ces deux problèmes au cœur de l'informatique.

{% info %}
Comme pseudo-code et machine de Turing sont equivalents, nous écrirons la plupart de nos machines sous la forme de pseudo-code, sans perte de généralité.
{% endinfo %}

On va se poser 2 questions sur un algorithme :

* S'arrête-t-il ?
* Et s'il s'arrête, que fait-il ?

On verra que ces questions sont loin d'être anecdotiques.

## Arrêt de la machine de Turing

Savoir si une machine de Turing va s'arrêter, ou pas, sur une entrée est un problème compliqué. Prenez par exemple l'[algorithme suivant](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) écrit en python :

```python
def syracuse(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
```

L'algorithme est très simple : à partir d'un entier $n$, il le divise par 2 s'il est pair ou le multiplie par 3 et ajoute 1 s'il est impair et recommence tant que ce nombre est strictement plus grand que 1.

{% faire %}
Testez chez vous pour plusieurs nombres, c'est assez bluffant.

Affichez également la suite de nombre ou la représenter graphiquement pour voir l'évolution de votre nombre d'entrée jusqu'à 1.
{% endfaire %}

Personne ne sait (à l'heure où je tape ces caractères) si cet algorithme s'arrête pour tout $n$.

De façon plus générale : si $M$ est une machine de Turing, on ne sait pas a priori si cette machine va s'arrêter.

Formalisons le problème.

Si on a une machine particulière, on peut l'étudier et démontrer qu'elle s'arrête ou pas.

> TBD exemple qui s'arrête et exemple qui s'arrête pas

Mais si on a une machine quelconque, on ne peut pas savoir a priori. On ne peut même pas l'exécuter pour savoir car elle peut s'arrêter *n'importe quand* : dans 1, 100, ou 10^1000 opérations, on en sait rien.

Allons plus loin et supposons qu'il existe une propriété démontrable qu'auraient toutes les machines qui s'arrêtent. Une démonstration étant un algorithme (une preuve est finie et s'appuie sur un nombre fini d'axiomes) et même un pseudo-code (c'est [la correspondance de Curry-Howard](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard)), si une telle propriété existait, il existerait une machine qui pourrait la vérifier :

{% note "**définition**" %}
UNe ***machine d'arrêt*** est une machine de Turing `01#` prenant en paramètre une machine utilisant le même encodage que celui de l'entrée d'une [machine de Turing universelle](./../définitions-alternatives/#MTU).

Cette machine s'arrête pour toute entrée $E$ avec comme sortie :

* 1 si la machine $E$ en entrée s'arrête
* 0 si la machine  $E$  en entrée ne s'arrête pas

{% endnote %}

Turing lui-même a montré qu'une telle machine ne peut exister !

Pour montrer que la machine d'arrêt n'existe pas, Turing a procédé par l'absurde et supposé qu'elle existe. Nommons la `HALT(E)`.

On peut alors fabriquer le pseudo-code d'une autre machine, nommé `CHELOU` :

```text
def CHELOU:
    Si le retour de HALT(CHELOU) vaut 1:
        fait une boucle infinie
    Sinon:
        return 1
```

{% info %}
Par abus de notation, on a associé la machine et sa représentation pour l'appel de `HALT`.
{% endinfo %}

Cette machine est infernale. En effet :

* `HALT(CHELOU)` ne peut valoir 1 car sinon elle ne s'arrête pas
* `HALT(CHELOU)` ne peut valoir 0 car sinon elle s'arrête

Bref, `CHELOU` ne peut exister et donc `HALT` non plus.

{% note "**théorème**" %}
La ***machine d'arrêt*** n'existe pas.
{% endnote %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (en temps fini) qu'auraient toute machine de Turing qui s'arrête. Si on peut montrer qu'une machine s'arrête, il faut faire la preuve pour cette machine spécifiquement.

## <span id="théorème-rice"></span>Théorème de Rice

S'il est impossible de savoir si un algorithme s'arrête ou pas a priori, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'une machine de Turing possède une *propriété* donnée, et ce que quelque soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% note "**définition**" %}
Une ***propriété*** est un ensemble non vide $\mathcal{M}$ de machines de Turing.

Une machine $M$ ***vérifie la propriété $\mathcal{M}$*** s'il existe une machine $M' \in \mathcal{M}$ telle que $M$ et $M'$ coincident pour toute entrée : $M(E) = M'(E)$ si $M(E)$ s'arrête et sinon $M(E)$ et $M'(E)$ ne s'arrêtent pas.

{% endnote %}

Et explicitons le théorème :

{% note "**théorème**" %}
Quelque soit la propriété $\mathcal{M}$, il n'existe pas de machine de Turing $P-\mathcal{M}$ prenant en paramètre une machine utilisant le même encodage que celui de l'entrée d'une [machine de Turing universelle](./../définitions-alternatives/#MTU) et telle que :

Cette machine s'arrête pour toute entrée $E$ avec comme sortie :

* 1 si la machine $E$ en entrée vérifie la propriété $\mathcal{M}$
* 0 si la machine  $E$  en entrée ne vérifie pas la propriété $\mathcal{M}$

{% endnote %}
{% details "preuve" %}
Soit $M0 \in \mathcal{M}$ et $M$ une machine de Turing. On peut alors construire la machine suivante :

```text
def A-M(E):
    M()
    A0(E)
```

L'algorithme `A-M` vérifie la propriété $\mathcal{M}$ si et seulement si la machine de Turing $M$ s'arrête.

On en conclut qu'il ne peut exister une machine décidant si un algorithme vérifie une propriété que s'il existe une machine d'arrêt, ce qui est impossible.

{% enddetails %}

Ceci signifie que pour toute propriété voulu sur la sortie d'une machine, il existe une infinité de façon différente de faire. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, il n'existe pas de preuve générale.

Et réciproquement, quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront.

Par exemple : il est indécidable de savoir si un algorithme calcule $n!$, en revanche il est parfois possible de démonter qu'un algorithme donné calcule ou pas $n!$.

Ceci rend impossible des méthodes automatisées de preuve d'algorithmes. Il est donc nécessaire :

* de prouver individuellement tout algorithme que l'on conçoit
* de tester personnellement toute fonction que l'on code

Il est **impossible** d'automatiser le processus.
