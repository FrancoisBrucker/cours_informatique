---
layout: layout/post.njk

title: Problème du tri

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% prerequis %}

Parties [bases](/cours/coder-et-développer/#bases){.interne} et [développer](/cours/coder-et-développer/#développer){.interne} du [cours de développement](/cours/coder-et-développer){.interne}.

{% endprerequis %}

Étude du problème du tri et implémentation de quelques algorithmes pour *voir* les différentes façon de trier et leurs complexités.

1. [Algorithmes de tri](./algorithmes-tris){.interne}
2. [Implémentation des algorithmes](./implémentation-tris){.interne}
