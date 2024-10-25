---
layout: layout/post.njk 
title: "S6 : Informatique au concours"

eleventyNavigation:
  order: 4

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Petit recueil de ce qui peut/est déjà tombé au concours.

## Algorithmie

- variations et calcul sur 3-SUM
- sac à dos en programmation dynamique
- graphes bi-parti
- algorithme du lièvre et de la tortue pour :
  - détecter des cycles
  - trouver des doublons dans un tableau d'entiers ($n$ entiers dont les valeurs vont de $1$ à $n-1$) en $\mathcal{O}(n)$ opérations et $\mathcal{O}(1)$ en mémoire (cf. <https://medium.com/@simrangarg0501/finding-the-duplicate-number-using-floyds-tortoise-and-hare-algorithm-618ced80e98e>)

## Java

Le java n'est pas enseigné en MPCI, mais est présent au concours, en particulier pour le QCM de GIE.

Sarah a effectué un stage sous ma direction visant à apprendre le java et à donner des liens nécessaires aux MPCI pour qu'ils puissent eux aussi l'apprendre. Consultez son rapport pour vous permettre de bien vous préparer :

{% lien %}
[Rapport de Sarah sur son stage d'apprentissage de Java](Rapport_de_stage_KEGHIAN_2024.pdf)
{% endlien %}
