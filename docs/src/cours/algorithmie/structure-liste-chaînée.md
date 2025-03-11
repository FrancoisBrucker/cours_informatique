---
layout: layout/post.njk
title: "Liste Chaînée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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
> TBD reprendre les exo récursif avec une liste. Montrer que ça marche bien.
