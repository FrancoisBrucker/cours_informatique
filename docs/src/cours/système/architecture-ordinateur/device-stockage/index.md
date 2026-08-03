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

> TBD : en chantier

## Physique

- accès par bloc : 512B pour le bloc physique
- accès 10 ms : disque à plateau / transfert 100MiB/s
- 100 micro s : ssd / transfert 500MiB/s
- USB SSD même techno
- avant disque à plateau et encore avant à bande.
- disque plateau : mécanique. N'existe quasi plus

- SSD : que 10000 écriture possible pour un secteur, il faut répartir la charge. Translation des adresses pour homogénéiser l'écriture.
- DMA  
- irq pour les interruptions. (comment ça marche)

C'est plus lent que la mémoire. Hiérarchie des vitesses.

<https://wiki.archlinux.org/title/Advanced_Format>

## Organisation logique

Un disque dur est organisé en partitions suivant la structure [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table).

{% lien %}
<https://doc.ubuntu-fr.org/uuid_et_label>
{% endlien %}

{% attention %}
Vous verrez encore des vieux tutos parler de MBR, ils sont obsolètes.
{% endattention %}

A chaque partition est associée deux [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) :

- son type
- son [identifiant](https://wiki.archlinux.org/title/Persistent_block_device_naming)

<https://wiki.archlinux.org/title/Partitioning>

### File system

L'organisation en dossier et fichier de votre système d'exploitation est généralement stocké sur une partition du disque.

Le format de cette partition peut varier, voir la partie système d'exploitation.

Il est tout à fait possible de grouper des file system ensemble, par exemple avoir une partition dédié au système et une autre pour les utilisateurs.

### Autres Partitions

Il existe d'autres type de partitions que celles utilisées pour stocker les données ou le système d'exploitation.

#### boot

Partition de démarrage.

<https://en.wikipedia.org/wiki/EFI_system_partition>

#### swap

Le [swap](https://fr.wikipedia.org/wiki/Swap) étend les possibilités de la mémoire virtuelle
