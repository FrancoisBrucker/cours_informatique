---
layout: layout/post.njk

title: "On s'entraîne à coder de petits projets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> debug : point de journalisation pour vérifier les invariants de boucles.

Quelques exercices pour se mettre le code dans les pattes. Utilisez toutes les bonnes pratiques vues dans le cours et forcez vous à prendre de bonnes habitudes :

{% faire %}

- utilisez des noms de fichiers, de variables et de fonctions signifiants
- utilisez black pour avoir un programme sans warnings du linter.
- **forcez vous** à utiliser le débogueur pour tester vos programmes

{% endfaire %}

Pour chacun des projets vous ferez 3 fichiers :

- le programme principal de nom `main.py`{.language-} qui sera exécuté
- le fichier contenant les différentes fonctions appelées dans le programme principal. Son nom doit être en relation avec son contenu.
- le fichier testant les différentes fonctions (si le fichier contenant les fonctions s'appelle `fonctions.py`{.language-}, le fichier de tests s'appelle `test_fonctions.py`{.language-})

Chaque sujet contient son corrigé, mais faites dans l'ordre :

{% faire "**Pour chaque sujet**" %}

1. faites tous les exercices
2. regardez les erreurs courantes et corriger si besoin votre projet
3. comparez votre code au corrigé

{% endfaire %}

> TBD explicitez l'utilisation du debug dans les sujets.

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

## <span id="compte-caractere"></span>Le compte est bon

{% exercice %}
[Sujet](./compte-caractere-sujet){.interne}
{% endexercice %}
{% details "corrigé", "open" %}

1. [Erreurs courantes à éviter](./compte-caractere-erreurs-courantes){.interne}
2. [Éléments de corrigé](./compte-caractere-corrigé){.interne}

{% enddetails %}

## <span id="polynomes"></span>Somme et produits de polynômes

Uniquement des fonctions à créer.

{% exercice %}
[Sujet](./polynome-sujet){.interne}
{% endexercice %}
{% details "corrigé", "open" %}
[Éléments de corrigé](./syracuse-corrigé){.interne}
{% enddetails %}
