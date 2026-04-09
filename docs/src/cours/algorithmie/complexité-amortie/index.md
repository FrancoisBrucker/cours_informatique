---
layout: layout/post.njk

title: Analyse et complexité amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'analyse amortie (et la complexité amortie qui en découle) est une technique utilisée pour calculer la complexité lorsque plusieurs exécutions successives d'un même bloc de code va être de complexités différentes.

Par l'exemple lors de l'utilisation de structures complexes où les instructions coûteuses ne sont faites qu'un petit nombre de fois lorsque l'on exécute la méthode plusieurs fois (comme pour [les listes](../structure-liste){.interne} par exemple).

Ce n'est **pas** une complexité en moyenne, c'est un moyen de calculer des complexités (maximum)

{% lien %}
<https://www.youtube.com/watch?v=3MpzavN3Mco>
{% endlien %}

## Définitions

Si lors de l'exécution d'un algorithme $A$, une opération $O$ (ou une fonction) de celui-ci se répète plusieurs fois et que sa
complexité diffère selon les appels, le calcul de la complexité de $A$ va nécessiter une analyse fine de de **toutes** les exécutions de l'opération $O$ car borner la complexité par le maximum conduit (souvent) à surestimer grandement la complexité réelle.

{% note2 "**Définition**" %}
L'**_analyse amortie_** est regroupe un ensemble des techniques permettant de calculer globalement la complexité maximale $C$ de $m$ exécutions successives d'un algorithme.

La **_complexité amortie_** de cet algorithme est alors $\frac{C}{m}$.
{% endnote2 %}
{% attention %}
Il ne faut pas le confondre avec la complexité en moyenne, c'est bien $m$ fois la complexité maximale que l'on considère lorsque l'on effectue les opération successivement.
{% endattention %}

## Méthodes d'analyse amortie

{% aller %}
[Analyse amortie](./analyses){.interne}
{% endaller %}

## Complexité amortie

{% aller %}
[Complexité amortie](./complexité){.interne}
{% endaller %}

## On s'entraîne

{% aller %}
[Projet : calculs de complexités amorties](./projet-complexité-amortie){.interne}
{% endaller %}
