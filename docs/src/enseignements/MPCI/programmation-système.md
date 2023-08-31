---
layout: layout/post.njk 
title: "S5 : [Programmation] Système"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Objectif : Le but de cette UE est d’acquérir les connaissances nécessaires en programmation bas-niveau et système. Cinq volets seront abordés :

- Architecture d'un ordinateur
- Système d'exploitation Linux/Ubuntu
- Programmation bas niveau avec le langage C :
  - langage (type, tableau, `struct`)
  - compilation (bibliothèques, édition de lien, makefile)
  - gestion de la mémoire (pointeurs, `malloc`, pile et tas)
  - structure de données (pile, file, dictionnaire, arbre)
- fichiers exécutables :
  - structure des fichiers elf
  - utilisation d'un débugueur
  - décompilation en assembleur x86
- Communication inter-processus (client/serveur avec socket) et programmation concurrente (thread)

Le but est de vous donner des bases solides sur comment fonctionne un ordinateur et son système d'exploitation. De vous donner le gout d'essayer de comprendre comment tout ça fonctionne pour que vous puissiez approfondir ces notions et maîtriser vos outils de développement.

## Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{DM+ DS + ET}{3}, ET)
$$

Avec :

- $DM$ devoir(s) maison ou exposé(s)
- $DS$ la note du devoir surveillé
- $ET$ est l'examen terminal
