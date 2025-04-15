---
layout: layout/post.njk 
title:  "Problèmes algorithmiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples de problèmes algorithmiques classiques car :

- pouvant être approchés de multiples manières,
- la solution optimale est non triviale et belle.

## Élément majoritaire

{% aller %}

[Élément majoritaire](/enseignements/MPCI/programmation-algorithmes/annales/2023-2024/ds-1/ds1_2023_2024.pdf)

> TBD ajouter le Boyer-Moore

```pseudocode
val <— T[0]
Nb <— 1
for i <— 1 to len(T) - 1 :
   if T[i] == val :
       Nb += 1
   Else :
       Nb -= 1
       if Nb == 0 :
           val <— T[i]
```

{% endaller %}

## Autres problèmes

{% aller %}

- [tri de crêpes (exercice 2)](/enseignements/MPCI/programmation-algorithmes/annales/2021-2022/ds_1_2021_2022.pdf)
- [échanges d'indices (exercice 3)](/enseignements/MPCI/programmation-algorithmes/annales/2021-2022/ds_1_2021_2022.pdf)
- [points fixe](/enseignements/MPCI/programmation-algorithmes/annales/2024-2025/dm-doublons/)
- [palindromes](/enseignements/MPCI/programmation-algorithmes/annales/2023-2024/palindromes/)
{% endaller %}
