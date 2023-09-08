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

<https://wiki.osdev.org/Paging>

changement d'adresse. Chaque process doit être organisé de la même manière mais on veut pouvoir avoir plusieurs process en mémoire.

On ajoute une indirection

Chaque process a une table de conversion en mémoire tenue à jour par l'OS. A chaque demande d'adresse, la MMU consulte cette table et rend une nouvelle adresse.

Impossible de faire ça byte à byte : on sépare la mémoire en page. Habituellement de 4KiB = $2^{12}$

On a vu que l'adressage logique ne pouvait dépasser les 48b. L'adressage physique c'est 52b. Il faut donc pouvoir convertir des adresses de $48-12 = 36b$ en adresses de $52-12=40b$. A ceci s'ajoute des méta-data pour savoir si on peut avoir accès à cette page ou pas :

- lecture
- écriture
- exécutable
- user ou kernel
- ...

Par convention on donne 64b pour cette entrée de cette table nommée [Page table](https://en.wikipedia.org/wiki/Page_table).

#### Page table

Si on voulait tout conserver il nous faudrait $2^{36} * 8B = 512GiB$ juste pour la table ! On aurait plus de place pour stocker effectivement les données.

Alors qu'un gros programme qui prend plein de mémoire, disons un chrome qui prend 1GiB=$2^{30}B$ a besoin de $2^{30-12} *8B = 2MiB$.

Il faut trouver un moyen de *pouvoir* tout représenter sans le faire. On utilise une [structure arborée qui découpe les adresses](https://en.wikipedia.org/wiki/X86-64#Page_table_structure).

> TBD un exemple

Remarquez que chaque nœud de l'arbre faire 4KiB, la taille de la page !

Le soucis est que le moindre appel nécessite 4 accès mémoire pour parcourir l'arbre. C'est pourquoi la MMU possède un cache, la [TLB](https://fr.wikipedia.org/wiki/Translation_lookaside_buffer) qui possède habituellement 16 entrées, assez pour la plupart des process. Le [sunny cove core](https://en.wikichip.org/wiki/intel/microarchitectures/sunny_cove#Architecture) possède ainsi deux TLB, un pour les instructions et un pour les données de 16 entrées chacune.

#### Et le cache dans tout ça ?

Le problème de cette transformation est que les caches L1 et L2 sont a priori avant la MMU et travaillent donc sur des adresses logiques. Ceci est fâcheux car :

- des adresses logiques différentes peuvent appartenir à la même adresse physique
- en changeant de processus la table change et invalide tous les caches

C'est pourquoi les caches sont en fait stocké avec le tag de l'adresse physique. La taille de page fait que que tag sera identique pour l'adresse logique et physique.

On accélère le processus en faisant un appel à la page (le tag) en même temps que l'on cherche l'index.
> TBD à faire bien

> <https://stackoverflow.com/questions/4666728/why-is-the-size-of-l1-cache-smaller-than-that-of-the-l2-cache-in-most-of-the-pro/38549736#38549736>
> TBD : <https://stackoverflow.com/questions/19039280/physical-or-virtual-addressing-is-used-in-processors-x86-x86-64-for-caching-in-t> : cache forcément physique car 1 meme adresse peut avoir 2 adresses virtuelles
> <https://stackoverflow.com/questions/32979067/what-will-be-used-for-data-exchange-between-threads-are-executing-on-one-core-wi>
>

Paging et caches : <https://stackoverflow.com/questions/19039280/physical-or-virtual-addressing-is-used-in-processors-x86-x86-64-for-caching-in-t> L1 virtual et L2 physical c'est lui qui est snoopé
