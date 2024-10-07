---
layout: layout/post.njk

title: Fork

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- faire 1 programme avec un fork et il répond moi (si 0) et toi (si 1)
- voir que les fichiers ouverts le sont pour les 2
- faire un pipe entre les 2 fork.

pas de ménoire partagées, ils sont différents

on peut faire un exec pour faire autre chose.

fork est en fait un clone. Il ne copie pas il ne le fait que s'il y a une modification. Ce qui va bien plus vite.