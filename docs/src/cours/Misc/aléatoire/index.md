---
layout: layout/post.njk

title: Aléatoire

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% aller %}

[_Truly Random Number Generator_](nombres-aléatoires){.interne}

{% endaller %}

{% aller %}

[_Pseudo Random Number Generator_](nombres-pseudo-aléatoires){.interne}

{% endaller %}
