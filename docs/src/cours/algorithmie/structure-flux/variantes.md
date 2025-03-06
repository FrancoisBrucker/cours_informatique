---
layout: layout/post.njk
title: "Variantes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Deux variantes très utilisées, les deques qui combinent pile et file et les listes chaînées qui sont des listes pouvant être infinies.

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

## Listes chaînées

{% lien %}
[Liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

Les listes chaînées sont très utilisés en algorithmie lorsque l'on a uniquement besoin de parcourir une suite d'éléments et que l'on souhaite pouvoir supprimer un élément de cette liste en temps constant.

Pouvoir supprimer un élément en temps constant nécessite de découper la liste en éléments indépendants collés les uns aux autres.

```pseudocode
structure Element:
    attributs:
        valeur: entier
        suivant: Element
        précédent: Element
    création(_valeur: entier, _suivant: Element, _précédent: Element) → Element:
        valeur ← _valeur
        suivant ← _suivant
        précédent ← _précédent
    méthodes:
        méthode ajouter(e: Element) → vide:
            e.suivant ← suivant
            suivant ← e
            e.précédent = self
        méthode supprimer() → vide:
            suivant.précédent ← précédent
            précédent.suivant ← suivant
```

{% info %}
On a utilisé le mot clé self pour parler de l'objet appelant.
{% endinfo %}

> TBD exemple d'utilisation.

Comme on a rien sans rien en algorithmie, permettre de supprimer un élément en temps constant va contraindre le fait que l'on ne peut plus aller à un élément particulier de la liste en temps constant (comme on le fait avec un tableau). On a les complexités :

- création : $\mathcal{O}(1)$
- suppression à une position donnée : $\mathcal{O}(1)$
- ajout à une position donnée : $\mathcal{O}(1)$
- aller à une position $n$ donnée : $\mathcal{O}(n)$

> TBD def récursive pour les langages fonctionnels comme le lisp (rappelez vous la fonction de McCarty) ou encore le haskell.
> TBD listes chaînées sont super aussi pour les algorithmes récursifs car on peut facilement ajouter des choses sans avoir besoin de recréer des objets.
