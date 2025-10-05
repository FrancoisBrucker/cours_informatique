---
layout: layout/post.njk

title: Principes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Usage

{% aller %}
[Usages](./usages/){.interne}
{% endaller %}
