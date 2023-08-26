---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Numérologie partie 1 - niveau 1.

<!-- fin résumé -->

On ne verra que le strict nécessaire pour pour faire fonctionner le code :

* utilisation basique d'un éditeur de texte performant, ici [vscode](https://code.visualstudio.com/),
* stricte minimum de html/css pour pouvoir mettre en oeuvre notre serveur web,
* on tentera de s'amuser en javascript sans rentrer trop dans les détails de fonctionnement.

## Plan

1. [préparation du projet](./1-preparation){.interne}
2. [code js](2-code_js){.interne}
3. [code html/css](./3-html_css){.interne}
4. [intégration js et html](./4-integration_html_js){.interne}
5. [projet final](./5-structures){.interne}
