---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent _contenir_ d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](../../principes/opérations#chaines-in){.interne}). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

Parmi ces conteneurs, la **_liste_** est certainement la plus utilisée.

## Listes

{% aller %}
[Listes](listes){.interne}
{% endaller %}

## <span id="ensembles-dictionnaires"></span>Ensembles et dictionnaires

Les deux autres conteneurs à connaître sont les **_ensembles_** et les **_dictionnaires_**. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages.

Les ensembles et les dictionnaires sont tous deux des conteneurs, donc itérables mais contrairement aux listes, leur ordre d'itération est **inconnu**. Il peut changer d'une itération à l'autre.

### Ensembles

{% aller %}
[Ensembles](ensembles){.interne}
{% endaller %}

### Dictionnaires

{% aller %}
[Dictionnaires](dictionnaires){.interne}
{% endaller %}
