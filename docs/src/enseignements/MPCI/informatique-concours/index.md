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

## Oraux Concours Commun INP

Pas forcément un concours que vous passez, mais peut valoir le coup de regarder puisqu'il y a aussi des corrigés :

<https://www.concours-commun-inp.fr/fr/epreuves/les-epreuves-orales.html>

## QCM GEI

### Remarques générales

Au fil des années, les QCM changent de format : moins de C et plus de python. Depuis 2024 il y a même du pseudo-code pour les questions algorithmiques.

{% attention "avec le pseudo-code" %}
Ils prennent (en tous cas en 2024) la convention du [Cormen](https://www.amazon.fr/Introduction-%C3%A0-lalgorithmique-Thomas-Cormen/dp/2100031287) en faisant commencer les tableaux à l'indice 1. Méfiez vous !
{% endattention %}

Lisez attentivement chaque question. Il y a de temps en temps des typos, des indentations fantaisistes, des incohérences. Prenez ça comme une feature et non un bug : elles sont là pour voir votre intuition/compréhension informatique. Arriver à comprendre l'esprit de la question, prenez de la hauteur.

{% attention "ne prenez pas la confiance" %}
Ce n'est pas parce que vous ne comprenez pas la question qu'il y a forcément une erreur...
{% endattention %}

### Méthode de résolution

Pour gérer un QCM il y a trois approches qui fonctionnent, par ordre de rapidité :

1. **Connaissance**. Vous reconnaissez l'algorithme, la notion : vous répondez directement la bonne réponse. **Attention** cependant à ne pas aller trop vite, il peut y avoir plusieurs réponses correctes et on est pas à l'abris d'un piège (il y en a...)
2. **Élimination**. On procède par élimination en supprimant itérativement les réponses incorrectes.
3. **Bourrinage**. Pour les questions algorithmiques, déroulez un exemple simple pour voir comment fonctionne l'algorithme et ce qu'il rend.

### Programme

> TBD
