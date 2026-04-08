---
layout: layout/post.njk
title: "Structures de dictionnaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Outre les les listes, la seconde structure dynamique la plus utilisée en code est sans conteste les dictionnaires, aussi appelés tableaux associatifs.

Cette structure est basée sur les fonctions de hash (ou de hachage) qui assure une complexité en moyenne performante.

## Fonctions de hash

{% aller %}
[Fonctions de hachage](fonctions-hash){.interne}
{% endaller %}

## Structure associée : le dictionnaire

La fonction de hachage va permettre de rajouter une indirection au tableau de stockage des données de la structure et créer une structure de données fondamentale :

{% aller %}
[Dictionnaires](dictionnaire){.interne}
{% endaller %}

Cette structure est intensivement utilisé en code, en particulier en python :

{% lien %}
[Dictionnaires python](/cours/coder-et-développer/bases-programmation/conteneurs/#ensembles-dictionnaires){.interne}
{% endlien %}

## Exercice : Structure Ensemble

{% exercice %}
Montrer que l'on peut définir une structure d'ensemble en utilisant les tableaux associatifs.
{% endexercice %}
{% details "corrigé" %}
On a uniquement besoin des clés.

```pseudocode
structure Ensemble<T>:
    T: Dictionnaire<T, booléen>


méthode (e: ensemble<T>) add(x: K) → ∅:
    e.T[x] ← Vrai
méthode (e: ensemble<T>) delete(x: T) → ∅: # supprime x de self = e.delete(x)
    e.T.delete(x)

méthode (e: ensemble<T>) in(x: T) → booléen:  # x est dans self = self.in(x)
    rendre e.T.in(x)

```

{% enddetails %}
{% exercice %}
Implémentez la méthode intersection. Elle devra être de complexité moyenne égale à la taille du plus petit ensemble.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
méthode (e: ensemble<T>)intersection(e': Ensemble<T>) → Ensemble<T>:
    si e.T.longueur > e'.T.longueur:
        a, b ← e', e
    sinon:
        a, b ← e, e'
    c := Ensemble<T> ← Ensemble<T>{}
    pour chaque (x:= T) de a:
        si x est dans b:
            c.add(x)
    rendre c
```

{% enddetails %}

On suppose maintenant que nos données soient des entiers entre 0 et $n$.

{% exercice %}
Explicitez une structure de données permettant de faire mieux que la structure de l'ensemble définie précédemment pour l'ajout la suppression et l'appartenance.

Quelle complexité a-t-elle pour l'intersection ?
{% endexercice %}
{% details "corrigé" %}

Il suffit d'utiliser un tableau de $n + 1$ booléen. Les complexités d'ajout et de suppression sont de complexité (maximale) $\mathcal{O}(1)$.

La complexité de l'intersection est en revanche plus grande, $\mathcal{O}(n)$, puisqu'on ne sait pas a priori si un indice est dans la structure, il faut aller le vérifier dans le tableau.

{% enddetails %}
{% exercice %}
Quand utiliser une structure plutôt que l'autre ?
{% endexercice %}
{% details "corrigé" %}

Si $n$ est pas trop grand ou que l'on ne fait pas beaucoup d'intersection ou que l'on a pas besoin de connaître l'objet d'indice $i$ la seconde structure est plus avantageuse.

Ceci est souvent le cas en algorithmie mais pas en code.

{% enddetails %}

Les ensembles étant une structure extrêmement utilisée, on s'autorisera l'abus de notation suivant :

{% note "**Type Ensemble**" %}
On écrira :

```pseudocode
x := {T}
```

À la place de :

```pseudocode
x := Ensemble<T>
```

On initialisera un ensemble vide ainsi :


```pseudocode
x ← {}
```

{% endnote %}