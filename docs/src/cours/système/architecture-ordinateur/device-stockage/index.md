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

USB SSD même techno
avant disque à plateau et encore avant à bande.

C'est plus lent que la mémoire.

Accès à une adresse particulière. Mais trop lent pur e faire : structure en page.

ex : FAT / ext4


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
>
> <https://blogs.oracle.com/linux/post/understanding-ext4-disk-layout-part-1>
>
> zfs : <https://opensolaris-discuss.opensolaris.narkive.com/86NkhwTm/inode-numbers-on-zfs> ?
