---
layout: layout/post.njk

title: "Erreurs courantes : Syracuse"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Après un input vous aurez **toujours** une chaîne de caractère. Il faut la convertir dans ce que va demander vos fonctions, ici des entiers.

Ne faites **PAS** de conversion de type dans vos fonctions. Si elles demandent des entrées entiers supposez que c'est le cas (par de `int(x) % 2` par exemple dans la fonction `syracuse`). Tôt ou tard ce genre chose va vous sauter à la figure car un jour vous votre programme va planter sans que vous compreniez pourquoi ni où est le soucis.
