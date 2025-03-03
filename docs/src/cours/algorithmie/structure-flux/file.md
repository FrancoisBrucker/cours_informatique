---
layout: layout/post.njk
title: "La file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[La file](https://fr.wikipedia.org/wiki/File_(structure_de_donn%C3%A9es))
{% endlien %}

La **_file_** est la structure de donnée idéale pour gérer un flux de donnée dont on doit conserver l'ordre. On appelle également cette structure **_FIFO_** pour _first in, first out_ : on rend toujours la donnée la plus anciennement stockée. La structure d'une file d'entiers sera alors :

```pseudocode
structure File:
    création(taille: entier) → File
    méthodes:
        méthode empiler(donnée: entier) → vide
        méthode dépiler() → entier
        méthode vide() → booléen
        méthode pleine() → booléen
        méthode nombre() → entier
```

La taille de la file est déterminée à la création et, en plus des méthodes de stockage (`enfiler`{.language-}) ert de rendu (`défiler`{.language-}), possède deux méthodes permettant de savoir si la file est vide ou pleine et une méthode donnant le nombre de données stockées.

{% note "**Utilité de la file**" %}
La file est utilisée comme [un **_buffer_**](https://fr.wikipedia.org/wiki/M%C3%A9moire_tampon) permettant de découpler l'arrivée du traitement de données temporelles.
{% endnote %}

> TBD exemple avec débit d'arrivée et de traitement différents

### Exemple : création des entiers binaires

> TBD <https://meloni.univ-tln.fr/static/cours/algo/7-pilefile.pdf>

### Implémentation

> TBD tableaux.

## Exemple fondamental : le buffer

> TBD fichier, réseau, etc.