---
layout: layout/post.njk
title: "Classes de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On a vu au début de ce cours que certains problèmes [ne pouvaient pas être résolu par un algorithme](../bases-théoriques/calculabilité){.interne} (certains réels ne sont pas calculables, le problème de l'arrêt, etc) : certaines questions resteront sans réponse. De plus, on a vu également que même s'il existe un algorithme pour résoudre un problème mais que si [sa complexité est exponentielle](../complexité-calculs/importance){.interne} le temps de calcul sera rédhibitoire : certaines questions resteront sans réponses en pratique.

Pouvoir séparer les problèmes selon la facilité de leurs résolutions semble une bonne approche. On sait par exemple que le [problème du tri](../problème-tris){.interne} est de complexité $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau d'entiers à trier ou encore que la complexité du [problème de l'exponentiation](../projet-exponentiation){.interne} est en $\mathcal{O}(\ln(n))$ où $n$ est l'exposant. Mais qu'en est-il d'un problème quelconque ? Cela nécessite quelques investigations avant de pouvoir ne serait-ce que poser le problème.

{% aller %}
[Problèmes NP](./problèmes-NP){.interne}
{% endaller %}

> TBD définition de problème, complexité et classes de problèmes.
> TBD : problème de décision, si structure finie on fait tous les cas et hop on a le résultat... Mais en beaucoup de temps

> pb vérifiable ont toujours une solution (une MT qui résout le problème) s'il existe un nombre infini de solutions possible (ie. s'il existe toujours une solution/certificat plus grand).

### Problèmes NPC

> TBD isomorphisme de graphe : status inconnu.
> TBD NPC = universel

## Algorithmes et code binaire

> TBD pour pseudo-code min et théorème de cook.

En remarquant que tout entier peut s'écrire sous sa [notation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire), qui peut être vue comme une suite finie de 0 et de 1 il existe une bijection entre $\mathbb{N}$ et l'ensemble des suite finies de $0$ et de $1$. On en conclut que la forme ultime d'un algorithme est :

{% note %}
Un **_algorithme_** est une fonction de :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies d'éléments de $\\{0, 1\\}$.
{% endnote %}

> TBD : entrée, travail et sorties sont deux listes de 0 et 1.
