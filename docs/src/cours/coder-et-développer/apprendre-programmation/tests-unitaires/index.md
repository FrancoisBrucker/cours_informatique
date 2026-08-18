---
layout: layout/post.njk
title: "Tests Unitaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les tests permettent de vérifier que notre code fonctionne. Ils font partie du programme et on peut s'y référer quand on veut. Lorsque l'on modifie le code, on pourra toujours exécuter **tous les tests** pour vérifier que notre programme fonctionne aussi bien qu'avant. Les tests font partie intégrante du projet : ils garantissent que votre programme fonctionne **maintenant**, et pas seulement au moment où vous avez écrit vos tests.

On y reviendra à de nombreuses reprises :

{% attention2 "**À retenir**" %}
Les tests sont la pierre angulaire d'une bonne programmation : ils garantissent le fonctionnement de votre code et qu'[il ne peut pas régresser](https://blog.octo.com/via-negativa-tdd-et-la-conception-de-logiciel/).
{% endattention2 %}

Les tests sont de petites fonctions dont le but est de _tester_ une fonctionnalité du programme (souvent le résultat de l'exécution d'une fonction). Le test consiste en [une assertion](https://fr.wikipedia.org/wiki/Assertion) que l'on veut être vraie si que le code fonctionne. Si l'assertion est fausse c'est qu'il y a un bug.


## Créer des tests

Commençons par voir comment tester des fonctions.

{% aller %}
[Créer des tests](créer-des-tests){.interne}
{% endaller %}

## Un projet avec ses tests

Maintenant que l'on a vu comment créer des tests, voyons ça dans un projet complet.

{% aller %}
[Un projet avec des tests](projet-avec-des-tests){.interne}
{% endaller %}
