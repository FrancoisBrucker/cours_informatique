---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests front"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Tests front.

<!-- fin résumé -->

{% lien %}
<https://www.browserstack.com/guide/front-end-testing>
{% endlien %}

* par comparaison de html : [jsdom](https://github.com/jsdom/jsdom)
* client lourd (selenium, voir ci-après)
* visuellement

<https://www.youtube.com/watch?v=jiEOXOjLfq4>

{% lien %}
<https://github.com/garris/BackstopJS>
{% endlien %}

> TBD : faire un test