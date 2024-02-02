---
layout: layout/post.njk

title: Utiliser markdown

eleventyNavigation:
  prerequis:
      - '/tutoriels/format-markdown/'


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Il existe aussi deux plugins intéressants pour écrire ou compiler du markdown avec vscode :

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) qui possède tout le nécessaire pour manipuler de façon agréable le markdown (n'hésitez pas à regarder la documentation, elle est très bien faite).
- [Markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) qui est un analyseur syntaxique pour Markdown (il va souligner en jaune ce qui n'est pas du bon markdown)
