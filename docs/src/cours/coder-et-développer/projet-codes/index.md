---
layout: layout/post.njk

title: "On s'entraîne à coder de petits projets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices pour se mettre le code dans les pattes. Pour chacun des projets vous ferez 2 fichiers :

- le programme principal de nom `main.py`{.language-} qui sera exécuté
- le fichier contenant les différentes fonctions appelées dans le programme principal. Son nom doit être en relation avec son contenu.

Chaque sujet contient son corrigé, mais faites dans l'ordre :

{% faire "**Pour chaque sujet**" %}

1. faites tous les exercices
2. regardez les erreurs courantes et corriger si besoin votre projet
3. comparez votre code au corrigé

{% endfaire %}

## <span id="syracuse"></span>Syracuse

{% exercice %}
[Sujet](./syracuse-sujet){.interne}
{% endexercice %}
{% details "corrigé", "open" %}

1. [Erreurs courantes à éviter](./syracuse-erreurs-courantes){.interne}
2. [Éléments de corrigé](./syracuse-corrigé){.interne}
{% enddetails %}

## <span id="pendu"></span>Jeu du pendu

{% exercice %}
[Sujet](./pendu-sujet){.interne}
{% endexercice %}
{% details "corrigé", "open" %}

1. [Erreurs courantes à éviter](./pendu-erreurs-courantes){.interne}
2. [Éléments de corrigé](./pendu-corrigé){.interne}

{% enddetails %}

## <span id="compte-caractère"></span>Le compte est bon

{% exercice %}
[Sujet](./compte-caractere-sujet){.interne}
{% endexercice %}
{% details "corrigé", "open" %}

1. [Erreurs courantes à éviter](./compte-caractere-erreurs-courantes){.interne}
2. [Éléments de corrigé](./compte-caractere-corrigé){.interne}

{% enddetails %}
