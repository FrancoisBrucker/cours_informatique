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
        méthode enfiler(donnée: entier) → vide
        méthode défiler() → entier
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

```pseudocode
F ← une nouvelle file de chaînes de caractères de taille n / 2
F.enfile("1")
i ← 0
j ← 1
tant que i < n:
    c ← F.défile()
    afficher à l'écran c
    si j < n:               # limite la taille de la pile
        F.enfile(c + "0")
        F.enfile(c + "1")
        j ← j + 2
    i ← i + 1
```

{% exercice %}
Montrer que pour l'algorithme précédent, il faut une file de taille n/2.
{% endexercice %}
{% details "corrigé" %}

Lorsque l'on crée le $n$ème élément que l'on place dans la file, on le crée avec la chaîne de caractères $n_0\dots,n_k$ que l'on vient de sortir de la file.

Le $n$ nombre est alors de la forme $n_0\dots,n_k0$ ou $n_0\dots,n_k1$. Supposons sans perte de généralité que c'est $n_0\dots,n_k0$.

Comme on vient de sortir $n_0\dots,n_k = n/2$ de la file et qu'on y a placé $n_0\dots,n_k0 = n$, il y a bien $n/2$ élément dans la pile.

{% enddetails %}

### Implémentation

```pseudocode
structure File:
    attributs:
        T: [entier]
        longueur: entier
        début: entier
        fin: entier
    création(taille: entier) → Pile:
        T ← un nouveau tableau d'entiers de longueur taille
        longueur ← taille
        début ← longueur - 1
        fin ← 0
    méthodes:
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

On voit facilement que :

{% note "**À retenir**" %}
Les complexités de toutes les méthodes de la structure `File`{.language-} sont en $\mathcal{O}(1)$.

Utiliser une file peut se voire comme une opération élémentaire.
{% endnote %}

> TBD exemple pour montrer que ça marche, avec des bords.

## Exemple fondamental : le buffer

> TBD fichier, réseau, etc.
> TBD calculer la taille avec le débit
