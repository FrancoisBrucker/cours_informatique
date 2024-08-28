---
layout: layout/post.njk
title: "Automates"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



Une classe de langages particulier, décidables, sont très utiles, c'est ceux que l'on peut créer avec un **_automate (fini)_** :

{% note "**Définition**" %}
Un **_automate_** est un décideur admettant comme entrée les mots d'un alphabet $\mathcal{A}$.

Il est défini grace à une **_fonction de transition_** $f: \mathcal{A} \times Q \rightarrow Q$, où $Q$ est un ensemble fini d'**_états_** et deux paramètres :

- $q_0 \in Q$ l'**_état initial_**
- $F \subseteq Q$ les **_états d'acceptation_**

Son algorithme est entièrement défini par eux :

```python
# avec f, q0 et F définis

def automate(m):
    q= q0
    for a in m:
        q = f(a, q)

    return q in F 
```

{% endnote %}

Un automate est une version simplifiée d'une machine de Turing (donc d'un algorithme), il n'y a pas de possibilité de stocker des variables, et sa forme est déterminée exclusivement par sa fonction de transition. On a alors coutume de représenter les automates par un [diagramme](https://fr.wikipedia.org/wiki/Automate_fini_d%C3%A9terministe#Repr%C3%A9sentation_graphique) :

> TBD exemple. avec départ et arrivées.
> TBD cours <https://pageperso.lis-lab.fr/arnaud.labourel/AUTO/cours7.pdf>

Les langages reconnaissables par un automates sont strictement inclus dans les langages décidables :

{% note "**Définition**" %}
Un langage est dit **_rationnel_** s'il existe un automate pour le reconnaître.
{% endnote %}

De nombreux langages sont rationnels :

- constante
- tbd exemples

> tbd rationnels

> tbd pas tout : palindrome marche pas. On est que à un endroit de la chaine alors que palindrome demaine d'être à deux endroit à la fois (début et fin).

> exercices classiques

> c'est une expression régulière.  def, ref et conversion des exercices en expressions

> dire que c'est super utile pour rechercher des motifs dans un texte (numéro de tel, un réel, etc)

> imlémentation d'un moteur d'expression reg compliqué. On va s'intéresser à un cas particulier. retrouver un sous-mot dans une chaine

## Autres Automate

> non déterministe = déterministe. Important car expression reg `.*ab.*` par exemple est très facile à écrire en non déterministe.

> on peu ajouter du stockage automate à pile, mais toujours pas tout.
> expression reg avec des `$1`

> <https://www-igm.univ-mlv.fr/~desar/Cours/automates/ch1.pdf>

> TBD (on appelle cela des [expression régulières](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re))

La formalisation et l'étude des expressions régulières dépassent le cadre de ce cours introductif mais c'est un sujet à la fois marrant, utile et intéressant. Si vous voulez vous initier en douceur, lisez [le tuto python](https://docs.python.org/fr/3/howto/regex.html) qui y est consacré, ou passez directement à [O'reilly](https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/).
