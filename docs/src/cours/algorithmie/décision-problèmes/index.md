---
layout: layout/post.njk
title: "Classes de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD mettre [langages et mots](./langages-mots)

On a vu au début de ce cours que certains problèmes [ne pouvaient pas être résolu par un algorithme](../bases-théoriques/calculabilité){.interne} (certains réels ne sont pas calculables, le problème de l'arrêt, etc) : certaines questions resteront sans réponse. De plus, on a vu également que même s'il existe un algorithme pour résoudre un problème mais que si [sa complexité est exponentielle](../complexité-calculs/importance){.interne} le temps de calcul sera rédhibitoire : certaines questions resteront sans réponses en pratique.

Pouvoir séparer les problèmes selon la facilité de leurs résolutions semble une bonne approche. On sait par exemple que le [problème du tri](../problème-tris){.interne} est de complexité $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau d'entiers à trier ou encore que la complexité du [problème de l'exponentiation](../projet-exponentiation){.interne} est en $\mathcal{O}(\ln(n))$ où $n$ est l'exposant. Mais qu'en est-il d'un problème quelconque ? Cela nécessite quelques investigations avant de pouvoir ne serait-ce que poser le problème.

{% aller %}
[NP et machines de Turing non déterministes](./Turing-non-déterministe){.interne}
{% endaller %}

> TBD retravailler la suite pour qu'elle colle avec avant. Turing = décision.
> Du coup les définitions de NP et de co-NP deviennent claires.

{% aller %}
[NP et problèmes de décision](./décideur-décision){.interne}
{% endaller %}

{% aller %}
[Problèmes NP complets](./problèmes-NPC){.interne}
{% endaller %}

{% lien %}

- <https://www2.math.upenn.edu/~wilf/AlgoComp.pdf>
- <https://www.youtube.com/watch?v=s9l6QTX9n0Q&list=PLwF3A0R8OzMpO6_9WbT1kK16akYFh3_Nt>
- <https://www.youtube.com/watch?v=KydXVE9Su5g&list=PLdUzuimxVcC0DENcdT8mfhI3iRRJLVjqH>

{% endlien %}
