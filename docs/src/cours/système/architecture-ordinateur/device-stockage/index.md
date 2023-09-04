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


> TBD : Disques dur, USB
> TBD : Formatage et accès. Tout un tas (FAT, NTFS windows, zfs, btrfs)...
