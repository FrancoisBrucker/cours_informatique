---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent *contenir* d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](./opérations#chaines-in){.interne}). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

Parmi ces conteneurs, la ***liste*** est certainement la plus utilisée :

{% aller %}
[Listes](listes){.interne}
{% endaller %}

Les deux autres conteneurs à connaître sont les ***ensembles*** et les ***dictionnaires***. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages :

{% aller %}
[Ensembles et dictionnaires](ensembles-dictionnaires)
{% endaller %}
