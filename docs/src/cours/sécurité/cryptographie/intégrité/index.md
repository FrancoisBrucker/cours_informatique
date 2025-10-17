---
layout: layout/post.njk

title: Intégrité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour vérifier que c'est bien le message envoyé qui est reçu, il est nécessaire d'ajouter des données au message envoyé. Ces données ajoutées peuvent avoir deux fonctions :

1. soit détecter les erreur de transmissions et tenter de les corriger si elles sont peu nombreuses. Ces ajoute permettent de corriger des erreurs aléatoires dues aux erreurs de transmissions (canal bruité) ou à l'usure (sur un dvd par exemple)
2. soit uniquement vérifier de l'intégrité du message. Ceci permet de détecter a priori toute modification.

La première approche est associée à la discipline du traitement du signal et à donné des algorithmes élégants comme les [codes de hamming](https://www.youtube.com/watch?v=X8jsijhllIA) ou encore les code de [Reed Solomon](https://www.youtube.com/watch?v=1pQJkt7-R4Q). Ces structures sont cependant prédictibles et ne permettent donc pas de protéger de modifications volontaires.

La seconde approche, utilisée en sécurité, consiste à résumer le message envoyé par un hash bien plus petit mais non prédictible.

{% lien %}
[hash et sécurité](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
{% endlien %}

## Pourquoi c'est important

{% lien %}
[Malléabilité](https://fr.wikipedia.org/wiki/Mall%C3%A9abilit%C3%A9_(cryptographie))
{% endlien %}

Si un message chiffré $c$ peut être modifié en un message chiffré $f(c)$ tout en étant encore déchiffrable, on dit que le code est malléable. Les chiffrement par flux utilisant le XOR sont par essence malléable [comme on l'a déjà vu](../chiffre-vernam/#Vernam-intégrité){.interne}, il est donc important de pouvoir se prémunir de ce genre d'attaque.

Enfin, il faut que cette protection soit elle même chiffrée, sans quoi si Mallory peut modifier le message chiffrée $c$ en $f(c)$, il peut très bien également modifier le la protection pour qu'elle corresponde à $f(c)$

## Hash et sécurité

Pour être utilisable en cryptographie, les [fonctions de hash](/cours/algorithmie/structure-dictionnaire/fonctions-hash/) doivent posséder [des propriétés spécifiques](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique).

### Définitions

{% aller %}
[Hash cryptographiques](./hash){.interne}
{% endaller %}

### Exemple

{% aller %}
[SHA](./sha){.interne}
{% endaller %}

## Hash chiffré

{% aller %}
[Message Authentification Code (MAC)](./mac){.interne}
{% endaller %}
{% aller %}
[poly1305](./poly1305){.interne}
{% endaller %}

## AEAD

L'intégrité est actuellement intégré au process de transmission des données :

{% aller %}
[Authenticated Encryption Associated Data](./aead){.interne}
{% endaller %}
