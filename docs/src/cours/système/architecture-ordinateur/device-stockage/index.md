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
> copy on write
> journalisé
> partitions
> gpt ? uuid
> block size
>
> <https://wiki.debian.org/ZFS>
> <https://ext4.wiki.kernel.org/index.php/Ext4_Disk_Layout>