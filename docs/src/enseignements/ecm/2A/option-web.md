---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "Web front/back"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  key: "Option : Web front et back"
  parent: 2A
  order: 2


---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb("Gestion des sources et site do-it", { includeSelf: true, allowMissing: false  }) -%}
{% if not loop.first %}<span style="padding-left: 0.25rem;padding-right:.25rem">/</span>{% endif %} <a href="{{ page.url | url }}">{{page.title}}</a>
{%- endfor -%}
{% endchemin %}

<!-- début résumé -->

Web front et back (avec node)

<!-- fin résumé -->

## Programme

1. du web
2. du node
