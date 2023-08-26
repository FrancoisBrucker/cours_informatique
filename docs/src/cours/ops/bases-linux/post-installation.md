---
layout: layout/post.njk

title: Post installation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Que faire après une première installation de Linux/Ubuntu

1. mise à jour des paquets :
   * `sudo apt update && sudo apt upgrade`
   * `sudo snap refresh`
2. 
<https://gist.github.com/bkanhu/827a7c0e250e30fa78109bf7120aeca5>

## sudo

Qu'est-ce que `sudo` et comment l'utiliser.

## apt


## Package à installer

* `man-db`
* `sudo unminimize`