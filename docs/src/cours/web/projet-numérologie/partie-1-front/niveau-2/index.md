---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 2"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On refait le projet numérologie en ajoutant une partie gestion de projet avec des des todos, une user story, et un balbutiement de tests.

<!-- fin résumé -->

## Plan

1. [préparation du projet](./1-preparation){.interne}
2. [code js](2-code_js){.interne}
3. [code html/css](./3-html_css){.interne}
4. [intégration js et html](./4-integration_html_js){.interne}
5. [projet final](./5-structures){.interne}
