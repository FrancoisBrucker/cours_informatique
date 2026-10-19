---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12){.externe}
{% endlien %}

Cette partie s'intéresse à la notion de complexités pour un algorithme qui permet de mesurer ses performances.


> TBD : une fois qu'on a un algorithme qui fait ce qu'on veut on essaie de le faire le plus vite possible (en moins d'instruction possible)