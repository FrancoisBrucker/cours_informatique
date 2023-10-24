---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Analyse des données
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% aller %}
[Cours analyse des données](/cours/analyse-données)
{% endaller %}
{% attention %}
Les rendus sont à [déposer sur moodle](https://moodle.centrale-marseille.fr/course/view.php?id=1221#section-1)
{% endattention %}
