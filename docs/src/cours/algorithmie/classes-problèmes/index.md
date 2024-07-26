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

{% aller %}
[Problèmes de décision](./décideur-décision){.interne}
{% endaller %}

{% aller %}
[Problèmes NP complets](./problèmes-NPC){.interne}
{% endaller %}

> TBD : en parler ?
{% aller %}
[Turing non déterministe](./Turing-non-déterministe){.interne}
{% endaller %}

> TBD isomorphisme de graphe : status inconnu.
> TBD organiser ça sous l'angle de $\leq$ de problèmes
> TBD réduction sac a dos à bi-partition : <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2017KnapSack.pdf>

> TBD <https://www.youtube.com/watch?v=9ONm1od1QZo>