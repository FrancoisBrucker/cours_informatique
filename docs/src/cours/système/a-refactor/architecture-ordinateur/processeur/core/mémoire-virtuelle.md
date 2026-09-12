---
layout: layout/post.njk

title: Mémoire virtuelle

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Adresse logique vs adresse physique

On a vu dans la partie système d'exploitation que la mémoire vue par le process n'est pas celle qui est physiquement présente en RAM. Les adresses mémoires sont séparées en pages et les pages sont réordonnées pour chaque process. La mémoire vue par le process est appelée mémoire logique (ou virtuelle), la mémoire réelle est appelée mémoire physique.

### Adresse et page

Chaque page contient une puissance de 2 adresses contiguës. Si la taille de la page est de 4KiB (valeur courante pour les x64),

On peut séparer une adresse en deux :

- les douze derniers bits qui correspondent à l'adresse dans la page
- les 52 premiers bits qui correspondent à un numéro de page

Remarquez que l'adresse à l'intérieur de la page est la même pour les adresses physiques et logiques.

### Adressage valide

Actuellement, les processeurs x64 ont les spécificités suivantes pour l'adressage.

- adresse sur 48 bit logique : les bits 48 à 63 sont identiques
- adresse sur 52 bit physique : on peut avoir plus de mémoire physique que de mémoire logique, ceci permet d'avoir plusieurs process en même temps en mémoire

Ces limitations sont tout de même très larges :

- un adressage sur $2^{48}$b permet d'adresser 256TiB de données
- un adressage sur $2^{48}$b permet d'adresser 4096TiB de données

A comparer avec les quantités de mémoire actuelles pour des ordinateur puissants :

- 128GiB de RAM
- 20TiB de stockage

## Table de conversion

Pour chaque page virtuelle, il faut lui associer une adresse de page physique. Cette adresse prend $52-12 = 40b$.

On lui adjoint des informations utiles à l'OS comme :

- un dirty bit
- un compteur du ombre de process ayant cette page
- ...

Pour amener à [une entrée sur 64b](https://www.geeksforgeeks.org/page-table-entries-in-page-table/) contenant :

- l'adresse physique de la page (sur 40b)
- 24 bit de contrôle

Il est impossible de maintenir toute cette structure en mémoire car il faudrait $2^40 \cdot 8B = 8 TiB$ de stockage...

### Structure

Comme un process ne va nécessite qu'u petit nombre de page, on utilise une structure arborée permettant, si nécessaire, de tout stocker mais également efficace pour en stocker une partie.

{% note "élément de design" %}

Le stockage par une structure arborée permet :

- de ne stocker que ce qui est nécessaire
- d'être efficace vide (peut de nœud) et plein (on accède à chaque nœud en log du nombre de nœuds)

Cette structure possède un [Overhead](https://en.wikipedia.org/wiki/Overhead_(computing)) faible en temps (en log) et en place (ajout des nœuds en plus des données)
{% endnote %}

La structure est une [structure arborée multi-level](https://en.wikipedia.org/wiki/Page_table#Multilevel_page_tables), elle comporte 4 niveaux en 64b :

- bit 0 à 11 : l'offset dans la page, 4096 possibilités
- bit 12 à 20 : 4ème page, 512 possibilités
- bit 21 à 29 : 3ème page, 512 possibilités
- bit 30 à 39 : 2ème page, 512 possibilités
- bit 40 à 49 : 1ème page, 512 possibilités
- bit 50 à 63 : identiques au bit 48.

Ce qui fait qu'une page sur 64 bit peut s'écrire en 4 nombres plus petit que 512 : ABCD

L'arbre est donc de racine une page de 512 entrée, initialement vide. Si u process contient la page d'adresse ABCD, on :

1. vérifie si la racine possède un enfant à l'entrée A.
   1. si oui on y va
   2. si non on crée une page vide à l'entrée A de la racine et on y va
2. vérifie si la page 2 possède un enfant à l'entrée B.
   1. si oui on y va
   2. si non on crée une page vide à l'entrée B de la page 2 et on y va
3. vérifie si la page 3 possède un enfant à l'entrée C.
   1. si oui on y va
   2. si non on crée une page vide à l'entrée C de la page 3 et on y va
4. vérifie si la page 4 possède un enfant à l'entrée D.
   1. si oui on trouve l'adresse physique
   2. si non lance une exception [page fault](https://fr.wikipedia.org/wiki/Erreur_de_page) pour que le noyau traite ce cas (soit en arrêtant le process soit en associant une page)

Seule les associations nécessaires sont stockées au prix d'un petit [overhead](https://en.wikipedia.org/wiki/Overhead_(computing)) :

- en mémoire : les pages
- en temps : il faut parcourir les 4 pages pour chaque appel

Cette structure est stockée en mémoire et son emplacement est connue de la MMU.

### Buffer dans la MMU

{% lien %}
<https://en.wikipedia.org/wiki/Translation_lookaside_buffer>
{% endlien %}

POur éviter les 4 appels à la mémoire au moindre chargement de page, la MMU possède un cache, la [TLB](https://fr.wikipedia.org/wiki/Translation_lookaside_buffer) qui possède habituellement 16 entrées, assez pour la plupart des process. Le [sunny cove core](https://en.wikichip.org/wiki/intel/microarchitectures/sunny_cove#Architecture) possède ainsi deux TLB, un pour les instructions et un pour les données de 16 entrées chacune.

## Et le cache dans tout ça ?

Le problème de cette transformation est que les caches L1 et L2 sont a priori placés avant la MMU et travaillent donc sur des adresses logiques. Ceci est fâcheux car :

- des adresses logiques différentes peuvent appartenir à la même adresse physique
- en changeant de processus la table change et invalide tous les caches

C'est pourquoi les caches sont en fait stocké avec le tag de l'adresse physique. La taille de page fait que que tag sera identique pour l'adresse logique et physique.

On accélère le processus en faisant un appel à la page (le tag) en même temps que l'on cherche l'index dans le cache.
