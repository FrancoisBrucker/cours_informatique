---
layout: layout/post.njk

title: Shell scripting DM

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- [python stdin](https://www.digitalocean.com/community/tutorials/read-stdin-python)
- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

[quel shebang utiliser](https://www.baeldung.com/linux/bash-shebang-lines)
exemple + DM

<https://www.youtube.com/watch?v=8L7cM4q6TL8>

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
https://itslinuxfoss.com/how-parse-json-shell-scripting-linux/