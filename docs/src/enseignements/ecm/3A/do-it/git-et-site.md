---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Gestion des source et site do-it
tags: ['enseignement', 'ECM']

eleventyNavigation:
  key: "Gestion des sources et site do-it"
  parent: "parcours doit"
  order: 1

---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb("Gestion des sources et site do-it", { includeSelf: true, allowMissing: false  }) -%}
{%- if not loop.first -%}<span style="padding-left: 0.25rem;padding-right:.25rem">/</span>{%- endif -%} <a href="{{ page.url | url }}">{{page.title}}</a>
{%- endfor -%}
{% endchemin %}

> TBD
