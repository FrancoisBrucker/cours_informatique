---
layout: layout/post.njk
title: "Liste doublement Chaînée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La liste doublement chaînée est très utilisée en algorithmie. Elle permet un traitement plus itératif des listes chaînées en utilisant décomposant la liste en maillons :

```pseudocode
structure Maillon<T>:
    valeur: T ← ∅
    précédent: Maillon<T> ← ∅
    suivant: Maillon<T> ← ∅
```

Chaque maillon contient :

- sa valeur
- le maillon précédent de la chaîne
- le maillon suivant de la chaîne

Une liste doublement chaînée commence par un maillon vide puis on accole les différentes valeurs a la suite :

```pseudocode
(L := Maillon<entier>) ← Maillon<entier>{}

(M := Maillon<entier>) ← Maillon<entier>{valeur: 1}
L.suivant ← M
```

L'exemple précédent crée une liste doublement chaînée à 1 élément.

L'intérêt de ce double lien est que l'pon peut maintenant créer des méthodes qui modifient directement la liste sans avoir besoin de rendre de nouvelles listes :

<span id="structure-liste-chaînée"></span>

```pseudocode
méthode (l Maillon<T>) ajoute(M: Maillon<T>) → ∅:
    l.suivant = M
    M.précédent = l

fonction supprime(M: Maillon<T>) → ∅:
    si M.précédent ≠ ∅:
        M.précédent.suivant ← M.suivant
    M.précédent ← ∅
    M.suivant ← ∅

```

