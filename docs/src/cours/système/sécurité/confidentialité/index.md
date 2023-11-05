---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


```
         k               k
         |               | 
         v               v
       _____           _____
       | v |           | v |
       |   |           |   |
 m --> | E | --> c --> | D | --> m
       -----           -----
```

Deux types d'attaques :

- brute-force : énumération des clés
- connaissances supplémentaires :
  - *a priori* sur $m$ si l'attaque est chiffre seul
  - acquises si on peut avoir ou produire des couples (message, chiffre)

On considère **en 2024** que si le [nombre de clés est supérieur $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}

## Codes historiques

{% aller %}
[Codes historiques](codes-historiques){.interne}
{% endaller %}

## Qu-est ce que la confidentialité ?

{% aller %}
[Définitions de la confidentialité](définitions){.interne}
{% endaller %}

## Types de code

### Stream

{% aller %}
[chiffrement en flux](chiffre-flux){.interne}
{% endaller %}

### Bloc

{% aller %}
[chiffrement par bloc](chiffre-bloc){.interne}
{% endaller %}

## Partager le secret

Le message ne doit pouvoir être lu que par son destinataire.

{% aller %}
[Partager la clé](partager-secret){.interne}
{% endaller %}

## Générer des clés

- aléatoire
- clé maître
