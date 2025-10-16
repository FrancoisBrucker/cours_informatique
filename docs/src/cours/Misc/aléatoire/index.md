---
layout: layout/post.njk

title: Aléatoire

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD <https://en.wikipedia.org/wiki/Entropy_(information_theory)>
> TBD <https://sortingsearching.com/2023/11/25/random.html>


Ca existe :

- [les nombres pseudo-aléatoire de python](https://docs.python.org/fr/3.14/library/random.html). Fonctionnent avec une seed.
- le modulo $x_{n+1} = a \cdot x_n + b \pmod p$ avec $p$ un nombre premier.

Ou encore les décimales de pi à partir de la $k$ème
voir des méthodes plus sophistiquée comme [les lsfr](./Rapport_de_Stage_Laura_Michelutti.pdf).


Ces générateur (python, ou encore le modulo avec un entier premier) sont parfait pour prédire le monde physique, les sorties sont bien uniformes et indétectables de l'aléatoire, mais pour les applications crypto on veut en plus non-prédictible.

Du coup $\pi$ marche pas non plus trop (<https://mathoverflow.net/questions/26942/is-pi-a-good-random-number-generator> et <https://www2.lbl.gov/Science-Articles/Archive/pi-random.html>).

Et les lsfr il faut travailler.

{% lien %}
[Différences entre les différents générateur pseudo-aléatoires](https://fr.eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/stream-ciphers/stream-ciphers-random-numbers-and-the-one-time-pad/examination-review-stream-ciphers-random-numbers-and-the-one-time-pad/what-are-the-key-differences-between-true-random-number-generators-trngs-pseudorandom-number-generators-prngs-and-cryptographically-secure-pseudorandom-number-generators-csprngs/)
{% endlien %}



<!-- > TBD TP
>
> - lsfr avec python etc.
> - les décimales de pi :
>   - <https://www.youtube.com/watch?v=FDXf1XxCXAk>
>   - sont aléatoires si tu ne sais pas que c'est elles.
>   - prendre les bits de la représentation binaire des décimales de pi et leur faire passer des tests d'aléatoire. -->
> 
{% aller %}

[_Truly Random Number Generator_](nombres-aléatoires){.interne}

{% endaller %}

{% aller %}

[_Pseudo Random Number Generator_](nombres-pseudo-aléatoires){.interne}

{% endaller %}
