---
layout: layout/post.njk
title: "Variantes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Deques

{% lien %}
<https://en.wikipedia.org/wiki/Double-ended_queue>
{% endlien %}

Une structure qui combine pile et file en une seule structure et avec les mêmes complexités. Cette structure ajoute les méthodes `empiler`{.language-} et `dépiler`{.language-} à la structure de file que l'on a déjà vu :

```pseudocode
structure Deque:
    attributs:
        T: [entier]
        longueur: entier
        début: entier
        fin: entier
    création(taille: entier) → Pile:
        T ← un nouveau tableau d'entiers de taille taille
        longueur ← taille
        début ← longueur - 1
        fin ← 0
    méthodes:
        méthode empiler(donnée: entier) → vide:
            T[suivant] ← donnée
            suivant ← (suivant + 1) % longueur
        méthode dépiler() → entier:
            suivant ← (suivant - 1 + longueur) % longueur
            rendre T[suivant]
        méthode enfiler(donnée: entier) → vide:
            T[fin] ← donnée
            fin ← (fin + 1) % longueur
        méthode défiler() → entier:
            début ← (début + 1) % longueur
            rendre T[début]
        méthode vide() → booléen:
            si nombre() == 0:
                rendre Faux
            rendre Vrai
        méthode pleine() → booléen:
            si (nombre() == longueur):
                rendre Vrai
            rendre Faux
        méthode nombre() → entier:
            rendre (fin - début - 1 + longueur) % longueur
```

{% note "**À retenir**" %}
La structure de Deque permet de combiner pile et file. Souvent c'est cette structure qui est implémentée.

{% endnote %}
{% info %}
En python, c'est [la classe deque](https://docs.python.org/fr/3.13/library/collections.html#collections.deque) du module [collections](https://docs.python.org/fr/3.13/library/collections.html) qui contient une série de classes implémentant des structures de données utiles.

{% endinfo %}
