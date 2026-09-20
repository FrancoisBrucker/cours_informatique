---
layout: layout/post.njk

title: Arbres et arborescences couvrants

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


### Algorithme de Chu-Liu/Edmonds

> 朱永津 (Zhū Yǒngjīn) et 刘振宏 (Liú Zhènhóng) en 1965 ; edmonds en 1967
> TBD marche sur l'ensemble des éléments atteignables par r (trouvé via parcours si nécessaire)

{% lien %}
[Algorithme de 朱-刘-Edmonds (Chu-Liu-Edmonds)](https://fr.wikipedia.org/wiki/Algorithme_de_Chu-Liu/Edmonds)
{% endlien %}

> TBD <https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15850-f18/www/scribes/lecture02.pdf>
