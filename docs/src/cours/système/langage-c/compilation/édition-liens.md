---
layout: layout/post.njk

title: Édition de liens

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


En ajoutant l'option `-v`, on voit que clang utilise en fait la commande [`ld`](https://linux.die.net/man/1/ld) qui est la commande pour faire l'édition de lien. Passer par `clang` permet d'avoir des options de `ld` positionnées comme :

- des options `-L` pour gérer des chemins
- des bibliothèques partagées incluses avec l'option `-l`

> TBD static avec -static
> ajout de ses propres lib.

- édition de lien, où sont les libs
- statiques vs dynamiques
- utiliser ar pour faire des lib statiques