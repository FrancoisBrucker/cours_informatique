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

[La définition d'un programme](../définition/#définition-règles-générales) stipule qu'il doit respecter 3 propriétés faciles à vérifier, il suffit que :

- la description de chaque instruction et leurs enchaînements soient compréhensibles s'il doit être exécuté par un humain
- le code soit syntaxiquement correct s'il est écrit sous la forme d'un programme.

Mais qu'en est-il de condition de terminaison (le programme s'arrête après un temps fini quelle que soit son entrée) pour définir un algorithme ? Cette question est cruciale et... compliquée. 

{% attention %}
On se placer ici, sans perte de généralité, dans le cadre des programmes prenant un entier en paramètre et rendant un entier (par défaut `0`).
{% endattention %}

## Problème de l'arrêt

Savoir si un programme va s'arrêter, peut-être très simple. Le programme suivant s'arrête tout le temps :

```text
Nom : compte à rebours
Entrée :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "Explosion dans"
        dire à voix haute la valeur de n
        dire à voix haute : "secondes"
        attendre 1 seconde
        décrémenter la valeur de n de 1
    dire à voix haute : "BOUM."
    rendre 0
```

Alors que celui ci ne s'arrête jamais :

<div id="syracuse"></div>

```text
Nom : vérité
Entrée :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "L'informatique c'est magnifique !"
```

Mais si on prend le programme suivant qui implémente [la célèbre conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){.externe}, on ne sait pas vraiment (on n'a pas de démonstration) s'il s'arrête tout le temps :

```text
Nom : syracuse
Entrée :
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 1:
        si n est pair:
            diviser n par 2
        sinon:
            multiplier n par 3 et lui ajouter 1
    rendre 1
```

{% lien %}

De nombreux travaux ont été faits pour mieux comprendre ce problème. Vous pouvez aller jeter un coup d'œil aux liens suivants pour (beaucoup) plus d'informations :

- <https://www.cristal.univ-lille.fr/~jdelahay/SIME/Cours/Syracuse_poly.pdf>{.externe}
- <https://hal.science/hal-01593181v3/document>{.externe}

{% endlien %}

{% faire %}
Testez le programme suivant écrit en python pour quelques entrées. Vous verrez que très rapidement $n$ va être égal à 1.


```python
def syracuse(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    return 1

x = int(input("Tapez un entier (puis entrée) : "))
syracuse(x)

```
{% endfaire %}

Le problème de l'arrêt d'un programme n'est donc pas simple. On ne peut pas le vérifier expérimentalement puisqu'attendre un temps infini avant de conclure n'est pas possible.

{% lien %}
Si vous voulez voir en vrai un programme qui ne s'arrête pas, regardez cette  [calculatrice ancienne tentant de diviser par zéro](https://www.youtube.com/watch?v=JU9ICaPZUCg){.externe}
{% endlien %}

Il n'y a pas de méthode générale pour le faire et c'est ce que nous allons démontrer. Supposons que l'on puisse automatiser le processus de vérification. Il existerait alors un algorithme permettant de le faire, nommons-le `stop`{.language-}. Il prendrait  en paramètre un entier représentant un programme ([on sait qu'on peut le faire](../définition/#proposition-encodage-algorithme)) et rendrait 1 si le programme en paramètre serait un algorithme et 0 sinon :

<div id="algorithme-STOP"></div>

```text
Nom : stop
Entrée :
    n : un entier représentant un programme
Sortie :
    rend 1 si le programme en entrée est un algorithme
    rend 0 sinon
```

Notez que la solution consistant à exécuter le programme en entrée pour voir s'il s'arrête n'est pas une solution valide car si ce dernier ne s'arrête pas `stop`{.language-} ne s'arrêtera pas non plus, ce qui est impossible puisque c'est un algorithme. C'est [Alan Turing](https://fr.wikipedia.org/wiki/Alan_Turing){.externe} lui-même qui a montré qu'un tel algorithme ne peut exister dans le cadre de ses machines (c'est [le problème de l'arrêt de la machine de Turing](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt){.externe}) :

{% note "**Théorème (Turing, 1936)**" %}
L'algorithme `stop`{.language-} n'existe pas.
{% endnote %}
{% details "preuve", "open" %}
Supposons que `stop`{.language-} soit un algorithme et construisons le programme suivant :

```text
Nom : oups
Programme :
    si le retour de l'algorithme stop avec comme entrée le numéro de oups vaut 1 (si stop(oups) == 1):
        répéter:             # c'est une boucle infinie
            ne rien faire 
    sinon:
        rendre 0
```

Le programme `oups`{.language-} ne peut exister puisque :

- `oups`{.language-} est un programme, il a donc un numéro $N$,
- si `oups`{.language-} est un algorithme alors `stop(N)`{.language-} va rendre 1 ce qui fait que `oups`{.language-} ne s'arrêtera pas,
- si `oups`{.language-} n'est pas un algorithme alors `stop(N)`{.language-} va rendre 0 ce qui fait que `oups`{.language-} s'arrêtera.

Si `oups`{.language-} ne peut pas exister, `stop`{.language-} ne le peut pas non plus, ce qui contredit notre hypothèse.

{% enddetails %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (donc en temps fini et donc pouvant être écrite comme un algorithme puisqu'une preuve mathématique est un algorithme et réciproquement) qu'auraient tous les algorithmes et qui les différencieraient des programmes. Si on peut montrer qu'un programme s'arrête, il faut faire la preuve pour ce programme spécifiquement.

{% retenir %}
Lorsque vous créez des algorithmes, il faut **toujours** démontrer qu'ils s'arrêtent. 
{% endretenir %}

## Que calcule un algorithme

{% lien %}
Cette partie est consacrée au [Théorème de Rice](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice){.externe}
{% endlien %}

S'il est impossible de savoir a priori si un programme s'arrête ou pas, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'un algorithme possède une _propriété_ donnée, et ce, quelle que soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% definition %}
Une **_propriété_** $P$ est un sous-ensemble non trivial d'algorithmes, c'est à dire que :

- il existe au moins un algorithme dans $P$
- il existe au moins un algorithme qui n'est pas dans $P$

Un algorithme $A$ **_satisfait la propriété_** $P$ s'il existe $A'\in P$ tel que $A(e) = A'(e)$ pour toute entrée $e$.
{% enddefinition %}

La notion de propriété permet de rendre compte du sens des algorithmes, de ce qu'ils font : les programmes faisant la même chose font partie de la même propriété.  Par exemple :

- l'ensemble des algorithmes calculant le double d'un entier passé en paramètre est une propriété :
  - il existe des algorithmes permettant de le faire (on peut utiliser [l'algorithme de l'addition posée](https://fr.wikipedia.org/wiki/Technique_de_l%27addition){.externe} des cours de primaire en additionnant deux fois le même nombre)
  - il existe des algorithmes qui ne calculent pas le double de leur entrée (on peut utiliser [un de ces algorithme](https://fr.wikipedia.org/wiki/Algorithme_de_multiplication_d%27entiers){.externe} avec 2 et le nombre comme paramètres)
- l'ensemble des algorithmes de valeurs de retour bornées par $K$ est une propriété :
  - l'algorithme constant rendant $K$ satisfait la propriété
  - l'algorithme constant rendant $K+1$ ne satisfait pas la propriété


On va la aussi donner un résultat négatif : il n'existe pas d'algorithme permettant de savoir si un programme respecte une propriété donnée. Il faut faire la démonstration pour chaque programme **et** chaque propriété.

<div id="théorème-rice"></div>
{% note "**Théorème (Rice, 1953)**" %}
Quelle que soit la propriété $P$, l'algorithme suivant n'existe pas :

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

Ceci signifie que pour toute propriété voulue sur la sortie d'un algorithme il faut la vérifier pour toutes les entrées. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, et il n'existe pas de preuve générale.

Réciproquement, quelle que soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront. Il est par exemple impossible de savoir si un programme calcule $n!$, en revanche il est parfois possible de démontrer qu'un programme donné le fait.

Il est donc nécessaire :

- de prouver individuellement tout algorithme que l'on conçoit
- de tester personnellement toute fonction que l'on code

{% retenir %}
Lorsque vous créez des algorithmes, il faut **toujours** :

1. expliciter ce que vous pensez qu'il fait,
2. démontrer qu'il le fait.

Il n'y a pas de condition nécessaire et suffisante qui garantirait qu'un algorithme fait ce que l'on pense qu'il fait et ce, quoi que l'on pense qu'il fasse.
{% endretenir %}
