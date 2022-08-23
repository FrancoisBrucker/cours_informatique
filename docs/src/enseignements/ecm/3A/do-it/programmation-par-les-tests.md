---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "Programmation par les tests"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  key: "Programmation par les tests"
  parent: "parcours doit"
  order: 2

---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb("Gestion des sources et site do-it", { includeSelf: true, allowMissing: false  }) -%}
{%- if not loop.first -%}<span style="padding-left: 0.25rem;padding-right:.25rem">/</span>{%- endif -%} <a href="{{ page.url | url }}">{{page.title}}</a>
{%- endfor -%}
{% endchemin %}

> TBD
