---
layout: layout/post.njk

title: Shell scripting

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


exemple + DM

- curl un fichier puis grep dessus
- donner des ressources (yt, man) pour comprendre les outils utilisés
- shebang. Faire avec python.
- diff entre `/usr/bin/python3` et `/usr/bin/env python3`
- on fait du shell scripting
- <https://dev.to/husseinalamutu/bash-vs-python-scripting-a-simple-practical-guide-16in> : manipulation fichier, bash plus utile que python.


1. exos : prendre un yt pour faire des exos
2. shell script

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```
