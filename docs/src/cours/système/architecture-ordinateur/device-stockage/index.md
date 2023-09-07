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

partition et chaque partition est organisée :

- swap
- fat pour le boot
- données en ntfs, ext4, zfs, ...

ex : uuid


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

<https://medium.com/@boutnaru/linux-what-is-an-inode-7ba47a519940>

<https://tldp.org/LDP/tlk/fs/filesystem.html>
diff entre ext2, 3 et 4 : <https://www.easeus.fr/partition-manager-tips/systeme-de-fichiers-ext2-ext3-ext4.html>