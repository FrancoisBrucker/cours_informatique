---
layout: layout/post.njk
title: Positionnement

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Positionnement des balises html.

<!-- fin résumé -->

{% lien "**Documentation**" %}

* <https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Positioning>
* <https://www.alsacreations.com/tuto/lire/608-initiation-au-positionnement-css-partie-2.html>

{% endlien %}

fixed, static, relative, absolute (dire que les flottants existent mais qu'on ne les utilisera pas car moins pratique que d'autres choses (comme flex). Peut-être juste parler de l'image dans le texte. Mais mettre des clear).
Utile avec les balise de comportement header, footer, aside, etc.

Parler du :

> TBD :
>
> * positionnement, faire des exemples.
> * z-index
> * overflow
