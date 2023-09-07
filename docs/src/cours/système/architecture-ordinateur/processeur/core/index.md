---
layout: layout/post.njk

title: Core

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Chaque core est une unité de calcul dont le but est d'exécuter des instructions. 


C'est le rôle du système d'exploitation de faire attention à ça, nous n'entrerons donc pas plus dans ces details et considérerons ici qu'un processeur est constitué d'un unique core.

L'architecture du core suit toujours le [modèle de Von Neumann](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann). Par exemple le core [sunny cove](https://en.wikichip.org/wiki/intel/microarchitectures/sunny_cove#Block_diagram) des architectures Ice lake d'intel se schématise encore en :

![core](processeur.png)

Le principe est le suivant :

1. l'instruction a exécuter est lue en mémoire par la [MMU (Memory Management Unit)](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_gestion_de_m%C3%A9moire) sous la forme d'un (ou plusieurs) entiers de 64bit
2. cet entier est passé à l'unité de contrôle qui la décode pour trouver l'instruction à réaliser
3. cette instruction est réalisée par l'unité de calcul dans une de ses sous-unités :
   - l'[ALU](https://fr.wikipedia.org/wiki/Unit%C3%A9_arithm%C3%A9tique_et_logique) pour les opérations logique et arithmétiques sur les entiers
   - la [FPU](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_calcul_en_virgule_flottante) pour les calculs sur les flottants
   - la [VPU](https://en.wikipedia.org/wiki/Vector_processor) pour les opérations vectorielles
4. si besoin, la MMU cherchera une donnée en mémoire pour effectuer l'opération ou enverra en mémoire son résultat.

En tant que tel, un processeur n'a **pas** de mémoire, il ne fait qu'utiliser celle mis à sa disposition par le bus.