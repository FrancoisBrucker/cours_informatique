---
layout: layout/post.njk

title: Devices de stockage

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- USB SSD même techno
- avant disque à plateau et encore avant à bande.

- DMA 
- irq pour les interruptions. (comment ça marche)

C'est plus lent que la mémoire. Hiérarchie des vitesses.

gestion / accès en page pour être pus rapide. ces bloc physique est plus petite que la séparation logique (qui en est un multiple) :

- 512B pour le bloc physique
- 8 KiB pour le bloc logique

> TBD à vérifier que c'est vrai pour les x-64

uuid pour chaque partition : EFI.

> <https://www.youtube.com/watch?v=Kr8yymG8s3c&list=PL2Yggtk_pK6-R9ehjj0AoTnWrNOLChuld&index=67>
